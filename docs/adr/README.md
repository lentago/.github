# Architecture decision records

These ADRs were **reconstructed on 2026-08-13** from this repo's own history —
commit and PR/issue records, `CLAUDE.md`, the incident register, and fleet session
archives — as part of a fleet-wide ADR recovery. They were not written at the time the
decisions were made. Each record's **status date is the original decision date**; the
"reconstructed 2026-08-13" note in every status line marks when the record itself was
written. Every issue/PR number, file path, and date cited below was verified against
this repo during reconstruction; anything that could not be confirmed was dropped or
hedged rather than asserted.

Each ADR's **Alternatives** section separates the options actually weighed at the time
from **retrospective** options (explicitly labelled *"retrospective — not considered at
the time"*), so the historical record is not confused with hindsight.

| ADR | Decision | Date |
| :-- | :-- | :-- |
| [0001](0001-fleet-ops-in-org-meta-repo.md) | Fleet governance tooling lives in the org `.github` meta-repo | 2026-06-20 |
| [0002](0002-declarative-terraform-settings-as-code.md) | Settings-as-code migrated from imperative sweep to declarative Terraform, incrementally | 2026-08-11 |
| [0003](0003-merge-gate-push-allowlist.md) | The merge gate is a classic branch-protection push allowlist, not ruleset bypass | 2026-08-12 |
| [0004](0004-per-repo-rulesets-free-tier.md) | Per-repo rulesets under the Free plan; org ruleset parked, free tier as policy | 2026-06-15 |
| [0005](0005-incident-register-publishes-verbatim.md) | The incident register publishes verbatim | 2026-07-13 |
| [0006](0006-required-link-checker-shared-resolver.md) | A link checker is required on every repo, from one shared resolver | 2026-07-25 |
