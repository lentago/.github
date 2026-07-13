# Lentago Labs Incident Register

> [!NOTE]
> **Co-authored with [Claude](https://claude.ai)** (the `/incident-digest` playbook). A chronological register of incident reports harvested from local Lentago lab activity and published as a periodic fleet report. Each row links to the full write-up under [`fleet-reports/incidents/`](incidents/). Unlike the [fleet report](fleet-report.md), these are published **verbatim** and *do* include homelab-internal architecture detail — but never credentials, keys, or secrets.

**Generated:** 2026-07-13 22:12 UTC · **2 incidents logged.**

| Date | Incident | Summary |
|------|----------|---------|
| 2026-07-12 | [n8n CT-113 destruction during Spotify-harvester work](incidents/2026-07-12-n8n-ct113-destruction.md) | A single local session, building the music-curator Spotify harvester, tried to give the n8n container (LXC 113) a NAS bind-mount through the kalmia Terraform pipeline. |
| 2026-06-19 | [Multi-Claude Collision](incidents/2026-06-19-multi-claude-collision.md) | On Jun 19 you had as many as four local Claude Code sessions running at once (≈10:50–13:55) plus the three-worker headless fleet churning in the background. |

_Generated with Claude Code (Repo Claude)._
