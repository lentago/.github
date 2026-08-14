# ADR-0004: Per-repo rulesets under the Free plan; org ruleset parked, free tier as policy

**Status:** Accepted (2026-06-15; reconstructed 2026-08-13)

## Context

Branch protection for the fleet can be expressed two ways on GitHub:

- **One org-level ruleset** — a single definition (`fleet-ops/org-ruleset.json`,
  `fleet-baseline`) targeting `~ALL` repos and `~DEFAULT_BRANCH`, applied once for the
  whole org. Maximally DRY.
- **Per-repo rulesets** — one `main` ruleset per repository, applied 15+ times.

The org-level path is the more elegant one, but it is gated by GitHub's plan tier.

## Decision

**Use per-repo rulesets; park the org-level ruleset.** Verified 2026-06-15: on the Free
plan, the org ruleset create call returns **403 *"Upgrade to GitHub Team"*** — and the
gate is the **plan**, not a permission the token is missing (`fleet-ops/README.md`
§ `org-ruleset.json` — PARKED). So `fleet-baseline` cannot be created today.

Rather than delete the work or upgrade, the org ruleset is **kept ready to reverse the
decision the moment the plan changes**: `fleet-ops/org-ruleset.json` holds the exact
definition and `fleet-ops/README.md` records the exact reversal command
(`gh api -X POST orgs/lentago/rulesets --input fleet-ops/org-ruleset.json`).

Staying on the Free tier is itself a **recorded stance, not an accident.** The org
profile states it emphatically: when a service offers a free tier, that is the one the
lab runs, and caps are treated as real operating constraints to manage rather than buy
past. Per-repo rulesets are the cost of that stance, and the cost is paid deliberately.

## Alternatives

- **One org-level ruleset (recorded — the blocked option).** Rejected *for now* by the
  2026-06-15 403, not on merits. It remains the preferred shape if the plan ever
  changes, which is precisely why `org-ruleset.json` and its apply command are parked
  intact rather than removed.
- **Upgrade to GitHub Team to unlock org rulesets (retrospective — not considered at
  the time).** *Lateral-to-worse* under current policy. It would buy the DRY org-level
  definition, but at a recurring subscription cost the lab's free-tier stance
  deliberately avoids — and per-repo rulesets, while more numerous, are generated from
  the same JSON and applied by the same tooling, so the duplication is machine-managed,
  not hand-maintained. The saving is real but small; the cost is ongoing.
- **No rulesets — configure branch protection by hand per repo (retrospective — not
  considered at the time).** *Worse.* It abandons settings-as-code entirely for the one
  surface that most needs to be uniform and auditable across the fleet.

## Consequences

- Each active repo carries its own `main` ruleset, managed via `fleet-ops` /
  `terraform/` from the shared JSON — uniform in practice despite being defined
  per-repo.
- `org-ruleset.json` is dormant but not dead: the decision is one command away from
  reversal if the org ever moves to a paid plan.
- The free-tier constraint recurs elsewhere in the fleet (e.g. auto-merge and private-
  repo rulesets are plan-gated too), so this decision is one instance of a standing
  policy rather than a one-off.
