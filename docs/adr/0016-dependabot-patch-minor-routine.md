# ADR-0016: Dependabot patch and minor updates are a routine that merges on a deterministic gate, through a dedicated merge App

**Status:** Proposed (2026-11-17). Records the maintainer's decision of
2026-11-17 on [#346](https://github.com/lentago/.github/issues/346) (option C: a
standing rule, codified in this repository) and the design posted there. It
becomes Accepted once the maintainer has decided on the merge identity
(Decision 3) and on the token fix in
[#225](https://github.com/lentago/.github/issues/225).

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
- **They cannot meet the arming rule.** The AI review
  ([ADR-0013](0013-haiku-reviews-every-pr-coderabbit-retires.md)) skips
  Dependabot PRs. A Dependabot-triggered run receives no Actions secrets, so the
  reviewer's token would be missing, and each caller excludes
  `dependabot[bot]` at the job level (see this repository's
  [`claude-review.yml`](../../.github/workflows/claude-review.yml) header).
  These PRs therefore never meet the arming rule that a review has posted and
  every finding is triaged. Merging them was recorded as the maintainer's
  call on 2026-10-13. Nobody makes that call on a schedule, so a backlog builds:
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
- **App allowances cannot be applied today.** The fine-grained
  `FLEET_ADMIN_TOKEN` that runs this repository's Terraform cannot resolve a
  GitHub App's node id. The first App allowance
  ([#224](https://github.com/lentago/.github/pull/224)) failed on apply for
  that reason, and [#225](https://github.com/lentago/.github/issues/225) holds
  the fix.

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
     grouped PR is judged by its largest update. The gate reads the type of
     each update, so it does not depend on how a repository groups them.
   - No update is a minor of a version below 1.0.0, judged by its
     `dependency-version`. Below 1.0.0 a minor release may break things, so such
     an update counts as a major and stays manual. A minor entry with no
     `dependency-version` is skipped.
   - It changes no file the sweeper itself runs: its workflow and any script
     that workflow calls. An update to an action the sweeper uses therefore stays
     manual. Otherwise the sweeper could merge a change to its own code, unread,
     and run it with the key on the next run.
   - Its `mergeStateStatus` is `CLEAN` at that head: the required status checks
     are green and, where the ruleset is strict, the branch is up to date.
   - The merge call carries the head that was evaluated:
     `gh pr merge --squash --match-head-commit <sha>`.

   The required status checks remain the merge gate. The ruleset enforces them
   at merge time, and the merge App is not a bypass actor. The sweeper merges
   only when the PR is already `CLEAN` and leaves nothing armed between runs.
   ADR-0014 point 5 therefore holds without a disarm step: if anything is pushed
   after the evaluation, the merge call fails.

3. **The merge identity.** The sweeper merges as a dedicated GitHub App,
   `lentago-dependabot-merge`, and as nothing else.
   - The App is private, with no webhook. It has Contents and Pull requests
     write, and Metadata read. GitHub may refuse to let an App merge a PR that
     edits `.github/workflows/`, which every `actions-routine` PR does, unless
     the App also has Workflows write. Workflows write is added only if the
     first such merge is refused without it.
   - Each run mints installation tokens per repository, narrowed to the
     permissions the call needs. Listing and reading use read-only tokens.
   - It is installed on every fleet repository.
   - Its private key lives in one place: a secret in this repository's
     `dependabot-merge` environment, which deploys from `main` only. Terraform
     creates the environment, and the key is set out of band
     ([ADR-0011](0011-fleet-secrets-handling.md) rule 4).
   - It is on the push allowlist of `main` on every repository in scope, through
     `gate_extra_allowances`, declared by its next-format node id. Each allowance
     is verified with the read-back command in
     [`terraform/locals.tf`](../../terraform/locals.tf) and with the apply job's
     post-apply convergence check.

4. **The mechanism.** One workflow in this repository runs hourly, plus on
   `workflow_dispatch` with a dry-run input, and only from `main`. It walks the
   open Dependabot PRs in scope and applies the gate. No other repository
   carries a caller, there is no reusable workflow in shared-workflows, and the
   kits gain no files.
   - It uses as few third-party actions as it can, each pinned by commit SHA.
     It never checks out or runs a pull request's content.
   - **Audit.** Every run lists the PRs merged by the App in the last 30 days.
     If any of them was not authored by `dependabot[bot]`, the run fails. A
     merge like that is an incident.
   - **Strict repositories.** In a repository whose ruleset requires branches
     to be up to date ([#266](https://github.com/lentago/.github/issues/266)),
     one merge leaves the rest of the batch behind `main`. For a PR that is
     behind, the sweeper comments `@dependabot rebase` and merges at the new
     head on a later run. It never updates the branch itself, because a push by
     anyone else makes Dependabot stop managing the PR. The sweeper also merges
     at most one PR per strict repository per run.
   - **Scope** is every repository in
     [`fleet-ops/repos.json`](../../fleet-ops/repos.json). Terraform derives the
     allowances from that file and the sweeper reads the same file, so the two
     cannot drift apart. No repository is excluded today.

## Alternatives

- **Per-repository callers of a reusable workflow, triggered on
  `pull_request`.** This was #346's first sketch. Rejected:
  - A Dependabot-triggered run can reach the key only as a Dependabot secret.
  - It runs the workflow file from the PR's own merge ref. A Dependabot PR that
    bumps an action used in that run would execute the new version, which nobody
    has reviewed, with the merge key in reach.
- **The same callers, triggered on `pull_request_target`.** Rejected. The
  workflow code would be reviewed, but the key would become an Actions secret in
  25 repositories, readable by any workflow in them. The kits would also need
  vendored copies, because they carry no cross-org workflows.
- **Auto-merge armed with `GITHUB_TOKEN`, with `github-actions` allowlisted.**
  Not possible: that identity is not an eligible push actor (ADR-0003, amendment
  of 2026-08-22). Not wanted either: every workflow would gain a path to `main`.
- **Reuse an existing App.** Rejected. The runner App and `claude` write code.
  `lentago-template-sync` and `lentago-pr-gate` each serve one job, and widening
  either would make its key a fleet-wide merge credential with a second purpose.
- **A personal access token authenticating as `cpitzi`.** Rejected. It merges as
  the gate's own actor, so the record could not tell a routine merge from the
  operator's. It is also a long-lived credential where an App identity serves
  (ADR-0011 rules 1 and 2).
- **Arm and wait (`gh pr merge --auto --match-head-commit`).** Rejected.
  Auto-merge stays enabled when someone with write access pushes. A Dependabot
  rebase, a group refresh or any other write-holder's push between two sweeps
  would then merge a head nobody evaluated, unless the sweeper also disarmed.
  Merging only when `CLEAN` closes that window without the disarm step.
- **Keep merging by hand.** Rejected. That is the backlog #346 was filed about.

## Consequences

- **A second actor on every gate.** `main` on every fleet repository admits
  `cpitzi` and `lentago-dependabot-merge`. This is the first fleet-wide use of
  `gate_extra_allowances`, the extension point ADR-0003 kept for this purpose.
  ADR-0003's decision stands.
- **What a leaked key could do.** This is the first key outside a person's hands
  that can both write to a branch and pass the merge gate. Whoever held it could
  open a pull request, or push to an existing one, and merge it once its
  required checks were green, in any repository in scope, with no review. It
  still could not push to `main` directly or bypass the required checks. That
  is the same concern that rules out widening an existing App (Alternatives),
  and this design answers it in four ways:
  - the key exists in one place, a main-only environment that no pull
    request's content ever reaches;
  - tokens are short-lived and narrowed for each call;
  - every run audits the App's merges, so one that Dependabot did not author
    turns the run red;
  - revoking the key or uninstalling the App ends it at once.

  The runner App's key already allows the first half (writing branches and
  opening pull requests). Merging is what this key adds.
- **Order of work.**
  1. #225 is fixed first. Until then the allowance cannot be applied.
  2. The maintainer mints and installs the App and sets its key.
  3. The allowances and the environment land in one PR here, and #225's three
     template-sync allowances come back into config in the same pass.
  4. The sweeper lands in dry-run, its list is checked against the open backlog,
     and then it starts merging.
  5. The first live merges are verified: `mergedBy` is the App, and the backlog
     drains.
- **Rebase requests from an App.** Whether Dependabot honours `@dependabot
  rebase` from an App is verified on the first dry-run. If it does not, the
  sweeper reports the PRs that are behind and a person posts the comment.
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
  adopter who wants it mints their own App in their own org
  ([ADR-0007](0007-client-owned-delivery-no-multi-tenant-saas.md)). That would
  be a kit feature, with its own issue.
- **Revisit** in any of these cases:
  - a patch or minor that this rule merged causes an incident (a register entry
    with `Deployment-caused: yes`);
  - an estate switches to two-reviewer mode, where a review-count rule would
    hold these PRs and the exemption has to be a check (ADR-0014 point 6);
  - the sweeper ever lists a major as eligible. That would be a defect in the
    gate, and the sweeper stops until it is fixed.
