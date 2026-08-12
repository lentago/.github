# Incident Digest — Bless-and-forget: a rename resolution merged at 07:54 and reversed as policy by 09:15, 2026-07-21

*An automation baked "fleet precedent" into a job spec, a worker faithfully
executed it, and the operator reversed the precedent eighty minutes later. The
origin story of the fleet's rename discipline.*
Compiled 2026-08-12 from a multi-session transcript harvest, cross-checked
against GitHub ground truth. All times **America/New_York (EDT, UTC-4)**.

---

## TL;DR

The night of 07-20, the new wall-display repo was created as `lunaria`, made
public, and renamed `brasenia` the same night when the operator caught the
codename-roster violation himself ("Lunaria is invasive here") — a clean
same-night rename, including a direct-push rejection by the hour-old branch
ruleset that correctly forced the rename through a PR. The incident came the
next morning: dispatching kalmia#61 (what to do about the legacy `lunaria`
runtime names), the local session **baked the "document the legacy names and
keep them" resolution into the bullpen job spec, citing fleet precedent** from
the 07-04 rebrand wave. The worker produced a docs-only blessing PR; it merged
and #61 closed by 07:54. At 09:15 the operator reversed the policy fleet-wide
("track renames all the way through runtime and never bless-and-forget") — the
just-closed issue became five freshly filed tracking issues, the four-tier
rename-discipline doctrine landed in `shared-workflows` the same morning, and
the docs merged eighty minutes earlier had to be corrected.

Nothing broke live. The cost was rework and a sharpened rule; the risk it
exposed is real: **an agent citing precedent can institutionalize a policy the
operator never ratified, at merge speed.**

---

## Timeline

| Time | Event |
|---|---|
| 07-20 22:27 | Repo `lunaria` created; wall-display concept work lands |
| 23:21 | Repo flipped public |
| 23:25 | Operator catches the roster violation: "Lunaria is invasive here. We need a native to new england name" |
| 23:32 | Direct push of the rename rejected by the hour-old ruleset — rename ships as brasenia PR #1 (system working as designed) |
| 07-21 07:50 | "ok dispatch kalmia 61" |
| 07:51 | Session bakes the bless-the-legacy-names resolution into the job spec, citing the betula/drosera/claytonia precedent |
| 07:53–07:54 | Worker PR (kalmia#62) merges; #61 closed |
| 09:15 | Operator reverses: "adjust instructions systemwide to track renames all the way through runtime and never bless-and-forget" |
| 09:17–09:23 | Doctrine codified (shared-workflows#25, the four-tier rename discipline); five tracking issues filed for the now-un-blessed debt: kalmia#63, betula#89, drosera#169, claytonia#65, brasenia#2 |

---

## What did NOT happen

- **No live system carried a wrong name because of the blessing** — the
  eighty-minute window contained only documentation.
- **The worker did nothing wrong.** It executed the resolution it was handed,
  competently. The steering decision was made upstream, in the dispatch.
- **The rename itself (lunaria→brasenia, tier 1–2) was clean and same-night**
  — the incident is entirely about how the *residue* was resolved.

## CTO lessons

1. **Precedent is not policy.** "The fleet did it this way before" is an
   observation, not a ratified rule. When an agent is about to close an issue
   by *choosing between policies*, that choice belongs in front of the
   operator — one AskUserQuestion would have cost thirty seconds and saved the
   morning's reversal.
2. **Steering decisions don't belong inside job specs.** The dispatch encoded
   the resolution, so the worker never saw an alternative. Dispatches should
   carry the task; contested judgment calls ride separately.
3. **A reversal's cheapness is a function of its latency.** Caught in eighty
   minutes, this cost a docs correction and five issue filings. The identical
   pattern left for a quarter becomes archaeology — which is exactly what the
   four-tier discipline (repo/docs → registries → IaC → runtime, tiers 3–4
   deferred only into open tracking issues) now prevents.
4. **The rule earned its keep immediately**: the grandfathered debt from the
   07-04 wave got tracking issues that morning, and one (solidago#142) was
   later discovered to have been filed from a stale premise — see the
   companion entry — because now there was a register to check.

---

## Sources

Sessions `2e315b0d` (07-20 evening, `~`) and the 07-21 morning dispatch;
bullpen run `20260721T115149Z-kalmia-61-brasenia-docs`; kalmia#61/#62,
shared-workflows#25 (merged 13:18Z); tracking issues kalmia#63 (still open at
harvest), betula#89, drosera#169, claytonia#65, brasenia#2; brasenia PR #1.
