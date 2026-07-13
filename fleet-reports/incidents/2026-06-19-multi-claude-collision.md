# Incident Digest — Multi-Claude Collision, 2026-06-19

*A CTO's-eye retrospective on the day control of the product went distributed.*
Compiled 2026-06-20 by Home Claude from local session transcripts in
`~/.claude/projects/`. All times **EDT**. Transcript timestamps are UTC in
the raw files; converted here.

---

## TL;DR

On Jun 19 you had **as many as four local Claude Code sessions running at
once** (≈10:50–13:55) plus the **three-worker headless fleet** churning in the
background. They didn't share a *working copy*, so **no local commits were lost
and no working tree was corrupted** — every local merge was a clean
fast-forward. The crossing happened one layer up, at the **shared
orchestration surfaces**:

1. **One shared GitHub repo, multiple authors** — a local session and the
   fleet bot both opened PRs against the *same Grafana panel* and the *same
   files*, on top of each other.
2. **One shared job queue, multiple producers** — a "fire 10 test jobs"
   session and a "run a real audit job" session both pushed work onto the same
   three runners, and a babysitter watcher hung on a job it didn't own.
3. **One repo, sequential sessions, dangling state** — `professional-endeavors`
   got handed between three sessions that each left the repo parked on a
   feature branch for the next one to find.

The damage was **wasted/abandoned work and confusion**, not data loss. The
lesson is about **governance of concurrency**, not recovery.

---

## The cast — 9 sessions on Jun 19

| # | Time (EDT) | Session | Repo / cwd | Given mission (first prompt) |
|---|---|---|---|---|
| 1 | 08:34–23:11 | `de0f122f` | `reference-checker` | "harvest the issues list and refine against current product state. Prioritize and list." |
| 2 | 09:18–15:23 | `2d342763` | `homelab-observability` | "file an issue to show on the 'runners underway' pane which model is running" |
| 3 | 09:47–14:34 | `d6448562` | `professional-endeavors` | "refresh the top eight Prospecting companies…" |
| 4 | 10:50–13:55 | `3e25bf3d` | `bullpen` | **"fire off 10 test jobs to the bullpen, of varying models — I am watching the grafana dash"** |
| 5 | 17:28–18:22 | `2d1b9a9f` | `professional-endeavors` | "check the intake" |
| 6 | 21:37–21:42 | `5a724bc0` | `~/Desktop` | "@contacts.csv — deduplicate and merge" |
| 7 | 21:48–22:19 | `c58dd5d2` | `~/Desktop` | "categorize commercial/impersonal vs personal contacts…" |
| 8 | 22:18–23:17 | `3bc3319a` | `professional-endeavors` | "process intake" |
| 9 | 22:41–23:04 | `c3293399` | `~` / `.vscode` | "I have messed up my vscode installation — memory HOG. start over" |

**Peak concurrency: four (sessions 1–4) overlapping ~10:50–13:55**, all of them
indirectly or directly touching the **bullpen fleet** and/or the
**`PitziLabs/bullpen` + `PitziLabs/homelab-observability`** repos.

---

## Collision A — the shared GitHub repos (the headline event)

**Window: ~10:00–13:45 EDT.** Three independent work-streams converged on two
repos. Every fleet PR below was opened by the bot **`app/pitzilabs-claude-runner`**;
the local homelab session (`2d342763`) was simultaneously reviewing, merging,
and *itself authoring* PRs on the same repos.

### The "Runners underway" panel — edited by three streams at once
- Session `2d342763`'s **own assigned task** (09:18) was to annotate the
  *"Runners underway"* Grafana panel with the running model.
- The fleet bot opened **homelab #88** ("rekey 'Runners underway' to count
  in-flight", created 13:00, merged 13:15) **and** **homelab #92** ("key
  'Runners underway' by worker", created 13:39, merged 13:45) — two successive
  PRs reworking the *same panel*, neither authored by the session that "owned"
  it.
- At **13:11** session `2d342763` literally stops and flags it:
  > "what is homelab #87 / PR #88? **(not mine — understand before merging same
  > panel)**"

  → A local Claude discovering that an external agent was editing the exact
  panel it was assigned. This is the cleanest single snapshot of "crossing each
  other's work."

### Stacked-PR clobber — bullpen #19 killed by #17
- Fleet **bullpen #17** ("sub-second Loki timestamps + 10s job_running
  cadence") merged 13:10.
- Fleet **bullpen #19** ("emit job_started one-shot event"), opened 13:07,
  **branched before #17 landed** → went `CONFLICTING / DIRTY`. At **13:15**:
  > "#19 has a **merge conflict** with bullpen's `main` … since #19 branched,
  > #17 landed."
- **#19 was abandoned, never merged.** It was redone from scratch as
  **bullpen #20** (merged 13:45). Net: one PR's worth of agent work thrown away
  to a race it couldn't see coming.

### The bot-PR gate that rejected its own fleet
- At **13:44** session `2d342763` finds a workflow input
  (`allowed_bots`) defaulted to `""`, so the action **"rejected every
  bot-authored PR — and every fleet PR is opened by `pitzilabs-claude-runner`."**
  A governance guardrail mis-configured into a self-inflicted block.

### What the homelab session merged that day
`#14` (cr-submit filename uniqueness), `#15` (pre-seed session id), `#17`
(heartbeat), `#85`/`#88`/`#90`/`#92` (dashboards) — plus it authored its own
**#86** (`ci(terraform): auto-apply dashboards on merge`, by `cpitzi`, merged
12:58). So one local session was the merge-gatekeeper for a stream of PRs the
*fleet* was generating in parallel — a single human-in-the-loop straining to
referee an async crowd.

---

## Collision B — the shared job queue (producers vs. producers)

**Window: ~10:50–14:00 EDT.** Two sessions pushed work onto the **same three
runners** with no coordination.

- Session **`3e25bf3d`** was told (10:50): *"fire off 10 test jobs to the
  bullpen, of varying models."* It flooded the fleet in waves.
- Session **`de0f122f`** had *separately* dispatched a **real ~1-hour
  reference-checker audit job (#3)** to the same fleet, and spent 11:56–13:52
  babysitting it ("runner still actively working it ~1 hour in, lock held").
- The two collided on the runners. At **13:54** `3e25bf3d` reports its
  drain-watcher stalled:
  > "the job that stalled my drain-watcher is an **unrelated, healthy job…
  > not mine, didn't touch it.**"

  → It was reference-checker's job. One session's watcher blocked on another
  session's work, with neither aware of the other.

### The bug the flood was actively triggering
- At **09:49** session `2d342763` had already spotted the latent footgun:
  > "any two same-project jobs submitted within the same second **clobber each
  > other with no error.**"
- Firing "10 test jobs of varying models" rapid-fire (`3e25bf3d`) is *exactly*
  the input that trips that bug. Meanwhile fleet **bullpen #14**
  ("make inbox filenames unique to **prevent collision**") was the in-flight
  fix. The bug was being **stress-tested and patched at the same moment, by
  different sessions, neither coordinating with the other.**
- `2d342763` even self-throttled to dodge it (10:08): *"submit one at a time so
  the two bullpen jobs don't land in the same second and clobber each other"* —
  a Claude manually working around a race another Claude was creating.

---

## Collision C — `professional-endeavors`, the relay-race repo

**Three sequential sessions, same repo, dangling branches handed forward.**
This repo is your single-writer "Career Claude" wiki, and the per-task
branch→commit→merge discipline mostly *held* — but the handoffs were messy.

- **AM (`d6448562`, 09:47–14:34):** at **11:12** it catches itself:
  > "I'm on `main`, and I've been editing there. Per the always-branch rule,
  > let me carry these uncommitted changes onto a feature branch immediately."

  Recovered cleanly (`git switch -c` carried the work over, no commit landed on
  `main`) — but it had started writing to `main` before noticing.
- **Eve (`2d1b9a9f`, 17:28–18:22):** committed the Schwartz/MGH packet (21c2199)
  onto branch `schwartz-center-mgh` and **left the repo parked on that branch,
  unmerged.**
- **Late (`3bc3319a`, 22:18–23:17):** opened the repo and found it **still on
  `schwartz-center-mgh`** (reflog: `22:20:38 checkout: moving from
  schwartz-center-mgh to main`). It had to reconcile the leftover branch before
  doing its own work, then ran **five** more branch/commit/merge cycles
  (britebound→teenvoice recon, teenvoice liveness, freshness pass, Schwartz
  honest rebuild). No data lost, but each session inherited the previous one's
  uncleaned desk.

---

## Evening — mostly clean, sequential

Sessions 6–9 ran late and were largely independent:
- **`5a724bc0` → `c58dd5d2`** (Desktop, 21:37→22:19): contacts dedup, then
  categorize — a deliberate hand-off on `contacts.csv`, sequential, no overlap.
- **`c3293399`** (22:41): the vscode "memory HOG" teardown — unrelated.
- **`3bc3319a`** (22:18): the prof-endeavors late session above.

Only minor overlap: `c3293399` and `3bc3319a` ran concurrently (22:41–23:04)
but in different trees (`~/.vscode` vs `professional-endeavors`) — no crossing.

---

## What did NOT happen (the reassuring part)

- **No lost local commits.** Every local merge on Jun 19 was a clean
  fast-forward; no `reset --hard` or force-push ran against your working trees
  (the `reset --hard` hits in the grep were inside the fleet's *reaper script
  source*, being read, not executed locally).
- **No working-tree corruption.** The four morning sessions were in four
  different cwds; they never wrote the same file on disk simultaneously.
- The losses were **abandoned PR work (#19)**, **redundant panel churn
  (#88 vs #92)**, **a self-inflicted bot-PR block**, and **operator confusion /
  babysitting time** — all recoverable, all avoidable.

---

## CTO lessons — where governance was missing

*Filed as the `governance` cohort on `PitziLabs/bullpen`: #21–#25.*

1. **The shared queue had no ownership or admission control.** → **bullpen #21** Two sessions
   producing jobs onto three runners, plus a 1-hour job hogging a slot, plus a
   same-second clobber bug. *Fix candidates: per-session job namespacing /
   tags, a "who's running what" view before you submit, capacity awareness,
   land the #14 collision fix (done) and add a submit-time dedupe guard.*
2. **The fleet and a human-driven session were both authoring PRs on the same
   repo with no lane separation.** → **bullpen #22** #88/#92 reworked one panel twice; #19 died to
   #17. *Fix candidates: one writer per panel/file at a time; have the fleet
   rebase-before-merge; don't let a local session and the fleet target the same
   open work item concurrently; a board that shows open agent PRs (you have the
   "Open agent PRs" panel — use it as the gate **before** dispatching more).*
3. **Auto-ish PR turnaround outran review.** → **bullpen #23** Several fleet PRs merged 6–15 min
   after creation while you were watching a dashboard, not a review queue. Your
   own standing rule is **no auto-merge — review locally**; Jun 19 shows what
   happens when velocity is set by the fleet instead of by the gate.
4. **Branch hygiene across sessions.** → **bullpen #24** Three prof-endeavors sessions each left
   the repo on a feature branch. *Fix candidate: a session-end "return to main,
   merged or stashed-clean" checklist; or always dispatch repo work through the
   fleet (clean checkout per job) rather than hand-editing across sessions.*
5. **No single pane of "what is every Claude doing right now."** → **bullpen #25** Each session
   repeatedly had to *discover* the others ("not mine", "same panel", "didn't
   touch it"). That discovery cost is the real tax of un-governed concurrency.

---

## Appendix — source transcripts

```
~/.claude/projects/-home-cpitzi-repos-reference-checker/de0f122f-….jsonl
~/.claude/projects/-home-cpitzi-repos-homelab-observability/2d342763-….jsonl
~/.claude/projects/-home-cpitzi-repos-professional-endeavors/d6448562-….jsonl
~/.claude/projects/-home-cpitzi-repos-bullpen/3e25bf3d-….jsonl
~/.claude/projects/-home-cpitzi-repos-professional-endeavors/2d1b9a9f-….jsonl
~/.claude/projects/-home-cpitzi-Desktop/5a724bc0-….jsonl
~/.claude/projects/-home-cpitzi-Desktop/c58dd5d2-….jsonl
~/.claude/projects/-home-cpitzi-repos-professional-endeavors/3bc3319a-….jsonl
~/.claude/projects/-home-cpitzi/c3293399-….jsonl
```
Reflogs cross-checked against `PitziLabs/{bullpen,homelab-observability}` PR
history via `gh`.
