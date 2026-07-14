# Incident Digest — Power outage → the log shipper's quiet death, 2026-05-28

*The first recorded instance of the fleet's most persistent failure class: a
log shipper that survives the crash but not the recovery — alive, healthy, and
delivering nothing.*
Compiled 2026-07-13 by Home Claude from local session transcripts in
`~/.claude/projects/` (harvested by the `/incident-digest` full-history scan).
All times **America/New_York (EDT, UTC-4)**; raw transcript timestamps are UTC.

---

## TL;DR

An early-morning power outage on 2026-05-28 knocked out both the Firewalla and
the Alloy relay LXC; they recovered at different speeds, and Fluent Bit on the
Firewalla exhausted its `Retry_Limit 3` on in-flight chunks while the relay was
still down — then **went permanently quiet instead of reconnecting** once the
relay came back. Container "Up", Zeek writing fresh logs, zero delivery, zero
errors. The gap was found ~4 hours later by a routine dashboard check, fixed by
one container restart, and hardened the same morning (`Retry_Limit False` —
issue #43, PR #44, deployed to the device by 09:44).

Three links, none of which raised an alarm:

1. **Uncoordinated recovery** — the outage took down sender and receiver
   together; nothing sequenced their comeback (Alloy also needed a WAL-corruption
   auto-repair, restarting twice: 01:26 and 07:49).
2. **Bounded retries on an unbounded outage** — `Retry_Limit 3` converted a
   temporary receiver absence into a permanent sender silence.
3. **No delivery signal** — the only symptom was *absence of data*, which
   nothing watched. Detection was a human asking "check all my grafana dashes
   for data."

The damage was a **~4-hour log gap** (Prometheus metrics stayed healthy — all 9
blackbox probes and all node exporters were green at diagnosis). The lesson is
about **recovery behavior and alerting on absence**, not the outage itself.

**Register significance:** this is the direct ancestor of the registered
[2026-07-10 silent log outage](2026-07-10-firewalla-silent-log-outage.md) — the
same shipper going dark-but-"Up", six weeks later, via a different wedge (a
boot race). The `Retry_Limit False` fix from this incident held (07-10 was not
a retry exhaustion); what recurred is the *class*: the pipeline's only failure
signal is silence, and silence wasn't monitored then either.

---

## Timeline (EDT)

| Time | Event | Ground truth |
|---|---|---|
| early AM | Power outage hits the house; Firewalla and pve3 (hosting the Alloy LXC) go down and come back | operator report; Alloy container logs |
| 01:26, 07:49 | Alloy restarts twice — second start follows a WAL-corruption repair | container logs (05:26/11:49 UTC) |
| ~AM | Fluent Bit on the Firewalla retries its in-flight chunks against the still-down relay, exhausts `Retry_Limit 3`, and stops sending — permanently. Container stays "Up"; Zeek keeps writing | on-box inspection later that morning |
| 09:27 | Session starts: *"check all my grafana dashes for data"* — a routine audit, not an outage report | transcript first prompt |
| 09:29 | Loki: 99k `zeek_dns` entries in the 7-day window, **nothing in the last hour**. Prometheus side fully healthy (9/9 probes, all node exporters) | live queries |
| 09:33 | Operator: *"yes. there was a power outage here this morning, so I presume some component in the chain didn't recover"* | transcript |
| 09:34–09:36 | Chain walked: pve3 → LXC → Alloy (up, listening) → Firewalla (no TCP connection to the relay). Zeek log mtimes fresh to the second; Fluent Bit silent 10+ minutes | on-box checks |
| 09:36 | **Fluent Bit container restarted** — reconnects immediately | `docker restart` |
| 09:39 | All four streams flowing again (375 dns / 312 conn / 177 ssl / 142 acl in 2 min). Root cause stated: `Retry_Limit 3` exhaustion during the receiver's absence | live Loki queries |
| 09:41 | Issue **#43** filed (bounded retry → permanent quiet death) | firewalla-axiom-pipeline#43 |
| 09:42 | PR **#44** — `Retry_Limit False` (unbounded retry with backoff) — opened, auto-merge armed; merged 09:42 | merged 2026-05-28T13:42:39Z |
| 09:43–09:44 | Surgical deploy of the one changed file to the device + container restart; streams verified flowing | transcript |
| 09:47 | Issue **#45** filed: GitOps auto-deploy for the device config (poll/validate/reload/rollback), so repo fixes stop requiring hand deploys | firewalla-axiom-pipeline#45 |
| 12:25 | GitOps loop built, deployed, and validated on the device — measured config-change-to-live wall clock: **2 seconds** | transcript (16:25 UTC) |

---

## The failure — bounded retries meet an unbounded outage

Fluent Bit's Loki output was configured with `Retry_Limit 3`. During normal
operation that's invisible; during a power event where the *receiver* is also
recovering, it's a time bomb: the sender burns its three retries in seconds
against a dead socket, marks the chunks failed, and — critically — **enters a
quiet state it never leaves**. When Alloy came back, nothing on the Firewalla
side tried again. The container stayed "Up" (nothing crashed), Zeek stayed
busy (nothing upstream broke), and the pipeline reported no errors (its erroring
was over).

> 09:36 — "Zeek is actively writing logs (mtime = now), but fluent-bit has been
> silent for 10+ minutes. The container's stuck post-outage even though
> connectivity is restored. Restarting it."

The fix (`Retry_Limit False`) makes retries unbounded with exponential backoff:
a receiver outage of any length becomes a delivery *delay*, not a delivery
*death*. It merged and reached the device within minutes because the deploy was
done surgically; the same morning's follow-up (#45) then built the GitOps loop
so future config fixes deploy themselves.

## What did NOT happen (the reassuring part)

- **Metrics were never affected.** All blackbox probes and node exporters were
  green throughout — the outage-recovery gap was confined to the log pipeline.
- **No data was lost at the source.** Zeek kept writing locally the whole time;
  what was lost was ~4 hours of *shipped* history in Loki (the local rotation
  window still held the raw logs at diagnosis time).
- **No config or state damage.** The power outage itself corrupted nothing that
  mattered: Alloy's WAL auto-repair worked, and every host came back on its own.
  Recovery on the pipeline was one `docker restart`.
- **The fix loop closed same-day**, including hardening (unbounded retry) and
  infrastructure (GitOps deploy) — this wasn't left as a known sharp edge.

## CTO lessons — where governance was missing

*Written with six weeks of hindsight, which is exactly what makes this one
worth registering: two of the three lessons were re-learned the hard way on
07-10.*

1. **Retry policy is recovery policy.** Any bounded retry on a shipper whose
   peer can be co-victim of the same outage converts transient failures into
   permanent silence. Fixed here (#43/#44) and it held.
2. **Alert on absence.** The failure emitted no errors; only missing data. No
   ingest-gap alerting existed on 05-28 — and none existed on 07-10 either,
   when the same silence lasted three days. The no-data alerting eventually
   filed as drosera#150 is the systemic close for this class; this incident is
   its earliest justification.
3. **Power events need a recovery audit, not an assumption.** Every component
   individually "came back"; the *pairing* didn't. A post-outage checklist
   (or the same no-data alerts) turns "I presume some component didn't recover"
   into a page.

---

## Appendix — sources

```
Transcript:  ~/.claude/projects/-home-cpitzi-repos-homelab-observability/1474ec79-*.jsonl
             (session start 2026-05-28 09:27 EDT)
Ground truth: firewalla-axiom-pipeline (now lentago/betula) issue #43, PR #44
             (merged 2026-05-28T13:42:39Z), issue #45 (GitOps deploy);
             live Loki/Prometheus queries quoted in-session
Related:     2026-07-10-firewalla-silent-log-outage.md (same failure class, later
             wedge); betula#86 (delivery-liveness healthcheck)
```
