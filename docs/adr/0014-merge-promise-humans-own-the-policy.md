# ADR-0014: The merge promise: humans own the policy and direct every change; runner-App PRs need a human approval

**Status:** Accepted (2026-11-01). Records Decision 1 on
[#304](https://github.com/lentago/.github/issues/304), made by the maintainer the
same day, with its AI-review clause narrowed to directed pull requests on review
of this record (decision recorded on
[#306](https://github.com/lentago/.github/issues/306)).

## Context

The org profile said **"Humans own every merge,"** and `CONTRIBUTING.md` said the
operator "owns every merge." The external review of 2026-11-01 (finding 6, filed
as [#304](https://github.com/lentago/.github/issues/304)) checked that sentence
against what the fleet enforces and found that the two had diverged. Verified the
same day:

- **No approval is required.** The `main` ruleset on every public repo
  ([`terraform/rulesets.tf`](../../terraform/rulesets.tf),
  [ADR-0004](0004-per-repo-rulesets-free-tier.md)) requires a pull request,
  squash merges and the mapped status checks, with
  `required_approving_review_count = 0`.
- **The org owner is the only push actor.** The merge gate
  ([ADR-0003](0003-merge-gate-push-allowlist.md)) is a push allowlist on `main`
  that admits only `cpitzi`.
- **The AI review is advisory.** Haiku reviews every PR in the operating repos
  ([ADR-0013](0013-haiku-reviews-every-pr-coderabbit-retires.md)), but the review
  is not a required check. What gates arming is a written rule: a review has
  posted and every finding is triaged.
- **Sessions arm merges.** Local Claude Code sessions run under the operator's
  identity and arm auto-merge once that rule is met. The operator directs every
  change and owns the rules that decide when it merges, but does not read every
  diff.
- **Scheduled routines merge on a deterministic gate.** claytonia
  [ADR-0009](https://github.com/lentago/claytonia/blob/main/docs/adr/0009-policy-gated-auto-merge-for-routine-prs.md)
  lets `bin/cr-automerge`, not the agent, arm auto-merge on a runner-App PR when
  the target repository's default branch opts that kind of PR in through
  `.claytonia/automerge.json`. No `lentago` repository carries that file today.
  The bullpen also works repositories outside the org, and one of them, a private
  repository, has run two routines under the exception since 2026-10-28; the
  runner App has merged their PRs itself.
- **Two paths merge with no AI review.** Found on review of this record:
  - That private repository has no reviewer caller, so its routine PRs merge on
    the rule and the required checks with no review at all.
  - This repository's weekly refresh
    ([`fleet-reports.yml`](../../.github/workflows/fleet-reports.yml)) is a
    scheduled workflow that arms auto-merge on its own PR as it opens it. It
    stages only the three generated report files, and the required checks are
    its gate. The review can post after the merge or not at all:
    [#275](https://github.com/lentago/.github/pull/275), the
    refresh of 2026-10-26, merged with no review comment. If arming fails, the
    step falls back to an immediate squash merge without
    `--match-head-commit`, outside point 5's rule;
    [#312](https://github.com/lentago/.github/issues/312) aligns it.
- **A human approval on agent-authored PRs is decided, not yet enforced.** The
  enforcement is the `agent-pr-gate` required check (claytonia#117, option A,
  decided 2026-10-30;
  [shared-workflows#84](https://github.com/lentago/shared-workflows/issues/84);
  rollout in [#289](https://github.com/lentago/.github/issues/289)).

The review's recommendation was to say what the fleet actually does on every
surface, and to make the **solo-operator** and **two-reviewer** modes explicit
rather than prescribing one approval count for everyone.

## Decision

1. **The public promise.** Humans own the policy and direct every change. Every
   directed pull request gets an AI review. Opted-in scheduled routines merge on
   their deterministic gate alone. The profile and `CONTRIBUTING.md` say this,
   and the sentence "humans own every merge" is retired.
   - A *directed* pull request is one a person asked for: a change the operator
     directs a session to make, or a job dispatched to the bullpen. Its AI
     review gates arming (ADR-0013).
   - A scheduled routine's pull request is not directed. Its gate is its rule
     and the required checks; the AI review is not part of it. Both paths in
     the Context fall under this clause, and neither is a gap to close.
   - The first wording, "every pull request gets an AI review," was narrowed
     because those two paths made it untrue.
2. **Runner-App PRs need a human approval.** In Decision 1, "agent-authored PRs"
   means a PR authored by the bullpen's runner App (`lentago-claude-runner[bot]`),
   the author `agent-pr-gate` keys on. It merges only after a human with write
   access submits an approving review on its current head commit.
   `agent-pr-gate` enforces this once #289 makes it required. A session may arm such a PR, but a
   session never submits that approval, even though it runs under the operator's
   identity. This closes the limit claytonia#117 states up front: the check
   cannot tell a person's approval from a session's when both use one identity.
3. **Session-armed PRs merge on the policy.** For a PR the operator directs a
   session to open, merging requires:
   - the AI review posted and every finding triaged (ADR-0013's arming rule);
   - the required status checks green;
   - the head being armed is the head that was reviewed (point 5).

   No human approval is required. In solo-operator mode there is no second human
   to give one, and GitHub does not let an author approve their own pull request.
4. **The routine exception and its gate.** A runner-App PR may merge without a
   human approval only when `cr-automerge` armed it under a rule. All of these
   hold, or it does not merge:
   - ADR-0009's conditions:
     - the job named the rule and succeeded;
     - the rule is read from the target's default branch, never from the PR head;
     - the PR is open, not a draft, from a same-repository branch to the default
       branch, and authored by the App;
     - its title matches the rule in full;
     - it changes between one and `max_files` paths, every one of them (a
       rename's old path included) matching the rule's globs.
   - The required status checks still gate. A rule removes the click, not the
     checks. The AI review is not part of the gate (point 1): where the
     repository has a reviewer caller it still posts, advisory, and where it has
     none the PR merges without one.
   - A rule's paths cover data files whose consumers validate them. They never
     cover code, workflows or infrastructure. A path-and-title gate bounds where
     an automated change lands, not what it says.
   - Where `agent-pr-gate` runs, it passes such a PR only when the PR's current
     head is the commit `cr-automerge` armed under a rule. ADR-0009's
     Consequences already name this requirement.
   - Opting in an org repository also means letting the runner App update that
     repository's `main` through the merge gate (`gate_extra_allowances` in
     [`terraform/locals.tf`](../../terraform/locals.tf)). That is a reviewed
     change in this repository, and none exists today. Verify that the first such
     merge lands before treating the gate as proven.
5. **The head-SHA rule, for every armed merge.** Whatever arms auto-merge, a
   session or `cr-automerge`, arms the head that was reviewed or evaluated and no
   other. For a session that means the reviewed commit, or a later one that only
   answers its findings. The arming call carries that commit
   (`gh pr merge --auto --squash --match-head-commit <sha>` for sessions), so a
   push between review and arming makes the arm fail. A substantive push after
   arming re-opens the question:
   - a session's PR is disarmed and takes a fresh review under ADR-0013's rule;
   - a routine PR is evaluated again by `cr-automerge`, or disarmed;
   - an agent PR's approval stops counting, because `agent-pr-gate` counts only
     an approval on the current head.

   The implementations belong to claytonia (`cr-automerge`) and
   shared-workflows#84. This record states the rule they meet.
6. **Two modes, named.**
   - **Solo operator.** This is the Lentago estate today, and the one-tech-person
     shop [ADR-0008](0008-pro-bono-practice-one-reader.md) writes for.
     - `required_approving_review_count = 0`, and the push allowlist names the one
       human.
     - Agent-authored PRs need that human's approval (point 2).
     - Everything else merges on the policy (points 3 and 4).
   - **Two reviewers.** This mode applies to an estate with a second human who
     has write access.
     - Every PR, whoever authored it, needs an approving review on its current
       head from a human other than its author: `required_approving_review_count
       = 1`, `dismiss_stale_reviews_on_push = true` and
       `require_last_push_approval = true`.
     - `agent-pr-gate` stays.
     - A count rule also holds routine PRs, and auto-merge does not honor ruleset
       bypass (ADR-0003). An estate that wants both this mode and the routine
       exception therefore needs the exemption expressed as a check, not as a
       bypass. That gets designed when the first such estate exists.

   An estate picks its mode and records the choice in its own repository. The
   fleet does not prescribe one count for everyone.

## Alternatives

- **Keep "humans own every merge" and make it true with
  `required_approving_review_count = 1` everywhere.** Rejected. A solo operator
  cannot approve their own PRs, and GitHub's auto-merge path does not honor
  ruleset bypass (ADR-0003), so every PR the only human authors would stall. This
  is claytonia#117's option B, rejected there on 2026-10-30 for the same reason.
- **Keep the sentence and rely on practice.** Rejected. The review showed that a
  reader can check the ruleset against the sentence. A promise the configuration
  contradicts costs more than a narrower promise it keeps.
- **Drop the routine exception so the sentence is closer to true.** Rejected. The
  maintainer accepted ADR-0009's exception on 2026-10-28 because the routines'
  cadence depends on it. The honest fix is to say it, not to withdraw it.

## Consequences

- `profile/README.md` and `CONTRIBUTING.md` carry the new wording in the same
  change as this record.
- The same claim appears on other surfaces, which their own repositories own:
  lentago.dev ([site-lentago-dev#111](https://github.com/lentago/site-lentago-dev/issues/111)),
  asclepias's `manual/estate-atlas.md` and drosera's `README.md`. claytonia's
  README already carries the ADR-0009 exception.
- The canonical PR-workflow text in `shared-workflows/CLAUDE.md` and its
  `~/repos/CLAUDE.md` mirror gain points 2 and 5 as rules for sessions. Neither
  has a `review_prompt` counterpart, for the same reason the arming rule has
  none: a reviewer reading the PR cannot observe how it was armed.
- ADR-0003 and ADR-0013 stand. This record states the promise their mechanisms
  add up to.
- The same review's finding 7, release tags that were immutable only by
  convention, is answered separately: the tag ruleset in
  [#305](https://github.com/lentago/.github/issues/305) and the ADR-0005 addendum
  in [shared-workflows#88](https://github.com/lentago/shared-workflows/issues/88).
- **Revisit** when `agent-pr-gate` is required fleet-wide (close the gap between
  points 2 and 4 against the live check), when an org repository first opts a
  routine in, or when a second human gains write access to an operating repo.
  That last event is the switch to two-reviewer mode.
