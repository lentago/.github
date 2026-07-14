# Incident Digest — The 22-day silent restart loop and the crontab that ate the appliance, 2026-07-02

*One maintenance session on the Firewalla pipeline surfaced two independent
root causes: a healthcheck that had been force-restarting a healthy container
every five minutes for 22 days, and a cron installer that silently replaced the
appliance's entire system crontab — whose downstream casualties (a dead Zeek
worker that never self-healed, a full log tmpfs, a dead ACL feed) unfolded live
during the session. Plus one self-inflicted wound on the way to fixing it.*
Compiled 2026-07-13 by Home Claude from local session transcripts in
`~/.claude/projects/` (harvested by the `/incident-digest` full-history scan).
All times **America/New_York (EDT, UTC-4)**; raw transcript timestamps are UTC.

---

## TL;DR

A routine "work the top three priority issues" session in the
firewalla-axiom-pipeline repo (now `lentago/betula`) turned into a 14-hour
incident chain. Fault line A: the pipeline's healthcheck ran bare `docker`
under cron, where the `pi` user has no docker socket — every check errored,
was misread as "container not running," and **force-recreated the Fluent Bit
container every 5 minutes, around the clock, for ~22 days** (6,385 restart
events since ~June 10), invisibly, while data kept flowing. Fault line B: the
repo's cron installer ran raw `crontab user_crontab`, which **replaces the
entire crontab** — the 11:29 GitOps apply of an unrelated PR silently deleted
every Firewalla *system* cron job, including `/alog` log rotation and Zeek's
crash-recovery cron. The consequences then arrived on schedule: a Zeek worker
died at 15:03 and stayed dead (its resurrection cron was gone), and `/alog`
filled to 100% by late evening, killing the ACL log feed mid-write. On the way
to fixing B, an operator-approved command run with `sudo` (the script expects
to run as `pi`) wiped `pi`'s crontab entirely — Claude's words: *"My fault on
the `sudo`"* — before the full 70-line crontab (system + pipeline entries) was
restored via Firewalla's own merge-based installer.

1. **Fault line A — the invisible restart loop**: healthcheck false positive
   ×6,385 over 22 days → issues #61/#65, PRs #62/#66.
2. **Fault line B — the crontab clobber cascade**: installer replaced the
   system crontab → Zeek non-recovery + `/alog` ENOSPC + dead ACL feed →
   issue #67 (CRITICAL), PR #68 (merge-based install).
3. **The operator error inside B**: a `sudo` mis-run left `pi` with *no*
   crontab for ~3 minutes before full restore.

The damage was **observability-side only and fully recovered same-session**;
Firewalla's routing, DNS, DHCP and enforcement never blinked. The lessons are
about **silent failure modes and appliance-state stewardship** — a guest
process on someone else's appliance must merge, never replace.

---

## Timeline (EDT)

| Time | Event | Ground truth |
|---|---|---|
| ~Jun 10 | Healthcheck begins force-recreating the Fluent Bit container every 5 minutes (bare `docker ps` under cron errors → "not running") — no visible symptom | 6,385 `container_not_running` events in the metric history |
| 07-02 11:15 | Session starts: *"work the top three priority issues to completion. Dispatch to bullpen where appropriate."* | transcript first prompt |
| 11:25–11:28 | Four planned PRs merge (#57–#60: docs, log rotation, new Zeek sources) | betula PRs, merged 15:25–15:28Z |
| **11:29** | **GitOps applies #59's crontab change via raw `crontab user_crontab` — every Firewalla system cron job is silently deleted** (log rotation, process watchdogs, Zeek crash-recovery, scheduled reboot). Nothing notices | `/alog` rotation `.gz` history stops 11:29; crontab inspection at 22:52 |
| 15:03 | Zeek's `br0` traffic worker dies (manager+logger stay up). The crash-recovery cron that would have restarted it no longer exists. Zeek log streams go quiet | `.status` + process list; Loki stream gap |
| 15:42 | **Fault line A found**: healthcheck has been restarting the container every 5 min for ~22 days. Issue **#61** filed; fix dispatched to the bullpen | betula#61 |
| 16:50 | `brofish` (Zeek) restart recovers workers on br0/br1/wg0 — and recreates `/bspool/worker-*`, **destroying the dead worker's `stderr.log`** (*"we destroyed the evidence"*) | transcript 21:11Z |
| 16:52 | PR **#62** (healthcheck: `sudo docker`) merged | merged 20:52Z |
| 16:55 | Final restart-loop kill — which incidentally heals a stale ("ghost") bind mount from the recreated Zeek spool | transcript |
| 17:00 | **First silent healthcheck cycle in 22 days.** All eight log sources flowing | transcript 21:03Z |
| 17:06 | Axiom canary monitor armed: "Zeek DNS silence (br0 worker canary)" — fires on 15 min of zero `zeek_dns`, alert-on-no-data, incident playbook embedded in the description | monitor config |
| 17:31 | PR **#64** (host+Zeek process metrics exporter) merged; its cron then fails every 5 min because the old GitOps copy-list never copied the new script — found and fixed inline | merged 21:31Z |
| 21:56 | Issue **#65** → PR **#66** merged: second healthcheck false-positive branch ("no output in 5m" restarted a *healthy* container every 10 minutes) | merged 07-03 01:56Z |
| 22:51 | ACL feed dead: rsyslog target file frozen mid-line while the kernel ring buffer flows. **`/alog` tmpfs is 100% full (20M/20M)** — the ENOSPC signature — because its rotation cron died at 11:29 | on-box df + file inspection |
| 22:53 | Full fault-line-B chain confirmed: pi's live crontab contains **only the seven pipeline entries**; all system jobs gone since 11:29, Zeek crash-recovery cron among them — retroactively explaining why the 15:03 worker death stayed dead | crontab -l |
| **23:06** | **The wound**: restore attempt run with `sudo` — the script expects to run as `pi` — fails `Permission denied` handing over its temp file and **leaves `pi` with no crontab at all**, pipeline entries included. *"My fault on the `sudo`"* | transcript 03:06Z |
| 23:09 | **Crontab fully restored — 70 lines** (all Firewalla system jobs + pipeline entries) via Firewalla's own `update_crontab.sh` merge path | transcript 03:09Z |
| 23:12 | Issue **#67** filed — *"CRITICAL: raw `crontab user_crontab` install clobbers Firewalla's system cron jobs"* — and dispatched | betula#67 |
| 23:17 | Restored rotation cron frees `/alog`; rsyslog resumes; **ACL feed self-heals** (793 events in 15 min) | Loki/Axiom queries |
| 23:25 | PR **#68** merged: installer now merges via `update_crontab.sh` instead of clobbering | merged 07-03 03:25Z |

---

## Fault line A — the watchdog that cried wolf 6,385 times

`fluent_bit_healthcheck.sh` line 69 ran bare `docker ps`. Interactively that
works (the operator's shell has group access); under cron as `pi` it fails —
and the script treated *command failure* as *container absence* and
force-recreated the container. Every five minutes. For 22 days. The reason
nobody noticed is the same reason it kept happening: recreation is fast, the
tail inputs resume from offset DBs, and the pipeline kept delivering — a
restart loop with no user-visible symptom, discoverable only in the
`health_check_restart` metric nobody had reason to look at.

Two fixes, because there were two false-positive branches: #62 (`sudo docker`
for the socket-access branch, same day) and #66 (the "no output in 5 minutes"
branch that bounced a *healthy but quiet* container every 10 minutes). The
deeper class — a healthcheck whose failure mode is *more restarts* rather than
*an alert* — is the same "watchdog watching the wrong signal" theme that
returned in the registered [07-10 outage](2026-07-10-firewalla-silent-log-outage.md).

## Fault line B — `crontab` replaces; it does not append

The repo's cron installer did `crontab user_crontab` — which **replaces the
invoking user's entire crontab** with the file's contents. On a stock host
that's merely rude; on the Firewalla, where the vendor's own stack schedules
its process watchdogs, log rotation, Zeek crash-recovery, and even a periodic
maintenance reboot through that same `pi` crontab, it's a slow-acting poison.
The 11:29 GitOps apply of #59 (itself an innocuous log-rotation PR) executed
the clobber; the appliance then degraded on a schedule set by whichever
deleted job was needed next:

- **15:03** — a Zeek worker crash that would normally self-heal within minutes
  became a multi-hour log outage, because the crash-recovery cron was gone.
- **~22:30** — `/alog` (a ~20 MB tmpfs) filled because `clean_log.sh` (every
  10 minutes, vendor-scheduled) was gone; rsyslog died mid-write with the
  classic partial-line ENOSPC signature, killing the ACL feed.

The elegant part of the diagnosis: the `.gz` rotation history under `/alog`
**stops at exactly 11:29** — the clobber timestamped its own crime scene.

The fix (#68) adopts Firewalla's own `update_crontab.sh`, which reads
`~/.firewalla/config/user_crontab` and *merges* user entries with system jobs —
as the session put it, *"our repo has been one wrong install command away from
correct all along."*

### The wound inside the fix

At 23:06, restoring the crontab, the restore command was run with `sudo` — but
Firewalla's tooling expects invocation as `pi` and does its own privilege
handling; root couldn't hand the temp file to `pi`'s crontab and the result was
**no crontab at all** for about three minutes (pipeline entries included).
Self-assessed in the moment — *"My fault on the `sudo`"* — and corrected by
re-running as `pi`. Cost: three minutes of no scheduled jobs and one honest
confession. Worth registering because it's the operator-error shape that
recurs: **on an appliance, the vendor's context (user, env, privilege model)
is part of the API.**

### Evidence destroyed en route

The 16:50 `brofish` restart recreated the Zeek spool directories — deleting
the dead worker's `stderr.log` before anyone read it. The *why* of the 15:03
worker death is therefore a reasoned verdict, not a proven one. The corrective
is now embedded in the canary monitor's own description: *next time, copy
`/bspool/worker-*` before restarting.*

## What did NOT happen (the reassuring part)

- **The Firewalla's core functions never degraded.** Routing, DNS, DHCP, ACL
  *enforcement*, and Zeek *capture* all ran throughout — every casualty was in
  the shipping/observability layer. The one riskier moment (a `brofish`
  restart) cycles only the monitoring daemon, ~30 s, no forwarding impact.
- **No data loss beyond bounded log-stream gaps** (Zeek streams ~15:03–16:50;
  ACL feed ~22:30–23:17), and the local capture side held the raw material.
- **The 22-day loop lost nothing** — its restarts were fast enough that
  delivery continued; the cost was risk exposure and 6,385 pointless container
  recreations, not a gap.
- **Every fix landed as code the same session** — four issues (#61, #65, #67,
  plus the copy-list gap fixed inline), four merged PRs (#62, #66, #68, #64),
  one canary monitor. Nothing was left as a hand-applied patch for the next
  GitOps run to revert.

## CTO lessons — where governance was missing

1. **A guest on an appliance must merge, never replace.** Raw `crontab <file>`
   on a vendor-managed box is a destructive write to shared state. Use the
   vendor's merge mechanism (`update_crontab.sh` + `user_crontab`) — now
   enforced by #68.
2. **Healthchecks need a false-positive budget.** A watchdog that acts (restart)
   rather than alerts will do its damage silently; 6,385 events sat in a metric
   nobody watched. Restart counters deserve their own alarm — a healthcheck
   that fires more than N times/day *is* the incident.
3. **Run-context is part of correctness.** Two of the day's three failures were
   context bugs, not logic bugs: `docker` without the cron user's socket
   access, and a `pi`-expecting script run as root. Test scripts in the
   context that will run them (cron env, target user) before deploy.
4. **Preserve the black box before restarting.** The one unanswered question of
   the day (why the Zeek worker died) is unanswered because recovery destroyed
   the evidence. Copy crash artifacts first; restart second — now in the
   canary-monitor playbook.

---

## Appendix — sources

```
Transcript:  ~/.claude/projects/-home-cpitzi-repos-firewalla-axiom-pipeline/54d0b5be-*.jsonl
             (session 2026-07-02 11:15 EDT → 07-03 ~00:30 EDT; includes an
             out-of-context continuation summary at 15:35)
Ground truth: lentago/betula issues #61, #65, #67; PRs #57–#60, #62, #64, #66,
             #68 (merge timestamps via gh); health_check_restart metric history
             (6,385 events); on-box crontab/df//alog inspection quoted in-session
Related:     2026-07-10-firewalla-silent-log-outage.md (Link 3 there — FireMain
             crontab regeneration — is the same "crontab is not durable state"
             surface from the other direction)
```
