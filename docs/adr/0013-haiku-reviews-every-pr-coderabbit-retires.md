# ADR-0013: Haiku reviews every PR in the operating repos; CodeRabbit retires

**Status:** Accepted (2026-10-29; amended 2026-10-29: Decision 5's `.coderabbit.yaml` step was superseded, see there)

## Context

CodeRabbit was installed org-wide on 2026-10-03 as an advisory reviewer. Every
repo without its own config inherits the central file in
[`lentago/coderabbit`](https://github.com/lentago/coderabbit). The operating
practice that grew up around it is that a PR is not armed for auto-merge until
its review has posted and been triaged. `--auto` merges the moment the required
checks are green, so arming *is* the merge decision. That practice was never
written into the fleet's PR-workflow text; this record and the change that
codifies it (see Consequences) fix that.

On 2026-10-29 the practice turned CodeRabbit's free-tier limit into a merge
queue. Concurrent sessions opened about a dozen PRs across brasenia and kalmia.
At least five of them came back with "Review limit reached" or "Review rate
limited", among them kalmia#197, kalmia#200, kalmia#201 and kalmia#205. Each of
those then waited about 40 minutes for the next window or for an explicit
waiver. Two waivers were granted that day, kalmia#200 and kalmia#201. Paid tiers
replace the waiting with per-seat and per-file costs, which are no easier to
predict.

The fleet already has its own reviewer.
[`claude-review.yml`](https://github.com/lentago/shared-workflows/blob/v1.4.0/.github/workflows/claude-review.yml)
in shared-workflows runs Claude Code on a PR with a repo-specific focus block
and defaults to Haiku. Its history:

- **2026-06-25:** per-PR triggering was switched off and callers were left
  `workflow_dispatch`-only. [drosera#96](https://github.com/lentago/drosera/pull/96)
  is one of those per-repo changes; its body calls the change fleet-wide, and
  the reason was not recorded.
- **2026-07-01:** shared-workflows
  [ADR-0003](https://github.com/lentago/shared-workflows/blob/main/docs/adr/0003-ai-reviewer-advisory-never-a-merge-gate.md)
  documented two failure modes: turn exhaustion before posting, and
  intermittent empty API responses. Both turned the check red with no review.
  ADR-0003 made them **non-blocking** rather than eliminating them: the step is
  `continue-on-error`, the job always exits 0 and posts a soft-fail comment
  instead, and `max_turns` defaults to 40. The empty-response path still has no
  retry, so **a run can still fail to post a review**.
- **2026-10-06:** the disabled callers were deleted once CodeRabbit was the
  org-wide reviewer
  ([kalmia#136](https://github.com/lentago/kalmia/pull/136) and its siblings).

On 2026-10-29 Haiku was run read-only against the same PRs CodeRabbit could not
reach, and against one CodeRabbit had reviewed:

- **Blind benchmark.** The reviewer was given kalmia#196's branch at 1ad7a2a,
  before CodeRabbit's fixes, and told nothing about what to look for. It found
  the defect CodeRabbit had marked major: a failed later task drops the
  runner-restart handler, and the next run never restarts. It also found one
  CodeRabbit had missed: the job guard's fallback fails open when no
  `Runner.Worker` ancestor is found. That one is still on `main` and is tracked
  as [kalmia#206](https://github.com/lentago/kalmia/issues/206).
- **Four open PRs, reviewed in parallel in 75 s to 3.5 min each**:
  - kalmia#205: a redirect bypass of LXC 118's allowed-sites gate.
  - brasenia#103: a path that writes the Grafana token into the journal,
    reproduced against a local HTTP server.
  - brasenia#104: query-string secrets that reach LAN-readable files.
  - Several smaller correctness and test gaps.

  None of the four hit a limit. One finding was wrong: a missing co-authorship
  line was attributed to a README that has none to copy, which brasenia#104's
  triage corrected.

## Decision

1. **Haiku reviews every PR in the operating repos.** Each of these 17 repos
   carries a thin caller of `claude-review.yml`, pinned to a shared-workflows
   tag (shared-workflows ADR-0005), with a `review_prompt` written for that
   repo: `.github`, asclepias, betula, brasenia, claytonia, drosera, epigaea,
   kalmia, mitchella, osmunda, repo-template, shared-workflows,
   site-icecreamtofightwith-com, site-lentago-dev, site-pondviewlane-com,
   solidago and uvularia.

   The caller passes `secrets: inherit`, and the reusable workflow requires
   **`CLAUDE_CODE_OAUTH_TOKEN`**. The org secret must therefore be visible to
   all 17 repos. Two of them (mitchella and shared-workflows) have never run a
   workflow that uses it, so an org admin confirms the secret's repository
   access before the rollout passes its pilot repo.
2. **Repos without a caller.** Three groups get no caller:
   - the kits (lupinus, monarda and the three `uvularia-*-template` repos),
     which carry no cross-org workflows;
   - the `uvularia-demo-*` repos, which stand in for what a client generates
     from a kit;
   - `coderabbit`, which is retiring.

   CodeRabbit was their only automated reviewer, and retiring it leaves them
   with none in CI. That is intended. The arming rule (point 4) still applies
   to them: whoever arms one of their PRs first runs the same reviewer locally,
   read-only, as was done on 2026-10-29, and posts its output on the PR as a
   comment headed "Review (Haiku, local)".
3. **Triggers and labels.** The caller runs on `pull_request` types `opened`,
   `ready_for_review` and `labeled`. A `labeled` event reviews only when the
   label is `re-review` (Haiku) or `review:sonnet` (Sonnet). The caller picks
   the model with an expression on the label name in its `with:` block. After
   the review job finishes, a second job removes the triggering label, so
   adding it again triggers again. Draft PRs are skipped by the reusable
   workflow.

   The reviewer does not run on every push. It draws on the same Claude
   subscription as the bullpen and the interactive sessions, and a day of
   force-pushes should not spend that budget. Both labels join the managed set
   in [`fleet-ops/labels.json`](../../fleet-ops/labels.json). The repo-template
   caller is the reference copy that the other repos follow.
4. **The review is advisory, and the arming rule is the gate.** Neither GitHub
   nor this repo's terraform makes the reviewer a required status check.
   Instead, nobody arms a PR until both of these hold:
   - **a review has posted for the PR.** ADR-0003's soft-fail comment ("could
     not complete") is not a review: label `re-review` and wait. In a repo with
     no caller, the posted local review (point 2) is the review. Commits that
     only answer review findings do not need a fresh review. Any other
     substantive change pushed after the review does: label `re-review` again.
   - **every finding is triaged on the PR,** either fixed with the commit named
     or declined with a reason.
5. **CodeRabbit retires once the callers are live:**
   - ~~auto-review goes off in the central `.coderabbit.yaml`~~ (*superseded
     2026-10-29*: uninstalling the app stops all CodeRabbit activity at once,
     and the repo is archived read-only, so a config edit first would only add
     a PR to a closing repo; see #284);
   - the app is uninstalled from the org;
   - `lentago/coderabbit` is archived and removed from this repo's fleet
     config and terraform state (`terraform/README.md` "Retiring a repo";
     #284).

## Alternatives

- **Keep CodeRabbit and wait out its limits.** Rejected: on a busy day the wait
  is the bottleneck, and the alternative is waiving the review, which defeats
  the rule.
- **Pay for CodeRabbit.** Rejected: the cost scales with seats and files, not
  with what the fleet gets back, and the reviewer the fleet already maintains
  did at least as well on the same PRs.
- **Make the reviewer a required status check everywhere.** Rejected for now,
  for three reasons:
  - The job is `continue-on-error` and always green (ADR-0003), so requiring it
    proves only that it ran, not that a review posted.
  - Because it does not run on every push, a new head commit would carry no
    check. A required context that never reports stays "Expected" and holds the
    PR, which is the trap the fleet's path-filtered `gate` jobs are built
    around (see the `terraform.yml` header in kalmia).
  - An exhausted subscription window or an Anthropic outage would block every
    merge in the fleet, hotfixes included.
- **Sonnet by default.** Rejected as a default and kept as an escalation.
  Haiku's findings on 2026-10-29 were substantive. The label covers the PRs
  that warrant more: terraform, security gates, anything that applies to live
  state on merge.

## Revisit

Two weeks after the callers are live, look at how often the reviewer failed to
post. If that rate is low, consider a required **`review-gate`** job on the six
repos where a merge changes live state: `.github`, betula, claytonia, drosera,
kalmia and solidago. The gate would:

- run on every push but call no model;
- pass when the PR carries a posted review or a `review-waived` label (a label
  this record does not yet define);
- fail otherwise.

That keeps the gate cheap and deterministic, and keeps the model off the
critical path. The review is tracked on
[#276](https://github.com/lentago/.github/issues/276).

## Consequences

- The rollout is tracked on [#276](https://github.com/lentago/.github/issues/276):
  this record and the labels; the arming rule written into the canonical
  PR-workflow text in shared-workflows' `CLAUDE.md` and its mirrors; one
  caller PR per repo, starting with a single pilot repo whose first run proves
  the secret and the trigger wiring; then CodeRabbit's retirement.
- Until a repo's caller lands, its PRs are reviewed by running the reviewer
  locally, as in point 2.
- [ADR-0011](0011-fleet-secrets-handling.md) notes that CodeRabbit's gitleaks
  run was once the fleet's only secret scan. ADR-0011 mandated scanning and
  push protection on every repo, and
  [#240](https://github.com/lentago/.github/issues/240) delivered it, so
  nothing replaces that scan here.
- Fleet docs that describe CodeRabbit as the reviewer are updated in the
  retirement step, not in this record.
