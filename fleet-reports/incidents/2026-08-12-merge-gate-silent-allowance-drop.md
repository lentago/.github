# Incident Digest — The gate that dropped a guard on the way up: merge-gate rollout's silent allowance loss, 2026-08-12

*Rolling a fleet-wide merge gate revealed that the previous day's "adoption"
had never populated state, that a placeholder in a command block will get
pasted, and that the provider silently discards app allowances it doesn't
recognize — one of which is still pending re-apply.*
Compiled 2026-08-12 from a multi-session transcript harvest, cross-checked
against live GitHub state at harvest time. All times **America/New_York (EDT,
UTC-4)**.

**Deployment-caused:** yes

---

## TL;DR

Sweeping the newly opened org, the operator asked to gate every merge to main
on an org owner/admin. The gate was codified as per-repo branch-protection
push allowlists (.github#96) and applied by hand (the local token is
deliberately read-mostly). The rollout surfaced four distinct defects. **(1)**
The drafted apply command contained a literal placeholder
(`<the fine-grained admin PAT …>`) that went into `GITHUB_TOKEN` verbatim —
401, plus the env var shadowing the keyring auth. **(2)** The failure revealed
that the previous day's Terraform adoption had **never populated state**: the
recorded "189 imports" didn't exist, so this run was the real first apply (190
imports). **(3)** A repo born live that same morning (asclepias) was missing
from the module's ruleset map — fixed in #97. **(4)** The genuine regression:
the branch-protection mutation **silently ignores legacy-format app node IDs**,
so music-curator's GitHub Actions app was dropped from its push allowance —
its automation degraded to manual merges. The fix (next-format node ID) merged
as .github#98 and served as the auto-merge canary proving the gate live on all
16 repos — but the **re-apply that restores the allowance was still
outstanding at harvest time** (live check: `restrictions.apps` still empty).
A worse incident was declined during design: the ruleset `bypass_actors` path
was researched, found incompatible with auto-merge's async completion (it
would have wedged every armed PR fleet-wide), and never applied.

---

## Timeline

| Time | Event |
|---|---|
| 15:19 | Session begins; gate design: branch-protection push allowlist per repo, not ruleset `bypass_actors` |
| (design) | `bypass_actors` canary staged against repo-template but **never applied** — research shows auto-merge completion ignores bypass_actors; the path is abandoned with the reasoning committed as code comments |
| 15:45 | Operator pastes the drafted apply block; the placeholder goes into `GITHUB_TOKEN` literally → 401 (and shadows keyring auth). Session owns the defect |
| 15:48–15:52 | Failure surfaces: asclepias missing from the ruleset map (#97); adoption state never populated — "this run is the real first apply" (190 imports) |
| ~15:51–16:14 | Real apply runs: 16 repos gated; post-apply verification 16/16 |
| 16:17 | **The regression found by read-back**: music-curator's Actions app allowance silently dropped — the mutation ignores legacy `MDM6…` node IDs without erroring. Re-declared with the next-format ID; #98 merged as the live-gate auto-merge canary |
| harvest | Live check: `restrictions.apps` on music-curator/main still `[]` — **the one-change re-apply remains outstanding** |

---

## What did NOT happen

- **No repo was left ungated** — post-apply verification confirmed the
  owner/admin gate live on all 16 mains, including the just-adopted repo.
- **The placeholder paste leaked nothing** — it was a placeholder, not a
  credential; the cost was one failed run and some shadowed auth confusion.
- **The bypass_actors fleet-wide wedge never happened.** The canary was
  staged, researched, and abandoned before touching anything — the sharpest
  save of the day, verified live (no `update` rule, empty `bypass_actors`).
- **music-curator's degradation is soft**: its automation waits for manual
  merges; nothing fails, nothing is lost.

## CTO lessons

1. **Silent partial application is the worst provider behavior — read back
   what you wrote.** The mutation accepted a legacy node ID and dropped it
   without erroring. On enforced surfaces, every apply needs a full read-back
   diff (which is exactly how this was caught) — "apply succeeded" is the
   provider's claim, not the state's.
2. **"Adopted" is a claim about state files — verify it when it's made.** The
   08-11 adoption recorded imports that never landed; the record went
   unchecked until the next apply tripped over it. An adoption isn't done
   until `terraform plan` on a fresh init shows the expected no-op.
3. **Never hand an operator a command block with an inline placeholder
   secret.** The paste is foreseeable — placeholders belong in a separate
   "set this first" step that fails loudly if unset (`: "${GITHUB_TOKEN:?}"`),
   never inline in the runnable block.
4. **Research async platform behavior before org-wide gates.** Auto-merge's
   completion path not honoring `bypass_actors` is community-documented, not
   intuited; checking before applying avoided wedging every armed PR in the
   fleet. Platform gates + platform automation interact; verify the pair.
5. **Open item, tracked here until closed:** one `terraform apply` (expect
   exactly one change) restores music-curator's allowance; verify with
   `gh api repos/lentago/music-curator/branches/main/protection` showing the
   Actions app back in `restrictions.apps`.

---

## Sources

Session `4f4eec0c` (2026-08-12, `~/repos` ↔ `~/repos/dotgithub`);
.github#96 (merged 19:37Z), #97 (19:48Z), #98 (20:17Z, the canary); live
read-back of music-curator branch protection at harvest; `terraform/locals.tf`
comments carrying the node-ID and bypass_actors gotchas; community refs
#162623/#113172 (auto-merge vs bypass_actors).
