# Game-day #1: killing a bullpen runner mid-job — the queue healed itself in 84 seconds, and nothing told anyone

Compiled 2026-08-17 from the live exercise (asclepias Lab 04 format; first scheduled game day, maintainer-coordinated).

**Deployment-caused:** no

---

## TL;DR

We killed a claytonia worker (`pct stop` on LXC 117, claude-runner-5) 94 seconds into a real job, with a pre-registered hypothesis: the queue's stale-heartbeat reaper should requeue the orphan within 90–150s, a second worker should finish it, the dashboard should show the loss, and **no alert should fire because none exists**. All four predictions held — recovery was fully autonomous (kill → reclaimed by claude-runner-2 in **84s**, second run finished clean, worker rejoined **20s** after `pct start`) — and the detection gap is now a filed workstream, not a suspicion.

## The contract under test

claytonia's queue README promises: workers heartbeat `workers/<host>.alive` every 30s; `process-inbox` reaps `processing/` entries whose owner is >90s stale, requeues once (`.retry`), fails them if stranded twice. At-least-once delivery; claim is an atomic rename.

## Timeline (UTC, 2026-08-17)

| T | Event |
|---|---|
| 22:34:09 | Sacrificial ad-hoc job dispatched (no repo side effects by design) |
| 22:34:12 | Claimed by **claude-runner-5** (atomic mv → processing/) |
| 22:35:49 | **T0 — `pct stop 117`** mid-job (94s into the run) |
| 22:37:13 | Reaper requeues the orphan as `.retry` |
| 22:37:14 | **Reclaimed by claude-runner-2** — 84s after the kill |
| 22:37:43 | `pct start 117` (recovery begins) |
| 22:38:03 | runner-5 heartbeating again — 20s |
| 22:39:11 | Retry run completes, exit 0 ($0.11, 118s). `failed/` stays empty |

## Hypothesis vs. reality

1. **"Requeue in 90–150s from the kill" — held, and taught a precision lesson.** Actual: 84s, *below* the predicted lower bound — because the staleness clock runs from the last heartbeat, not from the failure. The worker had last heartbeated ~35s before the kill, so the reaper's 90s window had a head start. Failure-detection latency is bounded by `staleness + poll cadence` measured from the last proof of life, not from the fault.
2. **"A second worker finishes the job" — held.** Clean handoff, single `.retry`, exit 0, nothing stranded.
3. **"Nothing alerts" — held, which is the finding.** The Runner Fleet dashboard showed the drop for anyone watching; no rule watches worker liveness or `.retry` events, so an unwatched dashboard was the entire detection surface. Filed as drosera#207.
4. **"Recovery is one command" — held.** `pct start`, 20 seconds to rejoin, no queue surgery.

## What the archive volunteered

Grepping `logs/` for `.retry` artifacts turned up two from 2026-07-08 — the reaper has already fired **in real production**, unnoticed, during the music-curator research waves. One of those retries even exercised the documented at-least-once boundary: the retried job found its predecessor's PR already open and stopped itself. Self-healing that works silently is the best argument for absence-alerting: the mechanism has been saving us without telling us.

## Residual findings

- A killed run leaves 0-byte `logs/<runid>.{json,stderr}` stubs from the dead worker. Cosmetic, but tooling that scans `logs/` should not read an empty stub as a completed run.
- The kill window matters: this exercise severed the worker *before* any PR push. A kill after branch-push but before PR-open is the nastier at-least-once case — the July chunk-10 retry shows the workers handle the duplicate-PR flavor of this, but it deserves its own game day.

## Governance lesson

The queue's crash recovery was CI-tested before tonight (bats harness, claim-by-rename races) — and the live exercise still earned its keep: it measured the actual numbers, surfaced the detection gap the tests can't see (tests assert recovery *happens*, not that humans *hear about it*), and pulled two unnoticed production recoveries out of the archive as corroboration. The register publishes all of it verbatim, per standing policy.
