# Lentago Labs Fleet Report

> [!NOTE]
> **Co-authored with [Claude](https://claude.ai)** (Repo Claude, the Lentago Labs fleet steward). Auto-generated weekly from the fleet's public state (GitHub issues/PRs + `cloc` over public repo contents) — no personal, security, or homelab-internal detail is included. A prettier, editorialised copy renders on the Lentago lab LAN.

**Generated:** 2026-07-29 22:13 UTC · Scope: the **15 active** `lentago` repos (archived repos frozen &amp; excluded) · Activity window: last 30 days (since 2026-06-29).

## Snapshot

| Open issues | PRs merged (30d) | Issues closed (30d) | Code (incl. instructions) | Instruction-markdown |
|---:|---:|---:|---:|---:|
| **45** | 448 | 162 | **53,491** | 3,471 (20 files) |

The fleet's hand-maintained natural-language instruction surface (**3,471 lines** across 20 files) is among the largest "languages" in the code base — `reference-checker` alone is almost entirely prompt-program source.

---

## Open issues — 45 across 7 repos

### drosera — 12 open

| # | Title |
|---|-------|
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

### kalmia — 10 open

| # | Title |
|---|-------|
| [63](https://github.com/lentago/kalmia/issues/63) | Complete the lunaria → brasenia rename through runtime |
| [53](https://github.com/lentago/kalmia/issues/53) | Pre-merge guard: verify a ForceNew guest change can actually be re-created under the apply identity |
| [52](https://github.com/lentago/kalmia/issues/52) | Codify the n8n container's provisioning (Docker + compose) — recreate yields a bare template |
| [51](https://github.com/lentago/kalmia/issues/51) | Guarantee vzdump coverage for every Terraform-enforced guest (CT 113 had none) |
| [50](https://github.com/lentago/kalmia/issues/50) | Add prevent_destroy to import-only guests the token pipeline can't recreate (starting CT 113) |
| [30](https://github.com/lentago/kalmia/issues/30) | Terraform: bring PVE backup jobs (jobs.cfg) under management |
| [20](https://github.com/lentago/kalmia/issues/20) | Roadmap: provisioning clients beyond Ansible-on-workstations — VMs and containers as peer targets |
| [16](https://github.com/lentago/kalmia/issues/16) | Harden the xubuntu profile for Ubuntu 26.04 (stale comment + Docker CE repo codename) |
| [15](https://github.com/lentago/kalmia/issues/15) | Live-test the crostini profile on the Chromebook penguin container |
| [14](https://github.com/lentago/kalmia/issues/14) | Live-test the ubuntu_laptop profile on real ThinkPad hardware |

### claytonia — 7 open

| # | Title |
|---|-------|
| [71](https://github.com/lentago/claytonia/issues/71) | Reaper cannot see a job left in processing/ without an .owner file — permanent phantom occupancy |
| [65](https://github.com/lentago/claytonia/issues/65) | Complete the bullpen → claytonia rename on-host |
| [47](https://github.com/lentago/claytonia/issues/47) | Roadmap: platform-agnostic workers — Claude Code as one runtime behind the queue contract |
| [31](https://github.com/lentago/claytonia/issues/31) | Add optional authentication to the n8n Bullpen job-submit form |
| [24](https://github.com/lentago/claytonia/issues/24) | Branch hygiene across overlapping sessions: clean-desk session-end + prefer fleet dispatch |
| [22](https://github.com/lentago/claytonia/issues/22) | Fleet PR lane separation: rebase-before-merge + dispatch-time overlap check (no two writers on one file/panel) |
| [21](https://github.com/lentago/claytonia/issues/21) | Queue admission control: job ownership, fleet occupancy, and capacity awareness at submit time |

### solidago — 7 open

| # | Title |
|---|-------|
| [156](https://github.com/lentago/solidago/issues/156) | Split plan/apply OIDC environments so the terraform environment can carry a branch policy |
| [153](https://github.com/lentago/solidago/issues/153) | bootstrap-backend.sh still references a nonexistent "foundry" AWS profile |
| [149](https://github.com/lentago/solidago/issues/149) | Rotating a Lambda's Axiom token requires an unrelated apply to take effect |
| [144](https://github.com/lentago/solidago/issues/144) | Ask Lambda logs land in CloudWatch with no path to Axiom |
| [124](https://github.com/lentago/solidago/issues/124) | ECS task defs show a perpetual replace-diff (container_definitions normalization) — plan noise + apply-side-effect landmine |
| [21](https://github.com/lentago/solidago/issues/21) | Evaluate migration from ElastiCache node-based to serverless |
| [20](https://github.com/lentago/solidago/issues/20) | Document: Phase 2 Secrets Manager secret unused after RDS-managed password choice |

### betula — 3 open

| # | Title |
|---|-------|
| [89](https://github.com/lentago/betula/issues/89) | Complete the firewalla-axiom-pipeline → betula rename on-device |
| [86](https://github.com/lentago/betula/issues/86) | Firewalla boot race: Fluent Bit starts before Zeek's spool is live and tails dead paths silently; healthcheck's error-based detection cannot see it |
| [74](https://github.com/lentago/betula/issues/74) | Roadmap: core/client split — Firewalla and solidago (AWS) as peer collector clients |

### music-curator — 3 open

| # | Title |
|---|-------|
| [45](https://github.com/lentago/music-curator/issues/45) | Web-verify the promoted person nodes' credit rows |
| [44](https://github.com/lentago/music-curator/issues/44) | Producer-class connectors: decide representation |
| [43](https://github.com/lentago/music-curator/issues/43) | Session-tie receipts: render the credits justifying each edge |

### reference-checker — 3 open

| # | Title |
|---|-------|
| [11](https://github.com/lentago/reference-checker/issues/11) | Implement pipeline decomposition (Opus / Sonnet / Haiku stages) |
| [10](https://github.com/lentago/reference-checker/issues/10) | [v4] Design batch-pattern detection across submissions |
| [8](https://github.com/lentago/reference-checker/issues/8) | [v4] Integrate Crossref retraction API for structured retraction checking |

## Activity — last 30 days

**610 events**, one stream, newest first — 🟣 448 PRs merged · 🟢 162 issues closed

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
- 🟣 2026-07-25 · [reference-checker#52](https://github.com/lentago/reference-checker/pull/52) — Adopt the shared docs-check workflow
- 🟣 2026-07-25 · [music-curator#68](https://github.com/lentago/music-curator/pull/68) — Adopt the shared docs-check workflow
- 🟣 2026-07-25 · [kalmia#69](https://github.com/lentago/kalmia/pull/69) — Adopt the shared docs-check workflow
- 🟣 2026-07-25 · [homeassistant-config#510](https://github.com/lentago/homeassistant-config/pull/510) — Adopt the shared docs-check workflow
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
- 🟢 2026-07-25 · [reference-checker#50](https://github.com/lentago/reference-checker/issues/50) — Apply the Lentago Labs brand header to the README
- 🟣 2026-07-25 · [reference-checker#51](https://github.com/lentago/reference-checker/pull/51) — chore(brand): apply Lentago Labs header and banner to README
- 🟢 2026-07-25 · [music-curator#66](https://github.com/lentago/music-curator/issues/66) — Apply the Lentago Labs brand header to the README
- 🟣 2026-07-25 · [music-curator#67](https://github.com/lentago/music-curator/pull/67) — brand: apply Lentago Labs header to README
- 🟣 2026-07-25 · [kalmia#68](https://github.com/lentago/kalmia/pull/68) — docs: apply Lentago Labs brand header to README
- 🟢 2026-07-25 · [kalmia#67](https://github.com/lentago/kalmia/issues/67) — Apply the Lentago Labs brand header to the README
- 🟣 2026-07-25 · [homeassistant-config#509](https://github.com/lentago/homeassistant-config/pull/509) — docs: apply Lentago Labs brand header to README
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
- 🟣 2026-07-25 · [homeassistant-config#508](https://github.com/lentago/homeassistant-config/pull/508) — docs: remove broken image reference from Lentago Lab Status section
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
- 🟣 2026-07-25 · [homeassistant-config#507](https://github.com/lentago/homeassistant-config/pull/507) — Stop office/playroom flicker loops on an external off command
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
- 🟢 2026-07-18 · [drosera#155](https://github.com/lentago/drosera/issues/155) — Add Sites folder with per-site dashboards for pondviewlane.com, icecreamtofightwith.com, lentago.dev
- 🟣 2026-07-18 · [drosera#159](https://github.com/lentago/drosera/pull/159) — Add Sites folder with per-site dashboards for the three public sites
- 🟢 2026-07-18 · [drosera#154](https://github.com/lentago/drosera/issues/154) — Probe the three public sites from the lab Alloy (uptime, latency, TLS expiry)
- 🟣 2026-07-18 · [drosera#158](https://github.com/lentago/drosera/pull/158) — Probe the three public sites from the lab Alloy
- 🟣 2026-07-18 · [site-pondviewlane-com#9](https://github.com/lentago/site-pondviewlane-com/pull/9) — Add the Parcel C deed to the library; document the easement dimensions
- 🟣 2026-07-18 · [site-pondviewlane-com#8](https://github.com/lentago/site-pondviewlane-com/pull/8) — Clarify the Ice House Lane easement's "20 feet" is its width
- 🟣 2026-07-18 · [site-pondviewlane-com#7](https://github.com/lentago/site-pondviewlane-com/pull/7) — Add "No tax burden on the parcel" section to the Common Land guide
- 🟣 2026-07-18 · [site-pondviewlane-com#6](https://github.com/lentago/site-pondviewlane-com/pull/6) — Scrub second-person voice from the static prose
- 🟣 2026-07-18 · [site-pondviewlane-com#5](https://github.com/lentago/site-pondviewlane-com/pull/5) — Flag the trustee recording gap (record documents 4 of 5)
- 🟣 2026-07-18 · [site-pondviewlane-com#4](https://github.com/lentago/site-pondviewlane-com/pull/4) — Refresh the hero: Lora serif, redesigned mark, warmer card copy
- 🟣 2026-07-17 · [site-pondviewlane-com#3](https://github.com/lentago/site-pondviewlane-com/pull/3) — Go public: remove noindex + open robots.txt
- 🟣 2026-07-17 · [solidago#135](https://github.com/lentago/solidago/pull/135) — Bring pondviewlane.com online (apex domain, public launch)
- 🟣 2026-07-17 · [site-pondviewlane-com#2](https://github.com/lentago/site-pondviewlane-com/pull/2) — Make the repo self-contained (own source + build-time generator)
- 🟣 2026-07-17 · [.github#52](https://github.com/lentago/.github/pull/52) — fleet-ops: require the Build check on site-pondviewlane-com
- 🟣 2026-07-17 · [site-pondviewlane-com#1](https://github.com/lentago/site-pondviewlane-com/pull/1) — chore: ignore editor/tooling cruft
- 🟣 2026-07-17 · [solidago#134](https://github.com/lentago/solidago/pull/134) — Prune cpitzi/essex-crossing-hoa from the app deploy OIDC trust
- 🟣 2026-07-17 · [solidago#133](https://github.com/lentago/solidago/pull/133) — Trust site-pondviewlane-com via its immutable OIDC subject claim
- 🟣 2026-07-17 · [solidago#132](https://github.com/lentago/solidago/pull/132) — Dual-trust site-pondviewlane-com on the app deploy OIDC role
- 🟣 2026-07-17 · [solidago#131](https://github.com/lentago/solidago/pull/131) — ask-pondview: drop the composer from Opus 4.8/high to Sonnet 5/medium for latency
- 🟣 2026-07-17 · [solidago#130](https://github.com/lentago/solidago/pull/130) — ask-pondview: reframe the SYSTEM prompt for the public-record site
- 🟣 2026-07-16 · [solidago#129](https://github.com/lentago/solidago/pull/129) — Ask the Wiki: answer in street numbers — bake the Lot crosswalk into the prompt
- 🟣 2026-07-16 · [solidago#128](https://github.com/lentago/solidago/pull/128) — ask-lambda: adaptive-thinking API for Opus 4.8 (fixes the 400)
- 🟣 2026-07-15 · [solidago#127](https://github.com/lentago/solidago/pull/127) — ask-lambda: log + surface upstream Anthropic error detail (diagnostic)
- 🟣 2026-07-15 · [solidago#126](https://github.com/lentago/solidago/pull/126) — ask-lambda: upgrade the pondview chat to Opus 4.8 + extended thinking, multi-turn, HOA voice
- 🟣 2026-07-15 · [solidago#125](https://github.com/lentago/solidago/pull/125) — ask-lambda: self-deploy src-only handler edits + fix the fabricated-link prompt nit
- 🟣 2026-07-15 · [solidago#123](https://github.com/lentago/solidago/pull/123) — ask-lambda: seed the answer prompt with a naturalist voice + compliance guardrails
- 🟣 2026-07-15 · [solidago#122](https://github.com/lentago/solidago/pull/122) — ask-lambda: seed the answer prompt with a naturalist voice + compliance guardrails
- 🟣 2026-07-15 · [solidago#121](https://github.com/lentago/solidago/pull/121) — ask-lambda: drop function-URL CORS block (handler owns CORS)
- 🟣 2026-07-15 · [solidago#120](https://github.com/lentago/solidago/pull/120) — ask-lambda: grant public InvokeFunction so the NONE function URL works
- 🟣 2026-07-15 · [solidago#119](https://github.com/lentago/solidago/pull/119) — Add ask-lambda module + wire pondview 'Ask the Wiki' answer endpoint
- 🟣 2026-07-15 · [solidago#118](https://github.com/lentago/solidago/pull/118) — iam: trust cpitzi/essex-crossing-hoa (owner-qualified) for pondview deploy
- 🟣 2026-07-15 · [solidago#117](https://github.com/lentago/solidago/pull/117) — Add site_pondview: hidden preview for the Essex Crossing HOA wiki
- 🟣 2026-07-15 · [music-curator#38](https://github.com/lentago/music-curator/pull/38) — feat: discography seeding — full catalogs for Zorn, Aesop Rock, Waits, Talking Heads + personnel layer
- 🟣 2026-07-14 · [.github#51](https://github.com/lentago/.github/pull/51) — Incident reports: correct drosera follow-up issue references
- 🟣 2026-07-14 · [.github#50](https://github.com/lentago/.github/pull/50) — Incident register: six harvested reports, 2026-05-28 → 2026-07-08
- 🟣 2026-07-14 · [.github#49](https://github.com/lentago/.github/pull/49) — Weekly fleet reports refresh — 2026-07-14
- 🟣 2026-07-14 · [.github#48](https://github.com/lentago/.github/pull/48) — Commingle merged PRs and closed issues into one color-coded activity stream
- 🟣 2026-07-14 · [.github#47](https://github.com/lentago/.github/pull/47) — Weekly fleet reports refresh — 2026-07-14
- 🟣 2026-07-14 · [.github#46](https://github.com/lentago/.github/pull/46) — Extend fleet-report activity window from 7 to 30 days
- 🟣 2026-07-14 · [.github#45](https://github.com/lentago/.github/pull/45) — Weekly fleet reports refresh — 2026-07-14
- 🟣 2026-07-14 · [.github#44](https://github.com/lentago/.github/pull/44) — Link filed issues in the Firewalla log-shipping incident report
- 🟣 2026-07-14 · [.github#43](https://github.com/lentago/.github/pull/43) — Add incident report: Firewalla log shipping silently dark for three days (2026-07-10→13)
- 🟣 2026-07-13 · [.github#42](https://github.com/lentago/.github/pull/42) — Delete brand/avatars/cjp-brackets-navy-512.png
- 🟣 2026-07-13 · [site-icecreamtofightwith-com#142](https://github.com/lentago/site-icecreamtofightwith-com/pull/142) — Style footer wordmark: calligraphic red "Fight" everywhere the mark appears
- 🟣 2026-07-13 · [site-icecreamtofightwith-com#141](https://github.com/lentago/site-icecreamtofightwith-com/pull/141) — Style header wordmark: calligraphic red "Fight" to match the hero
- 🟢 2026-07-13 · [.github#40](https://github.com/lentago/.github/issues/40) — Publish incident reports as a periodic fleet report (incident register)
- 🟣 2026-07-13 · [.github#41](https://github.com/lentago/.github/pull/41) — Publish incident reports as a periodic fleet report (incident register)
- 🟣 2026-07-13 · [site-icecreamtofightwith-com#140](https://github.com/lentago/site-icecreamtofightwith-com/pull/140) — Style Intro hero: calligraphic red "Fight", tighter space above title
- 🟣 2026-07-13 · [.github#39](https://github.com/lentago/.github/pull/39) — Weekly fleet reports refresh — 2026-07-13
- 🟣 2026-07-13 · [.github#38](https://github.com/lentago/.github/pull/38) — Combine the fleet reports into a single fleet-report.md
- 🟣 2026-07-13 · [.github#37](https://github.com/lentago/.github/pull/37) — Weekly fleet reports refresh — 2026-07-13
- 🟣 2026-07-13 · [.github#36](https://github.com/lentago/.github/pull/36) — Add scheduled GitHub Actions workflow for the weekly fleet reports
- 🟣 2026-07-13 · [.github#35](https://github.com/lentago/.github/pull/35) — Add weekly fleet-reports automation + link from org profile
- 🟣 2026-07-13 · [homeassistant-config#506](https://github.com/lentago/homeassistant-config/pull/506) — Silence UGREEN NAS metrics: recorder-exclude sensors + drop NAS dashboard cards
- 🟣 2026-07-13 · [music-curator#32](https://github.com/lentago/music-curator/pull/32) — feat: Spotify data-availability spec + periodic Web API harvester (n8n)
- 🟣 2026-07-13 · [music-curator#37](https://github.com/lentago/music-curator/pull/37) — chore: gitignore .spotify operator secrets file on main
- 🟣 2026-07-13 · [music-curator#36](https://github.com/lentago/music-curator/pull/36) — chore: gitignore the local Music/ Obsidian working copy
- 🟣 2026-07-13 · [music-curator#35](https://github.com/lentago/music-curator/pull/35) — feat: streaming + collection merge — rotation dimension from GDPR streaming history
- 🟣 2026-07-13 · [music-curator#33](https://github.com/lentago/music-curator/pull/33) — data: purge the untagged reservoir — 26 artists discarded
- 🟣 2026-07-13 · [kalmia#49](https://github.com/lentago/kalmia/pull/49) — fix: re-import n8n LXC 113 (root@pam-created) to unbreak the pipeline
- 🟣 2026-07-12 · [kalmia#48](https://github.com/lentago/kalmia/pull/48) — fix: recreate n8n LXC 113 without bind mount (recover destroyed CT)
- 🟣 2026-07-12 · [kalmia#47](https://github.com/lentago/kalmia/pull/47) — feat: mount NAS spotify-harvest into n8n LXC 113 for the music-curator harvester
- 🟢 2026-07-12 · [site-icecreamtofightwith-com#138](https://github.com/lentago/site-icecreamtofightwith-com/issues/138) — Scroll-up at the top of a page should load the previous page (mirror of the #133 auto-advance)
- 🟣 2026-07-12 · [site-icecreamtofightwith-com#139](https://github.com/lentago/site-icecreamtofightwith-com/pull/139) — Scroll-up at the top of a page loads the previous page
- 🟢 2026-07-12 · [site-icecreamtofightwith-com#133](https://github.com/lentago/site-icecreamtofightwith-com/issues/133) — Scroll-linked reading: auto-advance to the next page at end of scroll, keep the filmstrip in sync
- 🟣 2026-07-12 · [site-icecreamtofightwith-com#137](https://github.com/lentago/site-icecreamtofightwith-com/pull/137) — Scroll-linked reading: auto-advance at end of scroll, keep the filmstrip in sync
- 🟣 2026-07-12 · [drosera#149](https://github.com/lentago/drosera/pull/149) — Rework Offload panel: stack by model, merge local sessions into metric-family rows
- 🟢 2026-07-12 · [site-icecreamtofightwith-com#131](https://github.com/lentago/site-icecreamtofightwith-com/issues/131) — Field diagrams: re-audit the logic-check, then place each figure inline next to the step it explains
- 🟣 2026-07-12 · [site-icecreamtofightwith-com#136](https://github.com/lentago/site-icecreamtofightwith-com/pull/136) — Re-audit field diagrams and place each figure inline
- 🟢 2026-07-12 · [site-icecreamtofightwith-com#132](https://github.com/lentago/site-icecreamtofightwith-com/issues/132) — Homepage: add a large rendered title graphic that pushes the intro text below the fold
- 🟣 2026-07-12 · [site-icecreamtofightwith-com#135](https://github.com/lentago/site-icecreamtofightwith-com/pull/135) — feat(homepage): add TitleHero viewport-filling title graphic
- 🟢 2026-07-12 · [site-icecreamtofightwith-com#130](https://github.com/lentago/site-icecreamtofightwith-com/issues/130) — Front-of-book cleanup: retire Essay numbering, move Final Thoughts ahead of recipes, de-swear the tagline
- 🟣 2026-07-12 · [site-icecreamtofightwith-com#134](https://github.com/lentago/site-icecreamtofightwith-com/pull/134) — Drop essay numbering, move Final Thoughts before recipes, soften tagline
- 🟣 2026-07-11 · [site-icecreamtofightwith-com#129](https://github.com/lentago/site-icecreamtofightwith-com/pull/129) — Add red scoop-mark favicon
- 🟣 2026-07-11 · [site-icecreamtofightwith-com#128](https://github.com/lentago/site-icecreamtofightwith-com/pull/128) — Widen filmstrip tiles, drop repeated sublabels, unredact the site, retire "homie"
- 🟣 2026-07-11 · [site-icecreamtofightwith-com#127](https://github.com/lentago/site-icecreamtofightwith-com/pull/127) — Implement the editorial redesign from Claude Design
- 🟣 2026-07-10 · [.github#34](https://github.com/lentago/.github/pull/34) — docs: publish the 2026-07 fleet issue report (archived copy)
- 🟢 2026-07-10 · [solidago#80](https://github.com/lentago/solidago/issues/80) — Tear down the retired pitzilabs preview site (module.site_pitzilabs)
- 🟣 2026-07-10 · [solidago#116](https://github.com/lentago/solidago/pull/116) — Finish pitzilabs teardown: neutralize illustrative example in modules/site (#80)
- 🟣 2026-07-10 · [solidago#114](https://github.com/lentago/solidago/pull/114) — Tear down the retired pitzilabs preview site (#80)
- 🟣 2026-07-10 · [solidago#113](https://github.com/lentago/solidago/pull/113) — Bump betula_ref to adopt the ALB parser 34-field fix
- 🟣 2026-07-10 · [drosera#148](https://github.com/lentago/drosera/pull/148) — Genericize ECS panel description to drop stale pitzilabs site name
- 🟢 2026-07-10 · [betula#84](https://github.com/lentago/betula/issues/84) — ALB parser rejects real 34-field log lines (raises ValueError, drops every event)
- 🟣 2026-07-10 · [betula#85](https://github.com/lentago/betula/pull/85) — Tolerate extra trailing fields in ALB access-log lines
- 🟣 2026-07-10 · [kalmia#46](https://github.com/lentago/kalmia/pull/46) — Fix stale NAS path in pub LXC description after lentago rebrand
- 🟣 2026-07-10 · [betula#82](https://github.com/lentago/betula/pull/82) — Stop shipping to Axiom; Grafana Cloud Loki becomes the sole output
- 🟣 2026-07-10 · [.github#33](https://github.com/lentago/.github/pull/33) — Round the suite marks and inline them in the product name cells
- 🟣 2026-07-10 · [.github#32](https://github.com/lentago/.github/pull/32) — Add product marks to the suite table on the org profile
- 🟢 2026-07-10 · [solidago#110](https://github.com/lentago/solidago/issues/110) — CI terraform apply fails: deploy role lacks lambda:* (blocks ALB-log shipper + all merges to main)
- 🟣 2026-07-10 · [solidago#112](https://github.com/lentago/solidago/pull/112) — Unblock ALB-log shipper deploy: grant lambda:* and make the package build plan-safe
- 🟢 2026-07-10 · [solidago#108](https://github.com/lentago/solidago/issues/108) — Deploy the ALB-access-log → Axiom shipper (betula AWS client)
- 🟣 2026-07-10 · [solidago#109](https://github.com/lentago/solidago/pull/109) — Deploy the ALB-access-log → Axiom shipper as a Lambda (#108)
- 🟣 2026-07-10 · [drosera#147](https://github.com/lentago/drosera/pull/147) — docs: transcript shipper now runs on all five bullpen runners
- 🟣 2026-07-09 · [drosera#146](https://github.com/lentago/drosera/pull/146) — fix(dashboard): make stream-of-consciousness panels unconditional, one per runner
- 🟢 2026-07-09 · [betula#80](https://github.com/lentago/betula/issues/80) — AWS client: collect ALB access logs from S3 into Axiom (solidago visitor-source telemetry)
- 🟣 2026-07-09 · [betula#81](https://github.com/lentago/betula/pull/81) — feat(aws): ALB access-log S3 → Axiom shipper (clients/aws/alb-logs)
- 🟢 2026-07-09 · [solidago#106](https://github.com/lentago/solidago/issues/106) — Enable ALB access logs to S3 for visitor-source telemetry (betula/Axiom ingestion)
- 🟣 2026-07-09 · [solidago#107](https://github.com/lentago/solidago/pull/107) — Enable ALB access logs to S3 for visitor-source telemetry
- 🟣 2026-07-09 · [music-curator#31](https://github.com/lentago/music-curator/pull/31) — feat: switchable graph-preset library — default taste map + artist-web audit view
- 🟣 2026-07-09 · [music-curator#30](https://github.com/lentago/music-curator/pull/30) — refactor: nest subcategory hub notes under their category folder
- 🟣 2026-07-09 · [music-curator#29](https://github.com/lentago/music-curator/pull/29) — feat: two-tier taxonomy — 13 top-level genres + subcategories
- 🟣 2026-07-09 · [music-curator#28](https://github.com/lentago/music-curator/pull/28) — refactor: promote the wiki out of examples/ — vault/ + data/ at top level
- 🟣 2026-07-09 · [music-curator#27](https://github.com/lentago/music-curator/pull/27) — feat: personnel credits layer + session-tie edges
- 🟣 2026-07-08 · [music-curator#15](https://github.com/lentago/music-curator/pull/15) — refactor: collapse scenes + genres into a single category axis
- 🟣 2026-07-08 · [music-curator#14](https://github.com/lentago/music-curator/pull/14) — data: tag the reservoir (round 1) — 376 artists graduated
- 🟣 2026-07-08 · [music-curator#13](https://github.com/lentago/music-curator/pull/13) — feat(vault): filter meta-hubs and recolor the graph by node type
- 🟣 2026-07-08 · [music-curator#12](https://github.com/lentago/music-curator/pull/12) — refactor(vault): remove the anchor layer from the graph
- 🟣 2026-07-08 · [music-curator#11](https://github.com/lentago/music-curator/pull/11) — feat: richer graph edges — collaboration links and split genres
- 🟣 2026-07-08 · [music-curator#10](https://github.com/lentago/music-curator/pull/10) — feat: Obsidian graph-vault driver
- 🟣 2026-07-08 · [drosera#144](https://github.com/lentago/drosera/pull/144) — fix(alloy): stop passing the HA token secret through string.trim_space
- 🟢 2026-07-08 · [claytonia#57](https://github.com/lentago/claytonia/issues/57) — Update Terraform backend to solidago-tfstate-* after shared-state migration
- 🟣 2026-07-08 · [claytonia#58](https://github.com/lentago/claytonia/pull/58) — Migrate Terraform backend to solidago-tfstate-* (#57)
- 🟢 2026-07-08 · [kalmia#44](https://github.com/lentago/kalmia/issues/44) — Update Terraform backend to solidago-tfstate-* after shared-state migration
- 🟣 2026-07-08 · [kalmia#45](https://github.com/lentago/kalmia/pull/45) — Migrate Terraform backend to solidago-tfstate-* (#44)
- 🟢 2026-07-08 · [drosera#142](https://github.com/lentago/drosera/issues/142) — Update Terraform backend to solidago-tfstate-* after shared-state migration
- 🟣 2026-07-08 · [drosera#143](https://github.com/lentago/drosera/pull/143) — Migrate Terraform backend to solidago-tfstate-* (#142)
- 🟢 2026-07-08 · [solidago#103](https://github.com/lentago/solidago/issues/103) — Migrate shared Terraform state backend foundry-tfstate-* → solidago-tfstate-*
- 🟣 2026-07-08 · [solidago#105](https://github.com/lentago/solidago/pull/105) — Migrate shared Terraform state backend to solidago-tfstate-* (#103)
- 🟣 2026-07-08 · [site-lentago-dev#37](https://github.com/lentago/site-lentago-dev/pull/37) — fix(deploy): point deploy.yml at renamed solidago-dev-* resources
- 🟢 2026-07-08 · [betula#78](https://github.com/lentago/betula/issues/78) — Update Axiom ingest-header secret reference after solidago rename
- 🟣 2026-07-08 · [betula#79](https://github.com/lentago/betula/pull/79) — docs: update AWS Secrets Manager secret name in clients/aws
- 🟢 2026-07-08 · [drosera#140](https://github.com/lentago/drosera/issues/140) — Align foundry-* references to solidago-* after solidago rename
- 🟣 2026-07-08 · [drosera#141](https://github.com/lentago/drosera/pull/141) — fix(solidago): rename foundry-dev-* to solidago-dev-* (solidago#102)
- 🟢 2026-07-08 · [site-icecreamtofightwith-com#125](https://github.com/lentago/site-icecreamtofightwith-com/issues/125) — Align foundry-dev-* AWS resource references to solidago after solidago rename
- 🟣 2026-07-08 · [site-icecreamtofightwith-com#126](https://github.com/lentago/site-icecreamtofightwith-com/pull/126) — Align deploy pipeline to solidago-* resource names (#125)
- 🟢 2026-07-08 · [solidago#102](https://github.com/lentago/solidago/issues/102) — Rename internal foundry-* application resources → solidago-*
- 🟣 2026-07-08 · [solidago#104](https://github.com/lentago/solidago/pull/104) — Rename foundry-* AWS resource names to the solidago codename (#102)
- 🟣 2026-07-07 · [kalmia#43](https://github.com/lentago/kalmia/pull/43) — Docs: the runner image is consumed, not a pending follow-up
- 🟣 2026-07-07 · [claytonia#56](https://github.com/lentago/claytonia/pull/56) — Docs: describe the image-based worker flow
- 🟢 2026-07-07 · [claytonia#54](https://github.com/lentago/claytonia/issues/54) — Consume the kalmia runner image: cut workers from claytonia-runner-v1, retire provision/01–05
- 🟣 2026-07-07 · [claytonia#55](https://github.com/lentago/claytonia/pull/55) — Cut new workers from the kalmia runner image; retire provision/01–05
- 🟢 2026-07-07 · [.github#27](https://github.com/lentago/.github/issues/27) — Rulesets have no required status checks — auto-merge can't arm and the fleet convention silently degrades
- 🟣 2026-07-07 · [.github#30](https://github.com/lentago/.github/pull/30) — fleet-ops: require existing always-on checks on 3 more repos
- 🟢 2026-07-07 · [kalmia#36](https://github.com/lentago/kalmia/issues/36) — Image forge: bake the bullpen runner template as the first versioned image artifact
- 🟣 2026-07-07 · [kalmia#42](https://github.com/lentago/kalmia/pull/42) — Image forge + first artifact: the claytonia-runner LXC template
- 🟣 2026-07-07 · [.github#29](https://github.com/lentago/.github/pull/29) — fleet-ops: manage per-repo required status checks
- 🟣 2026-07-07 · [solidago#101](https://github.com/lentago/solidago/pull/101) — Detect terraform changes and gate merges on a `gate` check
- 🟣 2026-07-07 · [drosera#139](https://github.com/lentago/drosera/pull/139) — Always run terraform CI on PRs, gate merges on a `gate` check
- 🟣 2026-07-07 · [kalmia#41](https://github.com/lentago/kalmia/pull/41) — Always run terraform CI on PRs, gate merges on a `gate` check
- 🟣 2026-07-07 · [shared-workflows#24](https://github.com/lentago/shared-workflows/pull/24) — docs: mark claytonia runner-pool applies as CI-enforced-on-merge
- 🟢 2026-07-07 · [claytonia#51](https://github.com/lentago/claytonia/issues/51) — Own runner capacity: adopt the worker-pool guest layer from kalmia (Terraform, Proxmox as first platform client)
- 🟣 2026-07-07 · [claytonia#53](https://github.com/lentago/claytonia/pull/53) — Add terraform CI: plan-on-PR / apply-on-merge on the LAN runner
- 🟣 2026-07-07 · [shared-workflows#23](https://github.com/lentago/shared-workflows/pull/23) — Enforced surfaces: split the Proxmox guest row — runner pool moves to claytonia
- 🟣 2026-07-07 · [claytonia#52](https://github.com/lentago/claytonia/pull/52) — Adopt the worker-pool guest layer: Terraform root, Proxmox as first platform client
- 🟢 2026-07-07 · [kalmia#37](https://github.com/lentago/kalmia/issues/37) — Release the bullpen runner pool from the guest layer — capacity ownership moves to claytonia
- 🟣 2026-07-07 · [kalmia#40](https://github.com/lentago/kalmia/pull/40) — Release the bullpen runner pool from the guest layer — capacity moves to claytonia
- 🟢 2026-07-07 · [kalmia#38](https://github.com/lentago/kalmia/issues/38) — Terraform fights operator power state on pet VMs — ignore `started` on workstations and testbeds
- 🟣 2026-07-07 · [kalmia#39](https://github.com/lentago/kalmia/pull/39) — Ignore operator-driven power state on workstation and testbed VMs
- 🟢 2026-07-06 · [kalmia#33](https://github.com/lentago/kalmia/issues/33) — Terraform: scale the bullpen out by two runners (claude-runner-4/-5, LXC 116/117)
- 🟣 2026-07-06 · [kalmia#35](https://github.com/lentago/kalmia/pull/35) — Create bullpen runners 4/5 without a Terraform-managed bind mount
- 🟣 2026-07-06 · [kalmia#34](https://github.com/lentago/kalmia/pull/34) — Scale the bullpen out by two runners (claude-runner-4/-5, LXC 116/117)
- 🟣 2026-07-06 · [solidago#100](https://github.com/lentago/solidago/pull/100) — chore: drop stale app/ice_cream_site .gitignore rules
- 🟣 2026-07-06 · [solidago#99](https://github.com/lentago/solidago/pull/99) — Delete app directory
- 🟣 2026-07-06 · [site-icecreamtofightwith-com#124](https://github.com/lentago/site-icecreamtofightwith-com/pull/124) — Revert "Redesign the site as a dated punk-zine blog" (#123)
- 🟣 2026-07-06 · [site-icecreamtofightwith-com#123](https://github.com/lentago/site-icecreamtofightwith-com/pull/123) — Redesign the site as a dated punk-zine blog
- 🟢 2026-07-06 · [site-lentago-dev#32](https://github.com/lentago/site-lentago-dev/issues/32) — Rename Suite anchor #work → #systems for nav consistency
- 🟣 2026-07-06 · [site-lentago-dev#35](https://github.com/lentago/site-lentago-dev/pull/35) — Rename Suite anchor #work → #systems for nav consistency
- 🟢 2026-07-06 · [site-lentago-dev#31](https://github.com/lentago/site-lentago-dev/issues/31) — Wire the consult form so ./send is not a dead end
- 🟣 2026-07-06 · [site-lentago-dev#34](https://github.com/lentago/site-lentago-dev/pull/34) — Wire consult form to Formspree (native POST, no JS) + /thanks page
- 🟢 2026-07-06 · [site-lentago-dev#30](https://github.com/lentago/site-lentago-dev/issues/30) — Footer version string goes stale (make it build-time)
- 🟢 2026-07-06 · [site-lentago-dev#28](https://github.com/lentago/site-lentago-dev/issues/28) — Nav "Writing" links to the Operating Principles section
- 🟢 2026-07-06 · [site-lentago-dev#29](https://github.com/lentago/site-lentago-dev/issues/29) — Add Open Graph / Twitter Card meta + og:image for social sharing
- 🟣 2026-07-06 · [site-lentago-dev#33](https://github.com/lentago/site-lentago-dev/pull/33) — Add social-share meta + og:image, build-time footer version, and nav Principles relabel
- 🟢 2026-07-06 · [site-lentago-dev#26](https://github.com/lentago/site-lentago-dev/issues/26) — Suite: give each system row its botanical genus mark
- 🟣 2026-07-06 · [site-lentago-dev#27](https://github.com/lentago/site-lentago-dev/pull/27) — feat(suite): anchor each system row with its genus mark
- 🟣 2026-07-05 · [solidago#98](https://github.com/lentago/solidago/pull/98) — Add GitHub Pages domain-verification TXT record for lentago.dev
- 🟣 2026-07-05 · [solidago#96](https://github.com/lentago/solidago/pull/96) — Add GitHub org domain-verification TXT record for lentago.dev
- 🟣 2026-07-05 · [.github#26](https://github.com/lentago/.github/pull/26) — Add 'The suite' legend to the org profile README
- 🟢 2026-07-05 · [kalmia#31](https://github.com/lentago/kalmia/issues/31) — Terraform cleanup: pin the PVE CA (drop insecure = true)
- 🟣 2026-07-05 · [kalmia#32](https://github.com/lentago/kalmia/pull/32) — Pin the PVE CA and drop insecure = true (cleanup)
- 🟢 2026-07-05 · [kalmia#28](https://github.com/lentago/kalmia/issues/28) — Terraform phase 3: import pve5 guests + HAOS VM 100 (last, prevent_destroy)
- 🟣 2026-07-05 · [kalmia#29](https://github.com/lentago/kalmia/pull/29) — Import pve5 guests and HAOS VM 100 into Terraform (phase 3)
- 🟢 2026-07-05 · [kalmia#25](https://github.com/lentago/kalmia/issues/25) — Terraform phase 2: LAN apply-on-merge — self-hosted runner LXC + OIDC state role + terraform workflow
- 🟣 2026-07-05 · [kalmia#27](https://github.com/lentago/kalmia/pull/27) — LAN apply-on-merge: self-hosted runner LXC + terraform workflow (phase 2)
- 🟣 2026-07-05 · [shared-workflows#22](https://github.com/lentago/shared-workflows/pull/22) — Add kalmia Proxmox guest layer to the enforced-surfaces table
- 🟢 2026-07-05 · [kalmia#23](https://github.com/lentago/kalmia/issues/23) — Terraform phase 1: import the five pve4 LXCs (110–114) to a clean plan
- 🟣 2026-07-05 · [kalmia#24](https://github.com/lentago/kalmia/pull/24) — Import the five pve4 LXCs into Terraform (phase 1)
- 🟣 2026-07-05 · [repo-template#6](https://github.com/lentago/repo-template/pull/6) — Scrub homelab branding for the Lentago rebrand
- 🟣 2026-07-05 · [solidago#95](https://github.com/lentago/solidago/pull/95) — Scrub homelab branding for the Lentago rebrand
- 🟣 2026-07-05 · [site-lentago-dev#25](https://github.com/lentago/site-lentago-dev/pull/25) — Scrub homelab branding for the Lentago rebrand
- 🟣 2026-07-05 · [shared-workflows#21](https://github.com/lentago/shared-workflows/pull/21) — Scrub homelab branding for the Lentago rebrand
- 🟣 2026-07-05 · [.github#25](https://github.com/lentago/.github/pull/25) — Scrub homelab branding for the Lentago rebrand
- 🟣 2026-07-05 · [kalmia#26](https://github.com/lentago/kalmia/pull/26) — Scrub homelab branding for the Lentago rebrand
- 🟣 2026-07-05 · [homeassistant-config#505](https://github.com/lentago/homeassistant-config/pull/505) — Rename Homelab Status dashboard to Lentago Lab Status
- 🟣 2026-07-05 · [claytonia#50](https://github.com/lentago/claytonia/pull/50) — Scrub homelab branding for the Lentago rebrand
- 🟣 2026-07-05 · [betula#77](https://github.com/lentago/betula/pull/77) — Scrub homelab branding for the Lentago rebrand
- 🟣 2026-07-05 · [drosera#137](https://github.com/lentago/drosera/pull/137) — Scrub homelab branding for the Lentago rebrand
- 🟣 2026-07-05 · [site-lentago-dev#24](https://github.com/lentago/site-lentago-dev/pull/24) — Add mobile responsive layer (≤720px/≤460px) with zero desktop change
- 🟣 2026-07-05 · [drosera#136](https://github.com/lentago/drosera/pull/136) — Display dashboard temperatures in Fahrenheit
- 🟢 2026-07-05 · [kalmia#21](https://github.com/lentago/kalmia/issues/21) — Proxmox guest lifecycle under Terraform — phase 0: provider scaffolding, auth, state backend
- 🟣 2026-07-05 · [kalmia#22](https://github.com/lentago/kalmia/pull/22) — Add Terraform layer for Proxmox guest lifecycle (phase 0)
- 🟣 2026-07-04 · [site-lentago-dev#23](https://github.com/lentago/site-lentago-dev/pull/23) — Landing reorg: drop ice-cream case study, add Suite section
- 🟣 2026-07-04 · [betula#76](https://github.com/lentago/betula/pull/76) — Rebrand sweep: PitziLabs → Lentago Labs
- 🟣 2026-07-04 · [claytonia#48](https://github.com/lentago/claytonia/pull/48) — Rebrand sweep: PitziLabs → Lentago Labs
- 🟣 2026-07-04 · [.github#24](https://github.com/lentago/.github/pull/24) — Rebrand sweep: PitziLabs → Lentago Labs
- 🟣 2026-07-04 · [homeassistant-config#504](https://github.com/lentago/homeassistant-config/pull/504) — Rebrand sweep: PitziLabs → Lentago Labs
- 🟣 2026-07-04 · [site-icecreamtofightwith-com#122](https://github.com/lentago/site-icecreamtofightwith-com/pull/122) — Rebrand sweep: PitziLabs → Lentago Labs
- 🟣 2026-07-04 · [drosera#135](https://github.com/lentago/drosera/pull/135) — Rebrand sweep: PitziLabs → Lentago Labs
- 🟣 2026-07-04 · [solidago#94](https://github.com/lentago/solidago/pull/94) — Rebrand sweep: PitziLabs → Lentago Labs
- 🟣 2026-07-04 · [site-lentago-dev#22](https://github.com/lentago/site-lentago-dev/pull/22) — Rebrand sweep: PitziLabs → Lentago Labs
- 🟢 2026-07-04 · [solidago#92](https://github.com/lentago/solidago/issues/92) — Phase 2: ship ECS container logs to Axiom via FireLens
- 🟣 2026-07-04 · [solidago#93](https://github.com/lentago/solidago/pull/93) — Ship ECS container logs to Axiom via FireLens (Phase 2)
- 🟣 2026-07-04 · [betula#75](https://github.com/lentago/betula/pull/75) — Add clients/aws contract: solidago ECS logs → Axiom via FireLens (Phase 2)
- 🟣 2026-07-04 · [drosera#134](https://github.com/lentago/drosera/pull/134) — docs: note expected logs AccessDenied in CloudWatch datasource health check
- 🟢 2026-07-04 · [solidago#90](https://github.com/lentago/solidago/issues/90) — Phase 1: cross-account read-only IAM role for the Grafana Cloud CloudWatch datasource (Part A)
- 🟣 2026-07-04 · [solidago#91](https://github.com/lentago/solidago/pull/91) — Add grafana-cloud module: cross-account read-only role for Grafana Cloud CloudWatch datasource (Phase 1 Part A)
- 🟢 2026-07-04 · [drosera#132](https://github.com/lentago/drosera/issues/132) — Phase 1: Solidago CloudWatch datasource + platform-health dashboard (Part B)
- 🟣 2026-07-04 · [drosera#133](https://github.com/lentago/drosera/pull/133) — Add Solidago folder, CloudWatch datasource, and platform-health dashboard (Phase 1 Part B)
- 🟣 2026-07-04 · [shared-workflows#20](https://github.com/lentago/shared-workflows/pull/20) — Sync live-state mirror for site-repo renames
- 🟢 2026-07-04 · [site-lentago-dev#20](https://github.com/lentago/site-lentago-dev/issues/20) — Align repo contents with site-lentago-dev rename
- 🟣 2026-07-04 · [site-lentago-dev#21](https://github.com/lentago/site-lentago-dev/pull/21) — Align repo contents with site-lentago-dev rename
- 🟢 2026-07-04 · [site-icecreamtofightwith-com#120](https://github.com/lentago/site-icecreamtofightwith-com/issues/120) — Align repo contents with site-icecreamtofightwith-com rename
- 🟣 2026-07-04 · [site-icecreamtofightwith-com#121](https://github.com/lentago/site-icecreamtofightwith-com/pull/121) — Align repo contents with site-icecreamtofightwith-com rename
- 🟢 2026-07-04 · [solidago#88](https://github.com/lentago/solidago/issues/88) — Codify site-repo rename dual-trust in app OIDC role
- 🟣 2026-07-04 · [solidago#89](https://github.com/lentago/solidago/pull/89) — Codify site-repo rename dual-trust in app OIDC role
- 🟢 2026-07-04 · [betula#72](https://github.com/lentago/betula/issues/72) — Rebrand repo to Betula — Lentago Labs log capture-and-archive layer
- 🟣 2026-07-04 · [betula#73](https://github.com/lentago/betula/pull/73) — Rebrand repo to Betula — Lentago Labs log capture-and-archive layer
- 🟣 2026-07-04 · [drosera#130](https://github.com/lentago/drosera/pull/130) — docs: update bullpen repo link to claytonia
- 🟢 2026-07-04 · [claytonia#45](https://github.com/lentago/claytonia/issues/45) — Rebrand repo to Claytonia — Lentago Labs agent-fleet system
- 🟣 2026-07-04 · [claytonia#46](https://github.com/lentago/claytonia/pull/46) — Rebrand repo to Claytonia — Lentago Labs agent-fleet system
- 🟢 2026-07-04 · [claytonia#43](https://github.com/lentago/claytonia/issues/43) — Update homelab-observability references to drosera (repo renamed 2026-07-04)
- 🟣 2026-07-04 · [claytonia#44](https://github.com/lentago/claytonia/pull/44) — chore: rename homelab-observability → drosera refs
- 🟢 2026-07-04 · [drosera#127](https://github.com/lentago/drosera/issues/127) — Rebrand repo to Drosera — Lentago Labs observability suite
- 🟣 2026-07-04 · [drosera#128](https://github.com/lentago/drosera/pull/128) — Rebrand repo to Drosera — Lentago Labs observability suite
- 🟣 2026-07-04 · [kalmia#19](https://github.com/lentago/kalmia/pull/19) — Rebrand repo to Kalmia — Lentago Labs provisioning system
- 🟢 2026-07-04 · [kalmia#18](https://github.com/lentago/kalmia/issues/18) — Rebrand repo to Kalmia — Lentago Labs provisioning system
- 🟣 2026-07-04 · [shared-workflows#19](https://github.com/lentago/shared-workflows/pull/19) — Sync live-state mirror for homelab-observability → drosera rename
- 🟣 2026-07-04 · [solidago#87](https://github.com/lentago/solidago/pull/87) — docs: sync README, CLAUDE.md, and BOOTSTRAP.md with recent platform changes
- 🟣 2026-07-04 · [solidago#86](https://github.com/lentago/solidago/pull/86) — Add project-scoped DeepWiki MCP server config
- 🟣 2026-07-04 · [solidago#85](https://github.com/lentago/solidago/pull/85) — Update self-references for repo rename to solidago
- 🟣 2026-07-04 · [site-icecreamtofightwith-com#119](https://github.com/lentago/site-icecreamtofightwith-com/pull/119) — docs: rebrand foundry-platform-demo → solidago
- 🟣 2026-07-04 · [drosera#126](https://github.com/lentago/drosera/pull/126) — docs(terraform): rename foundry-platform-demo → solidago
- 🟣 2026-07-04 · [homeassistant-config#503](https://github.com/lentago/homeassistant-config/pull/503) — docs: update foundry-platform-demo reference to solidago
- 🟣 2026-07-04 · [betula#71](https://github.com/lentago/betula/pull/71) — docs: update foundry-platform-demo reference to solidago
- 🟣 2026-07-04 · [site-lentago-dev#19](https://github.com/lentago/site-lentago-dev/pull/19) — docs: update solidago repo references (formerly foundry-platform-demo)
- 🟣 2026-07-04 · [claytonia#42](https://github.com/lentago/claytonia/pull/42) — Update n8n submit-form project option for solidago rename
- 🟣 2026-07-04 · [homeassistant-config#502](https://github.com/lentago/homeassistant-config/pull/502) — chore(readme): add Ask DeepWiki badge
- 🟣 2026-07-04 · [site-icecreamtofightwith-com#118](https://github.com/lentago/site-icecreamtofightwith-com/pull/118) — chore(readme): add Ask DeepWiki badge
- 🟣 2026-07-04 · [kalmia#17](https://github.com/lentago/kalmia/pull/17) — chore(readme): add Ask DeepWiki badge
- 🟣 2026-07-04 · [site-lentago-dev#18](https://github.com/lentago/site-lentago-dev/pull/18) — chore(readme): add Ask DeepWiki badge
- 🟣 2026-07-04 · [shared-workflows#18](https://github.com/lentago/shared-workflows/pull/18) — chore(readme): add Ask DeepWiki badge
- 🟣 2026-07-04 · [solidago#84](https://github.com/lentago/solidago/pull/84) — chore(readme): add Ask DeepWiki badge
- 🟣 2026-07-04 · [repo-template#5](https://github.com/lentago/repo-template/pull/5) — chore(readme): add Ask DeepWiki badge
- 🟣 2026-07-04 · [reference-checker#49](https://github.com/lentago/reference-checker/pull/49) — chore(readme): add Ask DeepWiki badge
- 🟣 2026-07-04 · [drosera#125](https://github.com/lentago/drosera/pull/125) — chore(readme): add Ask DeepWiki badge
- 🟣 2026-07-04 · [music-curator#8](https://github.com/lentago/music-curator/pull/8) — chore(readme): add Ask DeepWiki badge
- 🟣 2026-07-04 · [betula#70](https://github.com/lentago/betula/pull/70) — chore(readme): add Ask DeepWiki badge
- 🟣 2026-07-04 · [claytonia#41](https://github.com/lentago/claytonia/pull/41) — chore(readme): add Ask DeepWiki badge
- 🟣 2026-07-04 · [.github#23](https://github.com/lentago/.github/pull/23) — chore(readme): add Ask DeepWiki badge
- 🟣 2026-07-04 · [homeassistant-config#501](https://github.com/lentago/homeassistant-config/pull/501) — feat(office): rework candle flicker into a physical fire model
- 🟣 2026-07-04 · [homeassistant-config#500](https://github.com/lentago/homeassistant-config/pull/500) — feat(dashboard): show live light color on Home light cards
- 🟣 2026-07-03 · [homeassistant-config#499](https://github.com/lentago/homeassistant-config/pull/499) — Reconcile NAS share rename in neptune dashboard card
- 🟣 2026-07-03 · [claytonia#40](https://github.com/lentago/claytonia/pull/40) — Reconcile NAS share rename: PitziLabs -> lentago paths
- 🟣 2026-07-03 · [shared-workflows#17](https://github.com/lentago/shared-workflows/pull/17) — Reconcile PitziLabs->lentago: runner bot name + org wording
- 🟣 2026-07-03 · [homeassistant-config#498](https://github.com/lentago/homeassistant-config/pull/498) — Reconcile PitziLabs->lentago: grafana URL in dashboard card
- 🟣 2026-07-03 · [betula#69](https://github.com/lentago/betula/pull/69) — Reconcile PitziLabs->lentago: architecture diagram
- 🟣 2026-07-03 · [claytonia#39](https://github.com/lentago/claytonia/pull/39) — Reconcile PitziLabs->lentago: runner App name + org URLs
- 🟣 2026-07-03 · [drosera#124](https://github.com/lentago/drosera/pull/124) — Reconcile PitziLabs->lentago: stack URL + datasource names + org URLs + alloy health-check
- 🟢 2026-07-03 · [drosera#113](https://github.com/lentago/drosera/issues/113) — Resolve raw IPs to device/host names across dashboards (inventory feed + join transformations)
- 🟣 2026-07-03 · [drosera#122](https://github.com/lentago/drosera/pull/122) — feat(device-inventory): Firewalla redis → Loki publisher (#113 Phase 1)
- 🟣 2026-07-03 · [drosera#121](https://github.com/lentago/drosera/pull/121) — feat(dashboards): device inventory join, dropdown, WAN lookup links (phases 2+3+4a of #113)
- 🟣 2026-07-03 · [shared-workflows#16](https://github.com/lentago/shared-workflows/pull/16) — CLAUDE.md: add fleet-wide live-state vs. code discipline (canonical source)
- 🟣 2026-07-03 · [drosera#120](https://github.com/lentago/drosera/pull/120) — CLAUDE.md: add anti-drift rule for live dashboard edits
- 🟣 2026-07-03 · [drosera#119](https://github.com/lentago/drosera/pull/119) — infra-health: restore fleet-scoreboard revamp lost to IaC drift stomp
- 🟢 2026-07-03 · [drosera#111](https://github.com/lentago/drosera/issues/111) — device_ip variable is an empty custom dropdown — per-device filtering impossible on DNS & Security and Traffic & Devices
- 🟣 2026-07-03 · [drosera#116](https://github.com/lentago/drosera/pull/116) — fix(dashboards): convert device_ip from empty custom dropdown to textbox
- 🟢 2026-07-03 · [drosera#108](https://github.com/lentago/drosera/issues/108) — Tables show 'Value #A' column header; Top-N sort and cell coloring silently broken (9 panels, 3 dashboards)
- 🟣 2026-07-03 · [drosera#118](https://github.com/lentago/drosera/pull/118) — fix: retarget Value #A field in 9 table panels (closes #108)
- 🟢 2026-07-03 · [drosera#112](https://github.com/lentago/drosera/issues/112) — Claude Runner Fleet: 'Jobs over time by status' legend shows unlabeled 'Value' series from or vector(0) fallback
- 🟣 2026-07-03 · [drosera#117](https://github.com/lentago/drosera/pull/117) — fix: panel 5 status label fallback with label_replace
- 🟢 2026-07-03 · [drosera#109](https://github.com/lentago/drosera/issues/109) — Three timeseries panels render fully blank: legacy legend {displayMode: hidden} without placement breaks panel init
- 🟣 2026-07-03 · [drosera#115](https://github.com/lentago/drosera/pull/115) — fix: migrate legacy hidden legend schema to modern shape (issue #109)
- 🟢 2026-07-03 · [drosera#110](https://github.com/lentago/drosera/issues/110) — Traffic & Devices: 'Connections by Protocol' pie shows a single 'Value #A' slice instead of per-protocol breakdown
- 🟣 2026-07-03 · [drosera#114](https://github.com/lentago/drosera/pull/114) — fix(traffic-devices): enable values in reduceOptions for proto piechart
- 🟣 2026-07-03 · [.github#22](https://github.com/lentago/.github/pull/22) — Recolor org profile to the 2026-07 Tidewater palette
- 🟣 2026-07-03 · [site-lentago-dev#17](https://github.com/lentago/site-lentago-dev/pull/17) — docs: reconcile CLAUDE.md GitHub-reference convention to the live lentago org
- 🟣 2026-07-03 · [site-lentago-dev#16](https://github.com/lentago/site-lentago-dev/pull/16) — Fix dead links and stale org references now that the site is live
- 🟢 2026-07-03 · [betula#67](https://github.com/lentago/betula/issues/67) — CRITICAL: raw 'crontab user_crontab' install clobbers Firewalla's system cron jobs
- 🟣 2026-07-03 · [betula#68](https://github.com/lentago/betula/pull/68) — fix(cron): merge via update_crontab.sh instead of clobbering system crontab (#67)
- 🟣 2026-07-03 · [drosera#107](https://github.com/lentago/drosera/pull/107) — office-display: cover pve3/4/5 + neptune, de-dup HA titles
- 🟣 2026-07-03 · [drosera#106](https://github.com/lentago/drosera/pull/106) — Zeek/Loki dashboards: filter consistency, label accuracy, descriptions
- 🟣 2026-07-03 · [drosera#105](https://github.com/lentago/drosera/pull/105) — infra-health: re-point probe panels to integrations/blackbox/* jobs
- 🟣 2026-07-03 · [drosera#104](https://github.com/lentago/drosera/pull/104) — NAS dashboard: LCD bar gauges for Memory + Volume, group CPU gauges
- 🟢 2026-07-03 · [betula#65](https://github.com/lentago/betula/issues/65) — Healthcheck 'no output in 5m' branch restarts a healthy container every 10 minutes
- 🟣 2026-07-03 · [betula#66](https://github.com/lentago/betula/pull/66) — fix(healthcheck): remove no-output restart that bounces healthy container
- 🟢 2026-07-02 · [betula#63](https://github.com/lentago/betula/issues/63) — Ship Firewalla host + Zeek process metrics to Axiom (system_metrics_export.sh)
- 🟣 2026-07-02 · [betula#64](https://github.com/lentago/betula/pull/64) — feat: ship host + Zeek process metrics to Axiom (system_metrics_export.sh)
- 🟢 2026-07-02 · [betula#61](https://github.com/lentago/betula/issues/61) — Healthcheck false positive: bare docker calls fail under cron, force-recreating the container every 5 minutes
- 🟣 2026-07-02 · [betula#62](https://github.com/lentago/betula/pull/62) — fix(healthcheck): use sudo docker to fix false-positive cron failures
- 🟢 2026-07-02 · [betula#10](https://github.com/lentago/betula/issues/10) — Pull-based GitOps deployment
- 🟣 2026-07-02 · [betula#60](https://github.com/lentago/betula/pull/60) — docs(axiom): align new Zeek log queries with canonical arg_max join pattern
- 🟢 2026-07-02 · [betula#4](https://github.com/lentago/betula/issues/4) — Add support for additional Zeek log types
- 🟣 2026-07-02 · [betula#58](https://github.com/lentago/betula/pull/58) — feat: ship Zeek http, files, notice, and weird logs (#4)
- 🟢 2026-07-02 · [betula#5](https://github.com/lentago/betula/issues/5) — Rotate health check and cleanup log files
- 🟣 2026-07-02 · [betula#59](https://github.com/lentago/betula/pull/59) — feat: rotate health check and cleanup log files (closes #5)
- 🟢 2026-07-02 · [betula#13](https://github.com/lentago/betula/issues/13) — Eliminate stale device lookup records in Axiom queries
- 🟣 2026-07-02 · [betula#57](https://github.com/lentago/betula/pull/57) — docs(axiom): robust device joins via arg_max latest-record-per-MAC
- 🟢 2026-07-02 · [homeassistant-config#433](https://github.com/lentago/homeassistant-config/issues/433) — Add room-level light controls (on/off + dimmers) to the Home dashboard
- 🟢 2026-07-02 · [claytonia#37](https://github.com/lentago/claytonia/issues/37) — Failed jobs are silent: surface a signal when a run lands in failed/
- 🟣 2026-07-02 · [claytonia#38](https://github.com/lentago/claytonia/pull/38) — feat(run-job): comment on originating GitHub issue when a project job fails
- 🟢 2026-07-02 · [solidago#17](https://github.com/lentago/solidago/issues/17) — Upgrade GitHub Actions to Node.js 24-compatible versions
- 🟣 2026-07-02 · [solidago#83](https://github.com/lentago/solidago/pull/83) — chore(ci): upgrade actions/checkout to v7 (Node.js 24 runtime)
- 🟢 2026-07-02 · [solidago#12](https://github.com/lentago/solidago/issues/12) — Standardize Terraform resource naming convention (this vs main)
- 🟣 2026-07-02 · [solidago#82](https://github.com/lentago/solidago/pull/82) — refactor(modules): standardize resource labels from "main" to "this" (#12)
- 🟢 2026-07-02 · [solidago#16](https://github.com/lentago/solidago/issues/16) — Refactor VPC subnets from count to for_each
- 🟣 2026-07-02 · [solidago#81](https://github.com/lentago/solidago/pull/81) — refactor(vpc): key subnets by AZ with for_each instead of count
- 🟢 2026-07-02 · [homeassistant-config#434](https://github.com/lentago/homeassistant-config/issues/434) — Stop media now-playing cards from collapsing when idle (only variable-height element on the page)
- 🟣 2026-07-02 · [homeassistant-config#497](https://github.com/lentago/homeassistant-config/pull/497) — fix(dashboard): pin media tiles to fixed height to stop layout reflow on playback change
- 🟣 2026-07-01 · [claytonia#36](https://github.com/lentago/claytonia/pull/36) — docs(frontends): mark n8n submit form as retired
- 🟣 2026-07-01 · [homeassistant-config#496](https://github.com/lentago/homeassistant-config/pull/496) — docs(dashboards): document the Home single-master / two-clone scheme
- 🟢 2026-07-01 · [homeassistant-config#432](https://github.com/lentago/homeassistant-config/issues/432) — Adopt a single-master / two-clone scheme for the Home dashboard
- 🟢 2026-07-01 · [homeassistant-config#332](https://github.com/lentago/homeassistant-config/issues/332) — binary_sensor.basement_kitchen_door + battery sensor both unavailable
- 🟢 2026-07-01 · [site-lentago-dev#11](https://github.com/lentago/site-lentago-dev/issues/11) — Scale the footer wordmark to match the enlarged nav lockup
- 🟣 2026-07-01 · [site-lentago-dev#15](https://github.com/lentago/site-lentago-dev/pull/15) — Scale footer wordmark to match enlarged nav lockup
- 🟢 2026-07-01 · [.github#18](https://github.com/lentago/.github/issues/18) — Decide whether to seed org-default community-health files
- 🟣 2026-07-01 · [.github#21](https://github.com/lentago/.github/pull/21) — Seed org-default community-health files
- 🟢 2026-07-01 · [.github#17](https://github.com/lentago/.github/issues/17) — Restore logos on the AWS / ECS Fargate / CloudWatch profile badges
- 🟣 2026-07-01 · [.github#20](https://github.com/lentago/.github/pull/20) — Restore logos on the AWS / ECS Fargate / CloudWatch profile badges
- 🟢 2026-07-01 · [.github#16](https://github.com/lentago/.github/issues/16) — Finish the Lentago rebrand of the public org profile (README, banner, avatar variant)
- 🟣 2026-07-01 · [.github#19](https://github.com/lentago/.github/pull/19) — Add the limestone on-dark blossom variant and settle the canonical avatar
- 🟣 2026-07-01 · [drosera#102](https://github.com/lentago/drosera/pull/102) — Rehome claude-cost-export from the archived workstation-bootstrap repo
- 🟢 2026-07-01 · [site-lentago-dev#10](https://github.com/lentago/site-lentago-dev/issues/10) — Promote the site to lentago.dev (Phase 2 go-live)
- 🟣 2026-07-01 · [site-lentago-dev#14](https://github.com/lentago/site-lentago-dev/pull/14) — Recolor: anther-gold accent + teal warmed toward green
- 🟣 2026-07-01 · [solidago#79](https://github.com/lentago/solidago/pull/79) — feat(dns): Fastmail mail records for lentago.dev
- 🟣 2026-07-01 · [site-lentago-dev#13](https://github.com/lentago/site-lentago-dev/pull/13) — docs: reflect that the site is live at lentago.dev
- 🟣 2026-07-01 · [solidago#78](https://github.com/lentago/solidago/pull/78) — chore(site): retire the redundant lt-preview host for lentago.dev
- 🟣 2026-07-01 · [solidago#77](https://github.com/lentago/solidago/pull/77) — feat(dns): promote lentagolabs-dev to lentago.dev
- 🟣 2026-07-01 · [homeassistant-config#495](https://github.com/lentago/homeassistant-config/pull/495) — fix(alarm): drop the dead basement-kitchen door from House Openings
- 🟢 2026-07-01 · [homeassistant-config#376](https://github.com/lentago/homeassistant-config/issues/376) — Proxmox button orphans across haos/pve/pve3 — same re-registration pattern as #333
- 🟢 2026-07-01 · [homeassistant-config#450](https://github.com/lentago/homeassistant-config/issues/450) — home-preview --url path aborts on false-negative `which display-show` over non-interactive SSH
- 🟣 2026-07-01 · [drosera#100](https://github.com/lentago/drosera/pull/100) — Fleet dashboard: offload overlay, combined spend + total, wider stream-of-consciousness
- 🟢 2026-07-01 · [solidago#14](https://github.com/lentago/solidago/issues/14) — Implement selective teardown/standup scripts for cost management
- 🟣 2026-07-01 · [solidago#76](https://github.com/lentago/solidago/pull/76) — feat: selective teardown/standup scripts + runbook for cost saving (Closes #14)
- 🟢 2026-07-01 · [music-curator#4](https://github.com/lentago/music-curator/issues/4) — Add an engineering spine: machine-checkable schema + validator for the taste-profile JSON
- 🟣 2026-07-01 · [music-curator#7](https://github.com/lentago/music-curator/pull/7) — feat(schema): add JSON Schema + validator for music-inventory.json
- 🟢 2026-07-01 · [site-lentago-dev#9](https://github.com/lentago/site-lentago-dev/issues/9) — Correct stale deploy-not-yet-wired language in CLAUDE.md
- 🟣 2026-07-01 · [site-lentago-dev#12](https://github.com/lentago/site-lentago-dev/pull/12) — docs: update deploy status in CLAUDE.md
- 🟢 2026-07-01 · [solidago#15](https://github.com/lentago/solidago/issues/15) — Upgrade state bucket encryption from AES256 to KMS CMK
- 🟣 2026-07-01 · [solidago#75](https://github.com/lentago/solidago/pull/75) — feat: encrypt Terraform state bucket with a dedicated KMS CMK (SSE-KMS)
- 🟢 2026-07-01 · [claytonia#5](https://github.com/lentago/claytonia/issues/5) — run-job: fail a project job that should have opened a PR but didn't
- 🟣 2026-07-01 · [claytonia#35](https://github.com/lentago/claytonia/pull/35) — fix(run-job): fail project jobs that complete without opening a PR
- 🟢 2026-07-01 · [claytonia#12](https://github.com/lentago/claytonia/issues/12) — cr-submit: --help (and bare/unknown-flag invocations) silently queue a junk ad-hoc job instead of printing usage
- 🟣 2026-07-01 · [claytonia#34](https://github.com/lentago/claytonia/pull/34) — feat(cr-submit): -h/--help, unknown-flag error, bare-invocation guard
- 🟢 2026-07-01 · [shared-workflows#14](https://github.com/lentago/shared-workflows/issues/14) — claude-review CI bot fails to post a review across fleet PRs (turn-cap exhaustion + intermittent 0-byte response)
- 🟣 2026-07-01 · [shared-workflows#15](https://github.com/lentago/shared-workflows/pull/15) — fix(claude-review): make the reviewer advisory and non-blocking
- 🟢 2026-07-01 · [music-curator#5](https://github.com/lentago/music-curator/issues/5) — Fix data-integrity drift and unmerged duplicate anchors in the flagship example profile
- 🟣 2026-07-01 · [music-curator#6](https://github.com/lentago/music-curator/pull/6) — fix(examples): correct meta counts and merge Eno/Byrne duplicates
- 🟢 2026-07-01 · [solidago#13](https://github.com/lentago/solidago/issues/13) — Replace deprecated dynamodb_table backend param with use_lockfile
- 🟣 2026-07-01 · [solidago#74](https://github.com/lentago/solidago/pull/74) — feat: migrate S3 backend to S3-native state locking (use_lockfile)
- 🟢 2026-07-01 · [betula#6](https://github.com/lentago/betula/issues/6) — Harden deploy.sh for idempotent re-runs
- 🟣 2026-07-01 · [betula#56](https://github.com/lentago/betula/pull/56) — fix: make deploy.sh idempotent (safe to re-run)
- 🟢 2026-07-01 · [claytonia#8](https://github.com/lentago/claytonia/issues/8) — cr-submit -m flag silently ignored — project registry model overrides explicit request
- 🟣 2026-07-01 · [claytonia#33](https://github.com/lentago/claytonia/pull/33) — fix(cr-submit): accept -m/-p/-f in any order
- 🟣 2026-07-01 · [claytonia#32](https://github.com/lentago/claytonia/pull/32) — docs(roadmap): drop retired pve2 wall-display/kiosk as a live-board target
- 🟣 2026-06-30 · [.github#15](https://github.com/lentago/.github/pull/15) — Swap org-profile banner mark to the limestone-chip blossom
- 🟣 2026-06-30 · [kalmia#13](https://github.com/lentago/kalmia/pull/13) — Record testbed validation status for xubuntu/fedora
- 🟢 2026-06-30 · [kalmia#11](https://github.com/lentago/kalmia/issues/11) — First real-target test run: playbook fails to start + entry-path bugs
- 🟣 2026-06-30 · [kalmia#12](https://github.com/lentago/kalmia/pull/12) — Fix playbook startup, Helm/openssl, and fzf install (first real-target test run)
- 🟣 2026-06-30 · [kalmia#10](https://github.com/lentago/kalmia/pull/10) — Document the Xubuntu/Fedora provisioning testbed VMs
- 🟢 2026-06-30 · [kalmia#8](https://github.com/lentago/kalmia/issues/8) — Finish the crostini profile (sudo + ~/.local/bin + CLI-only Docker)
- 🟣 2026-06-30 · [kalmia#9](https://github.com/lentago/kalmia/pull/9) — Finish the crostini profile (sudo, ~/.local/bin, CLI-only Docker)
- 🟢 2026-06-30 · [kalmia#6](https://github.com/lentago/kalmia/issues/6) — Add power role: TLP + ThinkPad charge thresholds + fwupd
- 🟣 2026-06-30 · [kalmia#7](https://github.com/lentago/kalmia/pull/7) — Add power role: TLP, ThinkPad charge thresholds, fwupd
- 🟢 2026-06-30 · [kalmia#4](https://github.com/lentago/kalmia/issues/4) — Drop remote desktop (XRDP) capability entirely
- 🟣 2026-06-30 · [kalmia#5](https://github.com/lentago/kalmia/pull/5) — Drop remote desktop (XRDP) capability entirely
- 🟢 2026-06-30 · [kalmia#2](https://github.com/lentago/kalmia/issues/2) — Fedora dnf-repo wiring for Docker and VS Code
- 🟣 2026-06-30 · [kalmia#3](https://github.com/lentago/kalmia/pull/3) — Wire Fedora dnf installs for Docker and VS Code
- 🟣 2026-06-30 · [site-lentago-dev#8](https://github.com/lentago/site-lentago-dev/pull/8) — Enlarge the brand lockup in the top nav
- 🟣 2026-06-30 · [kalmia#1](https://github.com/lentago/kalmia/pull/1) — Add Ansible scaffold and core roles (Debian-runnable)
- 🟣 2026-06-30 · [site-lentago-dev#7](https://github.com/lentago/site-lentago-dev/pull/7) — Feature the blossom mark prominently in the hero
- 🟣 2026-06-30 · [.github#14](https://github.com/lentago/.github/pull/14) — Regenerate language census (post-rebrand, 15 repos)
- 🟣 2026-06-30 · [.github#13](https://github.com/lentago/.github/pull/13) — Point org profile links to lentago.dev
- 🟣 2026-06-30 · [.github#12](https://github.com/lentago/.github/pull/12) — Adopt the blossom brand mark across org materials
- 🟣 2026-06-30 · [site-lentago-dev#6](https://github.com/lentago/site-lentago-dev/pull/6) — Refresh docs: deploy is live, mark is the blossom
- 🟣 2026-06-30 · [site-lentago-dev#5](https://github.com/lentago/site-lentago-dev/pull/5) — Replace benchmark-disk mark with the blossom
- 🟣 2026-06-30 · [.github#11](https://github.com/lentago/.github/pull/11) — Rebrand org profile to Lentago Labs (Tidewater)
- 🟣 2026-06-30 · [solidago#73](https://github.com/lentago/solidago/pull/73) — Rebrand: fix remaining org URL in backlog script
- 🟣 2026-06-30 · [solidago#72](https://github.com/lentago/solidago/pull/72) — Rebrand: backlog script → lentago/foundry-platform-demo
- 🟣 2026-06-30 · [solidago#71](https://github.com/lentago/solidago/pull/71) — docs: correct stale AWS profile reference in CLAUDE.md
- 🟣 2026-06-30 · [solidago#70](https://github.com/lentago/solidago/pull/70) — Rebrand GitHub org references: PitziLabs → lentago
- 🟣 2026-06-29 · [drosera#99](https://github.com/lentago/drosera/pull/99) — Fix runner-fleet dashboard: app renamed to lentago-claude-runner
- 🟣 2026-06-29 · [site-lentago-dev#4](https://github.com/lentago/site-lentago-dev/pull/4) — Rebrand docs: PitziLabs → Lentago Labs
- 🟣 2026-06-29 · [shared-workflows#13](https://github.com/lentago/shared-workflows/pull/13) — Rebrand docs: PitziLabs → Lentago Labs
- 🟣 2026-06-29 · [repo-template#4](https://github.com/lentago/repo-template/pull/4) — Rebrand docs: PitziLabs → Lentago Labs
- 🟣 2026-06-29 · [site-icecreamtofightwith-com#117](https://github.com/lentago/site-icecreamtofightwith-com/pull/117) — Rebrand docs: PitziLabs → Lentago Labs
- 🟣 2026-06-29 · [music-curator#3](https://github.com/lentago/music-curator/pull/3) — Rebrand docs: PitziLabs → Lentago Labs
- 🟣 2026-06-29 · [claytonia#30](https://github.com/lentago/claytonia/pull/30) — Rebrand docs: PitziLabs → Lentago Labs
- 🟣 2026-06-29 · [drosera#98](https://github.com/lentago/drosera/pull/98) — Rebrand docs: PitziLabs → Lentago Labs
- 🟣 2026-06-29 · [homeassistant-config#494](https://github.com/lentago/homeassistant-config/pull/494) — Rebrand docs: PitziLabs → Lentago Labs
- 🟣 2026-06-29 · [.github#10](https://github.com/lentago/.github/pull/10) — Rebrand docs: PitziLabs → Lentago Labs (meta-repo + fleet-ops)
- 🟣 2026-06-29 · [betula#55](https://github.com/lentago/betula/pull/55) — Rebrand docs: PitziLabs → Lentago Labs
- 🟣 2026-06-29 · [homeassistant-config#493](https://github.com/lentago/homeassistant-config/pull/493) — Repoint reusable-workflow refs to the lentago org
- 🟣 2026-06-29 · [reference-checker#48](https://github.com/lentago/reference-checker/pull/48) — Repoint reusable-workflow refs to the lentago org
- 🟣 2026-06-29 · [site-icecreamtofightwith-com#116](https://github.com/lentago/site-icecreamtofightwith-com/pull/116) — Repoint reusable-workflow refs to the lentago org
- 🟣 2026-06-29 · [site-lentago-dev#3](https://github.com/lentago/site-lentago-dev/pull/3) — Repoint reusable-workflow refs to the lentago org
- 🟣 2026-06-29 · [betula#54](https://github.com/lentago/betula/pull/54) — Repoint reusable-workflow refs to the lentago org
- 🟣 2026-06-29 · [drosera#97](https://github.com/lentago/drosera/pull/97) — Repoint reusable-workflow refs to the lentago org
- 🟣 2026-06-29 · [claytonia#29](https://github.com/lentago/claytonia/pull/29) — Repoint reusable-workflow refs to the lentago org
- 🟣 2026-06-29 · [music-curator#2](https://github.com/lentago/music-curator/pull/2) — Repoint reusable-workflow refs to the lentago org
- 🟣 2026-06-29 · [repo-template#3](https://github.com/lentago/repo-template/pull/3) — Repoint reusable-workflow refs to the lentago org
- 🟣 2026-06-29 · [shared-workflows#12](https://github.com/lentago/shared-workflows/pull/12) — Repoint reusable-workflow refs to the lentago org
- 🟣 2026-06-29 · [site-lentago-dev#2](https://github.com/lentago/site-lentago-dev/pull/2) — Add trigger for deployment on push to main branch
- 🟣 2026-06-29 · [solidago#69](https://github.com/lentago/solidago/pull/69) — Host lentagolabs-dev on the shared platform (site_lentago + OIDC trust)
- 🟣 2026-06-29 · [site-lentago-dev#1](https://github.com/lentago/site-lentago-dev/pull/1) — Add Foundry deployment guide for lentagolabs-dev

---

## Code census

**The lens:** a `CLAUDE.md` (and its kin — `AGENTS.md`, skill `SKILL.md`, and the LLM prompt-programs that *are* a tool's logic) is an instruction set maintained for hygiene, so it's counted as **natural-language code**. Documentation, content/data, and community-health markdown are tallied separately and excluded from the code total, as are data payloads and generated files. This is a deliberate re-cut of the canonical [`metrics/language-census.md`](../metrics/language-census.md), which instead counts all Markdown/JSON/HTML as code.

### Languages

cloc *code* lines (blank + comment excluded). Shell folds Bourne + Bash. Instruction-markdown is promoted into the count (**bold**); the excluded buckets sit below the total.

| # | Language | Code | Files | Share |
|---|----------|-----:|------:|------:|
| 1 | JSON | 15,243 | 39 | 28.5% |
| 2 | YAML | 8,836 | 160 | 16.5% |
| 3 | Python | 7,273 | 46 | 13.6% |
| 4 | HCL | 6,108 | 104 | 11.4% |
| 5 | Shell (Bourne + Bash) | 4,814 | 63 | 9.0% |
| 6 | **Instructions (CLAUDE.md family + prompt-programs)** | 3,471 | 20 | 6.5% |
| 7 | Text | 3,452 | 25 | 6.5% |
| 8 | JavaScript | 1,793 | 16 | 3.4% |
| 9 | CSS | 1,260 | 9 | 2.4% |
| 10 | JSX | 851 | 10 | 1.6% |
| 11 | TypeScript | 310 | 8 | 0.6% |
| 12 | Other (TOML / Dockerfile / …) | 80 | 6 | 0.1% |
| | **CODE TOTAL** | **53,491** | **506** | 100% |
| — | _Data / exports — excluded_ | 139,938 | 26 | — |
| — | _Generated (lockfiles, SVG, brand artefacts) — excluded_ | 24,196 | 82 | — |

### Instruction-markdown as code

- **Hygiene family** (16 files · `CLAUDE.md`, `AGENTS.md`, `SKILL.md`): **2,020 lines**
- **Prompt-programs** (4 files · reference-checker auditors): **1,451 lines**

#### Hygiene surface — each file is a maintenance obligation

| Repo | File | Lines |
|------|------|------:|
| homeassistant-config | `CLAUDE.md` | 399 |
| shared-workflows | `CLAUDE.md` | 228 |
| site-pondviewlane-com | `CLAUDE.md` | 212 |
| .github | `CLAUDE.md` | 179 |
| betula | `CLAUDE.md` | 156 |
| site-lentago-dev | `CLAUDE.md` | 108 |
| kalmia | `CLAUDE.md` | 99 |
| solidago | `CLAUDE.md` | 99 |
| site-icecreamtofightwith-com | `CLAUDE.md` | 98 |
| drosera | `CLAUDE.md` | 96 |
| reference-checker | `CLAUDE.md` | 76 |
| music-curator | `CLAUDE.md` | 68 |
| drosera | `AGENTS.md` | 67 |
| claytonia | `CLAUDE.md` | 57 |
| brasenia | `CLAUDE.md` | 56 |
| repo-template | `CLAUDE.md` | 22 |
| **16 files** | | **2,020** |

#### Prompt-programs — natural language *is* the logic

| Repo | File | Lines |
|------|------|------:|
| reference-checker | `prompts/v6-auditor.md` | 583 |
| reference-checker | `prompts/v5-auditor.md` | 462 |
| reference-checker | `prompts/v4-auditor.md` | 337 |
| reference-checker | `prompts/v3-auditor.md` | 69 |
| **4 files** | | **1,451** |

_Judgement call: these prompt files are counted as instruction-code because they're versioned natural-language instruction sets. Scope to only the CLAUDE.md hygiene family and the instruction figure is **2,020**, not 3,471._

### Per-repo

| Repo | Code | Instr | Doc-md | Content-md | Data |
|------|-----:|------:|-------:|-----------:|-----:|
| drosera | 14,564 | 163 | 862 | 0 | 0 |
| site-pondviewlane-com | 6,661 | 212 | 2,372 | 0 | 0 |
| homeassistant-config | 6,438 | 399 | 1,090 | 0 | 17,567 |
| solidago | 6,340 | 99 | 1,692 | 0 | 0 |
| music-curator | 5,413 | 68 | 1,159 | 11,645 | 117,197 |
| kalmia | 2,424 | 99 | 606 | 0 | 0 |
| site-icecreamtofightwith-com | 2,048 | 98 | 596 | 6,008 | 0 |
| claytonia | 1,857 | 57 | 578 | 0 | 0 |
| .github | 1,810 | 179 | 616 | 2,321 | 0 |
| betula | 1,791 | 156 | 1,125 | 0 | 0 |
| reference-checker | 1,594 | 1,527 | 733 | 669 | 5,174 |
| site-lentago-dev | 1,428 | 108 | 362 | 0 | 0 |
| shared-workflows | 863 | 228 | 122 | 0 | 0 |
| brasenia | 188 | 56 | 577 | 0 | 0 |
| repo-template | 72 | 22 | 50 | 0 | 0 |

### Markdown taxonomy

The fleet carries **37,006 lines of Markdown across 841 files**; only 9.4% is instruction-code.

| Class | Lines | Files | Disposition |
|-------|------:|------:|-------------|
| **Instructions** | 3,471 | 20 | **counted as code** |
| Content / data | 20,643 | 689 | payload (vault notes, recipes, test-sets) — excluded |
| Documentation | 12,540 | 117 | READMEs, docs, ADRs, runbooks — excluded |
| Community-health | 352 | 15 | CONTRIBUTING/SECURITY/templates — excluded |
| **All Markdown** | **37,006** | **841** | |

---

## Method

- **Issues:** open issues via `gh search issues --owner lentago --state open`; activity from `gh search prs --owner lentago --merged` and closed issues filtered to the 30-day window. Public metadata only — no transcript harvest, ops items, or homelab detail (those live in the LAN copy).
- **Census tool:** `cloc`, run per-repo as `cloc --by-file --vcs=git` so only git-tracked files count (build output, `node_modules`, `.terraform`, venvs never enter). Lines are cloc *code* lines.
- **Scope:** the active repos owned by the `lentago` org, derived at runtime — personal repos and third-party clones are out of scope; archived repos are frozen and excluded.
- **Markdown classifier:** instruction-code = `CLAUDE.md`/`AGENTS.md`/`SKILL.md` or a versioned `prompts/*-auditor.md`; community-health = governance filenames + issue/PR templates; content = repo-scoped payload paths (music-curator `vault/`, ice-cream `recipes/`·manuscript, reference-checker `test-sets/`·`reports/`, dotgithub `fleet-reports/`); everything else = documentation.
- **Data / generated carve-outs:** exported payloads under the declared data dirs (music-curator `data/`, homeassistant-config `context/`) count as data whatever their serialisation — JSON, JSONL, CSV/TSV, XML, YAML — as does reference-checker's rendered `reports/*.html`; lockfiles, SVG and `.github/brand/generated/` (emitted from `brand/fleet.json`) are generated. drosera's `dashboards/*.json` stay in code as Terraform-enforced dashboards-as-code.
- **Regenerating:** `python3 metrics/generate-fleet-reports.py --out-dir .`

_Generated with Claude Code (Repo Claude)._
