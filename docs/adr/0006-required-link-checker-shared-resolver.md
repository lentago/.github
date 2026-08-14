# ADR-0006: A link checker is required on every repo, from one shared resolver

**Status:** Accepted (2026-07-25; reconstructed 2026-08-13)

## Context

Most of what the fleet ships is documentation — on some nights, every open PR is pure
Markdown. Yet a docs-only PR merged having asserted *nothing* about the docs it changed:
repos path-filter their heavy CI jobs to skip on docs-only PRs, a skipped job counts as
passing, and the fan-in `gate` passes too (issue #57).

Issue #57 sized the actual problem honestly rather than dramatizing it. A relative-link
scan across 15 active repos raw-reported **240 failures — but 237 were the scanner's
fault**: ~223 were site-absolute Astro/Starlight routes the router resolves at build
time (not filesystem paths), and 14 were GitHub's `../../issues/N` convention that
resolves correctly on github.com. The **real rate was 3 broken links out of 430** — low.
But all three came from **renames and removals**, the fleet's single most common class of
change and the one most easily left half-finished. The recorded conclusion: *"A check is
worth having precisely where the failure mode is systematic rather than frequent."*

## Decision

**Require a relative-link checker on every active repo, served from one reusable
resolver** rather than copied per repo. The reusable `docs-check` workflow lives in
`shared-workflows` (promoted from this repo's own `check_relative_links`), is
**unconditional** (no `paths:` filter, so it can be a required status check), and #68
("fleet-ops: require docs-check on every active repo", 2026-07-25) closed the fleet map by
requiring it everywhere.

For **this** repo specifically, #66 ("Decide: replace … or keep both", closed 2026-07-25)
decided **replace, not add**: drop `check_relative_links` from `ci/validate.py`, call the
reusable, and leave `validate.py` to the three checks that are genuinely repo-specific
(`configs`, `census`/`register`, and the fleet-shape checks). The reasoning: the two
implementations had already diverged, with the reusable ahead (reference-style links,
inline-code-span stripping, `~~~` fences), so keeping both would check this repo by the
*weaker* copy and require mirroring every future fix by hand.

## Alternatives

- **Add — run the reusable *and* keep the local `check_relative_links` (recorded, #66,
  rejected).** Rejected. Two divergent implementations of one check, with this repo gated
  by the staler one. The promotion existed precisely to end that duplication.
- **Per-repo bespoke link checks (recorded — the implicit prior state, rejected).**
  Rejected in favor of one shared resolver: a fix lands once and every repo gets it,
  which is the whole argument for the reusable.
- **Recorded trade-off, accepted with the decision:** the reusable skips any link
  resolving *outside* the repo root (that is how it tolerates `../../issues/N`), so a
  genuine over-deep typo like `[x](../../README.md)` where `../README.md` was meant is
  silently skipped. This repo's old local check had the identical behavior, so replacing
  loses nothing — noted so the limitation is a recorded decision, not a later surprise.
- **Heavyweight or external-link checking on every PR (retrospective — not considered as
  the chosen path).** *Worse.* The honest 3-in-430 rate argues against anything heavy;
  #57 already flagged that per-PR network checks are flaky and slow and belong on a
  schedule, not the merge gate.
- **No check — rely on rename discipline alone (retrospective — not considered at the
  time).** *Worse.* #57's instructive case was a broken image on a public README whose
  exact line a human edited during a deliberate rename audit *without noticing it pointed
  at nothing*. Discipline had its shot on that line and missed; the check exists for the
  systematic failure mode discipline does not reliably catch.

## Consequences

- `docs-check` is a required status check across the active fleet; a docs-only PR now
  asserts its relative links resolve before it can merge.
- `ci/validate.py` keeps only the checks specific to this repo; the shared resolver is
  the single source for link checking, updated once for everyone.
- The out-of-root skip is an accepted, documented blind spot: over-deep relative typos
  that escape the repo root are not caught by design.
