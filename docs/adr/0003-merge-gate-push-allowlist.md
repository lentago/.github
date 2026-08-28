# ADR-0003: The merge gate is a classic branch-protection push allowlist, not ruleset bypass

**Status:** Accepted (2026-08-12; reconstructed 2026-08-13; amended 2026-08-22 and 2026-08-27 — see [Amendment (2026-08-22)](#amendment-2026-08-22) and [Amendment (2026-08-27)](#amendment-2026-08-27))

## Context

With the org opening up as a learning lab — colleagues on a Players team with triage on
the active repos — "only the owner can merge to `main`" needed to become a **declared
invariant** rather than a side-effect of who happens to hold write permission. The goal:
every merge to `main` lands through an org owner/admin, and a future write grant to
anyone else still cannot update the ref.

Two mechanisms can express that on GitHub:

- a **ruleset** with an `update` rule and `bypass_actors` listing the allowed
  identities, or
- a **classic branch-protection push allowlist** (`restrictions`) naming who may push
  to `main`.

They look equivalent, but they interact differently with GitHub's asynchronous
auto-merge — and the fleet's convention is to arm `gh pr merge --auto` on essentially
every PR.

## Decision

**Use a classic branch-protection push allowlist** (`terraform/protection.tf`),
allowing only `cpitzi` — plus the GitHub Actions app on `music-curator` alone, so that
repo's documented bot merge keeps working. PRs #96–#98 (all 2026-08-12).

The deciding fact: **GitHub's async auto-merge path does not honor ruleset
`bypass_actors`.** A PR whose merge depends on a bypass sits `BLOCKED` forever
(community discussions #162623, #113172). A ruleset `update` rule would therefore
silently kill the fleet's arm-auto-merge-on-every-PR convention. A push *allowlist* is
evaluated transparently for allowed users, so `gh pr merge --auto` keeps arming and
firing for the owner (and for PATs that authenticate as `cpitzi`, such as the
weekly fleet-reports automation). The gate declares **only** the allowlist; PR-required,
squash-only, required checks, and force-push/deletion protection stay in the `main`
ruleset, so the layers compose rather than duplicate.

A second defect surfaced on first apply and is recorded here and in the incident
register (`fleet-reports/incidents/2026-08-12-merge-gate-silent-allowance-drop.md`):
**app actors must be declared by their next-format node id.** The branch-protection
mutation *silently drops* an app actor declared by its legacy global node id
(`MDM6QXBwMTUzNjg=`) and reports no error; the fix (#98) re-declares the Actions app by
its next-format id (`A_kwHNJr_NPAg`), which GraphQL's deprecation warning supplies.
*(This diagnosis was wrong — see the Amendment below. The text is kept as the record of
what was believed on 2026-08-12.)*
PR #97 separately imported asclepias's live `main` ruleset id so adoption would not
create a duplicate.

## Alternatives

- **A ruleset `update` rule with `bypass_actors` (recorded — the rejected mechanism).**
  Rejected. Async auto-merge ignores the bypass, so every armed PR strands `BLOCKED` —
  it would break the convention it was meant to enforce. This is the whole reason the
  classic mechanism was chosen.
- **An org-level ruleset with bypass (retrospective — not considered at the time).**
  *Worse.* It inherits the same async-auto-merge defect *and* requires a paid GitHub
  Team plan the org deliberately does not buy (see ADR-0004). Two independent reasons it
  is a non-starter here.
- **No gate — rely on permission levels alone (retrospective — not considered at the
  time).** *Worse.* That is exactly the pre-existing state the decision replaces: "only
  the owner merges" would remain a side-effect of nobody else holding write, and the
  moment someone is granted write for another reason, the invariant silently
  evaporates. The gate exists to survive that grant.

## Consequences

- 16 `github_branch_protection` resources add the push allowlist across the public
  fleet; `music-curator` additionally allows the Actions app.
- The failure mode is **silent** (a PR that never merges), so the rollout step is
  explicitly: apply, then verify auto-merge still arms and fires on the next routine PR.
- ~~The node-id gotcha is now recorded in `locals.tf`, the adoption record, and the
  incident register — a hand-authored app-actor declaration by legacy id will silently
  under-provision the allowlist.~~ Superseded by the Amendment: the real gotcha is
  actor *eligibility*, and it is recorded in the same three places.
- Workflows that push to PR branches (not `main`) are unaffected; the restriction
  matches `main` only.

## Amendment (2026-08-22)

**The music-curator allowance is withdrawn, and the "second defect" above was
misdiagnosed.** Issue #148 established, against live state and GitHub's own
documentation, that the built-in GitHub Actions app is **not an eligible push actor**
on classic branch protection in any id format: the allowlist accepts users, teams, and
GitHub Apps *installed* on the repository, and the identity behind `GITHUB_TOKEN` is not
an installation (GitHub declines it deliberately — otherwise any collaborator could reach
`main` by authoring a workflow; community discussion #25305). The mutation drops an
ineligible actor silently, so #98's next-format id "fix" changed nothing: every CI apply
from 2026-08-12 to 2026-08-22 reported `1 changed` on `merge_gate["music-curator"]` and
live `restrictions.apps` stayed `[]` throughout — a perpetual diff, not an apply still
owed. The allowance was removed under #148; `gate_extra_allowances` stays as the
extension point, with the eligibility rule in its comment.

The decision itself stands unchanged: the gate is a classic push allowlist, and `cpitzi`
is its only actor. What changes is the consequence for `music-curator`: its follow-fold
bot merge was never reachable under `GITHUB_TOKEN` (a second, independent blocker —
required checks that never report on a `GITHUB_TOKEN` push — is recorded alongside it),
and **music-curator#87** owns the decision between a dedicated installed GitHub App,
a PAT of an allowed user, or dropping the bot merge. Whichever lands, the fleet-wide
invariant holds: a workflow reaches `main` only through an identity this allowlist
names explicitly.

Also adopted under #148: the apply job now runs `terraform plan -detailed-exitcode`
immediately after `apply` and fails the run if changes remain. "Apply complete" is the
provider's claim, not the state's; a silent drop is now a red run.

## Amendment (2026-08-27)

**The write grant this ADR was built to survive is now live, and the gate held.** The
org base repository permission moved `none` → `write`, so every member holds write on
every repo; the `Players` team, which carried `triage` on fifteen of them, was retired
the same day as strictly redundant beneath the new base. No member lost access.

This is the contingency the Context names — "a future write grant to anyone else still
cannot update the ref" — arriving in practice, and it confirms the mechanism choice
rather than disturbing it. `restrictions` was re-read on every public repo after the
change and remains `users: ["cpitzi"]`, `teams: []`, `apps: []`: because the allowlist
is evaluated against the ref rather than derived from permission levels, raising the
base grant changed nothing about who may update `main`. Had the gate been expressed as
a permission level, this would have been a merge-policy change; it was a no-op.

Two consequences worth recording. First, `teams: []` is now load-bearing in a way it
was not before — with no team in the org, the allowlist's team dimension is unused, and
`gate_extra_allowances` remains the only supported route for adding one. Second, the
base permission itself is **not** Terraform-managed: `default_repository_permission` is
live-only org state, so the invariant this ADR declares is enforced by `protection.tf`
alone and does not depend on the base grant staying put. Codifying the org settings
alongside it is open work owned by **#176**, not a gap in the gate — that issue also
carries the decision on whether the CI apply should be able to mutate org settings at
all, which is a question about the rails rather than about this ADR.
