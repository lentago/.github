# Incident Digest — Phantom debt: a rename ticket filed against work finished two weeks earlier, 2026-07-21→25

*The fleet inventory said the AWS rename was "deliberately unchanged." The
inventory was stale; the rename had shipped. A governance sweep read the file,
believed it, and filed tracking debt against finished work.*
Compiled 2026-08-12 from a multi-session transcript harvest, cross-checked
against GitHub and AWS ground truth. All times **America/New_York (EDT, UTC-4)**.

**Deployment-caused:** no

---

## TL;DR

On 07-21, the fleet rename-discipline sweep (see the companion blessing-reversal
entry) filed solidago#142 — "Track the foundry-* → solidago AWS resource
rename" — on the premise, read out of `~/repos/CLAUDE.md`, that the AWS
resource names had been "deliberately unchanged." That line was stale: **the
rename had fully shipped on 07-07/08** (solidago#102/#103), two weeks before
the ticket existed. On 07-25, the fleet-wide issue grooming caught it — because
that session deliberately verified every claim against live state rather than
issue text ("stale local state already misled me once this session"): repo grep
found only historical mentions, and live AWS showed zero `foundry-*` buckets,
clusters, roles, or KMS aliases. #142 was closed as overtaken by events with a
full provenance comment, and — the part that makes this an incident resolved
rather than repeated — **both stale lines in the source document were fixed at
the source**, with an explicit "Check live state before filing rename debt from
this inventory" warning added.

This is the register's 2026-07-03 class (a stale written premise generating
wrong work) with two twists: the poisoned document was the fleet's own
instruction-as-code surface, and the fix landed in the document, not just the
ticket. The class then recurred a third time on 08-12 — the *canonical* doctrine
file in `shared-workflows` was found attributing DNS ownership to the wrong
repo and carrying the closed #142 as open debt — fixed the same day
(shared-workflows#33). Doctrine files drift like any other cache.

---

## Timeline

| Time | Event |
|---|---|
| 07-07/08 | foundry→solidago AWS rename ships end-to-end (solidago#102/#103); `~/repos/CLAUDE.md` line claiming names were "deliberately kept" is not updated |
| 07-20 ~10:00 | Near-miss preview: a PR review almost rejects a *correct* PR because session memory carried the same stale "names deliberately kept" claim; the memory is fixed, the inventory file is not |
| 07-21 | Rename-discipline sweep reads the stale line, files solidago#142 as tracking debt |
| 07-25 20:40Z | Fleet issue grooming begins with fresh clones: "stale local state already misled me once this session" |
| 20:44Z | Live AWS verified: zero `foundry-*` resources in the workload account |
| 20:49Z | #142 closed OBE with provenance ("filed on 2026-07-21 … the premise … was itself stale") |
| 20:53Z | Both stale lines in `~/repos/CLAUDE.md` corrected at source, with the check-live-first warning |
| 08-12 | Third instance: canonical `shared-workflows/CLAUDE.md` found misattributing the Route 53/DNS live surface and carrying #142 as open; fixed same day (shared-workflows#33) |

---

## What did NOT happen

- **No work was performed against the phantom debt** — the ticket sat four
  days and died in grooming. The cost was ticket noise and grooming time, not
  wasted engineering.
- **Live AWS was never touched**; verification was read-only.
- **The grooming didn't take the issue's word for it** — four of that day's
  five closures were for work that had shipped un-closed, all verified against
  live state first.

## CTO lessons

1. **Instruction-as-code is a cache with no TTL.** The fleet inventory is
   loaded into every session as authority, but nothing invalidates it when
   reality changes. Any entry that asserts live state ("names deliberately
   kept", "X owns Y") is a claim to verify, not a fact to act on — now stated
   in the file itself.
2. **Fix the source, not the symptom.** The 07-20 near-miss fixed the memory
   and left the inventory; the inventory then poisoned the very next sweep.
   A stale premise isn't resolved until the *document that will be read next*
   is corrected.
3. **Groom from ground truth.** The 07-25 pass closed five issues by checking
   live state first — the only reason #142's provenance was understood rather
   than the debt being "completed" a second time.
4. **Expect recurrence; instrument for it.** Three instances in six weeks
   (memory, inventory, canonical doctrine) make this a standing failure class.
   The mirrors' sync obligation now includes a drift review whenever live
   reality changes underneath them.

---

## Sources

Sessions `e4dd0011` (07-20 near-miss), `3c927161` (07-25 grooming),
`b366627f` (08-12 doctrine fix); solidago#142 (closed 20:49Z 07-25), #102/#103;
edits to `~/repos/CLAUDE.md` (07-25) and shared-workflows#33 (merged 08-12);
collateral filing solidago#153.
