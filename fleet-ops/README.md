# fleet-ops — Lentago Labs repo settings as code

Tooling to keep repo settings consistent across the Lentago Labs fleet. Settings
drift is the thing `~/repos/CLAUDE.md` worries about most, and GitHub splits the
problem across three mechanisms — no single one covers everything:

| Layer | Covers | Mechanism here |
|---|---|---|
| **Branch protection** | PR-required, squash-only, no force-push/deletion | **per-repo rulesets** — created/verified by `fleet-apply.sh` (`repo-ruleset.json`) |
| **Required status checks** | the checks that must be green before merge (so auto-merge can arm and a red plan/lint blocks) | **`fleet-apply.sh --require-checks`** + `required-checks.json` (per-repo context map) |
| **Merge-button + topics** | squash-only button, auto-merge, delete-branch, the `lentago`+`claude` topic spine | **`fleet-apply.sh`** (rulesets can't set these) |
| **Leftover branches** | merged-PR residue + abandoned no-PR branches that `delete_branch_on_merge` never cleaned | **`fleet-apply.sh --prune-branches`** (the setting only fires forward, on merge) |
| **File skeleton** | README/CLAUDE/LICENSE/CI-wrapper starter files | **`lentago/repo-template`** GitHub template (copies files, not settings) |

The lesson that motivated this: a **GitHub template repo copies files, not
settings**, so it can't enforce branch protection or merge options. And a
**ruleset** governs branch rules but not merge-button options or topics. You
need all three layers — and on this org's **Free plan**, branch protection is
per-repo (`fleet-apply.sh` makes that one command), because the cleaner
org-wide ruleset is a paid feature (see below).

## `fleet-apply.sh` — merge settings + topic spine

```bash
./fleet-apply.sh                 # read-only check of all non-archived org repos
./fleet-apply.sh --apply         # apply merge-button + spine-topic fixes fleet-wide
./fleet-apply.sh --prune-branches # delete merged-residue branches fleet-wide
./fleet-apply.sh --repo NAME     # scope to one repo (e.g. a freshly created one)
```

Idempotent. Read-only by default; only `--apply` (settings) and
`--prune-branches` (branch deletion) mutate, and they are **independent flags**
so the destructive branch sweep is always opt-in. It enforces
squash-only + auto-merge + delete-branch-on-merge and the `lentago`+`claude`
topic spine, **creates the per-repo `main` branch ruleset** (`repo-ruleset.json`)
if one is missing, and **warns** if any repo still carries the copy-pasted
`bash bootstrap scripts…` review prompt (the regression fixed in June 2026). It
does not touch signature topics or existing rulesets.

## `--prune-branches` — sweep leftover branches

`delete_branch_on_merge` is enabled fleet-wide, but it only deletes a head
branch when its PR merges *after* the setting was turned on — it never
retroactively cleans branches whose PR merged earlier, and never touches
branches abandoned without a merged PR. That residue accumulates. The scan
classifies every non-default branch by its PR association and acts accordingly:

| Class | Signal | Action |
|---|---|---|
| **merged-residue** | a **merged** PR for the branch, no open PR | pruned by `--prune-branches` (its commits are in `main`'s history) |
| **active** | an **open** PR | left alone |
| **orphan** | **no PR at all** | **reported only, never auto-deleted** — a human must confirm the commits already landed on `main` some other way before removing it |

The read-only check lists both prunable residue and orphans; `--prune-branches`
deletes the residue and still only *reports* orphans. Squash-merge-safe: it keys
off PR merge state, not commit ancestry, so a squashed branch (which always looks
"ahead" of `main`) is still correctly seen as merged.

Bootstrapping a freshly created repo is therefore one command:

```bash
./fleet-apply.sh --apply --repo <new-repo-name>
```

## `repo-ruleset.json` — the per-repo branch ruleset

The minimal branch ruleset applied to each repo's default branch: PR-required
(0 approvals), squash-only merge, no force-push, no branch deletion. The
required *status checks* layer on top of this base ruleset is the
`required_status_checks` rule managed separately by `--require-checks` (next
section) — it edits this same `main` ruleset in place rather than adding a
second one.

## `required-checks.json` + `--require-checks` — required status checks

The base ruleset gates on "a PR must exist," but with **no required status
checks** GitHub treats a green PR as `clean` — and it refuses to *arm*
auto-merge on a clean PR (`Pull request is in clean status`). So
`gh pr merge --auto --squash`, the fleet's merge convention, could not arm, and
a red terraform plan / lint blocked nothing. On the enforced-surface repos where
**merge == deploy**, that meant CI was decoration. (Origin: lentago/.github#27.)

`required-checks.json` maps each repo to the **exact** check-run contexts to
require:

```jsonc
"checks": {
  "kalmia":  ["gate", "ansible-lint", "shellcheck / shellcheck"],
  "drosera": ["gate", "shellcheck / shellcheck"],
  "solidago":["gate"],
  "site-lentago-dev": ["Build"],
  "claytonia":["shellcheck / shellcheck"]
}
```

The read-only check reports the gap (`⧗ req-checks missing=[…]`); `--require-checks`
applies it by editing each repo's `main` ruleset's `required_status_checks` rule
(`integration_id` 15368 = GitHub Actions):

```bash
./fleet-apply.sh --require-checks              # fleet-wide
./fleet-apply.sh --require-checks --repo NAME  # one repo
```

Two rules make this safe rather than a fleet-wide foot-gun:

1. **Contexts are the exact check-run names, captured from live PR check runs —
   not workflow or job display names.** The surprises: the reusable ShellCheck
   reports as `shellcheck / shellcheck` (caller-job / reusable-job), and
   kalmia's ansible-lint reports as `ansible-lint` (the job id), *not*
   `Ansible Lint` (the workflow name). Guessing these wrong deadlocks the repo.
2. **Never require a context whose workflow is path-filtered at the `on:`
   level.** A required check whose workflow never triggers is held "Expected"
   forever and deadlocks every non-matching PR. The terraform repos solve this
   with an always-on `gate` job (see each repo's `terraform.yml`); only ever map
   checks that report on *every* PR (or skip at the job level, which counts as
   passing). `--require-checks` preflights every context against the repo's most
   recent PR check runs and **refuses** to require one that has never reported.

### Rollout order (do not invert)

The producing workflow must be **merged to `main` and observed reporting green
on a real PR before** the ruleset requires its check — never the reverse.
Requiring a check that isn't producing yet deadlocks the repo until the ruleset
is hand-reverted. So for each repo: (1) merge the workflow that emits the check;
(2) confirm it reports on a PR (a docs-only PR should show the check green with
the heavy jobs skipped); (3) `--require-checks`. The preflight enforces step 2
mechanically, but step 1 (merged to main, not just open in a PR) is on the
operator.

## `org-ruleset.json` — PARKED (needs GitHub Team)

The cleaner approach would be one ruleset at the org targeting `~ALL` repos, so
new repos inherit branch protection with no per-repo step. **Org-level rulesets
require a paid GitHub Team org plan** (verified 2026-06-15: on the Free plan the
create call returns 403 *"Upgrade to GitHub Team"* — and note it's the *plan*,
not token scope, that gates it). This file is kept ready for if/when the org
upgrades:

```bash
gh auth refresh -h github.com -s admin:org          # scope (necessary but not sufficient)
gh api -X POST orgs/lentago/rulesets --input fleet-ops/org-ruleset.json
```

Until then, `fleet-apply.sh` + `repo-ruleset.json` cover the same ground
per-repo.
