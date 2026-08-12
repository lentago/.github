# Incident Digest — The TV that kept showing yesterday's decision: a cross-session stomp on the wall display, 2026-07-21→22

*One session repointed the wall display on request. The next morning's session,
asked to push the daily brief, didn't know — found a real-but-irrelevant bug,
fixed it, and declared success while the TV kept showing the old content.*
Compiled 2026-08-12 from a multi-session transcript harvest, cross-checked
against GitHub ground truth. All times **America/New_York (EDT, UTC-4)**.

---

## TL;DR

On 07-21 afternoon, at the operator's request ("stream this inventory to the
roku"), a session codified a wall-display repoint via kalmia#65 — render source
switched from the Morning Brief to a runtime-inventory showcase — and it was
applied on the compositor container. Next morning, a **different session** was
asked to "Push the morning briefing to the roku app." It had no knowledge of
the repoint, found the TV showing stale content, and produced a confident
**wrong diagnosis**: a Drive-upload timing race in the brief pipeline — a real
defect, genuinely fixed, but not the cause of the symptom — and **declared
success at 08:33**. The operator corrected it at 08:45 ("Roku still shows the
fleet report"). The session then pulled the live frame off the container, found
the render source pointing at the inventory page, reverted via kalmia#66
(merged 08:48), redeployed, and verified by 08:52. Twenty-two minutes of
confusion, zero data loss, and a textbook instance of the register's
cross-session class: **an intentional change by one session becomes the next
session's mystery.**

---

## Timeline

| Time | Event |
|---|---|
| 07-21 15:20 | "publish this to pub.lan … stream this inventory to the roku, too" |
| 15:41 | kalmia#65 merged: render source → runtime inventory (correctly codified, per the live-state discipline) |
| 15:44 | Auto-mode classifier denies the session's on-host apply (mislabels it a CI bypass); session declines to work around it |
| 15:48 | Operator runs the apply by hand; TV now shows the inventory |
| 07-22 08:30 | New session, new mission: "Push the morning briefing to the roku app" |
| 08:33 | Wrong diagnosis declared as success: a real Drive-upload timing race found and fixed; "Today's brief is now live on the TV" — it wasn't |
| 08:45 | Operator: "Roku still shows the fleet report" |
| 08:46–08:48 | Live frame pulled off the container; render source found pointing at the inventory URL; kalmia#66 reverts, merged |
| 08:52 | Redeployed and verified — brief actually on the TV; `brasenia-wall-display-repoint` memory written as the fix-forward |

---

## What did NOT happen

- **No data or config was lost.** Both the repoint and the revert were clean,
  codified PRs; the inventory TV edition remained available at its own URL.
- **Neither session did anything unauthorized.** Both were executing explicit
  operator requests; the live-state discipline was followed both days.
- **The timing-race fix was not wasted** — it was a real latent defect in the
  brief pipeline. It was just the wrong answer to the question asked.

## CTO lessons

1. **Verify success at the user-visible surface.** The morning session
   verified the pipeline it had fixed, not the television. When the deliverable
   is "X is on the screen," the check is a frame capture of the screen —
   which is exactly what cracked the case eleven minutes later.
2. **A real bug found mid-diagnosis is the most dangerous wrong answer.** It
   terminates investigation with the satisfaction of a fix. Symptom-cause
   linkage ("would this bug produce *this* stale content?") is a separate
   verification step, not an inference.
3. **Intentional state changes need a session-visible record at change time.**
   The repoint was codified in the owning repo — the *right* place for the
   machine — but nothing told the next session "the TV currently shows X, on
   purpose." The memory written as the fix-forward is the durable answer;
   writing it belongs at the change, not at the incident.
4. **This is the register's 07-03 class, inverted.** The stale-memory incident
   was a session trusting old context; this one is a session lacking new
   context. Same gap — cross-session state visibility — approached from both
   ends.

---

## Sources

Sessions `444aa60e` (07-21, `~/repos`) and `3d88d885` (07-22, `~` →
`~/repos/kalmia`); kalmia#65 (merged 07-21 19:41Z), #66 (merged 07-22 12:48Z);
compositor LXC on the PVE cluster; memory `brasenia-wall-display-repoint.md`.
