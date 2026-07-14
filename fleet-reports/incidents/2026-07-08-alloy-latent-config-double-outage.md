# Incident Digest — The 18-day config time bomb and the double outage behind "no stats", 2026-07-08

*A config error merged on June 17 did nothing for eighteen days — because the
running collector silently rejected the reload and kept its old config in
memory. Then the container cold-started, read the broken file for the first
time, and crash-looped into a three-day metrics blackout. And when the fix was
ready, the GitOps pipeline couldn't deploy it: its validator ran inside the
very container that was crash-looping.*
Compiled 2026-07-13 by Home Claude from local session transcripts in
`~/.claude/projects/` (harvested by the `/incident-digest` full-history scan).
All times **America/New_York (EDT, UTC-4)**; raw transcript timestamps are UTC.

---

## TL;DR

"Hey I have no stats in grafana. troubleshoot please" turned out to be **two
independent outages that happened to overlap**. The big one: the central Alloy
collector on LXC 105 had been down since **07-05 01:02** — a stop-then-SIGKILL
(exit 137, *not* OOM), never restarted because its policy is `unless-stopped`
and the GitOps timer only acts on *config drift*, not container health. The
reason it couldn't come back: **drosera PR #76** (merged 06-17) had wrapped the
Home Assistant token secret in `string.trim_space()` — invalid in Alloy — and
the running container had **silently rejected the live reload and kept its
pre-#76 in-memory config for 18 days**. It looked healthy precisely because it
was ignoring the broken config it would die on. The cold start finally read it
→ crash loop. Ten of sixteen metric jobs vanished for ~3.6 days (every job
LXC 105 pushes: blackbox probes, the HA scrape, central node targets). The
second outage, found only after metrics recovered: the Firewalla's Fluent Bit
tail inputs had frozen on 07-06, silently starving the log side for ~2 days —
fixed with one restart.

1. **The time bomb** — #76's invalid config, armed 06-17, silent for 18 days,
   detonated by a cold start on 07-05.
2. **The blind spot** — GitOps reloads on drift only; a dead container is
   nobody's job to notice. Detection was the operator, 3.6 days later.
3. **The catch-22** — the fix merged (PR **#144**) but GitOps *validated* it by
   running `alloy fmt` **inside the crash-looping container**; the exec failed,
   was read as "bad config," and rolled back — the pipeline structurally could
   not self-heal. Operator-approved manual recovery closed it; filed
   in-session as **drosera#145**.
4. **The second outage underneath** — logs dark since 07-06 via an unrelated
   Fluent Bit wedge; same silence, separate cause.

The damage was **~3.6 days of metrics and ~2 days of logs — observability
only**; the fix was two restarts and a one-line revert. The lessons are about
**validating configs where they'll actually be read, and giving liveness a
owner** — a reload that silently fails is a time bomb with no countdown
display.

---

## Timeline (EDT)

| Time | Event | Ground truth |
|---|---|---|
| 06-17 | **PR #76** merges: "trim trailing newline from ha_token" — wraps a secret in `string.trim_space()`, which Alloy forbids (*"secrets may not be converted into strings"*). The live SIGHUP reload **fails silently**; the container keeps running its pre-#76 in-memory config | merged 06-17T23:31Z; config history |
| 06-17 → 07-05 | Eighteen days of apparent health: every later GitOps pull "succeeds," the box runs a config that no longer exists on disk | gitops journal |
| **07-05 01:02** | Container stopped — clean shutdown then SIGKILL at the stop timeout (exit 137; **not** OOM — 69 MB of 2 GB used; initiator never established). `unless-stopped` policy honors the stop; an LXC reboot on 07-07 doesn't resurrect it. Cold start would now read the broken config → **crash loop / down**. `count(up)` drops 16 → 6 (the 6 survivors are host-local push agents; the 10 lost are everything LXC 105 pushes) | container state + logs; Mimir `count(up)` step change |
| 07-06 (20:21 UTC) | *Separate fault:* last Firewalla log line reaches Cloud Loki — Fluent Bit's tail inputs freeze (offset DBs stop advancing) while Zeek keeps writing. No errors, no delivery | Loki last-entry; offset-DB mtimes |
| **07-08 14:58** | Operator: *"hey I have no stats in grafana. troubleshoot please"* | transcript first prompt |
| 14:58–14:59 | Container found dead 3 days; GitOps blind spot named (*"the gitops timer only reloads on config drift, so a dead container just stays dead"*); restart attempted → **crash-looping on config eval**: `local.file.ha_token.content secrets may not be converted into strings` (line 132) | transcript; container logs |
| 15:02 | Git history is definitive: the wrapper came from #76; `is_secret = true` predates it (#28). Cold-start-vs-reload asymmetry explained | git log on config.alloy |
| 15:04 | Fix decided: keep `is_secret = true`, drop the wrapper. Checked: the token file has **no trailing newline anyway** (#76 solved a non-problem — the repo already mandates newline-free token files); no other secret-through-string cases lurking | on-box file bytes; repo grep |
| **15:06** | **PR #144** merged: *"stop passing the HA token secret through string.trim_space"* | merged 19:06:06Z |
| 15:07 | Safety classifier blocks a forced remote deploy ("troubleshoot please" ≠ write authorization) — correctly. Plan: let the 5-minute GitOps timer self-heal | transcript |
| **15:12** | **The catch-22 fires**: GitOps fetches the fix but validates with `docker exec <container> alloy fmt` — the container is crash-looping, the exec fails, GitOps reads that as *bad config* and **rolls back to the broken one**. The pipeline cannot self-heal by design | gitops journal: "Updating 8c4107d → b448913" then rollback |
| 15:15 | Operator-approved recovery: box forced to the fix commit, container started | transcript |
| 15:16–15:17 | Healthy: zero eval errors, receiver + UI ports listening, WAL replayed. **`count(up)` snaps 6 → 16 instantly**; HA scrape authenticates (proving the untrimmed token was fine all along) | live PromQL |
| 15:18–15:27 | Metrics recovered but **logs still absent** → second outage diagnosed: Fluent Bit tails frozen since 07-07 morning, last delivery 07-06 (20:21 UTC). Two separate outages confirmed | Loki queries; offset DBs |
| 16:56–17:00 | Fluent Bit restarted → offset DBs jump, **2,308 entries across all 7 streams in 10 minutes**. **drosera#145** filed — the GitOps validator catch-22 (Link 3) | transcript; Loki stats |

---

## Link 1 — the silent reload rejection (the time bomb mechanism)

Alloy's live-reload behavior on an invalid config is *reject and continue*:
log a line, keep the old in-memory graph running. Operationally reasonable —
and observationally treacherous: from every outside signal (container up,
metrics flowing, GitOps pulls green), a box running a **dead man's config** is
indistinguishable from a healthy one. The failure didn't wait for a trigger;
it waited for the *first cold start*, which arrived 18 days later via an
unexplained stop. Anything would have done it: a host reboot, an image update,
a power blip.

The sharpest detail: #76 was a fix for a problem that didn't exist. The token
file already had no trailing newline (the repo's own docs mandate generating
it newline-free), so the incident's entire risk was purchased for zero benefit
— belt-and-suspenders where the suspenders strangled the belt.

## Link 2 — liveness had no owner

Three days of `count(up)` sitting at 6/16 raised nothing. The GitOps timer's
contract is *config drift*; the container's restart policy contract is *crash
recovery* (and an explicit stop is not a crash); no alert watched the metric
that plainly showed the step change. Every component honored its contract and
the system as a whole had no one on duty — the same **under-observation**
theme as the registered [07-10 outage](2026-07-10-firewalla-silent-log-outage.md),
two days before that incident began.

## Link 3 — the validator inside the patient

The GitOps deploy gate validates new configs by running `alloy fmt` **inside
the running container**. In the exact scenario where a config fix matters most
— the container is down *because of* the config — the validator cannot run,
its failure is misread as "bad config," and the good fix is rolled back.
The pipeline's own safety mechanism pinned the system in its broken state;
recovery required a human to overrule it. A validator must not depend on the
health of the thing it exists to repair (throwaway container, host binary, or
CI-side check — any of the three breaks the loop).

## What did NOT happen (the reassuring part)

- **No data at rest, config history, or dashboards were harmed.** The repo was
  correct throughout (after #144); the entire incident lived in runtime state.
- **Host-local metrics kept flowing** — 6 of 16 jobs (the push-model agents)
  never blinked, which is also what made the blast radius legible: the outage
  boundary exactly traced "things LXC 105 pushes."
- **The HA token secret was never exposed or mishandled** — `is_secret = true`
  was preserved through the fix; the incident was about *syntax*, not secret
  hygiene.
- **The safety classifier's block was correct behavior**, not friction: a
  troubleshooting authorization doesn't cover forced remote deploys. The
  manual recovery happened with explicit operator approval minutes later.
- **What the loss actually WAS:** ~3.6 days of 10 metric jobs and ~2 days of
  log shipping — gaps in Grafana Cloud history, unrecoverable but bounded.

## CTO lessons — where governance was missing

1. **Validate configs where they will be read.** A CI-side `alloy fmt` /
   config-eval check on every PR touching `config.alloy` would have failed #76
   at review time, eighteen days before it could hurt anything. (The gap that
   makes this systemic: live-reload rejection means a bad merge *passes* every
   runtime signal.)
2. **A reload that fails must say so somewhere that pages.** Alloy logs the
   rejection; nothing forwards it. A config-reload-failure alert (or a GitOps
   step that compares running-config hash to on-disk hash) turns "armed time
   bomb" into a same-day fix.
3. **Liveness needs an explicit owner.** `count(up)` no-data / step-change
   alerting on the collector's own job set — filed in spirit as drosera#150
   after the 07-10 sibling incident; this incident is its second justification.
   The GitOps timer could also cheaply assert "container running" each cycle.
4. **The validator must not live inside the patient** (see Link 3) —
   filed in-session as **drosera#145** (open; the catch-22 remains in the
   gitops script until it lands).
5. **Skepticism toward redundant hardening.** #76 added a transformation "for
   safety" that the system forbade and the data didn't need. A one-line check
   of the actual file bytes would have shown the fix was unnecessary — the
   cheapest of all the counterfactuals in this report.

---

## Appendix — sources

```
Transcript:  ~/.claude/projects/-home-cpitzi-repos-drosera/a692f627-*.jsonl
             (session 2026-07-08 14:58 → ~17:05 EDT)
Ground truth: lentago/drosera PR #76 (merged 06-17T23:31Z), PR #144 (merged
             07-08T19:06Z), issue #145 — via gh; gitops journal on LXC 105
             (fetch → alloy-fmt rollback → recovery); Mimir count(up) 16→6→16;
             Loki last-entry per stream; Fluent Bit offset-DB mtimes
Related:     2026-07-10-firewalla-silent-log-outage.md (cites this as "the
             07-05→08 outage, when metrics were the casualty"); 2026-05-28
             power-outage report (the log-side quiet-death class, first seen)
```
