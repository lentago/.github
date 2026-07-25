#!/usr/bin/env bash
# ============================================================================
# fleet-apply.sh — enforce Lentago Labs fleet repo settings that GitHub templates
# and branch rulesets do NOT carry: merge-button options, the topic spine, and
# the per-repo required status checks (required-checks.json).
#
#   ./fleet-apply.sh                 # check ALL non-archived org repos (read-only)
#   ./fleet-apply.sh --apply         # apply merge/topic fixes to ALL repos
#   ./fleet-apply.sh --repo NAME     # scope to one repo
#   ./fleet-apply.sh --apply --repo NAME
#   ./fleet-apply.sh --prune-branches         # delete merged-residue branches fleet-wide
#   ./fleet-apply.sh --prune-branches --repo NAME
#   ./fleet-apply.sh --require-checks         # set required status checks per required-checks.json
#   ./fleet-apply.sh --require-checks --repo NAME
#   ./fleet-apply.sh --apply-labels           # align the issue-label palette per labels.json
#   ./fleet-apply.sh --apply-labels --repo NAME
#
# Read-only by default. Only --apply (settings), --prune-branches (branch
# deletion), --require-checks (ruleset required-check rule) and --apply-labels
# (label color/description) mutate; they are independent flags so each
# destructive action is opt-in. delete_branch_on_merge
# auto-removes a head branch when its PR merges going forward, but it does NOT
# retroactively clean branches whose PR merged before the setting was enabled,
# nor abandoned no-PR branches — the branch scan closes that gap. The base
# branch protection (PR-required, squash-only, no force-push/deletion) is the
# per-repo `main` ruleset created by --apply; the required *status checks* layer
# on top of it is --require-checks (see "Required status checks" below).
#
# Required status checks (lentago/.github#27): the fleet rulesets used to define
# no required checks, so `gh pr merge --auto --squash` could not arm ("clean
# status") and a red plan/lint blocked nothing. required-checks.json maps each
# repo to the EXACT check-run contexts to require. --require-checks applies that
# map, but ONLY after a preflight confirms each context has actually reported on
# a recent PR — requiring a context whose workflow never triggers deadlocks the
# repo (see README § Required status checks and the rollout order there).
#
# Issue labels: labels.json carries the fleet's Tidewater label palette. Every
# repo ships GitHub's stock label colors, which clash with the brand everywhere
# issues and PRs are listed. --apply-labels aligns color + description for the
# labels named there and creates the ones marked ensure=true. Labels absent from
# labels.json are never touched or deleted — per-repo labels stay the repo's own.
# ============================================================================
set -euo pipefail

ORG=lentago
MODE=check
PRUNE=0
REQUIRE=0
LABELS=0
ONLY=""
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
SPINE_TOPICS=(lentago claude)
CHECKS_MAP="$SCRIPT_DIR/required-checks.json"
LABELS_MAP="$SCRIPT_DIR/labels.json"
ACTIONS_APP_ID=15368   # GitHub Actions app — integration_id for required-check contexts
# Sentinel: the copy-pasted review prompt that caused a fleet-wide regression.
# Any repo other than workstation-bootstrap carrying this is mis-customized.
BOILERPLATE='bash bootstrap scripts for Linux workstations'

while [ $# -gt 0 ]; do
  case "$1" in
    --apply) MODE=apply ;;
    --check) MODE=check ;;
    --prune-branches) PRUNE=1 ;;
    --require-checks) REQUIRE=1 ;;
    --apply-labels) LABELS=1 ;;
    --repo)  ONLY="${2:?--repo needs a name}"; shift ;;
    -h|--help) grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
  shift
done

# --- required-status-check helpers (issue #27) ------------------------------

# Current required-check contexts on a repo's `main` branch ruleset (may be empty).
required_contexts() {
  local r="$1" id
  id=$(gh api "repos/$ORG/$r/rulesets" \
        --jq '.[] | select(.target=="branch" and .name=="main") | .id' 2>/dev/null | head -1)
  [ -z "$id" ] && return
  gh api "repos/$ORG/$r/rulesets/$id" \
    --jq '.rules[]? | select(.type=="required_status_checks") | .parameters.required_status_checks[].context' \
    2>/dev/null || true
}

# Check-run names seen across the repo's most recent PR heads — the evidence that a
# context's workflow actually runs. Guards --require-checks against typos and
# premature flips. (Proves the workflow runs, NOT that it is merged to main —
# that ordering is the operator's job per the README.)
#
# Samples several PRs, not just the newest. Sampling only the newest gives a false
# negative whenever the latest PR predates the check being adopted — which is the
# normal case right after a rollout, since the adoption PR is by then one or more
# PRs back. That is exactly when --require-checks is run, so a 1-PR sample refuses
# the very flip it is meant to authorise.
SEEN_PR_SAMPLE=5
seen_contexts() {
  local r="$1" n sha
  while read -r n; do
    [ -z "$n" ] && continue
    sha=$(gh api "repos/$ORG/$r/pulls/$n" --jq '.head.sha' 2>/dev/null) || continue
    [ -z "$sha" ] && continue
    gh api "repos/$ORG/$r/commits/$sha/check-runs" --jq '.check_runs[].name' 2>/dev/null
  done < <(gh pr list --repo "$ORG/$r" --state all --limit "$SEEN_PR_SAMPLE" \
             --json number --jq '.[].number' 2>/dev/null) | sort -u
}

# Layer the mapped required-check contexts onto a repo's `main` ruleset.
require_checks_apply() {
  local r="$1"; shift
  local -a want=("$@")
  local id
  id=$(gh api "repos/$ORG/$r/rulesets" \
        --jq '.[] | select(.target=="branch" and .name=="main") | .id' 2>/dev/null | head -1)
  if [ -z "$id" ]; then
    echo "      ! $r: no main branch ruleset (run --apply first) — skipping required checks"
    return 1
  fi
  local -a seen=() unseen=()
  mapfile -t seen < <(seen_contexts "$r")
  local w
  for w in "${want[@]}"; do
    printf '%s\n' "${seen[@]}" | grep -qxF "$w" || unseen+=("$w")
  done
  if [ ${#unseen[@]} -gt 0 ]; then
    echo "      ! $r: context(s) never seen on a recent PR: [${unseen[*]}]"
    echo "        refusing to require them (would deadlock). Land + run the producing workflow on main first."
    return 1
  fi
  local checks_json body
  checks_json=$(printf '%s\n' "${want[@]}" \
    | jq -R --argjson id "$ACTIONS_APP_ID" '{context: ., integration_id: $id}' | jq -s '.')
  body=$(gh api "repos/$ORG/$r/rulesets/$id" | jq --argjson checks "$checks_json" '
    { name, target, enforcement,
      bypass_actors: (.bypass_actors // []),
      conditions,
      rules: ( [ .rules[] | select(.type != "required_status_checks") ]
               + [ { type: "required_status_checks",
                     parameters: { strict_required_status_checks_policy: false,
                                   do_not_enforce_on_create: false,
                                   required_status_checks: $checks } } ] ) }')
  printf '%s' "$body" | gh api -X PUT "repos/$ORG/$r/rulesets/$id" --input - >/dev/null \
    && echo "      → required checks set on $r: [${want[*]}]"
}

# --- issue-label palette helpers --------------------------------------------

# Align one repo's labels to labels.json. Only labels named there are touched:
# existing ones get color+description, ensure=true ones are created if absent,
# and everything else the repo has is left alone. Never deletes.
labels_apply() {
  local r="$1" name color desc ensure
  local -a have=()
  mapfile -t have < <(gh label list -R "$ORG/$r" --limit 200 --json name --jq '.[].name' 2>/dev/null)
  local changed=0
  while IFS=$'\t' read -r name color desc ensure; do
    if printf '%s\n' "${have[@]}" | grep -qxF "$name"; then
      gh label edit "$name" -R "$ORG/$r" --color "$color" --description "$desc" >/dev/null \
        && changed=$((changed + 1))
    elif [ "$ensure" = "true" ]; then
      gh label create "$name" -R "$ORG/$r" --color "$color" --description "$desc" >/dev/null \
        && changed=$((changed + 1))
    fi
  done < <(jq -r '.labels[] | [.name, .color, .description, (.ensure|tostring)] | @tsv' "$LABELS_MAP")
  echo "      → $r: $changed label(s) aligned"
}

# ----------------------------------------------------------------------------

echo "fleet-apply: mode=$MODE$([ "$PRUNE" = 1 ] && echo ' prune-branches=on')$([ "$REQUIRE" = 1 ] && echo ' require-checks=on')$([ "$LABELS" = 1 ] && echo ' apply-labels=on') org=$ORG ${ONLY:+repo=$ONLY}"
echo

if [ -n "$ONLY" ]; then
  repos="$ONLY"
else
  repos=$(gh repo list "$ORG" --no-archived --limit 100 --json name --jq '.[].name' | sort)
fi

drift_total=0
pruned_total=0
orphan_total=0
checks_missing_total=0

for r in $repos; do
  # --- merge-button settings (also grab default branch for the residue scan) ---
  read -r squash merge rebase auto del private def <<<"$(gh api "repos/$ORG/$r" \
    --jq '"\(.allow_squash_merge) \(.allow_merge_commit) \(.allow_rebase_merge) \(.allow_auto_merge) \(.delete_branch_on_merge) \(.private) \(.default_branch)"')"

  declare -a fixes=()
  [ "$squash" = true ]  || fixes+=(--enable-squash-merge)
  [ "$merge"  = false ] || fixes+=(--enable-merge-commit=false)
  [ "$rebase" = false ] || fixes+=(--enable-rebase-merge=false)
  [ "$del"    = true ]  || fixes+=(--delete-branch-on-merge)
  # Auto-merge isn't available on private repos on the Free plan. Don't nag
  # about an unachievable setting — note it instead of counting it as drift.
  auto_note=""
  if [ "$auto" != true ]; then
    if [ "$private" = true ]; then
      auto_note=" (auto-merge unavailable on private repo — plan limit)"
    else
      fixes+=(--enable-auto-merge)
    fi
  fi

  # --- spine topics ---
  mapfile -t have_topics < <(gh api "repos/$ORG/$r/topics" \
    -H "Accept: application/vnd.github.mercy-preview+json" --jq '.names[]' 2>/dev/null || true)
  declare -a add_topics=()
  for want in "${SPINE_TOPICS[@]}"; do
    printf '%s\n' "${have_topics[@]}" | grep -qxF "$want" || add_topics+=("$want")
  done

  # --- informational: branch ruleset presence ---
  # The rulesets API (like auto-merge) needs Pro for private repos, so a 403
  # here is a plan limit, not a real "no rulesets" answer.
  rs_json=$(gh api "repos/$ORG/$r/rulesets" 2>/dev/null || true)
  ruleset_missing=0
  if printf '%s' "$rs_json" | grep -q 'Upgrade to GitHub Pro\|"status": *"403"'; then
    rs_count="n/a (private/plan)"   # rulesets API needs Pro for private repos
  else
    rs_count=$(printf '%s' "$rs_json" | jq '[.[] | select(.target=="branch")] | length' 2>/dev/null || echo "?")
    [ "$rs_count" = "0" ] && ruleset_missing=1
  fi

  # --- required status checks vs the required-checks.json map (issue #27) ---
  declare -a want_checks=() have_checks=() missing_checks=()
  if [ -f "$CHECKS_MAP" ]; then
    mapfile -t want_checks < <(jq -r --arg r "$r" '.checks[$r][]? // empty' "$CHECKS_MAP" 2>/dev/null)
  fi
  checks_note=""
  if [ ${#want_checks[@]} -gt 0 ] && [ "$ruleset_missing" -eq 0 ] && [ "$rs_count" != "n/a (private/plan)" ]; then
    mapfile -t have_checks < <(required_contexts "$r")
    for w in "${want_checks[@]}"; do
      printf '%s\n' "${have_checks[@]}" | grep -qxF "$w" || missing_checks+=("$w")
    done
    if [ ${#missing_checks[@]} -gt 0 ]; then
      checks_note=" ⧗ req-checks missing=[${missing_checks[*]}]"
      checks_missing_total=$((checks_missing_total+1))
    fi
  fi

  # --- informational: boilerplate review-prompt guard ---
  warn=""
  if [ "$r" != "workstation-bootstrap" ]; then
    body=$(gh api "repos/$ORG/$r/contents/.github/workflows/claude-code-review.yml?ref=HEAD" \
            --jq '.content' 2>/dev/null | base64 -d 2>/dev/null || true)
    case "$body" in
      *"$BOILERPLATE"*) warn=" ⚠ review_prompt still has workstation-bootstrap boilerplate" ;;
    esac
  fi

  # --- leftover branch scan ---
  # delete_branch_on_merge only fires on a merge AFTER it was enabled, and never
  # for branches that were abandoned without a merged PR. Classify each
  # non-default branch by its PR association:
  #   merged PR + no open PR  → residue, safe to prune (content is in main history)
  #   open PR                 → active, leave alone
  #   no PR at all            → orphan, REPORT ONLY (a human must confirm whether
  #                             its commits already landed on main some other way)
  declare -a residue=() orphans=()
  while IFS= read -r b; do
    [ -z "$b" ] && continue
    [ "$b" = "$def" ] && continue
    states=$(gh pr list -R "$ORG/$r" --head "$b" --state all --json state \
               --jq '.[].state' 2>/dev/null || true)
    if printf '%s\n' "$states" | grep -qx OPEN; then
      continue                                   # active PR — hands off
    elif printf '%s\n' "$states" | grep -qx MERGED; then
      residue+=("$b")
    else
      orphans+=("$b")
    fi
  done < <(gh api --paginate "repos/$ORG/$r/branches?per_page=100" --jq '.[].name' 2>/dev/null || true)

  # --- report / apply ---
  if [ ${#fixes[@]} -eq 0 ] && [ ${#add_topics[@]} -eq 0 ] && [ -z "$warn" ] && [ "$ruleset_missing" -eq 0 ] \
     && [ ${#residue[@]} -eq 0 ] && [ ${#orphans[@]} -eq 0 ] && [ ${#missing_checks[@]} -eq 0 ]; then
    printf '  ✓ %-26s settings ok (branch rulesets: %s)%s\n' "$r" "$rs_count" "$auto_note"
  else
    drift_total=$((drift_total+1))
    pruned_total=$((pruned_total + ${#residue[@]}))
    orphan_total=$((orphan_total + ${#orphans[@]}))
    printf '  • %-26s ' "$r"
    [ ${#fixes[@]} -gt 0 ]      && printf 'merge-fixes=[%s] ' "${fixes[*]}"
    [ ${#add_topics[@]} -gt 0 ] && printf 'add-topics=[%s] ' "${add_topics[*]}"
    [ "$ruleset_missing" -eq 1 ] && printf 'no-branch-ruleset '
    [ ${#residue[@]} -gt 0 ]    && printf '%s-residue=[%s] ' "$([ "$PRUNE" = 1 ] && echo pruning || echo merged)" "${residue[*]}"
    [ ${#orphans[@]} -gt 0 ]    && printf 'orphan-branches=[%s] ' "${orphans[*]}"
    [ -n "$warn" ]              && printf '%s' "$warn"
    [ -n "$auto_note" ]        && printf '%s' "$auto_note"
    [ -n "$checks_note" ]      && printf '%s' "$checks_note"
    printf '\n'
    if [ "$MODE" = apply ]; then
      [ ${#fixes[@]} -gt 0 ] && gh repo edit "$ORG/$r" "${fixes[@]}" >/dev/null
      for t in "${add_topics[@]}"; do gh repo edit "$ORG/$r" --add-topic "$t" >/dev/null; done
      if [ "$ruleset_missing" -eq 1 ]; then
        gh api -X POST "repos/$ORG/$r/rulesets" --input "$SCRIPT_DIR/repo-ruleset.json" >/dev/null \
          && echo "      → created main branch ruleset"
      fi
      echo "      → applied (note: review_prompt warnings and required checks are NOT touched by --apply)"
    fi
    if [ "$PRUNE" = 1 ] && [ ${#residue[@]} -gt 0 ]; then
      for b in "${residue[@]}"; do
        gh api -X DELETE "repos/$ORG/$r/git/refs/heads/$b" >/dev/null \
          && echo "      → pruned merged-residue branch: $b"
      done
    fi
    [ ${#orphans[@]} -gt 0 ] && echo "      → orphan branch(es) left for manual review (no PR — verify content landed on main before deleting)"
  fi

  # --require-checks mutates independently of MODE (like --prune-branches).
  # `|| true` is load-bearing under `set -e`: require_checks_apply returns 1 when it
  # refuses a repo (no ruleset, or a context with no evidence it runs). Without this,
  # one refusal aborts the whole sweep and every repo after it — alphabetically — is
  # silently skipped, leaving the fleet half-applied with a zero exit status. The
  # refusal is already reported on stderr by the function itself.
  if [ "$REQUIRE" = 1 ] && [ ${#want_checks[@]} -gt 0 ]; then
    require_checks_apply "$r" "${want_checks[@]}" || true
  fi

  # --apply-labels likewise stands alone: purely cosmetic, no ruleset coupling.
  if [ "$LABELS" = 1 ]; then
    labels_apply "$r"
  fi

  unset fixes add_topics residue orphans want_checks have_checks missing_checks
done

echo
if [ "$PRUNE" = 1 ]; then
  echo "branch prune complete — $pruned_total merged-residue branch(es) deleted; $orphan_total orphan(s) left for manual review."
elif [ "$pruned_total" -gt 0 ] || [ "$orphan_total" -gt 0 ]; then
  echo "branch scan — $pruned_total merged-residue branch(es) prunable (re-run with --prune-branches), $orphan_total orphan(s) need manual review."
fi
if [ "$LABELS" = 1 ]; then
  echo "apply-labels complete — Tidewater palette per fleet-ops/labels.json."
fi
if [ "$REQUIRE" = 1 ]; then
  echo "require-checks complete."
elif [ "$checks_missing_total" -gt 0 ]; then
  echo "required-checks — $checks_missing_total repo(s) missing mapped checks. After each producing workflow is merged to main & observed green on a PR, run: $0 --require-checks"
fi
if [ "$MODE" = check ]; then
  echo "check complete — $drift_total repo(s) with drift. Re-run with --apply to fix merge/topics."
else
  echo "apply complete."
fi
