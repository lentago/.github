# Lentago Labs Fleet Report

> [!NOTE]
> **Co-authored with [Claude](https://claude.ai)** (Repo Claude, the Lentago Labs fleet steward). Auto-generated weekly from the fleet's public state (GitHub issues/PRs + `cloc` over public repo contents) — no personal, security, or homelab-internal detail is included. A prettier, editorialised copy renders on the Lentago lab LAN.

**Generated:** 2026-09-28 18:56 UTC · Scope: the **19 active** `lentago` repos (archived repos frozen &amp; excluded) · Activity window: last 30 days (since 2026-08-29).

## Snapshot

| Open issues | PRs merged (30d) | Issues closed (30d) | Code (incl. instructions) | Instruction-markdown |
|---:|---:|---:|---:|---:|
| **109** | 15 | 1 | **81,053** | 2,358 (20 files) |

The fleet's hand-maintained natural-language instruction surface (**2,358 lines** across 20 files) is among the largest "languages" in the code base — `reference-checker` alone is almost entirely prompt-program source.

---

## Open issues — 109 across 17 repos

### .github — 19 open

| # | Title |
|---|-------|
| [187](https://github.com/lentago/.github/issues/187) | [renewal] pondviewlane.com — domain registration — due 2026-11-03 |
| [182](https://github.com/lentago/.github/issues/182) | [renewal] lentago.dev — TLS certificate (ACME auto-renew backstop) — due 2026-09-10 |
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

### claytonia — 13 open

| # | Title |
|---|-------|
| [120](https://github.com/lentago/claytonia/issues/120) | Residual journal chatter: two condition-skipped units re-logged on every timer activation |
| [117](https://github.com/lentago/claytonia/issues/117) | Make never-merge a boundary: required check that blocks runner-App PRs without a human approval |
| [116](https://github.com/lentago/claytonia/issues/116) | Close the loop after the PR opens: a capped follow-up job for failing checks and review comments |
| [115](https://github.com/lentago/claytonia/issues/115) | An eval set for the fleet: replayable tasks, deterministic graders, and outcome measures |
| [114](https://github.com/lentago/claytonia/issues/114) | Bound every job: default turn, spend and wall-clock limits in run-job |
| [110](https://github.com/lentago/claytonia/issues/110) | Ship workers/<host>.alive heartbeats to Loki — unblocks the bullpen liveness alerts |
| [99](https://github.com/lentago/claytonia/issues/99) | Second job type: batch document/report jobs through the queue contract |
| [65](https://github.com/lentago/claytonia/issues/65) | Complete the bullpen → claytonia rename on-host |
| [47](https://github.com/lentago/claytonia/issues/47) | Roadmap: platform-agnostic workers — Claude Code as one runtime behind the queue contract |
| [31](https://github.com/lentago/claytonia/issues/31) | Add optional authentication to the n8n Bullpen job-submit form |
| [24](https://github.com/lentago/claytonia/issues/24) | Branch hygiene across overlapping sessions: clean-desk session-end + prefer fleet dispatch |
| [22](https://github.com/lentago/claytonia/issues/22) | Fleet PR lane separation: rebase-before-merge + dispatch-time overlap check (no two writers on one file/panel) |
| [21](https://github.com/lentago/claytonia/issues/21) | Queue admission control: job ownership, fleet occupancy, and capacity awareness at submit time |

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

**16 events**, one stream, newest first — 🟣 15 PRs merged · 🟢 1 issues closed

- 🟣 2026-09-22 · [drosera#214](https://github.com/lentago/drosera/pull/214) — feat(context-ledger)!: remove ledger alerts + dashboard row (decommissioned)
- 🟣 2026-09-22 · [claytonia#121](https://github.com/lentago/claytonia/pull/121) — feat(context-ledger)!: decommission the context ledger
- 🟣 2026-09-21 · [.github#188](https://github.com/lentago/.github/pull/188) — Weekly fleet reports refresh — 2026-09-21
- 🟢 2026-09-20 · [claytonia#118](https://github.com/lentago/claytonia/issues/118) — Idle workers churn ~130 KiB/s of journald writes each and ~7 SMB req/s against the NAS
- 🟣 2026-09-20 · [claytonia#119](https://github.com/lentago/claytonia/pull/119) — Poll the inbox every 60s and stop journaling per-activation systemd chatter
- 🟣 2026-09-14 · [.github#186](https://github.com/lentago/.github/pull/186) — Weekly fleet reports refresh — 2026-09-14
- 🟣 2026-09-07 · [.github#184](https://github.com/lentago/.github/pull/184) — Weekly fleet reports refresh — 2026-09-07
- 🟣 2026-08-31 · [.github#181](https://github.com/lentago/.github/pull/181) — Weekly fleet reports refresh — 2026-08-31
- 🟣 2026-08-31 · [.github#180](https://github.com/lentago/.github/pull/180) — Refresh language census — 2026-08-30
- 🟣 2026-08-31 · [.github#179](https://github.com/lentago/.github/pull/179) — Weekly fleet reports refresh — 2026-08-31
- 🟣 2026-08-30 · [site-pondviewlane-com#76](https://github.com/lentago/site-pondviewlane-com/pull/76) — essex: vary the escape-hatch link text from a per-page sneer pool
- 🟣 2026-08-30 · [site-pondviewlane-com#75](https://github.com/lentago/site-pondviewlane-com/pull/75) — essex: a footer escape hatch to the plainer sister skin
- 🟣 2026-08-30 · [drosera#212](https://github.com/lentago/drosera/pull/212) — feat(alerts): lab host + Home Assistant availability alerting (2026-08-29 pve3 outage)
- 🟣 2026-08-30 · [site-pondviewlane-com#73](https://github.com/lentago/site-pondviewlane-com/pull/73) — Bump the astro-stack group with 2 updates
- 🟣 2026-08-30 · [site-pondviewlane-com#72](https://github.com/lentago/site-pondviewlane-com/pull/72) — Bump nginx from `8f029c5` to `b34848e`
- 🟣 2026-08-30 · [.github#178](https://github.com/lentago/.github/pull/178) — build(deps): bump github/codeql-action/upload-sarif from 4.37.7 to 4.37.9 in the actions-routine group

---

## Code census

**The lens:** a `CLAUDE.md` (and its kin — `AGENTS.md`, skill `SKILL.md`, and the LLM prompt-programs that *are* a tool's logic) is an instruction set maintained for hygiene, so it's counted as **natural-language code**. Documentation, content/data, and community-health markdown are tallied separately and excluded from the code total, as are data payloads and generated files. This is a deliberate re-cut of the canonical [`metrics/language-census.md`](../metrics/language-census.md), which instead counts all Markdown/JSON/HTML as code.

### Languages

cloc *code* lines (blank + comment excluded). Shell folds Bourne + Bash. Instruction-markdown is promoted into the count (**bold**); the excluded buckets sit below the total.

| # | Language | Code | Files | Share |
|---|----------|-----:|------:|------:|
| 1 | JSON | 34,841 | 54 | 43.0% |
| 2 | YAML | 10,986 | 220 | 13.6% |
| 3 | Python | 9,488 | 70 | 11.7% |
| 4 | HCL | 6,948 | 116 | 8.6% |
| 5 | Shell (Bourne + Bash) | 4,945 | 67 | 6.1% |
| 6 | Text | 3,621 | 27 | 4.5% |
| 7 | **Instructions (CLAUDE.md family + prompt-programs)** | 2,358 | 20 | 2.9% |
| 8 | Astro | 2,280 | 27 | 2.8% |
| 9 | JavaScript | 1,875 | 17 | 2.3% |
| 10 | CSS | 1,402 | 10 | 1.7% |
| 11 | JSX | 1,023 | 12 | 1.3% |
| 12 | Jinja Template | 560 | 15 | 0.7% |
| 13 | TypeScript | 441 | 11 | 0.5% |
| 14 | TOML | 159 | 6 | 0.2% |
| 15 | Other (TOML / Dockerfile / …) | 69 | 5 | 0.1% |
| 16 | HTML | 57 | 1 | 0.1% |
| | **CODE TOTAL** | **81,053** | **678** | 100% |
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
| drosera | 16,726 | 163 | 1,623 | 0 | 0 |
| site-pondviewlane-com | 7,435 | 224 | 2,913 | 0 | 0 |
| solidago | 6,471 | 99 | 2,527 | 0 | 0 |
| music-curator | 5,622 | 68 | 1,254 | 11,645 | 119,165 |
| kalmia | 3,530 | 155 | 1,448 | 0 | 0 |
| site-icecreamtofightwith-com | 3,491 | 98 | 897 | 6,004 | 0 |
| .github | 3,418 | 218 | 1,559 | 3,265 | 0 |
| claytonia | 1,951 | 57 | 1,320 | 0 | 0 |
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

The fleet carries **46,793 lines of Markdown across 1023 files**; only 5.0% is instruction-code.

| Class | Lines | Files | Disposition |
|-------|------:|------:|-------------|
| **Instructions** | 2,358 | 20 | **counted as code** |
| Content / data | 20,914 | 697 | payload (vault notes, recipes, test-sets) — excluded |
| Documentation | 23,076 | 290 | READMEs, docs, ADRs, runbooks — excluded |
| Community-health | 445 | 16 | CONTRIBUTING/SECURITY/templates — excluded |
| **All Markdown** | **46,793** | **1023** | |

---

## Method

- **Issues:** open issues via `gh search issues --owner lentago --state open`; activity from `gh search prs --owner lentago --merged` and closed issues filtered to the 30-day window. Public metadata only — no transcript harvest, ops items, or homelab detail (those live in the LAN copy).
- **Census tool:** `cloc`, run per-repo as `cloc --by-file --vcs=git` so only git-tracked files count (build output, `node_modules`, `.terraform`, venvs never enter). Lines are cloc *code* lines.
- **Scope:** the active repos owned by the `lentago` org, derived at runtime — personal repos and third-party clones are out of scope; archived repos are frozen and excluded.
- **Markdown classifier:** instruction-code = `CLAUDE.md`/`AGENTS.md`/`SKILL.md` or a versioned `prompts/*-auditor.md`; community-health = governance filenames + issue/PR templates; content = repo-scoped payload paths (music-curator `vault/`, ice-cream `recipes/`·manuscript, reference-checker `test-sets/`·`reports/`, dotgithub `fleet-reports/`); everything else = documentation.
- **Data / generated carve-outs:** exported payloads under the declared data dirs (music-curator `data/`, homeassistant-config `context/`) count as data whatever their serialisation — JSON, JSONL, CSV/TSV, XML, YAML — as does reference-checker's rendered `reports/*.html`; lockfiles, SVG and `.github/brand/generated/` (emitted from `brand/fleet.json`) are generated. drosera's `dashboards/*.json` stay in code as Terraform-enforced dashboards-as-code.
- **Regenerating:** `python3 metrics/generate-fleet-reports.py --out-dir .`

_Generated with Claude Code (Repo Claude)._
