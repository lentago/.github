#!/usr/bin/env bash
# ============================================================================
# fleet-apply.sh — the Lentago Labs fleet's read-only drift check, its
# required-context preflight, and the merged-branch prune.
#
# Repo settings (merge-button options, the topic spine, rulesets, required
# status checks, labels, repo existence) are owned by terraform/ and change
# through a PR; the terraform apply on merge to main makes them live. This
# script never writes them. Its live-write flags (--apply, --require-checks,
# --allow-check-removal, --apply-labels) were removed in lentago/.github#298 and
# now exit with a pointer to that flow.
#
#   ./fleet-apply.sh                          # check ALL non-archived org repos (read-only)
#   ./fleet-apply.sh --repo NAME              # scope to one repo
#   ./fleet-apply.sh --prune-branches         # also delete merged-residue branches fleet-wide
#   ./fleet-apply.sh --prune-branches --repo NAME
#
# Read-only by default. The one mutation is --prune-branches (branch deletion),
# opt-in so the destructive sweep never runs by accident. delete_branch_on_merge
# auto-removes a head branch when its PR merges going forward, but it does NOT
# retroactively clean branches whose PR merged before the setting was enabled,
# nor abandoned no-PR branches — the branch scan closes that gap.
#
# What the read-only check reports per repo: merge-button and topic-spine drift,
# a missing `main` branch ruleset, required-check drift against
# required-checks.json in both directions, leftover branches, and the
# boilerplate review-prompt sentinel. Settings drift means live has diverged
# from terraform/; the next terraform apply on main corrects it.
#
# Required status checks (lentago/.github#27): required-checks.json maps each
# repo to the EXACT check-run contexts to require, and terraform/rulesets.tf
# applies that map on merge to main. The read-only check preflights every
# context the file adds but live lacks (✗ req-checks never-seen-on-a-PR) —
# requiring a context whose workflow never triggers deadlocks the repo, and
# Terraform cannot tell (see README § Required status checks and the rollout
# order there).
# ============================================================================
set -euo pipefail

ORG=lentago
PRUNE=0
ONLY=""
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
SPINE_TOPICS=(lentago claude)
CHECKS_MAP="$SCRIPT_DIR/required-checks.json"
# Sentinel: the copy-pasted review prompt that caused a fleet-wide regression.
# Any repo other than workstation-bootstrap carrying this is mis-customized.
BOILERPLATE='bash bootstrap scripts for Linux workstations'

while [ $# -gt 0 ]; do
  case "$1" in
    --check) ;;   # the default; still accepted
    --prune-branches) PRUNE=1 ;;
    --apply|--require-checks|--allow-check-removal|--apply-labels)
      echo "fleet-apply: $1 was removed (lentago/.github#298) — repo settings change through terraform/ on a PR; see fleet-ops/README.md" >&2
      exit 2 ;;
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
# context's workflow actually runs. The required-context preflight: guards a
# required-checks.json change against typos and premature flips before terraform/
# requires it. (Proves the workflow runs, NOT that it is merged to main — that
# ordering is the operator's job per the README.)
#
# Samples several PRs, not just the newest. Sampling only the newest gives a false
# negative whenever the latest PR predates the check being adopted — which is the
# normal case right after a rollout, since the adoption PR is by then one or more
# PRs back. That is exactly when the preflight is run, so a 1-PR sample flags the
# very flip it is meant to authorise.
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

# ----------------------------------------------------------------------------

echo "fleet-apply: mode=check$([ "$PRUNE" = 1 ] && echo ' prune-branches=on') org=$ORG ${ONLY:+repo=$ONLY}"
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
checks_extra_total=0

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
  # Diffed both directions: missing = want − live (file wants a check live
  # lacks) is the original check. extra = live − want (live requires a check
  # the file doesn't list) is the reverse — surfaced per lentago/.github#71,
  # since that's the lag the next terraform apply on main would remove.
  declare -a want_checks=() have_checks=() missing_checks=() extra_checks=() seen_checks=() unseen_checks=()
  if [ -f "$CHECKS_MAP" ]; then
    mapfile -t want_checks < <(jq -r --arg r "$r" '.checks[$r][]? // empty' "$CHECKS_MAP" 2>/dev/null)
  fi
  checks_note=""
  if [ -f "$CHECKS_MAP" ] && [ "$ruleset_missing" -eq 0 ] && [ "$rs_count" != "n/a (private/plan)" ]; then
    mapfile -t have_checks < <(required_contexts "$r")
    for w in "${want_checks[@]}"; do
      printf '%s\n' "${have_checks[@]}" | grep -qxF "$w" || missing_checks+=("$w")
    done
    for h in "${have_checks[@]}"; do
      [ -z "$h" ] && continue
      printf '%s\n' "${want_checks[@]}" | grep -qxF "$h" || extra_checks+=("$h")
    done
    if [ ${#missing_checks[@]} -gt 0 ]; then
      checks_note+=" ⧗ req-checks missing=[${missing_checks[*]}]"
      checks_missing_total=$((checks_missing_total+1))
      # Required-context preflight (lentago/.github#293): a missing context that
      # never reported on a recent PR deadlocks the repo once terraform/ requires it.
      mapfile -t seen_checks < <(seen_contexts "$r")
      for w in "${missing_checks[@]}"; do
        printf '%s\n' "${seen_checks[@]}" | grep -qxF "$w" || unseen_checks+=("$w")
      done
      if [ ${#unseen_checks[@]} -gt 0 ]; then
        checks_note+=" ✗ req-checks never-seen-on-a-PR=[${unseen_checks[*]}]"
      fi
    fi
    if [ ${#extra_checks[@]} -gt 0 ]; then
      checks_note+=" ⚠ req-checks live-not-in-file=[${extra_checks[*]}]"
      checks_extra_total=$((checks_extra_total+1))
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

  # --- report (and, with --prune-branches, prune) ---
  if [ ${#fixes[@]} -eq 0 ] && [ ${#add_topics[@]} -eq 0 ] && [ -z "$warn" ] && [ "$ruleset_missing" -eq 0 ] \
     && [ ${#residue[@]} -eq 0 ] && [ ${#orphans[@]} -eq 0 ] && [ ${#missing_checks[@]} -eq 0 ] \
     && [ ${#extra_checks[@]} -eq 0 ]; then
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
    if [ "$PRUNE" = 1 ] && [ ${#residue[@]} -gt 0 ]; then
      for b in "${residue[@]}"; do
        gh api -X DELETE "repos/$ORG/$r/git/refs/heads/$b" >/dev/null \
          && echo "      → pruned merged-residue branch: $b"
      done
    fi
    [ ${#orphans[@]} -gt 0 ] && echo "      → orphan branch(es) left for manual review (no PR — verify content landed on main before deleting)"
  fi

  unset fixes add_topics residue orphans want_checks have_checks missing_checks extra_checks
done

echo
if [ "$PRUNE" = 1 ]; then
  echo "branch prune complete — $pruned_total merged-residue branch(es) deleted; $orphan_total orphan(s) left for manual review."
elif [ "$pruned_total" -gt 0 ] || [ "$orphan_total" -gt 0 ]; then
  echo "branch scan — $pruned_total merged-residue branch(es) prunable (re-run with --prune-branches), $orphan_total orphan(s) need manual review."
fi
if [ "$checks_missing_total" -gt 0 ]; then
  echo "required-checks — $checks_missing_total repo(s) missing mapped checks. terraform/ makes required-checks.json live:" \
       "merge the change through a PR once this read-only preflight shows no '✗ req-checks never-seen-on-a-PR' for it," \
       "and the terraform apply on merge to main requires it (the PR's plan shows the ruleset diff)."
fi
if [ "$checks_extra_total" -gt 0 ]; then
  echo "required-checks — $checks_extra_total repo(s) have live required check(s) not in required-checks.json." \
       "The next terraform apply on main will REMOVE them from the ruleset (a terraform/ PR's plan shows it)." \
       "Add the missing context(s) to required-checks.json, or confirm the removal is intentional."
fi
echo "check complete — $drift_total repo(s) with drift."
if [ "$drift_total" -gt 0 ]; then
  echo "Settings drift (merge-fixes, add-topics, no-branch-ruleset, req-checks) means live has diverged from terraform/:" \
       "the next terraform apply on main corrects it, and that runs only on a merge touching terraform/ or fleet-ops/*.json," \
       "whose plan shows it. Branch residue is --prune-branches; orphan branches need manual review."
fi
