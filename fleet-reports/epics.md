# Lentago Labs Epics Report

> [!NOTE]
> **Co-authored with [Claude](https://claude.ai)** (Repo Claude, the Lentago Labs fleet steward). Auto-generated weekly from the fleet's public state. An **epic** here is a tracking issue: one labelled `epic`, or an open issue with sub-issues and no parent of its own. Progress is GitHub's own sub-issue count plus the issue's checklist, so an epic that is not kept up to date shows as not moving — that is the point. The sibling [fleet report](fleet-report.md) lists every open issue; this one asks what the issues add up to, and how much of the merged work they describe.

**Generated:** 2026-11-09 21:44 UTC · Scope: the **26 active** `lentago` repos · Merged-PR window: last 30 days (since 2026-10-10) · closed epics shown for 90 days.

## Snapshot

| Open epics | Closed epics (90d) | Open issues under an epic | Merged PRs (30d) | …that trace to an epic | …loose, with an issue | …loose, no issue | …bots |
|---:|---:|---:|---:|---:|---:|---:|---:|
| **18** | 13 | **125 / 190** (66%) | 512 | **268** (62% of non-bot) | 151 | 12 | 81 |

The *trace to an epic* share is the headline: how much of the month's merged work the epics describe. The two loose columns are work that happened outside any epic — tracked by a stand-alone issue, or by nothing but the PR. Bots are Dependabot and the fleet's own automation, excluded from the share. *Open issues under an epic* counts the issues other than the epics themselves; its complement is the list at the end.

---

## Open epics — 18

| Epic | Since | Sub-issues closed | Checklist | PRs (30d) | Last activity |
|------|-------|-------------------|-----------|----------:|---------------|
| [.github#318](https://github.com/lentago/.github/issues/318) Security review 2026-11-02: fleet follow-through | 2026-11-02 | `████████░░` 20/24 | 0/12 | 59 ⚠︎ 2 known from comments only | 2026-11-05 |
| [.github#285](https://github.com/lentago/.github/issues/285) Rename debt: the tier 3–4 renames still open across the fleet | 2026-10-30 | `██░░░░░░░░` 2/13 | — | 41 | 2026-10-30 |
| [.github#304](https://github.com/lentago/.github/issues/304) External review 2026-11-01: fleet follow-through | 2026-11-01 | `███████░░░` 19/27 | 20/30 | 30 | 2026-11-02 |
| [claytonia#117](https://github.com/lentago/claytonia/issues/117) Make never-merge a boundary: required check that blocks runner-App PRs without a human approval | 2026-09-17 | `██████████` 2/2 | — | 29 ⚠︎ 1 known from comments only | 2026-11-02 |
| [.github#276](https://github.com/lentago/.github/issues/276) Haiku replaces CodeRabbit as the fleet's PR reviewer | 2026-10-29 | — | 24/25 | 26 ⚠︎ 1 known from comments only | 2026-10-30 |
| [claytonia#47](https://github.com/lentago/claytonia/issues/47) Roadmap: platform-agnostic workers — Claude Code as one runtime behind the queue contract | 2026-07-04 | `████░░░░░░` 7/18 | 1/3 | 26 | 2026-11-04 |
| [epigaea#548](https://github.com/lentago/epigaea/issues/548) Signage: cards, labels and sheets posted at the point of use | 2026-10-31 | — | 14/15 | 17 | 2026-11-04 |
| [.github#134](https://github.com/lentago/.github/issues/134) Offerings roadmap — tracking epic (refreshed 2026-10-06) | 2026-08-16 | `████░░░░░░` 18/50 | 7/8 | 14 ⚠︎ 1 known from comments only | 2026-11-04 |
| [betula#74](https://github.com/lentago/betula/issues/74) Roadmap: core/client split — Firewalla and solidago (AWS) as peer collector clients | 2026-07-04 | `█░░░░░░░░░` 1/8 | 0/3 | 12 | 2026-10-30 |
| [brasenia#130](https://github.com/lentago/brasenia/issues/130) Phase 3: the fleet on the display, and what stays open after ADR-0020 | 2026-10-30 | `██████░░░░` 5/9 | — | 12 | 2026-10-30 |
| [uvularia#28](https://github.com/lentago/uvularia/issues/28) Template repositories: sync on merge (shipped 2026-10-06), drift, and their upkeep — epic | 2026-10-03 | `█████░░░░░` 2/4 | — | 10 | 2026-10-30 |
| [monarda#18](https://github.com/lentago/monarda/issues/18) Rung 2: the plain organization site, with a rescue import and editing without git — epic | 2026-10-12 | `██████████` 5/5 | 3/4 | 7 | 2026-11-04 |
| [mitchella#31](https://github.com/lentago/mitchella/issues/31) Roadmap to MVP: prove the desk, file on the user's behalf, run it unattended | 2026-10-30 | `██░░░░░░░░` 2/12 | — | 5 | 2026-10-30 |
| [.github#286](https://github.com/lentago/.github/issues/286) Fleet secrets handling (ADR-0011): the follow-through | 2026-10-30 | `█░░░░░░░░░` 1/10 | — | 4 | 2026-10-30 |
| [drosera#131](https://github.com/lentago/drosera/issues/131) Roadmap: multi-client telemetry pane — on-prem and solidago (AWS) as peer sources | 2026-07-04 | `░░░░░░░░░░` 0/7 | 0/3 | 2 | 2026-10-30 |
| [.github#235](https://github.com/lentago/.github/issues/235) Genus marks for the eight unmarked species | 2026-10-07 | `░░░░░░░░░░` 0/2 | 11/13 | 1 | 2026-10-30 |
| [kalmia#20](https://github.com/lentago/kalmia/issues/20) Roadmap: provisioning clients beyond Ansible-on-workstations — VMs and containers as peer targets | 2026-07-04 | `░░░░░░░░░░` 0/7 | 0/3 | 1 | 2026-10-30 |
| [lupinus#40](https://github.com/lentago/lupinus/issues/40) Epic: adoption guide — Phase 3 (receipts for the four near-Kits) | 2026-11-04 | `░░░░░░░░░░` 0/4 | — | 1 | 2026-11-04 |

*Sub-issues closed* is GitHub's native parent/child count (it crosses repos). *Checklist* is the `- [ ]` boxes in the epic's body. ⚠︎ counts merged PRs this report could attribute to the epic only because a comment on the epic cites them: neither the body nor a sub-issue names them, so a reader of the epic's face would miss that work.

### Offerings roadmap — tracking epic (refreshed 2026-10-06)

[.github#134](https://github.com/lentago/.github/issues/134) · open since 2026-08-16 · last activity 2026-11-04

> Tracking epic for the offerings roadmap: the kits we would build next for the reader ADR-0008 names — the one tech person at an organization that runs on volunteers and donations.

Progress: **18/50** sub-issues closed · checklist **7/8** · **14** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [.github#122](https://github.com/lentago/.github/issues/122) Offering: Good-Standing Kit — registry reconciliation on the uvularia vault (MA pack first)
- ⬜ [.github#123](https://github.com/lentago/.github/issues/123) Offering: Liberation Pipeline — SaaS-export collectors + restore drills — 0/1 sub-issues closed
  - ⬜ [betula#126](https://github.com/lentago/betula/issues/126) Liberation Pipeline: SaaS-export collectors + restore drills, as betula clients (lentago/.github#123)
- ⬜ [.github#124](https://github.com/lentago/.github/issues/124) Offering: Digital Custody audit — ownership insurance for the org's presence
- ⬜ [.github#125](https://github.com/lentago/.github/issues/125) Offering: Insurance-Receipts Pack — controls with evidence exhaust — 0/5 sub-issues closed
  - ⬜ [.github#251](https://github.com/lentago/.github/issues/251) Offering: Email trust receipt — SPF, DKIM and DMARC as code, an MFA audit, the phishing habit — 0/1 sub-issues closed
    - ⬜ [solidago#167](https://github.com/lentago/solidago/issues/167) DMARC posture on our own domains first (precondition for the Email Trust kit)
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
- ⬜ [.github#200](https://github.com/lentago/.github/issues/200) Offering: uvularia — client-owned records vault, grounded Ask, live compliance board (supersedes #128) — 18/20 sub-issues closed
  - ⬜ [uvularia#57](https://github.com/lentago/uvularia/issues/57) Records need an event time, and deadlines a local timezone, for lead rules to match the statute for evening meetings
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
- ⬜ [.github#247](https://github.com/lentago/.github/issues/247) Offering: Accessible by default — every page checked, a receipt per build — 0/2 sub-issues closed
  - ⬜ [site-icecreamtofightwith-com#158](https://github.com/lentago/site-icecreamtofightwith-com/issues/158) Tier accent swatches fail WCAG AA contrast as chip/step backgrounds (design decision needed)
  - ⬜ [site-lentago-dev#67](https://github.com/lentago/site-lentago-dev/issues/67) a11y gate ignores `color-contrast`: the Tidewater palette fails 4.5:1 at the design-token level
- ⬜ [.github#248](https://github.com/lentago/.github/issues/248) Offering: EOL radar — support end dates open Issues before they bite
- ⬜ [.github#249](https://github.com/lentago/.github/issues/249) Offering: Board pack — a one-page monthly operations report the board actually reads
- ⬜ [brasenia#41](https://github.com/lentago/brasenia/issues/41) Lobby-pane variant: a visitor-facing screen in a client's own front room
- ⬜ [drosera#197](https://github.com/lentago/drosera/issues/197) "Are we open" single source of truth
- ⬜ [drosera#272](https://github.com/lentago/drosera/issues/272) Notification-sink contract: one event shape, four sinks, "who gets the call" as a file
- ⬜ [kalmia#107](https://github.com/lentago/kalmia/issues/107) Donated-hardware refresh profiles (new client class) — 0/1 sub-issues closed
  - ⬜ [kalmia#151](https://github.com/lentago/kalmia/issues/151) OS stance for a nonprofit fleet; ChromeOS Flex as the first donated-hardware profile

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-11-04 · [epigaea#577](https://github.com/lentago/epigaea/pull/577) — feat(signage): one shared stylesheet, copied into every piece and checked in CI
- 2026-11-01 · [site-lentago-dev#113](https://github.com/lentago/site-lentago-dev/pull/113) — Copy: response-time and migration promises match the support page; form labels lead with the task
- 2026-10-31 · [epigaea#547](https://github.com/lentago/epigaea/pull/547) — feat(cards): adopt printable instruction cards; first card is the Kitchen Speaker Dial
- 2026-10-30 · [.github#287](https://github.com/lentago/.github/pull/287) — Epics report: epics, sub-issue progress, and where the merged work went
- 2026-10-12 · [lupinus#25](https://github.com/lentago/lupinus/pull/25) — Stories: one spine, three rungs, one map; one canonical product list
- 2026-10-12 · [monarda#26](https://github.com/lentago/monarda/pull/26) — feat: rung 2, the plain organization site page set
- 2026-10-12 · [site-lentago-dev#100](https://github.com/lentago/site-lentago-dev/pull/100) — Suite: redraw #systems as the six-promise map (ADR-0012)
- 2026-10-12 · [.github#259](https://github.com/lentago/.github/pull/259) — Regroup the profile suite table by promise; taglines lead with role
- 2026-10-12 · [uvularia#99](https://github.com/lentago/uvularia/pull/99) — Receipts: one-repository rung timed (6 min 09 s); Ask box's first live answer
- 2026-10-12 · [lupinus#22](https://github.com/lentago/lupinus/pull/22) — Tiers: refresh brasenia, add mitchella; picker: phones, printers, Wi-Fi
- 2026-10-12 · [mitchella#26](https://github.com/lentago/mitchella/pull/26) — Record the uvularia Ask function as the first front desk (ADR-0007)
- 2026-10-12 · [monarda#21](https://github.com/lentago/monarda/pull/21) — Record the first timed dry-run: 3 min 01 s, two defects filed
- 2026-10-12 · [.github#255](https://github.com/lentago/.github/pull/255) — Profile suite rows for epigaea, brasenia; betula tagline off-device
- 2026-10-12 · [epigaea#530](https://github.com/lentago/epigaea/pull/530) — docs: facilities kit is tracked, not built — README and CLAUDE.md

</details>

### Genus marks for the eight unmarked species

[.github#235](https://github.com/lentago/.github/issues/235) · open since 2026-10-07 · last activity 2026-10-30

> Six of the fourteen in-org species carry a genus mark (lentago, solidago, drosera, kalmia, claytonia, betula).

Progress: **0/2** sub-issues closed · checklist **11/13** · **1** PR merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [.github#239](https://github.com/lentago/.github/issues/239) brand: README header blocks drifted from brand/generated in monarda, osmunda, shared-workflows; coderabbit has none
- ⬜ [.github#282](https://github.com/lentago/.github/issues/282) brand: genus marks render with black-filled leaves in banners and social cards

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-10-29 · [.github#281](https://github.com/lentago/.github/pull/281) — brand: generate a Roku home-screen poster for repos that ship a Roku channel

</details>

### Haiku replaces CodeRabbit as the fleet's PR reviewer

[.github#276](https://github.com/lentago/.github/issues/276) · open since 2026-10-29 · last activity 2026-10-30

> Replace CodeRabbit with the fleet's own Haiku reviewer (lentago/shared-workflows claude-review.yml) on every org repo except the kits and the uvularia demo repos.

Progress: checklist **24/25** · **26** PRs merged in the window

_No sub-issues linked — progress is visible only through the checklist and cited PRs._

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-10-30 · [.github#288](https://github.com/lentago/.github/pull/288) — Epics report refresh after the epic label landed
- 2026-10-30 · [.github#287](https://github.com/lentago/.github/pull/287) — Epics report: epics, sub-issue progress, and where the merged work went
- 2026-10-30 · [.github#284](https://github.com/lentago/.github/pull/284) — Retire lentago/coderabbit (ADR-0013 step 3)
- 2026-10-29 · [kalmia#211](https://github.com/lentago/kalmia/pull/211) — Rename lunaria to brasenia through runtime: rebuild LXC 118 as brasenia
- 2026-10-29 · [brasenia#107](https://github.com/lentago/brasenia/pull/107) — Roku: show the brasenia logo on the home screen
- 2026-10-29 · [claytonia#156](https://github.com/lentago/claytonia/pull/156) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 2026-10-29 · [uvularia#111](https://github.com/lentago/uvularia/pull/111) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 2026-10-29 · [solidago#218](https://github.com/lentago/solidago/pull/218) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 2026-10-29 · [site-pondviewlane-com#96](https://github.com/lentago/site-pondviewlane-com/pull/96) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 2026-10-29 · [site-lentago-dev#110](https://github.com/lentago/site-lentago-dev/pull/110) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 2026-10-29 · [site-icecreamtofightwith-com#211](https://github.com/lentago/site-icecreamtofightwith-com/pull/211) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 2026-10-29 · [shared-workflows#82](https://github.com/lentago/shared-workflows/pull/82) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 2026-10-29 · [osmunda#19](https://github.com/lentago/osmunda/pull/19) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 2026-10-29 · [mitchella#29](https://github.com/lentago/mitchella/pull/29) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 2026-10-29 · [kalmia#210](https://github.com/lentago/kalmia/pull/210) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 2026-10-29 · [.github#279](https://github.com/lentago/.github/pull/279) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 2026-10-29 · [epigaea#537](https://github.com/lentago/epigaea/pull/537) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 2026-10-29 · [drosera#288](https://github.com/lentago/drosera/pull/288) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 2026-10-29 · [brasenia#105](https://github.com/lentago/brasenia/pull/105) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 2026-10-29 · [betula#145](https://github.com/lentago/betula/pull/145) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 2026-10-29 · [asclepias#25](https://github.com/lentago/asclepias/pull/25) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 2026-10-29 · [repo-template#30](https://github.com/lentago/repo-template/pull/30) — ci: pin the PR reviewer to shared-workflows v1.5.0 (posts the review)
- 2026-10-29 · [shared-workflows#81](https://github.com/lentago/shared-workflows/pull/81) — claude-review: post the review as a PR comment; soft-fail on any result-less run (v1.5.0)
- 2026-10-29 · [repo-template#28](https://github.com/lentago/repo-template/pull/28) — ci: add the advisory Claude PR reviewer (ADR-0013 reference copy)
- 2026-10-29 · [shared-workflows#78](https://github.com/lentago/shared-workflows/pull/78) — Fleet PR-workflow: don't arm until the AI review is in and triaged
- 2026-10-29 · [.github#277](https://github.com/lentago/.github/pull/277) — ADR-0013: Haiku reviews every PR in the operating repos; CodeRabbit retires

</details>

### Rename debt: the tier 3–4 renames still open across the fleet

[.github#285](https://github.com/lentago/.github/issues/285) · open since 2026-10-30 · last activity 2026-10-30

> Tracking issue for the fleet's remaining rename debt under the rename discipline (shared-workflows/CLAUDE.md, "Rename discipline"): a rename is done when no surface carries the old name, or every surface that does is owned by an open tracking issue.

Progress: **2/13** sub-issues closed · **41** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [betula#89](https://github.com/lentago/betula/issues/89) Complete the firewalla-axiom-pipeline → betula rename on-device
- ⬜ [drosera#169](https://github.com/lentago/drosera/issues/169) Complete the homelab-observability → drosera rename through CI and hosts — 0/3 sub-issues closed
  - ⬜ [drosera#299](https://github.com/lentago/drosera/issues/299) On or after 2026-11-06: remove LXC 105's pre-move Alloy volume and unit copies (#169)
  - ⬜ [solidago#221](https://github.com/lentago/solidago/issues/221) On or after 2026-11-06: retire the pre-rename drosera Terraform role and state key (drosera#169 Phase 3)
  - ⬜ [solidago#223](https://github.com/lentago/solidago/issues/223) docs: list the betula and drosera cross-repo roles in ADOPTION.md, and scope BOOTSTRAP's locking note to solidago's own backend
- ⬜ [drosera#282](https://github.com/lentago/drosera/issues/282) Migrate the cluster="lentago-lab" label value to "onprem" across emitters
- ⬜ [epigaea#518](https://github.com/lentago/epigaea/issues/518) Complete the epigaea rename through runtime (tiers 3–4)
- ⬜ [epigaea#533](https://github.com/lentago/epigaea/issues/533) Rename the lentago-lab-status dashboard and the pitzilabs_homelab_observability sensor
- ⬜ [kalmia#158](https://github.com/lentago/kalmia/issues/158) Rename the Proxmox cluster "homelab-cluster" to "onprem" (tier 4)
- ⬜ [osmunda#16](https://github.com/lentago/osmunda/issues/16) Move n8n from n8n.lab.lentago.dev to n8n.onprem.lentago.dev
- ✅ [claytonia#65](https://github.com/lentago/claytonia/issues/65) Complete the bullpen → claytonia rename on-host — 1/2 sub-issues closed
  - ⬜ [claytonia#157](https://github.com/lentago/claytonia/issues/157) gitops: the loop never notices its own installed copy drifting from the checkout
  - ✅ [kalmia#228](https://github.com/lentago/kalmia/issues/228) forge: the egress check passes on DNS alone

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-11-05 · [drosera#321](https://github.com/lentago/drosera/pull/321) — Tolerate a short single-task gap on the Spot-backed sites' SLO fast-burn page
- 2026-11-04 · [claytonia#223](https://github.com/lentago/claytonia/pull/223) — docs: remove manual PVE pool step from provision/README.md (#212)
- 2026-11-04 · [betula#157](https://github.com/lentago/betula/pull/157) — Describe terraform/'s Axiom tokens and the rotation guard in CLAUDE.md (#119 follow-up)
- 2026-11-04 · [claytonia#219](https://github.com/lentago/claytonia/pull/219) — rt-codex: create Codex's home when a worker has none
- 2026-11-04 · [drosera#316](https://github.com/lentago/drosera/pull/316) — Lift the #169 hold on runner-transcript.alloy: all five workers sync from /opt/drosera
- 2026-11-04 · [kalmia#282](https://github.com/lentago/kalmia/pull/282) — forge: the egress check passes on DNS alone
- 2026-11-04 · [shared-workflows#103](https://github.com/lentago/shared-workflows/pull/103) — Rename discipline: record claytonia#65 (on-host bullpen names) as paid
- 2026-11-04 · [claytonia#202](https://github.com/lentago/claytonia/pull/202) — Finish the on-host rename: prevent_destroy back on, rebuild runbook in the repo (#65 PR C)
- 2026-11-04 · [claytonia#200](https://github.com/lentago/claytonia/pull/200) — terraform: rebuild claude-runner (110) from runner image v3 (#65 R5)
- 2026-11-04 · [claytonia#199](https://github.com/lentago/claytonia/pull/199) — terraform: rebuild claude-runner-2 (111) from runner image v3 (#65 R4)
- 2026-11-03 · [claytonia#198](https://github.com/lentago/claytonia/pull/198) — terraform: rebuild claude-runner-3 (112) from runner image v3 (#65 R3)
- 2026-11-03 · [claytonia#197](https://github.com/lentago/claytonia/pull/197) — terraform: rebuild claude-runner-4 (116) from runner image v3 (#65 R2)
- 2026-11-02 · [claytonia#195](https://github.com/lentago/claytonia/pull/195) — terraform: rebuild claude-runner-5 (117) from runner image v3 (#65 R1)
- 2026-11-02 · [claytonia#194](https://github.com/lentago/claytonia/pull/194) — terraform: cut new workers from runner image v3 (part of #65)
- 2026-11-02 · [claytonia#192](https://github.com/lentago/claytonia/pull/192) — gitops: a run that loses the lock waits instead of reporting success; install.sh deploys before enabling the timer
- 2026-11-02 · [claytonia#191](https://github.com/lentago/claytonia/pull/191) — Keep the App private key out of the agent's reach: root-owned token broker
- 2026-11-02 · [claytonia#187](https://github.com/lentago/claytonia/pull/187) — Put the queue's NAS README under version control and publish it to the share from main
- 2026-11-02 · [kalmia#261](https://github.com/lentago/kalmia/pull/261) — forge: the runner substrate installs uuid-runtime, so workers have uuidgen (claytonia#179)
- 2026-11-02 · [kalmia#257](https://github.com/lentago/kalmia/pull/257) — forge: the claytonia runner image carries the Gemini and Codex CLIs (claytonia-runner-v3)
- 2026-11-01 · [solidago#238](https://github.com/lentago/solidago/pull/238) — docs: BOOTSTRAP and ADOPTION drift from the code (backend file, state key, required check, role bootstrap order)
- 2026-10-30 · [.github#287](https://github.com/lentago/.github/pull/287) — Epics report: epics, sub-issue progress, and where the merged work went
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

</details>

### Fleet secrets handling (ADR-0011): the follow-through

[.github#286](https://github.com/lentago/.github/issues/286) · open since 2026-10-30 · last activity 2026-10-30

> Tracking issue for the work ADR-0011 (how the fleet handles secrets, accepted 2026-10-07) left open: identity before secrets, values only in approved stores, Terraform holds slots not values, out-of-band values verified, scanning and push protection on every repo, leaks rotated not scrubbed.

Progress: **1/10** sub-issues closed · **4** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [.github#225](https://github.com/lentago/.github/issues/225) FLEET_ADMIN_TOKEN cannot resolve GitHub App node ids: merge-gate App allowances are unmanageable by Terraform
- ⬜ [.github#242](https://github.com/lentago/.github/issues/242) Re-mint two over-broad GitHub tokens: FLEET_REPORTS_TOKEN and the workstation PAT
- ⬜ [.github#243](https://github.com/lentago/.github/issues/243) Credential register: every fleet credential's store, scope, issuer and expiry (names only)
- ⬜ [.github#271](https://github.com/lentago/.github/issues/271) [renewal] FLEET_REPORTS_TOKEN — fine-grained PAT expiry — due 2026-10-30
- ⬜ [osmunda#12](https://github.com/lentago/osmunda/issues/12) Decide how Flux-managed workloads receive secrets, before the n8n cutover
- ⬜ [solidago#149](https://github.com/lentago/solidago/issues/149) Rotating a Lambda's Axiom token requires an unrelated apply to take effect
- ⬜ [solidago#213](https://github.com/lentago/solidago/issues/213) Fail the apply when an out-of-band secret still holds its placeholder
- ⬜ [solidago#220](https://github.com/lentago/solidago/issues/220) iam: give the cross-repo Terraform pipeline roles a read-only plan path
- ⬜ [solidago#222](https://github.com/lentago/solidago/issues/222) monitoring: pass the alert recipient as a sensitive variable, out of committed config and public plan output
- ✅ [solidago#156](https://github.com/lentago/solidago/issues/156) Split plan/apply OIDC environments so the terraform environment can carry a branch policy

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-11-02 · [solidago#227](https://github.com/lentago/solidago/pull/227) — ci(terraform): plan in the terraform-plan environment on the read-only role (#225 step 2 of 2)
- 2026-11-02 · [solidago#226](https://github.com/lentago/solidago/pull/226) — feat(iam): read-only Terraform plan role on the terraform-plan environment (#225 step 1 of 2)
- 2026-11-02 · [solidago#236](https://github.com/lentago/solidago/pull/236) — ask-lambda: read the Anthropic key from SSM at runtime instead of a Terraform variable
- 2026-10-30 · [.github#287](https://github.com/lentago/.github/pull/287) — Epics report: epics, sub-issue progress, and where the merged work went

</details>

### External review 2026-11-01: fleet follow-through

[.github#304](https://github.com/lentago/.github/issues/304) · open since 2026-11-01 · last activity 2026-11-02

> On 2026-11-01 an outside-style review of the public organization, the website, selected implementation paths and commit history reached the maintainer: 12 findings and 6 product and marketing critiques.

Progress: **19/27** sub-issues closed · checklist **20/30** · **30** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [.github#307](https://github.com/lentago/.github/issues/307) Immutable releases for shared-workflows once the provider supports it
- ⬜ [.github#312](https://github.com/lentago/.github/issues/312) fleet-reports.yml: arm the refresh PR on its pushed head and drop the immediate-merge fallback
- ⬜ [.github#313](https://github.com/lentago/.github/issues/313) Voice guide: the pull-request definition says "someone else reviews", which the solo-operator merge promise doesn't keep
- ⬜ [.github#316](https://github.com/lentago/.github/issues/316) ADR-0009: add an amendment note that the Ask box is now called source-linked, not grounded
- ⬜ [site-lentago-dev#112](https://github.com/lentago/site-lentago-dev/issues/112) Front page: three need-based doors above the suite map (draft PR for review)
- ⬜ [site-pondviewlane-com#99](https://github.com/lentago/site-pondviewlane-com/issues/99) Sync the Ask handler reference copy: key read from SSM (solidago#230)
- ⬜ [solidago#233](https://github.com/lentago/solidago/issues/233) Adoption receipt: one supervised cold run in a fresh AWS account
- ⬜ [solidago#237](https://github.com/lentago/solidago/issues/237) iam: one shared deploy role and task role span every site, so a trusted site repo can roll any service
- ✅ [.github#305](https://github.com/lentago/.github/issues/305) Tag ruleset for shared-workflows: forbid deleting or moving v* tags
- ✅ [.github#306](https://github.com/lentago/.github/issues/306) ADR: the merge promise, humans approve agent PRs, policy-owned merges for routines and session-armed PRs
- ✅ [.github#310](https://github.com/lentago/.github/issues/310) uvularia repo description and banner alt still say "grounded Ask"; align with the source-linked wording
- ✅ [.github#311](https://github.com/lentago/.github/issues/311) Codify solidago's GitHub environments: terraform with a main-only branch policy, terraform-plan with no rules
- ✅ [asclepias#26](https://github.com/lentago/asclepias/issues/26) estate-atlas: replace "humans own every merge" with the ADR-0014 wording
- ✅ [drosera#300](https://github.com/lentago/drosera/issues/300) README: replace "humans own every merge" with the ADR-0014 wording
- ✅ [shared-workflows#88](https://github.com/lentago/shared-workflows/issues/88) ADR-0005: 'immutable' is a convention until the tag ruleset lands; say so and reference it
- ✅ [shared-workflows#90](https://github.com/lentago/shared-workflows/issues/90) PR-workflow text: arm the checked head; a runner-App PR needs a human approval (.github ADR-0014)
- ✅ [site-lentago-dev#111](https://github.com/lentago/site-lentago-dev/issues/111) Copy: response-time and migration promises match the support page; form labels lead with the task
- ✅ [solidago#229](https://github.com/lentago/solidago/issues/229) iam: drop Terraform state and KMS access from the app deploy role
- ✅ [solidago#230](https://github.com/lentago/solidago/issues/230) ask-lambda: read the Anthropic key from SSM at runtime instead of a Terraform variable, then rotate it
- ✅ [solidago#231](https://github.com/lentago/solidago/issues/231) rds: module header says deletion protection is enabled; the code sets it off
- ✅ [solidago#232](https://github.com/lentago/solidago/issues/232) docs: BOOTSTRAP and ADOPTION drift from the code (backend file, state key, required check, role bootstrap order)
- ✅ [uvularia#114](https://github.com/lentago/uvularia/issues/114) Records template: say that issues, branches and attachments in the public repository are visible at once
- ✅ [uvularia#115](https://github.com/lentago/uvularia/issues/115) Board standing goes stale between publishes: re-evaluate on a schedule and show when it was evaluated
- ✅ [uvularia#116](https://github.com/lentago/uvularia/issues/116) Massachusetts pack: label proxy rules as operational reminders, add 2027 holidays, fail unknown on a missing holiday year
- ✅ [uvularia#117](https://github.com/lentago/uvularia/issues/117) Ask function: require a valid source for an answered reply, call it source-linked, disclose question logging
- ✅ [uvularia#118](https://github.com/lentago/uvularia/issues/118) Templates carry no license: add LICENSE to templates/records, templates/site and templates/ask-rules
- ✅ [uvularia#132](https://github.com/lentago/uvularia/issues/132) README banner alt text still says "grounded Ask"

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-11-04 · [shared-workflows#91](https://github.com/lentago/shared-workflows/pull/91) — PR-workflow text: arm the checked head; a runner-App PR needs a human approval (.github ADR-0014)
- 2026-11-02 · [solidago#249](https://github.com/lentago/solidago/pull/249) — iam: remove the shared ECS roles' database secret grants (no service uses the RDS secret)
- 2026-11-02 · [solidago#248](https://github.com/lentago/solidago/pull/248) — ask-lambda: harden the public Ask endpoint (durable cap, Turnstile, concurrency, timeout, alarms)
- 2026-11-02 · [drosera#302](https://github.com/lentago/drosera/pull/302) — docs(readme): replace merge-ownership sentence with ADR-0014 wording
- 2026-11-02 · [asclepias#27](https://github.com/lentago/asclepias/pull/27) — docs(estate-atlas): adopt ADR-0014 merge-promise wording
- 2026-11-02 · [lupinus#34](https://github.com/lentago/lupinus/pull/34) — tiers: add Readiness column; mark unreceipted Kit/Platform rows provisional
- 2026-11-02 · [shared-workflows#89](https://github.com/lentago/shared-workflows/pull/89) — docs(adr): ADR-0005 addendum on tag immutability and SHA pinning
- 2026-11-02 · [uvularia#134](https://github.com/lentago/uvularia/pull/134) — Banner: source-linked Ask, regenerated from the brand output
- 2026-11-02 · [.github#315](https://github.com/lentago/.github/pull/315) — uvularia repo description and banner: source-linked Ask, not grounded
- 2026-11-02 · [.github#314](https://github.com/lentago/.github/pull/314) — Codify solidago's GitHub environments: terraform with a main-only branch policy, terraform-plan with no rules
- 2026-11-02 · [solidago#227](https://github.com/lentago/solidago/pull/227) — ci(terraform): plan in the terraform-plan environment on the read-only role (#225 step 2 of 2)
- 2026-11-02 · [solidago#226](https://github.com/lentago/solidago/pull/226) — feat(iam): read-only Terraform plan role on the terraform-plan environment (#225 step 1 of 2)
- 2026-11-02 · [.github#309](https://github.com/lentago/.github/pull/309) — ADR-0014: the merge promise — humans approve agent PRs, policy-owned merges for routines and session-armed PRs
- 2026-11-02 · [uvularia#133](https://github.com/lentago/uvularia/pull/133) — README banner alt text: source-linked Ask, not grounded Ask
- 2026-11-02 · [solidago#236](https://github.com/lentago/solidago/pull/236) — ask-lambda: read the Anthropic key from SSM at runtime instead of a Terraform variable
- 2026-11-02 · [uvularia-demo-ask-rules#16](https://github.com/lentago/uvularia-demo-ask-rules/pull/16) — Sync the 2026-11-01 review batch from lentago/uvularia@4b2226e
- 2026-11-02 · [uvularia-demo-site#7](https://github.com/lentago/uvularia-demo-site/pull/7) — Sync the 2026-11-01 review batch from lentago/uvularia@4b2226e
- 2026-11-02 · [uvularia#131](https://github.com/lentago/uvularia/pull/131) — Ask: README states the source rule precisely; the question-log wiring test ignores commented lines
- 2026-11-02 · [uvularia#130](https://github.com/lentago/uvularia/pull/130) — Site home page: count lapsed standing rows as unknown
- 2026-11-02 · [uvularia-demo-records#21](https://github.com/lentago/uvularia-demo-records/pull/21) — Sync the 2026-11-01 review batch from lentago/uvularia@4b2226e
- 2026-11-02 · [uvularia#122](https://github.com/lentago/uvularia/pull/122) — Ask: require a valid source for an answered reply; call it source-linked; disclose question logging
- 2026-11-02 · [uvularia#124](https://github.com/lentago/uvularia/pull/124) — Massachusetts pack: proxy labels, 2027 holidays, no-data on a missing holiday year, and a fixed-date rule kind
- 2026-11-02 · [uvularia#119](https://github.com/lentago/uvularia/pull/119) — templates: add an MIT LICENSE to the three template subtrees
- 2026-11-02 · [uvularia#120](https://github.com/lentago/uvularia/pull/120) — records template: say that issues, branches and attachments are public at once
- 2026-11-02 · [uvularia#121](https://github.com/lentago/uvularia/pull/121) — Board standing: re-evaluate on a schedule and show when it was evaluated
- 2026-11-01 · [solidago#238](https://github.com/lentago/solidago/pull/238) — docs: BOOTSTRAP and ADOPTION drift from the code (backend file, state key, required check, role bootstrap order)
- 2026-11-01 · [solidago#234](https://github.com/lentago/solidago/pull/234) — iam: drop Terraform state and KMS access from the app deploy role
- 2026-11-01 · [solidago#235](https://github.com/lentago/solidago/pull/235) — rds: module header says deletion protection is enabled; the code sets it off
- 2026-11-01 · [.github#308](https://github.com/lentago/.github/pull/308) — Tag ruleset for shared-workflows: forbid deleting or moving v* tags
- 2026-11-01 · [site-lentago-dev#113](https://github.com/lentago/site-lentago-dev/pull/113) — Copy: response-time and migration promises match the support page; form labels lead with the task

</details>

### Security review 2026-11-02: fleet follow-through

[.github#318](https://github.com/lentago/.github/issues/318) · open since 2026-11-02 · last activity 2026-11-05

> Follow-on to lentago/.github#304.

Progress: **20/24** sub-issues closed · checklist **0/12** · **59** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [.github#319](https://github.com/lentago/.github/issues/319) agent-pr-gate verdict: a per-check source in rulesets.tf and a main-only agent-pr-gate environment per gated repo (shared-workflows#97)
- ⬜ [kalmia#262](https://github.com/lentago/kalmia/issues/262) Downloads, part 2: rpm_key fingerprints, the forge substrate's installers, and fzf
- ⬜ [osmunda#22](https://github.com/lentago/osmunda/issues/22) ci: run kube-linter on apps/ and clusters/, with the n8n securityContext as its baseline
- ⬜ [site-pondviewlane-com#100](https://github.com/lentago/site-pondviewlane-com/issues/100) Ask widget: send a Cloudflare Turnstile token (enables solidago#241's bot check)
- ✅ [claytonia#176](https://github.com/lentago/claytonia/issues/176) gh-token: scope installation tokens to the job's repository and minimum permissions
- ✅ [claytonia#177](https://github.com/lentago/claytonia/issues/177) Keep the App private key out of the agent's reach: root-owned token broker
- ✅ [claytonia#178](https://github.com/lentago/claytonia/issues/178) cr-automerge: pin the reviewed head commit and re-check after later pushes (ADR-0014)
- ✅ [kalmia#259](https://github.com/lentago/kalmia/issues/259) Downloads: checksums on every get_url and pinned releases instead of curl\|sh installers
- ✅ [kalmia#264](https://github.com/lentago/kalmia/issues/264) forge: replace the runner image's blanket sudoers rule with claytonia#177's narrow entries
- ✅ [osmunda#20](https://github.com/lentago/osmunda/issues/20) n8n: complete the pod securityContext (privilege escalation, capabilities, seccomp)
- ✅ [shared-workflows#92](https://github.com/lentago/shared-workflows/issues/92) site-deploy: fail the job when ECS rolls the deployment back (circuit breaker makes services-stable report green)
- ✅ [shared-workflows#95](https://github.com/lentago/shared-workflows/issues/95) docs-check: github.job_workflow_ref is empty, so callers run main's link resolver instead of the pinned tag's
- ✅ [shared-workflows#97](https://github.com/lentago/shared-workflows/issues/97) agent-pr-gate, part 2: a verdict check posted by a dedicated GitHub App and required by its integration ID
- ✅ [site-icecreamtofightwith-com#214](https://github.com/lentago/site-icecreamtofightwith-com/issues/214) Bump site-deploy caller to shared-workflows@v1.5.1
- ✅ [site-lentago-dev#115](https://github.com/lentago/site-lentago-dev/issues/115) CSP: enforce the policy; report-only with no report endpoint does nothing
- ✅ [site-lentago-dev#117](https://github.com/lentago/site-lentago-dev/issues/117) Bump site-deploy caller to shared-workflows@v1.5.1
- ✅ [site-pondviewlane-com#101](https://github.com/lentago/site-pondviewlane-com/issues/101) Bump site-deploy caller to shared-workflows@v1.5.1
- ✅ [solidago#241](https://github.com/lentago/solidago/issues/241) ask-lambda: harden the public Ask endpoint (shared cap, Turnstile, reserved concurrency, timeout, alarm)
- ✅ [solidago#242](https://github.com/lentago/solidago/issues/242) iam: scope the ECS task and execution roles' secret read to the one RDS secret in use
- ✅ [solidago#243](https://github.com/lentago/solidago/issues/243) guardduty: enable the detector in Terraform (decision 2 on the epic)
- ✅ [solidago#244](https://github.com/lentago/solidago/issues/244) cloudtrail: metric filters and alarms for root use, no-MFA sign-in, IAM and trail changes, unauthorized calls
- ✅ [solidago#245](https://github.com/lentago/solidago/issues/245) waf logging and ECS deployment circuit breaker
- ✅ [solidago#246](https://github.com/lentago/solidago/issues/246) logs: decide on a CMK for the CloudWatch log groups (default key today)
- ✅ [solidago#250](https://github.com/lentago/solidago/issues/250) monitoring: alert topics' policies block CloudWatch alarms from publishing, so no alarm notifies

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-11-05 · [solidago#279](https://github.com/lentago/solidago/pull/279) — cost: WAF to two rules — Common Rule Set and the rate limit (#277)
- 2026-11-04 · [claytonia#231](https://github.com/lentago/claytonia/pull/231) — docs: correct ADR-0004 token permission scope
- 2026-11-04 · [claytonia#230](https://github.com/lentago/claytonia/pull/230) — docs: correct historical sudo access in ADR-0010
- 2026-11-04 · [claytonia#203](https://github.com/lentago/claytonia/pull/203) — rt-codex: Codex CLI adapter (#171)
- 2026-11-04 · [kalmia#283](https://github.com/lentago/kalmia/pull/283) — Downloads, part 2: rpm_key fingerprints, fzf pinned to a tag, and the AWS CLI's PGP signature
- 2026-11-02 · [claytonia#195](https://github.com/lentago/claytonia/pull/195) — terraform: rebuild claude-runner-5 (117) from runner image v3 (#65 R1)
- 2026-11-02 · [claytonia#194](https://github.com/lentago/claytonia/pull/194) — terraform: cut new workers from runner image v3 (part of #65)
- 2026-11-02 · [.github#326](https://github.com/lentago/.github/pull/326) — Require agent-pr-verdict from the gate App on shared-workflows; each required check's source App is set per check (#319)
- 2026-11-02 · [.github#325](https://github.com/lentago/.github/pull/325) — Require agent-pr-gate on the kits, lupinus and monarda (#289)
- 2026-11-02 · [.github#324](https://github.com/lentago/.github/pull/324) — agent-pr-gate: set the gate App ID by hand beside the key, not by Terraform (#319)
- 2026-11-02 · [shared-workflows#98](https://github.com/lentago/shared-workflows/pull/98) — agent-pr-gate, part 2: a verdict check posted by a dedicated GitHub App and required by its integration ID
- 2026-11-02 · [.github#323](https://github.com/lentago/.github/pull/323) — agent-pr-gate environment on shared-workflows: main only, no admin bypass, with the gate App ID (#319)
- 2026-11-02 · [monarda#36](https://github.com/lentago/monarda/pull/36) — ci: vendor the agent-pr-gate (shared-workflows v1.6.0)
- 2026-11-02 · [.github#322](https://github.com/lentago/.github/pull/322) — Require agent-pr-gate on the 17 repos whose callers report it (#289)
- 2026-11-02 · [claytonia#193](https://github.com/lentago/claytonia/pull/193) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [site-pondviewlane-com#103](https://github.com/lentago/site-pondviewlane-com/pull/103) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [site-icecreamtofightwith-com#215](https://github.com/lentago/site-icecreamtofightwith-com/pull/215) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [uvularia#135](https://github.com/lentago/uvularia/pull/135) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [solidago#264](https://github.com/lentago/solidago/pull/264) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [site-lentago-dev#123](https://github.com/lentago/site-lentago-dev/pull/123) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [repo-template#33](https://github.com/lentago/repo-template/pull/33) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [osmunda#24](https://github.com/lentago/osmunda/pull/24) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [mitchella#33](https://github.com/lentago/mitchella/pull/33) — Add the agent-pr-gate caller (lentago/.github#289)
- 2026-11-02 · [kalmia#271](https://github.com/lentago/kalmia/pull/271) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [epigaea#566](https://github.com/lentago/epigaea/pull/566) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [drosera#307](https://github.com/lentago/drosera/pull/307) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [brasenia#132](https://github.com/lentago/brasenia/pull/132) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [betula#150](https://github.com/lentago/betula/pull/150) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [asclepias#29](https://github.com/lentago/asclepias/pull/29) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [site-pondviewlane-com#102](https://github.com/lentago/site-pondviewlane-com/pull/102) — ci: bump site-deploy shared workflow to v1.5.1
- 2026-11-02 · [site-icecreamtofightwith-com#216](https://github.com/lentago/site-icecreamtofightwith-com/pull/216) — ci: bump site-deploy reusable workflow pin to v1.5.1
- 2026-11-02 · [.github#320](https://github.com/lentago/.github/pull/320) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [site-lentago-dev#120](https://github.com/lentago/site-lentago-dev/pull/120) — Bump site-deploy caller to shared-workflows@v1.5.1
- 2026-11-02 · [kalmia#270](https://github.com/lentago/kalmia/pull/270) — forge: replace the runner image's blanket sudoers rule with claytonia#177's narrow entries
- 2026-11-02 · [claytonia#191](https://github.com/lentago/claytonia/pull/191) — Keep the App private key out of the agent's reach: root-owned token broker
- 2026-11-02 · [solidago#263](https://github.com/lentago/solidago/pull/263) — docs: correct the stated run rate to the observed $212–222/month; note the $100 budget is below it by choice
- 2026-11-02 · [solidago#259](https://github.com/lentago/solidago/pull/259) — guardduty: correct the header on the AI plans, stop a perpetual replace-diff, turn off RDS data-activity monitoring
- 2026-11-02 · [solidago#258](https://github.com/lentago/solidago/pull/258) — guardduty: enable the detector, email findings of severity 4+ to the alert topic, add a GuardDuty budget alarm (#243)
- 2026-11-02 · [solidago#257](https://github.com/lentago/solidago/pull/257) — waf: log every request to a 30-day aws-waf-logs group, authorization and cookie redacted (#245, WAF-logging half)
- 2026-11-02 · [solidago#256](https://github.com/lentago/solidago/pull/256) — iam: let the apply role manage the GuardDuty detector and this stack's EventBridge rules (#243, step 1)
- 2026-11-02 · [shared-workflows#96](https://github.com/lentago/shared-workflows/pull/96) — docs-check: run the resolver at the ref the caller pinned (github.job_workflow_ref is empty)
- 2026-11-02 · [shared-workflows#94](https://github.com/lentago/shared-workflows/pull/94) — agent-pr-gate: a required check that fails on runner-App PRs without a human approving review (claytonia#117 option A)
- 2026-11-02 · [claytonia#186](https://github.com/lentago/claytonia/pull/186) — cr-automerge: pin the reviewed head commit and re-check after later pushes
- 2026-11-02 · [claytonia#184](https://github.com/lentago/claytonia/pull/184) — gh-token: scope installation tokens to the job's repository and minimum permissions
- 2026-11-02 · [shared-workflows#93](https://github.com/lentago/shared-workflows/pull/93) — site-deploy: fail the job when ECS rolls the deployment back (circuit breaker makes services-stable report green)
- 2026-11-02 · [solidago#254](https://github.com/lentago/solidago/pull/254) — logs: decide on a CMK for the CloudWatch log groups (default key, except the Ask log)
- 2026-11-02 · [solidago#253](https://github.com/lentago/solidago/pull/253) — ecs: deployment circuit breaker with rollback on every service (#245, circuit-breaker half)
- 2026-11-02 · [solidago#249](https://github.com/lentago/solidago/pull/249) — iam: remove the shared ECS roles' database secret grants (no service uses the RDS secret)
- 2026-11-02 · [solidago#252](https://github.com/lentago/solidago/pull/252) — cloudtrail: metric filters and alarms for root use, no-MFA sign-in, IAM and trail changes, unauthorized calls
- 2026-11-02 · [kalmia#263](https://github.com/lentago/kalmia/pull/263) — Downloads: checksums on every get_url and pinned releases instead of curl\|sh installers
- 2026-11-02 · [solidago#251](https://github.com/lentago/solidago/pull/251) — monitoring: let CloudWatch alarms publish to the alert topics
- 2026-11-02 · [osmunda#21](https://github.com/lentago/osmunda/pull/21) — fix(n8n): complete pod and container securityContext
- 2026-11-02 · [solidago#248](https://github.com/lentago/solidago/pull/248) — ask-lambda: harden the public Ask endpoint (durable cap, Turnstile, concurrency, timeout, alarms)
- 2026-11-02 · [site-lentago-dev#116](https://github.com/lentago/site-lentago-dev/pull/116) — fix(nginx): enforce the Content-Security-Policy
- 2026-11-02 · [solidago#247](https://github.com/lentago/solidago/pull/247) — iam: let the apply role manage this stack's DynamoDB tables (#241 step 1 of 2)
- 2026-11-02 · [.github#314](https://github.com/lentago/.github/pull/314) — Codify solidago's GitHub environments: terraform with a main-only branch policy, terraform-plan with no rules
- 2026-11-02 · [solidago#227](https://github.com/lentago/solidago/pull/227) — ci(terraform): plan in the terraform-plan environment on the read-only role (#225 step 2 of 2)
- 2026-11-02 · [solidago#226](https://github.com/lentago/solidago/pull/226) — feat(iam): read-only Terraform plan role on the terraform-plan environment (#225 step 1 of 2)
- 2026-10-13 · [.github#262](https://github.com/lentago/.github/pull/262) — Stop using tier words in the banner eyebrow kind

</details>

### Roadmap: core/client split — Firewalla and solidago (AWS) as peer collector clients

[betula#74](https://github.com/lentago/betula/issues/74) · open since 2026-07-04 · last activity 2026-10-30

> Roadmap for betula's shape: a source-agnostic core and self-contained collector clients, so a new log source lands without touching an existing one.

Progress: **1/8** sub-issues closed · checklist **0/3** · **12** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [betula#106](https://github.com/lentago/betula/issues/106) Third AWS emitter: CloudTrail → archive + weekly access digest
- ⬜ [betula#107](https://github.com/lentago/betula/issues/107) Device drift self-report: deployed conf hash vs main
- ⬜ [betula#130](https://github.com/lentago/betula/issues/130) GitHub collector: first-tick backfill ran 7.5 min against a 10 min TimeoutStartSec; checkpoint per repo and reuse connections
- ⬜ [betula#133](https://github.com/lentago/betula/issues/133) GitHub Actions feed: carry the PR number so PR head SHAs join to merge commits (drosera ADR-0010)
- ⬜ [betula#147](https://github.com/lentago/betula/issues/147) Cover the pe-publish runner (LXC 123) in the queued-jobs feed
- ⬜ [betula#148](https://github.com/lentago/betula/issues/148) GitHub collector README: dry-run example puts secrets in argv
- ⬜ [solidago#144](https://github.com/lentago/solidago/issues/144) Ask Lambda logs land in CloudWatch with no path to Axiom
- ✅ [betula#119](https://github.com/lentago/betula/issues/119) Terraform the Axiom tokens (exact import + rotation handoff)

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-11-04 · [shared-workflows#106](https://github.com/lentago/shared-workflows/pull/106) — Live-state table: betula now manages the Axiom consumer tokens
- 2026-11-04 · [betula#157](https://github.com/lentago/betula/pull/157) — Describe terraform/'s Axiom tokens and the rotation guard in CLAUDE.md (#119 follow-up)
- 2026-11-04 · [drosera#318](https://github.com/lentago/drosera/pull/318) — Take the Solidago Axiom token from betula's state only; drop the variable and the repo secret (#313)
- 2026-11-04 · [betula#156](https://github.com/lentago/betula/pull/156) — Record what the bootstrap Axiom token needs (#119 step 4)
- 2026-11-04 · [betula#155](https://github.com/lentago/betula/pull/155) — Narrow cjp-solidago-alb-query to the ALB dataset as a planned rotation (#119 step 3)
- 2026-11-04 · [.github#333](https://github.com/lentago/.github/pull/333) — Scoped label for betula's token rotation guard override (betula#119)
- 2026-11-04 · [drosera#317](https://github.com/lentago/drosera/pull/317) — Read the Solidago Axiom token from betula's state, falling back to the repo secret (#313, first half)
- 2026-11-04 · [solidago#270](https://github.com/lentago/solidago/pull/270) — iam: let drosera's Terraform role read betula's state key (betula#119)
- 2026-11-04 · [betula#154](https://github.com/lentago/betula/pull/154) — Export the Axiom token values for consumers to read from betula's state (#119 step 2)
- 2026-11-04 · [betula#153](https://github.com/lentago/betula/pull/153) — Terraform the Axiom tokens: exact import of the three consumer tokens (#119 step 1)
- 2026-10-30 · [betula#146](https://github.com/lentago/betula/pull/146) — feat(github): sample queued jobs in queue_watch repos (drosera#292)
- 2026-10-12 · [lupinus#25](https://github.com/lentago/lupinus/pull/25) — Stories: one spine, three rungs, one map; one canonical product list

</details>

### Phase 3: the fleet on the display, and what stays open after ADR-0020

[brasenia#130](https://github.com/lentago/brasenia/issues/130) · open since 2026-10-30 · last activity 2026-10-30

> Tracking issue for the display's third phase (docs/concept.md, Phase 3: the governance snippet reaches every local Claude and the fleet, and panes arrive from real activity) and for the items left open after October's wall work.

Progress: **5/9** sub-issues closed · **12** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [brasenia#15](https://github.com/lentago/brasenia/issues/15) Adopt the display guest (LXC 118) capacity from kalmia
- ⬜ [brasenia#31](https://github.com/lentago/brasenia/issues/31) Focus producer: unauthenticated 304s spend the GitHub budget, so focus panes refresh every few minutes, not every minute
- ⬜ [brasenia#123](https://github.com/lentago/brasenia/issues/123) Close out the 1280×720 pane contract once the external search panes move (ADR-0019)
- ⬜ [claytonia#137](https://github.com/lentago/claytonia/issues/137) brasenia on the fleet: share mount on the workers, pane command in the worker prompt, fleet beacons
- ✅ [brasenia#17](https://github.com/lentago/brasenia/issues/17) Live-ingest pane: concept + ADR, acceptance spec, and VideoScene repoint to `live` with board fallback
- ✅ [brasenia#43](https://github.com/lentago/brasenia/issues/43) README intro still calls the pane bus and compositor "the roadmap"; ADR-0008 says they run
- ✅ [brasenia#51](https://github.com/lentago/brasenia/issues/51) Pane bus: a producer's author check isn't atomic with its write, so a claim made in between gets overwritten
- ✅ [brasenia#99](https://github.com/lentago/brasenia/issues/99) Roku: on a switch, show the new pane's still image until the stream catches up
- ✅ [kalmia#99](https://github.com/lentago/kalmia/issues/99) Cast client runtime for brasenia: watchdog sender, receiver hosting, then HLS-stack turn-down (brasenia ADR-0006)

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-11-04 · [kalmia#285](https://github.com/lentago/kalmia/pull/285) — docs(pub): record the first GitHub token seed in the rotation record
- 2026-11-04 · [kalmia#284](https://github.com/lentago/kalmia/pull/284) — pub: load a shared GitHub token into brasenia-prs and brasenia-focus (ADR-0021)
- 2026-11-04 · [brasenia#143](https://github.com/lentago/brasenia/pull/143) — Pane bus: make the author check atomic with the write (a new pane is renamed in whole; ADR-0022)
- 2026-11-04 · [brasenia#141](https://github.com/lentago/brasenia/pull/141) — README intro: the pane bus and compositor run, they are not the roadmap
- 2026-11-04 · [brasenia#138](https://github.com/lentago/brasenia/pull/138) — ADR-0021: a public-read-only GitHub token on pub for the PRs and focus producers
- 2026-10-30 · [.github#287](https://github.com/lentago/.github/pull/287) — Epics report: epics, sub-issue progress, and where the merged work went
- 2026-10-30 · [brasenia#124](https://github.com/lentago/brasenia/pull/124) — Migrate the family brief to one 1920×1080 band and retire its desk editions (ADR-0019, ADR-0020)
- 2026-10-30 · [brasenia#120](https://github.com/lentago/brasenia/pull/120) — docs: record the RTMP live-ingest retirement on ADR-0007
- 2026-10-30 · [kalmia#224](https://github.com/lentago/kalmia/pull/224) — brasenia: retire RTMP live ingest and remove mediamtx
- 2026-10-28 · [kalmia#175](https://github.com/lentago/kalmia/pull/175) — lunaria: retire the Cast receiver watchdog (the role now ensures it is absent)
- 2026-10-28 · [brasenia#53](https://github.com/lentago/brasenia/pull/53) — Office Roku: 4K family-brief client (HEVC over HLS); retire the play-room Roku client
- 2026-10-28 · [kalmia#168](https://github.com/lentago/kalmia/pull/168) — lunaria: 4K HEVC family-brief stream for the office Roku; retire the 720p board stream

</details>

### Roadmap: platform-agnostic workers — Claude Code as one runtime behind the queue contract

[claytonia#47](https://github.com/lentago/claytonia/issues/47) · open since 2026-07-04 · last activity 2026-11-04

> Roadmap for claytonia's thesis: the queue contract (plain-file inbox, atomic claim, branch-and-PR-never-merge, per-project context, at-least-once delivery) is the product; Claude Code headless is today's only worker runtime, and another agent CLI should slot in as a peer runtime without changing the dispatch spec, the…

Progress: **7/18** sub-issues closed · checklist **1/3** · **26** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [claytonia#99](https://github.com/lentago/claytonia/issues/99) Second job type: batch document/report jobs through the queue contract
- ⬜ [claytonia#115](https://github.com/lentago/claytonia/issues/115) An eval set for the fleet: replayable tasks, deterministic graders, and outcome measures
- ⬜ [claytonia#116](https://github.com/lentago/claytonia/issues/116) Close the loop after the PR opens: a capped follow-up job for failing checks and review comments
- ⬜ [claytonia#166](https://github.com/lentago/claytonia/issues/166) Peer worker runtimes: Gemini CLI and Codex CLI behind the queue contract — 7/14 sub-issues closed
  - ⬜ [.github#317](https://github.com/lentago/.github/issues/317) Peer worker runtimes, fleet half: an ADR, disclosure wording for non-Claude agents, and the runtime-label question (claytonia#166)
  - ⬜ [claytonia#172](https://github.com/lentago/claytonia/issues/172) cr-update: a per-runtime CLI update path
  - ⬜ [claytonia#173](https://github.com/lentago/claytonia/issues/173) Runtime and token fields in .meta and cr-emit; unknown cost as null
  - ⬜ [claytonia#174](https://github.com/lentago/claytonia/issues/174) Runtime disclosure on agent PRs: footer and preamble attribution written by run-job
  - ⬜ [drosera#304](https://github.com/lentago/drosera/issues/304) pricing.json: Gemini and Codex price rows, so non-Claude runner jobs get a cost
  - ⬜ [drosera#305](https://github.com/lentago/drosera/issues/305) Live transcript for Gemini and Codex runner jobs (runner-transcript.alloy)
  - ⬜ [kalmia#256](https://github.com/lentago/kalmia/issues/256) standing: `standing up <repo> --runtime gemini\|codex` — an Engineering Manager on another CLI
  - ✅ [claytonia#167](https://github.com/lentago/claytonia/issues/167) Extract the Claude invocation into bin/rt-claude with no behavior change
  - ✅ [claytonia#168](https://github.com/lentago/claytonia/issues/168) Runtime key in the job spec, registry, runner.env and cr-submit, with runtime-scoped model precedence
  - ✅ [claytonia#169](https://github.com/lentago/claytonia/issues/169) Test stubs and bats for the runtime seam
  - ✅ [claytonia#170](https://github.com/lentago/claytonia/issues/170) rt-gemini: Gemini CLI adapter
  - ✅ [claytonia#171](https://github.com/lentago/claytonia/issues/171) rt-codex: Codex CLI adapter
  - ✅ [drosera#303](https://github.com/lentago/drosera/issues/303) Claytonia — Runner Fleet: split jobs, failures, duration and cost by runtime, with an unknown cost state
  - ✅ [kalmia#255](https://github.com/lentago/kalmia/issues/255) forge: the claytonia runner image carries the Gemini and Codex CLIs (claytonia-runner-v3)

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-11-04 · [claytonia#220](https://github.com/lentago/claytonia/pull/220) — rt-codex: hand the key to Codex as CODEX_API_KEY, the name exec reads
- 2026-11-04 · [claytonia#214](https://github.com/lentago/claytonia/pull/214) — rt-gemini: keep the GitHub credential helper through Gemini's git overrides
- 2026-11-04 · [claytonia#219](https://github.com/lentago/claytonia/pull/219) — rt-codex: create Codex's home when a worker has none
- 2026-11-04 · [drosera#315](https://github.com/lentago/drosera/pull/315) — Show stat and bar-gauge splits of Loki instant queries as one value per row (#314)
- 2026-11-04 · [drosera#312](https://github.com/lentago/drosera/pull/312) — Runner Fleet: name stat values, drop the range zero fill, keep the Unpriced column (#303 follow-up)
- 2026-11-04 · [drosera#310](https://github.com/lentago/drosera/pull/310) — Claytonia — Runner Fleet: split jobs, failures, duration and cost by runtime, with an unknown cost state
- 2026-11-04 · [claytonia#208](https://github.com/lentago/claytonia/pull/208) — docs: the worker-runtime interface, as shipped for claude, gemini and codex (#47)
- 2026-11-04 · [claytonia#203](https://github.com/lentago/claytonia/pull/203) — rt-codex: Codex CLI adapter (#171)
- 2026-11-04 · [claytonia#207](https://github.com/lentago/claytonia/pull/207) — Gemini system settings owned by root, and a checkout cannot lift a job's turn cap (#205)
- 2026-11-04 · [claytonia#204](https://github.com/lentago/claytonia/pull/204) — rt-gemini: Gemini CLI adapter (#170)
- 2026-11-04 · [claytonia#202](https://github.com/lentago/claytonia/pull/202) — Finish the on-host rename: prevent_destroy back on, rebuild runbook in the repo (#65 PR C)
- 2026-11-04 · [claytonia#201](https://github.com/lentago/claytonia/pull/201) — Source the Claude token in rt-claude only (#170 prerequisite)
- 2026-11-02 · [claytonia#195](https://github.com/lentago/claytonia/pull/195) — terraform: rebuild claude-runner-5 (117) from runner image v3 (#65 R1)
- 2026-11-02 · [claytonia#194](https://github.com/lentago/claytonia/pull/194) — terraform: cut new workers from runner image v3 (part of #65)
- 2026-11-02 · [kalmia#270](https://github.com/lentago/kalmia/pull/270) — forge: replace the runner image's blanket sudoers rule with claytonia#177's narrow entries
- 2026-11-02 · [kalmia#269](https://github.com/lentago/kalmia/pull/269) — forge: the claytonia layer races claytonia-gitops' own timer for its lock, so the forced deploy can exit 0 having deployed nothing (v3 attempt 2 failed)
- 2026-11-02 · [kalmia#267](https://github.com/lentago/kalmia/pull/267) — forge: build.sh feeds scripts to pct exec on stdin, so a command that reads stdin silently ends the substrate (v3 build failed)
- 2026-11-02 · [claytonia#183](https://github.com/lentago/claytonia/pull/183) — Test stubs and bats for the runtime seam
- 2026-11-02 · [claytonia#182](https://github.com/lentago/claytonia/pull/182) — run-job: a session id is never empty, uuidgen or not
- 2026-11-02 · [claytonia#180](https://github.com/lentago/claytonia/pull/180) — Runtime key in the job spec, registry, runner.env and cr-submit, with runtime-scoped model precedence
- 2026-11-02 · [claytonia#175](https://github.com/lentago/claytonia/pull/175) — Extract the Claude invocation into bin/rt-claude with no behavior change
- 2026-11-02 · [kalmia#261](https://github.com/lentago/kalmia/pull/261) — forge: the runner substrate installs uuid-runtime, so workers have uuidgen (claytonia#179)
- 2026-11-02 · [kalmia#257](https://github.com/lentago/kalmia/pull/257) — forge: the claytonia runner image carries the Gemini and Codex CLIs (claytonia-runner-v3)
- 2026-10-28 · [claytonia#151](https://github.com/lentago/claytonia/pull/151) — Run scheduled routines on the fleet: schedules as data, a policy-gated merge step, per-repo App tokens, read-only Google access
- 2026-10-13 · [claytonia#144](https://github.com/lentago/claytonia/pull/144) — Fleet PR lane separation: rebase-before-merge + overlap check
- 2026-10-13 · [claytonia#142](https://github.com/lentago/claytonia/pull/142) — Queue admission control: ownership, occupancy, capacity at submit

</details>

### Make never-merge a boundary: required check that blocks runner-App PRs without a human approval

[claytonia#117](https://github.com/lentago/claytonia/issues/117) · open since 2026-09-17 · last activity 2026-11-02

> From the 2026-09-17 agentic-patterns review (Claude-assisted), which compared claytonia with the published design of commercial and in-house background coding agents.

Progress: **2/2** sub-issues closed · **29** PRs merged in the window

<details><summary>Sub-issues</summary>

- ✅ [.github#289](https://github.com/lentago/.github/issues/289) Require the agent-pr-gate context on every operating repo (claytonia#117 option A)
- ✅ [shared-workflows#84](https://github.com/lentago/shared-workflows/issues/84) agent-pr-gate: a required check that fails on runner-App PRs without a human approving review (claytonia#117 option A)

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-11-04 · [shared-workflows#91](https://github.com/lentago/shared-workflows/pull/91) — PR-workflow text: arm the checked head; a runner-App PR needs a human approval (.github ADR-0014)
- 2026-11-02 · [.github#325](https://github.com/lentago/.github/pull/325) — Require agent-pr-gate on the kits, lupinus and monarda (#289)
- 2026-11-02 · [shared-workflows#98](https://github.com/lentago/shared-workflows/pull/98) — agent-pr-gate, part 2: a verdict check posted by a dedicated GitHub App and required by its integration ID
- 2026-11-02 · [monarda#36](https://github.com/lentago/monarda/pull/36) — ci: vendor the agent-pr-gate (shared-workflows v1.6.0)
- 2026-11-02 · [lupinus#36](https://github.com/lentago/lupinus/pull/36) — ci: vendor the agent-pr-gate from shared-workflows v1.6.0
- 2026-11-02 · [.github#322](https://github.com/lentago/.github/pull/322) — Require agent-pr-gate on the 17 repos whose callers report it (#289)
- 2026-11-02 · [claytonia#193](https://github.com/lentago/claytonia/pull/193) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [site-pondviewlane-com#103](https://github.com/lentago/site-pondviewlane-com/pull/103) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [site-icecreamtofightwith-com#215](https://github.com/lentago/site-icecreamtofightwith-com/pull/215) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [uvularia#135](https://github.com/lentago/uvularia/pull/135) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [solidago#264](https://github.com/lentago/solidago/pull/264) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [site-lentago-dev#123](https://github.com/lentago/site-lentago-dev/pull/123) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [repo-template#33](https://github.com/lentago/repo-template/pull/33) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [osmunda#24](https://github.com/lentago/osmunda/pull/24) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [mitchella#33](https://github.com/lentago/mitchella/pull/33) — Add the agent-pr-gate caller (lentago/.github#289)
- 2026-11-02 · [kalmia#271](https://github.com/lentago/kalmia/pull/271) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [epigaea#566](https://github.com/lentago/epigaea/pull/566) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [drosera#307](https://github.com/lentago/drosera/pull/307) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [brasenia#132](https://github.com/lentago/brasenia/pull/132) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [betula#150](https://github.com/lentago/betula/pull/150) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [asclepias#29](https://github.com/lentago/asclepias/pull/29) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [.github#320](https://github.com/lentago/.github/pull/320) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 2026-11-02 · [claytonia#191](https://github.com/lentago/claytonia/pull/191) — Keep the App private key out of the agent's reach: root-owned token broker
- 2026-11-02 · [shared-workflows#94](https://github.com/lentago/shared-workflows/pull/94) — agent-pr-gate: a required check that fails on runner-App PRs without a human approving review (claytonia#117 option A)
- 2026-11-02 · [claytonia#186](https://github.com/lentago/claytonia/pull/186) — cr-automerge: pin the reviewed head commit and re-check after later pushes
- 2026-11-02 · [claytonia#184](https://github.com/lentago/claytonia/pull/184) — gh-token: scope installation tokens to the job's repository and minimum permissions
- 2026-11-02 · [.github#309](https://github.com/lentago/.github/pull/309) — ADR-0014: the merge promise — humans approve agent PRs, policy-owned merges for routines and session-armed PRs
- 2026-10-28 · [claytonia#151](https://github.com/lentago/claytonia/pull/151) — Run scheduled routines on the fleet: schedules as data, a policy-gated merge step, per-repo App tokens, read-only Google access
- 2026-10-12 · [lupinus#25](https://github.com/lentago/lupinus/pull/25) — Stories: one spine, three rungs, one map; one canonical product list

</details>

### Roadmap: multi-client telemetry pane — on-prem and solidago (AWS) as peer sources

[drosera#131](https://github.com/lentago/drosera/issues/131) · open since 2026-07-04 · last activity 2026-10-30

> Roadmap for drosera's shape: one live pane with every telemetry source as a peer client, the on-prem estate first and solidago (AWS) second, structured so that adding a source touches no other source's dashboards or Alloy config.

Progress: **0/7** sub-issues closed · checklist **0/3** · **2** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [drosera#93](https://github.com/lentago/drosera/issues/93) feat(alloy): attach runid label to the transcript stream from the <sid>.runid sidecar
- ⬜ [drosera#101](https://github.com/lentago/drosera/issues/101) Heartbeat blind spot: tool-less reasoning turns show no activity while tokens burn
- ⬜ [drosera#103](https://github.com/lentago/drosera/issues/103) Scrape node_exporter on the Firewalla via Alloy (bring the gateway into node dashboards)
- ⬜ [drosera#165](https://github.com/lentago/drosera/issues/165) New-domain radar: alert when an IoT/smart-home device queries a never-before-seen domain (migrated from betula#11)
- ⬜ [drosera#198](https://github.com/lentago/drosera/issues/198) Threat Weather: anonymized daily network weather report
- ⬜ [drosera#200](https://github.com/lentago/drosera/issues/200) Queue SLO for the agent fleet (pickup latency) + burn alert
- ⬜ [drosera#204](https://github.com/lentago/drosera/issues/204) Main-branch workflow failures notify nobody — alert on red deploys/applies

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-10-30 · [drosera#294](https://github.com/lentago/drosera/pull/294) — Alert when a self-hosted Actions job sits queued
- 2026-10-13 · [drosera#277](https://github.com/lentago/drosera/pull/277) — feat(dashboards): GitHub — Actions dashboard over the Actions feed

</details>

### Signage: cards, labels and sheets posted at the point of use

[epigaea#548](https://github.com/lentago/epigaea/issues/548) · open since 2026-10-31 · last activity 2026-11-04

> Make the paper half of every automation a first-class, versioned surface.

Progress: checklist **14/15** · **17** PRs merged in the window

_No sub-issues linked — progress is visible only through the checklist and cited PRs._

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-11-04 · [epigaea#577](https://github.com/lentago/epigaea/pull/577) — feat(signage): one shared stylesheet, copied into every piece and checked in CI
- 2026-11-04 · [epigaea#575](https://github.com/lentago/epigaea/pull/575) — feat(signage): add the label type, a label-maker strip and a sheet label, with the Tap Dial's label
- 2026-11-04 · [epigaea#571](https://github.com/lentago/epigaea/pull/571) — feat(signage): a QR code on every card and sheet that opens its own live page
- 2026-11-04 · [epigaea#574](https://github.com/lentago/epigaea/pull/574) — feat(signage): render every piece to PDF in CI and publish it beside the HTML
- 2026-11-04 · [epigaea#576](https://github.com/lentago/epigaea/pull/576) — fix(gitops): treat scripts/*.py as a no-op instead of a full Core restart
- 2026-11-04 · [epigaea#573](https://github.com/lentago/epigaea/pull/573) — feat(signage): an index page listing every piece by room
- 2026-11-04 · [epigaea#572](https://github.com/lentago/epigaea/pull/572) — feat(signage): check signage meta tags against the files they name
- 2026-11-04 · [epigaea#570](https://github.com/lentago/epigaea/pull/570) — feat(signage): add the sheet type with the hallway meeting-light placard; move cards under signage/
- 2026-10-31 · [epigaea#563](https://github.com/lentago/epigaea/pull/563) — fix(cards): fit every card in 7 by 5 inches and check it in CI
- 2026-10-31 · [epigaea#558](https://github.com/lentago/epigaea/pull/558) — feat(cards): instruction card for the meeting button
- 2026-10-31 · [epigaea#555](https://github.com/lentago/epigaea/pull/555) — feat(cards): instruction card for the downstairs lights button (Sonoff Button 1)
- 2026-10-31 · [epigaea#557](https://github.com/lentago/epigaea/pull/557) — fix(gitops-sync): route cards/ and other non-runtime paths to no reload
- 2026-10-31 · [epigaea#554](https://github.com/lentago/epigaea/pull/554) — feat(cards): instruction card for the office scene button (Sonoff Button 2)
- 2026-10-31 · [epigaea#553](https://github.com/lentago/epigaea/pull/553) — feat(cards): instruction card for the office wall switch (ZEN77)
- 2026-10-31 · [epigaea#549](https://github.com/lentago/epigaea/pull/549) — docs(roadmap): replace § Instruction cards with § Signage
- 2026-10-31 · [epigaea#547](https://github.com/lentago/epigaea/pull/547) — feat(cards): adopt printable instruction cards; first card is the Kitchen Speaker Dial
- 2026-10-31 · [epigaea#545](https://github.com/lentago/epigaea/pull/545) — feat(tap-dial): long and multi-presses group the Kitchen Sonos

</details>

### Roadmap: provisioning clients beyond Ansible-on-workstations — VMs and containers as peer targets

[kalmia#20](https://github.com/lentago/kalmia/issues/20) · open since 2026-07-04 · last activity 2026-10-30

> Roadmap for kalmia's shape: a provisioning system whose target classes are peer clients sharing conventions (the idempotency contract, the profile and toggle model, the secrets posture) without sharing implementation, so adding a target class touches no existing one.

Progress: **0/7** sub-issues closed · checklist **0/3** · **1** PR merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [drosera#194](https://github.com/lentago/drosera/issues/194) Adopt grafana-stack (LXC 105) guest capacity from kalmia
- ⬜ [kalmia#51](https://github.com/lentago/kalmia/issues/51) Guarantee vzdump coverage for every Terraform-enforced guest (CT 113 had none)
- ⬜ [kalmia#108](https://github.com/lentago/kalmia/issues/108) Forge: golden images with receipts (checksums, SBOM, provenance)
- ⬜ [kalmia#124](https://github.com/lentago/kalmia/issues/124) Retire CT 113 (n8n LXC) after the osmunda burn-in window
- ⬜ [kalmia#230](https://github.com/lentago/kalmia/issues/230) containers: remove or refuse the docker snap, which takes over apt docker-ce's socket
- ⬜ [kalmia#231](https://github.com/lentago/kalmia/issues/231) k3s install as a kalmia role: take the k3s guests (119, 122) to a joined cluster, with the unprivileged-LXC accommodations — 0/1 sub-issues closed
  - ⬜ [osmunda#4](https://github.com/lentago/osmunda/issues/4) osmunda's node-provisioning disclaimer points at kalmia's k3s role by name (the install lives in kalmia#231)

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-10-29 · [kalmia#211](https://github.com/lentago/kalmia/pull/211) — Rename lunaria to brasenia through runtime: rebuild LXC 118 as brasenia

</details>

### Epic: adoption guide — Phase 3 (receipts for the four near-Kits)

[lupinus#40](https://github.com/lentago/lupinus/issues/40) · open since 2026-11-04 · last activity 2026-11-04

> Phase 2 (#33) closes when #9 lands, with the four near-Kit rows in guide/tiers.md marked provisional instead of receipted.

Progress: **0/4** sub-issues closed · **1** PR merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [.github#331](https://github.com/lentago/.github/issues/331) Adoption receipt: one recorded run of the lock-in ledger from a clean clone
- ⬜ [drosera#309](https://github.com/lentago/drosera/issues/309) Adoption receipt: one timed drill of the status page to a Pages target
- ⬜ [kalmia#281](https://github.com/lentago/kalmia/issues/281) Adoption receipt: a runbook of record and one recorded drill for the Ansible workstation layer
- ⬜ [osmunda#26](https://github.com/lentago/osmunda/issues/26) Adoption receipt: commit the 2026-08-17 EKS drill timings as a receipt under receipts/

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-11-04 · [lupinus#43](https://github.com/lentago/lupinus/pull/43) — Reconcile the single-file ADOPTION.md template with the INTAKE/DRY-RUN split the exemplar uses

</details>

### Roadmap to MVP: prove the desk, file on the user's behalf, run it unattended

[mitchella#31](https://github.com/lentago/mitchella/issues/31) · open since 2026-10-30 · last activity 2026-10-30

> Tracking issue for ROADMAP.md, so the three milestones show their progress as sub-issues.

Progress: **2/12** sub-issues closed · **5** PRs merged in the window

<details><summary>Sub-issues</summary>

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
- ✅ [mitchella#1](https://github.com/lentago/mitchella/issues/1) Exercise the real API path end to end
- ✅ [mitchella#3](https://github.com/lentago/mitchella/issues/3) Slack hardening: visible failures, block limits, retries

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-11-04 · [mitchella#34](https://github.com/lentago/mitchella/pull/34) — Exercise the real API path end to end
- 2026-11-02 · [uvularia#122](https://github.com/lentago/uvularia/pull/122) — Ask: require a valid source for an answered reply; call it source-linked; disclose question logging
- 2026-10-30 · [.github#287](https://github.com/lentago/.github/pull/287) — Epics report: epics, sub-issue progress, and where the merged work went
- 2026-10-12 · [lupinus#25](https://github.com/lentago/lupinus/pull/25) — Stories: one spine, three rungs, one map; one canonical product list
- 2026-10-12 · [lupinus#22](https://github.com/lentago/lupinus/pull/22) — Tiers: refresh brasenia, add mitchella; picker: phones, printers, Wi-Fi

</details>

### Rung 2: the plain organization site, with a rescue import and editing without git — epic

[monarda#18](https://github.com/lentago/monarda/issues/18) · open since 2026-10-12 · last activity 2026-11-04

> Three of the five lupinus stories lean on monarda and two of them need the organization's whole site; the import story only pays off if that page set exists.

Progress: **5/5** sub-issues closed · checklist **3/4** · **7** PRs merged in the window

<details><summary>Sub-issues</summary>

- ✅ [lupinus#39](https://github.com/lentago/lupinus/issues/39) Cite monarda's rung-2 receipt in the tiers.md monarda row
- ✅ [monarda#22](https://github.com/lentago/monarda/issues/22) Rung 2: the plain organization site page set (home, about, programs, events, donate, contact)
- ✅ [monarda#23](https://github.com/lentago/monarda/issues/23) Rescue import: WordPress and Squarespace exports to rung-2 Markdown; Wayback as the last resort
- ✅ [monarda#24](https://github.com/lentago/monarda/issues/24) Editing without git: a git-backed editor (Sveltia CMS or Pages CMS) in front of the organization's own repository
- ✅ [monarda#39](https://github.com/lentago/monarda/issues/39) Rung-2 drill: switch the rung-1 drill site to rung 2, time it, and record its receipt

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-11-04 · [monarda#44](https://github.com/lentago/monarda/pull/44) — Document how a copy takes template updates: adopt uvularia's update door
- 2026-11-04 · [lupinus#41](https://github.com/lentago/lupinus/pull/41) — Cite monarda's rung-2 receipt in the tiers.md monarda row
- 2026-11-04 · [monarda#43](https://github.com/lentago/monarda/pull/43) — Rung-2 drill: switch the rung-1 drill site to rung 2, time it, and record its receipt
- 2026-10-12 · [monarda#28](https://github.com/lentago/monarda/pull/28) — feat: rescue import for WordPress and Squarespace exports
- 2026-10-12 · [monarda#27](https://github.com/lentago/monarda/pull/27) — docs: editing without git (Sveltia CMS, off by default)
- 2026-10-12 · [monarda#26](https://github.com/lentago/monarda/pull/26) — feat: rung 2, the plain organization site page set
- 2026-10-12 · [monarda#25](https://github.com/lentago/monarda/pull/25) — ADR-0004: a second rung, the plain organization site

</details>

### Template repositories: sync on merge (shipped 2026-10-06), drift, and their upkeep — epic

[uvularia#28](https://github.com/lentago/uvularia/issues/28) · open since 2026-10-03 · last activity 2026-10-30

> The App's push-allowlist entry on the three template repositories is still live-only; that is lentago/.github#225, under the secrets epic lentago/.github#286.

Progress: **2/4** sub-issues closed · **10** PRs merged in the window

<details><summary>Sub-issues</summary>

- ⬜ [uvularia#85](https://github.com/lentago/uvularia/issues/85) Template workflow action pins have no automated updater
- ⬜ [uvularia#91](https://github.com/lentago/uvularia/issues/91) templates/site: astro check fails on TypeScript 6 (28 strict-mode errors)
- ✅ [uvularia#98](https://github.com/lentago/uvularia/issues/98) Intake hint says "under library/" but validate resolves source.file from the repo root; first record fails the PR
- ✅ [uvularia#112](https://github.com/lentago/uvularia/issues/112) Upgrade path: how a repository created from a template receives later template changes

</details>

<details><summary>Merged PRs attributed (30d)</summary>

- 2026-11-04 · [uvularia#138](https://github.com/lentago/uvularia/pull/138) — Intake hint and validator: source.file is a path from the repository root, library/ included
- 2026-11-04 · [uvularia-demo-site#8](https://github.com/lentago/uvularia-demo-site/pull/8) — Install the template update door (lentago/uvularia ADR-0003)
- 2026-11-04 · [uvularia-demo-ask-rules#17](https://github.com/lentago/uvularia-demo-ask-rules/pull/17) — Install the template update door (lentago/uvularia ADR-0003)
- 2026-11-04 · [uvularia-demo-records#23](https://github.com/lentago/uvularia-demo-records/pull/23) — Install the template update door (lentago/uvularia ADR-0003)
- 2026-11-04 · [uvularia#137](https://github.com/lentago/uvularia/pull/137) — Update door: fail closed on a bad base, an uncommitted file in the way, or an unreadable branch list; recover a half-finished run
- 2026-11-04 · [uvularia#136](https://github.com/lentago/uvularia/pull/136) — Template upgrade path: an update door that opens a pull request in the client's repository (ADR-0003)
- 2026-11-02 · [uvularia#124](https://github.com/lentago/uvularia/pull/124) — Massachusetts pack: proxy labels, 2027 holidays, no-data on a missing holiday year, and a fixed-date rule kind
- 2026-11-02 · [uvularia#119](https://github.com/lentago/uvularia/pull/119) — templates: add an MIT LICENSE to the three template subtrees
- 2026-11-02 · [uvularia#121](https://github.com/lentago/uvularia/pull/121) — Board standing: re-evaluate on a schedule and show when it was evaluated
- 2026-10-12 · [uvularia#99](https://github.com/lentago/uvularia/pull/99) — Receipts: one-repository rung timed (6 min 09 s); Ask box's first live answer

</details>

---

## Closed in the last 90 days — 13

| Closed | Epic | Sub-issues | Still open underneath | PRs (30d) |
|--------|------|-----------:|----------------------:|----------:|
| 2026-11-04 | [.github#234](https://github.com/lentago/.github/issues/234) Enable Dependabot security updates fleet-wide (codified in terraform) | 4 | **4** | 1 |
| 2026-11-04 | [.github#237](https://github.com/lentago/.github/issues/237) Retire DeepWiki across the fleet | 0 | 0 | 2 |
| 2026-11-04 | [lupinus#33](https://github.com/lentago/lupinus/issues/33) Epic: adoption guide — Phase 2 (receipts for the near-Kits, and the template reconciled) | 2 | 0 | 6 |
| 2026-11-02 | [solidago#180](https://github.com/lentago/solidago/issues/180) Hardening backlog from tf-lint's first trivy run (ECR immutability, CI-role least-privilege, SNS encryption) | 3 | **2** | 5 |
| 2026-10-30 | [kalmia#63](https://github.com/lentago/kalmia/issues/63) Complete the lunaria → brasenia rename through runtime | 0 | 0 | 15 |
| 2026-10-28 | [brasenia#12](https://github.com/lentago/brasenia/issues/12) Second functional path: Cast-native rendering, then deprecate and turn down the Roku/HLS chain | 0 | 0 | 6 |
| 2026-10-14 | [.github#269](https://github.com/lentago/.github/issues/269) Scrub "homelab" and kin: the on-prem half of the estate is "on-prem" | 0 | 0 | 14 |
| 2026-10-13 | [.github#257](https://github.com/lentago/.github/issues/257) Adopt the six-promise map (ADR-0012) — rollout epic | 0 | 0 | 26 |
| 2026-10-13 | [brasenia#26](https://github.com/lentago/brasenia/issues/26) Phase 2: pane bus, compositor, and the first live panes (Cast-first) | 0 | 0 | 0 |
| 2026-10-13 | [drosera#251](https://github.com/lentago/drosera/issues/251) Change pipeline: see every merge travel from push to live, keyed by commit SHA | 1 | **1** | 1 |
| 2026-10-13 | [lupinus#4](https://github.com/lentago/lupinus/issues/4) Epic: adoption guide — Phase 1 (launch set: solidago + monarda) | 5 | 0 | 2 |
| 2026-10-04 | [.github#192](https://github.com/lentago/.github/issues/192) Epic: reposition every reader-facing surface to the pro-bono practice, one reader, one voice (ADR-0008) | 0 | 0 | 1 |
| 2026-08-19 | [.github#162](https://github.com/lentago/.github/issues/162) Epic: adoption guide (lupinus) — Phase 0 enablers | 4 | 0 | 0 |

A closed epic with open sub-issues is a hand-off: the work was spun out and still owes a result.

---

## Where the last 30 days went

**512 PRs merged** across the fleet. Each is attributed once (an epic, or one loose bucket); a PR that serves two epics counts for both.

| Destination | PRs | Share |
|-------------|----:|------:|
| [.github#318](https://github.com/lentago/.github/issues/318) Security review 2026-11-02: fleet follow-through | 59 | 12% |
| [.github#285](https://github.com/lentago/.github/issues/285) Rename debt: the tier 3–4 renames still open across the fleet | 41 | 8% |
| [.github#304](https://github.com/lentago/.github/issues/304) External review 2026-11-01: fleet follow-through | 30 | 6% |
| [claytonia#117](https://github.com/lentago/claytonia/issues/117) Make never-merge a boundary: required check that blocks runner-App PRs without a human approval | 29 | 6% |
| [claytonia#47](https://github.com/lentago/claytonia/issues/47) Roadmap: platform-agnostic workers — Claude Code as one runtime behind the queue contract | 26 | 5% |
| [.github#257](https://github.com/lentago/.github/issues/257) Adopt the six-promise map (ADR-0012) — rollout epic _(closed)_ | 26 | 5% |
| [.github#276](https://github.com/lentago/.github/issues/276) Haiku replaces CodeRabbit as the fleet's PR reviewer | 26 | 5% |
| [epigaea#548](https://github.com/lentago/epigaea/issues/548) Signage: cards, labels and sheets posted at the point of use | 17 | 3% |
| [kalmia#63](https://github.com/lentago/kalmia/issues/63) Complete the lunaria → brasenia rename through runtime _(closed)_ | 15 | 3% |
| [.github#134](https://github.com/lentago/.github/issues/134) Offerings roadmap — tracking epic (refreshed 2026-10-06) | 14 | 3% |
| [.github#269](https://github.com/lentago/.github/issues/269) Scrub "homelab" and kin: the on-prem half of the estate is "on-prem" _(closed)_ | 14 | 3% |
| [betula#74](https://github.com/lentago/betula/issues/74) Roadmap: core/client split — Firewalla and solidago (AWS) as peer collector clients | 12 | 2% |
| [brasenia#130](https://github.com/lentago/brasenia/issues/130) Phase 3: the fleet on the display, and what stays open after ADR-0020 | 12 | 2% |
| [uvularia#28](https://github.com/lentago/uvularia/issues/28) Template repositories: sync on merge (shipped 2026-10-06), drift, and their upkeep — epic | 10 | 2% |
| [monarda#18](https://github.com/lentago/monarda/issues/18) Rung 2: the plain organization site, with a rescue import and editing without git — epic | 7 | 1% |
| [lupinus#33](https://github.com/lentago/lupinus/issues/33) Epic: adoption guide — Phase 2 (receipts for the near-Kits, and the template reconciled) _(closed)_ | 6 | 1% |
| [brasenia#12](https://github.com/lentago/brasenia/issues/12) Second functional path: Cast-native rendering, then deprecate and turn down the Roku/HLS chain _(closed)_ | 6 | 1% |
| [mitchella#31](https://github.com/lentago/mitchella/issues/31) Roadmap to MVP: prove the desk, file on the user's behalf, run it unattended | 5 | 1% |
| [solidago#180](https://github.com/lentago/solidago/issues/180) Hardening backlog from tf-lint's first trivy run (ECR immutability, CI-role least-privilege, SNS encryption) _(closed)_ | 5 | 1% |
| [.github#286](https://github.com/lentago/.github/issues/286) Fleet secrets handling (ADR-0011): the follow-through | 4 | 1% |
| [.github#237](https://github.com/lentago/.github/issues/237) Retire DeepWiki across the fleet _(closed)_ | 2 | 0% |
| [drosera#131](https://github.com/lentago/drosera/issues/131) Roadmap: multi-client telemetry pane — on-prem and solidago (AWS) as peer sources | 2 | 0% |
| [lupinus#4](https://github.com/lentago/lupinus/issues/4) Epic: adoption guide — Phase 1 (launch set: solidago + monarda) _(closed)_ | 2 | 0% |
| [lupinus#40](https://github.com/lentago/lupinus/issues/40) Epic: adoption guide — Phase 3 (receipts for the four near-Kits) | 1 | 0% |
| [.github#234](https://github.com/lentago/.github/issues/234) Enable Dependabot security updates fleet-wide (codified in terraform) _(closed)_ | 1 | 0% |
| [.github#192](https://github.com/lentago/.github/issues/192) Epic: reposition every reader-facing surface to the pro-bono practice, one reader, one voice (ADR-0008) _(closed)_ | 1 | 0% |
| [drosera#251](https://github.com/lentago/drosera/issues/251) Change pipeline: see every merge travel from push to live, keyed by commit SHA _(closed)_ | 1 | 0% |
| [.github#235](https://github.com/lentago/.github/issues/235) Genus marks for the eight unmarked species | 1 | 0% |
| [kalmia#20](https://github.com/lentago/kalmia/issues/20) Roadmap: provisioning clients beyond Ansible-on-workstations — VMs and containers as peer targets | 1 | 0% |
| **All epics** | **268** | **52%** |
| Loose — closes or cites an issue outside any epic | 151 | 29% |
| Loose — no issue reference at all | 12 | 2% |
| Dependabot | 52 | 10% |
| Fleet automation (report refreshes, template sync) | 29 | 6% |

### De-facto epics

Issues outside any epic that at least 4 merged PRs reference. Each is a campaign that ran on a single issue; if it is still open, it is a candidate for the `epic` label or a parent.

| Issue | PRs | Repos touched | State |
|-------|----:|--------------:|-------|
| [solidago#271](https://github.com/lentago/solidago/issues/271) cost: one NAT gateway, Container Insights off, Single-AZ RDS, and a budget that matches the bill | 6 | 1 | closed |
| [solidago#277](https://github.com/lentago/solidago/issues/277) cost: app service to one task on ARM64, Fargate Spot for the site tasks, WAF to two rule groups | 4 | 1 | closed |
| [brasenia#121](https://github.com/lentago/brasenia/issues/121) Compositor: a strict total order, no rotation (ADR-0020: "There should not be ties") | 4 | 1 | closed |
| [.github#264](https://github.com/lentago/.github/issues/264) music-curator leaves the org for cpitzi/music-curator | 4 | 4 | closed |

### Loose work by repo

Where the merged work that no epic describes landed. A tall row is either a program that deserves an epic, or a repo whose convention is direct PRs.

| Repo | With an issue | No issue | Total |
|------|--------------:|---------:|------:|
| kalmia | 51 | 1 | **52** |
| brasenia | 36 | 3 | **39** |
| claytonia | 14 | 0 | **14** |
| .github | 11 | 0 | **11** |
| solidago | 9 | 0 | **9** |
| epigaea | 5 | 4 | **9** |
| drosera | 6 | 2 | **8** |
| shared-workflows | 4 | 1 | **5** |
| uvularia | 3 | 1 | **4** |
| monarda | 3 | 0 | **3** |
| betula | 2 | 0 | **2** |
| asclepias | 2 | 0 | **2** |
| uvularia-demo-site | 1 | 0 | **1** |
| uvularia-demo-ask-rules | 1 | 0 | **1** |
| uvularia-demo-records | 1 | 0 | **1** |
| lupinus | 1 | 0 | **1** |
| site-lentago-dev | 1 | 0 | **1** |

---

## Open issues outside any epic — 65

The backlog the epics do not describe. Some of it is deliberately small and stand-alone; the rest is either a program without a parent or an issue that should be linked under one.

**kalmia** — 10

- [kalmia#304](https://github.com/lentago/kalmia/issues/304) minecraft-lan: update the container description to the Servers join path _(since 2026-11-08)_
- [kalmia#290](https://github.com/lentago/kalmia/issues/290) standing: repeatable test for the model-selection helpers (effective_model / claude_argv) _(since 2026-11-05)_
- [kalmia#286](https://github.com/lentago/kalmia/issues/286) Host the Director and standing EMs on xubuntu-ws: resize VM 102 and provision it as the session host _(since 2026-11-04)_
- [kalmia#277](https://github.com/lentago/kalmia/issues/277) docs: record that standing and director start sessions with Remote Control by default, and the opt-out _(since 2026-11-02)_
- [kalmia#274](https://github.com/lentago/kalmia/issues/274) docs: README's CI table and CLAUDE.md's CI section lag the workflows (pinned shared-workflows tags, five required checks, agent-pr-gate) _(since 2026-11-02)_
- [kalmia#258](https://github.com/lentago/kalmia/issues/258) standing: a running EM can't find a replacement Director; add a fallback order and `standing redirect` _(since 2026-11-02)_
- [kalmia#251](https://github.com/lentago/kalmia/issues/251) site.yml: tagged runs skip the profile/family pre_tasks, so --tags shell renders .bashrc with role defaults _(since 2026-10-31)_
- [kalmia#247](https://github.com/lentago/kalmia/issues/247) standing: concurrent first launches race on new-session; one EM silently not started _(since 2026-10-31)_
- [kalmia#198](https://github.com/lentago/kalmia/issues/198) pe-publish: close the job guard's cancellation window with a publish the runner can't trigger alone _(since 2026-10-29)_
- [kalmia#14](https://github.com/lentago/kalmia/issues/14) Live-test the ubuntu_laptop profile on real ThinkPad hardware _(since 2026-07-01)_

**solidago** — 8

- [solidago#278](https://github.com/lentago/solidago/issues/278) docs/reference-notes.md: the resource-ID table predates the rebuild _(since 2026-11-05)_
- [solidago#276](https://github.com/lentago/solidago/issues/276) teardown: targets still use pre-#82 resource addresses and miss site_pondview _(since 2026-11-05)_
- [solidago#269](https://github.com/lentago/solidago/issues/269) Source the two Axiom ingest secrets from betula's state at their next planned rotation (betula#119) _(since 2026-11-04)_
- [solidago#261](https://github.com/lentago/solidago/issues/261) terraform: bump the AWS provider past 5.100.0 so GuardDuty's newer plans and sub-settings can be declared _(since 2026-11-02)_
- [solidago#255](https://github.com/lentago/solidago/issues/255) docs: ADOPTION.md line references into environments/dev/main.tf have drifted again _(since 2026-11-02)_
- [solidago#240](https://github.com/lentago/solidago/issues/240) Terraform CI roles can read every stack's state in the shared tfstate bucket (Bucket Key blocks per-object KMS scoping) _(since 2026-11-02)_
- [solidago#239](https://github.com/lentago/solidago/issues/239) uvularia-demo SSM slots use the aws/ssm key, which any ReadOnlyAccess principal can decrypt _(since 2026-11-01)_
- [solidago#184](https://github.com/lentago/solidago/issues/184) CI plans are never clean: standing task-definition replacements and a recreating SNS email subscription _(since 2026-08-19)_

**uvularia** — 8

- [uvularia#142](https://github.com/lentago/uvularia/issues/142) Template READMEs carry no co-authorship disclosure _(since 2026-11-04)_
- [uvularia#141](https://github.com/lentago/uvularia/issues/141) Intake hint: name every source kind, and test the whole block it tells you to paste _(since 2026-11-04)_
- [uvularia#140](https://github.com/lentago/uvularia/issues/140) Update door: close the "Template update waiting" issue once the pull request opens _(since 2026-11-04)_
- [uvularia#139](https://github.com/lentago/uvularia/issues/139) template-update.yml: "merge or close it and the next run opens a fresh one" is wrong for a closed update _(since 2026-11-04)_
- [uvularia#129](https://github.com/lentago/uvularia/issues/129) Site template: scope the Pages and OIDC write permissions to the deploy job _(since 2026-11-02)_
- [uvularia#126](https://github.com/lentago/uvularia/issues/126) demo: carry the public-at-once wording (#114) into the demo's own templates _(since 2026-11-02)_
- [uvularia#125](https://github.com/lentago/uvularia/issues/125) template-sync: drift on push compares origin/main, so back-to-back merges fail the earlier run _(since 2026-11-02)_
- [uvularia#123](https://github.com/lentago/uvularia/issues/123) Ask: make the unsourced-answer fallback reply a rules-side setting _(since 2026-11-02)_

**epigaea** — 6

- [epigaea#552](https://github.com/lentago/epigaea/issues/552) Retired RDM001 office remote still registered in ZHA _(since 2026-10-31)_
- [epigaea#551](https://github.com/lentago/epigaea/issues/551) Meeting button ESPHome config is not in git _(since 2026-10-31)_
- [epigaea#546](https://github.com/lentago/epigaea/issues/546) HA-side GitHub PAT returns 403 since the org transfer: version sync and context snapshot pipelines silent since 2026-06-24 _(since 2026-10-31)_
- [epigaea#544](https://github.com/lentago/epigaea/issues/544) Sonos entity ids inverted: media_player.office is the Basement Arc, media_player.office_office is the Office Playbar _(since 2026-10-31)_
- [epigaea#542](https://github.com/lentago/epigaea/issues/542) Proxmox VE integration no longer creates button entities (113 restored orphans; #376 regressed) _(since 2026-10-31)_
- [epigaea#541](https://github.com/lentago/epigaea/issues/541) UPS monitoring blind since ~2026-08-31: NUT connection refused at the NAS _(since 2026-10-31)_

**shared-workflows** — 5

- [shared-workflows#109](https://github.com/lentago/shared-workflows/issues/109) claude-review soft-fail notice drops the reported error text _(since 2026-11-09)_
- [shared-workflows#108](https://github.com/lentago/shared-workflows/issues/108) site-deploy: optional platforms input so a caller can build linux/arm64 (or multi-arch) images _(since 2026-11-05)_
- [shared-workflows#104](https://github.com/lentago/shared-workflows/issues/104) Arming rule: does a head that differs from the reviewed commit only by a rebase onto main count as checked? _(since 2026-11-04)_
- [shared-workflows#87](https://github.com/lentago/shared-workflows/issues/87) Add `timeout-minutes` to every reusable workflow job (8 of 9 have none) _(since 2026-11-01)_
- [shared-workflows#57](https://github.com/lentago/shared-workflows/issues/57) Rapid successive merges cancel site deploys, and `:latest`-pinned task defs make the survivor non-deterministic _(since 2026-08-30)_

**.github** — 4

- [.github#335](https://github.com/lentago/.github/issues/335) Profile: review "a person always decides" after the ADR-0014 amendment _(since 2026-11-04)_
- [.github#329](https://github.com/lentago/.github/issues/329) Census: surface a failed cloc run instead of skipping the repo; add --timeout 0 to the hand-run language-census recipe _(since 2026-11-04)_
- [.github#201](https://github.com/lentago/.github/issues/201) terraform: creating a repo from repos.json fails on GitHub's default labels (422 already_exists) _(since 2026-10-03)_
- [.github#175](https://github.com/lentago/.github/issues/175) A public repo entry with a null template_source cannot receive its first commit _(since 2026-08-28)_

**brasenia** — 4

- [brasenia#145](https://github.com/lentago/brasenia/issues/145) Producers: hold the eight copies of the bus helpers to one hash in a test _(since 2026-11-04)_
- [brasenia#144](https://github.com/lentago/brasenia/issues/144) Pane bus: nothing clears leftovers from viewport/staging/ _(since 2026-11-04)_
- [brasenia#142](https://github.com/lentago/brasenia/issues/142) README: the Roadmap and the "How it works today (Phase 1)" heading still describe Phase 2 as in progress _(since 2026-11-04)_
- [brasenia#139](https://github.com/lentago/brasenia/issues/139) Compositor: a burst of new focus panes flips the wall 8–10 times in under a minute _(since 2026-11-04)_

**claytonia** — 4

- [claytonia#233](https://github.com/lentago/claytonia/issues/233) README § Auth still says installation tokens inherit the full App grant _(since 2026-11-04)_
- [claytonia#222](https://github.com/lentago/claytonia/issues/222) n8n submit form and transcript-shipper comment still carry pre-rename and stale fleet facts _(since 2026-11-04)_
- [claytonia#181](https://github.com/lentago/claytonia/issues/181) Pre-run failures (failed checkout, refused runtime) post nothing on the job's issue _(since 2026-11-02)_
- [claytonia#164](https://github.com/lentago/claytonia/issues/164) A failed cr-update is visible only in the worker's journal _(since 2026-10-31)_

**drosera** — 4

- [drosera#319](https://github.com/lentago/drosera/issues/319) Pick up a betula token rotation without depending on a Terraform-touching merge _(since 2026-11-04)_
- [drosera#295](https://github.com/lentago/drosera/issues/295) Map-keyed dynamic rule blocks rewrite every later rule when a new key sorts mid-list _(since 2026-10-30)_
- [drosera#264](https://github.com/lentago/drosera/issues/264) terraform: cloud_usage rule group shows a perpetual repeat_interval diff (1d vs 24h) _(since 2026-10-07)_
- [drosera#199](https://github.com/lentago/drosera/issues/199) Error-budget monthly section in the fleet report _(since 2026-08-16)_

**site-icecreamtofightwith-com** — 2

- [site-icecreamtofightwith-com#223](https://github.com/lentago/site-icecreamtofightwith-com/issues/223) deploy: build the app image for ARM64 (multi-arch) so solidago can run it on Graviton Fargate _(since 2026-11-05)_
- [site-icecreamtofightwith-com#217](https://github.com/lentago/site-icecreamtofightwith-com/issues/217) deploy.yml header comment names site-deploy @ v1.2.3; the pin is @v1.5.1 _(since 2026-11-02)_

**site-lentago-dev** — 2

- [site-lentago-dev#121](https://github.com/lentago/site-lentago-dev/issues/121) deploy.yml header names a stale site-deploy version _(since 2026-11-02)_
- [site-lentago-dev#86](https://github.com/lentago/site-lentago-dev/issues/86) Remove committed .playwright-mcp/ scratch output and gitignore it _(since 2026-10-03)_

**site-pondviewlane-com** — 2

- [site-pondviewlane-com#104](https://github.com/lentago/site-pondviewlane-com/issues/104) deploy.yml header comment names site-deploy @ v1.2.3; the pin is @v1.5.1 _(since 2026-11-02)_
- [site-pondviewlane-com#46](https://github.com/lentago/site-pondviewlane-com/issues/46) Flip Content-Security-Policy from Report-Only to enforcing _(since 2026-08-16)_

**asclepias** — 1

- [asclepias#31](https://github.com/lentago/asclepias/issues/31) pattern-catalog: claytonia's gitops loop is claytonia-gitops, not bullpen-gitops _(since 2026-11-04)_

**lupinus** — 1

- [lupinus#42](https://github.com/lentago/lupinus/issues/42) Define "rung" once in the guide; it is used across tiers, picker and stories without a definition _(since 2026-11-04)_

**mitchella** — 1

- [mitchella#32](https://github.com/lentago/mitchella/issues/32) StandingProvider: treat a standing row evaluated more than a day ago as degraded, not green _(since 2026-11-01)_

**monarda** — 1

- [monarda#17](https://github.com/lentago/monarda/issues/17) Processor presets in the donate block, each with a sandbox walkthrough; one of them is the #5 receipt _(since 2026-10-12)_

**osmunda** — 1

- [osmunda#27](https://github.com/lentago/osmunda/issues/27) n8n: music-curator's workflows fail on every run — Redis and their env were left in CT 113 _(since 2026-11-04)_

**uvularia-demo-records** — 1

- [uvularia-demo-records#22](https://github.com/lentago/uvularia-demo-records/issues/22) Obligation ma-corp-annual-report is red: the deadline passed _(since 2026-11-02)_

---

## Method

- **Epics:** `gh search issues --owner lentago --label epic` (open, plus closed within 90 days) ∪ every issue with sub-issues and no parent that is open or closed within those 90 days. A labelled open epic that sits under a parent renders there, not at top level; a closed one is taken at top level, since the closed listing carries no parent field this report reads.
- **Sub-issues:** GitHub's native parent/child links, read through the REST `sub_issues` endpoint and followed 3 levels deep. They cross repos inside the org. Link one with `gh api -X POST repos/lentago/<repo>/issues/<epic>/sub_issues -F sub_issue_id=<child id>`.
- **Attribution:** a merged PR counts toward an epic when the epic's body or comments cite the PR, or when the PR's body references an issue in the epic's tree (or the epic itself). Otherwise it is loose: with an issue, or without one. Dependabot and the fleet's own bots are set aside.
- **Limits:** a citation is a citation — an epic that mentions a PR as an example counts it as work. An issue cannot have two parents, so a piece of work that serves two programs sits under one; the other may still cite it.
- **Regenerating:** `python3 metrics/generate-fleet-reports.py --out-dir . --epics-only` (needs `gh`, not `cloc`).

_Generated with Claude Code (Repo Claude)._
