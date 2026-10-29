# ADR-0013: Haiku reviews every fleet PR; CodeRabbit retires

**Status:** Accepted (2026-10-29)

## Context

CodeRabbit was installed org-wide on 2026-10-03 as an advisory reviewer. Every
repo without its own config inherits the central file in
[`lentago/coderabbit`](https://github.com/lentago/coderabbit). The operating
rule that grew up around it is that a PR is not armed for auto-merge until its
review has posted and been triaged. `--auto` merges the moment the required
checks are green, so arming *is* the merge decision.

On 2026-10-29 that rule turned CodeRabbit's free-tier limit into a merge queue.
Concurrent sessions opened about a dozen PRs across brasenia and kalmia. At
least five of them came back with "Review limit reached" or "Review rate
limited", among them kalmia#197, kalmia#200, kalmia#201 and kalmia#205. Each of
those then waited about 40 minutes for the next window or for an explicit
waiver. Two waivers were granted that day, kalmia#200 and kalmia#201. Paid tiers
replace the waiting with per-seat and per-file costs, which are no easier to
predict.

The fleet already has its own reviewer.
[`claude-review.yml`](https://github.com/lentago/shared-workflows/blob/v1.4.0/.github/workflows/claude-review.yml)
in shared-workflows runs Claude Code on a PR with a repo-specific focus block
and defaults to Haiku. Its history:

- **2026-06-25:** per-PR triggering was switched off fleet-wide, and callers
  were left `workflow_dispatch`-only
  ([drosera#96](https://github.com/lentago/drosera/pull/96)). The reason was not
  recorded.
- **2026-07-01:** the two failure modes that made it untrustworthy were turn
  exhaustion before posting and intermittent empty API responses, which turned
  the check red with no review. shared-workflows
  [ADR-0003](https://github.com/lentago/shared-workflows/blob/main/docs/adr/0003-ai-reviewer-advisory-never-a-merge-gate.md)
  fixed both: the step is `continue-on-error`, the job always exits 0, and
  `max_turns` defaults to 40.
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

1. **Haiku reviews every PR in the operating repos.** Each repo below carries a
   thin caller of `claude-review.yml`, pinned to a shared-workflows tag
   (shared-workflows ADR-0005), with a `review_prompt` written for that repo:
   `.github`, asclepias, betula, brasenia, claytonia, drosera, epigaea, kalmia,
   mitchella, osmunda, repo-template, shared-workflows,
   site-icecreamtofightwith-com, site-lentago-dev, site-pondviewlane-com,
   solidago and uvularia. Three groups are left out:
   - the kits (lupinus, monarda and the three `uvularia-*-template` repos),
     which carry no cross-org workflows;
   - the `uvularia-demo-*` repos, which stand in for what a client generates
     from a kit;
   - `coderabbit`, which is retiring.
2. **Triggers are `opened`, `ready_for_review`, and two labels.** Labelling a
   PR `re-review` reviews it again, and `review:sonnet` reviews it again with
   Sonnet. The reviewer does not run on every push. It draws on the same Claude
   subscription as the bullpen and the interactive sessions, and a day of
   force-pushes should not spend that budget. Both labels join the managed set
   in [`fleet-ops/labels.json`](../../fleet-ops/labels.json).
3. **The review is advisory, and the arming rule is the gate.** Neither GitHub
   nor this repo's terraform makes the reviewer a required status check.
   Instead, nobody arms a PR until its review has posted and every finding is
   triaged on the PR, either fixed or declined with a reason. That is the rule
   CodeRabbit ran under, unchanged.
4. **CodeRabbit retires once the callers are live:**
   - auto-review goes off in the central `.coderabbit.yaml`;
   - the app is uninstalled from the org;
   - `lentago/coderabbit` is archived through this repo's terraform.

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
    proves only that it ran.
  - Because it does not run on every push, a new head commit would carry no
    check, and a required context that never reports holds the PR. That is the
    deadlock class [#27](https://github.com/lentago/.github/issues/27) fixed for
    path-filtered workflows.
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
- pass when the PR carries a posted review or a `review-waived` label;
- fail otherwise.

That keeps the gate cheap and deterministic, and keeps the model off the
critical path. The review is tracked on
[#276](https://github.com/lentago/.github/issues/276).

## Consequences

- The rollout is tracked on [#276](https://github.com/lentago/.github/issues/276):
  this record and the labels, then one PR per repo, then CodeRabbit's
  retirement.
- Until a repo's caller lands, its PRs can still be reviewed by running the
  reviewer locally. That is how the 2026-10-29 reviews above were done.
- [ADR-0011](0011-fleet-secrets-handling.md) notes that CodeRabbit's gitleaks
  run was once the fleet's only secret scan. That gap was closed by ADR-0011
  itself (scanning and push protection on every repo), so nothing replaces it
  here.
- Fleet docs that describe CodeRabbit as the reviewer are updated in the
  retirement step, not in this record.
