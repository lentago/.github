# Lentago Labs Fleet — Issue Report & Thread Harvest

> [!NOTE]
> **Co-authored with [Claude](https://claude.ai)** (Repo Claude, the Lentago Labs fleet steward). Published archive of a living operational report; the canonical live copy renders on the Lentago lab LAN. A few personal/security details present in the LAN copy are redacted here (noted inline).

**2026-07-01** · Repo Claude (fleet steward) · **refreshed 2026-07-10 13:50 EDT** (original 07-01 10:44 · prior refreshes 07-01 17:55 / 18:05 / 18:20 / 19:40 · 07-02 09:35 · 07-04 09:05)

Scope: all 16 `lentago` repos + one personal repo, plus a 14-day harvest of local Claude Code session transcripts.

| Open issues | New issues filed (AM 07-01) | Closed since AM report | PRs merged 07-01 | Filed → closed by next morning |
|---|---|---|---|---|
| 39→55→36→28→25→38 | 16 | 30 | 28 | 12/16 |

> **2026-07-10 13:50 EDT — six-day delta (07-04 → 07-10): 25 → 38 open, 100+ PRs merged, 43 issues closed, 27 filed.** The fleet is back to within one of the original 39 — but the composition is entirely different: the March backlogs are gone; today's open set is suite roadmaps, governance, and fresh work.

> - **The botanical rename wave (07-04):** four product repos took Lentago suite codenames — bullpen → `claytonia`, homelab-observability → `drosera`, firewalla-axiom-pipeline → `betula`, workstation-ansible → `kalmia` — and site repos moved to the `site-<domain>` convention (`site-lentago-dev`, `site-icecreamtofightwith-com`, `site-pitzilabs-dev`). Four suite-agnosticism roadmap issues filed and open (betula#74, drosera#131, claytonia#47, kalmia#20). Part 1 tables keep the old names as morning-snapshot labels.

> - **kalmia put the whole Proxmox guest layer under Terraform (07-05):** phases 0–3 in one day — all 12 guests imported (HAOS VM 100 last, with `prevent_destroy`), LAN self-hosted runner + apply-on-merge, CA pinned. The bullpen then **scaled to 5 workers** (LXC 116/117, 07-06), and runner-pool ownership moved kalmia → claytonia (07-07) with the kalmia image forge cutting `claytonia-runner-v1` as the first versioned image artifact.

> - **Required status checks are now fleet-enforced** (.github#27, 07-07): rulesets carry required checks, terraform repos use an always-on `gate` job, music-curator#9 closed the last gap (07-09). Follow-up open: [.github#28](https://github.com/lentago/.github/issues/28).

> - **solidago:** Grafana CloudWatch Phase 1 + ECS-logs-to-Axiom Phase 2 shipped (07-04); the `foundry-*` → `solidago-*` AWS resource + tfstate backend migration landed 07-08 with downstream fixes across six repos (two doc stragglers open: site-lentago-dev#36, .github#31); the **ALB visitor-telemetry chain** shipped 07-09/10 (solidago#106/#108 + betula#80 AWS collector, a CI `lambda:*` unblock #110, and betula#84 parser fix — all same-day). And **solidago#80 is done (07-10):** the billable pitzilabs preview site is torn down (PRs #114/#116).

> - **betula architecture pivot (07-10):** Axiom retired as an output — **Grafana Cloud Loki is now the sole pipeline** ([PR #82](https://github.com/lentago/betula/pull/82)); [#83](https://github.com/lentago/betula/issues/83) (architecture.svg refresh) tracks the doc catch-up.

> - **music-curator productized** into an Obsidian wiki-manager (07-08/09): twelve PRs — graph-vault driver, two-tier genre taxonomy, personnel-credit edges, switchable graph presets.

> - **site-lentago-dev content wave (07-06):** genus marks per system row, OG/social meta, Formspree consult form, anchor cleanup. The ice-cream site's punk-zine redesign was merged and *reverted the same day*.

> - **New bug open:** [drosera#145](https://github.com/lentago/drosera/issues/145) — the gitops loop can't recover a crashed Alloy (validator runs inside the down container).

> - **Standing flag, third refresh running:** [claytonia#31](https://github.com/lentago/claytonia/issues/31) (n8n form auth, née bullpen#31) — still open, still obsolete post-form-retirement; recommend close not-planned.

> **2026-07-04 09:05 EDT — two-day delta (07-02 → 07-04): 28 → 25 open, 49 PRs merged, two rename waves.**

> - **foundry-platform-demo is now `solidago`** (renamed 07-03, first service-catalog codename; AWS `foundry-*` resource names unchanged). Its 5 open issues (#18–#21, #80) carry over; a reference sweep updated 7 sibling repos (07-03 eve). The Part 1 table below keeps the old name as the morning-snapshot label.

> - **PitziLabs → lentago reconciliation swept the fleet**: Grafana stack URL/datasources, runner-App name, org URLs, architecture diagrams — and the **NAS share itself renamed** (`/mnt/PitziLabs` → `/mnt/lentago`; bullpen [PR #40](https://github.com/lentago/bullpen/pull/40) + homeassistant-config #499 chased the paths).

> - **firewalla-axiom-pipeline 9 → 5 open**: four aged March items closed (#4, #5, #10, #13), plus a same-day filed-and-fixed cycle of four fresh bugs — #61 healthcheck false positive, #63 host/Zeek metrics, #65 restart loop, and **#67 CRITICAL** (crontab install was clobbering Firewalla's system cron; fixed by [PR #68](https://github.com/lentago/firewalla-axiom-pipeline/pull/68)).

> - **homelab-observability dashboard blitz (07-03)**: six issues (#108–#113) filed and fixed the same afternoon (PRs #114–#118, #121, #122 — table fields, blank panels, legends, device-inventory joins). [PR #119](https://github.com/lentago/homelab-observability/pull/119) restored the infra-health revamp lost to the **IaC drift stomp**, and the anti-drift rule is now codified fleet-wide (homelab-obs #120 + shared-workflows #16). One new open: [#103](https://github.com/lentago/homelab-observability/issues/103) (Firewalla node_exporter via Alloy).

> - **DeepWiki adopted as the docs layer**: all 16 public repos indexed at [deepwiki.com/lentago](https://deepwiki.com/lentago); *Ask DeepWiki* badges merged onto all 13 active repos (07-03 eve, 13 PRs, zero CI failures; archived three skipped).

> - Also merged, no linked issues: homeassistant-config [#500](https://github.com/lentago/homeassistant-config/pull/500) (live light color on Home cards) + [#501](https://github.com/lentago/homeassistant-config/pull/501) (candle-flicker fire model); lentagolabs-dev #16/#17 dead-link fixes; .github #22 Tidewater recolor.

> - **Standing flag:** [bullpen #31](https://github.com/lentago/bullpen/issues/31) (n8n form auth) remains open and still looks obsolete post-form-retirement — recommend close not-planned.

> **Refreshed 2026-07-01 17:55 EDT.** Since the morning report: **14 issues closed** (13 completed, 1 not-planned), **1 new issue** filed, **20 PRs merged** across the org — including the **lentago.dev go-live** . Closed rows below are kept, struck through, so the morning snapshot stays legible. Details in the [refresh delta](#delta) .

> **Evening update 18:05 EDT — two repos retired.** `pitzilabs-dev` and `workstation-bootstrap` are now **archived** (superseded by `lentagolabs-dev` and `workstation-ansible` ). Their open issues were resolved first: pitzilabs-dev #17 closed (decision made) and #8 closed not-planned; workstation-bootstrap #70 closed (decision made) and #72 **transferred** to [homelab-observability #101](https://github.com/lentago/homelab-observability/issues/101) . The live `claude-cost-export/` tooling was rehomed via [homelab-observability PR #102](https://github.com/lentago/homelab-observability/pull/102) (merged 18:05). [lentagolabs-dev #10](https://github.com/lentago/lentagolabs-dev/issues/10) (go-live) closed — the site is live. One new issue: [foundry #80](https://github.com/lentago/foundry-platform-demo/issues/80) to tear down the still-running (billable) `module.site_pitzilabs` preview deployment. Fleet total: **39 open** — back exactly where the morning started, with 16 threads tracked-and-burned in between.

> **2026-07-02 09:35 EDT — overnight burn-down: 36 → 28 open; homeassistant-config hits zero.** The three medium HA dashboard issues went through the bullpen (dispatched 19:49, all three jobs terminal by 21:05): **#432** closed via [PR #496](https://github.com/lentago/homeassistant-config/pull/496) (master/two-clone scheme docs, opus), **#434** via [PR #497](https://github.com/lentago/homeassistant-config/pull/497) (media tiles pinned to fixed height; the Codesign Sync gate needed a mirror regen pushed by the local steward), and **#433** found **already implemented** by PR #449 (merged 06-17, same day it was filed) — the worker correctly opened no PR; verified and closed this morning. **#332** (basement-kitchen ZHA door) also closed completed at 19:48 — **homeassistant-config is at 0 open for the first time** . Elsewhere: three more foundry March-backlog items landed ( [#81](https://github.com/lentago/foundry-platform-demo/pull/81) / [#82](https://github.com/lentago/foundry-platform-demo/pull/82) / [#83](https://github.com/lentago/foundry-platform-demo/pull/83) closing #16/#12/#17); [lentagolabs-dev PR #15](https://github.com/lentago/lentagolabs-dev/pull/15) merged 19:42, closing #11 (the in-flight branch from the 19:40 note landed); and bullpen filed *and* fixed **#37** (failed jobs are silent → [PR #38](https://github.com/lentago/bullpen/pull/38) now comments on the originating issue when a project job fails) in 18 minutes. **One flag:** [bullpen #31](https://github.com/lentago/bullpen/issues/31) (n8n form auth) is **likely obsolete** — the n8n submit-form deployment was retired 07-01 ( [PR #36](https://github.com/lentago/bullpen/pull/36) tombstones it as a redeployable recipe); recommend closing not-planned.

> **19:40 EDT — verification pass; fleet steady at 36 open.** All 36 rows below re-verified against live GitHub — no drift, no new issues, no closures since 18:20. Two updates: **(1)** [homelab-observability PR #102](https://github.com/lentago/homelab-observability/pull/102) (claude-cost-export rehome) confirmed **merged** . **(2)** One item is **in flight** : Chris dispatched [lentagolabs-dev #11](https://github.com/lentago/lentagolabs-dev/issues/11) (footer wordmark) to the Claude GitHub App at 19:09; the fix branch `claude/issue-11-20260701-2309` is pushed, but the app stopped short of opening a PR — it needs a [PR opened](https://github.com/lentago/lentagolabs-dev/compare/main...claude/issue-11-20260701-2309?quick_pull=1) + auto-merge armed to land. The org-avatar manual upload (below) also still remains.

> **18:20 EDT — .github cleared.** All three org-meta issues closed via PRs [#19](https://github.com/lentago/.github/pull/19) (limestone on-dark blossom variant added + deep-teal chip settled as the canonical avatar), [#20](https://github.com/lentago/.github/pull/20) (AWS / ECS Fargate / CloudWatch badges get neutral copper data-URI glyphs — simple-icons dropped the Amazon marks), and [#21](https://github.com/lentago/.github/pull/21) (org-default `CONTRIBUTING` / `SECURITY` / `CODE_OF_CONDUCT` seeded — decision: yes). Fleet total: **36 open** . **One manual step remains:** upload `brand/avatars/lentago-mark-512.png` at Org Settings → Profile — the rendered org avatar still shows the retired benchmark-disk mark (no API for this).

## Executive summary

- **Refresh (17:55):** the fleet burned down a quarter of its backlog in one afternoon — the three `bullpen` High bugs, the `shared-workflows` claude-review bot, three foundry March-backlog items, and 5 of the 16 issues filed this morning are all closed. `lentago.dev` is **live**. See the [delta](#delta) below.

- **Existing open issues:** 39 across 7 of 16 active repos. Two-thirds is an aged March backlog on `foundry-platform-demo` (10) and `firewalla-axiom-pipeline` (10). Live work concentrates in `bullpen` governance (8) and `homeassistant-config` (6). No repo has a stale-critical bug pileup.

- **Harvest:** six parallel agents read the last 14 days of transcripts, extracted genuine still-open threads, and deconflicted against the 39 existing issues and each other.

- **Action taken:** filed **16 new issues** + **2 comments** on existing foundry issues. Fleet total **39 → 55 open**. Six previously-empty repos now carry a tracked backlog.

- **Deliberately not filed:** `professional-endeavors` (in-wiki tracker), `ProxmoxMCP` (third-party clone), and the `pitzilabs-dev` copy fix (blocked behind a retirement decision).

- **Governance gap:** the fleet has **no formal priority-label scheme**. Priorities here are inferred from label semantics + recency.

## Refresh delta — what moved between 10:44 and 17:55

**14 issues closed** (times EDT), almost all via merged PRs:

| Repo | # | Issue | Closed via |
|---|---|---|---|
| bullpen | 8 | cr-submit `-m` flag silently ignored | [PR #33](https://github.com/lentago/bullpen/pull/33) · 11:01 |
| bullpen | 12 | cr-submit `--help`/unknown-flag queues junk job | [PR #34](https://github.com/lentago/bullpen/pull/34) · 12:09 |
| bullpen | 5 | run-job: fail project jobs that open no PR | [PR #35](https://github.com/lentago/bullpen/pull/35) · 12:10 |
| shared-workflows | 14 | claude-review bot fails to post reviews | [PR #15](https://github.com/lentago/shared-workflows/pull/15) (reviewer now advisory/non-blocking) · 11:58 |
| foundry-platform-demo | 13 | `dynamodb_table` → `use_lockfile` | [PR #74](https://github.com/lentago/foundry-platform-demo/pull/74) · 11:09 |
| foundry-platform-demo | 15 | State bucket AES256 → KMS CMK | [PR #75](https://github.com/lentago/foundry-platform-demo/pull/75) · 12:25 |
| foundry-platform-demo | 14 | Selective teardown/standup scripts | [PR #76](https://github.com/lentago/foundry-platform-demo/pull/76) (incl. the runbook edges from this morning's comment) · 13:07 |
| firewalla-axiom-pipeline | 6 | Harden deploy.sh for idempotent re-runs | [PR #56](https://github.com/lentago/firewalla-axiom-pipeline/pull/56) · 11:08 |
| music-curator | 5 | Data-integrity drift in flagship profile | [PR #6](https://github.com/lentago/music-curator/pull/6) · 11:10 |
| music-curator | 4 | JSON Schema + validator engineering spine | [PR #7](https://github.com/lentago/music-curator/pull/7) · 13:00 |
| lentagolabs-dev | 9 | Stale deploy-not-yet-wired CLAUDE.md language | [PR #12](https://github.com/lentago/lentagolabs-dev/pull/12) · 12:57 |
| workstation-bootstrap | 69 | Alacritty hardcoded `/home/cpitzi` path | [PR #71](https://github.com/lentago/workstation-bootstrap/pull/71) · 11:08 |
| homeassistant-config | 376 | Proxmox button orphans | completed · 14:07 |
| homeassistant-config | 450 | home-preview `--url` false-negative abort | **closed not-planned** · 13:58 |

**lentago.dev is live.** Foundry PRs [#77](https://github.com/lentago/foundry-platform-demo/pull/77) (DNS promotion), [#78](https://github.com/lentago/foundry-platform-demo/pull/78) (retire the `lt-preview` host), and [#79](https://github.com/lentago/foundry-platform-demo/pull/79) (Fastmail mail records) merged this afternoon, plus lentagolabs-dev [#13](https://github.com/lentago/lentagolabs-dev/pull/13) (docs: site live) and [#14](https://github.com/lentago/lentagolabs-dev/pull/14) (anther-gold recolor). Issue [lentagolabs-dev #10](https://github.com/lentago/lentagolabs-dev/issues/10) (Phase 2 go-live) was closed as completed at 18:04.

**1 new issue:** workstation-bootstrap #72 — the local `session_running` heartbeat only fires on tool-use hooks, so long tool-less reasoning stretches read as idle on the Fleet dashboard exactly when thinking tokens are burning. *(Transferred at 18:03 to [homelab-observability #101](https://github.com/lentago/homelab-observability/issues/101) ahead of the repo's archival.)*

**Also merged (no linked issue):** homeassistant-config [PR #495](https://github.com/lentago/homeassistant-config/pull/495) dropped the dead basement-kitchen door from House Openings (mitigates still-open #332 at the alarm layer; the ZHA sensor itself remains to fix) · homelab-observability [PR #100](https://github.com/lentago/homelab-observability/pull/100) fleet-dashboard improvements · bullpen [#32](https://github.com/lentago/bullpen/pull/32) pve2 roadmap tombstone (from this morning's Part 4).

**Back to zero backlog:** `music-curator` and `shared-workflows` — both went 0 → filed → fixed → 0 within the day.

## Part 1 — Existing open issues, by project and priority (morning snapshot; rows closed since are struck)

Inferred priority: **High** = `bug`/broken-now **Med** = active enhancement/governance/dashboard **Low** = deferred / aged unlabeled backlog.

### bullpen → renamed **claytonia** 07-04 — 8 open (the 5 governance items + #31 below, plus roadmap #47 and machine-account #49 filed post-snapshot)

| Pri | # | Title |
|---|---|---|
| **Closed** | 8 | ~~cr-submit `-m` flag silently ignored — registry model overrides explicit request `[bug]`~~ |
| **Closed** | 12 | ~~cr-submit `--help`/unknown-flag silently queues a junk ad-hoc job~~ |
| **Closed** | 5 | ~~run-job: fail a project job that should have opened a PR but didn't~~ |
| **Med** | 23 | Enforce no-auto-merge review gate; make 'Open agent PRs' the dispatch gate `[governance]` |
| **Med** | 21 | Queue admission control: ownership, occupancy, capacity at submit time `[governance]` |
| **Med** | 22 | Fleet PR lane separation: rebase-before-merge + overlap check `[governance]` |
| **Med** | 24 | Branch hygiene across overlapping sessions: clean-desk session-end `[governance]` |
| **Med** | 25 | Single 'what is every Claude doing right now' pane `[governance]` |

### homeassistant-config — 0 open (was 6 → 4 → 0 — cleared overnight 07-01/02; first zero-backlog state)

| Pri | # | Title |
|---|---|---|
| **Closed** | 332 | ~~basement_kitchen_door + battery sensor both unavailable `[bug,zha]`~~ alarm layer via PR #495, sensor resolved; closed 19:48 |
| **Closed** | 376 | ~~Proxmox button orphans across haos/pve/pve3 `[bug,config-cleanup]`~~ |
| **Not planned** | 450 | ~~home-preview `--url` aborts on false-negative `which display-show` over SSH `[bug]`~~ |
| **Closed** | 432 | ~~Single-master / two-clone scheme for the Home dashboard `[dashboard]`~~ bullpen (opus) → PR #496, 19:54 |
| **Closed** | 433 | ~~Room-level light controls (on/off + dimmers) on Home dashboard `[dashboard]`~~ already shipped in PR #449 (06-17); verified by bullpen, closed 07-02 09:29 |
| **Closed** | 434 | ~~Stop media now-playing cards collapsing when idle `[dashboard]`~~ bullpen (sonnet) → PR #497, 20:04 |

### firewalla-axiom-pipeline → renamed **betula** 07-04 — 7 open (was 10 → 9 → 5; #4/#5/#10/#13 closed 07-02; roadmap #74 + architecture-doc #83 filed post-snapshot, not in table)

| Pri | # | Title |
|---|---|---|
| **Closed** | 4 | ~~Add support for additional Zeek log types `[enhancement]`~~ 07-02 |
| **Med** | 8 | Resolve remaining "Unknown" devices in group mapping `[enhancement]` |
| **Med** | 9 | Add IPv6-to-device resolution `[enhancement]` |
| **Med** | 15 | Add conn.log bandwidth dashboard `[enhancement,observability]` |
| **Closed** | 10 | ~~Pull-based GitOps deployment `[enhancement]`~~ 07-02 |
| **Med** | 11 | Add New Domain Radar alert `[enhancement]` |
| **Med** | 12 | Terraform the Axiom backend `[enhancement]` |
| **Closed** | 6 | ~~Harden deploy.sh for idempotent re-runs~~ |
| **Closed** | 5 | ~~Rotate health check and cleanup log files~~ 07-02 |
| **Closed** | 13 | ~~Eliminate stale device lookup records in Axiom queries~~ 07-02 |

### foundry-platform-demo → renamed **solidago** 07-03 — 5 open (was 10 → 7 → 5; #12/#16/#17 closed via PRs #81–#83; **#80 preview teardown closed 07-10**; +#97 perpetual-task-def-diff filed 07-05, not in table)

| Pri | # | Title |
|---|---|---|
| **Closed** | 15 | ~~Upgrade state bucket encryption AES256 → KMS CMK *(security)*~~ |
| **Closed** | 13 | ~~Replace deprecated `dynamodb_table` backend param with `use_lockfile`~~ |
| **Closed** | 17 | ~~Upgrade GitHub Actions to Node.js 24-compatible versions~~ PR #83 · 20:13 |
| **Closed** | 14 | ~~Selective teardown/standup scripts for cost management~~ |
| **Closed** | 12 | ~~Standardize Terraform resource naming (`this` vs `main`)~~ PR #82 · 20:12 |
| **Closed** | 16 | ~~Refactor VPC subnets from `count` to `for_each`~~ PR #81 · 20:05 |
| **Low** | 21 | Evaluate ElastiCache node-based → serverless |
| **Low** | 19 | Design multi-domain architecture for portfolio sites |
| **Low** | 18 | Set up local Docker Engine on ChromeOS |
| **Low** | 20 | Document: Phase 2 Secrets Manager secret unused after RDS choice |

### Single-issue repos (homelab-observability → renamed **drosera** 07-04, since grown to 7 open — the 3 below plus #129/#131/#138/#145 filed post-snapshot)

| Repo | Pri | # | Title |
|---|---|---|---|
| homelab-observability | **Med** | 93 | feat(alloy): attach runid label to transcript stream from sidecar `[enhancement]` |
| homelab-observability | **Med** | 101 | Heartbeat blind spot: tool-less reasoning turns show no activity while tokens burn (transferred from workstation-bootstrap #72) |
| homelab-observability | **Med** | 103 | Scrape node_exporter on the Firewalla via Alloy (bring the gateway into node dashboards) filed 07-02 |
| pitzilabs-dev | **Not planned** | 8 | ~~org-README: reconcile voice (team → first-person) before promoting a variant~~ repo archived 18:05 |

### reference-checker — 3 open (all explicitly deferred to v4)

| Pri | # | Title |
|---|---|---|
| **Low** | 10 | [v4] Design batch-pattern detection across submissions `[deferred]` |
| **Low** | 11 | [v4] Implement pipeline decomposition (Opus/Sonnet/Haiku stages) `[deferred]` |
| **Low** | 8 | [v4] Integrate Crossref retraction API `[deferred]` |

**Clean before this harvest (0 open):** `.github` · `workstation-ansible` · `lentagolabs-dev` · `workstation-bootstrap` · `shared-workflows` · `repo-template` · `ice-cream-book` · `music-curator` · `office-presence` (archived) · `cpitzi/professional-endeavors` (personal).

## Part 2 — Harvested threads → issues filed

All 16 created 2026-07-01. Each body carries a one-line provenance note and source session date. Issue numbers link to GitHub. **Refresh:** 5 of the 16 were already fixed and closed by the afternoon (struck below).

| Repo | # | Pri | Title | Source |
|---|---|---|---|---|
| shared-workflows | [14](https://github.com/lentago/shared-workflows/issues/14) | **Closed** | ~~claude-review CI bot fails to post a review across fleet PRs (turn-cap exhaustion + intermittent 0-byte response)~~ | 06-19, 06-21/29 *(2 agents)* |
| bullpen | [31](https://github.com/lentago/claytonia/issues/31) | **Med** | Add optional authentication to the n8n Bullpen job-submit form — ⚠ likely obsolete: the form's reference deployment was retired 07-01 ([PR #36](https://github.com/lentago/claytonia/pull/36)); recommend close not-planned. Now **claytonia#31**; still open as of 07-10 | 06-24 |
| music-curator | [4](https://github.com/lentago/music-curator/issues/4) | **Closed** | ~~Add engineering spine: machine-checkable schema + validator for taste-profile JSON~~ | 06-27 |
| music-curator | [5](https://github.com/lentago/music-curator/issues/5) | **Closed** | ~~Fix data-integrity drift + unmerged duplicate anchors in flagship example profile~~ | 06-27 |
| workstation-ansible | [14](https://github.com/lentago/workstation-ansible/issues/14) | **Med** | Live-test the ubuntu_laptop profile on real ThinkPad hardware | 06-30 |
| workstation-ansible | [15](https://github.com/lentago/workstation-ansible/issues/15) | **Low** | Live-test the crostini profile on the Chromebook penguin container | 06-30 |
| workstation-ansible | [16](https://github.com/lentago/workstation-ansible/issues/16) | **Low-Med** | Harden xubuntu profile for Ubuntu 26.04 (stale comment + Docker CE repo codename) | 06-30 |
| lentagolabs-dev | [9](https://github.com/lentago/lentagolabs-dev/issues/9) | **Closed** | ~~Correct stale deploy-not-yet-wired language in CLAUDE.md~~ | 06-29 |
| lentagolabs-dev | [10](https://github.com/lentago/lentagolabs-dev/issues/10) | **Closed** | ~~Promote the site to lentago.dev (Phase 2 go-live)~~ — live at lentago.dev (foundry PRs #77–79); closed 18:04 | 06-28, 07-01 |
| lentagolabs-dev | [11](https://github.com/lentago/lentagolabs-dev/issues/11) | **Closed** | ~~Scale the footer wordmark to match the enlarged nav lockup~~ — Claude GitHub App branch → [PR #15](https://github.com/lentago/lentagolabs-dev/pull/15), merged 19:42 | 06-29 |
| .github | [16](https://github.com/lentago/.github/issues/16) | **Closed** | ~~Finish the Lentago rebrand of the public org profile (README, banner, avatar)~~ — PR #19, 18:14; avatar upload is a manual step, see banner | 06-29/30, 07-01 |
| .github | [17](https://github.com/lentago/.github/issues/17) | **Closed** | ~~Restore logos on AWS / ECS Fargate / CloudWatch profile badges~~ — PR #20, 18:15 | 06-24 |
| .github | [18](https://github.com/lentago/.github/issues/18) | **Closed** | ~~Decide whether to seed org-default community-health files~~ — decided yes; seeded in PR #21, 18:16 | 06-20 |
| pitzilabs-dev | [17](https://github.com/lentago/pitzilabs-dev/issues/17) | **Closed** | ~~Decide retirement of pitzilabs-dev in favor of lentagolabs-dev~~ — decided: retired & archived 18:05; foundry #80 tracks preview teardown | 06-21, 07-01 |
| workstation-bootstrap | [69](https://github.com/lentago/workstation-bootstrap/issues/69) | **Closed** | ~~Alacritty dotfiles hardcode the absolute path /home/cpitzi~~ | 06-17 |
| workstation-bootstrap | [70](https://github.com/lentago/workstation-bootstrap/issues/70) | **Closed** | ~~Decide disposition now that workstation-ansible reached parity~~ — decided: archived 18:05; claude-cost-export rehomed (homelab-obs PR #102) | 06-29 |

### foundry-platform-demo — comments, not new issues (tightly coupled to existing issues)

- **[#20](https://github.com/lentago/foundry-platform-demo/issues/20)** — the placeholder `db-credentials` secret creates a teardown→rebuild trap (restored on the old, delete-scheduled KMS key → convergence stalls; manual `--force-delete` each cycle). Removing the unused secret (this issue's subject) also kills the trap.

- **[#14](https://github.com/lentago/foundry-platform-demo/issues/14)** — three teardown→standup runbook edges as scope: two-phase Route 53 apply (else ACM validation hangs ~75 min); ECR repos recreated empty → sites 503 until deploys re-triggered; the KMS-secret re-key trap above.

## Part 3 — Deliberately NOT filed

**cpitzi/professional-endeavors** — tracks work in an **in-tree wiki** (`wiki/todos/`, `wiki/questions/`), groomed as recently as 06-30. Filing GitHub issues would fight its convention, and several threads are personal/employer-sensitive. Six in-wiki threads were surfaced and routed to the wiki tracker; *details redacted in this published copy*.

**ProxmoxMCP** — third-party vendored clone (`canvrno/ProxmoxMCP`). SIGABRT-on-shutdown fix lives on local branch `local/sigabrt-shutdown-fix` (commit `e102e46`); `main` kept pristine for upstream fast-forward. Track locally or PR upstream — not fileable in `lentago`.

**pitzilabs-dev stale copy** — "Twenty-five years" in `Experience.jsx:30` + `Layout.astro:13` meta, now wrong against `EST. 1997`. Held behind the retirement decision (pitzilabs-dev #17); file only if the repo is kept.

## Part 4 — Ops action items (not GitHub-fileable)

| Item | Status |
|---|---|
| Runner GitHub App private key on the workstation had an overly-permissive file mode *(path redacted)* | **Resolved** — permissions tightened 2026-07-01 |
| Stale world-readable local config backups possibly holding OAuth/MCP tokens *(paths redacted)* | **Cleared** 2026-07-01 — all removed; live config intact |
| Claude Desktop: leave idle vs `apt purge` (~970 MB) | **Purged** 2026-07-01 — package + `~/.config/Claude` userData removed (~990 MB reclaimed) |
| Stale retired-pve2 wall-display/kiosk references | **Fixed** 2026-07-01 — [bullpen PR #32](https://github.com/lentago/bullpen/pull/32) **merged 10:43**; other repos' pve2 refs verified accurate (tombstones / live node / live office-display) — no change needed |

## Part 5 — Doc-hygiene fix applied

`~/repos/CLAUDE.md` inventory snapshot corrected (2026-07-01):

- Removed the stale **"Still in the old PitziLabs org (transfer pending)"** bullet — `foundry-platform-demo` and `office-presence` transferred to `lentago` on 2026-07-01; PitziLabs is now empty (verified `gh repo list PitziLabs` → `[]`).

- Added the missing repos to the org list: `workstation-ansible`, `lentagolabs-dev`, `foundry-platform-demo`, `office-presence` (archived).

## Method notes

- **Harvest window:** transcripts modified in the last 14 days across `~/.claude/projects/` stores for every repo + `-home-cpitzi` (Home Claude) + `-home-cpitzi-repos` (Repo Claude).

- **Six parallel agents**, grouped by destination repo, each pre-loaded with the existing open-issue list for its repos to deconflict at the source.

- **Filtering:** completed/merged work, pure chit-chat, and generic "for now" phrasing were excluded. Every filed thread was cross-checked against live GitHub (not just transcripts, which predate the 2026-06-29 org migration).

- **Convergence caught by deconfliction:** the `claude-review` bot problem (two failure modes, two agents) and the `lentago.dev` go-live (two stores) were each merged into a single issue rather than filed twice.


