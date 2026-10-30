# Lentago Labs Epics Report

> [!NOTE]
> **Co-authored with [Claude](https://claude.ai)** (Repo Claude, the Lentago Labs fleet steward). Auto-generated weekly from the fleet's public state. An **epic** here is a tracking issue: one labelled `epic`, or an open issue with sub-issues and no parent of its own. Progress is GitHub's own sub-issue count plus the issue's checklist, so an epic that is not kept up to date shows as not moving — that is the point. The sibling [fleet report](fleet-report.md) lists every open issue; this one asks what the issues add up to, and how much of the merged work they describe.

**Generated:** 2026-10-30 15:08 UTC · Scope: the **26 active** `lentago` repos · Merged-PR window: last 30 days (since 2026-09-30) · closed epics shown for 90 days.

## Snapshot

| Open epics | Closed epics (90d) | Open issues under an epic | Merged PRs (30d) | …that trace to an epic | …loose, with an issue | …loose, no issue | …bots |
|---:|---:|---:|---:|---:|---:|---:|---:|
| **10** | 3 | **90 / 142** (63%) | 619 | **113** (22% of non-bot) | 346 | 61 | 99 |

The *trace to an epic* share is the headline: how much of the month's merged work the epics describe. The two loose columns are work that happened outside any epic — tracked by a stand-alone issue, or by nothing but the PR. Bots are Dependabot and the fleet's own automation, excluded from the share.

---

## Open epics — 10

| Epic | Since | Sub-issues closed | Checklist | PRs (30d) | Last activity |
|------|-------|-------------------|-----------|----------:|---------------|
| [.github#134](https://github.com/lentago/.github/issues/134) Offerings roadmap — tracking epic (refreshed 2026-10-06) | 2026-08-16 | `████░░░░░░` 18/45 | 7/8 | 41 ⚠︎ 1 PR cited in comments only | 2026-10-12 |
| [.github#285](https://github.com/lentago/.github/issues/285) Rename debt: the tier 3–4 renames still open across the fleet | 2026-10-30 | `░░░░░░░░░░` 0/13 | — | 22 | 2026-10-30 |
| [.github#235](https://github.com/lentago/.github/issues/235) Genus marks for the eight unmarked species | 2026-10-07 | `░░░░░░░░░░` 0/2 | 11/13 | 11 | 2026-10-13 |
| [brasenia#130](https://github.com/lentago/brasenia/issues/130) Phase 3: the fleet on the display, and what stays open after ADR-0020 | 2026-10-30 | `█░░░░░░░░░` 1/9 | — | 8 | 2026-10-30 |
| [betula#74](https://github.com/lentago/betula/issues/74) Roadmap: core/client split — Firewalla and solidago (AWS) as peer collector clients | 2026-07-04 | `░░░░░░░░░░` 0/2 | — | 5 | 2026-08-16 |
| [monarda#18](https://github.com/lentago/monarda/issues/18) Rung 2: the plain organization site, with a rescue import and editing without git — epic | 2026-10-12 | `██████████` 3/3 | 3/4 | 4 | 2026-10-12 |
| [.github#286](https://github.com/lentago/.github/issues/286) Fleet secrets handling (ADR-0011): the follow-through | 2026-10-30 | `░░░░░░░░░░` 0/9 | — | 3 | 2026-10-30 |
| [mitchella#31](https://github.com/lentago/mitchella/issues/31) Roadmap to MVP: prove the desk, file on the user's behalf, run it unattended | 2026-10-30 | `█░░░░░░░░░` 1/12 | — | 3 | 2026-10-30 |
| [.github#234](https://github.com/lentago/.github/issues/234) Enable Dependabot security updates fleet-wide (codified in terraform) | 2026-10-07 | `░░░░░░░░░░` 0/5 | — | 1 | 2026-10-07 |
| [claytonia#47](https://github.com/lentago/claytonia/issues/47) Roadmap: platform-agnostic workers — Claude Code as one runtime behind the queue contract | 2026-07-04 | `░░░░░░░░░░` 0/2 | — | 0 | 2026-08-16 |

*Sub-issues closed* is GitHub's native parent/child count (it crosses repos). *Checklist* is the `- [ ]` boxes in the epic's body. ⚠︎ marks progress that was recorded in comments while the body's checklist was not updated — the epic is moving, but its face is stale.

### Offerings roadmap — tracking epic (refreshed 2026-10-06)

[.github#134](https://github.com/lentago/.github/issues/134) · open since 2026-08-16 · last activity 2026-10-12

> Tracking epic for the offerings roadmap: the kits we would build next for the reader ADR-0008 names — the one tech person at an organization that runs on volunteers and donations.

Progress: **18/45** sub-issues closed · checklist **7/8** · **41** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [.github#122](https://github.com/lentago/.github/issues/122) Offering: Good-Standing Kit — registry reconciliation on the uvularia vault (MA pack first)
- ⬜ [.github#123](https://github.com/lentago/.github/issues/123) Offering: Liberation Pipeline — SaaS-export collectors + restore drills — 0/1 sub-issues closed
  - ⬜ [betula#126](https://github.com/lentago/betula/issues/126) Liberation Pipeline: SaaS-export collectors + restore drills, as betula clients (lentago/.github#123)
- ⬜ [.github#124](https://github.com/lentago/.github/issues/124) Offering: Digital Custody audit — ownership insurance for the org's presence
- ⬜ [.github#125](https://github.com/lentago/.github/issues/125) Offering: Insurance-Receipts Pack — controls with evidence exhaust — 0/4 sub-issues closed
  - ⬜ [.github#251](https://github.com/lentago/.github/issues/251) Offering: Email trust receipt — SPF, DKIM and DMARC as code, an MFA audit, the phishing habit
  - ⬜ [.github#252](https://github.com/lentago/.github/issues/252) Offering: Backup with a receipt — object-locked copies and a drilled restore
  - ⬜ [.github#253](https://github.com/lentago/.github/issues/253) Offering: Offboarding drill — the access register made real
  - ⬜ [uvularia#95](https://github.com/lentago/uvularia/issues/95) Retention ledger as an obligation pack: the org's own retention policy evaluated against live retention
- ⬜ [.github#126](https://github.com/lentago/.github/issues/126) Offering: Institutional Memory kit — the uvularia Ask box on a private lupinus vault
- ⬜ [.github#127](https://github.com/lentago/.github/issues/127) Guide page: AI-with-receipts — the reviewed-merge operating model, written for the one reader (ships in lupinus)
- ⬜ [.github#129](https://github.com/lentago/.github/issues/129) Offering: cold-chain & facilities telemetry kit
- ⬜ [.github#130](https://github.com/lentago/.github/issues/130) Offering: funder-report fact pipeline
- ⬜ [.github#131](https://github.com/lentago/.github/issues/131) Offering: privacy posture kit for newly covered orgs
- ⬜ [.github#132](https://github.com/lentago/.github/issues/132) Spike: volunteer-ops scheduling — evaluate, don't build (decision memo)
- ⬜ [.github#133](https://github.com/lentago/.github/issues/133) Offering: Ops-in-a-Box — the miniature estate starter kit
- ⬜ [.github#195](https://github.com/lentago/.github/issues/195) Offering: sensor trip opens a work order — epigaea alert to GitHub Issue
- ⬜ [.github#196](https://github.com/lentago/.github/issues/196) Offering: help-desk starter for a private repo — issue forms, labels, a board
- ⬜ [.github#200](https://github.com/lentago/.github/issues/200) Offering: uvularia — client-owned records vault, grounded Ask, live compliance board (supersedes #128) — 18/19 sub-issues closed
  - ⬜ [uvularia#92](https://github.com/lentago/uvularia/issues/92) Phase 3 — consumers: the vault-side contract for the funder-report pipeline and Good-Standing reconciliation
  - ✅ [drosera#218](https://github.com/lentago/drosera/issues/218) uvularia pipeline pane: the left-to-right dashboard and its alert rules, provisioned for a client's own Grafana Cloud stack
  - ✅ [solidago#195](https://github.com/lentago/solidago/issues/195) uvularia demo sandbox: an isolated OIDC role, permissions boundary, and state key for the demonstration Ask function
  - ✅ [uvularia#2](https://github.com/lentago/uvularia/issues/2) Phase 0 · core: record and obligation schemas
  - ✅ [uvularia#3](https://github.com/lentago/uvularia/issues/3) Phase 0 · core: validate.py (schema, links, privacy tripwires, no-delete, visibility)
  - ✅ [uvularia#4](https://github.com/lentago/uvularia/issues/4) Phase 0 · core: evaluate.py — obligations → standing.json
  - ✅ [uvularia#5](https://github.com/lentago/uvularia/issues/5) Phase 0 · obligations pack: Massachusetts (Open Meeting Law, charities filing, condo statute)
  - ✅ [uvularia#6](https://github.com/lentago/uvularia/issues/6) Phase 0 · templates/records: the vault template
  - ✅ [uvularia#7](https://github.com/lentago/uvularia/issues/7) Phase 0 · intake door: GitHub Issue form → scaffolded PR
  - ✅ [uvularia#8](https://github.com/lentago/uvularia/issues/8) Phase 0 · templates/site: the public "Is it posted?" board
  - ✅ [uvularia#9](https://github.com/lentago/uvularia/issues/9) Phase 0 · demo: org.yaml + seed.py + Stillwater Brook records (ADR-0001)
  - ✅ [uvularia#10](https://github.com/lentago/uvularia/issues/10) Phase 0 · ADOPTION.md, timed dry-run, and the first receipt
  - ✅ [uvularia#11](https://github.com/lentago/uvularia/issues/11) Phase 0 · lupinus picker row and lentago.dev receipt
  - ✅ [uvularia#33](https://github.com/lentago/uvularia/issues/33) Phase 1 · templates/ask-rules: the governance template and its eval gate
  - ✅ [uvularia#34](https://github.com/lentago/uvularia/issues/34) Phase 1 · Ask function: mitchella as a serverless runtime in the client's account
  - ✅ [uvularia#35](https://github.com/lentago/uvularia/issues/35) Phase 1 · templates/site: the Ask widget with verified citations
  - ✅ [uvularia#36](https://github.com/lentago/uvularia/issues/36) Phase 1 · board history: show lateness over time, not only the current standing
  - ✅ [uvularia#52](https://github.com/lentago/uvularia/issues/52) Phase 2 · emit one event per pipeline stage to the client's Grafana Cloud Loki
  - ✅ [uvularia#53](https://github.com/lentago/uvularia/issues/53) Phase 2 · alerts open GitHub Issues: stale served digest, obligation gone amber, cap at 80 %
- ⬜ [.github#247](https://github.com/lentago/.github/issues/247) Offering: Accessible by default — every page checked, a receipt per build
- ⬜ [.github#248](https://github.com/lentago/.github/issues/248) Offering: EOL radar — support end dates open Issues before they bite
- ⬜ [.github#249](https://github.com/lentago/.github/issues/249) Offering: Board pack — a one-page monthly operations report the board actually reads
- ⬜ [brasenia#41](https://github.com/lentago/brasenia/issues/41) Lobby-pane variant: a visitor-facing screen in a client's own front room
- ⬜ [drosera#197](https://github.com/lentago/drosera/issues/197) "Are we open" single source of truth
- ⬜ [kalmia#107](https://github.com/lentago/kalmia/issues/107) Donated-hardware refresh profiles (new client class) — 0/1 sub-issues closed
  - ⬜ [kalmia#151](https://github.com/lentago/kalmia/issues/151) OS stance for a nonprofit fleet; ChromeOS Flex as the first donated-hardware profile

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-10-12 · [lupinus#25](https://github.com/lentago/lupinus/pull/25) — Stories: one spine, three rungs, one map; one canonical product list
- 2026-10-12 · [monarda#26](https://github.com/lentago/monarda/pull/26) — feat: rung 2, the plain organization site page set
- 2026-10-12 · [.github#259](https://github.com/lentago/.github/pull/259) — Regroup the profile suite table by promise; taglines lead with role
- 2026-10-12 · [uvularia#99](https://github.com/lentago/uvularia/pull/99) — Receipts: one-repository rung timed (6 min 09 s); Ask box's first live answer
- 2026-10-12 · [lupinus#22](https://github.com/lentago/lupinus/pull/22) — Tiers: refresh brasenia, add mitchella; picker: phones, printers, Wi-Fi
- 2026-10-12 · [monarda#21](https://github.com/lentago/monarda/pull/21) — Record the first timed dry-run: 3 min 01 s, two defects filed
- 2026-10-12 · [.github#255](https://github.com/lentago/.github/pull/255) — Profile suite rows for epigaea, brasenia; betula tagline off-device
- 2026-10-12 · [epigaea#530](https://github.com/lentago/epigaea/pull/530) — docs: facilities kit is tracked, not built — README and CLAUDE.md
- 2026-10-09 · [lupinus#18](https://github.com/lentago/lupinus/pull/18) — Stories: cite uvularia for the watershed's public records, drop pondviewlane and closed #128
- 2026-10-06 · [.github#232](https://github.com/lentago/.github/pull/232) — Require shellcheck on the seven repos that just gained a caller
- 2026-10-04 · [uvularia#76](https://github.com/lentago/uvularia/pull/76) — template-sync: drift waits for sync on push; say plainly when auto-merge is refused
- 2026-10-04 · [uvularia#72](https://github.com/lentago/uvularia/pull/72) — Records template: publish a plain public board page so the vault is useful as one repository
- 2026-10-04 · [uvularia#64](https://github.com/lentago/uvularia/pull/64) — Telemetry: emit the fields drosera's pipeline pane reads (at, intake/reviewed snapshots, served heartbeat, asked.subject)
- 2026-10-04 · [uvularia#60](https://github.com/lentago/uvularia/pull/60) — Phase 2 · alerts open GitHub Issues: stale served digest, obligation gone amber, cap at 80 %
- 2026-10-04 · [drosera#220](https://github.com/lentago/drosera/pull/220) — feat(uvularia): records pipeline pane — dashboard, alert rules, client export (#218)
- 2026-10-04 · [uvularia#58](https://github.com/lentago/uvularia/pull/58) — Phase 2 · emit one event per pipeline stage to the client's Grafana Cloud Loki
- 2026-10-04 · [uvularia#55](https://github.com/lentago/uvularia/pull/55) — templates/site: keep the SiteConfig interface out of the client-edited file
- 2026-10-04 · [uvularia#50](https://github.com/lentago/uvularia/pull/50) — site tests: do not assert the template's own defaults; derive the base path from the config
- 2026-10-04 · [uvularia#49](https://github.com/lentago/uvularia/pull/49) — Phase 1 · templates/site: the Ask widget with verified citations
- 2026-10-03 · [solidago#196](https://github.com/lentago/solidago/pull/196) — feat(uvularia-demo-sandbox): fence the demo Ask function in-account (#195)
- 2026-10-03 · [uvularia#45](https://github.com/lentago/uvularia/pull/45) — Phase 1 · Ask function: mitchella as a hardened serverless runtime in the client's account (#34)
- 2026-10-03 · [uvularia#40](https://github.com/lentago/uvularia/pull/40) — Phase 1 · board history: show lateness over time, not only the current standing
- 2026-10-03 · [uvularia#38](https://github.com/lentago/uvularia/pull/38) — validate.py: fail on duplicate obligation ids
- 2026-10-03 · [mitchella#16](https://github.com/lentago/mitchella/pull/16) — uvularia Phase 1: bundle corpus source, StandingProvider, AnnouncementProvider
- 2026-10-03 · [uvularia#37](https://github.com/lentago/uvularia/pull/37) — Phase 1 · templates/ask-rules: the governance template and its eval gate
- 2026-10-03 · [.github#207](https://github.com/lentago/.github/pull/207) — Org profile: the public-record offering is live, with uvularia and its demo board
- 2026-10-03 · [site-lentago-dev#87](https://github.com/lentago/site-lentago-dev/pull/87) — Public-record offering is live: uvularia Phase 0 ran its first dry-run
- 2026-10-03 · [uvularia#32](https://github.com/lentago/uvularia/pull/32) — First dry-run receipt; point the adoption path at the template repos; document the intake-door traps
- 2026-10-03 · [lupinus#12](https://github.com/lentago/lupinus/pull/12) — Picker: add the uvularia records-vault row (Kit, with receipt)
- 2026-10-03 · [uvularia#24](https://github.com/lentago/uvularia/pull/24) — Phase 0 · adoption docs: ADOPTION.md, timed dry-run, and the first receipt
- 2026-10-03 · [uvularia#23](https://github.com/lentago/uvularia/pull/23) — Phase 0 · templates/site: the `<org>-site` repository template
- 2026-10-03 · [uvularia#22](https://github.com/lentago/uvularia/pull/22) — Phase 0 · intake door: Issue form → scaffolded PR
- 2026-10-03 · [uvularia#20](https://github.com/lentago/uvularia/pull/20) — Phase 0 · demo: org.yaml + seed.py + Stillwater Brook records (ADR-0001)
- 2026-10-03 · [uvularia#19](https://github.com/lentago/uvularia/pull/19) — Phase 0 · templates/records: the vault template (#6)
- 2026-10-03 · [uvularia#16](https://github.com/lentago/uvularia/pull/16) — Phase 0 · core: evaluate.py — obligations → standing.json
- 2026-10-03 · [uvularia#15](https://github.com/lentago/uvularia/pull/15) — Phase 0 · core: validate.py (schema, links, privacy tripwires, no-delete, visibility)
- 2026-10-03 · [uvularia#14](https://github.com/lentago/uvularia/pull/14) — Phase 0 · obligations pack: Massachusetts (Open Meeting Law, charities filing, condo statute)
- 2026-10-03 · [uvularia#12](https://github.com/lentago/uvularia/pull/12) — Phase 0 · core: record and obligation schemas
- 2026-10-03 · [site-lentago-dev#84](https://github.com/lentago/site-lentago-dev/pull/84) — Point the public-record offering at uvularia, not a client's site
- 2026-10-03 · [.github#199](https://github.com/lentago/.github/pull/199) — ADR-0009: uvularia records vault; create lentago/uvularia from repo-template
- 2026-10-01 · [lupinus#11](https://github.com/lentago/lupinus/pull/11) — Add guide/stories: five shops, one tech person each

</details>

### Enable Dependabot security updates fleet-wide (codified in terraform)

[.github#234](https://github.com/lentago/.github/issues/234) · open since 2026-10-07 · last activity 2026-10-07

> Related: monarda's dependabot.yml has no npm ecosystem at all (filed separately).

Progress: **0/5** sub-issues closed · **1** PR merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [monarda#11](https://github.com/lentago/monarda/issues/11) Clear the npm security-alert backlog; add npm to dependabot.yml
- ⬜ [site-icecreamtofightwith-com#198](https://github.com/lentago/site-icecreamtofightwith-com/issues/198) Clear the npm security-alert backlog (45 open, 42 patchable)
- ⬜ [uvularia#81](https://github.com/lentago/uvularia/issues/81) http-cache-semantics GHSA-ch52-4w7c-c8xp: no patched release; not reachable in static builds
- ⬜ [uvularia#85](https://github.com/lentago/uvularia/issues/85) Template workflow action pins have no automated updater
- ⬜ [uvularia#102](https://github.com/lentago/uvularia/issues/102) Dependabot alert 27: http-cache-semantics in templates/site, no fix yet

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-10-07 · [uvularia#86](https://github.com/lentago/uvularia/pull/86) — Revert Dependabot template directories (workflows are scanned at the root only)

</details>

### Genus marks for the eight unmarked species

[.github#235](https://github.com/lentago/.github/issues/235) · open since 2026-10-07 · last activity 2026-10-13

> Six of the fourteen in-org species carry a genus mark (lentago, solidago, drosera, kalmia, claytonia, betula).

Progress: **0/2** sub-issues closed · checklist **11/13** · **11** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [.github#239](https://github.com/lentago/.github/issues/239) brand: README header blocks drifted from brand/generated in monarda, osmunda, shared-workflows; coderabbit has none
- ⬜ [.github#282](https://github.com/lentago/.github/issues/282) brand: genus marks render with black-filled leaves in banners and social cards

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-10-29 · [.github#281](https://github.com/lentago/.github/pull/281) — brand: generate a Roku home-screen poster for repos that ship a Roku channel
- 2026-10-07 · [site-lentago-dev#93](https://github.com/lentago/site-lentago-dev/pull/93) — Carry the eight new genus marks; point mark canon at lentago/.github
- 2026-10-07 · [epigaea#527](https://github.com/lentago/epigaea/pull/527) — Banner with the epigaea genus mark
- 2026-10-07 · [asclepias#14](https://github.com/lentago/asclepias/pull/14) — Banner with the asclepias genus mark
- 2026-10-07 · [lupinus#15](https://github.com/lentago/lupinus/pull/15) — Banner with the lupinus genus mark
- 2026-10-07 · [uvularia#88](https://github.com/lentago/uvularia/pull/88) — Banner with the uvularia genus mark
- 2026-10-07 · [osmunda#8](https://github.com/lentago/osmunda/pull/8) — Banner with the osmunda genus mark
- 2026-10-07 · [brasenia#23](https://github.com/lentago/brasenia/pull/23) — Banner with the brasenia genus mark
- 2026-10-07 · [mitchella#21](https://github.com/lentago/mitchella/pull/21) — Banner with the mitchella genus mark
- 2026-10-07 · [monarda#13](https://github.com/lentago/monarda/pull/13) — Banner with the monarda genus mark
- 2026-10-07 · [.github#236](https://github.com/lentago/.github/pull/236) — brand: genus marks for the eight unmarked species

</details>

### Rename debt: the tier 3–4 renames still open across the fleet

[.github#285](https://github.com/lentago/.github/issues/285) · open since 2026-10-30 · last activity 2026-10-30

> Tracking issue for the fleet's remaining rename debt under the rename discipline (shared-workflows/CLAUDE.md, "Rename discipline"): a rename is done when no surface carries the old name, or every surface that does is owned by an open tracking issue.

Progress: **0/13** sub-issues closed · **22** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [betula#89](https://github.com/lentago/betula/issues/89) Complete the firewalla-axiom-pipeline → betula rename on-device
- ⬜ [claytonia#65](https://github.com/lentago/claytonia/issues/65) Complete the bullpen → claytonia rename on-host — 0/2 sub-issues closed
  - ⬜ [claytonia#157](https://github.com/lentago/claytonia/issues/157) gitops: the loop never notices its own installed copy drifting from the checkout
  - ⬜ [kalmia#228](https://github.com/lentago/kalmia/issues/228) forge: the egress check passes on DNS alone, and a build CT can't keep a Firewalla-approved MAC
- ⬜ [drosera#169](https://github.com/lentago/drosera/issues/169) Complete the homelab-observability → drosera rename through CI and hosts — 0/3 sub-issues closed
  - ⬜ [drosera#299](https://github.com/lentago/drosera/issues/299) On or after 2026-11-06: remove LXC 105's pre-move Alloy volume and unit copies (#169)
  - ⬜ [solidago#221](https://github.com/lentago/solidago/issues/221) On or after 2026-11-06: retire the pre-rename drosera Terraform role and state key (drosera#169 Phase 3)
  - ⬜ [solidago#223](https://github.com/lentago/solidago/issues/223) docs: list the betula and drosera cross-repo roles in ADOPTION.md, and scope BOOTSTRAP's locking note to solidago's own backend
- ⬜ [drosera#282](https://github.com/lentago/drosera/issues/282) Migrate the cluster="lentago-lab" label value to "onprem" across emitters
- ⬜ [epigaea#518](https://github.com/lentago/epigaea/issues/518) Complete the epigaea rename through runtime (tiers 3–4)
- ⬜ [epigaea#533](https://github.com/lentago/epigaea/issues/533) Rename the lentago-lab-status dashboard and the pitzilabs_homelab_observability sensor
- ⬜ [kalmia#158](https://github.com/lentago/kalmia/issues/158) Rename the Proxmox cluster "homelab-cluster" to "onprem" (tier 4)
- ⬜ [osmunda#16](https://github.com/lentago/osmunda/issues/16) Move n8n from n8n.lab.lentago.dev to n8n.onprem.lentago.dev

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-10-30 · [kalmia#229](https://github.com/lentago/kalmia/pull/229) — docs: name drosera as the owner of the pve-host alert rules
- 2026-10-30 · [drosera#298](https://github.com/lentago/drosera/pull/298) — Docs: the rename's state after the LXC 105 move (#169 Phase 7)
- 2026-10-30 · [claytonia#161](https://github.com/lentago/claytonia/pull/161) — Transcript shipper: check drosera out at /opt/drosera (drosera#169 Phase 5a)
- 2026-10-30 · [drosera#297](https://github.com/lentago/drosera/pull/297) — Prepare the host checkouts for /opt/drosera (#169 Phases 4a and 6)
- 2026-10-30 · [drosera#296](https://github.com/lentago/drosera/pull/296) — Move Terraform state and the CI role to the drosera name (#169 Phase 2)
- 2026-10-30 · [solidago#219](https://github.com/lentago/solidago/pull/219) — iam: add the drosera Terraform pipeline role (drosera#169 Phase 1)
- 2026-10-30 · [claytonia#160](https://github.com/lentago/claytonia/pull/160) — claude-review: point the gitops rule at claytonia-gitops (part of #65)
- 2026-10-30 · [claytonia#159](https://github.com/lentago/claytonia/pull/159) — terraform: per-worker rebuild triggers, and create workers in the claytonia pool (part of #65)
- 2026-10-30 · [kalmia#226](https://github.com/lentago/kalmia/pull/226) — forge: build the v2 runner image under the claytonia names, with cluster-checked VMIDs
- 2026-10-30 · [claytonia#158](https://github.com/lentago/claytonia/pull/158) — Rename the on-host gitops loop to claytonia-gitops (part of #65)
- 2026-10-30 · [shared-workflows#83](https://github.com/lentago/shared-workflows/pull/83) — Rename discipline: kalmia#63 (lunaria runtime) is paid
- 2026-10-29 · [kalmia#211](https://github.com/lentago/kalmia/pull/211) — Rename lunaria to brasenia through runtime: rebuild LXC 118 as brasenia
- 2026-10-14 · [.github#270](https://github.com/lentago/.github/pull/270) — voice: the on-prem half of the estate is "on-prem"; retire "homelab" and "lab"
- 2026-10-14 · [epigaea#534](https://github.com/lentago/epigaea/pull/534) — epigaea: retire "homelab"/"lab" wording for on-prem
- 2026-10-14 · [solidago#216](https://github.com/lentago/solidago/pull/216) — solidago: retire "homelab"/"lab" wording for on-prem
- 2026-10-14 · [betula#140](https://github.com/lentago/betula/pull/140) — Retire "homelab"/"lab" wording for on-prem
- 2026-10-14 · [drosera#283](https://github.com/lentago/drosera/pull/283) — Retire "homelab"/"lab" wording for on-prem
- 2026-10-14 · [osmunda#17](https://github.com/lentago/osmunda/pull/17) — osmunda: retire "homelab"/"lab" wording for on-prem
- 2026-10-14 · [claytonia#148](https://github.com/lentago/claytonia/pull/148) — Retire "homelab"/"lab" wording for on-prem
- 2026-10-14 · [kalmia#159](https://github.com/lentago/kalmia/pull/159) — Retire "homelab"/"lab" and "household" wording for on-prem
- 2026-10-04 · [epigaea#522](https://github.com/lentago/epigaea/pull/522) — fix: point live repository_dispatch targets at epigaea
- 2026-10-04 · [betula#112](https://github.com/lentago/betula/pull/112) — fix(firewalla): Fluent Bit boot race — wait for Zeek + delivery liveness check

</details>

### Fleet secrets handling (ADR-0011): the follow-through

[.github#286](https://github.com/lentago/.github/issues/286) · open since 2026-10-30 · last activity 2026-10-30

> Tracking issue for the work ADR-0011 (how the fleet handles secrets, accepted 2026-10-07) left open: identity before secrets, values only in approved stores, Terraform holds slots not values, out-of-band values verified, scanning and push protection on every repo, leaks rotated not scrubbed.

Progress: **0/9** sub-issues closed · **3** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [.github#225](https://github.com/lentago/.github/issues/225) FLEET_ADMIN_TOKEN cannot resolve GitHub App node ids: merge-gate App allowances are unmanageable by Terraform
- ⬜ [.github#242](https://github.com/lentago/.github/issues/242) Re-mint two over-broad GitHub tokens: FLEET_REPORTS_TOKEN and the workstation PAT
- ⬜ [.github#243](https://github.com/lentago/.github/issues/243) Credential register: every fleet credential's store, scope, issuer and expiry (names only)
- ⬜ [.github#271](https://github.com/lentago/.github/issues/271) [renewal] FLEET_REPORTS_TOKEN — fine-grained PAT expiry — due 2026-10-30
- ⬜ [osmunda#12](https://github.com/lentago/osmunda/issues/12) Decide how Flux-managed workloads receive secrets, before the n8n cutover
- ⬜ [solidago#149](https://github.com/lentago/solidago/issues/149) Rotating a Lambda's Axiom token requires an unrelated apply to take effect
- ⬜ [solidago#156](https://github.com/lentago/solidago/issues/156) Split plan/apply OIDC environments so the terraform environment can carry a branch policy
- ⬜ [solidago#213](https://github.com/lentago/solidago/issues/213) Fail the apply when an out-of-band secret still holds its placeholder
- ⬜ [solidago#222](https://github.com/lentago/solidago/issues/222) monitoring: pass the alert recipient as a sensitive variable, out of committed config and public plan output

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-10-07 · [.github#245](https://github.com/lentago/.github/pull/245) — ADR-0011: how the fleet handles secrets
- 2026-10-07 · [.github#241](https://github.com/lentago/.github/pull/241) — Enable secret scanning and push protection on every fleet repo
- 2026-10-04 · [.github#226](https://github.com/lentago/.github/pull/226) — merge gate: the template-sync App allowance is live-only until the fleet token can resolve App nodes

</details>

### Roadmap: core/client split — Firewalla and solidago (AWS) as peer collector clients

[betula#74](https://github.com/lentago/betula/issues/74) · open since 2026-07-04 · last activity 2026-08-16

> Betula's goal is to be the Lentago Labs log capture-and-archive layer, not a Firewalla tool.

Progress: **0/2** sub-issues closed · **5** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [betula#106](https://github.com/lentago/betula/issues/106) Third AWS emitter: CloudTrail → archive + weekly access digest
- ⬜ [betula#119](https://github.com/lentago/betula/issues/119) Terraform the Axiom tokens (exact import + rotation handoff)

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-10-12 · [lupinus#25](https://github.com/lentago/lupinus/pull/25) — Stories: one spine, three rungs, one map; one canonical product list
- 2026-10-07 · [.github#245](https://github.com/lentago/.github/pull/245) — ADR-0011: how the fleet handles secrets
- 2026-10-06 · [shared-workflows#63](https://github.com/lentago/shared-workflows/pull/63) — Add Axiom datasets and Firewalla on-box config to the enforced-surfaces table
- 2026-10-06 · [betula#120](https://github.com/lentago/betula/pull/120) — Terraform the Axiom side: datasets, retention, ingest tokens
- 2026-10-01 · [lupinus#11](https://github.com/lentago/lupinus/pull/11) — Add guide/stories: five shops, one tech person each

</details>

### Phase 3: the fleet on the display, and what stays open after ADR-0020

[brasenia#130](https://github.com/lentago/brasenia/issues/130) · open since 2026-10-30 · last activity 2026-10-30

> Tracking issue for the display's third phase (docs/concept.md, Phase 3: the governance snippet reaches every local Claude and the fleet, and panes arrive from real activity) and for the items left open after October's wall work.

Progress: **1/9** sub-issues closed · **8** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [brasenia#15](https://github.com/lentago/brasenia/issues/15) Adopt the display guest (LXC 118) capacity from kalmia
- ⬜ [brasenia#17](https://github.com/lentago/brasenia/issues/17) Live-ingest pane: concept + ADR, acceptance spec, and VideoScene repoint to `live` with board fallback
- ⬜ [brasenia#31](https://github.com/lentago/brasenia/issues/31) Focus producer: unauthenticated 304s spend the GitHub budget, so focus panes refresh every few minutes, not every minute
- ⬜ [brasenia#43](https://github.com/lentago/brasenia/issues/43) README intro still calls the pane bus and compositor "the roadmap"; ADR-0008 says they run
- ⬜ [brasenia#51](https://github.com/lentago/brasenia/issues/51) Pane bus: a producer's author check isn't atomic with its write, so a claim made in between gets overwritten
- ⬜ [brasenia#99](https://github.com/lentago/brasenia/issues/99) Roku: on a switch, show the new pane's still image until the stream catches up
- ⬜ [brasenia#123](https://github.com/lentago/brasenia/issues/123) Close out the 1280×720 pane contract once the external search panes move (ADR-0019)
- ⬜ [claytonia#137](https://github.com/lentago/claytonia/issues/137) brasenia on the fleet: share mount on the workers, pane command in the worker prompt, fleet beacons
- ✅ [kalmia#99](https://github.com/lentago/kalmia/issues/99) Cast client runtime for brasenia: watchdog sender, receiver hosting, then HLS-stack turn-down (brasenia ADR-0006)

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-10-30 · [brasenia#124](https://github.com/lentago/brasenia/pull/124) — Migrate the family brief to one 1920×1080 band and retire its desk editions (ADR-0019, ADR-0020)
- 2026-10-30 · [brasenia#120](https://github.com/lentago/brasenia/pull/120) — docs: record the RTMP live-ingest retirement on ADR-0007
- 2026-10-30 · [kalmia#224](https://github.com/lentago/kalmia/pull/224) — brasenia: retire RTMP live ingest and remove mediamtx
- 2026-10-28 · [kalmia#175](https://github.com/lentago/kalmia/pull/175) — lunaria: retire the Cast receiver watchdog (the role now ensures it is absent)
- 2026-10-28 · [brasenia#53](https://github.com/lentago/brasenia/pull/53) — Office Roku: 4K family-brief client (HEVC over HLS); retire the play-room Roku client
- 2026-10-28 · [kalmia#168](https://github.com/lentago/kalmia/pull/168) — lunaria: 4K HEVC family-brief stream for the office Roku; retire the 720p board stream
- 2026-10-08 · [brasenia#38](https://github.com/lentago/brasenia/pull/38) — fix(focus): show main's latest meaningful push run
- 2026-10-07 · [brasenia#33](https://github.com/lentago/brasenia/pull/33) — feat(producers): focus producer — open-PRs pane per beaconed repo

</details>

### Roadmap: platform-agnostic workers — Claude Code as one runtime behind the queue contract

[claytonia#47](https://github.com/lentago/claytonia/issues/47) · open since 2026-07-04 · last activity 2026-08-16

> Fleet principle: agnosticism and portability.

Progress: **0/2** sub-issues closed · **0** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [claytonia#99](https://github.com/lentago/claytonia/issues/99) Second job type: batch document/report jobs through the queue contract
- ⬜ [claytonia#116](https://github.com/lentago/claytonia/issues/116) Close the loop after the PR opens: a capped follow-up job for failing checks and review comments

</details>

### Roadmap to MVP: prove the desk, file on the user's behalf, run it unattended

[mitchella#31](https://github.com/lentago/mitchella/issues/31) · open since 2026-10-30 · last activity 2026-10-30

> Tracking issue for ROADMAP.md, so the three milestones show their progress as sub-issues.

Progress: **1/12** sub-issues closed · **3** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [mitchella#1](https://github.com/lentago/mitchella/issues/1) Exercise the real API path end to end
- ⬜ [mitchella#2](https://github.com/lentago/mitchella/issues/2) Hold a conversation: thread context across turns
- ⬜ [mitchella#4](https://github.com/lentago/mitchella/issues/4) ADR: supersede ADR-0005 to authorise one scoped write path
- ⬜ [mitchella#5](https://github.com/lentago/mitchella/issues/5) Slack: confirm-before-file button and modal
- ⬜ [mitchella#6](https://github.com/lentago/mitchella/issues/6) Issue tracker client: turn a confirmed draft into a filing
- ⬜ [mitchella#7](https://github.com/lentago/mitchella/issues/7) Decide attribution: service account or per-user OAuth
- ⬜ [mitchella#8](https://github.com/lentago/mitchella/issues/8) Filing controls: idempotency, rate limits, kill switch, audit
- ⬜ [mitchella#9](https://github.com/lentago/mitchella/issues/9) Deploy the desk so it outlives a terminal
- ⬜ [mitchella#10](https://github.com/lentago/mitchella/issues/10) Ship telemetry to drosera
- ⬜ [mitchella#11](https://github.com/lentago/mitchella/issues/11) An eval set, so changes are measurable
- ⬜ [mitchella#12](https://github.com/lentago/mitchella/issues/12) Bound the cost: caps and reporting
- ✅ [mitchella#3](https://github.com/lentago/mitchella/issues/3) Slack hardening: visible failures, block limits, retries

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-10-12 · [lupinus#25](https://github.com/lentago/lupinus/pull/25) — Stories: one spine, three rungs, one map; one canonical product list
- 2026-10-12 · [lupinus#22](https://github.com/lentago/lupinus/pull/22) — Tiers: refresh brasenia, add mitchella; picker: phones, printers, Wi-Fi
- 2026-10-04 · [mitchella#17](https://github.com/lentago/mitchella/pull/17) — Slack hardening: visible failures, block limits, retries

</details>

### Rung 2: the plain organization site, with a rescue import and editing without git — epic

[monarda#18](https://github.com/lentago/monarda/issues/18) · open since 2026-10-12 · last activity 2026-10-12

> Three of the five lupinus stories lean on monarda and two of them need the organization's whole site; the import story only pays off if that page set exists.

Progress: **3/3** sub-issues closed · checklist **3/4** · **4** PRs merged in the window

<details><summary>Sub-issues</summary>

- ✅ [monarda#22](https://github.com/lentago/monarda/issues/22) Rung 2: the plain organization site page set (home, about, programs, events, donate, contact)
- ✅ [monarda#23](https://github.com/lentago/monarda/issues/23) Rescue import: WordPress and Squarespace exports to rung-2 Markdown; Wayback as the last resort
- ✅ [monarda#24](https://github.com/lentago/monarda/issues/24) Editing without git: a git-backed editor (Sveltia CMS or Pages CMS) in front of the organization's own repository

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-10-12 · [monarda#28](https://github.com/lentago/monarda/pull/28) — feat: rescue import for WordPress and Squarespace exports
- 2026-10-12 · [monarda#27](https://github.com/lentago/monarda/pull/27) — docs: editing without git (Sveltia CMS, off by default)
- 2026-10-12 · [monarda#26](https://github.com/lentago/monarda/pull/26) — feat: rung 2, the plain organization site page set
- 2026-10-12 · [monarda#25](https://github.com/lentago/monarda/pull/25) — ADR-0004: a second rung, the plain organization site

</details>

---

## Closed in the last 90 days — 3

| Closed | Epic | Sub-issues | Still open underneath | PRs (30d) |
|--------|------|-----------:|----------------------:|----------:|
| 2026-10-13 | [drosera#251](https://github.com/lentago/drosera/issues/251) Change pipeline: see every merge travel from push to live, keyed by commit SHA | 1 | **1** | 20 |
| 2026-10-13 | [lupinus#4](https://github.com/lentago/lupinus/issues/4) Epic: adoption guide — Phase 1 (launch set: solidago + monarda) | 5 | 0 | 3 |
| 2026-08-19 | [.github#162](https://github.com/lentago/.github/issues/162) Epic: adoption guide (lupinus) — Phase 0 enablers | 4 | 0 | 1 |

A closed epic with open sub-issues is a hand-off: the work was spun out and still owes a result.

---

## Where the last 30 days went

**619 PRs merged** across the fleet. Each is attributed once (an epic, or one loose bucket); a PR that serves two epics counts for both.

| Destination | PRs | Share |
|-------------|----:|------:|
| [.github#134](https://github.com/lentago/.github/issues/134) Offerings roadmap — tracking epic (refreshed 2026-10-06) | 41 | 7% |
| [.github#285](https://github.com/lentago/.github/issues/285) Rename debt: the tier 3–4 renames still open across the fleet | 22 | 4% |
| [drosera#251](https://github.com/lentago/drosera/issues/251) Change pipeline: see every merge travel from push to live, keyed by commit SHA _(closed)_ | 20 | 3% |
| [.github#235](https://github.com/lentago/.github/issues/235) Genus marks for the eight unmarked species | 11 | 2% |
| [brasenia#130](https://github.com/lentago/brasenia/issues/130) Phase 3: the fleet on the display, and what stays open after ADR-0020 | 8 | 1% |
| [betula#74](https://github.com/lentago/betula/issues/74) Roadmap: core/client split — Firewalla and solidago (AWS) as peer collector clients | 5 | 1% |
| [monarda#18](https://github.com/lentago/monarda/issues/18) Rung 2: the plain organization site, with a rescue import and editing without git — epic | 4 | 1% |
| [lupinus#4](https://github.com/lentago/lupinus/issues/4) Epic: adoption guide — Phase 1 (launch set: solidago + monarda) _(closed)_ | 3 | 0% |
| [mitchella#31](https://github.com/lentago/mitchella/issues/31) Roadmap to MVP: prove the desk, file on the user's behalf, run it unattended | 3 | 0% |
| [.github#286](https://github.com/lentago/.github/issues/286) Fleet secrets handling (ADR-0011): the follow-through | 3 | 0% |
| [.github#234](https://github.com/lentago/.github/issues/234) Enable Dependabot security updates fleet-wide (codified in terraform) | 1 | 0% |
| [.github#162](https://github.com/lentago/.github/issues/162) Epic: adoption guide (lupinus) — Phase 0 enablers _(closed)_ | 1 | 0% |
| **All epics** | **113** | **18%** |
| Loose — closes or cites an issue outside any epic | 346 | 56% |
| Loose — no issue reference at all | 61 | 10% |
| Dependabot | 81 | 13% |
| Fleet automation (report refreshes, template sync) | 18 | 3% |

### De-facto epics

Issues outside any epic that at least 4 merged PRs reference. Each is a campaign that ran on a single issue; if it is still open, it is a candidate for the `epic` label or a parent.

| Issue | PRs | Repos touched | State |
|-------|----:|--------------:|-------|
| [uvularia#28](https://github.com/lentago/uvularia/issues/28) Sync templates/records and templates/site to their GitHub template repos on merge | 33 | 7 | open |
| [shared-workflows#64](https://github.com/lentago/shared-workflows/issues/64) ADR-0005 migration: move the remaining @main callers to v1.2.3 | 32 | 19 | closed |
| [.github#276](https://github.com/lentago/.github/issues/276) Haiku replaces CodeRabbit as the fleet's PR reviewer | 22 | 17 | open |
| [.github#257](https://github.com/lentago/.github/issues/257) Adopt the six-promise map (ADR-0012) — rollout epic | 20 | 14 | closed |
| [.github#237](https://github.com/lentago/.github/issues/237) Retire DeepWiki across the fleet | 20 | 20 | open |
| [.github#192](https://github.com/lentago/.github/issues/192) Epic: reposition every reader-facing surface to the pro-bono practice, one reader, one voice (ADR-0008) | 20 | 18 | closed |
| [.github#229](https://github.com/lentago/.github/issues/229) Fleet alignment 2026-10-06: stale repos.json facts and ready-to-require checks | 19 | 15 | closed |
| [kalmia#63](https://github.com/lentago/kalmia/issues/63) Complete the lunaria → brasenia rename through runtime | 9 | 2 | closed |
| [shared-workflows#56](https://github.com/lentago/shared-workflows/issues/56) chore(deps): Bump the actions-routine group with 3 updates | 7 | 7 | closed |
| [kalmia#194](https://github.com/lentago/kalmia/issues/194) lunaria: one renderer for the stream and the peek, rendering every pane ahead | 6 | 2 | closed |
| [.github#113](https://github.com/lentago/.github/issues/113) Fleet sweep: pin third-party actions to commit SHAs; pin container bases to digests | 6 | 5 | closed |
| [.github#201](https://github.com/lentago/.github/issues/201) terraform: creating a repo from repos.json fails on GitHub's default labels (422 already_exists) | 6 | 1 | open |
| [brasenia#97](https://github.com/lentago/brasenia/issues/97) Link panes: put any web page in a slot (pane claim --url, standing slots in the configurator) | 5 | 2 | closed |
| [.github#269](https://github.com/lentago/.github/issues/269) Scrub "homelab" and kin: the on-prem half of the estate is "on-prem" | 5 | 5 | closed |
| [brasenia#121](https://github.com/lentago/brasenia/issues/121) Compositor: a strict total order, no rotation (ADR-0020: "There should not be ties") | 4 | 1 | closed |
| [kalmia#207](https://github.com/lentago/kalmia/issues/207) pub: brasenia-compositor fails to start, Restart= line joined onto ExecStart | 4 | 1 | closed |
| [.github#264](https://github.com/lentago/.github/issues/264) music-curator leaves the org for cpitzi/music-curator | 4 | 4 | closed |
| [kalmia#140](https://github.com/lentago/kalmia/issues/140) Run the brasenia compositor and focus producer on pub (LXC 114) from /srv/brasenia | 4 | 2 | closed |
| [drosera#243](https://github.com/lentago/drosera/issues/243) Retire drosera's device-inventory publisher after the betula move; decide its egress path (ADR-0006) | 4 | 2 | closed |

### Loose work by repo

Where the merged work that no epic describes landed. A tall row is either a program that deserves an epic, or a repo whose convention is direct PRs.

| Repo | With an issue | No issue | Total |
|------|--------------:|---------:|------:|
| brasenia | 50 | 1 | **51** |
| kalmia | 48 | 1 | **49** |
| .github | 33 | 6 | **39** |
| uvularia | 23 | 11 | **34** |
| drosera | 31 | 2 | **33** |
| claytonia | 21 | 1 | **22** |
| site-lentago-dev | 10 | 8 | **18** |
| uvularia-demo-records | 9 | 8 | **17** |
| solidago | 10 | 5 | **15** |
| uvularia-demo-ask-rules | 5 | 10 | **15** |
| betula | 14 | 0 | **14** |
| shared-workflows | 9 | 1 | **10** |
| uvularia-records-template | 9 | 0 | **9** |
| asclepias | 8 | 0 | **8** |
| lupinus | 7 | 1 | **8** |
| osmunda | 7 | 0 | **7** |
| mitchella | 7 | 0 | **7** |
| epigaea | 7 | 0 | **7** |
| uvularia-rules-template | 7 | 0 | **7** |
| repo-template | 6 | 0 | **6** |
| monarda | 6 | 0 | **6** |
| uvularia-demo-site | 1 | 5 | **6** |
| site-pondviewlane-com | 5 | 0 | **5** |
| site-icecreamtofightwith-com | 5 | 0 | **5** |
| uvularia-site-template | 5 | 0 | **5** |
| coderabbit | 3 | 1 | **4** |

---

## Open issues outside any epic — 52

The backlog the epics do not describe. Some of it is deliberately small and stand-alone; the rest is either a program without a parent or an issue that should be linked under one.

**drosera** — 13

- [drosera#295](https://github.com/lentago/drosera/issues/295) Map-keyed dynamic rule blocks rewrite every later rule when a new key sorts mid-list _(since 2026-10-30)_
- [drosera#272](https://github.com/lentago/drosera/issues/272) Notification-sink contract: one event shape, four sinks, "who gets the call" as a file _(since 2026-10-12)_
- [drosera#264](https://github.com/lentago/drosera/issues/264) terraform: cloud_usage rule group shows a perpetual repeat_interval diff (1d vs 24h) _(since 2026-10-07)_
- [drosera#204](https://github.com/lentago/drosera/issues/204) Main-branch workflow failures notify nobody — alert on red deploys/applies _(since 2026-08-17)_
- [drosera#200](https://github.com/lentago/drosera/issues/200) Queue SLO for the agent fleet (pickup latency) + burn alert _(since 2026-08-16)_
- [drosera#199](https://github.com/lentago/drosera/issues/199) Error-budget monthly section in the fleet report _(since 2026-08-16)_
- [drosera#198](https://github.com/lentago/drosera/issues/198) Threat Weather: anonymized daily network weather report _(since 2026-08-16)_
- [drosera#194](https://github.com/lentago/drosera/issues/194) Adopt grafana-stack (LXC 105) guest capacity from kalmia _(since 2026-08-14)_
- [drosera#165](https://github.com/lentago/drosera/issues/165) New-domain radar: alert when an IoT/smart-home device queries a never-before-seen domain (migrated from betula#11) _(since 2026-07-20)_
- [drosera#131](https://github.com/lentago/drosera/issues/131) Roadmap: multi-client telemetry pane — homelab and solidago (AWS) as peer sources _(since 2026-07-04)_
- [drosera#103](https://github.com/lentago/drosera/issues/103) Scrape node_exporter on the Firewalla via Alloy (bring the gateway into node dashboards) _(since 2026-07-02)_
- [drosera#101](https://github.com/lentago/drosera/issues/101) Heartbeat blind spot: tool-less reasoning turns show no activity while tokens burn _(since 2026-07-01)_
- [drosera#93](https://github.com/lentago/drosera/issues/93) feat(alloy): attach runid label to the transcript stream from the <sid>.runid sidecar _(since 2026-06-19)_

**kalmia** — 7

- [kalmia#230](https://github.com/lentago/kalmia/issues/230) containers: remove or refuse the docker snap, which takes over apt docker-ce's socket _(since 2026-10-30)_
- [kalmia#198](https://github.com/lentago/kalmia/issues/198) pe-publish: close the job guard's cancellation window with a publish the runner can't trigger alone _(since 2026-10-29)_
- [kalmia#124](https://github.com/lentago/kalmia/issues/124) Retire CT 113 (n8n LXC) after the osmunda burn-in window _(since 2026-08-18)_
- [kalmia#108](https://github.com/lentago/kalmia/issues/108) Forge: golden images with receipts (checksums, SBOM, provenance) _(since 2026-08-16)_
- [kalmia#51](https://github.com/lentago/kalmia/issues/51) Guarantee vzdump coverage for every Terraform-enforced guest (CT 113 had none) _(since 2026-07-13)_
- [kalmia#20](https://github.com/lentago/kalmia/issues/20) Roadmap: provisioning clients beyond Ansible-on-workstations — VMs and containers as peer targets _(since 2026-07-04)_
- [kalmia#14](https://github.com/lentago/kalmia/issues/14) Live-test the ubuntu_laptop profile on real ThinkPad hardware _(since 2026-07-01)_

**solidago** — 6

- [solidago#220](https://github.com/lentago/solidago/issues/220) iam: give the cross-repo Terraform pipeline roles a read-only plan path _(since 2026-10-30)_
- [solidago#184](https://github.com/lentago/solidago/issues/184) CI plans are never clean: standing task-definition replacements and a recreating SNS email subscription _(since 2026-08-19)_
- [solidago#180](https://github.com/lentago/solidago/issues/180) Hardening backlog from tf-lint's first trivy run (ECR immutability, CI-role least-privilege, SNS encryption) _(since 2026-08-17)_
- [solidago#167](https://github.com/lentago/solidago/issues/167) DMARC posture on our own domains first (precondition for the Email Trust kit) _(since 2026-08-16)_
- [solidago#144](https://github.com/lentago/solidago/issues/144) Ask Lambda logs land in CloudWatch with no path to Axiom _(since 2026-07-24)_
- [solidago#21](https://github.com/lentago/solidago/issues/21) Evaluate migration from ElastiCache node-based to serverless _(since 2026-03-19)_

**betula** — 5

- [betula#148](https://github.com/lentago/betula/issues/148) GitHub collector README: dry-run example puts secrets in argv _(since 2026-10-30)_
- [betula#147](https://github.com/lentago/betula/issues/147) Cover the pe-publish runner (LXC 123) in the queued-jobs feed _(since 2026-10-30)_
- [betula#133](https://github.com/lentago/betula/issues/133) GitHub Actions feed: carry the PR number so PR head SHAs join to merge commits (drosera ADR-0010) _(since 2026-10-07)_
- [betula#130](https://github.com/lentago/betula/issues/130) GitHub collector: first-tick backfill ran 7.5 min against a 10 min TimeoutStartSec; checkpoint per repo and reuse connections _(since 2026-10-07)_
- [betula#107](https://github.com/lentago/betula/issues/107) Device drift self-report: deployed conf hash vs main _(since 2026-08-16)_

**.github** — 4

- [.github#276](https://github.com/lentago/.github/issues/276) Haiku replaces CodeRabbit as the fleet's PR reviewer _(since 2026-10-29)_
- [.github#237](https://github.com/lentago/.github/issues/237) Retire DeepWiki across the fleet _(since 2026-10-07)_
- [.github#201](https://github.com/lentago/.github/issues/201) terraform: creating a repo from repos.json fails on GitHub's default labels (422 already_exists) _(since 2026-10-03)_
- [.github#175](https://github.com/lentago/.github/issues/175) A public repo entry with a null template_source cannot receive its first commit _(since 2026-08-28)_

**uvularia** — 4

- [uvularia#98](https://github.com/lentago/uvularia/issues/98) Intake hint says "under library/" but validate resolves source.file from the repo root; first record fails the PR _(since 2026-10-12)_
- [uvularia#91](https://github.com/lentago/uvularia/issues/91) templates/site: astro check fails on TypeScript 6 (28 strict-mode errors) _(since 2026-10-07)_
- [uvularia#57](https://github.com/lentago/uvularia/issues/57) Records need an event time, and deadlines a local timezone, for lead rules to match the statute for evening meetings _(since 2026-10-04)_
- [uvularia#28](https://github.com/lentago/uvularia/issues/28) Sync templates/records and templates/site to their GitHub template repos on merge _(since 2026-10-03)_

**claytonia** — 3

- [claytonia#117](https://github.com/lentago/claytonia/issues/117) Make never-merge a boundary: required check that blocks runner-App PRs without a human approval _(since 2026-09-17)_
- [claytonia#115](https://github.com/lentago/claytonia/issues/115) An eval set for the fleet: replayable tasks, deterministic graders, and outcome measures _(since 2026-09-17)_
- [claytonia#24](https://github.com/lentago/claytonia/issues/24) Branch hygiene across overlapping sessions: clean-desk session-end + prefer fleet dispatch _(since 2026-06-20)_

**lupinus** — 2

- [lupinus#9](https://github.com/lentago/lupinus/issues/9) Reconcile the single-file ADOPTION.md template with the INTAKE/DRY-RUN split the exemplar uses _(since 2026-10-01)_
- [lupinus#8](https://github.com/lentago/lupinus/issues/8) Kit rows carry no receipt: mark them provisional or demote until a drill is recorded _(since 2026-10-01)_

**monarda** — 2

- [monarda#19](https://github.com/lentago/monarda/issues/19) First run is red: deploy-pages triggers on the template's initial commit before Pages is enabled _(since 2026-10-12)_
- [monarda#17](https://github.com/lentago/monarda/issues/17) Processor presets in the donate block, each with a sandbox walkthrough; one of them is the #5 receipt _(since 2026-10-12)_

**site-lentago-dev** — 2

- [site-lentago-dev#86](https://github.com/lentago/site-lentago-dev/issues/86) Remove committed .playwright-mcp/ scratch output and gitignore it _(since 2026-10-03)_
- [site-lentago-dev#67](https://github.com/lentago/site-lentago-dev/issues/67) a11y gate ignores `color-contrast`: the Tidewater palette fails 4.5:1 at the design-token level _(since 2026-08-26)_

**osmunda** — 1

- [osmunda#4](https://github.com/lentago/osmunda/issues/4) The k3s install is disclaimed by both osmunda and kalmia — it exists nowhere _(since 2026-08-21)_

**shared-workflows** — 1

- [shared-workflows#57](https://github.com/lentago/shared-workflows/issues/57) Rapid successive merges cancel site deploys, and `:latest`-pinned task defs make the survivor non-deterministic _(since 2026-08-30)_

**site-icecreamtofightwith-com** — 1

- [site-icecreamtofightwith-com#158](https://github.com/lentago/site-icecreamtofightwith-com/issues/158) Tier accent swatches fail WCAG AA contrast as chip/step backgrounds (design decision needed) _(since 2026-08-16)_

**site-pondviewlane-com** — 1

- [site-pondviewlane-com#46](https://github.com/lentago/site-pondviewlane-com/issues/46) Flip Content-Security-Policy from Report-Only to enforcing _(since 2026-08-16)_

---

## Method

- **Epics:** `gh search issues --owner lentago --label epic` (open, plus closed within 90 days) ∪ every open issue with sub-issues and no parent. A labelled epic that sits under a parent renders there, not at top level.
- **Sub-issues:** GitHub's native parent/child links, read through the REST `sub_issues` endpoint and followed 3 levels deep. They cross repos inside the org. Link one with `gh api -X POST repos/lentago/<repo>/issues/<epic>/sub_issues -F sub_issue_id=<child id>`.
- **Attribution:** a merged PR counts toward an epic when the epic's body or comments cite the PR, or when the PR's body references an issue in the epic's tree (or the epic itself). Otherwise it is loose: with an issue, or without one. Dependabot and the fleet's own bots are set aside.
- **Limits:** a citation is a citation — an epic that mentions a PR as an example counts it as work. An issue cannot have two parents, so a piece of work that serves two programs sits under one; the other may still cite it.
- **Regenerating:** `python3 metrics/generate-fleet-reports.py --out-dir . --epics-only` (needs `gh`, not `cloc`).

_Generated with Claude Code (Repo Claude)._
