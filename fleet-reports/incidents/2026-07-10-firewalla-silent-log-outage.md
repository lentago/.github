# Incident Digest — Firewalla log shipping went silently dark for three days, 2026-07-10→13

*A CTO's-eye retrospective on an outage with no error message: the log shipper
that looked healthy for three days while delivering nothing, and the watchdog
that couldn't see it.*
Compiled 2026-07-13 by Drosera Claude from firsthand session activity (a single
local session — the dashboard data-completeness sweep that found the outage),
cross-checked against on-box state, Grafana Cloud query results, and git/GitHub
ground truth. All times **America/New_York (EDT, UTC-4)**. (Loki timestamps and
container logs are UTC in the source; converted here.)

**Deployment-caused:** unknown

---

## TL;DR

The Firewalla's Fluent Bit log shipper delivered **zero log lines to Grafana
Cloud Loki for three days** (2026-07-10 17:58 → 2026-07-13 19:58 EDT) while its
container showed "Up" and healthy — three drosera dashboards (network-overview,
dns-security, traffic-devices) were completely dark and nobody noticed until a
routine dashboard audit. A second, unrelated feeder — the device-inventory
publisher that resolves LAN IPs to device names — had already been dead for
**nine days** (since 2026-07-04), also silently. Both were found in one sweep,
diagnosed in ~15 minutes, and fixed in ~20 (a container restart and an
idempotent redeploy).

The failure had three independent links, none of which produced a single error:

1. **Boot race** — a Firewalla reboot started the Fluent Bit container before
   Zeek's log spool existed; the bind-mounted tails watched dead paths from
   then on. No errors, no deliveries.
2. **Watchdog blind spot** — the existing 5-minute healthcheck detects *error
   output*; a silent stall emits none. It had correctly restarted the container
   that same morning on a burst of Loki HTTP 500s, then sat silent through
   three days of total non-delivery.
3. **Crontab regeneration** — Firewalla's FireMain regenerated the pi user's
   crontab and wiped the device-inventory publisher's entry; the `post_main.d`
   hook installed specifically to survive that did not restore it.

The damage was **~74 hours of unrecoverable Zeek DNS/conn + ACL history and
three days of dark dashboards**, not config, state, or security posture. The
lesson is about **alerting on absence** — a pipeline whose only failure signal
is silence needs a delivery-liveness check, because "no errors" and "working"
are not the same claim.

---

## Timeline (EDT)

| Time | Event | Ground truth |
|---|---|---|
| 07-03 13:48 | device-inventory publisher deployed to the Firewalla (hourly cron at :17, plus a `post_main.d` cron-reinstall hook) | file mtimes in `~/.firewalla/run/device-inventory/` |
| **07-04 21:20** | **Publisher's last run.** Sometime after, FireMain regenerated the crontab and wiped the entry; the reinstall hook never brought it back. Stream dead, silent. | `publish.log` last line; last Loki entry still carries the pre-migration `cluster="homelab"` label |
| 07-09 | betula **#82** merged — Axiom output removed; **Grafana Cloud Loki becomes the sole log destination** | commit `1fdc079` |
| 07-10 13:00 | Healthcheck correctly restarts Fluent Bit on a Loki HTTP-500 burst — the error-based detection working as designed | `fluent-bit-healthcheck.log`: "100% error rate (2/2 lines) — restarting" |
| 07-10 17:58 | Last `zeek_dns` / `zeek_conn` / `firewalla_acl` entries reach Cloud Loki | Loki last-entry queries |
| **07-10 ~18:00** | **Firewalla reboots.** `post_main.d/start_log_shipping.sh` starts the container before Zeek's spool (`/bspool/manager`) is live; the tails bind to dead paths. Zero deliveries, zero errors, from here on. | box uptime 3d 1:49 at diagnosis; container "Up 3 days"; startup banner is the only container log output |
| 07-10→13 | Three dashboards fully dark, two office-display panels dark. Healthcheck silent (nothing to detect). No ingest-gap alerting exists. | — |
| 07-13 ~19:42 | Routine dashboard data-completeness sweep begins: all 8 drosera dashboards, 132 panel queries replayed against live Mimir/Loki/CloudWatch | this session |
| 19:45 | All four Firewalla log streams: **zero entries in 24 h**. Metrics side fully green (6/6 nodes, 9/9 probes). | `query_loki_stats` per stream |
| 19:47–19:55 | Root causes pinned: tail offset DBs frozen at pre-reboot mtimes while Zeek writes fresh to the second; publisher script/env/hook intact on disk but crontab line gone; the Alloy relay it pushes through verified alive end-to-end with a test line (accepted HTTP 204, landed in Cloud Loki seconds later) | on-box inspection; test push |
| **19:58** | **Operator restarts `fluent-bit-axiom`** → all eight offset DBs move instantly; streams resume within a minute (199 dns / 71 conn / 37 acl entries in the first 5 min) | offset-DB mtimes; Loki stats |
| 20:04 | `deploy-device-inventory-publisher.sh` re-run; cron + hook reinstalled; dry run clean (225 records from 166 devices) | deploy output; DRY_RUN payload |
| 20:17 | First cron push of the restored publisher lands — 227 records from 166 devices, all confirmed in Cloud Loki | `publish.log` HTTP 204; Loki stats |
| 20:25 | **betula#86** filed — boot-race fix + delivery-liveness healthcheck | issue link below |

---

## Link 1 — the boot race (the headline event)

**07-10 ~18:00.** The Firewalla rebooted. Its `post_main.d/start_log_shipping.sh`
hook did its job — waited for Docker, started the container — but nothing waits
for **Zeek**. The container's bind mount (`/bspool/manager → /logs/zeek`)
captured a directory that Firewalla's own stack subsequently replaced, so every
tail input watched a dead path indefinitely.

The evidence that makes this diagnosis airtight, three days later:

- Tail offset DBs under `~/.firewalla/config/fluent-bit-data/*.db` frozen at
  17:17–17:54 on 07-10 — **not one write since boot** — while
  `/bspool/manager/*.log` carried mtimes fresh to the second.
- Container logs: the startup banner and nothing else. `Log_Level warn` plus a
  failure mode that never errors = a shipper that is indistinguishable from
  healthy unless you look at *delivery*.
- A plain `docker restart` at 19:58 on 07-13 — with the spool now live —
  recovered everything within a minute. No offset-DB surgery needed. The inputs
  weren't corrupted; they were pointed at nothing.

## Link 2 — the watchdog that watches for the wrong signal

betula ships a `fluent_bit_healthcheck.sh` (5-minute cron) that restarts the
container when it's stopped or its recent output is all errors. It is not
decorative: at **13:00 on 07-10** — five hours before the reboot — it caught a
Loki HTTP-500 burst and restarted the container, correctly.

> `2026-07-10 13:00:03 [healthcheck] WARNING: 100% error rate (2/2 lines) — restarting`

Then the boot race produced a failure with **no error output at all**, and the
healthcheck logged nothing for three days — behaving exactly as designed, and
exactly wrong. Error-rate detection answers "is it complaining?"; the question
that mattered was "is it delivering?". Nothing in the stack asked that question:
not the healthcheck, and not Grafana Cloud (no alert existed on ingest gaps for
the log streams — detection was a human running a dashboard audit for unrelated
reasons).

## Link 3 — the crontab that regenerates itself

The device-inventory publisher (drosera's `scripts/device-inventory-publisher/`,
deployed to the Firewalla, hourly cron) stopped running after **07-04 21:20** —
its `publish.log` simply ends there, with the script, env file, and reinstall
hook all still on disk. FireMain regenerates the pi user's crontab on restart;
the deployment anticipated exactly this with a `post_main.d` reinstall hook, and
the hook failed to do its one job (root cause not yet established — tracked as
follow-up). Nine days of the `device_inventory` stream missing meant the
DNS/traffic dashboards' device-name joins showed bare IPs.

A detail that sharpened the diagnosis: the stream's last entries still carried
the pre-migration `cluster="homelab"` label — it died *before* the 07-04 label
migration finished rolling out, which immediately dated the failure and
separated it from Link 1.

---

## What did NOT happen (the reassuring part)

*Mandatory blast-radius bounding. For a three-day silent outage, the negatives
are substantial.*

- **The metrics pipeline was unaffected throughout.** All node_exporter, blackbox
  probe, and Home Assistant metrics stayed green the entire window — host-down
  visibility and the infra-health/neptune-nas/office-display metric panels never
  blinked. (The mirror image of the 07-05→08 outage, when metrics were the
  casualty.)
- **The Firewalla's actual security functions were unaffected.** Zeek kept
  capturing and ACL enforcement kept enforcing the whole time — locally. Only
  the *shipping* of those records off-box was dark. Observability was blind;
  the network was not.
- **No config, state, or data-at-rest was lost.** The betula config on the box
  was intact and correct; recovery was one `docker restart` plus one idempotent
  deploy-script re-run. No repo drift, no dashboard changes needed — every
  panel query was correct; the data feeds were the problem.
- **Removing Axiom (betula#82) did not cause or worsen the loss.** Both outputs
  rode the same container and the same wedged tail inputs — a dual-destination
  setup would have gone dark identically. (It did, however, remove the second
  copy going forward: Loki is now the sole destination, so a shipping outage is
  a *total* loss window. Accepted trade-off, now an explicit one.)
- **What the loss actually WAS:** ~74 h of Zeek DNS/conn and ACL history
  (unrecoverable — the rotated logs aged off the box), nine days of device-name
  staleness, and three days of dark dashboards. No credentials, no enforcement,
  no hardware, no other host involved.

---

## What went right (worth keeping)

- **Dashboards-as-code made the audit mechanical.** Because every dashboard is
  JSON in the drosera repo, "scan all our dashes for missing data" decomposed
  into extracting all 132 panel queries and replaying them against the live
  datasources — full coverage, not spot checks. The outage was found by
  coverage, not luck.
- **The 07-05→08 outage's runbook memory paid for itself.** The prior incident's
  triage map ("two independent pipelines; check which one") pointed at the
  Fluent Bit shipper immediately — and flagged the stale README description
  (retired Promtail→Alloy relay) that would otherwise have misdirected the
  investigation.
- **Verify the path before redeploying the feeder.** A test line pushed through
  the Alloy relay end-to-end (accepted on-box, observed in Cloud Loki seconds
  later) proved the delivery path *before* the publisher redeploy — so the fix
  was known-good, not fix-and-hope.
- **Recovery was minutes once detected.** Both remediations were boring:
  restart, re-run an idempotent deploy script. The 3-day cost was entirely in
  *detection*, which is what every lesson below targets.

---

## CTO lessons — where governance was missing

*Systems lessons, not blame. Each is the gap + a concrete fix, offered as a
filable issue.*

1. **Alert on absence, not just errors.** Every failure in this incident was
   silent; every existing safeguard listened for noise. Grafana Cloud should
   carry no-data alerts on the critical log streams (`zeek_dns`, `zeek_conn`,
   `firewalla_acl`, `device_inventory`) — a 30–60 min ingest gap should page,
   turning a 3-day detection into a 30-minute one. → **drosera#150**
2. **Start-ordering and delivery-liveness for the shipper.** The container must
   wait for a *fresh* Zeek spool before starting, and the healthcheck needs a
   delivery signal (Zeek writing but offset DBs frozen → restart) alongside its
   error-rate check. → **betula#86** (filed during the incident)
3. **A regenerating crontab is not a home for load-bearing state.** The
   reinstall hook failed silently and nothing verified the publisher was still
   running. Either make the hook verifiable (log + alert on failure), have the
   publisher's absence caught by lesson 1's no-data alert, or move scheduling
   off the appliance entirely. Root-cause the hook failure first. → **drosera#151**
4. **Doc drift misleads triage under pressure.** drosera's README/CLAUDE.md
   still describe the retired "Promtail → Alloy :3100 relay" architecture for
   Zeek logs; the correct current map lived only in session memory. Update the
   docs to the direct-to-Loki reality (and note device_inventory as the one
   remaining relay user). → **drosera#152**

Distinct from both prior incidents in the register: 06-19 was concurrency
(sessions crossing), 07-12 was over-reach (one pipeline doing something
destructive). This one is **under-observation** — infrastructure that fails
without a signal, watched by monitors tuned to signals. The governance theme is
the same fail-closed instinct pointed at a new surface: *silence must be a
detectable state.*

---

## Appendix — sources

Firsthand single-session diagnosis (no transcript harvest needed). Evidence
gathered and cross-checked live:

```
Grafana Cloud:  query_loki_stats / last-entry queries per stream; instant PromQL
                sweeps (up, probe_success, HA sensors) proving metrics unaffected
On-box:         container status + logs, tail offset-DB mtimes vs /bspool/manager
                mtimes, publish.log, fluent-bit-healthcheck.log, crontab -l,
                post_main.d contents, box uptime
Repos:          betula git log (#82 remove-Axiom, 1fdc079); drosera dashboards/*.json
                (132 queries extracted); deploy script output
Filed:          betula#86 (boot race + delivery-liveness healthcheck);
                drosera#150 (no-data alerts), #151 (cron hook), #152 (doc drift)
```
