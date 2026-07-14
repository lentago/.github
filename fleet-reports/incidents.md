# Lentago Labs Incident Register

> [!NOTE]
> **Co-authored with [Claude](https://claude.ai)** (the `/incident-digest` playbook). A chronological register of incident reports harvested from local Lentago lab activity and published as a periodic fleet report. Each row links to the full write-up under [`fleet-reports/incidents/`](incidents/). Unlike the [fleet report](fleet-report.md), these are published **verbatim** and *do* include homelab-internal architecture detail — but never credentials, keys, or secrets.

**Generated:** 2026-07-14 01:24 UTC · **9 incidents logged.**

| Date | Incident | Summary |
|------|----------|---------|
| 2026-07-12 | [n8n CT-113 destruction during Spotify-harvester work](incidents/2026-07-12-n8n-ct113-destruction.md) | A single local session, building the music-curator Spotify harvester, tried to give the n8n container (LXC 113) a NAS bind-mount through the kalmia Terraform pipeline. |
| 2026-07-10 | [Firewalla log shipping went silently dark for three days, 2026-07-10→13](incidents/2026-07-10-firewalla-silent-log-outage.md) | The Firewalla's Fluent Bit log shipper delivered zero log lines to Grafana Cloud Loki for three days (2026-07-10 17:58 → 2026-07-13 19:58 EDT) while its container showed "Up" and healthy — three drosera dashboards (network-overview… |
| 2026-07-08 | [The 18-day config time bomb and the double outage behind "no stats"](incidents/2026-07-08-alloy-latent-config-double-outage.md) | "Hey I have no stats in grafana. |
| 2026-07-03 | [Terraform silently reverts the uncommitted dashboard revamp](incidents/2026-07-03-terraform-stomps-live-dashboard-revamp.md) | On the evening of 07-02, the Infrastructure Health dashboard got a substantial revamp — a six-node Fleet Scoreboard (finally covering pve3/4/5), per-host drill-downs, a NAS root-usage fix — applied to Grafana Cloud via the API only, never… |
| 2026-07-03 | [A stale memory steers a worker to regress correct code](incidents/2026-07-03-stale-memory-poisoned-dispatch.md) | Two days into the PitziLabs→Lentago rebrand, Home Claude dispatched rebrand-reconciliation jobs to the bullpen fleet. |
| 2026-07-02 | [The 22-day silent restart loop and the crontab that ate the appliance](incidents/2026-07-02-firewalla-crontab-clobber-and-22-day-loop.md) | A routine "work the top three priority issues" session in the firewalla-axiom-pipeline repo (now lentago/betula) turned into a 14-hour incident chain. |
| 2026-06-25 | [WireGuard handshake black-hole on ChromeOS](incidents/2026-06-25-wireguard-chromeos-arc-blackhole.md) | The operator's Chromebook "connected" to the Firewalla's WireGuard VPN but lost all network access — the classic full-tunnel black-hole: the client routes 0.0.0.0/0 into a tunnel whose data path never actually came up. |
| 2026-06-19 | [Multi-Claude Collision](incidents/2026-06-19-multi-claude-collision.md) | On Jun 19 you had as many as four local Claude Code sessions running at once (≈10:50–13:55) plus the three-worker headless fleet churning in the background. |
| 2026-05-28 | [Power outage → the log shipper's quiet death](incidents/2026-05-28-power-outage-fluent-bit-quiet-death.md) | An early-morning power outage on 2026-05-28 knocked out both the Firewalla and the Alloy relay LXC; they recovered at different speeds, and Fluent Bit on the Firewalla exhausted its Retry_Limit 3 on in-flight chunks while the relay was… |

_Generated with Claude Code (Repo Claude)._
