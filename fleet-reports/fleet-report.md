# Lentago Labs Fleet Report

> [!NOTE]
> **Co-authored with [Claude](https://claude.ai)** (Repo Claude, the Lentago Labs fleet steward). Auto-generated weekly from the fleet's public state (GitHub issues/PRs + `cloc` over public repo contents) — no personal, security, or homelab-internal detail is included. A prettier, editorialised copy renders on the Lentago lab LAN.

**Generated:** 2026-08-17 12:22 UTC · Scope: the **15 active** `lentago` repos (archived repos frozen &amp; excluded) · Activity window: last 30 days (since 2026-07-18).

## Snapshot

| Open issues | PRs merged (30d) | Issues closed (30d) | Code (incl. instructions) | Instruction-markdown |
|---:|---:|---:|---:|---:|
| **96** | 316 | 138 | **77,015** | 2,094 (16 files) |

The fleet's hand-maintained natural-language instruction surface (**2,094 lines** across 16 files) is among the largest "languages" in the code base — `reference-checker` alone is almost entirely prompt-program source.

---

## Open issues — 96 across 14 repos

### .github — 20 open

| # | Title |
|---|-------|
| [148](https://github.com/lentago/.github/issues/148) | music-curator push allowlist: the Actions-app entry applies successfully but never persists |
| [134](https://github.com/lentago/.github/issues/134) | Offerings pipeline — sovereignty track (2026-08 review) |
| [133](https://github.com/lentago/.github/issues/133) | Offering: Ops-in-a-Box — the miniature estate starter kit |
| [132](https://github.com/lentago/.github/issues/132) | Spike: volunteer-ops scheduling — evaluate, don't build (decision memo) |
| [131](https://github.com/lentago/.github/issues/131) | Offering: privacy posture kit for newly covered orgs |
| [130](https://github.com/lentago/.github/issues/130) | Offering: funder-report fact pipeline |
| [129](https://github.com/lentago/.github/issues/129) | Offering: cold-chain & facilities telemetry kit |
| [128](https://github.com/lentago/.github/issues/128) | Offering: Ask-the-Records kit — fact corpus + grounded Ask, client-owned |
| [127](https://github.com/lentago/.github/issues/127) | Offering: AI-with-receipts — the reviewed-merge operating model as an adoption framework |
| [126](https://github.com/lentago/.github/issues/126) | Offering: Institutional Memory kit + private grounded Ask |
| [125](https://github.com/lentago/.github/issues/125) | Offering: Insurance-Receipts Pack — controls with evidence exhaust |
| [124](https://github.com/lentago/.github/issues/124) | Offering: Digital Custody audit — ownership insurance for the org's presence |
| [123](https://github.com/lentago/.github/issues/123) | Offering: Liberation Pipeline — SaaS-export collectors + restore drills |
| [122](https://github.com/lentago/.github/issues/122) | Offering: Good-Standing Kit — obligations-as-code + registry reconciliation (MA pack first) |
| [121](https://github.com/lentago/.github/issues/121) | Publish the fleet's own lock-in ledger; then cut the client template |
| [120](https://github.com/lentago/.github/issues/120) | Create the campaign-site kit template repo |
| [119](https://github.com/lentago/.github/issues/119) | Create the Kubernetes platform repo (k3s + ephemeral EKS, pull-based GitOps, IRSA) |
| [118](https://github.com/lentago/.github/issues/118) | Incident register: tag entries deployment-caused y/n |
| [90](https://github.com/lentago/.github/issues/90) | Recommendation: engagement pathways — the lab ladder for new members |
| [81](https://github.com/lentago/.github/issues/81) | terraform: wire plan-on-PR and apply-on-merge for the fleet settings module |

### drosera — 18 open

| # | Title |
|---|-------|
| [200](https://github.com/lentago/drosera/issues/200) | Queue SLO for the agent fleet (pickup latency) + burn alert |
| [199](https://github.com/lentago/drosera/issues/199) | Error-budget monthly section in the fleet report |
| [198](https://github.com/lentago/drosera/issues/198) | Threat Weather: anonymized daily network weather report |
| [197](https://github.com/lentago/drosera/issues/197) | "Are we open" single source of truth |
| [196](https://github.com/lentago/drosera/issues/196) | Estate status page (uptime vs SLO, error budget, CI health) + client-facing variant |
| [194](https://github.com/lentago/drosera/issues/194) | Adopt grafana-stack (LXC 105) guest capacity from kalmia |
| [176](https://github.com/lentago/drosera/issues/176) | Four live Loki streams have no ingest-absence rule, and the documented stream list is stale |
| [169](https://github.com/lentago/drosera/issues/169) | Complete the homelab-observability → drosera rename through CI and hosts |
| [165](https://github.com/lentago/drosera/issues/165) | New-domain radar: alert when an IoT/smart-home device queries a never-before-seen domain (migrated from betula#11) |
| [164](https://github.com/lentago/drosera/issues/164) | Bandwidth panels from Zeek conn.log bytes (migrated from betula#15) |
| [157](https://github.com/lentago/drosera/issues/157) | Sites scoreboard row for the office display kiosk |
| [153](https://github.com/lentago/drosera/issues/153) | Terraform apply silently overwrites live dashboard edits — surface what an apply will revert |
| [151](https://github.com/lentago/drosera/issues/151) | device-inventory publisher: cron reinstall hook failed silently — root-cause and make the schedule survivable/verifiable |
| [145](https://github.com/lentago/drosera/issues/145) | gitops loop can't recover a crashed Alloy — validator runs inside the down container |
| [131](https://github.com/lentago/drosera/issues/131) | Roadmap: multi-client telemetry pane — homelab and solidago (AWS) as peer sources |
| [103](https://github.com/lentago/drosera/issues/103) | Scrape node_exporter on the Firewalla via Alloy (bring the gateway into node dashboards) |
| [101](https://github.com/lentago/drosera/issues/101) | Heartbeat blind spot: tool-less reasoning turns show no activity while tokens burn |
| [93](https://github.com/lentago/drosera/issues/93) | feat(alloy): attach runid label to the transcript stream from the <sid>.runid sidecar |

### kalmia — 14 open

| # | Title |
|---|-------|
| [108](https://github.com/lentago/kalmia/issues/108) | Forge: golden images with receipts (checksums, SBOM, provenance) |
| [107](https://github.com/lentago/kalmia/issues/107) | Donated-hardware refresh profiles (new client class) |
| [104](https://github.com/lentago/kalmia/issues/104) | Terraform: adopt backup-job `exclude` once bpg/proxmox ships it |
| [99](https://github.com/lentago/kalmia/issues/99) | Cast client runtime for brasenia: watchdog sender, receiver hosting, then HLS-stack turn-down (brasenia ADR-0006) |
| [85](https://github.com/lentago/kalmia/issues/85) | power: assert charge thresholds actually reached sysfs instead of trusting the drop-in |
| [63](https://github.com/lentago/kalmia/issues/63) | Complete the lunaria → brasenia rename through runtime |
| [53](https://github.com/lentago/kalmia/issues/53) | Pre-merge guard: verify a ForceNew guest change can actually be re-created under the apply identity |
| [52](https://github.com/lentago/kalmia/issues/52) | Codify the n8n container's provisioning (Docker + compose) — recreate yields a bare template |
| [51](https://github.com/lentago/kalmia/issues/51) | Guarantee vzdump coverage for every Terraform-enforced guest (CT 113 had none) |
| [50](https://github.com/lentago/kalmia/issues/50) | Add prevent_destroy to import-only guests the token pipeline can't recreate (starting CT 113) |
| [20](https://github.com/lentago/kalmia/issues/20) | Roadmap: provisioning clients beyond Ansible-on-workstations — VMs and containers as peer targets |
| [16](https://github.com/lentago/kalmia/issues/16) | Harden the xubuntu profile for Ubuntu 26.04 (stale comment + Docker CE repo codename) |
| [15](https://github.com/lentago/kalmia/issues/15) | Live-test the crostini profile on the Chromebook penguin container |
| [14](https://github.com/lentago/kalmia/issues/14) | Live-test the ubuntu_laptop profile on real ThinkPad hardware |

### solidago — 13 open

| # | Title |
|---|-------|
| [173](https://github.com/lentago/solidago/issues/173) | Prune the rename-era OIDC trust entries from the app deploy role |
| [172](https://github.com/lentago/solidago/issues/172) | SNS alert email subscription is recreated on every apply — alerts may be reaching nobody |
| [169](https://github.com/lentago/solidago/issues/169) | Extend variable validation blocks beyond 1 of 24 modules |
| [168](https://github.com/lentago/solidago/issues/168) | Ask the Estate: grounded-Ask demo over fleet docs |
| [167](https://github.com/lentago/solidago/issues/167) | Dogfood DMARC posture on fleet domains (precondition for the Email Trust kit) |
| [164](https://github.com/lentago/solidago/issues/164) | Enable ECR scan-on-push for the site repositories |
| [156](https://github.com/lentago/solidago/issues/156) | Split plan/apply OIDC environments so the terraform environment can carry a branch policy |
| [153](https://github.com/lentago/solidago/issues/153) | bootstrap-backend.sh still references a nonexistent "foundry" AWS profile |
| [149](https://github.com/lentago/solidago/issues/149) | Rotating a Lambda's Axiom token requires an unrelated apply to take effect |
| [144](https://github.com/lentago/solidago/issues/144) | Ask Lambda logs land in CloudWatch with no path to Axiom |
| [124](https://github.com/lentago/solidago/issues/124) | ECS task defs show a perpetual replace-diff (container_definitions normalization) — plan noise + apply-side-effect landmine |
| [21](https://github.com/lentago/solidago/issues/21) | Evaluate migration from ElastiCache node-based to serverless |
| [20](https://github.com/lentago/solidago/issues/20) | Document: Phase 2 Secrets Manager secret unused after RDS-managed password choice |

### claytonia — 8 open

| # | Title |
|---|-------|
| [99](https://github.com/lentago/claytonia/issues/99) | Second job type: batch document/report jobs through the queue contract |
| [71](https://github.com/lentago/claytonia/issues/71) | Reaper cannot see a job left in processing/ without an .owner file — permanent phantom occupancy |
| [65](https://github.com/lentago/claytonia/issues/65) | Complete the bullpen → claytonia rename on-host |
| [47](https://github.com/lentago/claytonia/issues/47) | Roadmap: platform-agnostic workers — Claude Code as one runtime behind the queue contract |
| [31](https://github.com/lentago/claytonia/issues/31) | Add optional authentication to the n8n Bullpen job-submit form |
| [24](https://github.com/lentago/claytonia/issues/24) | Branch hygiene across overlapping sessions: clean-desk session-end + prefer fleet dispatch |
| [22](https://github.com/lentago/claytonia/issues/22) | Fleet PR lane separation: rebase-before-merge + dispatch-time overlap check (no two writers on one file/panel) |
| [21](https://github.com/lentago/claytonia/issues/21) | Queue admission control: job ownership, fleet occupancy, and capacity awareness at submit time |

### betula — 7 open

| # | Title |
|---|-------|
| [107](https://github.com/lentago/betula/issues/107) | Device drift self-report: deployed conf hash vs main |
| [106](https://github.com/lentago/betula/issues/106) | Third AWS emitter: CloudTrail → archive + weekly access digest |
| [105](https://github.com/lentago/betula/issues/105) | State the per-client destination rule (README + estate atlas) |
| [104](https://github.com/lentago/betula/issues/104) | README: quantify the pipeline (events/day, GB/month, latency, retention) |
| [89](https://github.com/lentago/betula/issues/89) | Complete the firewalla-axiom-pipeline → betula rename on-device |
| [86](https://github.com/lentago/betula/issues/86) | Firewalla boot race: Fluent Bit starts before Zeek's spool is live and tails dead paths silently; healthcheck's error-based detection cannot see it |
| [74](https://github.com/lentago/betula/issues/74) | Roadmap: core/client split — Firewalla and solidago (AWS) as peer collector clients |

### brasenia — 4 open

| # | Title |
|---|-------|
| [17](https://github.com/lentago/brasenia/issues/17) | Live-ingest pane: concept + ADR, acceptance spec, and VideoScene repoint to `live` with board fallback |
| [15](https://github.com/lentago/brasenia/issues/15) | Adopt the display guest (LXC 118) capacity from kalmia |
| [13](https://github.com/lentago/brasenia/issues/13) | Cast client: custom web receiver + current-pane pointer contract |
| [12](https://github.com/lentago/brasenia/issues/12) | Second functional path: Cast-native rendering, then deprecate and turn down the Roku/HLS chain |

### music-curator — 3 open

| # | Title |
|---|-------|
| [45](https://github.com/lentago/music-curator/issues/45) | Web-verify the promoted person nodes' credit rows |
| [44](https://github.com/lentago/music-curator/issues/44) | Producer-class connectors: decide representation |
| [43](https://github.com/lentago/music-curator/issues/43) | Session-tie receipts: render the credits justifying each edge |

### shared-workflows — 2 open

| # | Title |
|---|-------|
| [41](https://github.com/lentago/shared-workflows/issues/41) | Reusable tf-lint workflow (fmt -check, tflint, trivy config) for the five Terraform repos |
| [39](https://github.com/lentago/shared-workflows/issues/39) | Artifact attestations on site images (SLSA Build L2 → L3 via the reusable deploy) |

### site-icecreamtofightwith-com — 2 open

| # | Title |
|---|-------|
| [158](https://github.com/lentago/site-icecreamtofightwith-com/issues/158) | Tier accent swatches fail WCAG AA contrast as chip/step backgrounds (design decision needed) |
| [156](https://github.com/lentago/site-icecreamtofightwith-com/issues/156) | Tagged releases: attested, versioned cookbook PDFs |

### site-lentago-dev — 2 open

| # | Title |
|---|-------|
| [49](https://github.com/lentago/site-lentago-dev/issues/49) | Site v3: sovereignty copy, Offerings↔receipts section, the pledge, bespoke shelf |
| [48](https://github.com/lentago/site-lentago-dev/issues/48) | Add @astrojs/sitemap and a pa11y smoke to the PR gate |

### asclepias — 1 open

| # | Title |
|---|-------|
| [6](https://github.com/lentago/asclepias/issues/6) | Run game-day #1 against the agent fleet; publish the post-mortem |

### epigaea — 1 open

| # | Title |
|---|-------|
| [518](https://github.com/lentago/epigaea/issues/518) | Complete the epigaea rename through runtime (tiers 3–4) |

### site-pondviewlane-com — 1 open

| # | Title |
|---|-------|
| [46](https://github.com/lentago/site-pondviewlane-com/issues/46) | Flip Content-Security-Policy from Report-Only to enforcing |

## Activity — last 30 days

**454 events**, one stream, newest first — 🟣 316 PRs merged · 🟢 138 issues closed

- 🟢 2026-08-17 · [.github#116](https://github.com/lentago/.github/issues/116) — Rename homeassistant-config → epigaea (settings-as-code)
- 🟣 2026-08-17 · [.github#147](https://github.com/lentago/.github/pull/147) — feat(fleet): rename homeassistant-config to epigaea
- 🟢 2026-08-17 · [shared-workflows#38](https://github.com/lentago/shared-workflows/issues/38) — Reusable site-deploy workflow: build → ECR → ECS → wait-stable → attest
- 🟣 2026-08-17 · [shared-workflows#47](https://github.com/lentago/shared-workflows/pull/47) — feat: add site-deploy reusable workflow (Astro → ECR → ECS)
- 🟢 2026-08-17 · [solidago#166](https://github.com/lentago/solidago/issues/166) — ADR: record the dev-tier RDS trade-offs
- 🟣 2026-08-17 · [solidago#176](https://github.com/lentago/solidago/pull/176) — docs: ADR-0008 — dev-tier RDS deletion-protection/snapshot trade-offs
- 🟢 2026-08-17 · [music-curator#82](https://github.com/lentago/music-curator/issues/82) — Package the Python surface: pyproject + lockfile
- 🟣 2026-08-17 · [music-curator#86](https://github.com/lentago/music-curator/pull/86) — chore: package the Python surface with pyproject.toml + pip-tools lockfile
- 🟢 2026-08-17 · [kalmia#106](https://github.com/lentago/kalmia/issues/106) — README architecture diagram: OIDC → S3 state / LAN runner → Proxmox
- 🟣 2026-08-17 · [kalmia#118](https://github.com/lentago/kalmia/pull/118) — docs: add hybrid-cloud architecture diagram to README
- 🟢 2026-08-17 · [claytonia#98](https://github.com/lentago/claytonia/issues/98) — README architecture diagram: job → clean checkout → reviewed PR loop
- 🟣 2026-08-17 · [claytonia#108](https://github.com/lentago/claytonia/pull/108) — docs(readme): add architecture diagram to top of README
- 🟢 2026-08-17 · [drosera#195](https://github.com/lentago/drosera/issues/195) — Site availability SLOs, error budgets, and multi-window burn-rate alerts
- 🟣 2026-08-17 · [drosera#203](https://github.com/lentago/drosera/pull/203) — feat: site availability SLOs, error budgets & multi-window burn-rate alerts (#195)
- 🟢 2026-08-17 · [.github#117](https://github.com/lentago/.github/issues/117) — Transfer reference-checker out of the org (bespoke shelf)
- 🟣 2026-08-17 · [.github#146](https://github.com/lentago/.github/pull/146) — chore(fleet): remove reference-checker from fleet settings ahead of transfer
- 🟢 2026-08-17 · [repo-template#14](https://github.com/lentago/repo-template/issues/14) — Codify the description template (+ kit tier), docs/adr and CLAUDE.md canon in SETUP
- 🟣 2026-08-17 · [repo-template#17](https://github.com/lentago/repo-template/pull/17) — docs(setup): codify description template, canonical paths, and anti-drift rule
- 🟢 2026-08-17 · [.github#111](https://github.com/lentago/.github/issues/111) — ADR: the delivery rule — kits into client-owned estates, no hosted multi-tenant services
- 🟣 2026-08-17 · [.github#145](https://github.com/lentago/.github/pull/145) — docs(adr): record the delivery rule as ADR-0007 (closes #111)
- 🟢 2026-08-17 · [.github#114](https://github.com/lentago/.github/issues/114) — Fleet sweep: Dependabot on every repo (github-actions, npm, pip)
- 🟢 2026-08-17 · [.github#113](https://github.com/lentago/.github/issues/113) — Fleet sweep: pin third-party actions to commit SHAs; pin container bases to digests
- 🟣 2026-08-17 · [site-icecreamtofightwith-com#173](https://github.com/lentago/site-icecreamtofightwith-com/pull/173) — chore: add astro-stack Dependabot group to prevent peer-conflict PRs
- 🟣 2026-08-17 · [site-pondviewlane-com#59](https://github.com/lentago/site-pondviewlane-com/pull/59) — build(deps): group astro-stack packages in dependabot.yml
- 🟣 2026-08-17 · [shared-workflows#45](https://github.com/lentago/shared-workflows/pull/45) — ci: supply-chain sweep — Dependabot grouped config
- 🟣 2026-08-17 · [site-lentago-dev#52](https://github.com/lentago/site-lentago-dev/pull/52) — build: pin GitHub Actions to SHAs, pin nginx digest, add Dependabot config
- 🟣 2026-08-17 · [epigaea#516](https://github.com/lentago/epigaea/pull/516) — ci: pin third-party actions to commit SHAs, add Dependabot
- 🟣 2026-08-17 · [music-curator#83](https://github.com/lentago/music-curator/pull/83) — chore(ci): pin third-party actions to commit SHAs; add Dependabot grouping
- 🟣 2026-08-17 · [brasenia#19](https://github.com/lentago/brasenia/pull/19) — chore: supply-chain sweep — add Dependabot (no third-party actions to pin)
- 🟣 2026-08-17 · [asclepias#7](https://github.com/lentago/asclepias/pull/7) — chore: supply-chain sweep — pin actions + add Dependabot
- 🟣 2026-08-17 · [betula#108](https://github.com/lentago/betula/pull/108) — ci: pin third-party actions to SHAs, add Dependabot config
- 🟣 2026-08-17 · [drosera#201](https://github.com/lentago/drosera/pull/201) — ci: pin third-party actions to SHAs, add grouped dependabot config
- 🟢 2026-08-16 · [shared-workflows#40](https://github.com/lentago/shared-workflows/issues/40) — Decide and document the @main consumption policy (version tags or a defending ADR)
- 🟣 2026-08-16 · [shared-workflows#44](https://github.com/lentago/shared-workflows/pull/44) — docs(adr): record immutable semver tag decision; add release process; migrate internal @main refs
- 🟣 2026-08-16 · [site-icecreamtofightwith-com#171](https://github.com/lentago/site-icecreamtofightwith-com/pull/171) — Bump the npm-routine group with 2 updates
- 🟣 2026-08-16 · [claytonia#106](https://github.com/lentago/claytonia/pull/106) — feat(dependabot): add update grouping to reduce PR flood
- 🟣 2026-08-16 · [kalmia#116](https://github.com/lentago/kalmia/pull/116) — ci: group dependabot updates by ecosystem (routine vs major)
- 🟣 2026-08-16 · [site-icecreamtofightwith-com#170](https://github.com/lentago/site-icecreamtofightwith-com/pull/170) — chore: add Dependabot update groups to reduce PR flood
- 🟣 2026-08-16 · [site-pondviewlane-com#56](https://github.com/lentago/site-pondviewlane-com/pull/56) — build(deps): add update grouping to dependabot.yml
- 🟣 2026-08-16 · [.github#142](https://github.com/lentago/.github/pull/142) — ci: group dependabot updates by routine/major per ecosystem
- 🟣 2026-08-16 · [solidago#175](https://github.com/lentago/solidago/pull/175) — ci: group dependabot updates into routine/major PRs
- 🟣 2026-08-16 · [repo-template#16](https://github.com/lentago/repo-template/pull/16) — ci: group dependabot updates by routine vs major
- 🟣 2026-08-16 · [claytonia#105](https://github.com/lentago/claytonia/pull/105) — ci(terraform): skip plan for Dependabot PRs so gate passes
- 🟣 2026-08-16 · [kalmia#115](https://github.com/lentago/kalmia/pull/115) — ci(terraform): skip plan job for Dependabot PRs
- 🟣 2026-08-16 · [site-icecreamtofightwith-com#160](https://github.com/lentago/site-icecreamtofightwith-com/pull/160) — chore: pin third-party actions to commit SHAs and add Dependabot
- 🟣 2026-08-16 · [site-pondviewlane-com#49](https://github.com/lentago/site-pondviewlane-com/pull/49) — build: pin GitHub Actions to SHAs, pin nginx digest, add Dependabot config
- 🟣 2026-08-16 · [.github#137](https://github.com/lentago/.github/pull/137) — ci: pin third-party actions to SHAs and add Dependabot
- 🟣 2026-08-16 · [claytonia#100](https://github.com/lentago/claytonia/pull/100) — ci: pin third-party actions to SHAs, add Dependabot config
- 🟣 2026-08-16 · [kalmia#109](https://github.com/lentago/kalmia/pull/109) — ci: pin third-party actions to SHA and add Dependabot config
- 🟣 2026-08-16 · [solidago#174](https://github.com/lentago/solidago/pull/174) — ci: pin third-party actions to SHAs, add dependabot config
- 🟢 2026-08-16 · [.github#115](https://github.com/lentago/.github/issues/115) — Fleet: OpenSSF Scorecard workflow + badge, trust roots first
- 🟣 2026-08-16 · [.github#136](https://github.com/lentago/.github/pull/136) — feat: add OpenSSF Scorecard workflow and badge
- 🟣 2026-08-16 · [shared-workflows#43](https://github.com/lentago/shared-workflows/pull/43) — feat: add OpenSSF Scorecard workflow and badge
- 🟢 2026-08-16 · [site-pondviewlane-com#45](https://github.com/lentago/site-pondviewlane-com/issues/45) — Add a pa11y accessibility smoke to the PR gate
- 🟣 2026-08-16 · [site-pondviewlane-com#48](https://github.com/lentago/site-pondviewlane-com/pull/48) — feat(a11y): pa11y-ci WCAG2AA smoke check on every PR (#45)
- 🟢 2026-08-16 · [site-icecreamtofightwith-com#154](https://github.com/lentago/site-icecreamtofightwith-com/issues/154) — Adopt the canonical hardened nginx: security headers + server_tokens off
- 🟣 2026-08-16 · [site-icecreamtofightwith-com#159](https://github.com/lentago/site-icecreamtofightwith-com/pull/159) — Adopt fleet-canonical hardened nginx: security headers + server_tokens off
- 🟢 2026-08-16 · [site-lentago-dev#47](https://github.com/lentago/site-lentago-dev/issues/47) — Adopt the canonical hardened nginx: security headers + server_tokens off
- 🟣 2026-08-16 · [site-lentago-dev#51](https://github.com/lentago/site-lentago-dev/pull/51) — feat(nginx): adopt fleet-canonical hardened security headers
- 🟢 2026-08-16 · [solidago#165](https://github.com/lentago/solidago/issues/165) — Tighten the app deploy role's OIDC trust from repo:*:* to main-ref or per-site environments
- 🟣 2026-08-16 · [solidago#171](https://github.com/lentago/solidago/pull/171) — iam: pin app deploy role OIDC trust to refs/heads/main (#165)
- 🟢 2026-08-16 · [site-icecreamtofightwith-com#155](https://github.com/lentago/site-icecreamtofightwith-com/issues/155) — Add a pa11y accessibility smoke to the PR gate
- 🟣 2026-08-16 · [site-icecreamtofightwith-com#157](https://github.com/lentago/site-icecreamtofightwith-com/pull/157) — Add pa11y accessibility smoke check to PR gate
- 🟢 2026-08-16 · [site-lentago-dev#46](https://github.com/lentago/site-lentago-dev/issues/46) — Compute the availability stamp at build time
- 🟣 2026-08-16 · [site-lentago-dev#50](https://github.com/lentago/site-lentago-dev/pull/50) — feat(config): derive availability quarter at build time
- 🟢 2026-08-16 · [.github#112](https://github.com/lentago/.github/issues/112) — Org profile v3: badge accuracy, re-pin, audience paths, positioning + pledge, glossary link
- 🟣 2026-08-16 · [.github#135](https://github.com/lentago/.github/pull/135) — Org profile v3: badge accuracy, positioning + pledge, audience paths, glossary link
- 🟢 2026-08-16 · [solidago#163](https://github.com/lentago/solidago/issues/163) — Remove committed tfplan artifact; ignore *.tfplan; audit history
- 🟣 2026-08-16 · [solidago#170](https://github.com/lentago/solidago/pull/170) — chore: remove committed tfplan artifact from index
- 🟢 2026-08-16 · [site-pondviewlane-com#44](https://github.com/lentago/site-pondviewlane-com/issues/44) — Complete the security-header set and promote this config as the fleet canonical
- 🟣 2026-08-16 · [site-pondviewlane-com#47](https://github.com/lentago/site-pondviewlane-com/pull/47) — Complete the security-header set (HSTS, X-Frame-Options, Permissions-Policy, CSP Report-Only)
- 🟣 2026-08-16 · [repo-template#15](https://github.com/lentago/repo-template/pull/15) — feat: supply-chain hardening — dependabot.yml + skeleton docs (fleet sweep)
- 🟣 2026-08-16 · [shared-workflows#42](https://github.com/lentago/shared-workflows/pull/42) — ci: pin third-party action refs to immutable commit SHAs
- 🟣 2026-08-16 · [shared-workflows#37](https://github.com/lentago/shared-workflows/pull/37) — Enforced-surfaces table: kalmia row now covers cluster vzdump backup jobs
- 🟢 2026-08-16 · [kalmia#30](https://github.com/lentago/kalmia/issues/30) — Terraform: bring PVE backup jobs (jobs.cfg) under management
- 🟣 2026-08-16 · [kalmia#105](https://github.com/lentago/kalmia/pull/105) — Terraform: bring PVE backup jobs (jobs.cfg) under management
- 🟣 2026-08-16 · [brasenia#18](https://github.com/lentago/brasenia/pull/18) — docs: live-ingest concept, ADR-0007, and acceptance spec
- 🟢 2026-08-16 · [kalmia#102](https://github.com/lentago/kalmia/issues/102) — lunaria runtime: enable generic RTMP live-ingest path in mediamtx (first client: DJI Fly)
- 🟣 2026-08-16 · [kalmia#103](https://github.com/lentago/kalmia/pull/103) — lunaria: enable generic RTMP live-ingest path in mediamtx
- 🟣 2026-08-15 · [asclepias#5](https://github.com/lentago/asclepias/pull/5) — Reposition the voice: a field guide among colleagues, not a training ground
- 🟣 2026-08-15 · [.github#110](https://github.com/lentago/.github/pull/110) — asclepias: reposition brand surfaces from training ground to field guide
- 🟣 2026-08-14 · [kalmia#101](https://github.com/lentago/kalmia/pull/101) — Cast Phase A wiring: registered values committed, pub checkout role-managed
- 🟣 2026-08-14 · [brasenia#16](https://github.com/lentago/brasenia/pull/16) — cast-app: record registered App ID and plain-HTTP receiver URL
- 🟣 2026-08-14 · [kalmia#100](https://github.com/lentago/kalmia/pull/100) — Cast receiver watchdog + receiver publishing (brasenia ADR-0006, Phase A)
- 🟣 2026-08-14 · [brasenia#14](https://github.com/lentago/brasenia/pull/14) — cast-app: Phase A Cast web receiver + registration doc
- 🟣 2026-08-14 · [brasenia#11](https://github.com/lentago/brasenia/pull/11) — docs: ADR-0006 — Chromecast web receiver as a second client; compositor output becomes a decision
- 🟣 2026-08-14 · [site-pondviewlane-com#43](https://github.com/lentago/site-pondviewlane-com/pull/43) — Remove stray local skill files that rode in on #42
- 🟢 2026-08-14 · [site-pondviewlane-com#41](https://github.com/lentago/site-pondviewlane-com/issues/41) — Record architecture decisions: add docs/adr from fleet evidence
- 🟣 2026-08-14 · [site-pondviewlane-com#42](https://github.com/lentago/site-pondviewlane-com/pull/42) — Record architecture decisions: add docs/adr from fleet evidence
- 🟢 2026-08-14 · [.github#108](https://github.com/lentago/.github/issues/108) — Record architecture decisions: add docs/adr from fleet evidence
- 🟣 2026-08-14 · [.github#109](https://github.com/lentago/.github/pull/109) — docs: reconstruct architecture decision records under docs/adr
- 🟢 2026-08-14 · [repo-template#12](https://github.com/lentago/repo-template/issues/12) — Record architecture decisions: add docs/adr from fleet evidence; ship the ADR scaffold in the template
- 🟣 2026-08-14 · [repo-template#13](https://github.com/lentago/repo-template/pull/13) — docs(adr): add reconstructed architecture decision records
- 🟢 2026-08-14 · [shared-workflows#35](https://github.com/lentago/shared-workflows/issues/35) — Record architecture decisions: add docs/adr from fleet evidence
- 🟣 2026-08-14 · [shared-workflows#36](https://github.com/lentago/shared-workflows/pull/36) — Record architecture decisions: add docs/adr from fleet evidence
- 🟣 2026-08-14 · [epigaea#515](https://github.com/lentago/epigaea/pull/515) — docs: reconstruct architecture decision records 0001-0005
- 🟢 2026-08-14 · [music-curator#80](https://github.com/lentago/music-curator/issues/80) — Record architecture decisions: add docs/adr from fleet evidence
- 🟣 2026-08-14 · [music-curator#81](https://github.com/lentago/music-curator/pull/81) — docs(adr): add reconstructed architecture decision records under docs/adr/
- 🟢 2026-08-14 · [kalmia#97](https://github.com/lentago/kalmia/issues/97) — Record architecture decisions: add docs/adr from fleet evidence
- 🟣 2026-08-14 · [kalmia#98](https://github.com/lentago/kalmia/pull/98) — docs: add reconstructed architecture decision records (docs/adr/)
- 🟢 2026-08-14 · [brasenia#9](https://github.com/lentago/brasenia/issues/9) — Record architecture decisions: add docs/adr from fleet evidence
- 🟣 2026-08-14 · [brasenia#10](https://github.com/lentago/brasenia/pull/10) — docs: reconstruct architecture decision records under docs/adr
- 🟢 2026-08-14 · [asclepias#3](https://github.com/lentago/asclepias/issues/3) — Record architecture decisions: add docs/adr from fleet evidence
- 🟣 2026-08-14 · [asclepias#4](https://github.com/lentago/asclepias/pull/4) — Add reconstructed architecture decision records under docs/adr
- 🟢 2026-08-14 · [betula#102](https://github.com/lentago/betula/issues/102) — Record architecture decisions: add docs/adr from fleet evidence
- 🟣 2026-08-14 · [betula#103](https://github.com/lentago/betula/pull/103) — docs(adr): reconstruct seven architecture decision records
- 🟢 2026-08-14 · [claytonia#96](https://github.com/lentago/claytonia/issues/96) — Record architecture decisions: add docs/adr from fleet evidence
- 🟣 2026-08-14 · [claytonia#97](https://github.com/lentago/claytonia/pull/97) — docs(adr): reconstruct architecture decision records (#96)
- 🟢 2026-08-14 · [drosera#192](https://github.com/lentago/drosera/issues/192) — Record architecture decisions: extend docs/adr from fleet evidence
- 🟣 2026-08-14 · [drosera#193](https://github.com/lentago/drosera/pull/193) — docs(adr): reconstruct architecture decisions 0002–0007
- 🟢 2026-08-14 · [site-icecreamtofightwith-com#152](https://github.com/lentago/site-icecreamtofightwith-com/issues/152) — Record architecture decisions: add docs/adr from fleet evidence
- 🟣 2026-08-14 · [site-icecreamtofightwith-com#153](https://github.com/lentago/site-icecreamtofightwith-com/pull/153) — Record architecture decisions: add docs/adr from fleet evidence
- 🟢 2026-08-14 · [site-lentago-dev#44](https://github.com/lentago/site-lentago-dev/issues/44) — Record architecture decisions: add docs/adr from fleet evidence
- 🟣 2026-08-14 · [site-lentago-dev#45](https://github.com/lentago/site-lentago-dev/pull/45) — docs(adr): reconstruct architecture decision records
- 🟢 2026-08-14 · [solidago#161](https://github.com/lentago/solidago/issues/161) — Record architecture decisions: extend docs/decisions from fleet evidence
- 🟣 2026-08-14 · [solidago#162](https://github.com/lentago/solidago/pull/162) — docs: record reconstructed architecture decisions (ADR-0002..0007)
- 🟢 2026-08-13 · [site-icecreamtofightwith-com#150](https://github.com/lentago/site-icecreamtofightwith-com/issues/150) — Six table-of-contents links in the compiled book do not resolve to their headings
- 🟣 2026-08-13 · [site-icecreamtofightwith-com#151](https://github.com/lentago/site-icecreamtofightwith-com/pull/151) — Fix seven dead TOC anchor links; add linter check to prevent regression
- 🟣 2026-08-13 · [site-icecreamtofightwith-com#149](https://github.com/lentago/site-icecreamtofightwith-com/pull/149) — Tone down remaining front matter: fewer profanities, tighter humor beats
- 🟢 2026-08-13 · [.github#106](https://github.com/lentago/.github/issues/106) — Fleet: add CODEOWNERS to the 11 repos missing it, so proposed changes reach the owner's inbox
- 🟣 2026-08-13 · [site-pondviewlane-com#40](https://github.com/lentago/site-pondviewlane-com/pull/40) — Add CODEOWNERS so pull requests request owner review
- 🟣 2026-08-13 · [asclepias#2](https://github.com/lentago/asclepias/pull/2) — Add CODEOWNERS so pull requests request owner review
- 🟣 2026-08-13 · [brasenia#8](https://github.com/lentago/brasenia/pull/8) — Add CODEOWNERS so pull requests request owner review
- 🟣 2026-08-13 · [site-icecreamtofightwith-com#148](https://github.com/lentago/site-icecreamtofightwith-com/pull/148) — Add CODEOWNERS so pull requests request owner review
- 🟣 2026-08-13 · [epigaea#514](https://github.com/lentago/epigaea/pull/514) — Add CODEOWNERS so pull requests request owner review
- 🟣 2026-08-13 · [site-lentago-dev#43](https://github.com/lentago/site-lentago-dev/pull/43) — Add CODEOWNERS so pull requests request owner review
- 🟣 2026-08-13 · [repo-template#11](https://github.com/lentago/repo-template/pull/11) — Add CODEOWNERS so pull requests request owner review
- 🟣 2026-08-13 · [music-curator#79](https://github.com/lentago/music-curator/pull/79) — Add CODEOWNERS so pull requests request owner review
- 🟣 2026-08-13 · [shared-workflows#34](https://github.com/lentago/shared-workflows/pull/34) — Add CODEOWNERS so pull requests request owner review
- 🟣 2026-08-13 · [.github#107](https://github.com/lentago/.github/pull/107) — Add CODEOWNERS so pull requests request owner review
- 🟣 2026-08-13 · [claytonia#95](https://github.com/lentago/claytonia/pull/95) — Add CODEOWNERS so pull requests request owner review
- 🟣 2026-08-13 · [drosera#191](https://github.com/lentago/drosera/pull/191) — Add CODEOWNERS so pull requests request owner review
- 🟣 2026-08-13 · [solidago#160](https://github.com/lentago/solidago/pull/160) — Add CODEOWNERS so pull requests request owner review
- 🟣 2026-08-13 · [site-icecreamtofightwith-com#147](https://github.com/lentago/site-icecreamtofightwith-com/pull/147) — Tone down Introduction: fewer profanities, tighter humor beats
- 🟢 2026-08-13 · [.github#104](https://github.com/lentago/.github/issues/104) — Org profile: state the free-tier preference, emphatically
- 🟣 2026-08-13 · [.github#105](https://github.com/lentago/.github/pull/105) — Org profile: state the free-tier preference, emphatically
- 🟢 2026-08-13 · [.github#102](https://github.com/lentago/.github/issues/102) — Org profile: frame the lab's patterns as candidates, not prescriptions
- 🟢 2026-08-13 · [.github#101](https://github.com/lentago/.github/issues/101) — Org profile: drop the employer name from the crew line
- 🟣 2026-08-13 · [.github#103](https://github.com/lentago/.github/pull/103) — Org profile: drop the employer name and frame the patterns as candidates
- 🟣 2026-08-12 · [.github#100](https://github.com/lentago/.github/pull/100) — Incident register: 14 reports harvested from the 2026-07-13 → 08-12 window
- 🟣 2026-08-12 · [.github#99](https://github.com/lentago/.github/pull/99) — Weekly fleet reports refresh — 2026-08-12
- 🟣 2026-08-12 · [.github#98](https://github.com/lentago/.github/pull/98) — terraform: declare the Actions app allowance by its next-format node id
- 🟣 2026-08-12 · [.github#97](https://github.com/lentago/.github/pull/97) — terraform: import asclepias's live main ruleset
- 🟣 2026-08-12 · [.github#96](https://github.com/lentago/.github/pull/96) — terraform: gate every merge to main on an org owner/admin
- 🟢 2026-08-12 · [shared-workflows#32](https://github.com/lentago/shared-workflows/issues/32) — Canonical doctrine drift: Route 53 owner misattributed; solidago#142 still listed as tracked debt
- 🟣 2026-08-12 · [shared-workflows#33](https://github.com/lentago/shared-workflows/pull/33) — Correct live-surface table DNS owner; record solidago#142 as closed OBE
- 🟣 2026-08-12 · [.github#95](https://github.com/lentago/.github/pull/95) — brand: render asclepias social-preview card
- 🟢 2026-08-12 · [.github#91](https://github.com/lentago/.github/issues/91) — Guest readiness: org base permission exposes private repos to all members
- 🟢 2026-08-12 · [.github#89](https://github.com/lentago/.github/issues/89) — Recommendation: unified operations manual — create a dedicated Training repo
- 🟢 2026-08-12 · [.github#88](https://github.com/lentago/.github/issues/88) — Team playground repositioning: fleet-wide README + org profile refresh
- 🟣 2026-08-12 · [asclepias#1](https://github.com/lentago/asclepias/pull/1) — Seed the training ground: manual, labs, onboarding, brand identity
- 🟣 2026-08-12 · [.github#94](https://github.com/lentago/.github/pull/94) — fleet: adopt asclepias — the Training product
- 🟣 2026-08-12 · [site-pondviewlane-com#39](https://github.com/lentago/site-pondviewlane-com/pull/39) — README: reposition as learning-lab exhibit (patterns, operator vectors, DeepWiki)
- 🟣 2026-08-12 · [site-lentago-dev#42](https://github.com/lentago/site-lentago-dev/pull/42) — README: reposition as learning-lab exhibit (patterns, operator vectors, DeepWiki)
- 🟣 2026-08-12 · [site-icecreamtofightwith-com#146](https://github.com/lentago/site-icecreamtofightwith-com/pull/146) — README: reposition as learning-lab exhibit (patterns, operator vectors, DeepWiki)
- 🟣 2026-08-12 · [repo-template#10](https://github.com/lentago/repo-template/pull/10) — README: reposition as learning-lab exhibit (patterns, operator vectors, DeepWiki)
- 🟣 2026-08-12 · [music-curator#78](https://github.com/lentago/music-curator/pull/78) — README: reposition as learning-lab exhibit (patterns, operator vectors, DeepWiki)
- 🟣 2026-08-12 · [epigaea#513](https://github.com/lentago/epigaea/pull/513) — README: reposition as learning-lab exhibit (patterns, operator vectors, DeepWiki)
- 🟣 2026-08-12 · [shared-workflows#31](https://github.com/lentago/shared-workflows/pull/31) — README: reposition as learning-lab exhibit (patterns, operator vectors, DeepWiki)
- 🟣 2026-08-12 · [brasenia#7](https://github.com/lentago/brasenia/pull/7) — README: reposition as learning-lab exhibit (patterns, operator vectors, DeepWiki)
- 🟣 2026-08-12 · [betula#101](https://github.com/lentago/betula/pull/101) — README: reposition as learning-lab exhibit (patterns, operator vectors, DeepWiki)
- 🟣 2026-08-12 · [kalmia#96](https://github.com/lentago/kalmia/pull/96) — README: reposition as learning-lab exhibit (patterns, operator vectors, DeepWiki)
- 🟣 2026-08-12 · [claytonia#92](https://github.com/lentago/claytonia/pull/92) — README: reposition as learning-lab exhibit (patterns, operator vectors, DeepWiki)
- 🟣 2026-08-12 · [solidago#159](https://github.com/lentago/solidago/pull/159) — README: reposition as learning-lab exhibit (patterns, operator vectors, DeepWiki)
- 🟣 2026-08-12 · [.github#92](https://github.com/lentago/.github/pull/92) — README: reposition as learning-lab exhibit (patterns, operator vectors, DeepWiki)
- 🟣 2026-08-12 · [drosera#189](https://github.com/lentago/drosera/pull/189) — README: reposition as learning-lab exhibit (patterns, operator vectors, DeepWiki)
- 🟣 2026-08-12 · [drosera#190](https://github.com/lentago/drosera/pull/190) — dashboards: repoint myosotis commit-link hint to cpitzi/myosotis
- 🟣 2026-08-12 · [claytonia#94](https://github.com/lentago/claytonia/pull/94) — context-ledger: catch provision/07 references missed by the relocation sweep
- 🟣 2026-08-12 · [claytonia#93](https://github.com/lentago/claytonia/pull/93) — context-ledger: repoint to cpitzi/myosotis (repo transferred out of org)
- 🟣 2026-08-12 · [.github#93](https://github.com/lentago/.github/pull/93) — fleet-ops: remove myosotis — transferred to a personal account
- 🟣 2026-08-11 · [.github#87](https://github.com/lentago/.github/pull/87) — Weekly fleet reports refresh — 2026-08-11
- 🟢 2026-08-11 · [.github#85](https://github.com/lentago/.github/issues/85) — fleet-reports: weekly run broken by the org's first private repo
- 🟣 2026-08-11 · [.github#86](https://github.com/lentago/.github/pull/86) — Scope fleet reports to public repos only
- 🟣 2026-08-11 · [.github#84](https://github.com/lentago/.github/pull/84) — Surface DeepWiki links on the org profile and finish the homepage sweep
- 🟣 2026-08-11 · [.github#83](https://github.com/lentago/.github/pull/83) — terraform: rename the validate job to tf-validate
- 🟣 2026-08-11 · [.github#82](https://github.com/lentago/.github/pull/82) — Manage the fleet's GitHub settings with the Terraform GitHub provider
- 🟣 2026-08-10 · [kalmia#95](https://github.com/lentago/kalmia/pull/95) — lunaria: append extra TV-contract panes to the wall-display rotation
- 🟢 2026-08-10 · [.github#78](https://github.com/lentago/.github/issues/78) — Pin cloc in the fleet-reports workflow — the unpinned 1.98 drops all Astro source from the census
- 🟣 2026-08-10 · [.github#80](https://github.com/lentago/.github/pull/80) — fix: pin cloc to v2.06 in fleet-reports workflow
- 🟣 2026-08-10 · [music-curator#77](https://github.com/lentago/music-curator/pull/77) — Stop re-including graph.json from the vault gitignore the driver writes
- 🟣 2026-08-10 · [music-curator#76](https://github.com/lentago/music-curator/pull/76) — Untrack vault Obsidian graph.json; document graph-presets swapping
- 🟢 2026-08-09 · [claytonia#84](https://github.com/lentago/claytonia/issues/84) — docs: context-tracking observability model + alert runbook (visibility layer, part 5)
- 🟣 2026-08-09 · [claytonia#91](https://github.com/lentago/claytonia/pull/91) — docs(context-ledger): signal model + alert runbook (issue #84)
- 🟢 2026-08-09 · [drosera#185](https://github.com/lentago/drosera/issues/185) — Alert rules: context tracking (quarantine, stale host, committer silence) (visibility layer, part 3)
- 🟣 2026-08-09 · [drosera#188](https://github.com/lentago/drosera/pull/188) — Add context-ledger alert rules: quarantine, stale host, committer silence
- 🟢 2026-08-09 · [claytonia#89](https://github.com/lentago/claytonia/issues/89) — context-snapshot: claude_version '(unavailable)' on workers — claude not on the unit's PATH
- 🟣 2026-08-09 · [claytonia#90](https://github.com/lentago/claytonia/pull/90) — fix(context-snapshot): add PATH to service unit so claude --version resolves (#89)
- 🟢 2026-08-09 · [drosera#184](https://github.com/lentago/drosera/issues/184) — Claytonia dashboard: Context Ledger section (visibility layer, part 2)
- 🟣 2026-08-09 · [drosera#187](https://github.com/lentago/drosera/pull/187) — feat(dashboard): Context Ledger section on Claytonia — Runner Fleet (#184)
- 🟣 2026-08-09 · [claytonia#88](https://github.com/lentago/claytonia/pull/88) — fix(test): restore closing brace lost at the #86 rebase conflict seam
- 🟢 2026-08-09 · [claytonia#83](https://github.com/lentago/claytonia/issues/83) — context-ledger: ledger-report CLI — kill the git-log incantations (visibility layer, part 4)
- 🟣 2026-08-09 · [claytonia#86](https://github.com/lentago/claytonia/pull/86) — feat(context-ledger): ledger-report CLI — visibility layer part 4 (#83)
- 🟢 2026-08-09 · [claytonia#82](https://github.com/lentago/claytonia/issues/82) — context-ledger: emit structured sweep/host events to Loki (visibility layer, part 1)
- 🟣 2026-08-09 · [claytonia#87](https://github.com/lentago/claytonia/pull/87) — feat(context-ledger): emit context_sweep/context_host events to Loki (#82)
- 🟢 2026-08-09 · [drosera#183](https://github.com/lentago/drosera/issues/183) — Loki label contract lags betula: producer emits eight log_source streams, consumer tracks four
- 🟣 2026-08-09 · [drosera#186](https://github.com/lentago/drosera/pull/186) — Reconcile the Loki label contract with betula's eight streams
- 🟢 2026-08-09 · [music-curator#74](https://github.com/lentago/music-curator/issues/74) — Active-artist count inconsistency: README says 543, inventory meta says 556
- 🟣 2026-08-09 · [music-curator#75](https://github.com/lentago/music-curator/pull/75) — docs: correct the active-artist count and name its authoritative source
- 🟢 2026-08-09 · [claytonia#79](https://github.com/lentago/claytonia/issues/79) — ShellCheck script list missing context-snapshot, context-ledger-commit, transcript-shipper-sync
- 🟣 2026-08-09 · [claytonia#85](https://github.com/lentago/claytonia/pull/85) — ci: add the three unlinted bin/ scripts to the ShellCheck list
- 🟢 2026-08-09 · [betula#99](https://github.com/lentago/betula/issues/99) — CI coverage gaps: AWS client unit tests never run in CI; three scripts missing from ShellCheck
- 🟣 2026-08-09 · [betula#100](https://github.com/lentago/betula/pull/100) — ci: gate AWS client unit tests on every PR; extend ShellCheck to all six scripts
- 🟢 2026-08-09 · [site-pondviewlane-com#37](https://github.com/lentago/site-pondviewlane-com/issues/37) — Stale doc claims: deploy.yml header cites the removed one-way firewall pipeline; nginx.conf calls the essex vhost inert
- 🟣 2026-08-09 · [site-pondviewlane-com#38](https://github.com/lentago/site-pondviewlane-com/pull/38) — Correct stale pre-decoupling and pre-launch comments
- 🟢 2026-08-09 · [solidago#157](https://github.com/lentago/solidago/issues/157) — README module inventory stale: lists 21 modules, omits alb-log-shipper, ask-lambda, grafana-cloud
- 🟣 2026-08-09 · [solidago#158](https://github.com/lentago/solidago/pull/158) — docs: refresh README module inventory to match modules/ reality
- 🟢 2026-08-09 · [claytonia#78](https://github.com/lentago/claytonia/issues/78) — README describes the retired n8n submit frontend in present tense
- 🟣 2026-08-09 · [claytonia#81](https://github.com/lentago/claytonia/pull/81) — docs(readme): mark the n8n submit frontend as retired
- 🟢 2026-08-09 · [epigaea#511](https://github.com/lentago/epigaea/issues/511) — README drift: File Structure lists home.yaml twice with retired grid-layout annotation; '40+ entities' undersells the registry
- 🟣 2026-08-09 · [epigaea#512](https://github.com/lentago/epigaea/pull/512) — docs: fix README File Structure duplicate, restate entity counts
- 🟢 2026-08-09 · [claytonia#77](https://github.com/lentago/claytonia/issues/77) — gitops: manual git pull in /opt/bullpen strands pending bin/ deploys
- 🟣 2026-08-09 · [claytonia#80](https://github.com/lentago/claytonia/pull/80) — fix(gitops): deploy pass runs unconditionally to self-heal manual-pull drift
- 🟢 2026-08-09 · [claytonia#73](https://github.com/lentago/claytonia/issues/73) — queue: stale processing/ entry survives job completion — reaper misses month-old orphan
- 🟣 2026-08-09 · [claytonia#76](https://github.com/lentago/claytonia/pull/76) — fix(queue): janitor sweeps ownerless completed orphans the reaper misses
- 🟢 2026-08-09 · [claytonia#74](https://github.com/lentago/claytonia/issues/74) — gitops: unit-change restart list doesn't cover the context-ledger timers
- 🟣 2026-08-09 · [claytonia#75](https://github.com/lentago/claytonia/pull/75) — fix(gitops): restart changed timers dynamically instead of hardcoded list
- 🟣 2026-08-09 · [claytonia#72](https://github.com/lentago/claytonia/pull/72) — feat: context ledger — fleet-wide host-side Claude context drift tracking
- 🟣 2026-08-07 · [kalmia#94](https://github.com/lentago/kalmia/pull/94) — docs: correct the branch ruleset description in CLAUDE.md
- 🟣 2026-08-07 · [kalmia#90](https://github.com/lentago/kalmia/pull/90) — shell: render the config the .bashrc block has always sourced
- 🟣 2026-08-07 · [kalmia#91](https://github.com/lentago/kalmia/pull/91) — repos: clone by default instead of opt-in
- 🟣 2026-08-07 · [kalmia#89](https://github.com/lentago/kalmia/pull/89) — repos: clone the org, and stop reporting success on a no-op
- 🟣 2026-08-07 · [kalmia#92](https://github.com/lentago/kalmia/pull/92) — shell: port the remaining two predecessor helpers
- 🟣 2026-08-07 · [kalmia#93](https://github.com/lentago/kalmia/pull/93) — shell: stop hardcoding ~/repos in the .bashrc block
- 🟣 2026-08-07 · [kalmia#88](https://github.com/lentago/kalmia/pull/88) — shell: ship the pull-all helper the Ansible rewrite dropped
- 🟣 2026-08-07 · [kalmia#87](https://github.com/lentago/kalmia/pull/87) — docs: distinguish M143 availability from M147 default for baguette
- 🟢 2026-08-07 · [kalmia#83](https://github.com/lentago/kalmia/issues/83) — power: predecessor TLP charge-threshold drop-in overrides the Ansible-managed one
- 🟣 2026-08-07 · [kalmia#86](https://github.com/lentago/kalmia/pull/86) — power: remove the predecessor TLP charge-threshold drop-in that overrides the managed one
- 🟣 2026-08-07 · [kalmia#84](https://github.com/lentago/kalmia/pull/84) — docs: mark baguette profile validated end-to-end
- 🟢 2026-08-07 · [kalmia#80](https://github.com/lentago/kalmia/issues/80) — check-mode robustness follow-ups: self-referencing changed_when, and two residual false positives
- 🟣 2026-08-07 · [kalmia#82](https://github.com/lentago/kalmia/pull/82) — editors: harden the VS Code extension conditionals against check mode; document known check-mode noise
- 🟢 2026-08-07 · [kalmia#77](https://github.com/lentago/kalmia/issues/77) — docs: record what the live ubuntu_laptop run proved — and what it did not
- 🟣 2026-08-07 · [kalmia#81](https://github.com/lentago/kalmia/pull/81) — docs: record what the live ubuntu_laptop run proved, and what it did not
- 🟢 2026-08-07 · [kalmia#75](https://github.com/lentago/kalmia/issues/75) — languages: --check mode aborts the play and falsely reports a Go reinstall
- 🟣 2026-08-07 · [kalmia#79](https://github.com/lentago/kalmia/pull/79) — roles: fix --check aborting on read-only version probes
- 🟢 2026-08-07 · [kalmia#76](https://github.com/lentago/kalmia/issues/76) — common: no way to converge a workstation without also dist-upgrading it
- 🟣 2026-08-07 · [kalmia#78](https://github.com/lentago/kalmia/pull/78) — common: add a base_system_upgrade toggle to decouple convergence from dist-upgrade
- 🟢 2026-08-07 · [kalmia#73](https://github.com/lentago/kalmia/issues/73) — editors: debconf pre-seed adds a second VS Code apt source and breaks apt host-wide
- 🟣 2026-08-07 · [kalmia#74](https://github.com/lentago/kalmia/pull/74) — editors: stop the VS Code postinst from adding a conflicting apt source
- 🟣 2026-08-07 · [kalmia#72](https://github.com/lentago/kalmia/pull/72) — Update the review prompt for the fifth profile
- 🟣 2026-08-07 · [kalmia#71](https://github.com/lentago/kalmia/pull/71) — Add a baguette profile for ChromeOS containerless Crostini
- 🟣 2026-08-03 · [.github#79](https://github.com/lentago/.github/pull/79) — Weekly fleet reports refresh — 2026-08-03
- 🟣 2026-08-01 · [music-curator#73](https://github.com/lentago/music-curator/pull/73) — chore(harvest): 2026-07 Spotify roll-up
- 🟣 2026-07-29 · [.github#77](https://github.com/lentago/.github/pull/77) — Weekly fleet reports refresh — 2026-07-29
- 🟣 2026-07-29 · [kalmia#70](https://github.com/lentago/kalmia/pull/70) — Fix Debian 13 package names and pin NVM_DIR; mark crostini validated
- 🟣 2026-07-28 · [music-curator#72](https://github.com/lentago/music-curator/pull/72) — Repair rip damage in album titles
- 🟢 2026-07-28 · [music-curator#42](https://github.com/lentago/music-curator/issues/42) — Merge name-variant duplicate artists in the inventory
- 🟣 2026-07-28 · [music-curator#71](https://github.com/lentago/music-curator/pull/71) — Merge name-variant duplicate artists across inventory and sidecars
- 🟣 2026-07-28 · [music-curator#70](https://github.com/lentago/music-curator/pull/70) — Categorize the follow reservoir and add Rock > Progressive
- 🟣 2026-07-28 · [site-pondviewlane-com#36](https://github.com/lentago/site-pondviewlane-com/pull/36) — Drop the severed private-source-repo publish pipeline from the docs
- 🟣 2026-07-28 · [site-pondviewlane-com#35](https://github.com/lentago/site-pondviewlane-com/pull/35) — Correct the stale pre-launch indexing status in the docs
- 🟣 2026-07-28 · [music-curator#69](https://github.com/lentago/music-curator/pull/69) — Revise artist categorization across the collection
- 🟣 2026-07-27 · [.github#76](https://github.com/lentago/.github/pull/76) — Weekly fleet reports refresh — 2026-07-27
- 🟣 2026-07-26 · [site-pondviewlane-com#34](https://github.com/lentago/site-pondviewlane-com/pull/34) — Make every claim independently checkable at its source portal
- 🟣 2026-07-26 · [site-pondviewlane-com#33](https://github.com/lentago/site-pondviewlane-com/pull/33) — Lead the common-land page with the parcel map
- 🟣 2026-07-26 · [site-pondviewlane-com#32](https://github.com/lentago/site-pondviewlane-com/pull/32) — Raise the shared small-print contrast to AA on both domains
- 🟣 2026-07-25 · [site-pondviewlane-com#31](https://github.com/lentago/site-pondviewlane-com/pull/31) — Fix the Essex notice panels: drop the stray quote mark, re-tone the ground
- 🟣 2026-07-25 · [site-pondviewlane-com#30](https://github.com/lentago/site-pondviewlane-com/pull/30) — Make the Essex hero name dominate, with "at Montserrat" as a subtitle
- 🟣 2026-07-25 · [site-pondviewlane-com#29](https://github.com/lentago/site-pondviewlane-com/pull/29) — Re-skin Essex Crossing at Montserrat as a gilded estate document
- 🟣 2026-07-25 · [.github#75](https://github.com/lentago/.github/pull/75) — chore: refresh fleet reports; exclude generated brand artefacts from the census
- 🟣 2026-07-25 · [solidago#154](https://github.com/lentago/solidago/pull/154) — ci(terraform): add workflow_dispatch trigger to allow deliberate applies
- 🟢 2026-07-25 · [claytonia#49](https://github.com/lentago/claytonia/issues/49) — Grant the runner App workflows+issues write (machine account shipped; permissions gap remains)
- 🟣 2026-07-25 · [claytonia#70](https://github.com/lentago/claytonia/pull/70) — docs: record the runner App's granted scopes
- 🟢 2026-07-25 · [claytonia#25](https://github.com/lentago/claytonia/issues/25) — Single 'what is every Claude doing right now' pane: unify local sessions + fleet jobs
- 🟢 2026-07-25 · [claytonia#23](https://github.com/lentago/claytonia/issues/23) — Enforce no-auto-merge review gate on fleet PRs; make 'Open agent PRs' the dispatch gate
- 🟢 2026-07-25 · [solidago#142](https://github.com/lentago/solidago/issues/142) — Track the foundry-* → solidago AWS resource rename
- 🟢 2026-07-25 · [betula#83](https://github.com/lentago/betula/issues/83) — Refresh docs/architecture.svg — Axiom path retired, Loki-only pipeline
- 🟣 2026-07-25 · [betula#98](https://github.com/lentago/betula/pull/98) — docs: drop stale architecture.svg caveats
- 🟢 2026-07-25 · [site-lentago-dev#36](https://github.com/lentago/site-lentago-dev/issues/36) — Update DEPLOYMENT.md to reference solidago instead of old repo name foundry-platform-demo
- 🟢 2026-07-25 · [.github#71](https://github.com/lentago/.github/issues/71) — fleet-apply --require-checks silently drops live contexts missing from required-checks.json
- 🟣 2026-07-25 · [.github#74](https://github.com/lentago/.github/pull/74) — fleet-ops: refuse to silently delete live required checks
- 🟢 2026-07-25 · [.github#28](https://github.com/lentago/.github/issues/28) — fleet-ops: require the terraform check on enforced-surface repos (claytonia requires only shellcheck; kalmia requires none)
- 🟣 2026-07-25 · [.github#73](https://github.com/lentago/.github/pull/73) — fleet-ops: require claytonia's terraform gate
- 🟢 2026-07-25 · [.github#31](https://github.com/lentago/.github/issues/31) — Update language-census.md to current repo name solidago (was foundry-platform-demo)
- 🟣 2026-07-25 · [.github#72](https://github.com/lentago/.github/pull/72) — Refresh the language census over git-tracked files
- 🟣 2026-07-25 · [claytonia#69](https://github.com/lentago/claytonia/pull/69) — terraform: add an always-on gate so the check can be required
- 🟣 2026-07-25 · [.github#70](https://github.com/lentago/.github/pull/70) — fleet-ops: restore the Compile and commit required check
- 🟣 2026-07-25 · [.github#69](https://github.com/lentago/.github/pull/69) — fleet-ops: don't let one refused repo abort the require-checks sweep
- 🟣 2026-07-25 · [.github#68](https://github.com/lentago/.github/pull/68) — fleet-ops: require docs-check on every active repo
- 🟢 2026-07-25 · [.github#66](https://github.com/lentago/.github/issues/66) — Decide: replace ci/validate.py's link check with the shared docs-check, or keep both
- 🟣 2026-07-25 · [.github#67](https://github.com/lentago/.github/pull/67) — Replace the local link check with the shared docs-check
- 🟣 2026-07-25 · [shared-workflows#29](https://github.com/lentago/shared-workflows/pull/29) — Dogfood docs-check on this repo's own markdown
- 🟣 2026-07-25 · [solidago#152](https://github.com/lentago/solidago/pull/152) — Adopt the shared docs-check workflow
- 🟣 2026-07-25 · [site-pondviewlane-com#28](https://github.com/lentago/site-pondviewlane-com/pull/28) — Adopt the shared docs-check workflow
- 🟣 2026-07-25 · [site-lentago-dev#41](https://github.com/lentago/site-lentago-dev/pull/41) — Adopt the shared docs-check workflow
- 🟣 2026-07-25 · [site-icecreamtofightwith-com#145](https://github.com/lentago/site-icecreamtofightwith-com/pull/145) — Adopt the shared docs-check workflow
- 🟣 2026-07-25 · [repo-template#9](https://github.com/lentago/repo-template/pull/9) — Adopt the shared docs-check workflow
- 🟣 2026-07-25 · [music-curator#68](https://github.com/lentago/music-curator/pull/68) — Adopt the shared docs-check workflow
- 🟣 2026-07-25 · [kalmia#69](https://github.com/lentago/kalmia/pull/69) — Adopt the shared docs-check workflow
- 🟣 2026-07-25 · [epigaea#510](https://github.com/lentago/epigaea/pull/510) — Adopt the shared docs-check workflow
- 🟣 2026-07-25 · [drosera#182](https://github.com/lentago/drosera/pull/182) — Adopt the shared docs-check workflow
- 🟣 2026-07-25 · [claytonia#68](https://github.com/lentago/claytonia/pull/68) — Adopt the shared docs-check workflow
- 🟣 2026-07-25 · [brasenia#6](https://github.com/lentago/brasenia/pull/6) — Adopt the shared docs-check workflow
- 🟣 2026-07-25 · [betula#97](https://github.com/lentago/betula/pull/97) — Adopt the shared docs-check workflow
- 🟣 2026-07-25 · [shared-workflows#30](https://github.com/lentago/shared-workflows/pull/30) — docs-check: resolve the tooling ref from job_workflow_ref
- 🟢 2026-07-25 · [.github#57](https://github.com/lentago/.github/issues/57) — Fleet gap: docs-only PRs pass CI without asserting anything
- 🟣 2026-07-25 · [shared-workflows#28](https://github.com/lentago/shared-workflows/pull/28) — Add reusable docs-check workflow (relative markdown links)
- 🟣 2026-07-25 · [.github#65](https://github.com/lentago/.github/pull/65) — fleet-ops: require music-curator's integrity check
- 🟣 2026-07-25 · [site-pondviewlane-com#27](https://github.com/lentago/site-pondviewlane-com/pull/27) — Add the @claude responder caller
- 🟣 2026-07-25 · [.github#64](https://github.com/lentago/.github/pull/64) — Add the @claude responder caller
- 🟢 2026-07-25 · [solidago#150](https://github.com/lentago/solidago/issues/150) — Apply the Lentago Labs brand header to the README
- 🟣 2026-07-25 · [solidago#151](https://github.com/lentago/solidago/pull/151) — docs: apply Lentago Labs brand header to README
- 🟢 2026-07-25 · [site-pondviewlane-com#25](https://github.com/lentago/site-pondviewlane-com/issues/25) — Apply the Lentago Labs brand header to the README
- 🟣 2026-07-25 · [site-pondviewlane-com#26](https://github.com/lentago/site-pondviewlane-com/pull/26) — Apply generated Lentago Labs brand header to README
- 🟢 2026-07-25 · [site-lentago-dev#39](https://github.com/lentago/site-lentago-dev/issues/39) — Apply the Lentago Labs brand header to the README
- 🟣 2026-07-25 · [site-lentago-dev#40](https://github.com/lentago/site-lentago-dev/pull/40) — docs(readme): apply generated Lentago Labs brand header
- 🟢 2026-07-25 · [site-icecreamtofightwith-com#143](https://github.com/lentago/site-icecreamtofightwith-com/issues/143) — Apply the Lentago Labs brand header to the README
- 🟣 2026-07-25 · [site-icecreamtofightwith-com#144](https://github.com/lentago/site-icecreamtofightwith-com/pull/144) — feat: apply Lentago Labs brand header to README
- 🟢 2026-07-25 · [shared-workflows#26](https://github.com/lentago/shared-workflows/issues/26) — Apply the Lentago Labs brand header to the README
- 🟣 2026-07-25 · [shared-workflows#27](https://github.com/lentago/shared-workflows/pull/27) — Add Lentago Labs brand header to README
- 🟢 2026-07-25 · [repo-template#7](https://github.com/lentago/repo-template/issues/7) — Apply the Lentago Labs brand header to the README
- 🟣 2026-07-25 · [repo-template#8](https://github.com/lentago/repo-template/pull/8) — feat: apply Lentago Labs brand header to README
- 🟢 2026-07-25 · [music-curator#66](https://github.com/lentago/music-curator/issues/66) — Apply the Lentago Labs brand header to the README
- 🟣 2026-07-25 · [music-curator#67](https://github.com/lentago/music-curator/pull/67) — brand: apply Lentago Labs header to README
- 🟣 2026-07-25 · [kalmia#68](https://github.com/lentago/kalmia/pull/68) — docs: apply Lentago Labs brand header to README
- 🟢 2026-07-25 · [kalmia#67](https://github.com/lentago/kalmia/issues/67) — Apply the Lentago Labs brand header to the README
- 🟣 2026-07-25 · [epigaea#509](https://github.com/lentago/epigaea/pull/509) — docs: apply Lentago Labs brand header to README
- 🟢 2026-07-25 · [drosera#180](https://github.com/lentago/drosera/issues/180) — Apply the Lentago Labs brand header to the README
- 🟣 2026-07-25 · [drosera#181](https://github.com/lentago/drosera/pull/181) — docs: apply Lentago Labs brand header to README
- 🟢 2026-07-25 · [claytonia#66](https://github.com/lentago/claytonia/issues/66) — Apply the Lentago Labs brand header to the README
- 🟣 2026-07-25 · [claytonia#67](https://github.com/lentago/claytonia/pull/67) — docs: add Lentago Labs brand header to README
- 🟢 2026-07-25 · [brasenia#4](https://github.com/lentago/brasenia/issues/4) — Apply the Lentago Labs brand header to the README
- 🟣 2026-07-25 · [brasenia#5](https://github.com/lentago/brasenia/pull/5) — feat: apply Lentago Labs brand header to README
- 🟢 2026-07-25 · [betula#95](https://github.com/lentago/betula/issues/95) — Apply the Lentago Labs brand header to the README
- 🟣 2026-07-25 · [betula#96](https://github.com/lentago/betula/pull/96) — docs: add Lentago Labs brand header to README
- 🟣 2026-07-25 · [.github#63](https://github.com/lentago/.github/pull/63) — README: carry the generated brand header
- 🟣 2026-07-25 · [.github#62](https://github.com/lentago/.github/pull/62) — Brand: per-repo identity generator and Tidewater label palette
- 🟣 2026-07-25 · [.github#61](https://github.com/lentago/.github/pull/61) — README: document ci/ and clarify what shared-workflows owns
- 🟣 2026-07-25 · [.github#60](https://github.com/lentago/.github/pull/60) — CI: validate this repo's invariants and gate PRs on them
- 🟣 2026-07-25 · [.github#59](https://github.com/lentago/.github/pull/59) — Census: classify data-dir exports by directory, not just JSON
- 🟣 2026-07-25 · [.github#58](https://github.com/lentago/.github/pull/58) — Fleet reports refresh — 2026-07-25
- 🟣 2026-07-25 · [epigaea#508](https://github.com/lentago/epigaea/pull/508) — docs: remove broken image reference from Lentago Lab Status section
- 🟢 2026-07-25 · [betula#93](https://github.com/lentago/betula/issues/93) — Dead links to the removed dashboards/ directory in the Zeek field reference
- 🟣 2026-07-25 · [betula#94](https://github.com/lentago/betula/pull/94) — docs: fix dead dashboards/axiom-queries.md links in zeek-field-reference
- 🟢 2026-07-25 · [drosera#178](https://github.com/lentago/drosera/issues/178) — README describes the retired single-container Alloy model
- 🟣 2026-07-25 · [drosera#179](https://github.com/lentago/drosera/pull/179) — docs: fix README's single-Alloy framing, add alerting + CloudWatch coverage
- 🟢 2026-07-25 · [.github#55](https://github.com/lentago/.github/issues/55) — README understates the repo and claims no community-health files are set
- 🟣 2026-07-25 · [.github#56](https://github.com/lentago/.github/pull/56) — docs(readme): fix false community-health claim and document fleet content
- 🟢 2026-07-25 · [music-curator#63](https://github.com/lentago/music-curator/issues/63) — README still frames the repo as a prompt-spec, not the tooling it became
- 🟣 2026-07-25 · [music-curator#64](https://github.com/lentago/music-curator/pull/64) — docs: reframe README around the productized toolchain
- 🟢 2026-07-25 · [music-curator#9](https://github.com/lentago/music-curator/issues/9) — Add an always-on gate check so auto-merge can arm (last .github#27 gap; sequence with the Obsidian wiki-manager productization)
- 🟣 2026-07-25 · [music-curator#65](https://github.com/lentago/music-curator/pull/65) — ci: replace the path-filtered validator with an unconditional integrity check
- 🟣 2026-07-25 · [epigaea#507](https://github.com/lentago/epigaea/pull/507) — Stop office/playroom flicker loops on an external off command
- 🟣 2026-07-25 · [drosera#177](https://github.com/lentago/drosera/pull/177) — Flatten the dashboard folder taxonomy into a single Lentago folder
- 🟢 2026-07-25 · [solidago#145](https://github.com/lentago/solidago/issues/145) — Mirror the Ask handler's structured logging into the vendored copy
- 🟣 2026-07-25 · [solidago#148](https://github.com/lentago/solidago/pull/148) — Mirror structured ask_query logging into the vendored handler
- 🟢 2026-07-25 · [drosera#150](https://github.com/lentago/drosera/issues/150) — Alert on ingest absence: no-data alerts for the critical Loki streams (zeek_dns, zeek_conn, firewalla_acl, device_inventory)
- 🟣 2026-07-25 · [drosera#175](https://github.com/lentago/drosera/pull/175) — Alert on ingest absence: no-data alerts for the critical Loki streams
- 🟢 2026-07-25 · [solidago#146](https://github.com/lentago/solidago/issues/146) — Bump betula_ref so the ALB shipper's IP truncation actually deploys
- 🟣 2026-07-25 · [solidago#147](https://github.com/lentago/solidago/pull/147) — Bump betula_ref to adopt ALB client-IP truncation
- 🟣 2026-07-25 · [drosera#174](https://github.com/lentago/drosera/pull/174) — Correct the uniques panel: IP truncation is not yet deployed
- 🟢 2026-07-25 · [drosera#161](https://github.com/lentago/drosera/issues/161) — Site analytics pane: Axiom datasource + per-site traffic panels
- 🟣 2026-07-25 · [drosera#173](https://github.com/lentago/drosera/pull/173) — Site analytics pane: Axiom datasource + per-site traffic panels
- 🟣 2026-07-25 · [betula#92](https://github.com/lentago/betula/pull/92) — feat(aws): CloudWatch Logs → Axiom forwarder (clients/aws/cloudwatch-logs)
- 🟢 2026-07-25 · [betula#90](https://github.com/lentago/betula/issues/90) — Decide retention and client-IP handling for the ALB access-log dataset
- 🟣 2026-07-25 · [betula#91](https://github.com/lentago/betula/pull/91) — feat(alb-logs): truncate client_ip at ingest for visitor privacy
- 🟢 2026-07-25 · [site-pondviewlane-com#23](https://github.com/lentago/site-pondviewlane-com/issues/23) — Ask box records nothing — no question, outcome, or cost is captured
- 🟣 2026-07-25 · [site-pondviewlane-com#24](https://github.com/lentago/site-pondviewlane-com/pull/24) — Ask box records nothing — no question, outcome, or cost is captured
- 🟢 2026-07-24 · [drosera#156](https://github.com/lentago/drosera/issues/156) — Decide Grafana-native alerting for site probes (ADR addendum)
- 🟣 2026-07-24 · [drosera#172](https://github.com/lentago/drosera/pull/172) — feat: Grafana-native alerting for site probes (ADR addendum)
- 🟢 2026-07-24 · [solidago#143](https://github.com/lentago/solidago/issues/143) — ECS app logs stopped reaching Axiom on 2026-07-08 and no signal fired
- 🟢 2026-07-24 · [drosera#170](https://github.com/lentago/drosera/issues/170) — essexcrossingatmontserrat.com has no probe and no dashboard
- 🟣 2026-07-24 · [drosera#171](https://github.com/lentago/drosera/pull/171) — feat: add essexcrossingatmontserrat.com probe and dashboard
- 🟢 2026-07-24 · [betula#87](https://github.com/lentago/betula/issues/87) — Collect ALB access logs for the public sites (S3 → Axiom)
- 🟣 2026-07-24 · [site-pondviewlane-com#22](https://github.com/lentago/site-pondviewlane-com/pull/22) — Add JSON-LD structured data, sitemap lastmod, and a /guides/ redirect
- 🟣 2026-07-24 · [site-pondviewlane-com#21](https://github.com/lentago/site-pondviewlane-com/pull/21) — Publish the July 28, 2026 Beverly ConCom agenda to the library
- 🟣 2026-07-23 · [music-curator#62](https://github.com/lentago/music-curator/pull/62) — Render Spotify follows in the vault + wire seeds via credits re-resolution
- 🟣 2026-07-23 · [music-curator#61](https://github.com/lentago/music-curator/pull/61) — Backfill 48 followed-but-unowned artists into the reservoir
- 🟣 2026-07-23 · [music-curator#60](https://github.com/lentago/music-curator/pull/60) — Follow ingestion automation — daily drain + fold Action
- 🟣 2026-07-23 · [site-pondviewlane-com#20](https://github.com/lentago/site-pondviewlane-com/pull/20) — Reframe both skins as a public site, not a residents' guide
- 🟣 2026-07-23 · [music-curator#59](https://github.com/lentago/music-curator/pull/59) — harvest_merge.py — fold Spotify follows into the inventory
- 🟣 2026-07-23 · [music-curator#58](https://github.com/lentago/music-curator/pull/58) — Fold accents in the dedup key, extract it to a shared module
- 🟣 2026-07-23 · [music-curator#57](https://github.com/lentago/music-curator/pull/57) — Spotify follow watcher: capture new follows and the song behind them
- 🟣 2026-07-23 · [music-curator#56](https://github.com/lentago/music-curator/pull/56) — Harvest follow deltas: first_followed / new_follow in the roll-up (schema v2)
- 🟣 2026-07-23 · [music-curator#55](https://github.com/lentago/music-curator/pull/55) — Drop the Compilations pseudo-artist from the inventory
- 🟣 2026-07-23 · [music-curator#54](https://github.com/lentago/music-curator/pull/54) — Restore the clean default preset as the active graph.json
- 🟣 2026-07-23 · [music-curator#53](https://github.com/lentago/music-curator/pull/53) — Surface the rotation layer in the vault
- 🟣 2026-07-23 · [music-curator#52](https://github.com/lentago/music-curator/pull/52) — Mark the periodic Spotify harvest shipped in the roadmap
- 🟢 2026-07-23 · [music-curator#47](https://github.com/lentago/music-curator/issues/47) — Spotify harvester has landed zero daily snapshots since setup (2026-07-12)
- 🟣 2026-07-23 · [music-curator#51](https://github.com/lentago/music-curator/pull/51) — Rework Spotify consumer to commit the roll-up via an auto-merged PR
- 🟣 2026-07-23 · [music-curator#50](https://github.com/lentago/music-curator/pull/50) — chore(harvest): 2026-07 Spotify roll-up
- 🟣 2026-07-22 · [music-curator#49](https://github.com/lentago/music-curator/pull/49) — Fix Spotify producer: URLSearchParams undefined in n8n Code sandbox
- 🟣 2026-07-22 · [music-curator#48](https://github.com/lentago/music-curator/pull/48) — Deploy prep for the Spotify harvester: monthly consumer + n8n staging
- 🟣 2026-07-22 · [music-curator#46](https://github.com/lentago/music-curator/pull/46) — Preserve the 2026-07-12 Spotify-migration collection CSVs
- 🟣 2026-07-22 · [brasenia#3](https://github.com/lentago/brasenia/pull/3) — Preserve the 2026-07-20 HLS validation artifacts
- 🟢 2026-07-22 · [music-curator#40](https://github.com/lentago/music-curator/issues/40) — Promote high-degree session connectors to person nodes
- 🟣 2026-07-22 · [music-curator#41](https://github.com/lentago/music-curator/pull/41) — feat: promote 15 session connectors to person nodes
- 🟣 2026-07-22 · [kalmia#66](https://github.com/lentago/kalmia/pull/66) — Repoint lunaria render source back to the Morning Brief
- 🟣 2026-07-21 · [.github#54](https://github.com/lentago/.github/pull/54) — Add runtime inventory (2026-07-21) to fleet-reports
- 🟣 2026-07-21 · [kalmia#65](https://github.com/lentago/kalmia/pull/65) — Repoint lunaria wall-display render source to the runtime inventory
- 🟣 2026-07-21 · [kalmia#64](https://github.com/lentago/kalmia/pull/64) — Point legacy-name notes at the rename tracking issue
- 🟣 2026-07-21 · [brasenia#2](https://github.com/lentago/brasenia/pull/2) — Cite kalmia#63 for the runtime rename under the fleet rename discipline
- 🟣 2026-07-21 · [shared-workflows#25](https://github.com/lentago/shared-workflows/pull/25) — Add fleet rename discipline (canonical source)
- 🟢 2026-07-21 · [kalmia#61](https://github.com/lentago/kalmia/issues/61) — Decide/execute runtime rename: lunaria → brasenia
- 🟣 2026-07-21 · [kalmia#62](https://github.com/lentago/kalmia/pull/62) — Decide/execute runtime rename: lunaria → brasenia
- 🟣 2026-07-21 · [brasenia#1](https://github.com/lentago/brasenia/pull/1) — Rename product lunaria → brasenia
- 🟣 2026-07-21 · [kalmia#60](https://github.com/lentago/kalmia/pull/60) — lunaria: pin container timezone (clock overlay showed UTC)
- 🟢 2026-07-21 · [kalmia#58](https://github.com/lentago/kalmia/issues/58) — lunaria: wall-display compositor LXC (terraform guest + provisioning role)
- 🟣 2026-07-21 · [kalmia#59](https://github.com/lentago/kalmia/pull/59) — lunaria: wall-display compositor LXC (terraform guest + provisioning role)
- 🟣 2026-07-21 · [kalmia#57](https://github.com/lentago/kalmia/pull/57) — pub: exclude TV edition from index.html and map it to tv.html
- 🟢 2026-07-21 · [kalmia#56](https://github.com/lentago/kalmia/issues/56) — pub: publish-morning-brief maps the TV edition onto index.html
- 🟢 2026-07-20 · [kalmia#54](https://github.com/lentago/kalmia/issues/54) — Bake the Morning Brief publisher into pub (LXC 114) provisioning
- 🟣 2026-07-20 · [kalmia#55](https://github.com/lentago/kalmia/pull/55) — feat: bake the Morning Brief publisher into pub (LXC 114) provisioning
- 🟢 2026-07-20 · [claytonia#63](https://github.com/lentago/claytonia/issues/63) — README: authorship disclosure missing; queue-core caveats predate the #61 test harness
- 🟣 2026-07-20 · [claytonia#64](https://github.com/lentago/claytonia/pull/64) — README: authorship disclosure + caveats updated for the queue-test harness
- 🟢 2026-07-20 · [claytonia#61](https://github.com/lentago/claytonia/issues/61) — Test harness for the queue core: claim-by-rename atomicity, at-least-once delivery, crash-mid-job recovery
- 🟣 2026-07-20 · [claytonia#62](https://github.com/lentago/claytonia/pull/62) — test: queue-core harness (claim races, delivery, crash recovery, write-then-rename) + atomic-first claim fix
- 🟣 2026-07-20 · [.github#53](https://github.com/lentago/.github/pull/53) — Weekly fleet reports refresh — 2026-07-20
- 🟣 2026-07-20 · [betula#88](https://github.com/lentago/betula/pull/88) — docs: refresh architecture.svg for Loki-only pipeline (#83)
- 🟢 2026-07-20 · [drosera#152](https://github.com/lentago/drosera/issues/152) — Doc drift: README/CLAUDE.md/AGENTS.md still describe the retired Promtail → Alloy :3100 relay for Zeek logs
- 🟣 2026-07-20 · [drosera#168](https://github.com/lentago/drosera/pull/168) — Fix doc drift: Zeek/ACL logs push directly to Cloud Loki
- 🟣 2026-07-20 · [site-lentago-dev#38](https://github.com/lentago/site-lentago-dev/pull/38) — docs(deploy): update resource names to solidago-dev
- 🟢 2026-07-20 · [music-curator#34](https://github.com/lentago/music-curator/issues/34) — spec: Dev Mode app cannot read playlist contents — data-availability allowlist row is wrong
- 🟣 2026-07-20 · [music-curator#39](https://github.com/lentago/music-curator/pull/39) — fix(spotify-spec): playlist track contents blocked in Dev Mode (#34)
- 🟢 2026-07-20 · [drosera#138](https://github.com/lentago/drosera/issues/138) — Trim node-exporter series with metric_relabel drop rules (~1k series of headroom under the 15k cap)
- 🟣 2026-07-20 · [drosera#167](https://github.com/lentago/drosera/pull/167) — Trim node-exporter series with metric_relabel drop rules
- 🟢 2026-07-20 · [drosera#129](https://github.com/lentago/drosera/issues/129) — claude-cost-export README: bullpen repo renamed to claytonia
- 🟣 2026-07-20 · [drosera#166](https://github.com/lentago/drosera/pull/166) — docs: update claude-cost-export README bullpen refs to Claytonia
- 🟢 2026-07-20 · [solidago#97](https://github.com/lentago/solidago/issues/97) — Eliminate perpetual ECS task-definition replacement in Terraform plans
- 🟢 2026-07-20 · [solidago#19](https://github.com/lentago/solidago/issues/19) — Design multi-domain architecture for portfolio sites
- 🟢 2026-07-20 · [solidago#18](https://github.com/lentago/solidago/issues/18) — Set up local Docker Engine on ChromeOS for local container builds
- 🟢 2026-07-20 · [betula#15](https://github.com/lentago/betula/issues/15) — Add conn.log bandwidth dashboard
- 🟢 2026-07-20 · [betula#12](https://github.com/lentago/betula/issues/12) — Terraform the Axiom backend
- 🟢 2026-07-20 · [betula#11](https://github.com/lentago/betula/issues/11) — Add New Domain Radar alert
- 🟢 2026-07-20 · [betula#9](https://github.com/lentago/betula/issues/9) — Add IPv6-to-device resolution
- 🟢 2026-07-20 · [betula#8](https://github.com/lentago/betula/issues/8) — Resolve remaining "Unknown" devices in group mapping
- 🟣 2026-07-19 · [solidago#141](https://github.com/lentago/solidago/pull/141) — ask-lambda: sync vendored handler — pondview naturalist homie persona
- 🟣 2026-07-19 · [site-pondviewlane-com#19](https://github.com/lentago/site-pondviewlane-com/pull/19) — Ask: pondview persona becomes the neighborhood-naturalist homie voice
- 🟣 2026-07-19 · [solidago#139](https://github.com/lentago/solidago/pull/139) — Add Google Search Console verification TXT for essexcrossingatmontserrat.com
- 🟣 2026-07-19 · [site-pondviewlane-com#18](https://github.com/lentago/site-pondviewlane-com/pull/18) — Repurpose the header search as an Ask entry; fix the dock's dead click target
- 🟣 2026-07-19 · [solidago#140](https://github.com/lentago/solidago/pull/140) — Vendoring sync: per-origin Ask persona (Obsequious Document on the essex apex)
- 🟢 2026-07-19 · [site-pondviewlane-com#15](https://github.com/lentago/site-pondviewlane-com/issues/15) — Rewrite the Essex skin in The Obsequious Document voice
- 🟣 2026-07-19 · [site-pondviewlane-com#17](https://github.com/lentago/site-pondviewlane-com/pull/17) — The Obsequious Document: Essex-skin rewrite, per-origin Ask persona, voiced generated framing
- 🟢 2026-07-19 · [site-pondviewlane-com#14](https://github.com/lentago/site-pondviewlane-com/issues/14) — Per-site prose architecture: content/base + content/essex overlay, composed docs tree, C7 facts-parity gate
- 🟣 2026-07-19 · [site-pondviewlane-com#16](https://github.com/lentago/site-pondviewlane-com/pull/16) — Per-site prose architecture: content/base + essex overlay, composed docs tree, C7 facts-parity gate
- 🟣 2026-07-19 · [site-pondviewlane-com#13](https://github.com/lentago/site-pondviewlane-com/pull/13) — Strike the About page's "The name" section
- 🟢 2026-07-19 · [solidago#137](https://github.com/lentago/solidago/issues/137) — Bring essexcrossingatmontserrat.com online in front of module.site_pondview
- 🟣 2026-07-19 · [solidago#138](https://github.com/lentago/solidago/pull/138) — Bring essexcrossingatmontserrat.com online in front of site_pondview (#137)
- 🟢 2026-07-19 · [site-pondviewlane-com#11](https://github.com/lentago/site-pondviewlane-com/issues/11) — Essex Crossing sister skin: two-domain build and Host-switched container
- 🟣 2026-07-19 · [site-pondviewlane-com#12](https://github.com/lentago/site-pondviewlane-com/pull/12) — Essex Crossing sister skin: two-domain build and Host-switched container
- 🟢 2026-07-19 · [claytonia#59](https://github.com/lentago/claytonia/issues/59) — run-job: allowed_tools breaks every job — variadic --allowedTools swallows the prompt argument
- 🟣 2026-07-19 · [claytonia#60](https://github.com/lentago/claytonia/pull/60) — fix: pass job prompt via stdin so --allowedTools stops swallowing it
- 🟢 2026-07-19 · [drosera#162](https://github.com/lentago/drosera/issues/162) — Reorganize and rename dashboards along product lines
- 🟣 2026-07-19 · [drosera#163](https://github.com/lentago/drosera/pull/163) — Reorganize and rename dashboards along product lines
- 🟣 2026-07-18 · [site-pondviewlane-com#10](https://github.com/lentago/site-pondviewlane-com/pull/10) — Polish pass: icon fallbacks, title/search/sitemap hygiene, styled 404, accurate lastUpdated
- 🟣 2026-07-18 · [solidago#136](https://github.com/lentago/solidago/pull/136) — Add Google Search Console verification TXT for lentago.dev and pondviewlane.com
- 🟣 2026-07-18 · [drosera#160](https://github.com/lentago/drosera/pull/160) — Unquote TargetGroup terms in site-dashboard SEARCH expressions
- 🟣 2026-07-18 · [drosera#159](https://github.com/lentago/drosera/pull/159) — Add Sites folder with per-site dashboards for the three public sites
- 🟣 2026-07-18 · [drosera#158](https://github.com/lentago/drosera/pull/158) — Probe the three public sites from the lab Alloy
- 🟣 2026-07-18 · [site-pondviewlane-com#9](https://github.com/lentago/site-pondviewlane-com/pull/9) — Add the Parcel C deed to the library; document the easement dimensions
- 🟣 2026-07-18 · [site-pondviewlane-com#8](https://github.com/lentago/site-pondviewlane-com/pull/8) — Clarify the Ice House Lane easement's "20 feet" is its width
- 🟣 2026-07-18 · [site-pondviewlane-com#7](https://github.com/lentago/site-pondviewlane-com/pull/7) — Add "No tax burden on the parcel" section to the Common Land guide
- 🟣 2026-07-18 · [site-pondviewlane-com#6](https://github.com/lentago/site-pondviewlane-com/pull/6) — Scrub second-person voice from the static prose
- 🟣 2026-07-18 · [site-pondviewlane-com#5](https://github.com/lentago/site-pondviewlane-com/pull/5) — Flag the trustee recording gap (record documents 4 of 5)
- 🟣 2026-07-18 · [site-pondviewlane-com#4](https://github.com/lentago/site-pondviewlane-com/pull/4) — Refresh the hero: Lora serif, redesigned mark, warmer card copy

---

## Code census

**The lens:** a `CLAUDE.md` (and its kin — `AGENTS.md`, skill `SKILL.md`, and the LLM prompt-programs that *are* a tool's logic) is an instruction set maintained for hygiene, so it's counted as **natural-language code**. Documentation, content/data, and community-health markdown are tallied separately and excluded from the code total, as are data payloads and generated files. This is a deliberate re-cut of the canonical [`metrics/language-census.md`](../metrics/language-census.md), which instead counts all Markdown/JSON/HTML as code.

### Languages

cloc *code* lines (blank + comment excluded). Shell folds Bourne + Bash. Instruction-markdown is promoted into the count (**bold**); the excluded buckets sit below the total.

| # | Language | Code | Files | Share |
|---|----------|-----:|------:|------:|
| 1 | JSON | 34,729 | 49 | 45.1% |
| 2 | YAML | 10,047 | 185 | 13.0% |
| 3 | Python | 7,527 | 47 | 9.8% |
| 4 | HCL | 6,696 | 115 | 8.7% |
| 5 | Shell (Bourne + Bash) | 5,432 | 69 | 7.1% |
| 6 | Text | 3,601 | 25 | 4.7% |
| 7 | **Instructions (CLAUDE.md family + prompt-programs)** | 2,094 | 16 | 2.7% |
| 8 | Astro | 1,895 | 19 | 2.5% |
| 9 | JavaScript | 1,842 | 17 | 2.4% |
| 10 | CSS | 1,260 | 9 | 1.6% |
| 11 | JSX | 852 | 10 | 1.1% |
| 12 | Jinja Template | 558 | 15 | 0.7% |
| 13 | TypeScript | 312 | 8 | 0.4% |
| 14 | Other (TOML / Dockerfile / …) | 113 | 7 | 0.1% |
| 15 | HTML | 57 | 1 | 0.1% |
| | **CODE TOTAL** | **77,015** | **592** | 100% |
| — | _Data / exports — excluded_ | 119,165 | 9 | — |
| — | _Generated (lockfiles, SVG, brand artefacts) — excluded_ | 28,101 | 82 | — |

### Instruction-markdown as code

- **Hygiene family** (16 files · `CLAUDE.md`, `AGENTS.md`, `SKILL.md`): **2,094 lines**
- **Prompt-programs** (0 files · reference-checker auditors): **0 lines**

#### Hygiene surface — each file is a maintenance obligation

| Repo | File | Lines |
|------|------|------:|
| epigaea | `CLAUDE.md` | 399 |
| shared-workflows | `CLAUDE.md` | 238 |
| site-pondviewlane-com | `CLAUDE.md` | 212 |
| .github | `CLAUDE.md` | 205 |
| betula | `CLAUDE.md` | 156 |
| kalmia | `CLAUDE.md` | 155 |
| site-lentago-dev | `CLAUDE.md` | 108 |
| solidago | `CLAUDE.md` | 99 |
| site-icecreamtofightwith-com | `CLAUDE.md` | 98 |
| drosera | `CLAUDE.md` | 96 |
| music-curator | `CLAUDE.md` | 68 |
| drosera | `AGENTS.md` | 67 |
| asclepias | `CLAUDE.md` | 58 |
| claytonia | `CLAUDE.md` | 57 |
| brasenia | `CLAUDE.md` | 56 |
| repo-template | `CLAUDE.md` | 22 |
| **16 files** | | **2,094** |

### Per-repo

| Repo | Code | Instr | Doc-md | Content-md | Data |
|------|-----:|------:|-------:|-----------:|-----:|
| epigaea | 24,021 | 399 | 1,495 | 0 | 0 |
| drosera | 16,522 | 163 | 1,470 | 0 | 0 |
| site-pondviewlane-com | 7,324 | 212 | 2,711 | 0 | 0 |
| solidago | 6,356 | 99 | 2,233 | 0 | 0 |
| music-curator | 5,622 | 68 | 1,254 | 11,645 | 119,165 |
| site-icecreamtofightwith-com | 3,459 | 98 | 897 | 6,004 | 0 |
| kalmia | 3,449 | 155 | 1,389 | 0 | 0 |
| .github | 2,688 | 205 | 1,421 | 3,104 | 0 |
| claytonia | 2,478 | 57 | 1,547 | 0 | 0 |
| betula | 1,832 | 156 | 1,565 | 0 | 0 |
| site-lentago-dev | 1,621 | 108 | 624 | 0 | 0 |
| shared-workflows | 1,082 | 238 | 729 | 0 | 0 |
| brasenia | 307 | 56 | 1,609 | 0 | 0 |
| asclepias | 166 | 58 | 587 | 0 | 0 |
| repo-template | 88 | 22 | 269 | 0 | 0 |

### Markdown taxonomy

The fleet carries **42,999 lines of Markdown across 950 files**; only 4.9% is instruction-code.

| Class | Lines | Files | Disposition |
|-------|------:|------:|-------------|
| **Instructions** | 2,094 | 16 | **counted as code** |
| Content / data | 20,753 | 693 | payload (vault notes, recipes, test-sets) — excluded |
| Documentation | 19,800 | 226 | READMEs, docs, ADRs, runbooks — excluded |
| Community-health | 352 | 15 | CONTRIBUTING/SECURITY/templates — excluded |
| **All Markdown** | **42,999** | **950** | |

---

## Method

- **Issues:** open issues via `gh search issues --owner lentago --state open`; activity from `gh search prs --owner lentago --merged` and closed issues filtered to the 30-day window. Public metadata only — no transcript harvest, ops items, or homelab detail (those live in the LAN copy).
- **Census tool:** `cloc`, run per-repo as `cloc --by-file --vcs=git` so only git-tracked files count (build output, `node_modules`, `.terraform`, venvs never enter). Lines are cloc *code* lines.
- **Scope:** the active repos owned by the `lentago` org, derived at runtime — personal repos and third-party clones are out of scope; archived repos are frozen and excluded.
- **Markdown classifier:** instruction-code = `CLAUDE.md`/`AGENTS.md`/`SKILL.md` or a versioned `prompts/*-auditor.md`; community-health = governance filenames + issue/PR templates; content = repo-scoped payload paths (music-curator `vault/`, ice-cream `recipes/`·manuscript, reference-checker `test-sets/`·`reports/`, dotgithub `fleet-reports/`); everything else = documentation.
- **Data / generated carve-outs:** exported payloads under the declared data dirs (music-curator `data/`, homeassistant-config `context/`) count as data whatever their serialisation — JSON, JSONL, CSV/TSV, XML, YAML — as does reference-checker's rendered `reports/*.html`; lockfiles, SVG and `.github/brand/generated/` (emitted from `brand/fleet.json`) are generated. drosera's `dashboards/*.json` stay in code as Terraform-enforced dashboards-as-code.
- **Regenerating:** `python3 metrics/generate-fleet-reports.py --out-dir .`

_Generated with Claude Code (Repo Claude)._
