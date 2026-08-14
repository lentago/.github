# ADR-0003: The merge gate is a classic branch-protection push allowlist, not ruleset bypass

**Status:** Accepted (2026-08-12; reconstructed 2026-08-13)

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
- The node-id gotcha is now recorded in `locals.tf`, the adoption record, and the
  incident register — a hand-authored app-actor declaration by legacy id will silently
  under-provision the allowlist.
- Workflows that push to PR branches (not `main`) are unaffected; the restriction
  matches `main` only.
