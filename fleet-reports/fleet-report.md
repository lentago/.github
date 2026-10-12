# Lentago Labs Fleet Report

> [!NOTE]
> **Co-authored with [Claude](https://claude.ai)** (Repo Claude, the Lentago Labs fleet steward). Auto-generated weekly from the fleet's public state (GitHub issues/PRs + `cloc` over public repo contents) — no personal, security, or homelab-internal detail is included. A prettier, editorialised copy renders on the Lentago lab LAN.

**Generated:** 2026-10-12 20:35 UTC · Scope: the **27 active** `lentago` repos (archived repos frozen &amp; excluded) · Activity window: last 30 days (since 2026-09-12).

## Snapshot

| Open issues | PRs merged (30d) | Issues closed (30d) | Code (incl. instructions) | Instruction-markdown |
|---:|---:|---:|---:|---:|
| **135** | 378 | 148 | **134,198** | 2,497 (21 files) |

The fleet's hand-maintained natural-language instruction surface (**2,497 lines** across 21 files) is among the largest "languages" in the code base — `reference-checker` alone is almost entirely prompt-program source.

---

## Open issues — 135 across 18 repos

### .github — 31 open

| # | Title |
|---|-------|
| [253](https://github.com/lentago/.github/issues/253) | Offering: Offboarding drill — the access register made real |
| [252](https://github.com/lentago/.github/issues/252) | Offering: Backup with a receipt — object-locked copies and a drilled restore |
| [251](https://github.com/lentago/.github/issues/251) | Offering: Email trust receipt — SPF, DKIM and DMARC as code, an MFA audit, the phishing habit |
| [249](https://github.com/lentago/.github/issues/249) | Offering: Board pack — a one-page monthly operations report the board actually reads |
| [248](https://github.com/lentago/.github/issues/248) | Offering: EOL radar — support end dates open Issues before they bite |
| [247](https://github.com/lentago/.github/issues/247) | Offering: Accessible by default — every page checked, a receipt per build |
| [243](https://github.com/lentago/.github/issues/243) | Credential register: every fleet credential's store, scope, issuer and expiry (names only) |
| [242](https://github.com/lentago/.github/issues/242) | Re-mint two over-broad GitHub tokens: FLEET_REPORTS_TOKEN and the workstation PAT |
| [239](https://github.com/lentago/.github/issues/239) | brand: README header blocks drifted from brand/generated in monarda, osmunda, shared-workflows; coderabbit has none |
| [237](https://github.com/lentago/.github/issues/237) | Retire DeepWiki across the fleet |
| [235](https://github.com/lentago/.github/issues/235) | Genus marks for the eight unmarked species |
| [234](https://github.com/lentago/.github/issues/234) | Enable Dependabot security updates fleet-wide (codified in terraform) |
| [225](https://github.com/lentago/.github/issues/225) | FLEET_ADMIN_TOKEN cannot resolve GitHub App node ids: merge-gate App allowances are unmanageable by Terraform |
| [201](https://github.com/lentago/.github/issues/201) | terraform: creating a repo from repos.json fails on GitHub's default labels (422 already_exists) |
| [200](https://github.com/lentago/.github/issues/200) | Offering: uvularia — client-owned records vault, grounded Ask, live compliance board (supersedes #128) |
| [196](https://github.com/lentago/.github/issues/196) | Offering: help-desk starter for a private repo — issue forms, labels, a board |
| [195](https://github.com/lentago/.github/issues/195) | Offering: sensor trip opens a work order — epigaea alert to GitHub Issue |
| [176](https://github.com/lentago/.github/issues/176) | Codify org settings in Terraform — default_repository_permission is live-only |
| [175](https://github.com/lentago/.github/issues/175) | A public repo entry with a null template_source cannot receive its first commit |
| [134](https://github.com/lentago/.github/issues/134) | Offerings roadmap — tracking epic (refreshed 2026-10-06) |
| [133](https://github.com/lentago/.github/issues/133) | Offering: Ops-in-a-Box — the miniature estate starter kit |
| [132](https://github.com/lentago/.github/issues/132) | Spike: volunteer-ops scheduling — evaluate, don't build (decision memo) |
| [131](https://github.com/lentago/.github/issues/131) | Offering: privacy posture kit for newly covered orgs |
| [130](https://github.com/lentago/.github/issues/130) | Offering: funder-report fact pipeline |
| [129](https://github.com/lentago/.github/issues/129) | Offering: cold-chain & facilities telemetry kit |
| [127](https://github.com/lentago/.github/issues/127) | Guide page: AI-with-receipts — the reviewed-merge operating model, written for the one reader (ships in lupinus) |
| [126](https://github.com/lentago/.github/issues/126) | Offering: Institutional Memory kit — the uvularia Ask box on a private lupinus vault |
| [125](https://github.com/lentago/.github/issues/125) | Offering: Insurance-Receipts Pack — controls with evidence exhaust |
| [124](https://github.com/lentago/.github/issues/124) | Offering: Digital Custody audit — ownership insurance for the org's presence |
| [123](https://github.com/lentago/.github/issues/123) | Offering: Liberation Pipeline — SaaS-export collectors + restore drills |
| [122](https://github.com/lentago/.github/issues/122) | Offering: Good-Standing Kit — registry reconciliation on the uvularia vault (MA pack first) |

### drosera — 16 open

| # | Title |
|---|-------|
| [272](https://github.com/lentago/drosera/issues/272) | Notification-sink contract: one event shape, four sinks, "who gets the call" as a file |
| [264](https://github.com/lentago/drosera/issues/264) | terraform: cloud_usage rule group shows a perpetual repeat_interval diff (1d vs 24h) |
| [251](https://github.com/lentago/drosera/issues/251) | Change pipeline: see every merge travel from push to live, keyed by commit SHA |
| [234](https://github.com/lentago/drosera/issues/234) | GitHub — Actions dashboard: fleet-wide run history, queue time, and failure trends (feed: betula#113) |
| [204](https://github.com/lentago/drosera/issues/204) | Main-branch workflow failures notify nobody — alert on red deploys/applies |
| [200](https://github.com/lentago/drosera/issues/200) | Queue SLO for the agent fleet (pickup latency) + burn alert |
| [199](https://github.com/lentago/drosera/issues/199) | Error-budget monthly section in the fleet report |
| [198](https://github.com/lentago/drosera/issues/198) | Threat Weather: anonymized daily network weather report |
| [197](https://github.com/lentago/drosera/issues/197) | "Are we open" single source of truth |
| [194](https://github.com/lentago/drosera/issues/194) | Adopt grafana-stack (LXC 105) guest capacity from kalmia |
| [169](https://github.com/lentago/drosera/issues/169) | Complete the homelab-observability → drosera rename through CI and hosts |
| [165](https://github.com/lentago/drosera/issues/165) | New-domain radar: alert when an IoT/smart-home device queries a never-before-seen domain (migrated from betula#11) |
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

### claytonia — 10 open

| # | Title |
|---|-------|
| [137](https://github.com/lentago/claytonia/issues/137) | brasenia on the fleet: share mount on the workers, pane command in the worker prompt, fleet beacons |
| [117](https://github.com/lentago/claytonia/issues/117) | Make never-merge a boundary: required check that blocks runner-App PRs without a human approval |
| [116](https://github.com/lentago/claytonia/issues/116) | Close the loop after the PR opens: a capped follow-up job for failing checks and review comments |
| [115](https://github.com/lentago/claytonia/issues/115) | An eval set for the fleet: replayable tasks, deterministic graders, and outcome measures |
| [99](https://github.com/lentago/claytonia/issues/99) | Second job type: batch document/report jobs through the queue contract |
| [65](https://github.com/lentago/claytonia/issues/65) | Complete the bullpen → claytonia rename on-host |
| [47](https://github.com/lentago/claytonia/issues/47) | Roadmap: platform-agnostic workers — Claude Code as one runtime behind the queue contract |
| [24](https://github.com/lentago/claytonia/issues/24) | Branch hygiene across overlapping sessions: clean-desk session-end + prefer fleet dispatch |
| [22](https://github.com/lentago/claytonia/issues/22) | Fleet PR lane separation: rebase-before-merge + dispatch-time overlap check (no two writers on one file/panel) |
| [21](https://github.com/lentago/claytonia/issues/21) | Queue admission control: job ownership, fleet occupancy, and capacity awareness at submit time |

### kalmia — 9 open

| # | Title |
|---|-------|
| [151](https://github.com/lentago/kalmia/issues/151) | OS stance for a nonprofit fleet; ChromeOS Flex as the first donated-hardware profile |
| [124](https://github.com/lentago/kalmia/issues/124) | Retire CT 113 (n8n LXC) after the osmunda burn-in window |
| [108](https://github.com/lentago/kalmia/issues/108) | Forge: golden images with receipts (checksums, SBOM, provenance) |
| [107](https://github.com/lentago/kalmia/issues/107) | Donated-hardware refresh profiles (new client class) |
| [99](https://github.com/lentago/kalmia/issues/99) | Cast client runtime for brasenia: watchdog sender, receiver hosting, then HLS-stack turn-down (brasenia ADR-0006) |
| [63](https://github.com/lentago/kalmia/issues/63) | Complete the lunaria → brasenia rename through runtime |
| [51](https://github.com/lentago/kalmia/issues/51) | Guarantee vzdump coverage for every Terraform-enforced guest (CT 113 had none) |
| [20](https://github.com/lentago/kalmia/issues/20) | Roadmap: provisioning clients beyond Ansible-on-workstations — VMs and containers as peer targets |
| [14](https://github.com/lentago/kalmia/issues/14) | Live-test the ubuntu_laptop profile on real ThinkPad hardware |

### solidago — 9 open

| # | Title |
|---|-------|
| [213](https://github.com/lentago/solidago/issues/213) | Fail the apply when an out-of-band secret still holds its placeholder |
| [184](https://github.com/lentago/solidago/issues/184) | CI plans are never clean: standing task-definition replacements and a recreating SNS email subscription |
| [180](https://github.com/lentago/solidago/issues/180) | Hardening backlog from tf-lint's first trivy run (ECR immutability, CI-role least-privilege, SNS encryption) |
| [172](https://github.com/lentago/solidago/issues/172) | SNS alert email subscription is recreated on every apply — alerts may be reaching nobody |
| [167](https://github.com/lentago/solidago/issues/167) | DMARC posture on our own domains first (precondition for the Email Trust kit) |
| [156](https://github.com/lentago/solidago/issues/156) | Split plan/apply OIDC environments so the terraform environment can carry a branch policy |
| [149](https://github.com/lentago/solidago/issues/149) | Rotating a Lambda's Axiom token requires an unrelated apply to take effect |
| [144](https://github.com/lentago/solidago/issues/144) | Ask Lambda logs land in CloudWatch with no path to Axiom |
| [21](https://github.com/lentago/solidago/issues/21) | Evaluate migration from ElastiCache node-based to serverless |

### betula — 8 open

| # | Title |
|---|-------|
| [133](https://github.com/lentago/betula/issues/133) | GitHub Actions feed: carry the PR number so PR head SHAs join to merge commits (drosera ADR-0010) |
| [130](https://github.com/lentago/betula/issues/130) | GitHub collector: first-tick backfill ran 7.5 min against a 10 min TimeoutStartSec; checkpoint per repo and reuse connections |
| [126](https://github.com/lentago/betula/issues/126) | Liberation Pipeline: SaaS-export collectors + restore drills, as betula clients (lentago/.github#123) |
| [119](https://github.com/lentago/betula/issues/119) | Terraform the Axiom tokens (exact import + rotation handoff) |
| [107](https://github.com/lentago/betula/issues/107) | Device drift self-report: deployed conf hash vs main |
| [106](https://github.com/lentago/betula/issues/106) | Third AWS emitter: CloudTrail → archive + weekly access digest |
| [89](https://github.com/lentago/betula/issues/89) | Complete the firewalla-axiom-pipeline → betula rename on-device |
| [74](https://github.com/lentago/betula/issues/74) | Roadmap: core/client split — Firewalla and solidago (AWS) as peer collector clients |

### uvularia — 8 open

| # | Title |
|---|-------|
| [98](https://github.com/lentago/uvularia/issues/98) | Intake hint says "under library/" but validate resolves source.file from the repo root; first record fails the PR |
| [95](https://github.com/lentago/uvularia/issues/95) | Retention ledger as an obligation pack: the org's own retention policy evaluated against live retention |
| [92](https://github.com/lentago/uvularia/issues/92) | Phase 3 — consumers: the vault-side contract for the funder-report pipeline and Good-Standing reconciliation |
| [91](https://github.com/lentago/uvularia/issues/91) | templates/site: astro check fails on TypeScript 6 (28 strict-mode errors) |
| [85](https://github.com/lentago/uvularia/issues/85) | Template workflow action pins have no automated updater |
| [81](https://github.com/lentago/uvularia/issues/81) | http-cache-semantics GHSA-ch52-4w7c-c8xp: no patched release; not reachable in static builds |
| [57](https://github.com/lentago/uvularia/issues/57) | Records need an event time, and deadlines a local timezone, for lead rules to match the statute for evening meetings |
| [28](https://github.com/lentago/uvularia/issues/28) | Sync templates/records and templates/site to their GitHub template repos on merge |

### brasenia — 7 open

| # | Title |
|---|-------|
| [43](https://github.com/lentago/brasenia/issues/43) | README intro still calls the pane bus and compositor "the roadmap"; ADR-0008 says they run |
| [41](https://github.com/lentago/brasenia/issues/41) | Lobby-pane variant: a visitor-facing screen in a client's own front room |
| [31](https://github.com/lentago/brasenia/issues/31) | Focus producer: unauthenticated 304s spend the GitHub budget, so focus panes refresh every few minutes, not every minute |
| [26](https://github.com/lentago/brasenia/issues/26) | Phase 2: pane bus, compositor, and the first live panes (Cast-first) |
| [17](https://github.com/lentago/brasenia/issues/17) | Live-ingest pane: concept + ADR, acceptance spec, and VideoScene repoint to `live` with board fallback |
| [15](https://github.com/lentago/brasenia/issues/15) | Adopt the display guest (LXC 118) capacity from kalmia |
| [12](https://github.com/lentago/brasenia/issues/12) | Second functional path: Cast-native rendering, then deprecate and turn down the Roku/HLS chain |

### lupinus — 7 open

| # | Title |
|---|-------|
| [21](https://github.com/lentago/lupinus/issues/21) | Tier registry: brasenia row is stale since 2026-10-07; mitchella has no row |
| [20](https://github.com/lentago/lupinus/issues/20) | Picker: "What we are not" names phones, printers and Wi-Fi |
| [19](https://github.com/lentago/lupinus/issues/19) | Stories: one spine, three rungs, one map; a six-row coverage matrix |
| [10](https://github.com/lentago/lupinus/issues/10) | One canonical product list; support/README.md is missing claytonia, epigaea, and brasenia |
| [9](https://github.com/lentago/lupinus/issues/9) | Reconcile the single-file ADOPTION.md template with the INTAKE/DRY-RUN split the exemplar uses |
| [8](https://github.com/lentago/lupinus/issues/8) | Kit rows carry no receipt: mark them provisional or demote until a drill is recorded |
| [4](https://github.com/lentago/lupinus/issues/4) | Epic: adoption guide — Phase 1 (launch set: solidago + monarda) |

### monarda — 5 open

| # | Title |
|---|-------|
| [20](https://github.com/lentago/monarda/issues/20) | npm run a11y: the pinned 127.0.0.1 URL fails when run against the live site as the runbooks say |
| [19](https://github.com/lentago/monarda/issues/19) | First run is red: deploy-pages triggers on the template's initial commit before Pages is enabled |
| [18](https://github.com/lentago/monarda/issues/18) | Decision: a plain org-site rung (multi-page) and a rescue import from WordPress or Squarespace |
| [17](https://github.com/lentago/monarda/issues/17) | Processor presets in the donate block, each with a sandbox walkthrough; one of them is the #5 receipt |
| [11](https://github.com/lentago/monarda/issues/11) | Clear the npm security-alert backlog; add npm to dependabot.yml |

### music-curator — 3 open

| # | Title |
|---|-------|
| [87](https://github.com/lentago/music-curator/issues/87) | follow-fold's bot merge cannot work under GITHUB_TOKEN — two blockers; decide App identity vs human merge |
| [45](https://github.com/lentago/music-curator/issues/45) | Web-verify the promoted person nodes' credit rows |
| [44](https://github.com/lentago/music-curator/issues/44) | Producer-class connectors: decide representation |

### site-lentago-dev — 3 open

| # | Title |
|---|-------|
| [99](https://github.com/lentago/site-lentago-dev/issues/99) | Suite section becomes the six-promise map |
| [86](https://github.com/lentago/site-lentago-dev/issues/86) | Remove committed .playwright-mcp/ scratch output and gitignore it |
| [67](https://github.com/lentago/site-lentago-dev/issues/67) | a11y gate ignores `color-contrast`: the Tidewater palette fails 4.5:1 at the design-token level |

### osmunda — 2 open

| # | Title |
|---|-------|
| [12](https://github.com/lentago/osmunda/issues/12) | Decide how Flux-managed workloads receive secrets, before the n8n cutover |
| [4](https://github.com/lentago/osmunda/issues/4) | The k3s install is disclaimed by both osmunda and kalmia — it exists nowhere |

### shared-workflows — 2 open

| # | Title |
|---|-------|
| [68](https://github.com/lentago/shared-workflows/issues/68) | claude-responder: skip events initiated by bots instead of failing the `claude / claude` check |
| [57](https://github.com/lentago/shared-workflows/issues/57) | Rapid successive merges cancel site deploys, and `:latest`-pinned task defs make the survivor non-deterministic |

### site-icecreamtofightwith-com — 2 open

| # | Title |
|---|-------|
| [198](https://github.com/lentago/site-icecreamtofightwith-com/issues/198) | Clear the npm security-alert backlog (45 open, 42 patchable) |
| [158](https://github.com/lentago/site-icecreamtofightwith-com/issues/158) | Tier accent swatches fail WCAG AA contrast as chip/step backgrounds (design decision needed) |

### epigaea — 1 open

| # | Title |
|---|-------|
| [518](https://github.com/lentago/epigaea/issues/518) | Complete the epigaea rename through runtime (tiers 3–4) |

### site-pondviewlane-com — 1 open

| # | Title |
|---|-------|
| [46](https://github.com/lentago/site-pondviewlane-com/issues/46) | Flip Content-Security-Policy from Report-Only to enforcing |

## Activity — last 30 days

**526 events**, one stream, newest first — 🟣 378 PRs merged · 🟢 148 issues closed

- 🟢 2026-10-12 · [uvularia#96](https://github.com/lentago/uvularia/issues/96) — README says Phase 0 complete while Phase 1 and 2 artifacts are in-tree; name the Ask function's relationship to mitchella
- 🟣 2026-10-12 · [uvularia#97](https://github.com/lentago/uvularia/pull/97) — README: Phases 1 and 2 are built, receipts pending; name the front desk
- 🟢 2026-10-12 · [mitchella#25](https://github.com/lentago/mitchella/issues/25) — ROADMAP says no live API call has been made; uvularia's Ask function runs the engine — record the relationship
- 🟣 2026-10-12 · [mitchella#26](https://github.com/lentago/mitchella/pull/26) — Record the uvularia Ask function as the first front desk (ADR-0007)
- 🟢 2026-10-12 · [monarda#5](https://github.com/lentago/monarda/issues/5) — Run the dry-run and record the first receipt
- 🟣 2026-10-12 · [monarda#21](https://github.com/lentago/monarda/pull/21) — Record the first timed dry-run: 3 min 01 s, two defects filed
- 🟢 2026-10-12 · [.github#254](https://github.com/lentago/.github/issues/254) — Profile suite table omits epigaea and brasenia; betula banner tagline overstates retention
- 🟣 2026-10-12 · [.github#255](https://github.com/lentago/.github/pull/255) — Profile suite rows for epigaea, brasenia; betula tagline off-device
- 🟣 2026-10-12 · [epigaea#530](https://github.com/lentago/epigaea/pull/530) — docs: facilities kit is tracked, not built — README and CLAUDE.md
- 🟢 2026-10-12 · [betula#137](https://github.com/lentago/betula/issues/137) — README still carries the retired learning-lab blurb; banner overstates retention
- 🟣 2026-10-12 · [betula#138](https://github.com/lentago/betula/pull/138) — docs: drop retired learning-lab blurb; banner says off-device search
- 🟢 2026-10-12 · [drosera#255](https://github.com/lentago/drosera/issues/255) — docs/adr/README.md index is missing rows for ADR-0008 and ADR-0009
- 🟢 2026-10-12 · [drosera#257](https://github.com/lentago/drosera/issues/257) — docs/adr/README.md index is missing the rows for ADR-0008 and ADR-0009
- 🟣 2026-10-12 · [drosera#273](https://github.com/lentago/drosera/pull/273) — docs(adr): add index rows for ADR-0008 and ADR-0009
- 🟢 2026-10-12 · [kalmia#152](https://github.com/lentago/kalmia/issues/152) — CLAUDE.md says four target profiles; README and the tree have five
- 🟣 2026-10-12 · [kalmia#153](https://github.com/lentago/kalmia/pull/153) — CLAUDE.md: five target profiles, not four
- 🟣 2026-10-09 · [lupinus#18](https://github.com/lentago/lupinus/pull/18) — Stories: cite uvularia for the watershed's public records, drop pondviewlane and closed #128
- 🟣 2026-10-08 · [.github#246](https://github.com/lentago/.github/pull/246) — Revise README content for better presentation
- 🟣 2026-10-08 · [site-pondviewlane-com#88](https://github.com/lentago/site-pondviewlane-com/pull/88) — ci: version.json without source identity so the content guard passes
- 🟢 2026-10-08 · [drosera#270](https://github.com/lentago/drosera/issues/270) — Change pipeline: stuck alert, the newest main commit with no live event after its budget
- 🟣 2026-10-08 · [drosera#271](https://github.com/lentago/drosera/pull/271) — feat(alerts): Change pipeline stuck alert for heads not live
- 🟢 2026-10-08 · [kalmia#148](https://github.com/lentago/kalmia/issues/148) — pub: run brasenia's change-pipeline pane producer next to the focus producer
- 🟣 2026-10-08 · [kalmia#149](https://github.com/lentago/kalmia/pull/149) — pub: run the change-pipeline pane producer beside the focus producer
- 🟢 2026-10-08 · [drosera#266](https://github.com/lentago/drosera/issues/266) — Change pipeline: pipeline.json producer on LXC 105 and the change_pipeline_state stream
- 🟣 2026-10-08 · [drosera#269](https://github.com/lentago/drosera/pull/269) — pipeline-producer: pipeline.json producer and change_pipeline_state
- 🟣 2026-10-08 · [site-pondviewlane-com#87](https://github.com/lentago/site-pondviewlane-com/pull/87) — ci: site-deploy v1.3.0 so the build serves /version.json
- 🟣 2026-10-08 · [site-icecreamtofightwith-com#201](https://github.com/lentago/site-icecreamtofightwith-com/pull/201) — ci: site-deploy v1.3.0 so the build serves /version.json
- 🟢 2026-10-08 · [brasenia#36](https://github.com/lentago/brasenia/issues/36) — Change-pipeline pane: a producer on pub that renders the in-flight changes from pipeline.json
- 🟣 2026-10-08 · [brasenia#40](https://github.com/lentago/brasenia/pull/40) — feat(producers): change-pipeline pane from pipeline.json
- 🟢 2026-10-08 · [drosera#267](https://github.com/lentago/drosera/issues/267) — Change pipeline: sites live probe on LXC 105 reading each site's version.json
- 🟣 2026-10-08 · [drosera#268](https://github.com/lentago/drosera/pull/268) — feat(sites-live): sites live probe reading version.json
- 🟣 2026-10-08 · [site-lentago-dev#98](https://github.com/lentago/site-lentago-dev/pull/98) — ci: site-deploy v1.3.0 so the build serves /version.json
- 🟢 2026-10-08 · [brasenia#32](https://github.com/lentago/brasenia/issues/32) — Focus producer: main's "latest completed run" is often a skipped comment-triggered workflow
- 🟣 2026-10-08 · [brasenia#38](https://github.com/lentago/brasenia/pull/38) — fix(focus): show main's latest meaningful push run
- 🟢 2026-10-07 · [kalmia#146](https://github.com/lentago/kalmia/issues/146) — pub: proxy /viewport/pipeline.json to drosera's pipeline producer on LXC 105
- 🟣 2026-10-07 · [kalmia#147](https://github.com/lentago/kalmia/pull/147) — pub: proxy /viewport/pipeline.json to the producer on LXC 105
- 🟣 2026-10-07 · [shared-workflows#71](https://github.com/lentago/shared-workflows/pull/71) — release: internal action refs to v1.3.0, date the changelog
- 🟢 2026-10-07 · [shared-workflows#69](https://github.com/lentago/shared-workflows/issues/69) — site-deploy: write public/version.json with the commit before the Astro build
- 🟣 2026-10-07 · [shared-workflows#70](https://github.com/lentago/shared-workflows/pull/70) — site-deploy: write version.json with the commit pre-build
- 🟢 2026-10-07 · [brasenia#37](https://github.com/lentago/brasenia/issues/37) — ADR: the compositor and the producers run on pub, the display guest stays a client
- 🟢 2026-10-07 · [betula#134](https://github.com/lentago/betula/issues/134) — GitHub collector: emit a github_branch_head event per repo per tick (the newest main for the stuck alert)
- 🟣 2026-10-07 · [betula#135](https://github.com/lentago/betula/pull/135) — feat(github): emit github_branch_head per repo per tick
- 🟣 2026-10-07 · [brasenia#39](https://github.com/lentago/brasenia/pull/39) — docs(adr): ADR-0008 compositor and producers run on pub
- 🟢 2026-10-07 · [drosera#262](https://github.com/lentago/drosera/issues/262) — Change — Pipeline: per-repo stage strip with the Graphviz panel
- 🟣 2026-10-07 · [drosera#265](https://github.com/lentago/drosera/pull/265) — Change — Pipeline: per-repo stage strip with the Graphviz panel
- 🟣 2026-10-07 · [drosera#263](https://github.com/lentago/drosera/pull/263) — terraform: install the Graphviz panel plugin for the per-repo stage strip
- 🟢 2026-10-07 · [kalmia#144](https://github.com/lentago/kalmia/issues/144) — pub: sortable directory index, and codify the Caddy config in the pub role
- 🟣 2026-10-07 · [kalmia#145](https://github.com/lentago/kalmia/pull/145) — pub: sortable directory index, Caddy config managed by the role
- 🟣 2026-10-07 · [.github#227](https://github.com/lentago/.github/pull/227) — Weekly fleet reports refresh — 2026-10-05
- 🟣 2026-10-07 · [site-icecreamtofightwith-com#195](https://github.com/lentago/site-icecreamtofightwith-com/pull/195) — Bump wait-on from 9.1.0 to 9.5.1 in the npm-routine group across 1 directory
- 🟣 2026-10-07 · [site-icecreamtofightwith-com#193](https://github.com/lentago/site-icecreamtofightwith-com/pull/193) — Bump the astro-stack group across 1 directory with 2 updates
- 🟣 2026-10-07 · [uvularia#84](https://github.com/lentago/uvularia/pull/84) — build(deps): bump the actions-major group across 1 directory with 3 updates
- 🟣 2026-10-07 · [solidago#206](https://github.com/lentago/solidago/pull/206) — build(deps): bump aws-actions/configure-aws-credentials from 6.2.4 to 6.3.0 in the actions-routine group across 1 directory
- 🟣 2026-10-07 · [site-lentago-dev#88](https://github.com/lentago/site-lentago-dev/pull/88) — chore(deps): Bump the astro-stack group across 1 directory with 2 updates
- 🟣 2026-10-07 · [site-icecreamtofightwith-com#194](https://github.com/lentago/site-icecreamtofightwith-com/pull/194) — Bump crate-ci/typos from 1.49.1 to 1.50.3 in the actions-routine group across 1 directory
- 🟣 2026-10-07 · [shared-workflows#61](https://github.com/lentago/shared-workflows/pull/61) — chore(deps): Bump the actions-routine group with 4 updates
- 🟣 2026-10-07 · [monarda#10](https://github.com/lentago/monarda/pull/10) — Bump aws-actions/configure-aws-credentials from 6.2.4 to 6.3.0 in the actions-routine group
- 🟣 2026-10-07 · [mitchella#19](https://github.com/lentago/mitchella/pull/19) — Bump actions/setup-python from 5.6.0 to 7.0.0 in the actions-major group
- 🟣 2026-10-07 · [coderabbit#3](https://github.com/lentago/coderabbit/pull/3) — Bump the actions-major group with 2 updates
- 🟢 2026-10-07 · [.github#244](https://github.com/lentago/.github/issues/244) — ADR-0011: how the fleet handles secrets
- 🟣 2026-10-07 · [.github#245](https://github.com/lentago/.github/pull/245) — ADR-0011: how the fleet handles secrets
- 🟢 2026-10-07 · [.github#240](https://github.com/lentago/.github/issues/240) — Enable secret scanning and push protection on every fleet repo
- 🟣 2026-10-07 · [.github#241](https://github.com/lentago/.github/pull/241) — Enable secret scanning and push protection on every fleet repo
- 🟣 2026-10-07 · [drosera#261](https://github.com/lentago/drosera/pull/261) — change-pipeline: escape the regex dot as \\. in LogQL strings so Grafana's frontend accepts the queries
- 🟣 2026-10-07 · [drosera#260](https://github.com/lentago/drosera/pull/260) — change-pipeline: run the table panels as instant queries; match the merged value field name
- 🟢 2026-10-07 · [kalmia#142](https://github.com/lentago/kalmia/issues/142) — lunaria-frames follows the viewport pointer: the Roku/HLS adapter for the brasenia compositor
- 🟣 2026-10-07 · [kalmia#143](https://github.com/lentago/kalmia/pull/143) — feat(lunaria): lunaria-frames follows the viewport pointer (#142)
- 🟢 2026-10-07 · [drosera#258](https://github.com/lentago/drosera/issues/258) — Change — Pipeline dashboard: where every merge stands, from the Actions feed and the live emitters
- 🟣 2026-10-07 · [drosera#259](https://github.com/lentago/drosera/pull/259) — feat(dashboard): Change — Pipeline, where every merge stands
- 🟢 2026-10-07 · [brasenia#34](https://github.com/lentago/brasenia/issues/34) — `pane` command: claim, renew and release a pane on the viewport bus, plus the governance page every Claude reads
- 🟣 2026-10-07 · [brasenia#35](https://github.com/lentago/brasenia/pull/35) — feat(bin): pane command and the claiming-the-display page
- 🟢 2026-10-07 · [kalmia#140](https://github.com/lentago/kalmia/issues/140) — Run the brasenia compositor and focus producer on pub (LXC 114) from /srv/brasenia
- 🟣 2026-10-07 · [kalmia#141](https://github.com/lentago/kalmia/pull/141) — feat(pub): run the brasenia compositor and focus producer on pub (#140)
- 🟢 2026-10-07 · [brasenia#27](https://github.com/lentago/brasenia/issues/27) — Compositor v1: rank the pane bus by rubric and publish current.json; write the v1 contracts into concept.md
- 🟣 2026-10-07 · [brasenia#30](https://github.com/lentago/brasenia/pull/30) — Compositor v1: rank the pane bus by rubric v1 and publish current.json
- 🟢 2026-10-07 · [drosera#252](https://github.com/lentago/drosera/issues/252) — session-heartbeat.sh: write a viewport focus beacon alongside the Loki heartbeat
- 🟣 2026-10-07 · [drosera#254](https://github.com/lentago/drosera/pull/254) — feat(claude-cost-export): viewport focus beacon alongside heartbeat
- 🟢 2026-10-07 · [brasenia#28](https://github.com/lentago/brasenia/issues/28) — Focus producer: render an open-PRs pane for every repo with a fresh session beacon
- 🟣 2026-10-07 · [brasenia#33](https://github.com/lentago/brasenia/pull/33) — feat(producers): focus producer — open-PRs pane per beaconed repo
- 🟢 2026-10-07 · [betula#131](https://github.com/lentago/betula/issues/131) — Firewalla gitops-sync emits a `live` change-pipeline event with the deployed SHA
- 🟣 2026-10-07 · [betula#132](https://github.com/lentago/betula/pull/132) — feat(gitops-sync): emit live change-pipeline event per sync tick
- 🟢 2026-10-07 · [drosera#253](https://github.com/lentago/drosera/issues/253) — ADR-0010: the change pipeline keyed by commit SHA, and the first `live` emitter (alloy gitops on LXC 105)
- 🟣 2026-10-07 · [drosera#256](https://github.com/lentago/drosera/pull/256) — ADR-0010 change pipeline keyed by SHA, and the first live emitter (alloy gitops)
- 🟢 2026-10-07 · [brasenia#13](https://github.com/lentago/brasenia/issues/13) — Cast client: custom web receiver + current-pane pointer contract
- 🟣 2026-10-07 · [brasenia#29](https://github.com/lentago/brasenia/pull/29) — feat(cast-app): receiver follows the compositor pointer (Phase B)
- 🟢 2026-10-07 · [betula#113](https://github.com/lentago/betula/issues/113) — GitHub Actions collector client: poll org run/job history into Grafana Cloud Loki
- 🟣 2026-10-07 · [betula#129](https://github.com/lentago/betula/pull/129) — feat(github): GitHub Actions collector client → Grafana Cloud Loki (#113)
- 🟢 2026-10-07 · [osmunda#10](https://github.com/lentago/osmunda/issues/10) — Align the README header block with brand/generated
- 🟣 2026-10-07 · [osmunda#11](https://github.com/lentago/osmunda/pull/11) — Align the README header block with brand/generated
- 🟢 2026-10-07 · [monarda#15](https://github.com/lentago/monarda/issues/15) — Align the README header block with brand/generated
- 🟣 2026-10-07 · [monarda#16](https://github.com/lentago/monarda/pull/16) — Align the README header block with brand/generated
- 🟢 2026-10-07 · [epigaea#529](https://github.com/lentago/epigaea/issues/529) — Remove DeepWiki from the README
- 🟢 2026-10-07 · [site-pondviewlane-com#86](https://github.com/lentago/site-pondviewlane-com/issues/86) — Remove DeepWiki from the README
- 🟢 2026-10-07 · [asclepias#16](https://github.com/lentago/asclepias/issues/16) — Retire DeepWiki: README, Lab 00, day-one, glossary, pattern catalog, CLAUDE.md
- 🟢 2026-10-07 · [lupinus#17](https://github.com/lentago/lupinus/issues/17) — Remove DeepWiki from the README, CLAUDE.md, and the story footers
- 🟢 2026-10-07 · [music-curator#94](https://github.com/lentago/music-curator/issues/94) — Remove DeepWiki from the README
- 🟢 2026-10-07 · [drosera#250](https://github.com/lentago/drosera/issues/250) — Remove DeepWiki from the README
- 🟢 2026-10-07 · [shared-workflows#67](https://github.com/lentago/shared-workflows/issues/67) — Remove DeepWiki from the README
- 🟢 2026-10-07 · [coderabbit#5](https://github.com/lentago/coderabbit/issues/5) — Remove DeepWiki from the README footer
- 🟢 2026-10-07 · [solidago#212](https://github.com/lentago/solidago/issues/212) — Remove DeepWiki from the README and .mcp.json
- 🟢 2026-10-07 · [betula#128](https://github.com/lentago/betula/issues/128) — Remove DeepWiki from the README
- 🟢 2026-10-07 · [repo-template#25](https://github.com/lentago/repo-template/issues/25) — Remove DeepWiki from the README
- 🟢 2026-10-07 · [uvularia#90](https://github.com/lentago/uvularia/issues/90) — Remove DeepWiki from the README
- 🟢 2026-10-07 · [claytonia#136](https://github.com/lentago/claytonia/issues/136) — Remove DeepWiki from the README
- 🟢 2026-10-07 · [brasenia#25](https://github.com/lentago/brasenia/issues/25) — Remove DeepWiki from the README
- 🟢 2026-10-07 · [site-icecreamtofightwith-com#200](https://github.com/lentago/site-icecreamtofightwith-com/issues/200) — Remove DeepWiki from the README
- 🟢 2026-10-07 · [site-lentago-dev#97](https://github.com/lentago/site-lentago-dev/issues/97) — Remove DeepWiki from the README
- 🟢 2026-10-07 · [mitchella#23](https://github.com/lentago/mitchella/issues/23) — Remove DeepWiki from the README
- 🟢 2026-10-07 · [kalmia#139](https://github.com/lentago/kalmia/issues/139) — Remove DeepWiki from the README
- 🟣 2026-10-07 · [claytonia#135](https://github.com/lentago/claytonia/pull/135) — fleet: retire DeepWiki — header badge, README section, footer clause
- 🟣 2026-10-07 · [site-icecreamtofightwith-com#199](https://github.com/lentago/site-icecreamtofightwith-com/pull/199) — fleet: retire DeepWiki — header badge, README section, footer clause
- 🟣 2026-10-07 · [uvularia#89](https://github.com/lentago/uvularia/pull/89) — fleet: retire DeepWiki — header badge, footer clause
- 🟣 2026-10-07 · [site-pondviewlane-com#85](https://github.com/lentago/site-pondviewlane-com/pull/85) — fleet: retire DeepWiki — header badge, README section, footer clause
- 🟣 2026-10-07 · [lupinus#16](https://github.com/lentago/lupinus/pull/16) — fleet: retire DeepWiki — header badge, footer clause, story footers
- 🟣 2026-10-07 · [epigaea#528](https://github.com/lentago/epigaea/pull/528) — fleet: retire DeepWiki — header badge, README section, footer clause
- 🟣 2026-10-07 · [asclepias#15](https://github.com/lentago/asclepias/pull/15) — fleet: retire DeepWiki — header badge, README section, footer clause, Lab 00
- 🟣 2026-10-07 · [solidago#211](https://github.com/lentago/solidago/pull/211) — fleet: retire DeepWiki — header badge, README section, footer clause, `.mcp.json`
- 🟣 2026-10-07 · [coderabbit#4](https://github.com/lentago/coderabbit/pull/4) — fleet: retire DeepWiki — footer clause
- 🟣 2026-10-07 · [site-lentago-dev#96](https://github.com/lentago/site-lentago-dev/pull/96) — fleet: retire DeepWiki — header badge, README section, footer clause
- 🟣 2026-10-07 · [kalmia#138](https://github.com/lentago/kalmia/pull/138) — fleet: retire DeepWiki — header badge, README section, footer clause
- 🟣 2026-10-07 · [mitchella#22](https://github.com/lentago/mitchella/pull/22) — fleet: retire DeepWiki — header badge
- 🟣 2026-10-07 · [music-curator#93](https://github.com/lentago/music-curator/pull/93) — fleet: retire DeepWiki — header badge, README section, footer clause
- 🟣 2026-10-07 · [repo-template#24](https://github.com/lentago/repo-template/pull/24) — fleet: retire DeepWiki — header badge, README section, footer clause
- 🟣 2026-10-07 · [shared-workflows#66](https://github.com/lentago/shared-workflows/pull/66) — fleet: retire DeepWiki — header badge, README section, footer clause
- 🟣 2026-10-07 · [osmunda#9](https://github.com/lentago/osmunda/pull/9) — fleet: retire DeepWiki — header badge, README section, footer clause
- 🟣 2026-10-07 · [monarda#14](https://github.com/lentago/monarda/pull/14) — fleet: retire DeepWiki — header badge, footer clause
- 🟣 2026-10-07 · [drosera#249](https://github.com/lentago/drosera/pull/249) — fleet: retire DeepWiki — header badge, README section, footer clause
- 🟣 2026-10-07 · [betula#127](https://github.com/lentago/betula/pull/127) — fleet: retire DeepWiki — header badge, README section, footer clause
- 🟣 2026-10-07 · [brasenia#24](https://github.com/lentago/brasenia/pull/24) — fleet: retire DeepWiki — header badge, README section, footer clause
- 🟣 2026-10-07 · [.github#238](https://github.com/lentago/.github/pull/238) — fleet: retire DeepWiki — generator, footer, profile, homepages, ADR-0010
- 🟢 2026-10-07 · [site-lentago-dev#94](https://github.com/lentago/site-lentago-dev/issues/94) — Offerings grid: uvularia card predates the one-repository first rung
- 🟣 2026-10-07 · [site-lentago-dev#95](https://github.com/lentago/site-lentago-dev/pull/95) — Offerings grid: uvularia card reflects the one-repository first rung
- 🟢 2026-10-07 · [site-lentago-dev#92](https://github.com/lentago/site-lentago-dev/issues/92) — Carry the eight new genus marks; point mark canon at lentago/.github
- 🟣 2026-10-07 · [site-lentago-dev#93](https://github.com/lentago/site-lentago-dev/pull/93) — Carry the eight new genus marks; point mark canon at lentago/.github
- 🟢 2026-10-07 · [epigaea#526](https://github.com/lentago/epigaea/issues/526) — Banner with the epigaea genus mark
- 🟣 2026-10-07 · [epigaea#527](https://github.com/lentago/epigaea/pull/527) — Banner with the epigaea genus mark
- 🟢 2026-10-07 · [asclepias#13](https://github.com/lentago/asclepias/issues/13) — Banner with the asclepias genus mark
- 🟣 2026-10-07 · [asclepias#14](https://github.com/lentago/asclepias/pull/14) — Banner with the asclepias genus mark
- 🟢 2026-10-07 · [lupinus#14](https://github.com/lentago/lupinus/issues/14) — Banner with the lupinus genus mark
- 🟣 2026-10-07 · [lupinus#15](https://github.com/lentago/lupinus/pull/15) — Banner with the lupinus genus mark
- 🟢 2026-10-07 · [uvularia#87](https://github.com/lentago/uvularia/issues/87) — Banner with the uvularia genus mark
- 🟣 2026-10-07 · [uvularia#88](https://github.com/lentago/uvularia/pull/88) — Banner with the uvularia genus mark
- 🟢 2026-10-07 · [osmunda#7](https://github.com/lentago/osmunda/issues/7) — Banner with the osmunda genus mark
- 🟣 2026-10-07 · [osmunda#8](https://github.com/lentago/osmunda/pull/8) — Banner with the osmunda genus mark
- 🟢 2026-10-07 · [brasenia#22](https://github.com/lentago/brasenia/issues/22) — Banner with the brasenia genus mark
- 🟣 2026-10-07 · [brasenia#23](https://github.com/lentago/brasenia/pull/23) — Banner with the brasenia genus mark
- 🟢 2026-10-07 · [mitchella#20](https://github.com/lentago/mitchella/issues/20) — Banner with the mitchella genus mark
- 🟣 2026-10-07 · [mitchella#21](https://github.com/lentago/mitchella/pull/21) — Banner with the mitchella genus mark
- 🟢 2026-10-07 · [monarda#12](https://github.com/lentago/monarda/issues/12) — Banner with the monarda genus mark
- 🟣 2026-10-07 · [monarda#13](https://github.com/lentago/monarda/pull/13) — Banner with the monarda genus mark
- 🟣 2026-10-07 · [.github#236](https://github.com/lentago/.github/pull/236) — brand: genus marks for the eight unmarked species
- 🟣 2026-10-07 · [uvularia#86](https://github.com/lentago/uvularia/pull/86) — Revert Dependabot template directories (workflows are scanned at the root only)
- 🟣 2026-10-07 · [uvularia#82](https://github.com/lentago/uvularia/pull/82) — Dependabot: scan the templates' GitHub Actions pins
- 🟣 2026-10-07 · [uvularia-demo-site#6](https://github.com/lentago/uvularia-demo-site/pull/6) — ci: SHA-pin third-party actions (hand-sync from uvularia-site-template)
- 🟣 2026-10-07 · [uvularia-demo-ask-rules#15](https://github.com/lentago/uvularia-demo-ask-rules/pull/15) — ci: SHA-pin third-party actions (hand-sync from uvularia-rules-template)
- 🟣 2026-10-07 · [uvularia-demo-records#20](https://github.com/lentago/uvularia-demo-records/pull/20) — ci: SHA-pin third-party actions (hand-sync from uvularia-records-template)
- 🟣 2026-10-07 · [uvularia-records-template#13](https://github.com/lentago/uvularia-records-template/pull/13) — Sync from lentago/uvularia@3364e23
- 🟣 2026-10-07 · [epigaea#525](https://github.com/lentago/epigaea/pull/525) — One shellcheck gate: shared caller at style severity, inline job removed
- 🟣 2026-10-07 · [uvularia-rules-template#9](https://github.com/lentago/uvularia-rules-template/pull/9) — Sync from lentago/uvularia@3364e23
- 🟣 2026-10-07 · [claytonia#134](https://github.com/lentago/claytonia/pull/134) — Move remaining shared-workflows pins to v1.2.3
- 🟣 2026-10-07 · [uvularia-site-template#7](https://github.com/lentago/uvularia-site-template/pull/7) — Sync from lentago/uvularia@3364e23
- 🟣 2026-10-07 · [uvularia#80](https://github.com/lentago/uvularia/pull/80) — ci: SHA-pin third-party actions in templates and own workflows
- 🟣 2026-10-07 · [drosera#248](https://github.com/lentago/drosera/pull/248) — Move remaining shared-workflows pins to v1.2.3
- 🟣 2026-10-07 · [kalmia#137](https://github.com/lentago/kalmia/pull/137) — Move remaining shared-workflows pins to v1.2.3
- 🟣 2026-10-07 · [site-icecreamtofightwith-com#197](https://github.com/lentago/site-icecreamtofightwith-com/pull/197) — Move remaining shared-workflows pins to v1.2.3
- 🟣 2026-10-07 · [site-pondviewlane-com#84](https://github.com/lentago/site-pondviewlane-com/pull/84) — Move remaining shared-workflows pins to v1.2.3
- 🟣 2026-10-07 · [solidago#210](https://github.com/lentago/solidago/pull/210) — Move remaining shared-workflows pins to v1.2.3
- 🟣 2026-10-07 · [betula#125](https://github.com/lentago/betula/pull/125) — Move remaining shared-workflows pins to v1.2.3
- 🟣 2026-10-07 · [site-lentago-dev#91](https://github.com/lentago/site-lentago-dev/pull/91) — Move remaining shared-workflows pins to v1.2.3
- 🟣 2026-10-07 · [.github#233](https://github.com/lentago/.github/pull/233) — Move remaining shared-workflows pins to v1.2.3
- 🟢 2026-10-06 · [shared-workflows#64](https://github.com/lentago/shared-workflows/issues/64) — ADR-0005 migration: move the remaining @main callers to v1.2.3
- 🟣 2026-10-06 · [repo-template#23](https://github.com/lentago/repo-template/pull/23) — Retire the dispatch-only claude-code-review stub
- 🟣 2026-10-06 · [site-lentago-dev#90](https://github.com/lentago/site-lentago-dev/pull/90) — Retire the dispatch-only claude-code-review stub
- 🟣 2026-10-06 · [.github#232](https://github.com/lentago/.github/pull/232) — Require shellcheck on the seven repos that just gained a caller
- 🟣 2026-10-06 · [uvularia#79](https://github.com/lentago/uvularia/pull/79) — Retire the dispatch-only claude-code-review stub
- 🟣 2026-10-06 · [music-curator#92](https://github.com/lentago/music-curator/pull/92) — Retire the dispatch-only claude-code-review stub
- 🟣 2026-10-06 · [uvularia-demo-ask-rules#14](https://github.com/lentago/uvularia-demo-ask-rules/pull/14) — Vendor the loki-event action; drop the lentago/drosera@main dependency
- 🟣 2026-10-06 · [uvularia-demo-records#19](https://github.com/lentago/uvularia-demo-records/pull/19) — Vendor the loki-event action; drop the lentago/drosera@main dependency
- 🟣 2026-10-06 · [epigaea#524](https://github.com/lentago/epigaea/pull/524) — CLAUDE.md: required checks match the live ruleset
- 🟣 2026-10-06 · [betula#124](https://github.com/lentago/betula/pull/124) — CLAUDE.md CI section: match the live required checks
- 🟣 2026-10-06 · [uvularia-site-template#6](https://github.com/lentago/uvularia-site-template/pull/6) — Sync from lentago/uvularia@df4a41e
- 🟣 2026-10-06 · [uvularia-rules-template#8](https://github.com/lentago/uvularia-rules-template/pull/8) — Sync from lentago/uvularia@df4a41e
- 🟣 2026-10-06 · [mitchella#18](https://github.com/lentago/mitchella/pull/18) — Add Dependabot for GitHub Actions and pip
- 🟣 2026-10-06 · [uvularia-records-template#12](https://github.com/lentago/uvularia-records-template/pull/12) — Sync from lentago/uvularia@df4a41e
- 🟣 2026-10-06 · [coderabbit#2](https://github.com/lentago/coderabbit/pull/2) — Add Dependabot and CODEOWNERS, SHA-pin validate's actions, pin docs-check to v1.2.3
- 🟢 2026-10-06 · [.github#229](https://github.com/lentago/.github/issues/229) — Fleet alignment 2026-10-06: stale repos.json facts and ready-to-require checks
- 🟣 2026-10-06 · [.github#230](https://github.com/lentago/.github/pull/230) — Fleet alignment 2026-10-06: stale repos.json facts and ready-to-require checks
- 🟣 2026-10-06 · [shared-workflows#65](https://github.com/lentago/shared-workflows/pull/65) — Enforced-surfaces table: every org repo (27), not 15
- 🟣 2026-10-06 · [uvularia#78](https://github.com/lentago/uvularia/pull/78) — Pin shared-workflows to v1.2.3, add ShellCheck, vendor loki-event into the templates
- 🟣 2026-10-06 · [claytonia#133](https://github.com/lentago/claytonia/pull/133) — Pin shared workflows to v1.2.3 (ADR-0005)
- 🟣 2026-10-06 · [solidago#209](https://github.com/lentago/solidago/pull/209) — Pin shared workflows to v1.2.3 (ADR-0005)
- 🟣 2026-10-06 · [.github#231](https://github.com/lentago/.github/pull/231) — Pin shared workflows to v1.2.3 (ADR-0005)
- 🟣 2026-10-06 · [epigaea#523](https://github.com/lentago/epigaea/pull/523) — Pin shared workflows to v1.2.3 (ADR-0005)
- 🟣 2026-10-06 · [repo-template#22](https://github.com/lentago/repo-template/pull/22) — Pin shared workflows to v1.2.3 (ADR-0005)
- 🟣 2026-10-06 · [site-pondviewlane-com#83](https://github.com/lentago/site-pondviewlane-com/pull/83) — Pin shared workflows to v1.2.3 (ADR-0005)
- 🟣 2026-10-06 · [site-lentago-dev#89](https://github.com/lentago/site-lentago-dev/pull/89) — Pin shared workflows to v1.2.3 (ADR-0005)
- 🟣 2026-10-06 · [drosera#247](https://github.com/lentago/drosera/pull/247) — Pin shared workflows to v1.2.3 (ADR-0005)
- 🟣 2026-10-06 · [kalmia#136](https://github.com/lentago/kalmia/pull/136) — Pin shared workflows to v1.2.3 (ADR-0005)
- 🟣 2026-10-06 · [site-icecreamtofightwith-com#196](https://github.com/lentago/site-icecreamtofightwith-com/pull/196) — Pin shared workflows to v1.2.3 (ADR-0005)
- 🟣 2026-10-06 · [asclepias#12](https://github.com/lentago/asclepias/pull/12) — Pin shared workflows to v1.2.3 (ADR-0005)
- 🟣 2026-10-06 · [osmunda#6](https://github.com/lentago/osmunda/pull/6) — Pin shared workflows to v1.2.3 (ADR-0005)
- 🟣 2026-10-06 · [music-curator#91](https://github.com/lentago/music-curator/pull/91) — Pin shared workflows to v1.2.3 (ADR-0005)
- 🟣 2026-10-06 · [brasenia#21](https://github.com/lentago/brasenia/pull/21) — Pin shared workflows to v1.2.3 (ADR-0005)
- 🟣 2026-10-06 · [betula#123](https://github.com/lentago/betula/pull/123) — Pin shared workflows to v1.2.3 (ADR-0005)
- 🟢 2026-10-06 · [betula#121](https://github.com/lentago/betula/issues/121) — Require gate and tf-lint now that betula carries Terraform
- 🟣 2026-10-06 · [.github#228](https://github.com/lentago/.github/pull/228) — Require gate and tf-lint now that betula carries Terraform
- 🟣 2026-10-06 · [betula#122](https://github.com/lentago/betula/pull/122) — Require gate and tf-lint now that betula carries Terraform
- 🟢 2026-10-06 · [shared-workflows#62](https://github.com/lentago/shared-workflows/issues/62) — Add Axiom datasets and Firewalla on-box config to the enforced-surfaces table
- 🟣 2026-10-06 · [shared-workflows#63](https://github.com/lentago/shared-workflows/pull/63) — Add Axiom datasets and Firewalla on-box config to the enforced-surfaces table
- 🟢 2026-10-06 · [betula#118](https://github.com/lentago/betula/issues/118) — Terraform the Axiom side: datasets, retention, ingest tokens
- 🟣 2026-10-06 · [betula#120](https://github.com/lentago/betula/pull/120) — Terraform the Axiom side: datasets, retention, ingest tokens
- 🟢 2026-10-06 · [solidago#207](https://github.com/lentago/solidago/issues/207) — OIDC role for betula's Terraform state (betula/terraform.tfstate)
- 🟣 2026-10-06 · [solidago#208](https://github.com/lentago/solidago/pull/208) — OIDC role for betula's Terraform state (betula/terraform.tfstate)
- 🟢 2026-10-05 · [drosera#243](https://github.com/lentago/drosera/issues/243) — Retire drosera's device-inventory publisher after the betula move; decide its egress path (ADR-0006)
- 🟣 2026-10-05 · [drosera#246](https://github.com/lentago/drosera/pull/246) — Retire drosera's device-inventory publisher after the betula move; decide its egress path (ADR-0006)
- 🟣 2026-10-05 · [betula#117](https://github.com/lentago/betula/pull/117) — Push device inventory direct to Grafana Cloud Loki
- 🟢 2026-10-05 · [drosera#238](https://github.com/lentago/drosera/issues/238) — Transient Grafana Cloud query errors page as critical DatasourceError — use KeepLast on paging groups
- 🟣 2026-10-05 · [drosera#241](https://github.com/lentago/drosera/pull/241) — Transient Grafana Cloud query errors page as critical DatasourceError — use KeepLast on paging groups
- 🟢 2026-10-05 · [betula#115](https://github.com/lentago/betula/issues/115) — Own the Firewalla device-inventory publisher as a betula collector
- 🟣 2026-10-05 · [betula#116](https://github.com/lentago/betula/pull/116) — Own the Firewalla device-inventory publisher as a betula collector
- 🟢 2026-10-05 · [drosera#151](https://github.com/lentago/drosera/issues/151) — device-inventory publisher: cron reinstall hook failed silently — root-cause and make the schedule survivable/verifiable
- 🟣 2026-10-05 · [drosera#244](https://github.com/lentago/drosera/pull/244) — Retire drosera's device-inventory publisher after the betula move
- 🟢 2026-10-05 · [drosera#239](https://github.com/lentago/drosera/issues/239) — Billable metric series ~26k vs 10k free-tier cap — 15s node cadence bills ~4 DPM per series
- 🟣 2026-10-05 · [drosera#245](https://github.com/lentago/drosera/pull/245) — Billable metric series ~26k vs 10k free-tier cap — 15s node cadence bills ~4 DPM per series
- 🟢 2026-10-05 · [drosera#237](https://github.com/lentago/drosera/issues/237) — Uvularia stale-digest alert flaps between heartbeat runs while digest is current
- 🟣 2026-10-05 · [drosera#240](https://github.com/lentago/drosera/pull/240) — Uvularia stale-digest alert flaps between heartbeat runs while digest is current
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

---

## Code census

**The lens:** a `CLAUDE.md` (and its kin — `AGENTS.md`, skill `SKILL.md`, and the LLM prompt-programs that *are* a tool's logic) is an instruction set maintained for hygiene, so it's counted as **natural-language code**. Documentation, content/data, and community-health markdown are tallied separately and excluded from the code total, as are data payloads and generated files. This is a deliberate re-cut of the canonical [`metrics/language-census.md`](../metrics/language-census.md), which instead counts all Markdown/JSON/HTML as code.

### Languages

cloc *code* lines (blank + comment excluded). Shell folds Bourne + Bash. Instruction-markdown is promoted into the count (**bold**); the excluded buckets sit below the total.

| # | Language | Code | Files | Share |
|---|----------|-----:|------:|------:|
| 1 | JSON | 47,814 | 474 | 35.6% |
| 2 | Python | 34,243 | 242 | 25.5% |
| 3 | YAML | 16,679 | 299 | 12.4% |
| 4 | HCL | 8,877 | 137 | 6.6% |
| 5 | Shell (Bourne + Bash) | 6,159 | 86 | 4.6% |
| 6 | JavaScript | 4,848 | 56 | 3.6% |
| 7 | Text | 4,817 | 231 | 3.6% |
| 8 | Astro | 3,831 | 51 | 2.9% |
| 9 | **Instructions (CLAUDE.md family + prompt-programs)** | 2,497 | 21 | 1.9% |
| 10 | CSS | 1,402 | 10 | 1.0% |
| 11 | JSX | 1,046 | 12 | 0.8% |
| 12 | TypeScript | 682 | 35 | 0.5% |
| 13 | Jinja Template | 611 | 18 | 0.5% |
| 14 | HTML | 340 | 3 | 0.3% |
| 15 | TOML | 193 | 13 | 0.1% |
| 16 | XML | 129 | 5 | 0.1% |
| 17 | Other (TOML / Dockerfile / …) | 30 | 4 | 0.0% |
| | **CODE TOTAL** | **134,198** | **1697** | 100% |
| — | _Data / exports — excluded_ | 119,165 | 9 | — |
| — | _Generated (lockfiles, SVG, brand artefacts) — excluded_ | 52,658 | 134 | — |

### Instruction-markdown as code

- **Hygiene family** (21 files · `CLAUDE.md`, `AGENTS.md`, `SKILL.md`): **2,497 lines**
- **Prompt-programs** (0 files · reference-checker auditors): **0 lines**

#### Hygiene surface — each file is a maintenance obligation

| Repo | File | Lines |
|------|------|------:|
| epigaea | `CLAUDE.md` | 406 |
| shared-workflows | `CLAUDE.md` | 241 |
| site-pondviewlane-com | `CLAUDE.md` | 224 |
| .github | `CLAUDE.md` | 223 |
| betula | `CLAUDE.md` | 185 |
| kalmia | `CLAUDE.md` | 155 |
| site-lentago-dev | `CLAUDE.md` | 108 |
| solidago | `CLAUDE.md` | 99 |
| drosera | `CLAUDE.md` | 98 |
| site-icecreamtofightwith-com | `CLAUDE.md` | 98 |
| uvularia | `CLAUDE.md` | 79 |
| lupinus | `CLAUDE.md` | 73 |
| asclepias | `CLAUDE.md` | 70 |
| drosera | `AGENTS.md` | 68 |
| music-curator | `CLAUDE.md` | 68 |
| mitchella | `CLAUDE.md` | 62 |
| brasenia | `CLAUDE.md` | 58 |
| claytonia | `CLAUDE.md` | 57 |
| osmunda | `CLAUDE.md` | 53 |
| monarda | `CLAUDE.md` | 50 |
| repo-template | `CLAUDE.md` | 22 |
| **21 files** | | **2,497** |

### Per-repo

| Repo | Code | Instr | Doc-md | Content-md | Data |
|------|-----:|------:|-------:|-----------:|-----:|
| epigaea | 23,996 | 406 | 1,544 | 0 | 0 |
| drosera | 22,010 | 166 | 2,623 | 0 | 0 |
| uvularia | 16,773 | 79 | 6,176 | 0 | 0 |
| uvularia-demo-records | 7,882 | 0 | 3,675 | 0 | 0 |
| site-pondviewlane-com | 7,438 | 224 | 2,898 | 0 | 0 |
| solidago | 7,190 | 99 | 2,650 | 0 | 0 |
| music-curator | 5,629 | 68 | 1,247 | 12,754 | 119,165 |
| uvularia-records-template | 5,242 | 0 | 865 | 0 | 0 |
| .github | 4,000 | 223 | 2,335 | 3,518 | 0 |
| kalmia | 3,998 | 155 | 1,590 | 0 | 0 |
| mitchella | 3,659 | 62 | 725 | 0 | 0 |
| betula | 3,477 | 185 | 1,851 | 0 | 0 |
| site-icecreamtofightwith-com | 3,463 | 98 | 893 | 6,004 | 0 |
| brasenia | 3,342 | 58 | 2,074 | 0 | 0 |
| uvularia-demo-ask-rules | 2,930 | 0 | 424 | 0 | 0 |
| site-lentago-dev | 2,810 | 108 | 671 | 0 | 0 |
| claytonia | 2,076 | 57 | 1,380 | 0 | 0 |
| uvularia-site-template | 2,011 | 0 | 191 | 0 | 0 |
| uvularia-demo-site | 2,009 | 0 | 191 | 0 | 0 |
| shared-workflows | 1,189 | 241 | 773 | 0 | 0 |
| uvularia-rules-template | 1,101 | 0 | 243 | 0 | 0 |
| monarda | 960 | 50 | 647 | 0 | 0 |
| osmunda | 364 | 53 | 454 | 0 | 0 |
| lupinus | 226 | 73 | 1,308 | 0 | 0 |
| coderabbit | 196 | 0 | 38 | 0 | 0 |
| asclepias | 158 | 70 | 735 | 0 | 0 |
| repo-template | 69 | 22 | 271 | 0 | 0 |

### Markdown taxonomy

The fleet carries **63,801 lines of Markdown across 1377 files**; only 3.9% is instruction-code.

| Class | Lines | Files | Disposition |
|-------|------:|------:|-------------|
| **Instructions** | 2,497 | 21 | **counted as code** |
| Content / data | 22,276 | 697 | payload (vault notes, recipes, test-sets) — excluded |
| Documentation | 38,472 | 642 | READMEs, docs, ADRs, runbooks — excluded |
| Community-health | 556 | 17 | CONTRIBUTING/SECURITY/templates — excluded |
| **All Markdown** | **63,801** | **1377** | |

---

## Method

- **Issues:** open issues via `gh search issues --owner lentago --state open`; activity from `gh search prs --owner lentago --merged` and closed issues filtered to the 30-day window. Public metadata only — no transcript harvest, ops items, or homelab detail (those live in the LAN copy).
- **Census tool:** `cloc`, run per-repo as `cloc --by-file --vcs=git` so only git-tracked files count (build output, `node_modules`, `.terraform`, venvs never enter). Lines are cloc *code* lines.
- **Scope:** the active repos owned by the `lentago` org, derived at runtime — personal repos and third-party clones are out of scope; archived repos are frozen and excluded.
- **Markdown classifier:** instruction-code = `CLAUDE.md`/`AGENTS.md`/`SKILL.md` or a versioned `prompts/*-auditor.md`; community-health = governance filenames + issue/PR templates; content = repo-scoped payload paths (music-curator `vault/`, ice-cream `recipes/`·manuscript, reference-checker `test-sets/`·`reports/`, dotgithub `fleet-reports/`); everything else = documentation.
- **Data / generated carve-outs:** exported payloads under the declared data dirs (music-curator `data/`, homeassistant-config `context/`) count as data whatever their serialisation — JSON, JSONL, CSV/TSV, XML, YAML — as does reference-checker's rendered `reports/*.html`; lockfiles, SVG and `.github/brand/generated/` (emitted from `brand/fleet.json`) are generated. drosera's `dashboards/*.json` stay in code as Terraform-enforced dashboards-as-code.
- **Regenerating:** `python3 metrics/generate-fleet-reports.py --out-dir .`

_Generated with Claude Code (Repo Claude)._
