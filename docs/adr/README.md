# Architecture decision records

ADRs **0001–0006** were **reconstructed on 2026-08-13** from this repo's own history —
commit and PR/issue records, `CLAUDE.md`, the incident register, and fleet session
archives — as part of a fleet-wide ADR recovery. They were not written at the time the
decisions were made. Each reconstructed record's **status date is the original decision
date**; the "reconstructed 2026-08-13" note in every such status line marks when the
record itself was written. Every issue/PR number, file path, and date cited in them was
verified against this repo during reconstruction; anything that could not be confirmed
was dropped or hedged rather than asserted. From **ADR-0007 onward, records are authored
at decision time** and carry no reconstruction note.

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
| [0007](0007-client-owned-delivery-no-multi-tenant-saas.md) | Kits ship into client-owned estates; the practice never operates a multi-tenant service | 2026-08-17 |
| [0008](0008-pro-bono-practice-one-reader.md) | Lentago Labs is a pro-bono practice with one reader; the estate is the demonstration | 2026-09-30 |
| [0009](0009-uvularia-client-owned-records-vault.md) | uvularia: a client-owned records vault with a grounded Ask box and a live compliance board, as three repos and three pipelines (amended 2026-10-04: adoption is a ladder, one repo first) | 2026-10-03 |
| [0010](0010-retire-deepwiki.md) | Retire DeepWiki across the fleet: no badge, section, footer clause, profile link, or repo homepage points at it; Lab 00 to be deleted and the Devin app uninstalled in the sweep on #237 | 2026-10-07 |
| [0011](0011-fleet-secrets-handling.md) | How the fleet handles secrets: identity before secrets, values only in approved stores, Terraform holds slots not values, out-of-band values verified, scanning and push protection required on every repo, leaks rotated not scrubbed | 2026-10-07 |
| [0012](0012-six-promises-codenames-are-parts.md) | The offering is told as six promises (plus three when you need them); every codename is a part under exactly one promise, with a plain-words role; one map on every surface | 2026-10-12 |
| [0013](0013-haiku-reviews-every-pr-coderabbit-retires.md) | Haiku reviews every PR in the operating repos; the review is advisory and the arming rule (a posted review, every finding triaged) is the gate; CodeRabbit retires; a model-free required gate on the apply-on-merge repos is revisited in two weeks | 2026-10-29 |
| [0014](0014-merge-promise-humans-own-the-policy.md) | The merge promise: humans own the policy and direct every change, every PR gets an AI review, opted-in routines merge on a deterministic gate; runner-App PRs need a human approval; solo-operator and two-reviewer modes named | 2026-11-01 |
