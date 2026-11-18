# ADR-0016: Dependabot patch and minor updates are a routine that merges on a deterministic gate, under the operator's identity

**Status:** Accepted (2026-11-17). Records the maintainer's decisions of
2026-11-17 on [#346](https://github.com/lentago/.github/issues/346). The rule is
option C, a standing rule codified in this repository. The merge identity is a
fine-grained personal access token that authenticates as the operator, chosen
over a dedicated GitHub App (see Alternatives).

## Context

- **What Dependabot opens.** Every fleet repository runs Dependabot weekly.
  Every repository splits its `github-actions` updates into two groups:
  `actions-routine` for minor and patch, and `actions-major` for majors
  ([#114](https://github.com/lentago/.github/issues/114); this repository's
  copy is [`.github/dependabot.yml`](../../.github/dependabot.yml)). That way a
  breaking change never hides inside a pile of patches. The npm, pip and docker
  configurations in a few repositories group differently, and some of their
  groups have no update-type split. Dependabot security updates are also on
  fleet-wide ([#234](https://github.com/lentago/.github/issues/234)).
- **They cannot meet the arming rule.** The AI review skips Dependabot PRs. A
  Dependabot-triggered run receives no Actions secrets, so the reviewer's token
  would be missing, and each caller excludes `dependabot[bot]` at the job level
  (see this repository's
  [`claude-review.yml`](../../.github/workflows/claude-review.yml), header and
  job condition). These PRs therefore never meet
  [ADR-0013](0013-haiku-reviews-every-pr-coderabbit-retires.md)'s arming rule,
  that a review has posted and every finding is triaged. Merging them has been
  left to the maintainer
  ([#346](https://github.com/lentago/.github/issues/346)). Nobody makes that
  call on a schedule, so a backlog builds:
  on 2026-11-17 it stood at 18 open PRs. 16 were green and current, one was a
  failing major ([monarda#54](https://github.com/lentago/monarda/pull/54),
  Astro 5 → 7) and one was superseded.
- **The merge gate admits one actor.** `main` on every fleet repository takes
  updates only from `cpitzi`, plus whatever `gate_extra_allowances` names, and
  that is empty today ([ADR-0003](0003-merge-gate-push-allowlist.md)). The
  identity behind a workflow's `GITHUB_TOKEN` is not an eligible push actor (the
  ADR-0003 amendment of 2026-08-22), so the usual "auto-merge Dependabot from a
  workflow" recipe cannot pass the gate. It should not pass, either: if that
  identity could update `main`, any workflow could.
- **The promise already admits routines.**
  [ADR-0014](0014-merge-promise-humans-own-the-policy.md) Decision 1 says that
  opted-in scheduled routines merge on their deterministic gate alone. Its
  point 4 defines that gate for one kind of routine only: runner-App PRs armed
  by `cr-automerge`.

## Decision

1. **The rule.** A Dependabot patch or minor update is a routine under
   ADR-0014 Decision 1. It merges on the gate in point 2, with no AI review and
   no human click. This covers version updates and security updates. Majors
   stay manual, security majors included.

2. **The gate.** The sweeper (point 4) merges a pull request only when every
   one of these holds:
   - Its author is `dependabot[bot]`, its head branch is in the same
     repository, and every commit on it is authored by Dependabot and verified
     by GitHub.
   - Every entry in the head commit's `updated-dependencies` block (the field
     `dependabot/fetch-metadata` reads) has `update-type` set to
     `version-update:semver-patch` or `version-update:semver-minor`. A major, a
     missing type or a block that does not parse means the PR is skipped. A
     grouped PR passes only if every one of its entries does, so a single major
     anywhere in the group skips the whole PR. The gate reads the type of each
     update, so it does not depend on how a repository groups them.
   - No update is a minor of a version below 1.0.0, judged by its
     `dependency-version`. Below 1.0.0 a minor release may break things, so such
     an update counts as a major and stays manual. A minor entry with no
     `dependency-version` is skipped.
   - It changes no file the sweeper itself runs: its workflow and any script
     that workflow calls. An update to an action the sweeper uses therefore stays
     manual. Otherwise the sweeper could merge a change to its own code, unread,
     and run it with the token on the next run.
   - Its `mergeStateStatus` is `CLEAN` at that head: the required status checks
     are green and, where the ruleset is strict, the branch is up to date.
   - The merge call carries the head that was evaluated:
     `gh pr merge --squash --match-head-commit <sha>`, and never `--admin`.

   The required status checks remain the merge gate. The ruleset enforces them
   at merge time, and the sweeper never asks to bypass them. The sweeper merges
   only when the PR is already `CLEAN` and leaves nothing armed between runs.
   ADR-0014 point 5 therefore holds without a disarm step: if anything is pushed
   after the evaluation, the merge call fails.

3. **The merge identity.** The sweeper authenticates with a fine-grained personal
   access token that the operator mints, so its merges carry the operator's
   identity, `cpitzi`, which is already the merge gate's one actor.
   - **Scope.** The resource owner is `lentago`, with access to only the
     repositories in [`fleet-ops/repos.json`](../../fleet-ops/repos.json).
     Repository permissions: Contents and Pull requests read and write, plus
     Metadata read. GitHub may refuse a merge that edits `.github/workflows/`,
     which every `actions-routine` PR does, unless the token also has Workflows
     write. Workflows write is added only if the first such merge is refused
     without it.
   - **Expiry.** At most one year. The expiry date goes into
     [`fleet-reports/lock-in/renewals.yml`](../../fleet-reports/lock-in/renewals.yml)
     when the token is minted, so the renewal calendar opens an issue before it
     lapses.
   - **Store.** The token is a secret in this repository's `dependabot-merge`
     environment, which deploys from `main` only. Terraform creates the
     environment, and the value is set out of band
     ([ADR-0011](0011-fleet-secrets-handling.md) rule 4).
   - **No gate change.** `gate_extra_allowances` stays empty, so this rule does
     not depend on [#225](https://github.com/lentago/.github/issues/225).

4. **The mechanism.** One workflow in this repository runs hourly, plus on
   `workflow_dispatch` with a dry-run input, and only from `main`. It walks the
   open Dependabot PRs in scope and applies the gate. No other repository
   carries a caller, there is no reusable workflow in shared-workflows, and the
   kits gain no files.
   - It uses as few third-party actions as it can, each pinned by commit SHA.
     It never checks out or runs a pull request's content.
   - **Strict repositories.** In a repository whose ruleset requires branches
     to be up to date ([#266](https://github.com/lentago/.github/issues/266)),
     one merge leaves the rest of the batch behind `main`. For a PR that is
     behind, the sweeper comments `@dependabot rebase` and merges at the new
     head on a later run. It never updates the branch itself, because a push by
     anyone else makes Dependabot stop managing the PR. It merges at most one PR
     per strict repository per run.
   - **Scope** is every repository in `fleet-ops/repos.json`. The token's
     repository list is cut from the same file, and a repository the token
     cannot reach turns the run red, so the two cannot drift apart silently. No
     repository is excluded today.

5. **The audit trail.** A merge under the operator's identity looks like the
   operator's own merge, so every sweeper merge is marked as the sweeper's:
   - Before merging, the sweeper comments on the PR, naming this ADR, the run
     that merged it and the head it evaluated.
   - The squash commit's message ends with the trailer
     `Merged-by-routine: dependabot-sweeper` and the run's URL.
   - Every run lists the merges of the last 30 days that carry the trailer. If
     any of them was not authored by `dependabot[bot]`, the run fails. A merge
     like that is an incident.

## Alternatives

- **A dedicated GitHub App, `lentago-dependabot-merge`, added to every
  repository's merge-gate allowlist.** Weighed and not chosen; the maintainer
  picked the token on 2026-11-17. An App would have given the sweeper's merges a
  distinct identity (`mergedBy` would name it) and short-lived installation
  tokens (ADR-0011 rule 1). It would also have needed:
  - an App to mint, install and keep;
  - a second actor on the merge gate of every repository, the first fleet-wide
    use of `gate_extra_allowances`;
  - [#225](https://github.com/lentago/.github/issues/225) fixed first, because
    the fleet Terraform's token could not then declare an App allowance.
- **Per-repository callers of a reusable workflow, triggered on
  `pull_request`.** This was #346's first sketch. Rejected:
  - A Dependabot-triggered run can reach a credential only as a Dependabot
    secret.
  - It runs the workflow file from the PR's own merge ref. A Dependabot PR that
    bumps an action used in that run would execute the new version, which nobody
    has reviewed, with the merge credential in reach.
- **The same callers, triggered on `pull_request_target`.** Rejected. The
  workflow code would be reviewed, but the credential would become an Actions
  secret in 25 repositories, readable by any workflow in them. The kits would
  also need vendored copies, because they carry no cross-org workflows.
- **Auto-merge armed with `GITHUB_TOKEN`, with `github-actions` allowlisted.**
  Not possible: that identity is not an eligible push actor (ADR-0003, amendment
  of 2026-08-22). Not wanted either: every workflow would gain a path to `main`.
- **Reuse an existing App.** Rejected. The runner App and `claude` write code.
  `lentago-template-sync` and `lentago-pr-gate` each serve one job, and widening
  either would make its key a fleet-wide merge credential with a second purpose.
- **Arm and wait (`gh pr merge --auto --match-head-commit`).** Rejected.
  Auto-merge stays enabled when someone with write access pushes. A Dependabot
  rebase, a group refresh or any other write-holder's push between two sweeps
  would then merge a head nobody evaluated, unless the sweeper also disarmed.
  Merging only when `CLEAN` closes that window without the disarm step.
- **Keep merging by hand.** Rejected. That is the backlog #346 was filed about.

## Consequences

- **The merge gate is unchanged.** `cpitzi` stays its one actor, and
  `gate_extra_allowances` stays empty. ADR-0003 is untouched.
- **Merges carry the operator's identity.** On GitHub, `mergedBy` on a sweeper
  merge is `cpitzi`, the same as on a merge the operator armed. Point 5's
  comment and trailer are what tell them apart, and the audit holds the sweeper
  to them. A merge made with the token outside the sweeper carries neither mark,
  so the record cannot tell it from the operator's own.
- **ADR-0011 rule 1 exception.** Rule 1 prefers an App's short-lived tokens for
  automation that acts on GitHub, and asks a new long-lived credential for a
  reason. This token is that exception, recorded here as ADR-0011 requires.
  Rule 2 still holds: the token reaches only the fleet repositories, with two
  permissions (three if Workflows proves needed), and expires within a year.
- **What a leaked token could do.** Whoever held it could act as the operator in
  any repository in scope, with no review:
  - open a pull request, or push to an existing one, and merge it once its
    required checks were green;
  - comment as the operator.

  It could not push to `main` directly or bypass the required checks, and it
  reaches nothing outside the fleet repositories. Four things limit it:
  - the token exists in one place, a main-only environment that no pull
    request's content ever reaches;
  - it expires within a year;
  - revoking it ends it at once;
  - the audit catches misuse only through the sweeper. A leaked token used
    elsewhere would leave no mark, which is the cost of the operator's identity
    named above.
- **Order of work.**
  1. This record.
  2. A PR here creates the `dependabot-merge` environment (main-only).
  3. The operator mints the token to the form in Decision 3, stores it in that
     environment, and records its expiry in `renewals.yml`.
  4. The sweeper lands in dry-run, its list is checked against the open backlog,
     and then it starts merging.
  5. The first live merges are verified: each carries the comment and the
     trailer, and the backlog drains.
- **The promise.** The profile and `CONTRIBUTING.md` already say that opted-in
  scheduled routines merge on their deterministic gate alone, so their wording
  does not change. This record names Dependabot as the second such routine.
- **Mirrors.** The canonical PR-workflow text in `shared-workflows/CLAUDE.md`
  and its `~/repos/CLAUDE.md` mirror gain one line: the sweeper merges
  Dependabot patch and minor PRs, and majors remain the maintainer's call.
- **What the rule trusts.** Merging minors and patches unread trusts upstream
  semantic versioning, and the required checks are the only test. The
  maintainer accepted that trade on 2026-11-17. A major still gets read.
- **Kit adopters.** A client estate built from a kit does not get this rule. An
  adopter who wants it sets up their own sweeper and credential in their own org
  ([ADR-0007](0007-client-owned-delivery-no-multi-tenant-saas.md)). That would
  be a kit feature, with its own issue.
- **Revisit** in any of these cases:
  - a patch or minor that this rule merged causes an incident (a register entry
    with `Deployment-caused: yes`);
  - a second human gains write access, because merges under the operator's
    identity then blur two people's records, and in two-reviewer mode a
    review-count rule would hold these PRs (ADR-0014 point 6);
  - the token is ever found used outside the sweeper;
  - the sweeper ever lists a major as eligible. That would be a defect in the
    gate, and the sweeper stops until it is fixed.
