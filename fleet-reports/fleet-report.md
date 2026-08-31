# Lentago Labs Fleet Report

> [!NOTE]
> **Co-authored with [Claude](https://claude.ai)** (Repo Claude, the Lentago Labs fleet steward). Auto-generated weekly from the fleet's public state (GitHub issues/PRs + `cloc` over public repo contents) — no personal, security, or homelab-internal detail is included. A prettier, editorialised copy renders on the Lentago lab LAN.

**Generated:** 2026-08-31 00:13 UTC · Scope: the **19 active** `lentago` repos (archived repos frozen &amp; excluded) · Activity window: last 30 days (since 2026-08-01).

## Snapshot

| Open issues | PRs merged (30d) | Issues closed (30d) | Code (incl. instructions) | Instruction-markdown |
|---:|---:|---:|---:|---:|
| **102** | 285 | 111 | **82,073** | 2,358 (20 files) |

The fleet's hand-maintained natural-language instruction surface (**2,358 lines** across 20 files) is among the largest "languages" in the code base — `reference-checker` alone is almost entirely prompt-program source.

---

## Open issues — 102 across 17 repos

### drosera — 18 open

| # | Title |
|---|-------|
| [204](https://github.com/lentago/drosera/issues/204) | Main-branch workflow failures notify nobody — alert on red deploys/applies |
| [200](https://github.com/lentago/drosera/issues/200) | Queue SLO for the agent fleet (pickup latency) + burn alert |
| [199](https://github.com/lentago/drosera/issues/199) | Error-budget monthly section in the fleet report |
| [198](https://github.com/lentago/drosera/issues/198) | Threat Weather: anonymized daily network weather report |
| [197](https://github.com/lentago/drosera/issues/197) | "Are we open" single source of truth |
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

### .github — 17 open

| # | Title |
|---|-------|
| [176](https://github.com/lentago/.github/issues/176) | Codify org settings in Terraform — default_repository_permission is live-only |
| [175](https://github.com/lentago/.github/issues/175) | A public repo entry with a null template_source cannot receive its first commit |
| [167](https://github.com/lentago/.github/issues/167) | Fleet reports - one-off run |
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
| [90](https://github.com/lentago/.github/issues/90) | Recommendation: engagement pathways — the lab ladder for new members |

### kalmia — 13 open

| # | Title |
|---|-------|
| [124](https://github.com/lentago/kalmia/issues/124) | Retire CT 113 (n8n LXC) after the osmunda burn-in window |
| [108](https://github.com/lentago/kalmia/issues/108) | Forge: golden images with receipts (checksums, SBOM, provenance) |
| [107](https://github.com/lentago/kalmia/issues/107) | Donated-hardware refresh profiles (new client class) |
| [104](https://github.com/lentago/kalmia/issues/104) | Terraform: adopt backup-job `exclude` once bpg/proxmox ships it |
| [99](https://github.com/lentago/kalmia/issues/99) | Cast client runtime for brasenia: watchdog sender, receiver hosting, then HLS-stack turn-down (brasenia ADR-0006) |
| [85](https://github.com/lentago/kalmia/issues/85) | power: assert charge thresholds actually reached sysfs instead of trusting the drop-in |
| [63](https://github.com/lentago/kalmia/issues/63) | Complete the lunaria → brasenia rename through runtime |
| [53](https://github.com/lentago/kalmia/issues/53) | Pre-merge guard: verify a ForceNew guest change can actually be re-created under the apply identity |
| [51](https://github.com/lentago/kalmia/issues/51) | Guarantee vzdump coverage for every Terraform-enforced guest (CT 113 had none) |
| [50](https://github.com/lentago/kalmia/issues/50) | Add prevent_destroy to import-only guests the token pipeline can't recreate (starting CT 113) |
| [20](https://github.com/lentago/kalmia/issues/20) | Roadmap: provisioning clients beyond Ansible-on-workstations — VMs and containers as peer targets |
| [15](https://github.com/lentago/kalmia/issues/15) | Live-test the crostini profile on the Chromebook penguin container |
| [14](https://github.com/lentago/kalmia/issues/14) | Live-test the ubuntu_laptop profile on real ThinkPad hardware |

### solidago — 13 open

| # | Title |
|---|-------|
| [190](https://github.com/lentago/solidago/issues/190) | docs/BOOTSTRAP.md still instructs operators to configure a nonexistent `foundry` AWS profile |
| [188](https://github.com/lentago/solidago/issues/188) | Make the Axiom integration optional, as Grafana Cloud now is |
| [184](https://github.com/lentago/solidago/issues/184) | CI plans are never clean: standing task-definition replacements and a recreating SNS email subscription |
| [180](https://github.com/lentago/solidago/issues/180) | Hardening backlog from tf-lint's first trivy run (ECR immutability, CI-role least-privilege, SNS encryption) |
| [172](https://github.com/lentago/solidago/issues/172) | SNS alert email subscription is recreated on every apply — alerts may be reaching nobody |
| [169](https://github.com/lentago/solidago/issues/169) | Extend variable validation blocks beyond 1 of 24 modules |
| [168](https://github.com/lentago/solidago/issues/168) | Ask the Estate: grounded-Ask demo over fleet docs |
| [167](https://github.com/lentago/solidago/issues/167) | Dogfood DMARC posture on fleet domains (precondition for the Email Trust kit) |
| [156](https://github.com/lentago/solidago/issues/156) | Split plan/apply OIDC environments so the terraform environment can carry a branch policy |
| [149](https://github.com/lentago/solidago/issues/149) | Rotating a Lambda's Axiom token requires an unrelated apply to take effect |
| [144](https://github.com/lentago/solidago/issues/144) | Ask Lambda logs land in CloudWatch with no path to Axiom |
| [124](https://github.com/lentago/solidago/issues/124) | ECS task defs show a perpetual replace-diff (container_definitions normalization) — plan noise + apply-side-effect landmine |
| [21](https://github.com/lentago/solidago/issues/21) | Evaluate migration from ElastiCache node-based to serverless |

### mitchella — 12 open

| # | Title |
|---|-------|
| [12](https://github.com/lentago/mitchella/issues/12) | Bound the cost: caps and reporting |
| [11](https://github.com/lentago/mitchella/issues/11) | An eval set, so changes are measurable |
| [10](https://github.com/lentago/mitchella/issues/10) | Ship telemetry to drosera |
| [9](https://github.com/lentago/mitchella/issues/9) | Deploy the desk so it outlives a terminal |
| [8](https://github.com/lentago/mitchella/issues/8) | Filing controls: idempotency, rate limits, kill switch, audit |
| [7](https://github.com/lentago/mitchella/issues/7) | Decide attribution: service account or per-user OAuth |
| [6](https://github.com/lentago/mitchella/issues/6) | Issue tracker client: turn a confirmed draft into a filing |
| [5](https://github.com/lentago/mitchella/issues/5) | Slack: confirm-before-file button and modal |
| [4](https://github.com/lentago/mitchella/issues/4) | ADR: supersede ADR-0005 to authorise one scoped write path |
| [3](https://github.com/lentago/mitchella/issues/3) | Slack hardening: visible failures, block limits, retries |
| [2](https://github.com/lentago/mitchella/issues/2) | Hold a conversation: thread context across turns |
| [1](https://github.com/lentago/mitchella/issues/1) | Exercise the real API path end to end |

### claytonia — 8 open

| # | Title |
|---|-------|
| [110](https://github.com/lentago/claytonia/issues/110) | Ship workers/<host>.alive heartbeats to Loki — unblocks the bullpen liveness alerts |
| [99](https://github.com/lentago/claytonia/issues/99) | Second job type: batch document/report jobs through the queue contract |
| [65](https://github.com/lentago/claytonia/issues/65) | Complete the bullpen → claytonia rename on-host |
| [47](https://github.com/lentago/claytonia/issues/47) | Roadmap: platform-agnostic workers — Claude Code as one runtime behind the queue contract |
| [31](https://github.com/lentago/claytonia/issues/31) | Add optional authentication to the n8n Bullpen job-submit form |
| [24](https://github.com/lentago/claytonia/issues/24) | Branch hygiene across overlapping sessions: clean-desk session-end + prefer fleet dispatch |
| [22](https://github.com/lentago/claytonia/issues/22) | Fleet PR lane separation: rebase-before-merge + dispatch-time overlap check (no two writers on one file/panel) |
| [21](https://github.com/lentago/claytonia/issues/21) | Queue admission control: job ownership, fleet occupancy, and capacity awareness at submit time |

### betula — 5 open

| # | Title |
|---|-------|
| [107](https://github.com/lentago/betula/issues/107) | Device drift self-report: deployed conf hash vs main |
| [106](https://github.com/lentago/betula/issues/106) | Third AWS emitter: CloudTrail → archive + weekly access digest |
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

### music-curator — 4 open

| # | Title |
|---|-------|
| [87](https://github.com/lentago/music-curator/issues/87) | follow-fold's bot merge cannot work under GITHUB_TOKEN — two blockers; decide App identity vs human merge |
| [45](https://github.com/lentago/music-curator/issues/45) | Web-verify the promoted person nodes' credit rows |
| [44](https://github.com/lentago/music-curator/issues/44) | Producer-class connectors: decide representation |
| [43](https://github.com/lentago/music-curator/issues/43) | Session-tie receipts: render the credits justifying each edge |

### epigaea — 1 open

| # | Title |
|---|-------|
| [518](https://github.com/lentago/epigaea/issues/518) | Complete the epigaea rename through runtime (tiers 3–4) |

### lupinus — 1 open

| # | Title |
|---|-------|
| [4](https://github.com/lentago/lupinus/issues/4) | Epic: adoption guide — Phase 1 (launch set: solidago + monarda) |

### monarda — 1 open

| # | Title |
|---|-------|
| [5](https://github.com/lentago/monarda/issues/5) | Run the dry-run and record the first receipt |

### osmunda — 1 open

| # | Title |
|---|-------|
| [4](https://github.com/lentago/osmunda/issues/4) | The k3s install is disclaimed by both osmunda and kalmia — it exists nowhere |

### shared-workflows — 1 open

| # | Title |
|---|-------|
| [57](https://github.com/lentago/shared-workflows/issues/57) | Rapid successive merges cancel site deploys, and `:latest`-pinned task defs make the survivor non-deterministic |

### site-icecreamtofightwith-com — 1 open

| # | Title |
|---|-------|
| [158](https://github.com/lentago/site-icecreamtofightwith-com/issues/158) | Tier accent swatches fail WCAG AA contrast as chip/step backgrounds (design decision needed) |

### site-lentago-dev — 1 open

| # | Title |
|---|-------|
| [67](https://github.com/lentago/site-lentago-dev/issues/67) | a11y gate ignores `color-contrast`: the Tidewater palette fails 4.5:1 at the design-token level |

### site-pondviewlane-com — 1 open

| # | Title |
|---|-------|
| [46](https://github.com/lentago/site-pondviewlane-com/issues/46) | Flip Content-Security-Policy from Report-Only to enforcing |

## Activity — last 30 days

**396 events**, one stream, newest first — 🟣 285 PRs merged · 🟢 111 issues closed

- 🟣 2026-08-30 · [site-pondviewlane-com#76](https://github.com/lentago/site-pondviewlane-com/pull/76) — essex: vary the escape-hatch link text from a per-page sneer pool
- 🟣 2026-08-30 · [site-pondviewlane-com#75](https://github.com/lentago/site-pondviewlane-com/pull/75) — essex: a footer escape hatch to the plainer sister skin
- 🟣 2026-08-30 · [drosera#212](https://github.com/lentago/drosera/pull/212) — feat(alerts): lab host + Home Assistant availability alerting (2026-08-29 pve3 outage)
- 🟣 2026-08-30 · [site-pondviewlane-com#73](https://github.com/lentago/site-pondviewlane-com/pull/73) — Bump the astro-stack group with 2 updates
- 🟣 2026-08-30 · [site-pondviewlane-com#72](https://github.com/lentago/site-pondviewlane-com/pull/72) — Bump nginx from `8f029c5` to `b34848e`
- 🟣 2026-08-30 · [.github#178](https://github.com/lentago/.github/pull/178) — build(deps): bump github/codeql-action/upload-sarif from 4.37.7 to 4.37.9 in the actions-routine group
- 🟣 2026-08-28 · [mitchella#13](https://github.com/lentago/mitchella/pull/13) — Add a roadmap to MVP
- 🟢 2026-08-28 · [asclepias#8](https://github.com/lentago/asclepias/issues/8) — Re-audit lab and onboarding access statements after the Players team retirement
- 🟣 2026-08-28 · [asclepias#9](https://github.com/lentago/asclepias/pull/9) — docs: re-audit access statements after Players team retirement
- 🟣 2026-08-28 · [.github#177](https://github.com/lentago/.github/pull/177) — Cite #176 from the ADR-0003 open-work note
- 🟣 2026-08-28 · [.github#174](https://github.com/lentago/.github/pull/174) — Add mitchella to the fleet
- 🟣 2026-08-28 · [.github#173](https://github.com/lentago/.github/pull/173) — Retire the Players team from the merge-gate rationale
- 🟢 2026-08-26 · [solidago#20](https://github.com/lentago/solidago/issues/20) — Document: Phase 2 Secrets Manager secret unused after RDS-managed password choice
- 🟣 2026-08-26 · [solidago#192](https://github.com/lentago/solidago/pull/192) — docs: document Phase 2 db-credentials secret as unused
- 🟣 2026-08-26 · [lupinus#5](https://github.com/lentago/lupinus/pull/5) — build(deps): Bump actions/checkout from 4.2.2 to 7.0.1 in the actions-major group
- 🟢 2026-08-26 · [kalmia#16](https://github.com/lentago/kalmia/issues/16) — Harden the xubuntu profile for Ubuntu 26.04 (stale comment + Docker CE repo codename)
- 🟣 2026-08-26 · [kalmia#128](https://github.com/lentago/kalmia/pull/128) — fix(xubuntu): update stale 24.04 comment, fall back Docker CE repo codename
- 🟢 2026-08-26 · [site-lentago-dev#48](https://github.com/lentago/site-lentago-dev/issues/48) — Add @astrojs/sitemap and a pa11y smoke to the PR gate
- 🟣 2026-08-26 · [site-lentago-dev#66](https://github.com/lentago/site-lentago-dev/pull/66) — feat: add @astrojs/sitemap and pa11y/axe WCAG 2.2 AA smoke test
- 🟢 2026-08-26 · [site-lentago-dev#61](https://github.com/lentago/site-lentago-dev/issues/61) — Add a 'Do it yourself' link to the adoption guide
- 🟣 2026-08-26 · [site-lentago-dev#65](https://github.com/lentago/site-lentago-dev/pull/65) — Add adoption guide link to pledge section
- 🟢 2026-08-26 · [claytonia#71](https://github.com/lentago/claytonia/issues/71) — Reaper cannot see a job left in processing/ without an .owner file — permanent phantom occupancy
- 🟣 2026-08-26 · [claytonia#112](https://github.com/lentago/claytonia/pull/112) — fix(reaper): reclaim ownerless processing entries with no completion proof
- 🟢 2026-08-26 · [solidago#153](https://github.com/lentago/solidago/issues/153) — bootstrap-backend.sh still references a nonexistent "foundry" AWS profile
- 🟣 2026-08-26 · [solidago#191](https://github.com/lentago/solidago/pull/191) — fix(bootstrap): remove hardcoded foundry AWS_PROFILE and correct KMS key description
- 🟣 2026-08-26 · [.github#171](https://github.com/lentago/.github/pull/171) — build(deps): bump the actions-major group with 2 updates
- 🟣 2026-08-26 · [site-lentago-dev#63](https://github.com/lentago/site-lentago-dev/pull/63) — chore(deps): Bump lentago/shared-workflows/.github/workflows/site-deploy.yml from 1.1.1 to 1.2.2 in the actions-routine group
- 🟣 2026-08-26 · [site-pondviewlane-com#70](https://github.com/lentago/site-pondviewlane-com/pull/70) — Bump lentago/shared-workflows/.github/workflows/site-deploy.yml from 1.1.1 to 1.2.2 in the actions-routine group
- 🟣 2026-08-26 · [site-lentago-dev#64](https://github.com/lentago/site-lentago-dev/pull/64) — chore(deps): Bump the astro-stack group with 2 updates
- 🟣 2026-08-26 · [site-icecreamtofightwith-com#183](https://github.com/lentago/site-icecreamtofightwith-com/pull/183) — Bump the astro-stack group with 2 updates
- 🟣 2026-08-26 · [site-icecreamtofightwith-com#185](https://github.com/lentago/site-icecreamtofightwith-com/pull/185) — Bump the actions-major group with 2 updates
- 🟣 2026-08-26 · [site-icecreamtofightwith-com#184](https://github.com/lentago/site-icecreamtofightwith-com/pull/184) — Bump the actions-routine group with 2 updates
- 🟣 2026-08-26 · [site-pondviewlane-com#71](https://github.com/lentago/site-pondviewlane-com/pull/71) — Bump astro from 7.2.2 to 7.2.4 in the astro-stack group
- 🟣 2026-08-26 · [site-pondviewlane-com#69](https://github.com/lentago/site-pondviewlane-com/pull/69) — Bump nginx from `8541484` to `8f029c5`
- 🟣 2026-08-26 · [site-lentago-dev#62](https://github.com/lentago/site-lentago-dev/pull/62) — chore(deps): Bump nginx from `8541484` to `0d4374c`
- 🟣 2026-08-26 · [site-icecreamtofightwith-com#182](https://github.com/lentago/site-icecreamtofightwith-com/pull/182) — Bump nginx from `8541484` to `0d4374c`
- 🟣 2026-08-26 · [repo-template#20](https://github.com/lentago/repo-template/pull/20) — Bump the actions-routine group with 3 updates
- 🟣 2026-08-26 · [monarda#7](https://github.com/lentago/monarda/pull/7) — Bump the actions-major group with 6 updates
- 🟣 2026-08-26 · [claytonia#111](https://github.com/lentago/claytonia/pull/111) — chore(deps): bump lentago/shared-workflows/.github/workflows/tf-lint.yml from 1.2.0 to 1.2.2 in the actions-routine group
- 🟣 2026-08-26 · [solidago#189](https://github.com/lentago/solidago/pull/189) — build(deps): bump lentago/shared-workflows/.github/workflows/tf-lint.yml from 1.2.0 to 1.2.2 in the actions-routine group
- 🟣 2026-08-26 · [kalmia#125](https://github.com/lentago/kalmia/pull/125) — build(deps): bump lentago/shared-workflows/.github/workflows/tf-lint.yml from 1.2.0 to 1.2.2 in the actions-routine group
- 🟣 2026-08-26 · [drosera#211](https://github.com/lentago/drosera/pull/211) — chore(deps): Bump lentago/shared-workflows/.github/workflows/tf-lint.yml from 1.2.0 to 1.2.2 in the actions-routine group
- 🟣 2026-08-26 · [.github#170](https://github.com/lentago/.github/pull/170) — build(deps): bump lentago/shared-workflows/.github/workflows/tf-lint.yml from 1.2.0 to 1.2.2 in the actions-routine group
- 🟣 2026-08-26 · [shared-workflows#56](https://github.com/lentago/shared-workflows/pull/56) — chore(deps): Bump the actions-routine group with 3 updates
- 🟣 2026-08-24 · [.github#172](https://github.com/lentago/.github/pull/172) — Weekly fleet reports refresh — 2026-08-24
- 🟢 2026-08-23 · [kalmia#126](https://github.com/lentago/kalmia/issues/126) — repos role clones flat into ~/repos/<name>; fleet layout is owner-grouped (lentago/, cpitzi/)
- 🟣 2026-08-23 · [kalmia#127](https://github.com/lentago/kalmia/pull/127) — repos: clone owner-grouped into ~/repos/<owner>/<name> (closes #126)
- 🟢 2026-08-22 · [.github#148](https://github.com/lentago/.github/issues/148) — music-curator push allowlist: the Actions-app entry applies successfully but never persists
- 🟣 2026-08-22 · [.github#169](https://github.com/lentago/.github/pull/169) — fix: drop the dead Actions-app allowance and add a post-apply convergence check
- 🟣 2026-08-22 · [.github#168](https://github.com/lentago/.github/pull/168) — Weekly fleet reports refresh — 2026-08-22
- 🟣 2026-08-22 · [.github#166](https://github.com/lentago/.github/pull/166) — docs: catch the org profile and repo docs up to the current fleet
- 🟢 2026-08-21 · [solidago#186](https://github.com/lentago/solidago/issues/186) — Add ADOPTION.md — the adopter's front door, with BOOTSTRAP as its step reference
- 🟣 2026-08-21 · [solidago#187](https://github.com/lentago/solidago/pull/187) — docs: add ADOPTION.md as the adopter's front door (#186)
- 🟢 2026-08-21 · [monarda#4](https://github.com/lentago/monarda/issues/4) — Add ADOPTION.md — the kit's front door in the fleet's standard shape
- 🟣 2026-08-21 · [monarda#6](https://github.com/lentago/monarda/pull/6) — docs: add ADOPTION.md — standard drill-and-receipt runbook (closes #4)
- 🟢 2026-08-21 · [lupinus#1](https://github.com/lentago/lupinus/issues/1) — Kit CI: inline docs-check, drop the Claude workflows
- 🟣 2026-08-21 · [lupinus#2](https://github.com/lentago/lupinus/pull/2) — ci: inline docs-check, drop cross-org Claude workflows
- 🟣 2026-08-21 · [lupinus#3](https://github.com/lentago/lupinus/pull/3) — feat: the adoption guide and ops-vault scaffold
- 🟣 2026-08-20 · [solidago#185](https://github.com/lentago/solidago/pull/185) — Elevate the essex Ask persona to full prostration (vendored handler sync)
- 🟣 2026-08-20 · [site-pondviewlane-com#68](https://github.com/lentago/site-pondviewlane-com/pull/68) — Elevate the Essex Crossing persona to full prostration
- 🟣 2026-08-20 · [site-pondviewlane-com#67](https://github.com/lentago/site-pondviewlane-com/pull/67) — guides: trees — worked example of the three layers, the 2026 nine-pine removal
- 🟣 2026-08-20 · [site-pondviewlane-com#66](https://github.com/lentago/site-pondviewlane-com/pull/66) — library: ConCom 7/28/2026 minutes excerpt — nine-pine removal approved (Negative 3)
- 🟢 2026-08-19 · [.github#162](https://github.com/lentago/.github/issues/162) — Epic: adoption guide (lupinus) — Phase 0 enablers
- 🟣 2026-08-19 · [shared-workflows#55](https://github.com/lentago/shared-workflows/pull/55) — chore(release): bump internal composite-action refs to v1.2.2 ahead of tagging
- 🟢 2026-08-19 · [shared-workflows#53](https://github.com/lentago/shared-workflows/issues/53) — shellcheck reusable: apt-get stall wedges required checks — use preinstalled shellcheck + job timeout
- 🟣 2026-08-19 · [shared-workflows#54](https://github.com/lentago/shared-workflows/pull/54) — fix(shellcheck): use preinstalled shellcheck with guarded apt fallback
- 🟢 2026-08-19 · [.github#164](https://github.com/lentago/.github/issues/164) — Birth apply races GitHub's async default-label seeding (lupinus lost, osmunda/monarda won)
- 🟣 2026-08-19 · [.github#165](https://github.com/lentago/.github/pull/165) — docs: record the birth-labels race in the add-a-repo runbook
- 🟢 2026-08-19 · [.github#161](https://github.com/lentago/.github/issues/161) — Add lupinus to the fleet — the adoption guide and ops-vault kit
- 🟣 2026-08-19 · [.github#163](https://github.com/lentago/.github/pull/163) — feat: birth lupinus — the adoption guide and ops-vault kit
- 🟢 2026-08-19 · [solidago#182](https://github.com/lentago/solidago/issues/182) — Adoption enablers: ship terraform.tfvars.example and make Grafana Cloud variables optional
- 🟣 2026-08-19 · [solidago#183](https://github.com/lentago/solidago/pull/183) — feat(adoption): tfvars.example, optional Grafana Cloud, fix BOOTSTRAP Step 4 (#182)
- 🟢 2026-08-19 · [monarda#2](https://github.com/lentago/monarda/issues/2) — Remove cross-org CI residue from the template: inline docs-check, drop Claude workflows
- 🟣 2026-08-19 · [monarda#3](https://github.com/lentago/monarda/pull/3) — Remove cross-org CI residue: inline docs-check, drop Claude workflows
- 🟢 2026-08-19 · [repo-template#18](https://github.com/lentago/repo-template/issues/18) — Pin shared-workflows caller refs to release tags
- 🟣 2026-08-19 · [repo-template#19](https://github.com/lentago/repo-template/pull/19) — ci: pin shared-workflows caller refs to v1.2.1
- 🟢 2026-08-18 · [.github#153](https://github.com/lentago/.github/issues/153) — Policy decision: require signed commits on main? (tf-lint GIT-0004)
- 🟣 2026-08-18 · [.github#160](https://github.com/lentago/.github/pull/160) — docs: signed commits deliberately not required (resolves #153, option 2)
- 🟢 2026-08-18 · [kalmia#52](https://github.com/lentago/kalmia/issues/52) — Codify the n8n container's provisioning (Docker + compose) — recreate yields a bare template
- 🟢 2026-08-18 · [solidago#164](https://github.com/lentago/solidago/issues/164) — Enable ECR scan-on-push for the site repositories
- 🟢 2026-08-18 · [shared-workflows#39](https://github.com/lentago/shared-workflows/issues/39) — Artifact attestations on site images (SLSA Build L2 → L3 via the reusable deploy)
- 🟣 2026-08-17 · [site-lentago-dev#55](https://github.com/lentago/site-lentago-dev/pull/55) — chore(deps): Bump the npm-major group across 1 directory with 4 updates
- 🟣 2026-08-17 · [drosera#210](https://github.com/lentago/drosera/pull/210) — chore(deps): Bump the actions-major group across 1 directory with 7 updates
- 🟣 2026-08-17 · [site-lentago-dev#60](https://github.com/lentago/site-lentago-dev/pull/60) — build(deps): upgrade Astro 5 → 7.2.2 + @astrojs/react 4 → 6.0.2 (astro-stack)
- 🟣 2026-08-17 · [site-icecreamtofightwith-com#181](https://github.com/lentago/site-icecreamtofightwith-com/pull/181) — build: upgrade Astro 5 → 7.2.2 (astro-stack major migration)
- 🟣 2026-08-17 · [claytonia#107](https://github.com/lentago/claytonia/pull/107) — chore(deps): bump the actions-major group with 4 updates
- 🟢 2026-08-17 · [.github#119](https://github.com/lentago/.github/issues/119) — Create the Kubernetes platform repo (k3s + ephemeral EKS, pull-based GitOps, IRSA)
- 🟣 2026-08-17 · [osmunda#3](https://github.com/lentago/osmunda/pull/3) — feat: EKS drill scripts + measured numbers from drill #1
- 🟣 2026-08-17 · [site-pondviewlane-com#64](https://github.com/lentago/site-pondviewlane-com/pull/64) — build(deps): upgrade astro 5→7.2.2 + Starlight 0.36→0.41.7 (astro-stack)
- 🟢 2026-08-17 · [drosera#207](https://github.com/lentago/drosera/issues/207) — Bullpen liveness + retry-event alerting — game-day #1's confirmed gap
- 🟣 2026-08-17 · [drosera#209](https://github.com/lentago/drosera/pull/209) — feat(alerts): bullpen liveness + retry alerting (#207)
- 🟢 2026-08-17 · [kalmia#122](https://github.com/lentago/kalmia/issues/122) — Guests with feature flags beyond nesting cannot be born via CI — document the pre-create+import path (hit on k3s pool)
- 🟣 2026-08-17 · [kalmia#123](https://github.com/lentago/kalmia/pull/123) — docs(terraform): document feature-flag pre-create rail
- 🟣 2026-08-17 · [drosera#208](https://github.com/lentago/drosera/pull/208) — ci: skip terraform plan for dependabot PRs
- 🟢 2026-08-17 · [solidago#173](https://github.com/lentago/solidago/issues/173) — Prune the rename-era OIDC trust entries from the app deploy role
- 🟣 2026-08-17 · [solidago#181](https://github.com/lentago/solidago/pull/181) — iam: prune rename-era dead OIDC trust subs from app deploy role (#173)
- 🟣 2026-08-17 · [kalmia#117](https://github.com/lentago/kalmia/pull/117) — build(deps): bump the actions-major group with 5 updates
- 🟣 2026-08-17 · [site-pondviewlane-com#60](https://github.com/lentago/site-pondviewlane-com/pull/60) — Bump sharp from 0.33.5 to 0.35.3 in the npm-routine group across 1 directory
- 🟣 2026-08-17 · [shared-workflows#49](https://github.com/lentago/shared-workflows/pull/49) — chore(deps): Bump the actions-major group across 1 directory with 5 updates
- 🟣 2026-08-17 · [site-pondviewlane-com#63](https://github.com/lentago/site-pondviewlane-com/pull/63) — Bump the actions-major group across 1 directory with 2 updates
- 🟣 2026-08-17 · [site-lentago-dev#57](https://github.com/lentago/site-lentago-dev/pull/57) — chore(deps): Bump the actions-major group across 1 directory with 2 updates
- 🟣 2026-08-17 · [site-icecreamtofightwith-com#176](https://github.com/lentago/site-icecreamtofightwith-com/pull/176) — Bump the actions-major group across 1 directory with 4 updates
- 🟣 2026-08-17 · [music-curator#84](https://github.com/lentago/music-curator/pull/84) — chore(deps): bump the actions-major group across 1 directory with 2 updates
- 🟣 2026-08-17 · [.github#156](https://github.com/lentago/.github/pull/156) — build(deps): bump the actions-major group across 1 directory with 7 updates
- 🟣 2026-08-17 · [epigaea#517](https://github.com/lentago/epigaea/pull/517) — build(deps): bump the actions-major group across 1 directory with 2 updates
- 🟣 2026-08-17 · [betula#109](https://github.com/lentago/betula/pull/109) — chore(deps): bump the actions-major group with 2 updates
- 🟢 2026-08-17 · [.github#120](https://github.com/lentago/.github/issues/120) — Create the campaign-site kit template repo
- 🟢 2026-08-17 · [asclepias#6](https://github.com/lentago/asclepias/issues/6) — Run game-day #1 against the agent fleet; publish the post-mortem
- 🟣 2026-08-17 · [.github#159](https://github.com/lentago/.github/pull/159) — docs: game-day #1 post-mortem (runner kill → 84s self-heal, no alert fired)
- 🟣 2026-08-17 · [osmunda#2](https://github.com/lentago/osmunda/pull/2) — fix: n8n memory limit + ingress class (first live deploy findings)
- 🟢 2026-08-17 · [drosera#196](https://github.com/lentago/drosera/issues/196) — Estate status page (uptime vs SLO, error budget, CI health) + client-facing variant
- 🟣 2026-08-17 · [drosera#206](https://github.com/lentago/drosera/pull/206) — feat: estate status page (uptime vs SLO, error budget, CI health)
- 🟢 2026-08-17 · [.github#121](https://github.com/lentago/.github/issues/121) — Publish the fleet's own lock-in ledger; then cut the client template
- 🟣 2026-08-17 · [.github#158](https://github.com/lentago/.github/pull/158) — Lock-in Ledger: fleet self-audit + client template with renewal-calendar-as-code
- 🟢 2026-08-17 · [site-lentago-dev#49](https://github.com/lentago/site-lentago-dev/issues/49) — Site v3: sovereignty copy, Offerings↔receipts section, the pledge, bespoke shelf
- 🟣 2026-08-17 · [site-lentago-dev#59](https://github.com/lentago/site-lentago-dev/pull/59) — Site v3: sovereignty hero, Offerings↔receipts, the pledge, bespoke shelf
- 🟣 2026-08-17 · [monarda#1](https://github.com/lentago/monarda/pull/1) — P14: campaign-site kit (Astro site + deploy workflows + intake/dry-run)
- 🟣 2026-08-17 · [osmunda#1](https://github.com/lentago/osmunda/pull/1) — Scaffold osmunda Kubernetes platform (C01)
- 🟣 2026-08-17 · [kalmia#121](https://github.com/lentago/kalmia/pull/121) — feat(terraform): provision osmunda k3s node pool (C01 phase 1)
- 🟣 2026-08-17 · [.github#157](https://github.com/lentago/.github/pull/157) — feat: birth osmunda (Kubernetes platform) and monarda (campaign-site kit)
- 🟣 2026-08-17 · [shared-workflows#52](https://github.com/lentago/shared-workflows/pull/52) — docs: enforced-surfaces table — .github settings are now apply-on-merge
- 🟢 2026-08-17 · [.github#81](https://github.com/lentago/.github/issues/81) — terraform: wire plan-on-PR and apply-on-merge for the fleet settings module
- 🟣 2026-08-17 · [.github#155](https://github.com/lentago/.github/pull/155) — ci: require gate — settings apply-on-merge phase complete (R19 step 4)
- 🟣 2026-08-17 · [.github#152](https://github.com/lentago/.github/pull/152) — ci(terraform): wire plan-on-PR and apply-on-merge (R19 step 3)
- 🟣 2026-08-17 · [site-icecreamtofightwith-com#161](https://github.com/lentago/site-icecreamtofightwith-com/pull/161) — Bump nginx from `963cfe6` to `8541484`
- 🟣 2026-08-17 · [site-icecreamtofightwith-com#180](https://github.com/lentago/site-icecreamtofightwith-com/pull/180) — fix: release workflow missing lmodern (PDF conversion failed)
- 🟣 2026-08-17 · [.github#154](https://github.com/lentago/.github/pull/154) — ci: require tf-lint / tf-lint on the five Terraform repos
- 🟣 2026-08-17 · [solidago#179](https://github.com/lentago/solidago/pull/179) — iam: add scoped OIDC terraform role for lentago/.github (R19 step 1)
- 🟢 2026-08-17 · [site-icecreamtofightwith-com#156](https://github.com/lentago/site-icecreamtofightwith-com/issues/156) — Tagged releases: attested, versioned cookbook PDFs
- 🟣 2026-08-17 · [site-icecreamtofightwith-com#178](https://github.com/lentago/site-icecreamtofightwith-com/pull/178) — ci: tag-driven attested cookbook PDF releases (issue #156)
- 🟣 2026-08-17 · [site-icecreamtofightwith-com#179](https://github.com/lentago/site-icecreamtofightwith-com/pull/179) — fix: spelling in Dockerfile comment (typos gate)
- 🟣 2026-08-17 · [solidago#178](https://github.com/lentago/solidago/pull/178) — ci: adopt fleet Terraform lint reusable workflow (shared-workflows v1.2.0)
- 🟣 2026-08-17 · [.github#151](https://github.com/lentago/.github/pull/151) — feat(ci): adopt shared tf-lint reusable workflow
- 🟣 2026-08-17 · [kalmia#120](https://github.com/lentago/kalmia/pull/120) — ci: adopt fleet shared tf-lint workflow (shared-workflows v1.2.0)
- 🟣 2026-08-17 · [drosera#205](https://github.com/lentago/drosera/pull/205) — ci: adopt shared tf-lint reusable workflow (v1.2.0)
- 🟣 2026-08-17 · [claytonia#109](https://github.com/lentago/claytonia/pull/109) — ci(terraform): adopt shared tf-lint reusable workflow (R18)
- 🟣 2026-08-17 · [site-pondviewlane-com#62](https://github.com/lentago/site-pondviewlane-com/pull/62) — ci: adopt site-deploy reusable workflow @ v1.1.1
- 🟣 2026-08-17 · [site-icecreamtofightwith-com#177](https://github.com/lentago/site-icecreamtofightwith-com/pull/177) — fix: move nginx digest comment off the FROM line (deploys broken since R01 pin)
- 🟣 2026-08-17 · [site-icecreamtofightwith-com#175](https://github.com/lentago/site-icecreamtofightwith-com/pull/175) — ci: adopt shared site-deploy reusable workflow (v1.1.1)
- 🟣 2026-08-17 · [epigaea#520](https://github.com/lentago/epigaea/pull/520) — docs: add GitOps loop diagram, document HA_SYNC_PAT
- 🟢 2026-08-17 · [shared-workflows#41](https://github.com/lentago/shared-workflows/issues/41) — Reusable tf-lint workflow (fmt -check, tflint, trivy config) for the five Terraform repos
- 🟣 2026-08-17 · [shared-workflows#50](https://github.com/lentago/shared-workflows/pull/50) — feat: add reusable Terraform lint workflow (tf-lint.yml)
- 🟢 2026-08-17 · [.github#118](https://github.com/lentago/.github/issues/118) — Incident register: tag entries deployment-caused y/n
- 🟣 2026-08-17 · [.github#150](https://github.com/lentago/.github/pull/150) — feat(incidents): add Deployment-caused marker for DORA metrics
- 🟢 2026-08-17 · [betula#105](https://github.com/lentago/betula/issues/105) — State the per-client destination rule (README + estate atlas)
- 🟢 2026-08-17 · [betula#104](https://github.com/lentago/betula/issues/104) — README: quantify the pipeline (events/day, GB/month, latency, retention)
- 🟣 2026-08-17 · [betula#110](https://github.com/lentago/betula/pull/110) — docs(readme): quantify pipeline scale and clarify per-client destination rule
- 🟣 2026-08-17 · [solidago#177](https://github.com/lentago/solidago/pull/177) — fix(iam): allow ecr:DescribeImages on the deploy role (attestation digest lookup)
- 🟣 2026-08-17 · [site-lentago-dev#58](https://github.com/lentago/site-lentago-dev/pull/58) — fix(deploy): bump site-deploy reusable to v1.1.1 (concurrency deadlock fix)
- 🟣 2026-08-17 · [shared-workflows#51](https://github.com/lentago/shared-workflows/pull/51) — fix(site-deploy): drop job-level concurrency — deadlocks callers holding their own group
- 🟣 2026-08-17 · [site-lentago-dev#56](https://github.com/lentago/site-lentago-dev/pull/56) — ci: adopt shared site-deploy reusable workflow (v1.1.0)
- 🟣 2026-08-17 · [shared-workflows#48](https://github.com/lentago/shared-workflows/pull/48) — chore(release): bump internal self-references to v1.1.0 ahead of tagging
- 🟣 2026-08-17 · [epigaea#519](https://github.com/lentago/epigaea/pull/519) — rename: update repo self-description to epigaea
- 🟣 2026-08-17 · [.github#149](https://github.com/lentago/.github/pull/149) — Weekly fleet reports refresh — 2026-08-17
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

---

## Code census

**The lens:** a `CLAUDE.md` (and its kin — `AGENTS.md`, skill `SKILL.md`, and the LLM prompt-programs that *are* a tool's logic) is an instruction set maintained for hygiene, so it's counted as **natural-language code**. Documentation, content/data, and community-health markdown are tallied separately and excluded from the code total, as are data payloads and generated files. This is a deliberate re-cut of the canonical [`metrics/language-census.md`](../metrics/language-census.md), which instead counts all Markdown/JSON/HTML as code.

### Languages

cloc *code* lines (blank + comment excluded). Shell folds Bourne + Bash. Instruction-markdown is promoted into the count (**bold**); the excluded buckets sit below the total.

| # | Language | Code | Files | Share |
|---|----------|-----:|------:|------:|
| 1 | JSON | 35,173 | 54 | 42.9% |
| 2 | YAML | 10,988 | 220 | 13.4% |
| 3 | Python | 9,488 | 70 | 11.6% |
| 4 | HCL | 7,080 | 116 | 8.6% |
| 5 | Shell (Bourne + Bash) | 5,499 | 71 | 6.7% |
| 6 | Text | 3,621 | 27 | 4.4% |
| 7 | **Instructions (CLAUDE.md family + prompt-programs)** | 2,358 | 20 | 2.9% |
| 8 | Astro | 2,280 | 27 | 2.8% |
| 9 | JavaScript | 1,875 | 17 | 2.3% |
| 10 | CSS | 1,402 | 10 | 1.7% |
| 11 | JSX | 1,023 | 12 | 1.2% |
| 12 | Jinja Template | 560 | 15 | 0.7% |
| 13 | TypeScript | 441 | 11 | 0.5% |
| 14 | TOML | 159 | 6 | 0.2% |
| 15 | Other (TOML / Dockerfile / …) | 69 | 5 | 0.1% |
| 16 | HTML | 57 | 1 | 0.1% |
| | **CODE TOTAL** | **82,073** | **682** | 100% |
| — | _Data / exports — excluded_ | 119,165 | 9 | — |
| — | _Generated (lockfiles, SVG, brand artefacts) — excluded_ | 36,886 | 96 | — |

### Instruction-markdown as code

- **Hygiene family** (20 files · `CLAUDE.md`, `AGENTS.md`, `SKILL.md`): **2,358 lines**
- **Prompt-programs** (0 files · reference-checker auditors): **0 lines**

#### Hygiene surface — each file is a maintenance obligation

| Repo | File | Lines |
|------|------|------:|
| epigaea | `CLAUDE.md` | 400 |
| shared-workflows | `CLAUDE.md` | 239 |
| site-pondviewlane-com | `CLAUDE.md` | 224 |
| .github | `CLAUDE.md` | 218 |
| betula | `CLAUDE.md` | 156 |
| kalmia | `CLAUDE.md` | 155 |
| site-lentago-dev | `CLAUDE.md` | 108 |
| solidago | `CLAUDE.md` | 99 |
| site-icecreamtofightwith-com | `CLAUDE.md` | 98 |
| drosera | `CLAUDE.md` | 96 |
| lupinus | `CLAUDE.md` | 68 |
| music-curator | `CLAUDE.md` | 68 |
| drosera | `AGENTS.md` | 67 |
| asclepias | `CLAUDE.md` | 62 |
| mitchella | `CLAUDE.md` | 62 |
| claytonia | `CLAUDE.md` | 57 |
| brasenia | `CLAUDE.md` | 56 |
| osmunda | `CLAUDE.md` | 53 |
| monarda | `CLAUDE.md` | 50 |
| repo-template | `CLAUDE.md` | 22 |
| **20 files** | | **2,358** |

### Per-repo

| Repo | Code | Instr | Doc-md | Content-md | Data |
|------|-----:|------:|-------:|-----------:|-----:|
| epigaea | 24,022 | 400 | 1,549 | 0 | 0 |
| drosera | 17,190 | 163 | 1,634 | 0 | 0 |
| site-pondviewlane-com | 7,435 | 224 | 2,913 | 0 | 0 |
| solidago | 6,471 | 99 | 2,527 | 0 | 0 |
| music-curator | 5,622 | 68 | 1,254 | 11,645 | 119,165 |
| kalmia | 3,530 | 155 | 1,448 | 0 | 0 |
| site-icecreamtofightwith-com | 3,491 | 98 | 897 | 6,004 | 0 |
| .github | 3,418 | 218 | 1,547 | 3,625 | 0 |
| claytonia | 2,507 | 57 | 1,547 | 0 | 0 |
| betula | 1,832 | 156 | 1,595 | 0 | 0 |
| site-lentago-dev | 1,802 | 108 | 624 | 0 | 0 |
| mitchella | 1,443 | 62 | 539 | 0 | 0 |
| shared-workflows | 1,170 | 239 | 769 | 0 | 0 |
| monarda | 960 | 50 | 525 | 0 | 0 |
| osmunda | 394 | 53 | 453 | 0 | 0 |
| brasenia | 307 | 56 | 1,609 | 0 | 0 |
| lupinus | 221 | 68 | 986 | 0 | 0 |
| asclepias | 170 | 62 | 617 | 0 | 0 |
| repo-template | 88 | 22 | 269 | 0 | 0 |

### Markdown taxonomy

The fleet carries **47,379 lines of Markdown across 1024 files**; only 5.0% is instruction-code.

| Class | Lines | Files | Disposition |
|-------|------:|------:|-------------|
| **Instructions** | 2,358 | 20 | **counted as code** |
| Content / data | 21,274 | 697 | payload (vault notes, recipes, test-sets) — excluded |
| Documentation | 23,302 | 291 | READMEs, docs, ADRs, runbooks — excluded |
| Community-health | 445 | 16 | CONTRIBUTING/SECURITY/templates — excluded |
| **All Markdown** | **47,379** | **1024** | |

---

## Method

- **Issues:** open issues via `gh search issues --owner lentago --state open`; activity from `gh search prs --owner lentago --merged` and closed issues filtered to the 30-day window. Public metadata only — no transcript harvest, ops items, or homelab detail (those live in the LAN copy).
- **Census tool:** `cloc`, run per-repo as `cloc --by-file --vcs=git` so only git-tracked files count (build output, `node_modules`, `.terraform`, venvs never enter). Lines are cloc *code* lines.
- **Scope:** the active repos owned by the `lentago` org, derived at runtime — personal repos and third-party clones are out of scope; archived repos are frozen and excluded.
- **Markdown classifier:** instruction-code = `CLAUDE.md`/`AGENTS.md`/`SKILL.md` or a versioned `prompts/*-auditor.md`; community-health = governance filenames + issue/PR templates; content = repo-scoped payload paths (music-curator `vault/`, ice-cream `recipes/`·manuscript, reference-checker `test-sets/`·`reports/`, dotgithub `fleet-reports/`); everything else = documentation.
- **Data / generated carve-outs:** exported payloads under the declared data dirs (music-curator `data/`, homeassistant-config `context/`) count as data whatever their serialisation — JSON, JSONL, CSV/TSV, XML, YAML — as does reference-checker's rendered `reports/*.html`; lockfiles, SVG and `.github/brand/generated/` (emitted from `brand/fleet.json`) are generated. drosera's `dashboards/*.json` stay in code as Terraform-enforced dashboards-as-code.
- **Regenerating:** `python3 metrics/generate-fleet-reports.py --out-dir .`

_Generated with Claude Code (Repo Claude)._
