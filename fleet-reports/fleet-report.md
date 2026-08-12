# Lentago Labs Fleet Report

> [!NOTE]
> **Co-authored with [Claude](https://claude.ai)** (Repo Claude, the Lentago Labs fleet steward). Auto-generated weekly from the fleet's public state (GitHub issues/PRs + `cloc` over public repo contents) — no personal, security, or homelab-internal detail is included. A prettier, editorialised copy renders on the Lentago lab LAN.

**Generated:** 2026-08-12 20:22 UTC · Scope: the **16 active** `lentago` repos (archived repos frozen &amp; excluded) · Activity window: last 30 days (since 2026-07-13).

## Snapshot

| Open issues | PRs merged (30d) | Issues closed (30d) | Code (incl. instructions) | Instruction-markdown |
|---:|---:|---:|---:|---:|
| **48** | 271 | 98 | **58,209** | 3,609 (21 files) |

The fleet's hand-maintained natural-language instruction surface (**3,609 lines** across 21 files) is among the largest "languages" in the code base — `reference-checker` alone is almost entirely prompt-program source.

---

## Open issues — 48 across 8 repos

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

### kalmia — 11 open

| # | Title |
|---|-------|
| [85](https://github.com/lentago/kalmia/issues/85) | power: assert charge thresholds actually reached sysfs instead of trusting the drop-in |
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

### .github — 2 open

| # | Title |
|---|-------|
| [90](https://github.com/lentago/.github/issues/90) | Recommendation: engagement pathways — the lab ladder for new members |
| [81](https://github.com/lentago/.github/issues/81) | terraform: wire plan-on-PR and apply-on-merge for the fleet settings module |

## Activity — last 30 days

**369 events**, one stream, newest first — 🟣 271 PRs merged · 🟢 98 issues closed

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
- 🟣 2026-08-12 · [reference-checker#53](https://github.com/lentago/reference-checker/pull/53) — README: reposition as learning-lab exhibit (patterns, operator vectors, DeepWiki)
- 🟣 2026-08-12 · [music-curator#78](https://github.com/lentago/music-curator/pull/78) — README: reposition as learning-lab exhibit (patterns, operator vectors, DeepWiki)
- 🟣 2026-08-12 · [homeassistant-config#513](https://github.com/lentago/homeassistant-config/pull/513) — README: reposition as learning-lab exhibit (patterns, operator vectors, DeepWiki)
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
- 🟢 2026-08-09 · [homeassistant-config#511](https://github.com/lentago/homeassistant-config/issues/511) — README drift: File Structure lists home.yaml twice with retired grid-layout annotation; '40+ entities' undersells the registry
- 🟣 2026-08-09 · [homeassistant-config#512](https://github.com/lentago/homeassistant-config/pull/512) — docs: fix README File Structure duplicate, restate entity counts
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

---

## Code census

**The lens:** a `CLAUDE.md` (and its kin — `AGENTS.md`, skill `SKILL.md`, and the LLM prompt-programs that *are* a tool's logic) is an instruction set maintained for hygiene, so it's counted as **natural-language code**. Documentation, content/data, and community-health markdown are tallied separately and excluded from the code total, as are data payloads and generated files. This is a deliberate re-cut of the canonical [`metrics/language-census.md`](../metrics/language-census.md), which instead counts all Markdown/JSON/HTML as code.

### Languages

cloc *code* lines (blank + comment excluded). Shell folds Bourne + Bash. Instruction-markdown is promoted into the count (**bold**); the excluded buckets sit below the total.

| # | Language | Code | Files | Share |
|---|----------|-----:|------:|------:|
| 1 | JSON | 16,032 | 40 | 27.5% |
| 2 | YAML | 9,177 | 168 | 15.8% |
| 3 | Python | 7,393 | 46 | 12.7% |
| 4 | HCL | 6,474 | 114 | 11.1% |
| 5 | Shell (Bourne + Bash) | 5,416 | 68 | 9.3% |
| 6 | **Instructions (CLAUDE.md family + prompt-programs)** | 3,609 | 21 | 6.2% |
| 7 | Text | 3,452 | 25 | 5.9% |
| 8 | Astro | 1,895 | 19 | 3.3% |
| 9 | JavaScript | 1,793 | 16 | 3.1% |
| 10 | CSS | 1,260 | 9 | 2.2% |
| 11 | JSX | 851 | 10 | 1.5% |
| 12 | Jinja Template | 467 | 10 | 0.8% |
| 13 | TypeScript | 310 | 8 | 0.5% |
| 14 | Other (TOML / Dockerfile / …) | 80 | 6 | 0.1% |
| | **CODE TOTAL** | **58,209** | **560** | 100% |
| — | _Data / exports — excluded_ | 141,906 | 26 | — |
| — | _Generated (lockfiles, SVG, brand artefacts) — excluded_ | 24,489 | 85 | — |

### Instruction-markdown as code

- **Hygiene family** (17 files · `CLAUDE.md`, `AGENTS.md`, `SKILL.md`): **2,158 lines**
- **Prompt-programs** (4 files · reference-checker auditors): **1,451 lines**

#### Hygiene surface — each file is a maintenance obligation

| Repo | File | Lines |
|------|------|------:|
| homeassistant-config | `CLAUDE.md` | 399 |
| shared-workflows | `CLAUDE.md` | 232 |
| site-pondviewlane-com | `CLAUDE.md` | 212 |
| .github | `CLAUDE.md` | 205 |
| betula | `CLAUDE.md` | 156 |
| kalmia | `CLAUDE.md` | 155 |
| site-lentago-dev | `CLAUDE.md` | 108 |
| solidago | `CLAUDE.md` | 99 |
| site-icecreamtofightwith-com | `CLAUDE.md` | 98 |
| drosera | `CLAUDE.md` | 96 |
| reference-checker | `CLAUDE.md` | 76 |
| music-curator | `CLAUDE.md` | 68 |
| drosera | `AGENTS.md` | 67 |
| claytonia | `CLAUDE.md` | 57 |
| brasenia | `CLAUDE.md` | 56 |
| asclepias | `CLAUDE.md` | 52 |
| repo-template | `CLAUDE.md` | 22 |
| **17 files** | | **2,158** |

#### Prompt-programs — natural language *is* the logic

| Repo | File | Lines |
|------|------|------:|
| reference-checker | `prompts/v6-auditor.md` | 583 |
| reference-checker | `prompts/v5-auditor.md` | 462 |
| reference-checker | `prompts/v4-auditor.md` | 337 |
| reference-checker | `prompts/v3-auditor.md` | 69 |
| **4 files** | | **1,451** |

_Judgement call: these prompt files are counted as instruction-code because they're versioned natural-language instruction sets. Scope to only the CLAUDE.md hygiene family and the instruction figure is **2,158**, not 3,609._

### Per-repo

| Repo | Code | Instr | Doc-md | Content-md | Data |
|------|-----:|------:|-------:|-----------:|-----:|
| drosera | 15,060 | 163 | 945 | 0 | 0 |
| site-pondviewlane-com | 7,210 | 212 | 2,429 | 0 | 0 |
| homeassistant-config | 6,438 | 399 | 1,113 | 0 | 17,567 |
| solidago | 6,340 | 99 | 1,731 | 0 | 0 |
| music-curator | 5,413 | 68 | 1,141 | 11,645 | 119,165 |
| site-icecreamtofightwith-com | 3,260 | 98 | 603 | 6,008 | 0 |
| kalmia | 3,109 | 155 | 740 | 0 | 0 |
| .github | 2,675 | 205 | 951 | 2,070 | 0 |
| claytonia | 2,461 | 57 | 897 | 0 | 0 |
| betula | 1,816 | 156 | 1,190 | 0 | 0 |
| reference-checker | 1,594 | 1,527 | 777 | 669 | 5,174 |
| site-lentago-dev | 1,562 | 108 | 390 | 0 | 0 |
| shared-workflows | 867 | 232 | 221 | 0 | 0 |
| brasenia | 188 | 56 | 632 | 0 | 0 |
| asclepias | 144 | 52 | 393 | 0 | 0 |
| repo-template | 72 | 22 | 84 | 0 | 0 |

### Markdown taxonomy

The fleet carries **38,590 lines of Markdown across 859 files**; only 9.4% is instruction-code.

| Class | Lines | Files | Disposition |
|-------|------:|------:|-------------|
| **Instructions** | 3,609 | 21 | **counted as code** |
| Content / data | 20,392 | 689 | payload (vault notes, recipes, test-sets) — excluded |
| Documentation | 14,237 | 134 | READMEs, docs, ADRs, runbooks — excluded |
| Community-health | 352 | 15 | CONTRIBUTING/SECURITY/templates — excluded |
| **All Markdown** | **38,590** | **859** | |

---

## Method

- **Issues:** open issues via `gh search issues --owner lentago --state open`; activity from `gh search prs --owner lentago --merged` and closed issues filtered to the 30-day window. Public metadata only — no transcript harvest, ops items, or homelab detail (those live in the LAN copy).
- **Census tool:** `cloc`, run per-repo as `cloc --by-file --vcs=git` so only git-tracked files count (build output, `node_modules`, `.terraform`, venvs never enter). Lines are cloc *code* lines.
- **Scope:** the active repos owned by the `lentago` org, derived at runtime — personal repos and third-party clones are out of scope; archived repos are frozen and excluded.
- **Markdown classifier:** instruction-code = `CLAUDE.md`/`AGENTS.md`/`SKILL.md` or a versioned `prompts/*-auditor.md`; community-health = governance filenames + issue/PR templates; content = repo-scoped payload paths (music-curator `vault/`, ice-cream `recipes/`·manuscript, reference-checker `test-sets/`·`reports/`, dotgithub `fleet-reports/`); everything else = documentation.
- **Data / generated carve-outs:** exported payloads under the declared data dirs (music-curator `data/`, homeassistant-config `context/`) count as data whatever their serialisation — JSON, JSONL, CSV/TSV, XML, YAML — as does reference-checker's rendered `reports/*.html`; lockfiles, SVG and `.github/brand/generated/` (emitted from `brand/fleet.json`) are generated. drosera's `dashboards/*.json` stay in code as Terraform-enforced dashboards-as-code.
- **Regenerating:** `python3 metrics/generate-fleet-reports.py --out-dir .`

_Generated with Claude Code (Repo Claude)._
