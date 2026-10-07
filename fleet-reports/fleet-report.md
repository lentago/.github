# Lentago Labs Fleet Report

> [!NOTE]
> **Co-authored with [Claude](https://claude.ai)** (Repo Claude, the Lentago Labs fleet steward). Auto-generated weekly from the fleet's public state (GitHub issues/PRs + `cloc` over public repo contents) — no personal, security, or homelab-internal detail is included. A prettier, editorialised copy renders on the Lentago lab LAN.

**Generated:** 2026-10-05 19:56 UTC · Scope: the **27 active** `lentago` repos (archived repos frozen &amp; excluded) · Activity window: last 30 days (since 2026-09-05).

## Snapshot

| Open issues | PRs merged (30d) | Issues closed (30d) | Code (incl. instructions) | Instruction-markdown |
|---:|---:|---:|---:|---:|
| **95** | 228 | 73 | **125,040** | 2,455 (21 files) |

The fleet's hand-maintained natural-language instruction surface (**2,455 lines** across 21 files) is among the largest "languages" in the code base — `reference-checker` alone is almost entirely prompt-program source.

---

## Open issues — 95 across 18 repos

### .github — 19 open

| # | Title |
|---|-------|
| [225](https://github.com/lentago/.github/issues/225) | FLEET_ADMIN_TOKEN cannot resolve GitHub App node ids: merge-gate App allowances are unmanageable by Terraform |
| [201](https://github.com/lentago/.github/issues/201) | terraform: creating a repo from repos.json fails on GitHub's default labels (422 already_exists) |
| [200](https://github.com/lentago/.github/issues/200) | Offering: uvularia — client-owned records vault, grounded Ask, live compliance board (supersedes #128) |
| [196](https://github.com/lentago/.github/issues/196) | Offering: help-desk starter for a private repo — issue forms, labels, a board |
| [195](https://github.com/lentago/.github/issues/195) | Offering: sensor trip opens a work order — epigaea alert to GitHub Issue |
| [176](https://github.com/lentago/.github/issues/176) | Codify org settings in Terraform — default_repository_permission is live-only |
| [175](https://github.com/lentago/.github/issues/175) | A public repo entry with a null template_source cannot receive its first commit |
| [134](https://github.com/lentago/.github/issues/134) | Offerings pipeline — sovereignty track (2026-08 review) |
| [133](https://github.com/lentago/.github/issues/133) | Offering: Ops-in-a-Box — the miniature estate starter kit |
| [132](https://github.com/lentago/.github/issues/132) | Spike: volunteer-ops scheduling — evaluate, don't build (decision memo) |
| [131](https://github.com/lentago/.github/issues/131) | Offering: privacy posture kit for newly covered orgs |
| [130](https://github.com/lentago/.github/issues/130) | Offering: funder-report fact pipeline |
| [129](https://github.com/lentago/.github/issues/129) | Offering: cold-chain & facilities telemetry kit |
| [127](https://github.com/lentago/.github/issues/127) | Offering: AI-with-receipts — the reviewed-merge operating model as an adoption framework |
| [126](https://github.com/lentago/.github/issues/126) | Offering: Institutional Memory kit + private grounded Ask |
| [125](https://github.com/lentago/.github/issues/125) | Offering: Insurance-Receipts Pack — controls with evidence exhaust |
| [124](https://github.com/lentago/.github/issues/124) | Offering: Digital Custody audit — ownership insurance for the org's presence |
| [123](https://github.com/lentago/.github/issues/123) | Offering: Liberation Pipeline — SaaS-export collectors + restore drills |
| [122](https://github.com/lentago/.github/issues/122) | Offering: Good-Standing Kit — obligations-as-code + registry reconciliation (MA pack first) |

### drosera — 14 open

| # | Title |
|---|-------|
| [234](https://github.com/lentago/drosera/issues/234) | GitHub — Actions dashboard: fleet-wide run history, queue time, and failure trends (feed: betula#113) |
| [204](https://github.com/lentago/drosera/issues/204) | Main-branch workflow failures notify nobody — alert on red deploys/applies |
| [200](https://github.com/lentago/drosera/issues/200) | Queue SLO for the agent fleet (pickup latency) + burn alert |
| [199](https://github.com/lentago/drosera/issues/199) | Error-budget monthly section in the fleet report |
| [198](https://github.com/lentago/drosera/issues/198) | Threat Weather: anonymized daily network weather report |
| [197](https://github.com/lentago/drosera/issues/197) | "Are we open" single source of truth |
| [194](https://github.com/lentago/drosera/issues/194) | Adopt grafana-stack (LXC 105) guest capacity from kalmia |
| [169](https://github.com/lentago/drosera/issues/169) | Complete the homelab-observability → drosera rename through CI and hosts |
| [165](https://github.com/lentago/drosera/issues/165) | New-domain radar: alert when an IoT/smart-home device queries a never-before-seen domain (migrated from betula#11) |
| [151](https://github.com/lentago/drosera/issues/151) | device-inventory publisher: cron reinstall hook failed silently — root-cause and make the schedule survivable/verifiable |
| [131](https://github.com/lentago/drosera/issues/131) | Roadmap: multi-client telemetry pane — homelab and solidago (AWS) as peer sources |
| [103](https://github.com/lentago/drosera/issues/103) | Scrape node_exporter on the Firewalla via Alloy (bring the gateway into node dashboards) |
| [101](https://github.com/lentago/drosera/issues/101) | Heartbeat blind spot: tool-less reasoning turns show no activity while tokens burn |
| [93](https://github.com/lentago/drosera/issues/93) | feat(alloy): attach runid label to the transcript stream from the <sid>.runid sidecar |

### mitchella — 11 open

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
| [2](https://github.com/lentago/mitchella/issues/2) | Hold a conversation: thread context across turns |
| [1](https://github.com/lentago/mitchella/issues/1) | Exercise the real API path end to end |

### claytonia — 9 open

| # | Title |
|---|-------|
| [117](https://github.com/lentago/claytonia/issues/117) | Make never-merge a boundary: required check that blocks runner-App PRs without a human approval |
| [116](https://github.com/lentago/claytonia/issues/116) | Close the loop after the PR opens: a capped follow-up job for failing checks and review comments |
| [115](https://github.com/lentago/claytonia/issues/115) | An eval set for the fleet: replayable tasks, deterministic graders, and outcome measures |
| [99](https://github.com/lentago/claytonia/issues/99) | Second job type: batch document/report jobs through the queue contract |
| [65](https://github.com/lentago/claytonia/issues/65) | Complete the bullpen → claytonia rename on-host |
| [47](https://github.com/lentago/claytonia/issues/47) | Roadmap: platform-agnostic workers — Claude Code as one runtime behind the queue contract |
| [24](https://github.com/lentago/claytonia/issues/24) | Branch hygiene across overlapping sessions: clean-desk session-end + prefer fleet dispatch |
| [22](https://github.com/lentago/claytonia/issues/22) | Fleet PR lane separation: rebase-before-merge + dispatch-time overlap check (no two writers on one file/panel) |
| [21](https://github.com/lentago/claytonia/issues/21) | Queue admission control: job ownership, fleet occupancy, and capacity awareness at submit time |

### kalmia — 8 open

| # | Title |
|---|-------|
| [124](https://github.com/lentago/kalmia/issues/124) | Retire CT 113 (n8n LXC) after the osmunda burn-in window |
| [108](https://github.com/lentago/kalmia/issues/108) | Forge: golden images with receipts (checksums, SBOM, provenance) |
| [107](https://github.com/lentago/kalmia/issues/107) | Donated-hardware refresh profiles (new client class) |
| [99](https://github.com/lentago/kalmia/issues/99) | Cast client runtime for brasenia: watchdog sender, receiver hosting, then HLS-stack turn-down (brasenia ADR-0006) |
| [63](https://github.com/lentago/kalmia/issues/63) | Complete the lunaria → brasenia rename through runtime |
| [51](https://github.com/lentago/kalmia/issues/51) | Guarantee vzdump coverage for every Terraform-enforced guest (CT 113 had none) |
| [20](https://github.com/lentago/kalmia/issues/20) | Roadmap: provisioning clients beyond Ansible-on-workstations — VMs and containers as peer targets |
| [14](https://github.com/lentago/kalmia/issues/14) | Live-test the ubuntu_laptop profile on real ThinkPad hardware |

### solidago — 8 open

| # | Title |
|---|-------|
| [184](https://github.com/lentago/solidago/issues/184) | CI plans are never clean: standing task-definition replacements and a recreating SNS email subscription |
| [180](https://github.com/lentago/solidago/issues/180) | Hardening backlog from tf-lint's first trivy run (ECR immutability, CI-role least-privilege, SNS encryption) |
| [172](https://github.com/lentago/solidago/issues/172) | SNS alert email subscription is recreated on every apply — alerts may be reaching nobody |
| [167](https://github.com/lentago/solidago/issues/167) | DMARC posture on our own domains first (precondition for the Email Trust kit) |
| [156](https://github.com/lentago/solidago/issues/156) | Split plan/apply OIDC environments so the terraform environment can carry a branch policy |
| [149](https://github.com/lentago/solidago/issues/149) | Rotating a Lambda's Axiom token requires an unrelated apply to take effect |
| [144](https://github.com/lentago/solidago/issues/144) | Ask Lambda logs land in CloudWatch with no path to Axiom |
| [21](https://github.com/lentago/solidago/issues/21) | Evaluate migration from ElastiCache node-based to serverless |

### betula — 5 open

| # | Title |
|---|-------|
| [113](https://github.com/lentago/betula/issues/113) | GitHub Actions collector client: poll org run/job history into Grafana Cloud Loki |
| [107](https://github.com/lentago/betula/issues/107) | Device drift self-report: deployed conf hash vs main |
| [106](https://github.com/lentago/betula/issues/106) | Third AWS emitter: CloudTrail → archive + weekly access digest |
| [89](https://github.com/lentago/betula/issues/89) | Complete the firewalla-axiom-pipeline → betula rename on-device |
| [74](https://github.com/lentago/betula/issues/74) | Roadmap: core/client split — Firewalla and solidago (AWS) as peer collector clients |

### brasenia — 4 open

| # | Title |
|---|-------|
| [17](https://github.com/lentago/brasenia/issues/17) | Live-ingest pane: concept + ADR, acceptance spec, and VideoScene repoint to `live` with board fallback |
| [15](https://github.com/lentago/brasenia/issues/15) | Adopt the display guest (LXC 118) capacity from kalmia |
| [13](https://github.com/lentago/brasenia/issues/13) | Cast client: custom web receiver + current-pane pointer contract |
| [12](https://github.com/lentago/brasenia/issues/12) | Second functional path: Cast-native rendering, then deprecate and turn down the Roku/HLS chain |

### lupinus — 4 open

| # | Title |
|---|-------|
| [10](https://github.com/lentago/lupinus/issues/10) | One canonical product list; support/README.md is missing claytonia, epigaea, and brasenia |
| [9](https://github.com/lentago/lupinus/issues/9) | Reconcile the single-file ADOPTION.md template with the INTAKE/DRY-RUN split the exemplar uses |
| [8](https://github.com/lentago/lupinus/issues/8) | Kit rows carry no receipt: mark them provisional or demote until a drill is recorded |
| [4](https://github.com/lentago/lupinus/issues/4) | Epic: adoption guide — Phase 1 (launch set: solidago + monarda) |

### music-curator — 3 open

| # | Title |
|---|-------|
| [87](https://github.com/lentago/music-curator/issues/87) | follow-fold's bot merge cannot work under GITHUB_TOKEN — two blockers; decide App identity vs human merge |
| [45](https://github.com/lentago/music-curator/issues/45) | Web-verify the promoted person nodes' credit rows |
| [44](https://github.com/lentago/music-curator/issues/44) | Producer-class connectors: decide representation |

### site-lentago-dev — 2 open

| # | Title |
|---|-------|
| [86](https://github.com/lentago/site-lentago-dev/issues/86) | Remove committed .playwright-mcp/ scratch output and gitignore it |
| [67](https://github.com/lentago/site-lentago-dev/issues/67) | a11y gate ignores `color-contrast`: the Tidewater palette fails 4.5:1 at the design-token level |

### uvularia — 2 open

| # | Title |
|---|-------|
| [57](https://github.com/lentago/uvularia/issues/57) | Records need an event time, and deadlines a local timezone, for lead rules to match the statute for evening meetings |
| [28](https://github.com/lentago/uvularia/issues/28) | Sync templates/records and templates/site to their GitHub template repos on merge |

### epigaea — 1 open

| # | Title |
|---|-------|
| [518](https://github.com/lentago/epigaea/issues/518) | Complete the epigaea rename through runtime (tiers 3–4) |

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

### site-pondviewlane-com — 1 open

| # | Title |
|---|-------|
| [46](https://github.com/lentago/site-pondviewlane-com/issues/46) | Flip Content-Security-Policy from Report-Only to enforcing |

## Activity — last 30 days

**301 events**, one stream, newest first — 🟣 228 PRs merged · 🟢 73 issues closed

- 🟣 2026-10-04 · [.github#226](https://github.com/lentago/.github/pull/226) — merge gate: the template-sync App allowance is live-only until the fleet token can resolve App nodes
- 🟣 2026-10-04 · [.github#224](https://github.com/lentago/.github/pull/224) — merge gate: allow lentago-template-sync to arm auto-merge on the three uvularia template repos
- 🟣 2026-10-04 · [uvularia#77](https://github.com/lentago/uvularia/pull/77) — runbook: the fix for a refused auto-merge is the push allowlist, not a ruleset bypass
- 🟣 2026-10-04 · [uvularia#76](https://github.com/lentago/uvularia/pull/76) — template-sync: drift waits for sync on push; say plainly when auto-merge is refused
- 🟣 2026-10-04 · [uvularia-demo-records#18](https://github.com/lentago/uvularia-demo-records/pull/18) — Sync .nojekyll on the published branch from lentago/uvularia@d68c3c3 (#75)
- 🟣 2026-10-04 · [uvularia-records-template#11](https://github.com/lentago/uvularia-records-template/pull/11) — Sync from lentago/uvularia@d68c3c3
- 🟢 2026-10-04 · [uvularia#73](https://github.com/lentago/uvularia/issues/73) — Records template: add .nojekyll to the published branch so Pages serves the artifacts as-is
- 🟣 2026-10-04 · [uvularia#75](https://github.com/lentago/uvularia/pull/75) — records template: .nojekyll on the published branch so Pages serves it verbatim
- 🟣 2026-10-04 · [.github#223](https://github.com/lentago/.github/pull/223) — Weekly fleet reports refresh — 2026-10-04
- 🟣 2026-10-04 · [claytonia#132](https://github.com/lentago/claytonia/pull/132) — Link issue claim comments to the run-filtered fleet dashboard
- 🟢 2026-10-04 · [claytonia#130](https://github.com/lentago/claytonia/issues/130) — Resolve a job's target issue explicitly, not from the first #N in the prompt
- 🟣 2026-10-04 · [claytonia#131](https://github.com/lentago/claytonia/pull/131) — feat(run-job): resolve a job's target issue explicitly (#130)
- 🟢 2026-10-04 · [drosera#235](https://github.com/lentago/drosera/issues/235) — runid variable on the runner-fleet dashboard (for claytonia claim-comment links)
- 🟣 2026-10-04 · [drosera#236](https://github.com/lentago/drosera/pull/236) — feat(runner-fleet): runid template variable (#235)
- 🟢 2026-10-04 · [.github#221](https://github.com/lentago/.github/issues/221) — Require claytonia's queue-core bats check before merge
- 🟣 2026-10-04 · [.github#222](https://github.com/lentago/.github/pull/222) — Require claytonia's queue-core check before merge
- 🟢 2026-10-04 · [.github#192](https://github.com/lentago/.github/issues/192) — Epic: reposition every reader-facing surface to the pro-bono practice, one reader, one voice (ADR-0008)
- 🟣 2026-10-04 · [kalmia#135](https://github.com/lentago/kalmia/pull/135) — build(deps): bump aws-actions/configure-aws-credentials from 6.2.4 to 6.3.0 in the actions-routine group
- 🟣 2026-10-04 · [epigaea#522](https://github.com/lentago/epigaea/pull/522) — fix: point live repository_dispatch targets at epigaea
- 🟢 2026-10-04 · [claytonia#128](https://github.com/lentago/claytonia/issues/128) — Signal on the GitHub issue when a worker starts working it
- 🟣 2026-10-04 · [claytonia#129](https://github.com/lentago/claytonia/pull/129) — feat(run-job): claim comment on the issue, edited in place at completion
- 🟢 2026-10-04 · [solidago#188](https://github.com/lentago/solidago/issues/188) — Make the Axiom integration optional, as Grafana Cloud now is
- 🟣 2026-10-04 · [solidago#205](https://github.com/lentago/solidago/pull/205) — feat(axiom): make the Axiom integration optional (#188)
- 🟢 2026-10-04 · [claytonia#114](https://github.com/lentago/claytonia/issues/114) — Bound every job: default turn, spend and wall-clock limits in run-job
- 🟣 2026-10-04 · [claytonia#127](https://github.com/lentago/claytonia/pull/127) — feat(run-job): bound every job with turn, spend and wall-clock limits (#114)
- 🟢 2026-10-04 · [drosera#145](https://github.com/lentago/drosera/issues/145) — gitops loop can't recover a crashed Alloy — validator runs inside the down container
- 🟣 2026-10-04 · [drosera#230](https://github.com/lentago/drosera/pull/230) — fix(alloy-host): out-of-band config validation + liveness guard
- 🟢 2026-10-04 · [drosera#164](https://github.com/lentago/drosera/issues/164) — Bandwidth panels from Zeek conn.log bytes (migrated from betula#15)
- 🟣 2026-10-04 · [drosera#232](https://github.com/lentago/drosera/pull/232) — feat(traffic-devices): bandwidth over time — top devices (#164)
- 🟢 2026-10-04 · [drosera#176](https://github.com/lentago/drosera/issues/176) — Four live Loki streams have no ingest-absence rule, and the documented stream list is stale
- 🟣 2026-10-04 · [drosera#233](https://github.com/lentago/drosera/pull/233) — fix(alerts): firewalla_acl absence window 2h→30m + stream checklist (#176)
- 🟢 2026-10-04 · [solidago#169](https://github.com/lentago/solidago/issues/169) — Extend variable validation blocks beyond 1 of 24 modules
- 🟣 2026-10-04 · [solidago#204](https://github.com/lentago/solidago/pull/204) — feat(modules): validate vpc, ecs and rds inputs
- 🟢 2026-10-04 · [kalmia#53](https://github.com/lentago/kalmia/issues/53) — Pre-merge guard: verify a ForceNew guest change can actually be re-created under the apply identity
- 🟣 2026-10-04 · [kalmia#131](https://github.com/lentago/kalmia/pull/131) — ci(terraform): pre-merge guard against ForceNew guest replacement
- 🟢 2026-10-04 · [drosera#153](https://github.com/lentago/drosera/issues/153) — Terraform apply silently overwrites live dashboard edits — surface what an apply will revert
- 🟣 2026-10-04 · [drosera#231](https://github.com/lentago/drosera/pull/231) — ci(terraform): live-drift warning on PR plan and apply log
- 🟢 2026-10-04 · [kalmia#50](https://github.com/lentago/kalmia/issues/50) — Add prevent_destroy to import-only guests the token pipeline can't recreate (starting CT 113)
- 🟣 2026-10-04 · [kalmia#132](https://github.com/lentago/kalmia/pull/132) — feat(terraform): prevent_destroy on import-only guests (#50)
- 🟢 2026-10-04 · [music-curator#43](https://github.com/lentago/music-curator/issues/43) — Session-tie receipts: render the credits justifying each edge
- 🟣 2026-10-04 · [music-curator#90](https://github.com/lentago/music-curator/pull/90) — feat(driver): session-tie receipts (#43)
- 🟢 2026-10-04 · [solidago#190](https://github.com/lentago/solidago/issues/190) — docs/BOOTSTRAP.md still instructs operators to configure a nonexistent `foundry` AWS profile
- 🟣 2026-10-04 · [solidago#203](https://github.com/lentago/solidago/pull/203) — docs(BOOTSTRAP.md): remove nonexistent foundry AWS profile
- 🟢 2026-10-04 · [claytonia#110](https://github.com/lentago/claytonia/issues/110) — Ship workers/<host>.alive heartbeats to Loki — unblocks the bullpen liveness alerts
- 🟣 2026-10-04 · [claytonia#126](https://github.com/lentago/claytonia/pull/126) — feat(heartbeat): ship worker_alive liveness to Loki
- 🟢 2026-10-04 · [kalmia#85](https://github.com/lentago/kalmia/issues/85) — power: assert charge thresholds actually reached sysfs instead of trusting the drop-in
- 🟣 2026-10-04 · [kalmia#133](https://github.com/lentago/kalmia/pull/133) — feat(power): assert charge thresholds reached sysfs (#85)
- 🟢 2026-10-04 · [mitchella#3](https://github.com/lentago/mitchella/issues/3) — Slack hardening: visible failures, block limits, retries
- 🟣 2026-10-04 · [mitchella#17](https://github.com/lentago/mitchella/pull/17) — Slack hardening: visible failures, block limits, retries
- 🟢 2026-10-04 · [solidago#124](https://github.com/lentago/solidago/issues/124) — ECS task defs show a perpetual replace-diff (container_definitions normalization) — plan noise + apply-side-effect landmine
- 🟣 2026-10-04 · [solidago#202](https://github.com/lentago/solidago/pull/202) — fix(ecs): stop perpetual task-definition replacement (#124 option 1)
- 🟢 2026-10-04 · [kalmia#104](https://github.com/lentago/kalmia/issues/104) — Terraform: adopt backup-job `exclude` once bpg/proxmox ships it
- 🟣 2026-10-04 · [kalmia#134](https://github.com/lentago/kalmia/pull/134) — feat(terraform): adopt backup-job exclude and comment (bpg/proxmox 0.115.0)
- 🟣 2026-10-04 · [.github#220](https://github.com/lentago/.github/pull/220) — profile: uvularia's first rung is one repository; live board is the vault's own
- 🟣 2026-10-04 · [uvularia#74](https://github.com/lentago/uvularia/pull/74) — Adoption as a ladder: rung 1 is one repository; the drill, README and concept follow
- 🟣 2026-10-04 · [lupinus#13](https://github.com/lentago/lupinus/pull/13) — picker: uvularia's first rung is one repository
- 🟣 2026-10-04 · [uvularia-demo-records#17](https://github.com/lentago/uvularia-demo-records/pull/17) — Sync the public board page from lentago/uvularia@59a8060 (#72)
- 🟣 2026-10-04 · [uvularia-records-template#10](https://github.com/lentago/uvularia-records-template/pull/10) — Sync from lentago/uvularia@59a8060 (#72)
- 🟢 2026-10-04 · [uvularia#70](https://github.com/lentago/uvularia/issues/70) — Records template: publish a plain public board page so the vault is useful as one repository
- 🟣 2026-10-04 · [uvularia#72](https://github.com/lentago/uvularia/pull/72) — Records template: publish a plain public board page so the vault is useful as one repository
- 🟣 2026-10-04 · [uvularia#71](https://github.com/lentago/uvularia/pull/71) — ADR-0002: adoption is a ladder, and the first rung is one repository
- 🟣 2026-10-04 · [.github#219](https://github.com/lentago/.github/pull/219) — ADR-0009: amendment, adoption is a ladder and the first rung is one repository
- 🟢 2026-10-04 · [betula#86](https://github.com/lentago/betula/issues/86) — Firewalla boot race: Fluent Bit starts before Zeek's spool is live and tails dead paths silently; healthcheck's error-based detection cannot see it
- 🟣 2026-10-04 · [betula#112](https://github.com/lentago/betula/pull/112) — fix(firewalla): Fluent Bit boot race — wait for Zeek + delivery liveness check
- 🟢 2026-10-04 · [claytonia#120](https://github.com/lentago/claytonia/issues/120) — Residual journal chatter: two condition-skipped units re-logged on every timer activation
- 🟣 2026-10-04 · [claytonia#125](https://github.com/lentago/claytonia/pull/125) — Mask first-boot units to stop per-activation journal chatter (#120)
- 🟢 2026-10-04 · [.github#187](https://github.com/lentago/.github/issues/187) — [renewal] pondviewlane.com — domain registration — due 2026-11-03
- 🟢 2026-10-04 · [.github#182](https://github.com/lentago/.github/issues/182) — [renewal] lentago.dev — TLS certificate (ACME auto-renew backstop) — due 2026-09-10
- 🟣 2026-10-04 · [.github#218](https://github.com/lentago/.github/pull/218) — fix(lock-in): align renewals.yml with live cert and registration state
- 🟢 2026-10-04 · [solidago#168](https://github.com/lentago/solidago/issues/168) — Ask the Estate: grounded-Ask demo over fleet docs
- 🟢 2026-10-04 · [kalmia#15](https://github.com/lentago/kalmia/issues/15) — Live-test the crostini profile on the Chromebook penguin container
- 🟢 2026-10-04 · [drosera#157](https://github.com/lentago/drosera/issues/157) — Sites scoreboard row for the office display kiosk
- 🟢 2026-10-04 · [claytonia#31](https://github.com/lentago/claytonia/issues/31) — Add optional authentication to the n8n Bullpen job-submit form
- 🟢 2026-10-04 · [.github#167](https://github.com/lentago/.github/issues/167) — Fleet reports - one-off run
- 🟣 2026-10-04 · [.github#217](https://github.com/lentago/.github/pull/217) — uvularia: require the drift context
- 🟣 2026-10-04 · [uvularia-demo-records#16](https://github.com/lentago/uvularia-demo-records/pull/16) — Sync the intake outcome fix from lentago/uvularia@d2f71c1 (#68)
- 🟣 2026-10-04 · [uvularia-records-template#9](https://github.com/lentago/uvularia-records-template/pull/9) — Sync from lentago/uvularia@d2f71c1 (#68)
- 🟣 2026-10-04 · [uvularia#69](https://github.com/lentago/uvularia/pull/69) — Template sync: drift check on every PR, automatic sync behind a GitHub App, and the guide to create it
- 🟢 2026-10-04 · [drosera#221](https://github.com/lentago/drosera/issues/221) — Non-converging plan: two rule groups and the Axiom plugin are re-applied on every run
- 🟣 2026-10-04 · [drosera#229](https://github.com/lentago/drosera/pull/229) — Non-converging plan: two rule groups and the Axiom plugin are re-applied on every run
- 🟢 2026-10-04 · [uvularia#63](https://github.com/lentago/uvularia/issues/63) — intake event reports outcome=failed when the PR is deliberately left for a person
- 🟣 2026-10-04 · [uvularia#68](https://github.com/lentago/uvularia/pull/68) — intake event reports outcome=failed when the PR is deliberately left for a person
- 🟣 2026-10-04 · [site-pondviewlane-com#81](https://github.com/lentago/site-pondviewlane-com/pull/81) — Bump the astro-stack group across 1 directory with 2 updates
- 🟣 2026-10-04 · [site-pondviewlane-com#82](https://github.com/lentago/site-pondviewlane-com/pull/82) — Bump sharp from 0.35.4 to 0.35.5 in the npm-routine group
- 🟢 2026-10-04 · [drosera#227](https://github.com/lentago/drosera/issues/227) — Uvularia pane: stat panels fed by Loki instant queries cannot show the digest, rules tag or question kind
- 🟣 2026-10-04 · [drosera#228](https://github.com/lentago/drosera/pull/228) — Uvularia pane: stat panels fed by Loki instant queries cannot show the digest, rules tag or question kind
- 🟣 2026-10-04 · [uvularia-demo-ask-rules#13](https://github.com/lentago/uvularia-demo-ask-rules/pull/13) — Sync asked.subject matching from lentago/uvularia@42a1b2c (#67)
- 🟢 2026-10-04 · [uvularia#66](https://github.com/lentago/uvularia/issues/66) — asked.subject: match a subject's singular as well as its listed plural
- 🟣 2026-10-04 · [uvularia#67](https://github.com/lentago/uvularia/pull/67) — asked.subject: match a subject's singular as well as its listed plural
- 🟢 2026-10-04 · [drosera#225](https://github.com/lentago/drosera/issues/225) — Uvularia pane: Intake, Reviewed, Served and Asked stat panels show "Value #A…" and hide the digest, rules tag and question kinds
- 🟣 2026-10-04 · [drosera#226](https://github.com/lentago/drosera/pull/226) — Uvularia pane: Intake, Reviewed, Served and Asked stat panels show "Value #A…" and hide the digest, rules tag and question kinds
- 🟣 2026-10-04 · [uvularia-rules-template#7](https://github.com/lentago/uvularia-rules-template/pull/7) — Sync from lentago/uvularia@bed8e64 (#65)
- 🟣 2026-10-04 · [uvularia-demo-ask-rules#12](https://github.com/lentago/uvularia-demo-ask-rules/pull/12) — Sync deploy-ask from lentago/uvularia@bed8e64 (#65)
- 🟣 2026-10-04 · [uvularia#65](https://github.com/lentago/uvularia/pull/65) — deploy-ask and the function tests work in a rules repo with or without a vendored ask-function
- 🟣 2026-10-04 · [uvularia-demo-ask-rules#11](https://github.com/lentago/uvularia-demo-ask-rules/pull/11) — ask-function tests: find policy.yaml beside the vendored function
- 🟣 2026-10-04 · [uvularia-demo-records#15](https://github.com/lentago/uvularia-demo-records/pull/15) — README: bring current with the template
- 🟣 2026-10-04 · [uvularia-records-template#8](https://github.com/lentago/uvularia-records-template/pull/8) — Sync from lentago/uvularia@a249ebb (#64)
- 🟣 2026-10-04 · [uvularia-demo-ask-rules#10](https://github.com/lentago/uvularia-demo-ask-rules/pull/10) — Sync the telemetry producers from lentago/uvularia@a249ebb (#64)
- 🟣 2026-10-04 · [uvularia-rules-template#6](https://github.com/lentago/uvularia-rules-template/pull/6) — Sync from lentago/uvularia@a249ebb (#64)
- 🟣 2026-10-04 · [uvularia-demo-records#14](https://github.com/lentago/uvularia-demo-records/pull/14) — Sync the telemetry producers from lentago/uvularia@a249ebb (#64)
- 🟢 2026-10-04 · [uvularia#59](https://github.com/lentago/uvularia/issues/59) — Telemetry: emit the fields drosera's pipeline pane reads (at, intake/reviewed snapshots, served heartbeat, asked.subject)
- 🟣 2026-10-04 · [uvularia#64](https://github.com/lentago/uvularia/pull/64) — Telemetry: emit the fields drosera's pipeline pane reads (at, intake/reviewed snapshots, served heartbeat, asked.subject)
- 🟢 2026-10-04 · [drosera#223](https://github.com/lentago/drosera/issues/223) — Uvularia pane: Published stat panel shows "Value #B…#E" instead of green / amber / red / no data
- 🟣 2026-10-04 · [drosera#224](https://github.com/lentago/drosera/pull/224) — Uvularia Records pipeline: name the Published stat series
- 🟢 2026-10-04 · [uvularia-demo-records#12](https://github.com/lentago/uvularia-demo-records/issues/12) — Add a record: Annual Form PC filing (2026)
- 🟢 2026-10-04 · [uvularia-demo-records#11](https://github.com/lentago/uvularia-demo-records/issues/11) — Obligation ma-ag-charity-annual-filing is amber: due soon
- 🟣 2026-10-04 · [uvularia-demo-records#13](https://github.com/lentago/uvularia-demo-records/pull/13) — Intake for #12: Annual Form PC filing (2026)
- 🟣 2026-10-04 · [uvularia#62](https://github.com/lentago/uvularia/pull/62) — deploy-ask: run apply on a manual dispatch from main
- 🟣 2026-10-04 · [uvularia-demo-ask-rules#9](https://github.com/lentago/uvularia-demo-ask-rules/pull/9) — deploy-ask: run apply on a manual dispatch from main
- 🟣 2026-10-04 · [uvularia-demo-ask-rules#8](https://github.com/lentago/uvularia-demo-ask-rules/pull/8) — deploy-ask: manual trigger (sync from lentago/uvularia@cae0e43)
- 🟣 2026-10-04 · [uvularia-rules-template#5](https://github.com/lentago/uvularia-rules-template/pull/5) — Sync from lentago/uvularia@cae0e43
- 🟣 2026-10-04 · [drosera#222](https://github.com/lentago/drosera/pull/222) — uvularia-pipeline: each alert names its dashboard panel
- 🟣 2026-10-04 · [uvularia#61](https://github.com/lentago/uvularia/pull/61) — deploy-ask: allow a manual run so a changed variable can be applied
- 🟣 2026-10-04 · [uvularia-records-template#7](https://github.com/lentago/uvularia-records-template/pull/7) — Sync from lentago/uvularia@4330fa5
- 🟣 2026-10-04 · [uvularia-demo-ask-rules#7](https://github.com/lentago/uvularia-demo-ask-rules/pull/7) — Sync ask-function from lentago/uvularia@4330fa5 (GET /health)
- 🟣 2026-10-04 · [uvularia-demo-records#10](https://github.com/lentago/uvularia-demo-records/pull/10) — Sync the watch workflow from lentago/uvularia@4330fa5
- 🟢 2026-10-04 · [uvularia#53](https://github.com/lentago/uvularia/issues/53) — Phase 2 · alerts open GitHub Issues: stale served digest, obligation gone amber, cap at 80 %
- 🟣 2026-10-04 · [uvularia#60](https://github.com/lentago/uvularia/pull/60) — Phase 2 · alerts open GitHub Issues: stale served digest, obligation gone amber, cap at 80 %
- 🟢 2026-10-04 · [drosera#218](https://github.com/lentago/drosera/issues/218) — uvularia pipeline pane: the left-to-right dashboard and its alert rules, provisioned for a client's own Grafana Cloud stack
- 🟣 2026-10-04 · [drosera#220](https://github.com/lentago/drosera/pull/220) — feat(uvularia): records pipeline pane — dashboard, alert rules, client export (#218)
- 🟣 2026-10-04 · [.github#215](https://github.com/lentago/.github/pull/215) — uvularia: require the template-telemetry context
- 🟣 2026-10-04 · [uvularia-rules-template#4](https://github.com/lentago/uvularia-rules-template/pull/4) — Sync from lentago/uvularia@ce2a962
- 🟣 2026-10-04 · [uvularia-demo-ask-rules#6](https://github.com/lentago/uvularia-demo-ask-rules/pull/6) — Sync from lentago/uvularia@ce2a962 (stage telemetry, no-op until configured)
- 🟣 2026-10-04 · [uvularia-demo-records#9](https://github.com/lentago/uvularia-demo-records/pull/9) — Sync from lentago/uvularia@ce2a962 (stage telemetry, no-op until configured)
- 🟣 2026-10-04 · [uvularia-records-template#6](https://github.com/lentago/uvularia-records-template/pull/6) — Sync from lentago/uvularia@ce2a962
- 🟢 2026-10-04 · [uvularia#52](https://github.com/lentago/uvularia/issues/52) — Phase 2 · emit one event per pipeline stage to the client's Grafana Cloud Loki
- 🟣 2026-10-04 · [uvularia#58](https://github.com/lentago/uvularia/pull/58) — Phase 2 · emit one event per pipeline stage to the client's Grafana Cloud Loki
- 🟣 2026-10-04 · [uvularia-demo-site#5](https://github.com/lentago/uvularia-demo-site/pull/5) — Sync the site template (values-only config over the template-owned schema)
- 🟣 2026-10-04 · [uvularia-site-template#5](https://github.com/lentago/uvularia-site-template/pull/5) — Sync from lentago/uvularia@689a9f4
- 🟣 2026-10-04 · [uvularia-demo-records#8](https://github.com/lentago/uvularia-demo-records/pull/8) — Re-sync core and the meeting-notice rule (OML weekday/holiday window)
- 🟣 2026-10-04 · [uvularia-records-template#5](https://github.com/lentago/uvularia-records-template/pull/5) — Sync from lentago/uvularia@689a9f4
- 🟢 2026-10-04 · [drosera#217](https://github.com/lentago/drosera/issues/217) — Actions → Loki: a reusable push step so a GitHub workflow can emit one structured event to Grafana Cloud
- 🟣 2026-10-04 · [drosera#219](https://github.com/lentago/drosera/pull/219) — feat(clients): loki-event action + loki_push.py — Actions/serverless → Loki
- 🟢 2026-10-04 · [uvularia#13](https://github.com/lentago/uvularia/issues/13) — Schema: extend obligation lead type with calendar-day exclusion for OML 48-hour rule
- 🟣 2026-10-04 · [uvularia#56](https://github.com/lentago/uvularia/pull/56) — Schema: extend obligation lead type with calendar-day exclusion for OML 48-hour rule
- 🟢 2026-10-04 · [uvularia#51](https://github.com/lentago/uvularia/issues/51) — templates/site: keep the SiteConfig interface out of the client-edited file
- 🟣 2026-10-04 · [uvularia#55](https://github.com/lentago/uvularia/pull/55) — templates/site: keep the SiteConfig interface out of the client-edited file
- 🟢 2026-10-04 · [uvularia#41](https://github.com/lentago/uvularia/issues/41) — Version skew: a newer site must tolerate an older standing.json (history was made required)
- 🟣 2026-10-04 · [uvularia#54](https://github.com/lentago/uvularia/pull/54) — Version skew: a newer site must tolerate an older standing.json (history was made required)
- 🟣 2026-10-04 · [uvularia-demo-site#4](https://github.com/lentago/uvularia-demo-site/pull/4) — Turn on the Ask box: point it at the demonstration function
- 🟣 2026-10-04 · [uvularia-site-template#4](https://github.com/lentago/uvularia-site-template/pull/4) — Sync from lentago/uvularia@5007bd0
- 🟣 2026-10-04 · [uvularia#50](https://github.com/lentago/uvularia/pull/50) — site tests: do not assert the template's own defaults; derive the base path from the config
- 🟣 2026-10-04 · [.github#214](https://github.com/lentago/.github/pull/214) — coderabbit: require the schema-validation context
- 🟣 2026-10-04 · [coderabbit#1](https://github.com/lentago/coderabbit/pull/1) — The fleet's central CodeRabbit configuration, with a schema check
- 🟣 2026-10-04 · [uvularia-site-template#3](https://github.com/lentago/uvularia-site-template/pull/3) — Sync from lentago/uvularia@6999ecf
- 🟢 2026-10-04 · [uvularia#35](https://github.com/lentago/uvularia/issues/35) — Phase 1 · templates/site: the Ask widget with verified citations
- 🟣 2026-10-04 · [uvularia#49](https://github.com/lentago/uvularia/pull/49) — Phase 1 · templates/site: the Ask widget with verified citations
- 🟣 2026-10-04 · [.github#213](https://github.com/lentago/.github/pull/213) — Create lentago/coderabbit: the fleet's central CodeRabbit configuration repo
- 🟣 2026-10-04 · [uvularia-demo-records#7](https://github.com/lentago/uvularia-demo-records/pull/7) — Correct the weekday on the October 17 meeting notice
- 🟣 2026-10-04 · [uvularia-demo-ask-rules#5](https://github.com/lentago/uvularia-demo-ask-rules/pull/5) — Turn the demonstration Ask box on
- 🟣 2026-10-04 · [uvularia-demo-ask-rules#4](https://github.com/lentago/uvularia-demo-ask-rules/pull/4) — Sync ask-function from lentago/uvularia (lazy key read)
- 🟣 2026-10-04 · [uvularia#48](https://github.com/lentago/uvularia/pull/48) — ask-function: read the API key lazily; an unreadable key is a 503 maintenance reply, never a crash
- 🟣 2026-10-04 · [uvularia-demo-ask-rules#3](https://github.com/lentago/uvularia-demo-ask-rules/pull/3) — Sync deploy-ask and ask-function from lentago/uvularia (build the package every run)
- 🟣 2026-10-04 · [uvularia-rules-template#3](https://github.com/lentago/uvularia-rules-template/pull/3) — Sync from lentago/uvularia@04dfe0c
- 🟣 2026-10-04 · [uvularia#47](https://github.com/lentago/uvularia/pull/47) — deploy-ask: build the function package on every run, before plan and apply
- 🟣 2026-10-04 · [solidago#201](https://github.com/lentago/solidago/pull/201) — uvularia-demo-sandbox: match the bare log-group ARN as well as its streams
- 🟣 2026-10-04 · [uvularia-demo-ask-rules#2](https://github.com/lentago/uvularia-demo-ask-rules/pull/2) — Sync ask-function from lentago/uvularia (parameters by ARN, no plan-time read)
- 🟣 2026-10-04 · [uvularia#46](https://github.com/lentago/uvularia/pull/46) — ask-function: reference the SSM parameters by ARN; never read them at plan time
- 🟣 2026-10-04 · [solidago#200](https://github.com/lentago/solidago/pull/200) — uvularia-demo-sandbox: let the function decrypt its SSM parameters (kms:Decrypt via SSM only)
- 🟣 2026-10-04 · [solidago#199](https://github.com/lentago/solidago/pull/199) — uvularia-demo-sandbox: trust the immutable OIDC subject the demo rules repo presents
- 🟣 2026-10-04 · [solidago#198](https://github.com/lentago/solidago/pull/198) — uvularia-demo-sandbox: the fence protects itself; ListBucket for the state prefix
- 🟣 2026-10-04 · [solidago#197](https://github.com/lentago/solidago/pull/197) — uvularia-demo-sandbox: trust the immutable OIDC subject the demo rules repo actually presents
- 🟣 2026-10-03 · [uvularia-demo-ask-rules#1](https://github.com/lentago/uvularia-demo-ask-rules/pull/1) — Configure the demonstration Ask box
- 🟣 2026-10-03 · [.github#212](https://github.com/lentago/.github/pull/212) — Create uvularia-demo-ask-rules from uvularia-rules-template
- 🟣 2026-10-03 · [uvularia-rules-template#2](https://github.com/lentago/uvularia-rules-template/pull/2) — Sync from lentago/uvularia@9fdceeb
- 🟣 2026-10-03 · [.github#211](https://github.com/lentago/.github/pull/211) — uvularia: require the test-ask-function context
- 🟢 2026-10-03 · [solidago#195](https://github.com/lentago/solidago/issues/195) — uvularia demo sandbox: an isolated OIDC role, permissions boundary, and state key for the demonstration Ask function
- 🟣 2026-10-03 · [solidago#196](https://github.com/lentago/solidago/pull/196) — feat(uvularia-demo-sandbox): fence the demo Ask function in-account (#195)
- 🟢 2026-10-03 · [uvularia#34](https://github.com/lentago/uvularia/issues/34) — Phase 1 · Ask function: mitchella as a serverless runtime in the client's account
- 🟣 2026-10-03 · [uvularia#45](https://github.com/lentago/uvularia/pull/45) — Phase 1 · Ask function: mitchella as a hardened serverless runtime in the client's account (#34)
- 🟣 2026-10-03 · [uvularia-rules-template#1](https://github.com/lentago/uvularia-rules-template/pull/1) — Replace the scaffold with templates/ask-rules from lentago/uvularia
- 🟣 2026-10-03 · [drosera#216](https://github.com/lentago/drosera/pull/216) — fix(claytonia-dashboard): stream-of-consciousness panes oldest-first
- 🟣 2026-10-03 · [.github#210](https://github.com/lentago/.github/pull/210) — uvularia-rules-template: description within GitHub's 350-char limit for template creates
- 🟣 2026-10-03 · [claytonia#124](https://github.com/lentago/claytonia/pull/124) — cr-update: weekly, idle-guarded Claude Code update for the runners
- 🟣 2026-10-03 · [.github#209](https://github.com/lentago/.github/pull/209) — Create uvularia-rules-template (born from repo-template so main exists)
- 🟣 2026-10-03 · [uvularia#44](https://github.com/lentago/uvularia/pull/44) — ask-rules: a fresh repo with no published corpus is a notice, not a red check
- 🟣 2026-10-03 · [uvularia-demo-records#6](https://github.com/lentago/uvularia-demo-records/pull/6) — Re-sync core and the publish workflow (receipt names carry the publish instant)
- 🟣 2026-10-03 · [uvularia-demo-site#3](https://github.com/lentago/uvularia-demo-site/pull/3) — Sync the site template (receipt lookup follows the instant-stamped name)
- 🟣 2026-10-03 · [uvularia-site-template#2](https://github.com/lentago/uvularia-site-template/pull/2) — Sync from lentago/uvularia@37d33e5
- 🟣 2026-10-03 · [uvularia-records-template#4](https://github.com/lentago/uvularia-records-template/pull/4) — Sync from lentago/uvularia@37d33e5
- 🟢 2026-10-03 · [uvularia#42](https://github.com/lentago/uvularia/issues/42) — Publish overwrites a receipt when the corpus digest is unchanged, losing record provenance
- 🟣 2026-10-03 · [uvularia#43](https://github.com/lentago/uvularia/pull/43) — Receipts are named by publish instant, never overwritten
- 🟣 2026-10-03 · [uvularia-records-template#3](https://github.com/lentago/uvularia-records-template/pull/3) — Sync from lentago/uvularia@1915546
- 🟣 2026-10-03 · [uvularia-demo-site#2](https://github.com/lentago/uvularia-demo-site/pull/2) — Sync the site template from lentago/uvularia (board track record)
- 🟣 2026-10-03 · [uvularia-demo-records#5](https://github.com/lentago/uvularia-demo-records/pull/5) — Re-sync core from lentago/uvularia (board history)
- 🟣 2026-10-03 · [uvularia-site-template#1](https://github.com/lentago/uvularia-site-template/pull/1) — Sync from lentago/uvularia@1915546
- 🟢 2026-10-03 · [uvularia#36](https://github.com/lentago/uvularia/issues/36) — Phase 1 · board history: show lateness over time, not only the current standing
- 🟣 2026-10-03 · [uvularia#40](https://github.com/lentago/uvularia/pull/40) — Phase 1 · board history: show lateness over time, not only the current standing
- 🟣 2026-10-03 · [uvularia-records-template#1](https://github.com/lentago/uvularia-records-template/pull/1) — Sync from lentago/uvularia@c80a42e
- 🟢 2026-10-03 · [uvularia#31](https://github.com/lentago/uvularia/issues/31) — Intake door depends on an add-record label the template never creates
- 🟢 2026-10-03 · [uvularia#30](https://github.com/lentago/uvularia/issues/30) — Intake workflow cannot open its PR where Actions may not create pull requests (GitHub's default)
- 🟣 2026-10-03 · [uvularia#39](https://github.com/lentago/uvularia/pull/39) — Intake door: drop the label gate, detect the form by its headings, handle the PR-create 403
- 🟢 2026-10-03 · [uvularia#29](https://github.com/lentago/uvularia/issues/29) — validate.py: fail on duplicate obligation ids
- 🟣 2026-10-03 · [uvularia#38](https://github.com/lentago/uvularia/pull/38) — validate.py: fail on duplicate obligation ids
- 🟣 2026-10-03 · [.github#208](https://github.com/lentago/.github/pull/208) — uvularia: require the test-rules context
- 🟢 2026-10-03 · [mitchella#15](https://github.com/lentago/mitchella/issues/15) — uvularia Phase 1: bundle corpus source, StandingProvider, AnnouncementProvider
- 🟣 2026-10-03 · [mitchella#16](https://github.com/lentago/mitchella/pull/16) — uvularia Phase 1: bundle corpus source, StandingProvider, AnnouncementProvider
- 🟢 2026-10-03 · [uvularia#33](https://github.com/lentago/uvularia/issues/33) — Phase 1 · templates/ask-rules: the governance template and its eval gate
- 🟣 2026-10-03 · [uvularia#37](https://github.com/lentago/uvularia/pull/37) — Phase 1 · templates/ask-rules: the governance template and its eval gate
- 🟢 2026-10-03 · [uvularia#11](https://github.com/lentago/uvularia/issues/11) — Phase 0 · lupinus picker row and lentago.dev receipt
- 🟣 2026-10-03 · [.github#207](https://github.com/lentago/.github/pull/207) — Org profile: the public-record offering is live, with uvularia and its demo board
- 🟣 2026-10-03 · [site-lentago-dev#87](https://github.com/lentago/site-lentago-dev/pull/87) — Public-record offering is live: uvularia Phase 0 ran its first dry-run
- 🟣 2026-10-03 · [uvularia#32](https://github.com/lentago/uvularia/pull/32) — First dry-run receipt; point the adoption path at the template repos; document the intake-door traps
- 🟣 2026-10-03 · [lupinus#12](https://github.com/lentago/lupinus/pull/12) — Picker: add the uvularia records-vault row (Kit, with receipt)
- 🟢 2026-10-03 · [uvularia-demo-records#3](https://github.com/lentago/uvularia-demo-records/issues/3) — Add a record: Notice of board meeting, 2026-10-17
- 🟣 2026-10-03 · [uvularia-demo-records#4](https://github.com/lentago/uvularia-demo-records/pull/4) — Intake for #3: Notice of regular board meeting, October 17, 2026
- 🟣 2026-10-03 · [uvularia-demo-records#2](https://github.com/lentago/uvularia-demo-records/pull/2) — Drop the template's example obligation (step 4, missed)
- 🟣 2026-10-03 · [uvularia-demo-site#1](https://github.com/lentago/uvularia-demo-site/pull/1) — Point the site at the demonstration vault
- 🟣 2026-10-03 · [uvularia-demo-records#1](https://github.com/lentago/uvularia-demo-records/pull/1) — Seed the demonstration vault
- 🟣 2026-10-03 · [.github#206](https://github.com/lentago/.github/pull/206) — Create uvularia-demo-records and uvularia-demo-site from the uvularia templates
- 🟣 2026-10-03 · [.github#205](https://github.com/lentago/.github/pull/205) — Create uvularia-records-template and uvularia-site-template as GitHub template repos
- 🟣 2026-10-03 · [site-lentago-dev#85](https://github.com/lentago/site-lentago-dev/pull/85) — Fix the zeugma in the migration card copy
- 🟣 2026-10-03 · [uvularia#27](https://github.com/lentago/uvularia/pull/27) — Bump the actions-major group with 3 updates
- 🟣 2026-10-03 · [uvularia#25](https://github.com/lentago/uvularia/pull/25) — site template: upgrade Astro to clear Dependabot alerts; add npm Dependabot
- 🟢 2026-10-03 · [uvularia#10](https://github.com/lentago/uvularia/issues/10) — Phase 0 · ADOPTION.md, timed dry-run, and the first receipt
- 🟣 2026-10-03 · [uvularia#24](https://github.com/lentago/uvularia/pull/24) — Phase 0 · adoption docs: ADOPTION.md, timed dry-run, and the first receipt
- 🟣 2026-10-03 · [.github#204](https://github.com/lentago/.github/pull/204) — uvularia: require the test-site context
- 🟢 2026-10-03 · [uvularia#8](https://github.com/lentago/uvularia/issues/8) — Phase 0 · templates/site: the public "Is it posted?" board
- 🟣 2026-10-03 · [uvularia#23](https://github.com/lentago/uvularia/pull/23) — Phase 0 · templates/site: the `<org>-site` repository template
- 🟣 2026-10-03 · [.github#203](https://github.com/lentago/.github/pull/203) — uvularia: require the test-intake context
- 🟢 2026-10-03 · [uvularia#7](https://github.com/lentago/uvularia/issues/7) — Phase 0 · intake door: GitHub Issue form → scaffolded PR
- 🟣 2026-10-03 · [uvularia#22](https://github.com/lentago/uvularia/pull/22) — Phase 0 · intake door: Issue form → scaffolded PR
- 🟣 2026-10-03 · [.github#202](https://github.com/lentago/.github/pull/202) — uvularia: require its four CI contexts on main
- 🟣 2026-10-03 · [uvularia#21](https://github.com/lentago/uvularia/pull/21) — Fix the name-leak self-test for the slug needle; sync the vendored example
- 🟢 2026-10-03 · [uvularia#9](https://github.com/lentago/uvularia/issues/9) — Phase 0 · demo: org.yaml + seed.py + Stillwater Brook records (ADR-0001)
- 🟣 2026-10-03 · [uvularia#20](https://github.com/lentago/uvularia/pull/20) — Phase 0 · demo: org.yaml + seed.py + Stillwater Brook records (ADR-0001)
- 🟢 2026-10-03 · [uvularia#6](https://github.com/lentago/uvularia/issues/6) — Phase 0 · templates/records: the vault template
- 🟣 2026-10-03 · [uvularia#19](https://github.com/lentago/uvularia/pull/19) — Phase 0 · templates/records: the vault template (#6)
- 🟢 2026-10-03 · [uvularia#17](https://github.com/lentago/uvularia/issues/17) — Wire the Massachusetts pack fixtures into the evaluator test suite
- 🟣 2026-10-03 · [uvularia#18](https://github.com/lentago/uvularia/pull/18) — Wire the Massachusetts pack fixtures into the evaluator test suite
- 🟢 2026-10-03 · [uvularia#4](https://github.com/lentago/uvularia/issues/4) — Phase 0 · core: evaluate.py — obligations → standing.json
- 🟣 2026-10-03 · [uvularia#16](https://github.com/lentago/uvularia/pull/16) — Phase 0 · core: evaluate.py — obligations → standing.json
- 🟢 2026-10-03 · [uvularia#3](https://github.com/lentago/uvularia/issues/3) — Phase 0 · core: validate.py (schema, links, privacy tripwires, no-delete, visibility)
- 🟣 2026-10-03 · [uvularia#15](https://github.com/lentago/uvularia/pull/15) — Phase 0 · core: validate.py (schema, links, privacy tripwires, no-delete, visibility)
- 🟢 2026-10-03 · [uvularia#5](https://github.com/lentago/uvularia/issues/5) — Phase 0 · obligations pack: Massachusetts (Open Meeting Law, charities filing, condo statute)
- 🟣 2026-10-03 · [uvularia#14](https://github.com/lentago/uvularia/pull/14) — Phase 0 · obligations pack: Massachusetts (Open Meeting Law, charities filing, condo statute)
- 🟢 2026-10-03 · [uvularia#2](https://github.com/lentago/uvularia/issues/2) — Phase 0 · core: record and obligation schemas
- 🟣 2026-10-03 · [uvularia#12](https://github.com/lentago/uvularia/pull/12) — Phase 0 · core: record and obligation schemas
- 🟣 2026-10-03 · [site-lentago-dev#84](https://github.com/lentago/site-lentago-dev/pull/84) — Point the public-record offering at uvularia, not a client's site
- 🟣 2026-10-03 · [uvularia#1](https://github.com/lentago/uvularia/pull/1) — Seed uvularia: README, CLAUDE.md, concept, ADR-0001, banner, review prompt
- 🟣 2026-10-03 · [.github#199](https://github.com/lentago/.github/pull/199) — ADR-0009: uvularia records vault; create lentago/uvularia from repo-template
- 🟢 2026-10-03 · [.github#128](https://github.com/lentago/.github/issues/128) — Offering: Ask-the-Records kit — fact corpus + grounded Ask, client-owned
- 🟣 2026-10-03 · [.github#198](https://github.com/lentago/.github/pull/198) — Drop the pondviewlane receipt from the org profile
- 🟣 2026-10-03 · [.github#197](https://github.com/lentago/.github/pull/197) — Align the org profile with lentago.dev and fix the DeepWiki links
- 🟣 2026-10-03 · [site-lentago-dev#83](https://github.com/lentago/site-lentago-dev/pull/83) — Add printer profiles and CMYK exports to the business card render
- 🟣 2026-10-03 · [site-lentago-dev#82](https://github.com/lentago/site-lentago-dev/pull/82) — Add the business card as a token-driven HTML source with a print-ready PDF
- 🟣 2026-10-02 · [site-lentago-dev#81](https://github.com/lentago/site-lentago-dev/pull/81) — Rewrite the Suite section in plain language
- 🟣 2026-10-02 · [site-lentago-dev#80](https://github.com/lentago/site-lentago-dev/pull/80) — Break up the hero copy and tighten the hero's vertical rhythm
- 🟣 2026-10-02 · [site-lentago-dev#79](https://github.com/lentago/site-lentago-dev/pull/79) — Refine two phrases in the About section
- 🟣 2026-10-02 · [site-lentago-dev#78](https://github.com/lentago/site-lentago-dev/pull/78) — Rewrite the About section timeline from the operator's actual career
- 🟣 2026-10-01 · [site-lentago-dev#77](https://github.com/lentago/site-lentago-dev/pull/77) — Correct three stale suite claims on lentago.dev
- 🟣 2026-10-01 · [lupinus#11](https://github.com/lentago/lupinus/pull/11) — Add guide/stories: five shops, one tech person each
- 🟣 2026-10-01 · [site-lentago-dev#73](https://github.com/lentago/site-lentago-dev/pull/73) — chore(deps): Bump the npm-routine group across 1 directory with 4 updates
- 🟣 2026-10-01 · [music-curator#88](https://github.com/lentago/music-curator/pull/88) — docs: add CONTRIBUTING.md
- 🟣 2026-10-01 · [site-pondviewlane-com#79](https://github.com/lentago/site-pondviewlane-com/pull/79) — Bump nginx from `b34848e` to `abe4772`
- 🟣 2026-10-01 · [site-lentago-dev#74](https://github.com/lentago/site-lentago-dev/pull/74) — chore(deps): Bump nginx from `0d4374c` to `abe4772`
- 🟣 2026-10-01 · [site-icecreamtofightwith-com#191](https://github.com/lentago/site-icecreamtofightwith-com/pull/191) — Bump nginx from `0d4374c` to `abe4772`
- 🟣 2026-10-01 · [site-icecreamtofightwith-com#190](https://github.com/lentago/site-icecreamtofightwith-com/pull/190) — Bump the astro-stack group across 1 directory with 3 updates
- 🟣 2026-10-01 · [solidago#193](https://github.com/lentago/solidago/pull/193) — build(deps): bump aws-actions/configure-aws-credentials from 6.2.3 to 6.2.4 in the actions-routine group
- 🟣 2026-10-01 · [site-pondviewlane-com#78](https://github.com/lentago/site-pondviewlane-com/pull/78) — Bump the astro-stack group with 3 updates
- 🟣 2026-10-01 · [site-lentago-dev#72](https://github.com/lentago/site-lentago-dev/pull/72) — chore(deps): Bump the astro-stack group across 1 directory with 3 updates
- 🟣 2026-10-01 · [site-icecreamtofightwith-com#188](https://github.com/lentago/site-icecreamtofightwith-com/pull/188) — Bump crate-ci/typos from 1.49.0 to 1.49.1 in the actions-routine group
- 🟣 2026-10-01 · [shared-workflows#59](https://github.com/lentago/shared-workflows/pull/59) — chore(deps): Bump the actions-routine group across 1 directory with 4 updates
- 🟣 2026-10-01 · [monarda#8](https://github.com/lentago/monarda/pull/8) — Bump the actions-routine group with 2 updates
- 🟣 2026-10-01 · [kalmia#129](https://github.com/lentago/kalmia/pull/129) — build(deps): bump aws-actions/configure-aws-credentials from 6.2.3 to 6.2.4 in the actions-routine group
- 🟣 2026-10-01 · [.github#185](https://github.com/lentago/.github/pull/185) — build(deps): bump the actions-routine group across 1 directory with 2 updates
- 🟣 2026-10-01 · [drosera#213](https://github.com/lentago/drosera/pull/213) — chore(deps): Bump the actions-routine group across 1 directory with 2 updates
- 🟣 2026-10-01 · [claytonia#113](https://github.com/lentago/claytonia/pull/113) — chore(deps): bump aws-actions/configure-aws-credentials from 6.2.3 to 6.3.0 in the actions-routine group across 1 directory
- 🟣 2026-10-01 · [site-lentago-dev#76](https://github.com/lentago/site-lentago-dev/pull/76) — Voice pass on the landing copy: plain words, no paid-consulting residue, no mock live data
- 🟣 2026-10-01 · [.github#194](https://github.com/lentago/.github/pull/194) — Drop 'dirt pay' from the reader description
- 🟣 2026-09-30 · [.github#191](https://github.com/lentago/.github/pull/191) — Fork-first wording in the merge-gate comments; asclepias is vol. 1 of the guide
- 🟣 2026-09-30 · [claytonia#123](https://github.com/lentago/claytonia/pull/123) — Reword the exhibit paragraph for the practice framing
- 🟣 2026-09-30 · [solidago#194](https://github.com/lentago/solidago/pull/194) — Voice pass on ADOPTION.md; canonical README framing (ADR-0008)
- 🟣 2026-09-30 · [lupinus#7](https://github.com/lentago/lupinus/pull/7) — Reposition the adoption guide as vol. 2 of the guide, one voice with asclepias (ADR-0004)
- 🟣 2026-09-30 · [asclepias#11](https://github.com/lentago/asclepias/pull/11) — Reposition the field guide as vol. 1 of the guide: one reader, fork-first labs (ADR-0005)
- 🟣 2026-09-30 · [monarda#9](https://github.com/lentago/monarda/pull/9) — Voice pass on the client-facing kit docs (ADR-0008)
- 🟣 2026-09-30 · [osmunda#5](https://github.com/lentago/osmunda/pull/5) — Voice pass on the runbooks; canonical README footer (ADR-0008)
- 🟣 2026-09-30 · [site-pondviewlane-com#80](https://github.com/lentago/site-pondviewlane-com/pull/80) — Canonical README framing for the pro-bono practice (ADR-0008)
- 🟣 2026-09-30 · [site-icecreamtofightwith-com#192](https://github.com/lentago/site-icecreamtofightwith-com/pull/192) — Canonical README framing for the pro-bono practice (ADR-0008)
- 🟣 2026-09-30 · [shared-workflows#60](https://github.com/lentago/shared-workflows/pull/60) — Canonical README framing for the pro-bono practice (ADR-0008)
- 🟣 2026-09-30 · [repo-template#21](https://github.com/lentago/repo-template/pull/21) — Canonical README framing for the pro-bono practice (ADR-0008)
- 🟣 2026-09-30 · [music-curator#89](https://github.com/lentago/music-curator/pull/89) — Canonical README framing for the pro-bono practice (ADR-0008)
- 🟣 2026-09-30 · [drosera#215](https://github.com/lentago/drosera/pull/215) — Voice pass on the status-page docs; canonical README framing (ADR-0008)
- 🟣 2026-09-30 · [.github#193](https://github.com/lentago/.github/pull/193) — Voice pass on the lock-in kit docs (ADR-0008)
- 🟣 2026-09-30 · [kalmia#130](https://github.com/lentago/kalmia/pull/130) — Voice pass on the Quick start; canonical README framing (ADR-0008)
- 🟣 2026-09-30 · [epigaea#521](https://github.com/lentago/epigaea/pull/521) — Canonical README framing for the pro-bono practice (ADR-0008)
- 🟣 2026-09-30 · [claytonia#122](https://github.com/lentago/claytonia/pull/122) — Canonical README framing for the pro-bono practice (ADR-0008)
- 🟣 2026-09-30 · [brasenia#20](https://github.com/lentago/brasenia/pull/20) — Canonical README framing for the pro-bono practice (ADR-0008)
- 🟣 2026-09-30 · [betula#111](https://github.com/lentago/betula/pull/111) — Canonical README framing for the pro-bono practice (ADR-0008)
- 🟢 2026-09-30 · [.github#90](https://github.com/lentago/.github/issues/90) — Recommendation: engagement pathways — the lab ladder for new members
- 🟣 2026-09-30 · [mitchella#14](https://github.com/lentago/mitchella/pull/14) — Swap the learning-lab blockquote for the practice framing
- 🟣 2026-09-30 · [.github#190](https://github.com/lentago/.github/pull/190) — Reposition Lentago Labs as a pro-bono practice with one reader (ADR-0008)
- 🟣 2026-09-30 · [site-lentago-dev#75](https://github.com/lentago/site-lentago-dev/pull/75) — Say plainly that help is free for mission-driven orgs
- 🟣 2026-09-28 · [.github#189](https://github.com/lentago/.github/pull/189) — Weekly fleet reports refresh — 2026-09-28
- 🟣 2026-09-22 · [drosera#214](https://github.com/lentago/drosera/pull/214) — feat(context-ledger)!: remove ledger alerts + dashboard row (decommissioned)
- 🟣 2026-09-22 · [claytonia#121](https://github.com/lentago/claytonia/pull/121) — feat(context-ledger)!: decommission the context ledger
- 🟣 2026-09-21 · [.github#188](https://github.com/lentago/.github/pull/188) — Weekly fleet reports refresh — 2026-09-21
- 🟢 2026-09-20 · [claytonia#118](https://github.com/lentago/claytonia/issues/118) — Idle workers churn ~130 KiB/s of journald writes each and ~7 SMB req/s against the NAS
- 🟣 2026-09-20 · [claytonia#119](https://github.com/lentago/claytonia/pull/119) — Poll the inbox every 60s and stop journaling per-activation systemd chatter
- 🟣 2026-09-14 · [.github#186](https://github.com/lentago/.github/pull/186) — Weekly fleet reports refresh — 2026-09-14
- 🟣 2026-09-07 · [.github#184](https://github.com/lentago/.github/pull/184) — Weekly fleet reports refresh — 2026-09-07

---

## Code census

**The lens:** a `CLAUDE.md` (and its kin — `AGENTS.md`, skill `SKILL.md`, and the LLM prompt-programs that *are* a tool's logic) is an instruction set maintained for hygiene, so it's counted as **natural-language code**. Documentation, content/data, and community-health markdown are tallied separately and excluded from the code total, as are data payloads and generated files. This is a deliberate re-cut of the canonical [`metrics/language-census.md`](../metrics/language-census.md), which instead counts all Markdown/JSON/HTML as code.

### Languages

cloc *code* lines (blank + comment excluded). Shell folds Bourne + Bash. Instruction-markdown is promoted into the count (**bold**); the excluded buckets sit below the total.

| # | Language | Code | Files | Share |
|---|----------|-----:|------:|------:|
| 1 | JSON | 46,101 | 469 | 36.9% |
| 2 | Python | 28,567 | 182 | 22.8% |
| 3 | YAML | 16,309 | 290 | 13.0% |
| 4 | HCL | 8,445 | 132 | 6.8% |
| 5 | Shell (Bourne + Bash) | 5,440 | 79 | 4.4% |
| 6 | Text | 4,817 | 231 | 3.9% |
| 7 | JavaScript | 4,776 | 56 | 3.8% |
| 8 | Astro | 3,831 | 51 | 3.1% |
| 9 | **Instructions (CLAUDE.md family + prompt-programs)** | 2,455 | 21 | 2.0% |
| 10 | CSS | 1,402 | 10 | 1.1% |
| 11 | JSX | 1,046 | 12 | 0.8% |
| 12 | TypeScript | 682 | 35 | 0.5% |
| 13 | Jinja Template | 560 | 15 | 0.4% |
| 14 | HTML | 257 | 2 | 0.2% |
| 15 | TOML | 193 | 13 | 0.2% |
| 16 | XML | 129 | 5 | 0.1% |
| 17 | Other (TOML / Dockerfile / …) | 30 | 4 | 0.0% |
| | **CODE TOTAL** | **125,040** | **1607** | 100% |
| — | _Data / exports — excluded_ | 119,165 | 9 | — |
| — | _Generated (lockfiles, SVG, brand artefacts) — excluded_ | 54,194 | 118 | — |

### Instruction-markdown as code

- **Hygiene family** (21 files · `CLAUDE.md`, `AGENTS.md`, `SKILL.md`): **2,455 lines**
- **Prompt-programs** (0 files · reference-checker auditors): **0 lines**

#### Hygiene surface — each file is a maintenance obligation

| Repo | File | Lines |
|------|------|------:|
| epigaea | `CLAUDE.md` | 400 |
| shared-workflows | `CLAUDE.md` | 239 |
| site-pondviewlane-com | `CLAUDE.md` | 224 |
| .github | `CLAUDE.md` | 223 |
| betula | `CLAUDE.md` | 156 |
| kalmia | `CLAUDE.md` | 155 |
| site-lentago-dev | `CLAUDE.md` | 108 |
| solidago | `CLAUDE.md` | 99 |
| site-icecreamtofightwith-com | `CLAUDE.md` | 98 |
| drosera | `CLAUDE.md` | 96 |
| uvularia | `CLAUDE.md` | 79 |
| lupinus | `CLAUDE.md` | 73 |
| asclepias | `CLAUDE.md` | 70 |
| music-curator | `CLAUDE.md` | 68 |
| drosera | `AGENTS.md` | 67 |
| mitchella | `CLAUDE.md` | 62 |
| claytonia | `CLAUDE.md` | 57 |
| brasenia | `CLAUDE.md` | 56 |
| osmunda | `CLAUDE.md` | 53 |
| monarda | `CLAUDE.md` | 50 |
| repo-template | `CLAUDE.md` | 22 |
| **21 files** | | **2,455** |

### Per-repo

| Repo | Code | Instr | Doc-md | Content-md | Data |
|------|-----:|------:|-------:|-----------:|-----:|
| epigaea | 24,022 | 400 | 1,552 | 0 | 0 |
| drosera | 18,694 | 163 | 2,064 | 0 | 0 |
| uvularia | 16,536 | 79 | 6,167 | 0 | 0 |
| uvularia-demo-records | 7,760 | 0 | 3,675 | 0 | 0 |
| site-pondviewlane-com | 7,435 | 224 | 2,914 | 0 | 0 |
| solidago | 7,129 | 99 | 2,662 | 0 | 0 |
| music-curator | 5,667 | 68 | 1,254 | 12,754 | 119,165 |
| uvularia-records-template | 5,120 | 0 | 862 | 0 | 0 |
| .github | 3,793 | 223 | 2,018 | 3,508 | 0 |
| kalmia | 3,632 | 155 | 1,502 | 0 | 0 |
| mitchella | 3,629 | 62 | 614 | 0 | 0 |
| site-icecreamtofightwith-com | 3,491 | 98 | 901 | 6,004 | 0 |
| site-lentago-dev | 2,851 | 108 | 674 | 0 | 0 |
| uvularia-demo-ask-rules | 2,808 | 0 | 424 | 0 | 0 |
| claytonia | 2,106 | 57 | 1,392 | 0 | 0 |
| uvularia-site-template | 2,011 | 0 | 191 | 0 | 0 |
| uvularia-demo-site | 2,009 | 0 | 191 | 0 | 0 |
| betula | 1,865 | 156 | 1,599 | 0 | 0 |
| shared-workflows | 1,170 | 239 | 772 | 0 | 0 |
| uvularia-rules-template | 979 | 0 | 241 | 0 | 0 |
| monarda | 960 | 50 | 555 | 0 | 0 |
| osmunda | 394 | 53 | 466 | 0 | 0 |
| brasenia | 307 | 56 | 1,612 | 0 | 0 |
| lupinus | 226 | 73 | 1,315 | 0 | 0 |
| coderabbit | 180 | 0 | 39 | 0 | 0 |
| asclepias | 178 | 70 | 792 | 0 | 0 |
| repo-template | 88 | 22 | 272 | 0 | 0 |

### Markdown taxonomy

The fleet carries **61,997 lines of Markdown across 1361 files**; only 4.0% is instruction-code.

| Class | Lines | Files | Disposition |
|-------|------:|------:|-------------|
| **Instructions** | 2,455 | 21 | **counted as code** |
| Content / data | 22,266 | 697 | payload (vault notes, recipes, test-sets) — excluded |
| Documentation | 36,720 | 626 | READMEs, docs, ADRs, runbooks — excluded |
| Community-health | 556 | 17 | CONTRIBUTING/SECURITY/templates — excluded |
| **All Markdown** | **61,997** | **1361** | |

---

## Method

- **Issues:** open issues via `gh search issues --owner lentago --state open`; activity from `gh search prs --owner lentago --merged` and closed issues filtered to the 30-day window. Public metadata only — no transcript harvest, ops items, or homelab detail (those live in the LAN copy).
- **Census tool:** `cloc`, run per-repo as `cloc --by-file --vcs=git` so only git-tracked files count (build output, `node_modules`, `.terraform`, venvs never enter). Lines are cloc *code* lines.
- **Scope:** the active repos owned by the `lentago` org, derived at runtime — personal repos and third-party clones are out of scope; archived repos are frozen and excluded.
- **Markdown classifier:** instruction-code = `CLAUDE.md`/`AGENTS.md`/`SKILL.md` or a versioned `prompts/*-auditor.md`; community-health = governance filenames + issue/PR templates; content = repo-scoped payload paths (music-curator `vault/`, ice-cream `recipes/`·manuscript, reference-checker `test-sets/`·`reports/`, dotgithub `fleet-reports/`); everything else = documentation.
- **Data / generated carve-outs:** exported payloads under the declared data dirs (music-curator `data/`, homeassistant-config `context/`) count as data whatever their serialisation — JSON, JSONL, CSV/TSV, XML, YAML — as does reference-checker's rendered `reports/*.html`; lockfiles, SVG and `.github/brand/generated/` (emitted from `brand/fleet.json`) are generated. drosera's `dashboards/*.json` stay in code as Terraform-enforced dashboards-as-code.
- **Regenerating:** `python3 metrics/generate-fleet-reports.py --out-dir .`

_Generated with Claude Code (Repo Claude)._
