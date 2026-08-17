# Incident Digest — The kernel keeps shooting the biggest Claude: workstation OOM kills during concurrent-session work, 2026-07-14

*Eleven OOM kills in one boot, and the fattest process is always an agent
session. Concurrency risk has a resource dimension, not just a git one.*
Compiled 2026-08-12 from a multi-session transcript harvest. All times
**America/New_York (EDT, UTC-4)**.

**Deployment-caused:** no

---

## TL;DR

At 17:57 on 2026-07-14, during a 4-concurrent-session window (a heavy
enterprise-search harvest plus long-runners), the workstation (14 GiB RAM +
4 GiB swap) hit global out-of-memory and the kernel killed the fattest process:
a **5.8 GB `claude` process inside the terminal's cgroup**, taking the terminal
and its in-flight session with it. Diagnosis in a fresh session showed this was
a **repeating pattern, not a one-off: 11 OOM kills that boot** — 4 on Jul 9
(including a ~12 GB claude process inside VS Code), 2 on Jul 10, 5 on Jul 14.
Large-context sessions balloon to 6–12 GB each; run three or four at once on a
14 GiB laptop and the kernel eventually chooses one. A stale `npm run preview`
server that had been running for 3d19h was found squatting in the baseline and
killed. Transcripts survived; work resumed via continuation sessions; no repo
data was lost. Structural remediation (bigger swap, or simply a bigger
machine) was acknowledged and deferred.

---

## Timeline

| Time | Event |
|---|---|
| Jul 9 | 4 OOM kills, incl. a ~12 GB claude process in VS Code — pattern begins |
| Jul 10 | 2 more kills |
| 07-14 15:58–17:13 | 4 concurrent sessions active (the month's first high-concurrency window) |
| 17:57 | Global OOM; kernel kills the 5.8 GB claude process; terminal dies with it |
| 18:01 | Fresh diagnosis session: "laptop. gnome just killed my term" |
| 18:02–18:04 | Root cause pinned: hard kernel OOM, not GNOME/oomd; 11 kills this boot enumerated |
| 18:05 | Stale 3d19h `npm run preview` (port 4323) found and killed |
| 18:07 | Swap-grow + don't-parallel-heavies advice given; structural fix deferred ("I can afford a beefier laptop now") |
| →02:29 | Harvest continues in continuation sessions; nothing re-lost |

---

## What did NOT happen

- **No repository or file data was lost.** The kill took a process, not a
  working tree; transcripts persisted and the work continued in continuation
  sessions the same evening.
- **The kernel behaved correctly** — genuine memory pressure, correct victim
  selection. This is capacity, not a bug.
- **The concurrent sessions did not collide on shared state** — the 4-way
  window's risk materialized as RAM, not as git.

## CTO lessons

1. **Concurrency budgets include memory.** The fleet's collision thinking is
   git-shaped (branches, queues, PRs), but four large-context sessions is
   also ~2–3× physical RAM on this machine. A concurrency habit needs a
   resource ceiling: either fewer simultaneous heavies or hardware sized for
   the habit.
2. **The fattest process is your active session.** The kernel's victim
   selection means the *most important* work dies first. Swap headroom is the
   difference between a slowdown and a kill — the suggested swap growth was
   never applied and the pattern continued until it was structural.
3. **Long-lived dev servers leak into the baseline.** A preview server nobody
   remembered had been holding memory for almost four days. Session-spawned
   servers need a lifetime tied to their session or a periodic sweep.
4. **Detection was a human noticing their terminal vanish.** `journalctl -k`
   held the whole story; an OOM event feeding the observability stack would
   have surfaced the Jul 9 kills before Jul 14's took a live session.

---

## Sources

Sessions `aa8a99a3` (diagnosis, `~`), `f3d053dc` (victim) and continuations
`107eaf66`/`3e5e613b`; kernel OOM records via `journalctl -k` for the boot;
killed pid 229719 (port 4323).
