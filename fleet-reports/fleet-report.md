# Lentago Labs Fleet Report

> [!NOTE]
> **Co-authored with [Claude](https://claude.ai)** (Repo Claude, the Lentago Labs fleet steward). Auto-generated weekly from the fleet's public state (GitHub issues/PRs + `cloc` over public repo contents) — no personal, security, or homelab-internal detail is included. A prettier, editorialised copy renders on the Lentago lab LAN.

**Generated:** 2026-07-14 00:37 UTC · Scope: the **13 active** `lentago` repos (archived repos frozen &amp; excluded) · Activity window: last 30 days (since 2026-06-14).

## Snapshot

| Open issues | PRs merged (30d) | Issues closed (30d) | Code (incl. instructions) | Instruction-markdown |
|---:|---:|---:|---:|---:|
| **47** | 418 | 142 | **34,597** | 3,098 (18 files) |

The fleet's hand-maintained natural-language instruction surface (**3,098 lines** across 18 files) is among the largest "languages" in the code base — `reference-checker` alone is almost entirely prompt-program source.

---

## Open issues — 47 across 9 repos

### drosera — 10 open

| # | Title |
|---|-------|
| [152](https://github.com/lentago/drosera/issues/152) | Doc drift: README/CLAUDE.md/AGENTS.md still describe the retired Promtail → Alloy :3100 relay for Zeek logs |
| [151](https://github.com/lentago/drosera/issues/151) | device-inventory publisher: cron reinstall hook failed silently — root-cause and make the schedule survivable/verifiable |
| [150](https://github.com/lentago/drosera/issues/150) | Alert on ingest absence: no-data alerts for the critical Loki streams (zeek_dns, zeek_conn, firewalla_acl, device_inventory) |
| [145](https://github.com/lentago/drosera/issues/145) | gitops loop can't recover a crashed Alloy — validator runs inside the down container |
| [138](https://github.com/lentago/drosera/issues/138) | Trim node-exporter series with metric_relabel drop rules (~1k series of headroom under the 15k cap) |
| [131](https://github.com/lentago/drosera/issues/131) | Roadmap: multi-client telemetry pane — homelab and solidago (AWS) as peer sources |
| [129](https://github.com/lentago/drosera/issues/129) | claude-cost-export README: bullpen repo renamed to claytonia |
| [103](https://github.com/lentago/drosera/issues/103) | Scrape node_exporter on the Firewalla via Alloy (bring the gateway into node dashboards) |
| [101](https://github.com/lentago/drosera/issues/101) | Heartbeat blind spot: tool-less reasoning turns show no activity while tokens burn |
| [93](https://github.com/lentago/drosera/issues/93) | feat(alloy): attach runid label to the transcript stream from the <sid>.runid sidecar |

### kalmia — 9 open

| # | Title |
|---|-------|
| [53](https://github.com/lentago/kalmia/issues/53) | Pre-merge guard: verify a ForceNew guest change can actually be re-created under the apply identity |
| [52](https://github.com/lentago/kalmia/issues/52) | Codify the n8n container's provisioning (Docker + compose) — recreate yields a bare template |
| [51](https://github.com/lentago/kalmia/issues/51) | Guarantee vzdump coverage for every Terraform-enforced guest (CT 113 had none) |
| [50](https://github.com/lentago/kalmia/issues/50) | Add prevent_destroy to import-only guests the token pipeline can't recreate (starting CT 113) |
| [30](https://github.com/lentago/kalmia/issues/30) | Terraform: bring PVE backup jobs (jobs.cfg) under management |
| [20](https://github.com/lentago/kalmia/issues/20) | Roadmap: provisioning clients beyond Ansible-on-workstations — VMs and containers as peer targets |
| [16](https://github.com/lentago/kalmia/issues/16) | Harden the xubuntu profile for Ubuntu 26.04 (stale comment + Docker CE repo codename) |
| [15](https://github.com/lentago/kalmia/issues/15) | Live-test the crostini profile on the Chromebook penguin container |
| [14](https://github.com/lentago/kalmia/issues/14) | Live-test the ubuntu_laptop profile on real ThinkPad hardware |

### betula — 8 open

| # | Title |
|---|-------|
| [86](https://github.com/lentago/betula/issues/86) | Firewalla boot race: Fluent Bit starts before Zeek's spool is live and tails dead paths silently; healthcheck's error-based detection cannot see it |
| [83](https://github.com/lentago/betula/issues/83) | Refresh docs/architecture.svg — Axiom path retired, Loki-only pipeline |
| [74](https://github.com/lentago/betula/issues/74) | Roadmap: core/client split — Firewalla and solidago (AWS) as peer collector clients |
| [15](https://github.com/lentago/betula/issues/15) | Add conn.log bandwidth dashboard |
| [12](https://github.com/lentago/betula/issues/12) | Terraform the Axiom backend |
| [11](https://github.com/lentago/betula/issues/11) | Add New Domain Radar alert |
| [9](https://github.com/lentago/betula/issues/9) | Add IPv6-to-device resolution |
| [8](https://github.com/lentago/betula/issues/8) | Resolve remaining "Unknown" devices in group mapping |

### claytonia — 8 open

| # | Title |
|---|-------|
| [49](https://github.com/lentago/claytonia/issues/49) | Give the runner fleet a dedicated machine account instead of Chris's PAT |
| [47](https://github.com/lentago/claytonia/issues/47) | Roadmap: platform-agnostic workers — Claude Code as one runtime behind the queue contract |
| [31](https://github.com/lentago/claytonia/issues/31) | Add optional authentication to the n8n Bullpen job-submit form |
| [25](https://github.com/lentago/claytonia/issues/25) | Single 'what is every Claude doing right now' pane: unify local sessions + fleet jobs |
| [24](https://github.com/lentago/claytonia/issues/24) | Branch hygiene across overlapping sessions: clean-desk session-end + prefer fleet dispatch |
| [23](https://github.com/lentago/claytonia/issues/23) | Enforce no-auto-merge review gate on fleet PRs; make 'Open agent PRs' the dispatch gate |
| [22](https://github.com/lentago/claytonia/issues/22) | Fleet PR lane separation: rebase-before-merge + dispatch-time overlap check (no two writers on one file/panel) |
| [21](https://github.com/lentago/claytonia/issues/21) | Queue admission control: job ownership, fleet occupancy, and capacity awareness at submit time |

### solidago — 5 open

| # | Title |
|---|-------|
| [97](https://github.com/lentago/solidago/issues/97) | Eliminate perpetual ECS task-definition replacement in Terraform plans |
| [21](https://github.com/lentago/solidago/issues/21) | Evaluate migration from ElastiCache node-based to serverless |
| [20](https://github.com/lentago/solidago/issues/20) | Document: Phase 2 Secrets Manager secret unused after RDS-managed password choice |
| [19](https://github.com/lentago/solidago/issues/19) | Design multi-domain architecture for portfolio sites |
| [18](https://github.com/lentago/solidago/issues/18) | Set up local Docker Engine on ChromeOS for local container builds |

### reference-checker — 3 open

| # | Title |
|---|-------|
| [11](https://github.com/lentago/reference-checker/issues/11) | Implement pipeline decomposition (Opus / Sonnet / Haiku stages) |
| [10](https://github.com/lentago/reference-checker/issues/10) | [v4] Design batch-pattern detection across submissions |
| [8](https://github.com/lentago/reference-checker/issues/8) | [v4] Integrate Crossref retraction API for structured retraction checking |

### .github — 2 open

| # | Title |
|---|-------|
| [31](https://github.com/lentago/.github/issues/31) | Update language-census.md to current repo name solidago (was foundry-platform-demo) |
| [28](https://github.com/lentago/.github/issues/28) | fleet-ops: require the terraform check on enforced-surface repos (claytonia requires only shellcheck; kalmia requires none) |

### music-curator — 1 open

| # | Title |
|---|-------|
| [34](https://github.com/lentago/music-curator/issues/34) | spec: Dev Mode app cannot read playlist contents — data-availability allowlist row is wrong |

### site-lentago-dev — 1 open

| # | Title |
|---|-------|
| [36](https://github.com/lentago/site-lentago-dev/issues/36) | Update DEPLOYMENT.md to reference solidago instead of old repo name foundry-platform-demo |

## Activity — last 30 days

**418 PRs merged**

- 2026-07-14 · [.github#46](https://github.com/lentago/.github/pull/46) — Extend fleet-report activity window from 7 to 30 days
- 2026-07-14 · [.github#45](https://github.com/lentago/.github/pull/45) — Weekly fleet reports refresh — 2026-07-14
- 2026-07-14 · [.github#44](https://github.com/lentago/.github/pull/44) — Link filed issues in the Firewalla log-shipping incident report
- 2026-07-14 · [.github#43](https://github.com/lentago/.github/pull/43) — Add incident report: Firewalla log shipping silently dark for three days (2026-07-10→13)
- 2026-07-13 · [.github#42](https://github.com/lentago/.github/pull/42) — Delete brand/avatars/cjp-brackets-navy-512.png
- 2026-07-13 · [site-icecreamtofightwith-com#142](https://github.com/lentago/site-icecreamtofightwith-com/pull/142) — Style footer wordmark: calligraphic red "Fight" everywhere the mark appears
- 2026-07-13 · [site-icecreamtofightwith-com#141](https://github.com/lentago/site-icecreamtofightwith-com/pull/141) — Style header wordmark: calligraphic red "Fight" to match the hero
- 2026-07-13 · [.github#41](https://github.com/lentago/.github/pull/41) — Publish incident reports as a periodic fleet report (incident register)
- 2026-07-13 · [site-icecreamtofightwith-com#140](https://github.com/lentago/site-icecreamtofightwith-com/pull/140) — Style Intro hero: calligraphic red "Fight", tighter space above title
- 2026-07-13 · [.github#39](https://github.com/lentago/.github/pull/39) — Weekly fleet reports refresh — 2026-07-13
- 2026-07-13 · [.github#38](https://github.com/lentago/.github/pull/38) — Combine the fleet reports into a single fleet-report.md
- 2026-07-13 · [.github#37](https://github.com/lentago/.github/pull/37) — Weekly fleet reports refresh — 2026-07-13
- 2026-07-13 · [.github#36](https://github.com/lentago/.github/pull/36) — Add scheduled GitHub Actions workflow for the weekly fleet reports
- 2026-07-13 · [.github#35](https://github.com/lentago/.github/pull/35) — Add weekly fleet-reports automation + link from org profile
- 2026-07-13 · [homeassistant-config#506](https://github.com/lentago/homeassistant-config/pull/506) — Silence UGREEN NAS metrics: recorder-exclude sensors + drop NAS dashboard cards
- 2026-07-13 · [music-curator#32](https://github.com/lentago/music-curator/pull/32) — feat: Spotify data-availability spec + periodic Web API harvester (n8n)
- 2026-07-13 · [music-curator#37](https://github.com/lentago/music-curator/pull/37) — chore: gitignore .spotify operator secrets file on main
- 2026-07-13 · [music-curator#36](https://github.com/lentago/music-curator/pull/36) — chore: gitignore the local Music/ Obsidian working copy
- 2026-07-13 · [music-curator#35](https://github.com/lentago/music-curator/pull/35) — feat: streaming + collection merge — rotation dimension from GDPR streaming history
- 2026-07-13 · [music-curator#33](https://github.com/lentago/music-curator/pull/33) — data: purge the untagged reservoir — 26 artists discarded
- 2026-07-13 · [kalmia#49](https://github.com/lentago/kalmia/pull/49) — fix: re-import n8n LXC 113 (root@pam-created) to unbreak the pipeline
- 2026-07-12 · [kalmia#48](https://github.com/lentago/kalmia/pull/48) — fix: recreate n8n LXC 113 without bind mount (recover destroyed CT)
- 2026-07-12 · [kalmia#47](https://github.com/lentago/kalmia/pull/47) — feat: mount NAS spotify-harvest into n8n LXC 113 for the music-curator harvester
- 2026-07-12 · [site-icecreamtofightwith-com#139](https://github.com/lentago/site-icecreamtofightwith-com/pull/139) — Scroll-up at the top of a page loads the previous page
- 2026-07-12 · [site-icecreamtofightwith-com#137](https://github.com/lentago/site-icecreamtofightwith-com/pull/137) — Scroll-linked reading: auto-advance at end of scroll, keep the filmstrip in sync
- 2026-07-12 · [drosera#149](https://github.com/lentago/drosera/pull/149) — Rework Offload panel: stack by model, merge local sessions into metric-family rows
- 2026-07-12 · [site-icecreamtofightwith-com#136](https://github.com/lentago/site-icecreamtofightwith-com/pull/136) — Re-audit field diagrams and place each figure inline
- 2026-07-12 · [site-icecreamtofightwith-com#135](https://github.com/lentago/site-icecreamtofightwith-com/pull/135) — feat(homepage): add TitleHero viewport-filling title graphic
- 2026-07-12 · [site-icecreamtofightwith-com#134](https://github.com/lentago/site-icecreamtofightwith-com/pull/134) — Drop essay numbering, move Final Thoughts before recipes, soften tagline
- 2026-07-11 · [site-icecreamtofightwith-com#129](https://github.com/lentago/site-icecreamtofightwith-com/pull/129) — Add red scoop-mark favicon
- 2026-07-11 · [site-icecreamtofightwith-com#128](https://github.com/lentago/site-icecreamtofightwith-com/pull/128) — Widen filmstrip tiles, drop repeated sublabels, unredact the site, retire "homie"
- 2026-07-11 · [site-icecreamtofightwith-com#127](https://github.com/lentago/site-icecreamtofightwith-com/pull/127) — Implement the editorial redesign from Claude Design
- 2026-07-10 · [.github#34](https://github.com/lentago/.github/pull/34) — docs: publish the 2026-07 fleet issue report (archived copy)
- 2026-07-10 · [solidago#116](https://github.com/lentago/solidago/pull/116) — Finish pitzilabs teardown: neutralize illustrative example in modules/site (#80)
- 2026-07-10 · [solidago#114](https://github.com/lentago/solidago/pull/114) — Tear down the retired pitzilabs preview site (#80)
- 2026-07-10 · [solidago#113](https://github.com/lentago/solidago/pull/113) — Bump betula_ref to adopt the ALB parser 34-field fix
- 2026-07-10 · [drosera#148](https://github.com/lentago/drosera/pull/148) — Genericize ECS panel description to drop stale pitzilabs site name
- 2026-07-10 · [betula#85](https://github.com/lentago/betula/pull/85) — Tolerate extra trailing fields in ALB access-log lines
- 2026-07-10 · [kalmia#46](https://github.com/lentago/kalmia/pull/46) — Fix stale NAS path in pub LXC description after lentago rebrand
- 2026-07-10 · [betula#82](https://github.com/lentago/betula/pull/82) — Stop shipping to Axiom; Grafana Cloud Loki becomes the sole output
- 2026-07-10 · [.github#33](https://github.com/lentago/.github/pull/33) — Round the suite marks and inline them in the product name cells
- 2026-07-10 · [.github#32](https://github.com/lentago/.github/pull/32) — Add product marks to the suite table on the org profile
- 2026-07-10 · [solidago#112](https://github.com/lentago/solidago/pull/112) — Unblock ALB-log shipper deploy: grant lambda:* and make the package build plan-safe
- 2026-07-10 · [solidago#109](https://github.com/lentago/solidago/pull/109) — Deploy the ALB-access-log → Axiom shipper as a Lambda (#108)
- 2026-07-10 · [drosera#147](https://github.com/lentago/drosera/pull/147) — docs: transcript shipper now runs on all five bullpen runners
- 2026-07-09 · [drosera#146](https://github.com/lentago/drosera/pull/146) — fix(dashboard): make stream-of-consciousness panels unconditional, one per runner
- 2026-07-09 · [betula#81](https://github.com/lentago/betula/pull/81) — feat(aws): ALB access-log S3 → Axiom shipper (clients/aws/alb-logs)
- 2026-07-09 · [solidago#107](https://github.com/lentago/solidago/pull/107) — Enable ALB access logs to S3 for visitor-source telemetry
- 2026-07-09 · [music-curator#31](https://github.com/lentago/music-curator/pull/31) — feat: switchable graph-preset library — default taste map + artist-web audit view
- 2026-07-09 · [music-curator#30](https://github.com/lentago/music-curator/pull/30) — refactor: nest subcategory hub notes under their category folder
- 2026-07-09 · [music-curator#29](https://github.com/lentago/music-curator/pull/29) — feat: two-tier taxonomy — 13 top-level genres + subcategories
- 2026-07-09 · [music-curator#28](https://github.com/lentago/music-curator/pull/28) — refactor: promote the wiki out of examples/ — vault/ + data/ at top level
- 2026-07-09 · [music-curator#27](https://github.com/lentago/music-curator/pull/27) — feat: personnel credits layer + session-tie edges
- 2026-07-08 · [music-curator#15](https://github.com/lentago/music-curator/pull/15) — refactor: collapse scenes + genres into a single category axis
- 2026-07-08 · [music-curator#14](https://github.com/lentago/music-curator/pull/14) — data: tag the reservoir (round 1) — 376 artists graduated
- 2026-07-08 · [music-curator#13](https://github.com/lentago/music-curator/pull/13) — feat(vault): filter meta-hubs and recolor the graph by node type
- 2026-07-08 · [music-curator#12](https://github.com/lentago/music-curator/pull/12) — refactor(vault): remove the anchor layer from the graph
- 2026-07-08 · [music-curator#11](https://github.com/lentago/music-curator/pull/11) — feat: richer graph edges — collaboration links and split genres
- 2026-07-08 · [music-curator#10](https://github.com/lentago/music-curator/pull/10) — feat: Obsidian graph-vault driver
- 2026-07-08 · [drosera#144](https://github.com/lentago/drosera/pull/144) — fix(alloy): stop passing the HA token secret through string.trim_space
- 2026-07-08 · [claytonia#58](https://github.com/lentago/claytonia/pull/58) — Migrate Terraform backend to solidago-tfstate-* (#57)
- 2026-07-08 · [kalmia#45](https://github.com/lentago/kalmia/pull/45) — Migrate Terraform backend to solidago-tfstate-* (#44)
- 2026-07-08 · [drosera#143](https://github.com/lentago/drosera/pull/143) — Migrate Terraform backend to solidago-tfstate-* (#142)
- 2026-07-08 · [solidago#105](https://github.com/lentago/solidago/pull/105) — Migrate shared Terraform state backend to solidago-tfstate-* (#103)
- 2026-07-08 · [site-lentago-dev#37](https://github.com/lentago/site-lentago-dev/pull/37) — fix(deploy): point deploy.yml at renamed solidago-dev-* resources
- 2026-07-08 · [betula#79](https://github.com/lentago/betula/pull/79) — docs: update AWS Secrets Manager secret name in clients/aws
- 2026-07-08 · [drosera#141](https://github.com/lentago/drosera/pull/141) — fix(solidago): rename foundry-dev-* to solidago-dev-* (solidago#102)
- 2026-07-08 · [site-icecreamtofightwith-com#126](https://github.com/lentago/site-icecreamtofightwith-com/pull/126) — Align deploy pipeline to solidago-* resource names (#125)
- 2026-07-08 · [solidago#104](https://github.com/lentago/solidago/pull/104) — Rename foundry-* AWS resource names to the solidago codename (#102)
- 2026-07-07 · [kalmia#43](https://github.com/lentago/kalmia/pull/43) — Docs: the runner image is consumed, not a pending follow-up
- 2026-07-07 · [claytonia#56](https://github.com/lentago/claytonia/pull/56) — Docs: describe the image-based worker flow
- 2026-07-07 · [claytonia#55](https://github.com/lentago/claytonia/pull/55) — Cut new workers from the kalmia runner image; retire provision/01–05
- 2026-07-07 · [.github#30](https://github.com/lentago/.github/pull/30) — fleet-ops: require existing always-on checks on 3 more repos
- 2026-07-07 · [kalmia#42](https://github.com/lentago/kalmia/pull/42) — Image forge + first artifact: the claytonia-runner LXC template
- 2026-07-07 · [.github#29](https://github.com/lentago/.github/pull/29) — fleet-ops: manage per-repo required status checks
- 2026-07-07 · [solidago#101](https://github.com/lentago/solidago/pull/101) — Detect terraform changes and gate merges on a `gate` check
- 2026-07-07 · [drosera#139](https://github.com/lentago/drosera/pull/139) — Always run terraform CI on PRs, gate merges on a `gate` check
- 2026-07-07 · [kalmia#41](https://github.com/lentago/kalmia/pull/41) — Always run terraform CI on PRs, gate merges on a `gate` check
- 2026-07-07 · [shared-workflows#24](https://github.com/lentago/shared-workflows/pull/24) — docs: mark claytonia runner-pool applies as CI-enforced-on-merge
- 2026-07-07 · [claytonia#53](https://github.com/lentago/claytonia/pull/53) — Add terraform CI: plan-on-PR / apply-on-merge on the LAN runner
- 2026-07-07 · [shared-workflows#23](https://github.com/lentago/shared-workflows/pull/23) — Enforced surfaces: split the Proxmox guest row — runner pool moves to claytonia
- 2026-07-07 · [claytonia#52](https://github.com/lentago/claytonia/pull/52) — Adopt the worker-pool guest layer: Terraform root, Proxmox as first platform client
- 2026-07-07 · [kalmia#40](https://github.com/lentago/kalmia/pull/40) — Release the bullpen runner pool from the guest layer — capacity moves to claytonia
- 2026-07-07 · [kalmia#39](https://github.com/lentago/kalmia/pull/39) — Ignore operator-driven power state on workstation and testbed VMs
- 2026-07-06 · [kalmia#35](https://github.com/lentago/kalmia/pull/35) — Create bullpen runners 4/5 without a Terraform-managed bind mount
- 2026-07-06 · [kalmia#34](https://github.com/lentago/kalmia/pull/34) — Scale the bullpen out by two runners (claude-runner-4/-5, LXC 116/117)
- 2026-07-06 · [solidago#100](https://github.com/lentago/solidago/pull/100) — chore: drop stale app/ice_cream_site .gitignore rules
- 2026-07-06 · [solidago#99](https://github.com/lentago/solidago/pull/99) — Delete app directory
- 2026-07-06 · [site-icecreamtofightwith-com#124](https://github.com/lentago/site-icecreamtofightwith-com/pull/124) — Revert "Redesign the site as a dated punk-zine blog" (#123)
- 2026-07-06 · [site-icecreamtofightwith-com#123](https://github.com/lentago/site-icecreamtofightwith-com/pull/123) — Redesign the site as a dated punk-zine blog
- 2026-07-06 · [site-lentago-dev#35](https://github.com/lentago/site-lentago-dev/pull/35) — Rename Suite anchor #work → #systems for nav consistency
- 2026-07-06 · [site-lentago-dev#34](https://github.com/lentago/site-lentago-dev/pull/34) — Wire consult form to Formspree (native POST, no JS) + /thanks page
- 2026-07-06 · [site-lentago-dev#33](https://github.com/lentago/site-lentago-dev/pull/33) — Add social-share meta + og:image, build-time footer version, and nav Principles relabel
- 2026-07-06 · [site-lentago-dev#27](https://github.com/lentago/site-lentago-dev/pull/27) — feat(suite): anchor each system row with its genus mark
- 2026-07-05 · [solidago#98](https://github.com/lentago/solidago/pull/98) — Add GitHub Pages domain-verification TXT record for lentago.dev
- 2026-07-05 · [solidago#96](https://github.com/lentago/solidago/pull/96) — Add GitHub org domain-verification TXT record for lentago.dev
- 2026-07-05 · [.github#26](https://github.com/lentago/.github/pull/26) — Add 'The suite' legend to the org profile README
- 2026-07-05 · [kalmia#32](https://github.com/lentago/kalmia/pull/32) — Pin the PVE CA and drop insecure = true (cleanup)
- 2026-07-05 · [kalmia#29](https://github.com/lentago/kalmia/pull/29) — Import pve5 guests and HAOS VM 100 into Terraform (phase 3)
- 2026-07-05 · [kalmia#27](https://github.com/lentago/kalmia/pull/27) — LAN apply-on-merge: self-hosted runner LXC + terraform workflow (phase 2)
- 2026-07-05 · [shared-workflows#22](https://github.com/lentago/shared-workflows/pull/22) — Add kalmia Proxmox guest layer to the enforced-surfaces table
- 2026-07-05 · [kalmia#24](https://github.com/lentago/kalmia/pull/24) — Import the five pve4 LXCs into Terraform (phase 1)
- 2026-07-05 · [repo-template#6](https://github.com/lentago/repo-template/pull/6) — Scrub homelab branding for the Lentago rebrand
- 2026-07-05 · [solidago#95](https://github.com/lentago/solidago/pull/95) — Scrub homelab branding for the Lentago rebrand
- 2026-07-05 · [site-lentago-dev#25](https://github.com/lentago/site-lentago-dev/pull/25) — Scrub homelab branding for the Lentago rebrand
- 2026-07-05 · [shared-workflows#21](https://github.com/lentago/shared-workflows/pull/21) — Scrub homelab branding for the Lentago rebrand
- 2026-07-05 · [.github#25](https://github.com/lentago/.github/pull/25) — Scrub homelab branding for the Lentago rebrand
- 2026-07-05 · [kalmia#26](https://github.com/lentago/kalmia/pull/26) — Scrub homelab branding for the Lentago rebrand
- 2026-07-05 · [homeassistant-config#505](https://github.com/lentago/homeassistant-config/pull/505) — Rename Homelab Status dashboard to Lentago Lab Status
- 2026-07-05 · [claytonia#50](https://github.com/lentago/claytonia/pull/50) — Scrub homelab branding for the Lentago rebrand
- 2026-07-05 · [betula#77](https://github.com/lentago/betula/pull/77) — Scrub homelab branding for the Lentago rebrand
- 2026-07-05 · [drosera#137](https://github.com/lentago/drosera/pull/137) — Scrub homelab branding for the Lentago rebrand
- 2026-07-05 · [site-lentago-dev#24](https://github.com/lentago/site-lentago-dev/pull/24) — Add mobile responsive layer (≤720px/≤460px) with zero desktop change
- 2026-07-05 · [drosera#136](https://github.com/lentago/drosera/pull/136) — Display dashboard temperatures in Fahrenheit
- 2026-07-05 · [kalmia#22](https://github.com/lentago/kalmia/pull/22) — Add Terraform layer for Proxmox guest lifecycle (phase 0)
- 2026-07-04 · [site-lentago-dev#23](https://github.com/lentago/site-lentago-dev/pull/23) — Landing reorg: drop ice-cream case study, add Suite section
- 2026-07-04 · [betula#76](https://github.com/lentago/betula/pull/76) — Rebrand sweep: PitziLabs → Lentago Labs
- 2026-07-04 · [claytonia#48](https://github.com/lentago/claytonia/pull/48) — Rebrand sweep: PitziLabs → Lentago Labs
- 2026-07-04 · [.github#24](https://github.com/lentago/.github/pull/24) — Rebrand sweep: PitziLabs → Lentago Labs
- 2026-07-04 · [homeassistant-config#504](https://github.com/lentago/homeassistant-config/pull/504) — Rebrand sweep: PitziLabs → Lentago Labs
- 2026-07-04 · [site-icecreamtofightwith-com#122](https://github.com/lentago/site-icecreamtofightwith-com/pull/122) — Rebrand sweep: PitziLabs → Lentago Labs
- 2026-07-04 · [drosera#135](https://github.com/lentago/drosera/pull/135) — Rebrand sweep: PitziLabs → Lentago Labs
- 2026-07-04 · [solidago#94](https://github.com/lentago/solidago/pull/94) — Rebrand sweep: PitziLabs → Lentago Labs
- 2026-07-04 · [site-lentago-dev#22](https://github.com/lentago/site-lentago-dev/pull/22) — Rebrand sweep: PitziLabs → Lentago Labs
- 2026-07-04 · [solidago#93](https://github.com/lentago/solidago/pull/93) — Ship ECS container logs to Axiom via FireLens (Phase 2)
- 2026-07-04 · [betula#75](https://github.com/lentago/betula/pull/75) — Add clients/aws contract: solidago ECS logs → Axiom via FireLens (Phase 2)
- 2026-07-04 · [drosera#134](https://github.com/lentago/drosera/pull/134) — docs: note expected logs AccessDenied in CloudWatch datasource health check
- 2026-07-04 · [solidago#91](https://github.com/lentago/solidago/pull/91) — Add grafana-cloud module: cross-account read-only role for Grafana Cloud CloudWatch datasource (Phase 1 Part A)
- 2026-07-04 · [drosera#133](https://github.com/lentago/drosera/pull/133) — Add Solidago folder, CloudWatch datasource, and platform-health dashboard (Phase 1 Part B)
- 2026-07-04 · [shared-workflows#20](https://github.com/lentago/shared-workflows/pull/20) — Sync live-state mirror for site-repo renames
- 2026-07-04 · [site-lentago-dev#21](https://github.com/lentago/site-lentago-dev/pull/21) — Align repo contents with site-lentago-dev rename
- 2026-07-04 · [site-icecreamtofightwith-com#121](https://github.com/lentago/site-icecreamtofightwith-com/pull/121) — Align repo contents with site-icecreamtofightwith-com rename
- 2026-07-04 · [solidago#89](https://github.com/lentago/solidago/pull/89) — Codify site-repo rename dual-trust in app OIDC role
- 2026-07-04 · [betula#73](https://github.com/lentago/betula/pull/73) — Rebrand repo to Betula — Lentago Labs log capture-and-archive layer
- 2026-07-04 · [drosera#130](https://github.com/lentago/drosera/pull/130) — docs: update bullpen repo link to claytonia
- 2026-07-04 · [claytonia#46](https://github.com/lentago/claytonia/pull/46) — Rebrand repo to Claytonia — Lentago Labs agent-fleet system
- 2026-07-04 · [claytonia#44](https://github.com/lentago/claytonia/pull/44) — chore: rename homelab-observability → drosera refs
- 2026-07-04 · [drosera#128](https://github.com/lentago/drosera/pull/128) — Rebrand repo to Drosera — Lentago Labs observability suite
- 2026-07-04 · [kalmia#19](https://github.com/lentago/kalmia/pull/19) — Rebrand repo to Kalmia — Lentago Labs provisioning system
- 2026-07-04 · [shared-workflows#19](https://github.com/lentago/shared-workflows/pull/19) — Sync live-state mirror for homelab-observability → drosera rename
- 2026-07-04 · [solidago#87](https://github.com/lentago/solidago/pull/87) — docs: sync README, CLAUDE.md, and BOOTSTRAP.md with recent platform changes
- 2026-07-04 · [solidago#86](https://github.com/lentago/solidago/pull/86) — Add project-scoped DeepWiki MCP server config
- 2026-07-04 · [solidago#85](https://github.com/lentago/solidago/pull/85) — Update self-references for repo rename to solidago
- 2026-07-04 · [site-icecreamtofightwith-com#119](https://github.com/lentago/site-icecreamtofightwith-com/pull/119) — docs: rebrand foundry-platform-demo → solidago
- 2026-07-04 · [drosera#126](https://github.com/lentago/drosera/pull/126) — docs(terraform): rename foundry-platform-demo → solidago
- 2026-07-04 · [homeassistant-config#503](https://github.com/lentago/homeassistant-config/pull/503) — docs: update foundry-platform-demo reference to solidago
- 2026-07-04 · [betula#71](https://github.com/lentago/betula/pull/71) — docs: update foundry-platform-demo reference to solidago
- 2026-07-04 · [site-lentago-dev#19](https://github.com/lentago/site-lentago-dev/pull/19) — docs: update solidago repo references (formerly foundry-platform-demo)
- 2026-07-04 · [claytonia#42](https://github.com/lentago/claytonia/pull/42) — Update n8n submit-form project option for solidago rename
- 2026-07-04 · [homeassistant-config#502](https://github.com/lentago/homeassistant-config/pull/502) — chore(readme): add Ask DeepWiki badge
- 2026-07-04 · [site-icecreamtofightwith-com#118](https://github.com/lentago/site-icecreamtofightwith-com/pull/118) — chore(readme): add Ask DeepWiki badge
- 2026-07-04 · [kalmia#17](https://github.com/lentago/kalmia/pull/17) — chore(readme): add Ask DeepWiki badge
- 2026-07-04 · [site-lentago-dev#18](https://github.com/lentago/site-lentago-dev/pull/18) — chore(readme): add Ask DeepWiki badge
- 2026-07-04 · [shared-workflows#18](https://github.com/lentago/shared-workflows/pull/18) — chore(readme): add Ask DeepWiki badge
- 2026-07-04 · [solidago#84](https://github.com/lentago/solidago/pull/84) — chore(readme): add Ask DeepWiki badge
- 2026-07-04 · [repo-template#5](https://github.com/lentago/repo-template/pull/5) — chore(readme): add Ask DeepWiki badge
- 2026-07-04 · [reference-checker#49](https://github.com/lentago/reference-checker/pull/49) — chore(readme): add Ask DeepWiki badge
- 2026-07-04 · [drosera#125](https://github.com/lentago/drosera/pull/125) — chore(readme): add Ask DeepWiki badge
- 2026-07-04 · [music-curator#8](https://github.com/lentago/music-curator/pull/8) — chore(readme): add Ask DeepWiki badge
- 2026-07-04 · [betula#70](https://github.com/lentago/betula/pull/70) — chore(readme): add Ask DeepWiki badge
- 2026-07-04 · [claytonia#41](https://github.com/lentago/claytonia/pull/41) — chore(readme): add Ask DeepWiki badge
- 2026-07-04 · [.github#23](https://github.com/lentago/.github/pull/23) — chore(readme): add Ask DeepWiki badge
- 2026-07-04 · [homeassistant-config#501](https://github.com/lentago/homeassistant-config/pull/501) — feat(office): rework candle flicker into a physical fire model
- 2026-07-04 · [homeassistant-config#500](https://github.com/lentago/homeassistant-config/pull/500) — feat(dashboard): show live light color on Home light cards
- 2026-07-03 · [homeassistant-config#499](https://github.com/lentago/homeassistant-config/pull/499) — Reconcile NAS share rename in neptune dashboard card
- 2026-07-03 · [claytonia#40](https://github.com/lentago/claytonia/pull/40) — Reconcile NAS share rename: PitziLabs -> lentago paths
- 2026-07-03 · [shared-workflows#17](https://github.com/lentago/shared-workflows/pull/17) — Reconcile PitziLabs->lentago: runner bot name + org wording
- 2026-07-03 · [homeassistant-config#498](https://github.com/lentago/homeassistant-config/pull/498) — Reconcile PitziLabs->lentago: grafana URL in dashboard card
- 2026-07-03 · [betula#69](https://github.com/lentago/betula/pull/69) — Reconcile PitziLabs->lentago: architecture diagram
- 2026-07-03 · [claytonia#39](https://github.com/lentago/claytonia/pull/39) — Reconcile PitziLabs->lentago: runner App name + org URLs
- 2026-07-03 · [drosera#124](https://github.com/lentago/drosera/pull/124) — Reconcile PitziLabs->lentago: stack URL + datasource names + org URLs + alloy health-check
- 2026-07-03 · [drosera#122](https://github.com/lentago/drosera/pull/122) — feat(device-inventory): Firewalla redis → Loki publisher (#113 Phase 1)
- 2026-07-03 · [drosera#121](https://github.com/lentago/drosera/pull/121) — feat(dashboards): device inventory join, dropdown, WAN lookup links (phases 2+3+4a of #113)
- 2026-07-03 · [shared-workflows#16](https://github.com/lentago/shared-workflows/pull/16) — CLAUDE.md: add fleet-wide live-state vs. code discipline (canonical source)
- 2026-07-03 · [drosera#120](https://github.com/lentago/drosera/pull/120) — CLAUDE.md: add anti-drift rule for live dashboard edits
- 2026-07-03 · [drosera#119](https://github.com/lentago/drosera/pull/119) — infra-health: restore fleet-scoreboard revamp lost to IaC drift stomp
- 2026-07-03 · [drosera#116](https://github.com/lentago/drosera/pull/116) — fix(dashboards): convert device_ip from empty custom dropdown to textbox
- 2026-07-03 · [drosera#118](https://github.com/lentago/drosera/pull/118) — fix: retarget Value #A field in 9 table panels (closes #108)
- 2026-07-03 · [drosera#117](https://github.com/lentago/drosera/pull/117) — fix: panel 5 status label fallback with label_replace
- 2026-07-03 · [drosera#115](https://github.com/lentago/drosera/pull/115) — fix: migrate legacy hidden legend schema to modern shape (issue #109)
- 2026-07-03 · [drosera#114](https://github.com/lentago/drosera/pull/114) — fix(traffic-devices): enable values in reduceOptions for proto piechart
- 2026-07-03 · [.github#22](https://github.com/lentago/.github/pull/22) — Recolor org profile to the 2026-07 Tidewater palette
- 2026-07-03 · [site-lentago-dev#17](https://github.com/lentago/site-lentago-dev/pull/17) — docs: reconcile CLAUDE.md GitHub-reference convention to the live lentago org
- 2026-07-03 · [site-lentago-dev#16](https://github.com/lentago/site-lentago-dev/pull/16) — Fix dead links and stale org references now that the site is live
- 2026-07-03 · [betula#68](https://github.com/lentago/betula/pull/68) — fix(cron): merge via update_crontab.sh instead of clobbering system crontab (#67)
- 2026-07-03 · [drosera#107](https://github.com/lentago/drosera/pull/107) — office-display: cover pve3/4/5 + neptune, de-dup HA titles
- 2026-07-03 · [drosera#106](https://github.com/lentago/drosera/pull/106) — Zeek/Loki dashboards: filter consistency, label accuracy, descriptions
- 2026-07-03 · [drosera#105](https://github.com/lentago/drosera/pull/105) — infra-health: re-point probe panels to integrations/blackbox/* jobs
- 2026-07-03 · [drosera#104](https://github.com/lentago/drosera/pull/104) — NAS dashboard: LCD bar gauges for Memory + Volume, group CPU gauges
- 2026-07-03 · [betula#66](https://github.com/lentago/betula/pull/66) — fix(healthcheck): remove no-output restart that bounces healthy container
- 2026-07-02 · [betula#64](https://github.com/lentago/betula/pull/64) — feat: ship host + Zeek process metrics to Axiom (system_metrics_export.sh)
- 2026-07-02 · [betula#62](https://github.com/lentago/betula/pull/62) — fix(healthcheck): use sudo docker to fix false-positive cron failures
- 2026-07-02 · [betula#60](https://github.com/lentago/betula/pull/60) — docs(axiom): align new Zeek log queries with canonical arg_max join pattern
- 2026-07-02 · [betula#58](https://github.com/lentago/betula/pull/58) — feat: ship Zeek http, files, notice, and weird logs (#4)
- 2026-07-02 · [betula#59](https://github.com/lentago/betula/pull/59) — feat: rotate health check and cleanup log files (closes #5)
- 2026-07-02 · [betula#57](https://github.com/lentago/betula/pull/57) — docs(axiom): robust device joins via arg_max latest-record-per-MAC
- 2026-07-02 · [claytonia#38](https://github.com/lentago/claytonia/pull/38) — feat(run-job): comment on originating GitHub issue when a project job fails
- 2026-07-02 · [solidago#83](https://github.com/lentago/solidago/pull/83) — chore(ci): upgrade actions/checkout to v7 (Node.js 24 runtime)
- 2026-07-02 · [solidago#82](https://github.com/lentago/solidago/pull/82) — refactor(modules): standardize resource labels from "main" to "this" (#12)
- 2026-07-02 · [solidago#81](https://github.com/lentago/solidago/pull/81) — refactor(vpc): key subnets by AZ with for_each instead of count
- 2026-07-02 · [homeassistant-config#497](https://github.com/lentago/homeassistant-config/pull/497) — fix(dashboard): pin media tiles to fixed height to stop layout reflow on playback change
- 2026-07-01 · [claytonia#36](https://github.com/lentago/claytonia/pull/36) — docs(frontends): mark n8n submit form as retired
- 2026-07-01 · [homeassistant-config#496](https://github.com/lentago/homeassistant-config/pull/496) — docs(dashboards): document the Home single-master / two-clone scheme
- 2026-07-01 · [site-lentago-dev#15](https://github.com/lentago/site-lentago-dev/pull/15) — Scale footer wordmark to match enlarged nav lockup
- 2026-07-01 · [.github#21](https://github.com/lentago/.github/pull/21) — Seed org-default community-health files
- 2026-07-01 · [.github#20](https://github.com/lentago/.github/pull/20) — Restore logos on the AWS / ECS Fargate / CloudWatch profile badges
- 2026-07-01 · [.github#19](https://github.com/lentago/.github/pull/19) — Add the limestone on-dark blossom variant and settle the canonical avatar
- 2026-07-01 · [drosera#102](https://github.com/lentago/drosera/pull/102) — Rehome claude-cost-export from the archived workstation-bootstrap repo
- 2026-07-01 · [site-lentago-dev#14](https://github.com/lentago/site-lentago-dev/pull/14) — Recolor: anther-gold accent + teal warmed toward green
- 2026-07-01 · [solidago#79](https://github.com/lentago/solidago/pull/79) — feat(dns): Fastmail mail records for lentago.dev
- 2026-07-01 · [site-lentago-dev#13](https://github.com/lentago/site-lentago-dev/pull/13) — docs: reflect that the site is live at lentago.dev
- 2026-07-01 · [solidago#78](https://github.com/lentago/solidago/pull/78) — chore(site): retire the redundant lt-preview host for lentago.dev
- 2026-07-01 · [solidago#77](https://github.com/lentago/solidago/pull/77) — feat(dns): promote lentagolabs-dev to lentago.dev
- 2026-07-01 · [homeassistant-config#495](https://github.com/lentago/homeassistant-config/pull/495) — fix(alarm): drop the dead basement-kitchen door from House Openings
- 2026-07-01 · [drosera#100](https://github.com/lentago/drosera/pull/100) — Fleet dashboard: offload overlay, combined spend + total, wider stream-of-consciousness
- 2026-07-01 · [solidago#76](https://github.com/lentago/solidago/pull/76) — feat: selective teardown/standup scripts + runbook for cost saving (Closes #14)
- 2026-07-01 · [music-curator#7](https://github.com/lentago/music-curator/pull/7) — feat(schema): add JSON Schema + validator for music-inventory.json
- 2026-07-01 · [site-lentago-dev#12](https://github.com/lentago/site-lentago-dev/pull/12) — docs: update deploy status in CLAUDE.md
- 2026-07-01 · [solidago#75](https://github.com/lentago/solidago/pull/75) — feat: encrypt Terraform state bucket with a dedicated KMS CMK (SSE-KMS)
- 2026-07-01 · [claytonia#35](https://github.com/lentago/claytonia/pull/35) — fix(run-job): fail project jobs that complete without opening a PR
- 2026-07-01 · [claytonia#34](https://github.com/lentago/claytonia/pull/34) — feat(cr-submit): -h/--help, unknown-flag error, bare-invocation guard
- 2026-07-01 · [shared-workflows#15](https://github.com/lentago/shared-workflows/pull/15) — fix(claude-review): make the reviewer advisory and non-blocking
- 2026-07-01 · [music-curator#6](https://github.com/lentago/music-curator/pull/6) — fix(examples): correct meta counts and merge Eno/Byrne duplicates
- 2026-07-01 · [solidago#74](https://github.com/lentago/solidago/pull/74) — feat: migrate S3 backend to S3-native state locking (use_lockfile)
- 2026-07-01 · [betula#56](https://github.com/lentago/betula/pull/56) — fix: make deploy.sh idempotent (safe to re-run)
- 2026-07-01 · [claytonia#33](https://github.com/lentago/claytonia/pull/33) — fix(cr-submit): accept -m/-p/-f in any order
- 2026-07-01 · [claytonia#32](https://github.com/lentago/claytonia/pull/32) — docs(roadmap): drop retired pve2 wall-display/kiosk as a live-board target
- 2026-06-30 · [.github#15](https://github.com/lentago/.github/pull/15) — Swap org-profile banner mark to the limestone-chip blossom
- 2026-06-30 · [kalmia#13](https://github.com/lentago/kalmia/pull/13) — Record testbed validation status for xubuntu/fedora
- 2026-06-30 · [kalmia#12](https://github.com/lentago/kalmia/pull/12) — Fix playbook startup, Helm/openssl, and fzf install (first real-target test run)
- 2026-06-30 · [kalmia#10](https://github.com/lentago/kalmia/pull/10) — Document the Xubuntu/Fedora provisioning testbed VMs
- 2026-06-30 · [kalmia#9](https://github.com/lentago/kalmia/pull/9) — Finish the crostini profile (sudo, ~/.local/bin, CLI-only Docker)
- 2026-06-30 · [kalmia#7](https://github.com/lentago/kalmia/pull/7) — Add power role: TLP, ThinkPad charge thresholds, fwupd
- 2026-06-30 · [kalmia#5](https://github.com/lentago/kalmia/pull/5) — Drop remote desktop (XRDP) capability entirely
- 2026-06-30 · [kalmia#3](https://github.com/lentago/kalmia/pull/3) — Wire Fedora dnf installs for Docker and VS Code
- 2026-06-30 · [site-lentago-dev#8](https://github.com/lentago/site-lentago-dev/pull/8) — Enlarge the brand lockup in the top nav
- 2026-06-30 · [kalmia#1](https://github.com/lentago/kalmia/pull/1) — Add Ansible scaffold and core roles (Debian-runnable)
- 2026-06-30 · [site-lentago-dev#7](https://github.com/lentago/site-lentago-dev/pull/7) — Feature the blossom mark prominently in the hero
- 2026-06-30 · [.github#14](https://github.com/lentago/.github/pull/14) — Regenerate language census (post-rebrand, 15 repos)
- 2026-06-30 · [.github#13](https://github.com/lentago/.github/pull/13) — Point org profile links to lentago.dev
- 2026-06-30 · [.github#12](https://github.com/lentago/.github/pull/12) — Adopt the blossom brand mark across org materials
- 2026-06-30 · [site-lentago-dev#6](https://github.com/lentago/site-lentago-dev/pull/6) — Refresh docs: deploy is live, mark is the blossom
- 2026-06-30 · [site-lentago-dev#5](https://github.com/lentago/site-lentago-dev/pull/5) — Replace benchmark-disk mark with the blossom
- 2026-06-30 · [.github#11](https://github.com/lentago/.github/pull/11) — Rebrand org profile to Lentago Labs (Tidewater)
- 2026-06-30 · [solidago#73](https://github.com/lentago/solidago/pull/73) — Rebrand: fix remaining org URL in backlog script
- 2026-06-30 · [solidago#72](https://github.com/lentago/solidago/pull/72) — Rebrand: backlog script → lentago/foundry-platform-demo
- 2026-06-30 · [solidago#71](https://github.com/lentago/solidago/pull/71) — docs: correct stale AWS profile reference in CLAUDE.md
- 2026-06-30 · [solidago#70](https://github.com/lentago/solidago/pull/70) — Rebrand GitHub org references: PitziLabs → lentago
- 2026-06-29 · [drosera#99](https://github.com/lentago/drosera/pull/99) — Fix runner-fleet dashboard: app renamed to lentago-claude-runner
- 2026-06-29 · [site-lentago-dev#4](https://github.com/lentago/site-lentago-dev/pull/4) — Rebrand docs: PitziLabs → Lentago Labs
- 2026-06-29 · [shared-workflows#13](https://github.com/lentago/shared-workflows/pull/13) — Rebrand docs: PitziLabs → Lentago Labs
- 2026-06-29 · [repo-template#4](https://github.com/lentago/repo-template/pull/4) — Rebrand docs: PitziLabs → Lentago Labs
- 2026-06-29 · [site-icecreamtofightwith-com#117](https://github.com/lentago/site-icecreamtofightwith-com/pull/117) — Rebrand docs: PitziLabs → Lentago Labs
- 2026-06-29 · [music-curator#3](https://github.com/lentago/music-curator/pull/3) — Rebrand docs: PitziLabs → Lentago Labs
- 2026-06-29 · [claytonia#30](https://github.com/lentago/claytonia/pull/30) — Rebrand docs: PitziLabs → Lentago Labs
- 2026-06-29 · [drosera#98](https://github.com/lentago/drosera/pull/98) — Rebrand docs: PitziLabs → Lentago Labs
- 2026-06-29 · [homeassistant-config#494](https://github.com/lentago/homeassistant-config/pull/494) — Rebrand docs: PitziLabs → Lentago Labs
- 2026-06-29 · [.github#10](https://github.com/lentago/.github/pull/10) — Rebrand docs: PitziLabs → Lentago Labs (meta-repo + fleet-ops)
- 2026-06-29 · [betula#55](https://github.com/lentago/betula/pull/55) — Rebrand docs: PitziLabs → Lentago Labs
- 2026-06-29 · [homeassistant-config#493](https://github.com/lentago/homeassistant-config/pull/493) — Repoint reusable-workflow refs to the lentago org
- 2026-06-29 · [reference-checker#48](https://github.com/lentago/reference-checker/pull/48) — Repoint reusable-workflow refs to the lentago org
- 2026-06-29 · [site-icecreamtofightwith-com#116](https://github.com/lentago/site-icecreamtofightwith-com/pull/116) — Repoint reusable-workflow refs to the lentago org
- 2026-06-29 · [site-lentago-dev#3](https://github.com/lentago/site-lentago-dev/pull/3) — Repoint reusable-workflow refs to the lentago org
- 2026-06-29 · [betula#54](https://github.com/lentago/betula/pull/54) — Repoint reusable-workflow refs to the lentago org
- 2026-06-29 · [drosera#97](https://github.com/lentago/drosera/pull/97) — Repoint reusable-workflow refs to the lentago org
- 2026-06-29 · [claytonia#29](https://github.com/lentago/claytonia/pull/29) — Repoint reusable-workflow refs to the lentago org
- 2026-06-29 · [music-curator#2](https://github.com/lentago/music-curator/pull/2) — Repoint reusable-workflow refs to the lentago org
- 2026-06-29 · [repo-template#3](https://github.com/lentago/repo-template/pull/3) — Repoint reusable-workflow refs to the lentago org
- 2026-06-29 · [shared-workflows#12](https://github.com/lentago/shared-workflows/pull/12) — Repoint reusable-workflow refs to the lentago org
- 2026-06-29 · [site-lentago-dev#2](https://github.com/lentago/site-lentago-dev/pull/2) — Add trigger for deployment on push to main branch
- 2026-06-29 · [solidago#69](https://github.com/lentago/solidago/pull/69) — Host lentagolabs-dev on the shared platform (site_lentago + OIDC trust)
- 2026-06-29 · [site-lentago-dev#1](https://github.com/lentago/site-lentago-dev/pull/1) — Add Foundry deployment guide for lentagolabs-dev
- 2026-06-28 · [homeassistant-config#492](https://github.com/lentago/homeassistant-config/pull/492) — fix(dashboards): repoint presence tiles from WiFi device_tracker to GPS person.* entities
- 2026-06-25 · [repo-template#2](https://github.com/lentago/repo-template/pull/2) — Disable automated Claude PR review (manual-only trigger)
- 2026-06-25 · [reference-checker#47](https://github.com/lentago/reference-checker/pull/47) — Disable automated Claude PR review (manual-only trigger)
- 2026-06-25 · [homeassistant-config#490](https://github.com/lentago/homeassistant-config/pull/490) — Disable automated Claude PR review (manual-only trigger)
- 2026-06-25 · [music-curator#1](https://github.com/lentago/music-curator/pull/1) — Disable automated Claude PR review (manual-only trigger)
- 2026-06-25 · [site-icecreamtofightwith-com#115](https://github.com/lentago/site-icecreamtofightwith-com/pull/115) — Disable automated Claude PR review (manual-only trigger)
- 2026-06-25 · [drosera#96](https://github.com/lentago/drosera/pull/96) — Disable automated Claude PR review (manual-only trigger)
- 2026-06-25 · [solidago#68](https://github.com/lentago/solidago/pull/68) — Disable automated Claude PR review (manual-only trigger)
- 2026-06-25 · [betula#53](https://github.com/lentago/betula/pull/53) — Disable automated Claude PR review (manual-only trigger)
- 2026-06-25 · [claytonia#28](https://github.com/lentago/claytonia/pull/28) — Disable automated Claude PR review (manual-only trigger)
- 2026-06-25 · [drosera#95](https://github.com/lentago/drosera/pull/95) — fix(dashboard): panel-11 — count distinct sessions, not per-worker boolean
- 2026-06-25 · [claytonia#26](https://github.com/lentago/claytonia/pull/26) — feat(frontends): n8n web form to submit bullpen jobs
- 2026-06-25 · [claytonia#27](https://github.com/lentago/claytonia/pull/27) — docs: drop Origin section from PR template, neutralize Summary voice
- 2026-06-25 · [homeassistant-config#489](https://github.com/lentago/homeassistant-config/pull/489) — docs: neutralize PR summary voice (drop Origin/Prompt-Origin)
- 2026-06-25 · [shared-workflows#11](https://github.com/lentago/shared-workflows/pull/11) — docs: neutralize PR voice — drop the ## Origin section and Prompt-Origin trailer
- 2026-06-25 · [homeassistant-config#488](https://github.com/lentago/homeassistant-config/pull/488) — chore: remove home-host/ and retire pve2 display-host references
- 2026-06-25 · [homeassistant-config#487](https://github.com/lentago/homeassistant-config/pull/487) — docs: retire pve2 display-host references in CLAUDE.md
- 2026-06-24 · [.github#9](https://github.com/lentago/.github/pull/9) — profile: tighten badge wall to attested stack + AI-delivery row + runbook link
- 2026-06-24 · [homeassistant-config#486](https://github.com/lentago/homeassistant-config/pull/486) — context-snapshot: 20260624-160008
- 2026-06-24 · [homeassistant-config#485](https://github.com/lentago/homeassistant-config/pull/485) — context-snapshot: 20260624-040010
- 2026-06-23 · [homeassistant-config#484](https://github.com/lentago/homeassistant-config/pull/484) — context-snapshot: 20260623-220008
- 2026-06-23 · [homeassistant-config#483](https://github.com/lentago/homeassistant-config/pull/483) — context-snapshot: 20260623-160001
- 2026-06-23 · [homeassistant-config#482](https://github.com/lentago/homeassistant-config/pull/482) — context-snapshot: 20260623-100001
- 2026-06-23 · [homeassistant-config#481](https://github.com/lentago/homeassistant-config/pull/481) — context-snapshot: 20260623-085052
- 2026-06-23 · [homeassistant-config#480](https://github.com/lentago/homeassistant-config/pull/480) — context-snapshot: 20260623-040001
- 2026-06-22 · [homeassistant-config#479](https://github.com/lentago/homeassistant-config/pull/479) — context-snapshot: 20260622-220001
- 2026-06-22 · [homeassistant-config#478](https://github.com/lentago/homeassistant-config/pull/478) — context-snapshot: 20260622-160001
- 2026-06-22 · [homeassistant-config#477](https://github.com/lentago/homeassistant-config/pull/477) — context-snapshot: 20260622-100001
- 2026-06-22 · [homeassistant-config#476](https://github.com/lentago/homeassistant-config/pull/476) — context-snapshot: 20260622-040001
- 2026-06-21 · [homeassistant-config#475](https://github.com/lentago/homeassistant-config/pull/475) — context-snapshot: 20260621-220001
- 2026-06-21 · [.github#8](https://github.com/lentago/.github/pull/8) — brand/avatars: add square (sharp-corner) variants
- 2026-06-21 · [.github#7](https://github.com/lentago/.github/pull/7) — profile: align org README to collective "we" voice
- 2026-06-21 · [.github#6](https://github.com/lentago/.github/pull/6) — brand: add canonical GitHub avatar marks (org &lt;pl:&gt;, personal &lt;cjp:&gt;)
- 2026-06-21 · [homeassistant-config#474](https://github.com/lentago/homeassistant-config/pull/474) — context-snapshot: 20260621-160001
- 2026-06-21 · [.github#5](https://github.com/lentago/.github/pull/5) — fleet-ops: sweep leftover branches via fleet-apply.sh --prune-branches
- 2026-06-21 · [homeassistant-config#473](https://github.com/lentago/homeassistant-config/pull/473) — context-snapshot: 20260621-100001
- 2026-06-21 · [homeassistant-config#472](https://github.com/lentago/homeassistant-config/pull/472) — context-snapshot: 20260621-040001
- 2026-06-20 · [repo-template#1](https://github.com/lentago/repo-template/pull/1) — Update SETUP.md fleet-ops paths to dotgithub/fleet-ops/
- 2026-06-20 · [.github#4](https://github.com/lentago/.github/pull/4) — Adopt fleet-ops as versioned tooling in the org meta-repo
- 2026-06-20 · [.github#3](https://github.com/lentago/.github/pull/3) — Add CLAUDE.md with Org Claude persona + fleet conventions
- 2026-06-20 · [homeassistant-config#471](https://github.com/lentago/homeassistant-config/pull/471) — context-snapshot: 20260620-220001
- 2026-06-20 · [homeassistant-config#470](https://github.com/lentago/homeassistant-config/pull/470) — context-snapshot: 20260620-160008
- 2026-06-20 · [homeassistant-config#469](https://github.com/lentago/homeassistant-config/pull/469) — context-snapshot: 20260620-100001
- 2026-06-20 · [homeassistant-config#468](https://github.com/lentago/homeassistant-config/pull/468) — context-snapshot: 20260620-040001
- 2026-06-20 · [reference-checker#46](https://github.com/lentago/reference-checker/pull/46) — feat(baseline): v6 production baseline — H10 functional check, regression gate, scoring calibration
- 2026-06-19 · [homeassistant-config#467](https://github.com/lentago/homeassistant-config/pull/467) — context-snapshot: 20260619-220001
- 2026-06-19 · [claytonia#20](https://github.com/lentago/claytonia/pull/20) — feat(cr-emit): add job_started one-shot event for fleet start markers
- 2026-06-19 · [drosera#92](https://github.com/lentago/drosera/pull/92) — fix(dashboards): key "Runners underway" by worker, window 20s→15s
- 2026-06-19 · [shared-workflows#10](https://github.com/lentago/shared-workflows/pull/10) — fix(claude-review): default allowed_bots to "*" so fleet bot PRs get reviewed
- 2026-06-19 · [claytonia#15](https://github.com/lentago/claytonia/pull/15) — feat(runner): pre-seed session id for live transcript runid labeling
- 2026-06-19 · [claytonia#14](https://github.com/lentago/claytonia/pull/14) — fix(cr-submit): make inbox filenames unique to prevent same-second collision
- 2026-06-19 · [reference-checker#44](https://github.com/lentago/reference-checker/pull/44) — feat(prompt): v6 auditor — journal legitimacy (H10) and scoring formula fix
- 2026-06-19 · [drosera#88](https://github.com/lentago/drosera/pull/88) — fix(dashboards): rekey "Runners underway" to count in-flight jobs by runid (#87)
- 2026-06-19 · [drosera#90](https://github.com/lentago/drosera/pull/90) — feat(dashboards): task start/end annotations on Runner Fleet dashboard
- 2026-06-19 · [claytonia#17](https://github.com/lentago/claytonia/pull/17) — feat(heartbeat): sub-second Loki timestamps + 10s job_running cadence
- 2026-06-19 · [drosera#86](https://github.com/lentago/drosera/pull/86) — ci(terraform): auto-apply dashboards on merge to main (S3-backed state)
- 2026-06-19 · [reference-checker#42](https://github.com/lentago/reference-checker/pull/42) — feat(test-sets): add real-article clean corpus for false-positive calibration
- 2026-06-19 · [homeassistant-config#466](https://github.com/lentago/homeassistant-config/pull/466) — context-snapshot: 20260619-160001
- 2026-06-19 · [reference-checker#41](https://github.com/lentago/reference-checker/pull/41) — feat(baseline): establish v5 production baseline — regression gate, H9 functional check
- 2026-06-19 · [drosera#85](https://github.com/lentago/drosera/pull/85) — fix(dashboards): set allValue=".*" on project/worker vars so "All" includes new projects/workers
- 2026-06-19 · [reference-checker#39](https://github.com/lentago/reference-checker/pull/39) — feat(prompt): ship v5 auditor — Heuristic 9 (temporal impossibility) + full COPE alignment
- 2026-06-19 · [drosera#82](https://github.com/lentago/drosera/pull/82) — feat(dashboards): per-worker stream-of-consciousness viewports (#80)
- 2026-06-19 · [drosera#83](https://github.com/lentago/drosera/pull/83) — feat(dashboards): color Runners Underway panel by model (#79)
- 2026-06-19 · [reference-checker#38](https://github.com/lentago/reference-checker/pull/38) — fix(test-sets): correct adversarial-30 trap index and recompute baseline metrics
- 2026-06-19 · [reference-checker#36](https://github.com/lentago/reference-checker/pull/36) — audit: adversarial-30 v4 baseline run with live web verification
- 2026-06-19 · [reference-checker#34](https://github.com/lentago/reference-checker/pull/34) — docs(test-sets): reconcile real-articles README with committed artifacts
- 2026-06-19 · [reference-checker#35](https://github.com/lentago/reference-checker/pull/35) — docs: sync README and heuristics.md to v4
- 2026-06-19 · [homeassistant-config#465](https://github.com/lentago/homeassistant-config/pull/465) — context-snapshot: 20260619-100001
- 2026-06-19 · [homeassistant-config#464](https://github.com/lentago/homeassistant-config/pull/464) — context-snapshot: 20260619-040001
- 2026-06-18 · [homeassistant-config#463](https://github.com/lentago/homeassistant-config/pull/463) — context-snapshot: 20260618-220001
- 2026-06-18 · [homeassistant-config#462](https://github.com/lentago/homeassistant-config/pull/462) — context-snapshot: 20260618-160001
- 2026-06-18 · [site-icecreamtofightwith-com#114](https://github.com/lentago/site-icecreamtofightwith-com/pull/114) — Add hidden Pitzi Labs easter-egg link in hero tagline
- 2026-06-18 · [homeassistant-config#461](https://github.com/lentago/homeassistant-config/pull/461) — context-snapshot: 20260618-100001
- 2026-06-18 · [homeassistant-config#460](https://github.com/lentago/homeassistant-config/pull/460) — context-snapshot: 20260618-040001
- 2026-06-18 · [claytonia#11](https://github.com/lentago/claytonia/pull/11) — feat(provision): bake the live fleet transcript shipper into the worker image
- 2026-06-18 · [drosera#78](https://github.com/lentago/drosera/pull/78) — fix(alloy): self-label the transcript shipper via constants.hostname
- 2026-06-17 · [drosera#77](https://github.com/lentago/drosera/pull/77) — feat(fleet): live "stream of consciousness" reasoning viewport (#71)
- 2026-06-17 · [drosera#76](https://github.com/lentago/drosera/pull/76) — fix(alloy): trim trailing newline from ha_token with string.trim_space
- 2026-06-17 · [drosera#75](https://github.com/lentago/drosera/pull/75) — docs(readme): add Loki output contract section
- 2026-06-17 · [homeassistant-config#459](https://github.com/lentago/homeassistant-config/pull/459) — Remove the Screen Time dashboard (Roku device is gone)
- 2026-06-17 · [shared-workflows#9](https://github.com/lentago/shared-workflows/pull/9) — chore: add MIT LICENSE
- 2026-06-17 · [homeassistant-config#458](https://github.com/lentago/homeassistant-config/pull/458) — chore: add MIT LICENSE
- 2026-06-17 · [claytonia#9](https://github.com/lentago/claytonia/pull/9) — chore: add MIT LICENSE
- 2026-06-17 · [homeassistant-config#457](https://github.com/lentago/homeassistant-config/pull/457) — Prune resolved allowlist entries + drop dead Roku refs from screen-time
- 2026-06-17 · [homeassistant-config#456](https://github.com/lentago/homeassistant-config/pull/456) — context-snapshot: 20260617-230716
- 2026-06-17 · [homeassistant-config#455](https://github.com/lentago/homeassistant-config/pull/455) — fix(context-dump): pass configs via stdin to avoid ARG_MAX in build_dashboards_storage
- 2026-06-17 · [.github#2](https://github.com/lentago/.github/pull/2) — Re-scope language census to PitziLabs org repos only
- 2026-06-17 · [drosera#74](https://github.com/lentago/drosera/pull/74) — fix(dashboards): default the runner fleet to a 3h window
- 2026-06-17 · [.github#1](https://github.com/lentago/.github/pull/1) — Add periodic language census report
- 2026-06-17 · [homeassistant-config#454](https://github.com/lentago/homeassistant-config/pull/454) — fix(context-dump): make snapshot step non-fatal, replace xxd with busybox-safe od (#453)
- 2026-06-17 · [drosera#73](https://github.com/lentago/drosera/pull/73) — feat(dashboards): add "Local sessions underway" pane below runners
- 2026-06-17 · [homeassistant-config#452](https://github.com/lentago/homeassistant-config/pull/452) — feat(dashboard): stack climate dials, widen weather, drop Home Status (#445, #446, #448)
- 2026-06-17 · [drosera#72](https://github.com/lentago/drosera/pull/72) — feat(dashboards): runner-fleet layout — underway on top, full-width timeseries
- 2026-06-17 · [drosera#70](https://github.com/lentago/drosera/pull/70) — feat(dashboards): stack the runner-underway panel (concurrency view)
- 2026-06-17 · [drosera#69](https://github.com/lentago/drosera/pull/69) — fix(dashboards): draw runner-underway as continuous bands, not dots
- 2026-06-17 · [homeassistant-config#451](https://github.com/lentago/homeassistant-config/pull/451) — feat(dashboard): remove TV card, square media tiles, regroup openings
- 2026-06-17 · [drosera#68](https://github.com/lentago/drosera/pull/68) — feat(dashboards): add "Runners underway" timeseries to runner fleet
- 2026-06-17 · [claytonia#7](https://github.com/lentago/claytonia/pull/7) — feat(runner): emit job_running heartbeat to Loki while a job is in flight
- 2026-06-17 · [homeassistant-config#449](https://github.com/lentago/homeassistant-config/pull/449) — feat(dashboard): room-level dimmers, inline light sliders, hallway→Family Room
- 2026-06-17 · [homeassistant-config#439](https://github.com/lentago/homeassistant-config/pull/439) — Ignore legacy kiosk-*.png display frame grabs
- 2026-06-17 · [homeassistant-config#438](https://github.com/lentago/homeassistant-config/pull/438) — Add in-HA button to seed UI-editable dashboards from YAML
- 2026-06-17 · [homeassistant-config#437](https://github.com/lentago/homeassistant-config/pull/437) — Operationalize dashboard import as a reusable ad-hoc CLI
- 2026-06-17 · [homeassistant-config#436](https://github.com/lentago/homeassistant-config/pull/436) — context-snapshot: 20260617-160001
- 2026-06-17 · [homeassistant-config#435](https://github.com/lentago/homeassistant-config/pull/435) — feat(dashboard): promote home dashboard; retire kiosk term repo-wide
- 2026-06-17 · [homeassistant-config#430](https://github.com/lentago/homeassistant-config/pull/430) — context-snapshot: 20260617-100001
- 2026-06-17 · [homeassistant-config#429](https://github.com/lentago/homeassistant-config/pull/429) — context-snapshot: 20260617-040001
- 2026-06-16 · [solidago#67](https://github.com/lentago/solidago/pull/67) — Host the Pitzi Labs landing site on the shared platform (modules/site)
- 2026-06-16 · [homeassistant-config#428](https://github.com/lentago/homeassistant-config/pull/428) — context-snapshot: 20260616-220001
- 2026-06-16 · [drosera#67](https://github.com/lentago/drosera/pull/67) — docs(terraform): fix datasource-UID rewrite description in README
- 2026-06-16 · [drosera#66](https://github.com/lentago/drosera/pull/66) — docs(terraform): correct datasource-UID rewrite description in README
- 2026-06-16 · [drosera#65](https://github.com/lentago/drosera/pull/65) — fix(dashboards): correct Cloud datasource UIDs + zero-fill runner-fleet panels
- 2026-06-16 · [drosera#64](https://github.com/lentago/drosera/pull/64) — Reconcile dashboards folder title to "Homelab"
- 2026-06-16 · [solidago#66](https://github.com/lentago/solidago/pull/66) — ci: bump GHA actions to Node 24-compatible majors
- 2026-06-16 · [reference-checker#31](https://github.com/lentago/reference-checker/pull/31) — Add .gitignore
- 2026-06-16 · [claytonia#6](https://github.com/lentago/claytonia/pull/6) — docs: roadmap — live job radiator (amber→green job board with PR links)
- 2026-06-16 · [drosera#62](https://github.com/lentago/drosera/pull/62) — Claude Runner Fleet: add Local sessions row (job=claude_local)
- 2026-06-16 · [betula#52](https://github.com/lentago/betula/pull/52) — docs: add Loki output contract section to README
- 2026-06-16 · [drosera#61](https://github.com/lentago/drosera/pull/61) — feat: add scripts/check-loki-labels.sh
- 2026-06-16 · [drosera#63](https://github.com/lentago/drosera/pull/63) — fix(dashboards): live GitHub open-PR queue + reconcile TF state drift
- 2026-06-16 · [homeassistant-config#427](https://github.com/lentago/homeassistant-config/pull/427) — context-snapshot: 20260616-160001
- 2026-06-16 · [homeassistant-config#426](https://github.com/lentago/homeassistant-config/pull/426) — context-snapshot: 20260616-100001
- 2026-06-16 · [homeassistant-config#425](https://github.com/lentago/homeassistant-config/pull/425) — context-snapshot: 20260616-040001
- 2026-06-16 · [claytonia#4](https://github.com/lentago/claytonia/pull/4) — Never let a runner-bot PR auto-merge (override repo conventions)
- 2026-06-16 · [homeassistant-config#424](https://github.com/lentago/homeassistant-config/pull/424) — fix(dashboards): remove unavailable Proxmox button.* grids from haos/pve/pve3 (#376)
- 2026-06-15 · [claytonia#3](https://github.com/lentago/claytonia/pull/3) — Fix model precedence (project beats global) + add cr-submit -m
- 2026-06-15 · [claytonia#2](https://github.com/lentago/claytonia/pull/2) — Capture each job's full reasoning transcript to the NAS
- 2026-06-15 · [claytonia#1](https://github.com/lentago/claytonia/pull/1) — Onboard bullpen to PitziLabs fleet standards
- 2026-06-15 · [homeassistant-config#423](https://github.com/lentago/homeassistant-config/pull/423) — context-snapshot: 20260615-220001
- 2026-06-15 · [drosera#60](https://github.com/lentago/drosera/pull/60) — Add Claude Runner Fleet dashboard (gitops-managed)
- 2026-06-15 · [reference-checker#30](https://github.com/lentago/reference-checker/pull/30) — Add two real-article audit reports + DOI-less metadata-mismatch heuristic
- 2026-06-15 · [site-icecreamtofightwith-com#113](https://github.com/lentago/site-icecreamtofightwith-com/pull/113) — docs: fix stale front_matter directory tree in README
- 2026-06-15 · [homeassistant-config#422](https://github.com/lentago/homeassistant-config/pull/422) — context-snapshot: 20260615-160008
- 2026-06-15 · [homeassistant-config#421](https://github.com/lentago/homeassistant-config/pull/421) — Trim Origin/Prompt-Origin restatement to a pointer (now fleet-wide)
- 2026-06-15 · [shared-workflows#8](https://github.com/lentago/shared-workflows/pull/8) — Make ## Origin + Prompt-Origin: a fleet-wide PR convention
- 2026-06-15 · [homeassistant-config#420](https://github.com/lentago/homeassistant-config/pull/420) — Fix review prompt: Home Assistant config, not bash/Terraform
- 2026-06-15 · [solidago#65](https://github.com/lentago/solidago/pull/65) — Fix review prompt: Terraform/AWS focus, not workstation bash
- 2026-06-15 · [site-icecreamtofightwith-com#112](https://github.com/lentago/site-icecreamtofightwith-com/pull/112) — Fix review prompt: ice-cream cookbook, not bash/Terraform
- 2026-06-15 · [reference-checker#29](https://github.com/lentago/reference-checker/pull/29) — Fix review prompt: forensic citation auditor, not bash/Terraform
- 2026-06-14 · [homeassistant-config#419](https://github.com/lentago/homeassistant-config/pull/419) — context-snapshot: 20260614-220001
- 2026-06-14 · [homeassistant-config#418](https://github.com/lentago/homeassistant-config/pull/418) — context-snapshot: 20260614-160000
- 2026-06-14 · [homeassistant-config#417](https://github.com/lentago/homeassistant-config/pull/417) — context-snapshot: 20260614-100000
- 2026-06-14 · [homeassistant-config#416](https://github.com/lentago/homeassistant-config/pull/416) — context-snapshot: 20260614-064054
- 2026-06-14 · [homeassistant-config#415](https://github.com/lentago/homeassistant-config/pull/415) — Office scenes: add Blue + Red Desk flicker, purge yellow/green/purple candles
- 2026-06-14 · [homeassistant-config#414](https://github.com/lentago/homeassistant-config/pull/414) — context-snapshot: 20260614-040001
- 2026-06-14 · [homeassistant-config#413](https://github.com/lentago/homeassistant-config/pull/413) — Kiosk: one section per column to eliminate inter-row gaps
- 2026-06-14 · [homeassistant-config#412](https://github.com/lentago/homeassistant-config/pull/412) — Kiosk: fill the wall display — 5 columns, unified tile language, no camera

**142 issues closed**

- 2026-07-13 · [.github#40](https://github.com/lentago/.github/issues/40) — Publish incident reports as a periodic fleet report (incident register)
- 2026-07-12 · [site-icecreamtofightwith-com#138](https://github.com/lentago/site-icecreamtofightwith-com/issues/138) — Scroll-up at the top of a page should load the previous page (mirror of the #133 auto-advance)
- 2026-07-12 · [site-icecreamtofightwith-com#133](https://github.com/lentago/site-icecreamtofightwith-com/issues/133) — Scroll-linked reading: auto-advance to the next page at end of scroll, keep the filmstrip in sync
- 2026-07-12 · [site-icecreamtofightwith-com#131](https://github.com/lentago/site-icecreamtofightwith-com/issues/131) — Field diagrams: re-audit the logic-check, then place each figure inline next to the step it explains
- 2026-07-12 · [site-icecreamtofightwith-com#132](https://github.com/lentago/site-icecreamtofightwith-com/issues/132) — Homepage: add a large rendered title graphic that pushes the intro text below the fold
- 2026-07-12 · [site-icecreamtofightwith-com#130](https://github.com/lentago/site-icecreamtofightwith-com/issues/130) — Front-of-book cleanup: retire Essay numbering, move Final Thoughts ahead of recipes, de-swear the tagline
- 2026-07-10 · [solidago#80](https://github.com/lentago/solidago/issues/80) — Tear down the retired pitzilabs preview site (module.site_pitzilabs)
- 2026-07-10 · [betula#84](https://github.com/lentago/betula/issues/84) — ALB parser rejects real 34-field log lines (raises ValueError, drops every event)
- 2026-07-10 · [solidago#110](https://github.com/lentago/solidago/issues/110) — CI terraform apply fails: deploy role lacks lambda:* (blocks ALB-log shipper + all merges to main)
- 2026-07-10 · [solidago#108](https://github.com/lentago/solidago/issues/108) — Deploy the ALB-access-log → Axiom shipper (betula AWS client)
- 2026-07-09 · [betula#80](https://github.com/lentago/betula/issues/80) — AWS client: collect ALB access logs from S3 into Axiom (solidago visitor-source telemetry)
- 2026-07-09 · [solidago#106](https://github.com/lentago/solidago/issues/106) — Enable ALB access logs to S3 for visitor-source telemetry (betula/Axiom ingestion)
- 2026-07-09 · [music-curator#9](https://github.com/lentago/music-curator/issues/9) — Add an always-on gate check so auto-merge can arm (last .github#27 gap; sequence with the Obsidian wiki-manager productization)
- 2026-07-08 · [claytonia#57](https://github.com/lentago/claytonia/issues/57) — Update Terraform backend to solidago-tfstate-* after shared-state migration
- 2026-07-08 · [kalmia#44](https://github.com/lentago/kalmia/issues/44) — Update Terraform backend to solidago-tfstate-* after shared-state migration
- 2026-07-08 · [drosera#142](https://github.com/lentago/drosera/issues/142) — Update Terraform backend to solidago-tfstate-* after shared-state migration
- 2026-07-08 · [solidago#103](https://github.com/lentago/solidago/issues/103) — Migrate shared Terraform state backend foundry-tfstate-* → solidago-tfstate-*
- 2026-07-08 · [betula#78](https://github.com/lentago/betula/issues/78) — Update Axiom ingest-header secret reference after solidago rename
- 2026-07-08 · [drosera#140](https://github.com/lentago/drosera/issues/140) — Align foundry-* references to solidago-* after solidago rename
- 2026-07-08 · [site-icecreamtofightwith-com#125](https://github.com/lentago/site-icecreamtofightwith-com/issues/125) — Align foundry-dev-* AWS resource references to solidago after solidago rename
- 2026-07-08 · [solidago#102](https://github.com/lentago/solidago/issues/102) — Rename internal foundry-* application resources → solidago-*
- 2026-07-07 · [claytonia#54](https://github.com/lentago/claytonia/issues/54) — Consume the kalmia runner image: cut workers from claytonia-runner-v1, retire provision/01–05
- 2026-07-07 · [.github#27](https://github.com/lentago/.github/issues/27) — Rulesets have no required status checks — auto-merge can't arm and the fleet convention silently degrades
- 2026-07-07 · [kalmia#36](https://github.com/lentago/kalmia/issues/36) — Image forge: bake the bullpen runner template as the first versioned image artifact
- 2026-07-07 · [claytonia#51](https://github.com/lentago/claytonia/issues/51) — Own runner capacity: adopt the worker-pool guest layer from kalmia (Terraform, Proxmox as first platform client)
- 2026-07-07 · [kalmia#37](https://github.com/lentago/kalmia/issues/37) — Release the bullpen runner pool from the guest layer — capacity ownership moves to claytonia
- 2026-07-07 · [kalmia#38](https://github.com/lentago/kalmia/issues/38) — Terraform fights operator power state on pet VMs — ignore `started` on workstations and testbeds
- 2026-07-06 · [kalmia#33](https://github.com/lentago/kalmia/issues/33) — Terraform: scale the bullpen out by two runners (claude-runner-4/-5, LXC 116/117)
- 2026-07-06 · [site-lentago-dev#32](https://github.com/lentago/site-lentago-dev/issues/32) — Rename Suite anchor #work → #systems for nav consistency
- 2026-07-06 · [site-lentago-dev#31](https://github.com/lentago/site-lentago-dev/issues/31) — Wire the consult form so ./send is not a dead end
- 2026-07-06 · [site-lentago-dev#30](https://github.com/lentago/site-lentago-dev/issues/30) — Footer version string goes stale (make it build-time)
- 2026-07-06 · [site-lentago-dev#28](https://github.com/lentago/site-lentago-dev/issues/28) — Nav "Writing" links to the Operating Principles section
- 2026-07-06 · [site-lentago-dev#29](https://github.com/lentago/site-lentago-dev/issues/29) — Add Open Graph / Twitter Card meta + og:image for social sharing
- 2026-07-06 · [site-lentago-dev#26](https://github.com/lentago/site-lentago-dev/issues/26) — Suite: give each system row its botanical genus mark
- 2026-07-05 · [kalmia#31](https://github.com/lentago/kalmia/issues/31) — Terraform cleanup: pin the PVE CA (drop insecure = true)
- 2026-07-05 · [kalmia#28](https://github.com/lentago/kalmia/issues/28) — Terraform phase 3: import pve5 guests + HAOS VM 100 (last, prevent_destroy)
- 2026-07-05 · [kalmia#25](https://github.com/lentago/kalmia/issues/25) — Terraform phase 2: LAN apply-on-merge — self-hosted runner LXC + OIDC state role + terraform workflow
- 2026-07-05 · [kalmia#23](https://github.com/lentago/kalmia/issues/23) — Terraform phase 1: import the five pve4 LXCs (110–114) to a clean plan
- 2026-07-05 · [kalmia#21](https://github.com/lentago/kalmia/issues/21) — Proxmox guest lifecycle under Terraform — phase 0: provider scaffolding, auth, state backend
- 2026-07-04 · [solidago#92](https://github.com/lentago/solidago/issues/92) — Phase 2: ship ECS container logs to Axiom via FireLens
- 2026-07-04 · [solidago#90](https://github.com/lentago/solidago/issues/90) — Phase 1: cross-account read-only IAM role for the Grafana Cloud CloudWatch datasource (Part A)
- 2026-07-04 · [drosera#132](https://github.com/lentago/drosera/issues/132) — Phase 1: Solidago CloudWatch datasource + platform-health dashboard (Part B)
- 2026-07-04 · [site-lentago-dev#20](https://github.com/lentago/site-lentago-dev/issues/20) — Align repo contents with site-lentago-dev rename
- 2026-07-04 · [site-icecreamtofightwith-com#120](https://github.com/lentago/site-icecreamtofightwith-com/issues/120) — Align repo contents with site-icecreamtofightwith-com rename
- 2026-07-04 · [solidago#88](https://github.com/lentago/solidago/issues/88) — Codify site-repo rename dual-trust in app OIDC role
- 2026-07-04 · [betula#72](https://github.com/lentago/betula/issues/72) — Rebrand repo to Betula — Lentago Labs log capture-and-archive layer
- 2026-07-04 · [claytonia#45](https://github.com/lentago/claytonia/issues/45) — Rebrand repo to Claytonia — Lentago Labs agent-fleet system
- 2026-07-04 · [claytonia#43](https://github.com/lentago/claytonia/issues/43) — Update homelab-observability references to drosera (repo renamed 2026-07-04)
- 2026-07-04 · [drosera#127](https://github.com/lentago/drosera/issues/127) — Rebrand repo to Drosera — Lentago Labs observability suite
- 2026-07-04 · [kalmia#18](https://github.com/lentago/kalmia/issues/18) — Rebrand repo to Kalmia — Lentago Labs provisioning system
- 2026-07-03 · [drosera#113](https://github.com/lentago/drosera/issues/113) — Resolve raw IPs to device/host names across dashboards (inventory feed + join transformations)
- 2026-07-03 · [drosera#111](https://github.com/lentago/drosera/issues/111) — device_ip variable is an empty custom dropdown — per-device filtering impossible on DNS & Security and Traffic & Devices
- 2026-07-03 · [drosera#108](https://github.com/lentago/drosera/issues/108) — Tables show 'Value #A' column header; Top-N sort and cell coloring silently broken (9 panels, 3 dashboards)
- 2026-07-03 · [drosera#112](https://github.com/lentago/drosera/issues/112) — Claude Runner Fleet: 'Jobs over time by status' legend shows unlabeled 'Value' series from or vector(0) fallback
- 2026-07-03 · [drosera#109](https://github.com/lentago/drosera/issues/109) — Three timeseries panels render fully blank: legacy legend {displayMode: hidden} without placement breaks panel init
- 2026-07-03 · [drosera#110](https://github.com/lentago/drosera/issues/110) — Traffic & Devices: 'Connections by Protocol' pie shows a single 'Value #A' slice instead of per-protocol breakdown
- 2026-07-03 · [betula#67](https://github.com/lentago/betula/issues/67) — CRITICAL: raw 'crontab user_crontab' install clobbers Firewalla's system cron jobs
- 2026-07-03 · [betula#65](https://github.com/lentago/betula/issues/65) — Healthcheck 'no output in 5m' branch restarts a healthy container every 10 minutes
- 2026-07-02 · [betula#63](https://github.com/lentago/betula/issues/63) — Ship Firewalla host + Zeek process metrics to Axiom (system_metrics_export.sh)
- 2026-07-02 · [betula#61](https://github.com/lentago/betula/issues/61) — Healthcheck false positive: bare docker calls fail under cron, force-recreating the container every 5 minutes
- 2026-07-02 · [betula#10](https://github.com/lentago/betula/issues/10) — Pull-based GitOps deployment
- 2026-07-02 · [betula#4](https://github.com/lentago/betula/issues/4) — Add support for additional Zeek log types
- 2026-07-02 · [betula#5](https://github.com/lentago/betula/issues/5) — Rotate health check and cleanup log files
- 2026-07-02 · [betula#13](https://github.com/lentago/betula/issues/13) — Eliminate stale device lookup records in Axiom queries
- 2026-07-02 · [homeassistant-config#433](https://github.com/lentago/homeassistant-config/issues/433) — Add room-level light controls (on/off + dimmers) to the Home dashboard
- 2026-07-02 · [claytonia#37](https://github.com/lentago/claytonia/issues/37) — Failed jobs are silent: surface a signal when a run lands in failed/
- 2026-07-02 · [solidago#17](https://github.com/lentago/solidago/issues/17) — Upgrade GitHub Actions to Node.js 24-compatible versions
- 2026-07-02 · [solidago#12](https://github.com/lentago/solidago/issues/12) — Standardize Terraform resource naming convention (this vs main)
- 2026-07-02 · [solidago#16](https://github.com/lentago/solidago/issues/16) — Refactor VPC subnets from count to for_each
- 2026-07-02 · [homeassistant-config#434](https://github.com/lentago/homeassistant-config/issues/434) — Stop media now-playing cards from collapsing when idle (only variable-height element on the page)
- 2026-07-01 · [homeassistant-config#432](https://github.com/lentago/homeassistant-config/issues/432) — Adopt a single-master / two-clone scheme for the Home dashboard
- 2026-07-01 · [homeassistant-config#332](https://github.com/lentago/homeassistant-config/issues/332) — binary_sensor.basement_kitchen_door + battery sensor both unavailable
- 2026-07-01 · [site-lentago-dev#11](https://github.com/lentago/site-lentago-dev/issues/11) — Scale the footer wordmark to match the enlarged nav lockup
- 2026-07-01 · [.github#18](https://github.com/lentago/.github/issues/18) — Decide whether to seed org-default community-health files
- 2026-07-01 · [.github#17](https://github.com/lentago/.github/issues/17) — Restore logos on the AWS / ECS Fargate / CloudWatch profile badges
- 2026-07-01 · [.github#16](https://github.com/lentago/.github/issues/16) — Finish the Lentago rebrand of the public org profile (README, banner, avatar variant)
- 2026-07-01 · [site-lentago-dev#10](https://github.com/lentago/site-lentago-dev/issues/10) — Promote the site to lentago.dev (Phase 2 go-live)
- 2026-07-01 · [homeassistant-config#376](https://github.com/lentago/homeassistant-config/issues/376) — Proxmox button orphans across haos/pve/pve3 — same re-registration pattern as #333
- 2026-07-01 · [homeassistant-config#450](https://github.com/lentago/homeassistant-config/issues/450) — home-preview --url path aborts on false-negative `which display-show` over non-interactive SSH
- 2026-07-01 · [solidago#14](https://github.com/lentago/solidago/issues/14) — Implement selective teardown/standup scripts for cost management
- 2026-07-01 · [music-curator#4](https://github.com/lentago/music-curator/issues/4) — Add an engineering spine: machine-checkable schema + validator for the taste-profile JSON
- 2026-07-01 · [site-lentago-dev#9](https://github.com/lentago/site-lentago-dev/issues/9) — Correct stale deploy-not-yet-wired language in CLAUDE.md
- 2026-07-01 · [solidago#15](https://github.com/lentago/solidago/issues/15) — Upgrade state bucket encryption from AES256 to KMS CMK
- 2026-07-01 · [claytonia#5](https://github.com/lentago/claytonia/issues/5) — run-job: fail a project job that should have opened a PR but didn't
- 2026-07-01 · [claytonia#12](https://github.com/lentago/claytonia/issues/12) — cr-submit: --help (and bare/unknown-flag invocations) silently queue a junk ad-hoc job instead of printing usage
- 2026-07-01 · [shared-workflows#14](https://github.com/lentago/shared-workflows/issues/14) — claude-review CI bot fails to post a review across fleet PRs (turn-cap exhaustion + intermittent 0-byte response)
- 2026-07-01 · [music-curator#5](https://github.com/lentago/music-curator/issues/5) — Fix data-integrity drift and unmerged duplicate anchors in the flagship example profile
- 2026-07-01 · [solidago#13](https://github.com/lentago/solidago/issues/13) — Replace deprecated dynamodb_table backend param with use_lockfile
- 2026-07-01 · [betula#6](https://github.com/lentago/betula/issues/6) — Harden deploy.sh for idempotent re-runs
- 2026-07-01 · [claytonia#8](https://github.com/lentago/claytonia/issues/8) — cr-submit -m flag silently ignored — project registry model overrides explicit request
- 2026-06-30 · [kalmia#11](https://github.com/lentago/kalmia/issues/11) — First real-target test run: playbook fails to start + entry-path bugs
- 2026-06-30 · [kalmia#8](https://github.com/lentago/kalmia/issues/8) — Finish the crostini profile (sudo + ~/.local/bin + CLI-only Docker)
- 2026-06-30 · [kalmia#6](https://github.com/lentago/kalmia/issues/6) — Add power role: TLP + ThinkPad charge thresholds + fwupd
- 2026-06-30 · [kalmia#4](https://github.com/lentago/kalmia/issues/4) — Drop remote desktop (XRDP) capability entirely
- 2026-06-30 · [kalmia#2](https://github.com/lentago/kalmia/issues/2) — Fedora dnf-repo wiring for Docker and VS Code
- 2026-06-28 · [homeassistant-config#491](https://github.com/lentago/homeassistant-config/issues/491) — Home dashboard presence tiles bound to stale WiFi device_trackers — show wrong state when home
- 2026-06-25 · [drosera#94](https://github.com/lentago/drosera/issues/94) — Fleet dashboard panel-11 "Local sessions underway" collapses to a per-worker boolean — switch to distinct-session count
- 2026-06-20 · [reference-checker#45](https://github.com/lentago/reference-checker/issues/45) — Establish v6 baseline: validate H10 detection, scoring recalibration, and adversarial-30 regression
- 2026-06-19 · [claytonia#18](https://github.com/lentago/claytonia/issues/18) — run-job: emit a one-shot job_started event (fleet underway start-markers)
- 2026-06-19 · [drosera#91](https://github.com/lentago/drosera/issues/91) — fix(dashboard): "Runners underway" over-counts on back-to-back handoffs — key by worker, not runid
- 2026-06-19 · [claytonia#10](https://github.com/lentago/claytonia/issues/10) — Pre-seed Claude session id so the live fleet transcript stream can carry a runid label
- 2026-06-19 · [claytonia#13](https://github.com/lentago/claytonia/issues/13) — cr-submit: same-second same-project submits collide on inbox filename → silent job loss
- 2026-06-19 · [reference-checker#43](https://github.com/lentago/reference-checker/issues/43) — Scoring formula: D×3 base cost makes the headline score misleading for large reference lists
- 2026-06-19 · [reference-checker#7](https://github.com/lentago/reference-checker/issues/7) — [v4] Implement predatory journal flagging
- 2026-06-19 · [drosera#87](https://github.com/lentago/drosera/issues/87) — fix(dashboard): "Runners underway" counts (worker×model) over 2m, not concurrent jobs
- 2026-06-19 · [drosera#89](https://github.com/lentago/drosera/issues/89) — feat(dashboards): task start/end markers on the Runners underway pane (annotations)
- 2026-06-19 · [claytonia#16](https://github.com/lentago/claytonia/issues/16) — feat(heartbeat): sub-second Loki timestamps + 10s job_running cadence
- 2026-06-19 · [reference-checker#3](https://github.com/lentago/reference-checker/issues/3) — Add real-article reference lists to test-sets/real-articles/
- 2026-06-19 · [reference-checker#4](https://github.com/lentago/reference-checker/issues/4) — Add sample audit reports to reports/
- 2026-06-19 · [reference-checker#40](https://github.com/lentago/reference-checker/issues/40) — Establish v5 baseline: run v5 against adversarial-30, temporal-impossibility, and real-articles
- 2026-06-19 · [drosera#84](https://github.com/lentago/drosera/issues/84) — fix(dashboards): set allValue=".*" on project/worker vars so "All" includes new projects/workers
- 2026-06-19 · [reference-checker#9](https://github.com/lentago/reference-checker/issues/9) — [v4] Align recommendations with COPE investigation flowcharts
- 2026-06-19 · [reference-checker#6](https://github.com/lentago/reference-checker/issues/6) — [v4] Implement temporal impossibility checks
- 2026-06-19 · [drosera#80](https://github.com/lentago/drosera/issues/80) — Per-agent viewports for the fleet stream of consciousness (one pane per worker)
- 2026-06-19 · [drosera#79](https://github.com/lentago/drosera/issues/79) — Color the 'Runners underway' pane by model (opus / sonnet / haiku)
- 2026-06-19 · [reference-checker#37](https://github.com/lentago/reference-checker/issues/37) — test-sets/adversarial-30: trap-index ground-truth errors surfaced by the v4 baseline run
- 2026-06-19 · [drosera#81](https://github.com/lentago/drosera/issues/81) — Correlate the live reasoning stream with the bullpen runid (set session-id up front, stamp it on the events)
- 2026-06-19 · [reference-checker#13](https://github.com/lentago/reference-checker/issues/13) — Run fresh adversarial-30 test with v3 prompt and commit report
- 2026-06-19 · [reference-checker#33](https://github.com/lentago/reference-checker/issues/33) — test-sets: reconcile real-articles README table with files actually on disk
- 2026-06-19 · [reference-checker#32](https://github.com/lentago/reference-checker/issues/32) — docs: sync README to v4 (8 heuristics; sneaked + COPE shipped, not planned)
- 2026-06-19 · [reference-checker#12](https://github.com/lentago/reference-checker/issues/12) — Choose and apply a license
- 2026-06-19 · [reference-checker#5](https://github.com/lentago/reference-checker/issues/5) — [v4] Implement sneaked-reference detection
- 2026-06-19 · [reference-checker#2](https://github.com/lentago/reference-checker/issues/2) — Merge project-scaffold branch into main
- 2026-06-17 · [drosera#71](https://github.com/lentago/drosera/issues/71) — Live agent-reasoning viewport on the Claude Runner Fleet dashboard (Alloy → Loki → Grafana)
- 2026-06-17 · [drosera#36](https://github.com/lentago/drosera/issues/36) — Alloy HA scrape silently fails when alloy/ha_token has a trailing newline
- 2026-06-17 · [drosera#43](https://github.com/lentago/drosera/issues/43) — Docs: add "Loki output contract" section to README (sister change in firewalla-axiom-pipeline)
- 2026-06-17 · [drosera#39](https://github.com/lentago/drosera/issues/39) — Probe target drift: ap-office IP changed; pluto retired (now Neptune)
- 2026-06-17 · [homeassistant-config#453](https://github.com/lentago/homeassistant-config/issues/453) — ha-context-dump.sh: build_dashboards_storage rc 126 (E2BIG) — passes ~304KB storage-dashboard configs via jq --argjson over ARG_MAX
- 2026-06-17 · [homeassistant-config#448](https://github.com/lentago/homeassistant-config/issues/448) — Drop the Home Status section and its cards
- 2026-06-17 · [homeassistant-config#446](https://github.com/lentago/homeassistant-config/issues/446) — Weather: span the weather card across a couple of columns
- 2026-06-17 · [homeassistant-config#445](https://github.com/lentago/homeassistant-config/issues/445) — Climate: shrink thermostats and stack upstairs/downstairs vertically
- 2026-06-17 · [homeassistant-config#447](https://github.com/lentago/homeassistant-config/issues/447) — Openings: group doors, place garage doors adjacent, group motion sensors
- 2026-06-17 · [homeassistant-config#444](https://github.com/lentago/homeassistant-config/issues/444) — Media: keep now-playing cards square, don't collapse them
- 2026-06-17 · [homeassistant-config#443](https://github.com/lentago/homeassistant-config/issues/443) — Media: remove Play Room TV card and retire the Roku integration
- 2026-06-17 · [homeassistant-config#442](https://github.com/lentago/homeassistant-config/issues/442) — Lights: treat upstairs & downstairs hallway lights as part of the Family Room
- 2026-06-17 · [homeassistant-config#441](https://github.com/lentago/homeassistant-config/issues/441) — Lights: inline click-drag dimmers for individual lights
- 2026-06-17 · [homeassistant-config#440](https://github.com/lentago/homeassistant-config/issues/440) — Lights: whole-room controls with dimmer support
- 2026-06-17 · [homeassistant-config#431](https://github.com/lentago/homeassistant-config/issues/431) — Promote kiosk dashboard to default Home; retire the "kiosk" term repo-wide
- 2026-06-16 · [solidago#53](https://github.com/lentago/solidago/issues/53) — Bump GitHub Actions to Node 24-compatible versions before 2026-09-16
- 2026-06-16 · [reference-checker#14](https://github.com/lentago/reference-checker/issues/14) — Add .gitignore
- 2026-06-16 · [betula#42](https://github.com/lentago/betula/issues/42) — Docs: add "Loki output contract" section to README (sister change in homelab-observability)
- 2026-06-16 · [drosera#44](https://github.com/lentago/drosera/issues/44) — Add scripts/check-loki-labels.sh — alert if expected log_source values stop appearing

---

## Code census

**The lens:** a `CLAUDE.md` (and its kin — `AGENTS.md`, skill `SKILL.md`, and the LLM prompt-programs that *are* a tool's logic) is an instruction set maintained for hygiene, so it's counted as **natural-language code**. Documentation, content/data, and community-health markdown are tallied separately and excluded from the code total, as are data payloads and generated files. This is a deliberate re-cut of the canonical [`metrics/language-census.md`](../metrics/language-census.md), which instead counts all Markdown/JSON/HTML as code.

### Languages

cloc *code* lines (blank + comment excluded). Shell folds Bourne + Bash. Instruction-markdown is promoted into the count (**bold**); the excluded buckets sit below the total.

| # | Language | Code | Files | Share |
|---|----------|-----:|------:|------:|
| 1 | JSON | 8,325 | 25 | 24.1% |
| 2 | YAML | 8,121 | 127 | 23.5% |
| 3 | HCL | 5,425 | 99 | 15.7% |
| 4 | Shell (Bourne + Bash) | 4,569 | 54 | 13.2% |
| 5 | **Instructions (CLAUDE.md family + prompt-programs)** | 3,098 | 18 | 9.0% |
| 6 | Python | 2,836 | 19 | 8.2% |
| 7 | JSX | 851 | 10 | 2.5% |
| 8 | JavaScript | 773 | 7 | 2.2% |
| 9 | TypeScript | 304 | 7 | 0.9% |
| 10 | CSS | 258 | 7 | 0.7% |
| 11 | Other (TOML / Dockerfile / …) | 37 | 5 | 0.1% |
| | **CODE TOTAL** | **34,597** | **378** | 100% |
| — | _Data / exports — excluded_ | 85,159 | 19 | — |
| — | _Generated (lockfiles, SVG) — excluded_ | 12,629 | 23 | — |

### Instruction-markdown as code

- **Hygiene family** (14 files · `CLAUDE.md`, `AGENTS.md`, `SKILL.md`): **1,647 lines**
- **Prompt-programs** (4 files · reference-checker auditors): **1,451 lines**

#### Hygiene surface — each file is a maintenance obligation

| Repo | File | Lines |
|------|------|------:|
| homeassistant-config | `CLAUDE.md` | 399 |
| shared-workflows | `CLAUDE.md` | 181 |
| betula | `CLAUDE.md` | 156 |
| .github | `CLAUDE.md` | 135 |
| site-lentago-dev | `CLAUDE.md` | 108 |
| solidago | `CLAUDE.md` | 99 |
| site-icecreamtofightwith-com | `CLAUDE.md` | 98 |
| drosera | `CLAUDE.md` | 95 |
| kalmia | `CLAUDE.md` | 94 |
| reference-checker | `CLAUDE.md` | 76 |
| drosera | `AGENTS.md` | 66 |
| music-curator | `CLAUDE.md` | 61 |
| claytonia | `CLAUDE.md` | 57 |
| repo-template | `CLAUDE.md` | 22 |
| **14 files** | | **1,647** |

#### Prompt-programs — natural language *is* the logic

| Repo | File | Lines |
|------|------|------:|
| reference-checker | `prompts/v6-auditor.md` | 583 |
| reference-checker | `prompts/v5-auditor.md` | 462 |
| reference-checker | `prompts/v4-auditor.md` | 337 |
| reference-checker | `prompts/v3-auditor.md` | 69 |
| **4 files** | | **1,451** |

_Judgement call: these prompt files are counted as instruction-code because they're versioned natural-language instruction sets. Scope to only the CLAUDE.md hygiene family and the instruction figure is **1,647**, not 3,098._

### Per-repo

| Repo | Code | Instr | Doc-md | Content-md | Data |
|------|-----:|------:|-------:|-----------:|-----:|
| drosera | 9,156 | 161 | 667 | 0 | 0 |
| homeassistant-config | 6,495 | 399 | 1,090 | 0 | 17,420 |
| solidago | 5,831 | 99 | 1,690 | 0 | 0 |
| site-icecreamtofightwith-com | 2,041 | 98 | 594 | 6,008 | 0 |
| kalmia | 1,982 | 94 | 463 | 0 | 0 |
| claytonia | 1,736 | 57 | 520 | 0 | 0 |
| reference-checker | 1,587 | 1,527 | 731 | 669 | 5,174 |
| music-curator | 1,504 | 61 | 866 | 7,909 | 62,565 |
| site-lentago-dev | 1,421 | 108 | 360 | 0 | 0 |
| betula | 1,288 | 156 | 923 | 0 | 0 |
| .github | 920 | 135 | 371 | 966 | 0 |
| shared-workflows | 571 | 181 | 83 | 0 | 0 |
| repo-template | 65 | 22 | 46 | 0 | 0 |

### Markdown taxonomy

The fleet carries **27,406 lines of Markdown across 730 files**; only 11.3% is instruction-code.

| Class | Lines | Files | Disposition |
|-------|------:|------:|-------------|
| **Instructions** | 3,098 | 18 | **counted as code** |
| Content / data | 15,552 | 628 | payload (vault notes, recipes, test-sets) — excluded |
| Documentation | 8,404 | 69 | READMEs, docs, ADRs, runbooks — excluded |
| Community-health | 352 | 15 | CONTRIBUTING/SECURITY/templates — excluded |
| **All Markdown** | **27,406** | **730** | |

---

## Method

- **Issues:** open issues via `gh search issues --owner lentago --state open`; activity from `gh search prs --owner lentago --merged` and closed issues filtered to the 30-day window. Public metadata only — no transcript harvest, ops items, or homelab detail (those live in the LAN copy).
- **Census tool:** `cloc`, run per-repo as `cloc --by-file --vcs=git` so only git-tracked files count (build output, `node_modules`, `.terraform`, venvs never enter). Lines are cloc *code* lines.
- **Scope:** the active repos owned by the `lentago` org, derived at runtime — personal repos and third-party clones are out of scope; archived repos are frozen and excluded.
- **Markdown classifier:** instruction-code = `CLAUDE.md`/`AGENTS.md`/`SKILL.md` or a versioned `prompts/*-auditor.md`; community-health = governance filenames + issue/PR templates; content = repo-scoped payload paths (music-curator `vault/`, ice-cream `recipes/`·manuscript, reference-checker `test-sets/`·`reports/`, dotgithub `fleet-reports/`); everything else = documentation.
- **Data / generated carve-outs:** large exported JSON (music-curator `data/`, homeassistant-config `context/`) and reference-checker's rendered `reports/*.html` are data/output; lockfiles and SVG are generated. drosera's `dashboards/*.json` stay in code as Terraform-enforced dashboards-as-code.
- **Regenerating:** `python3 metrics/generate-fleet-reports.py --out-dir .`

_Generated with Claude Code (Repo Claude)._
