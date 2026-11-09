# Lentago Labs Fleet Report

> [!NOTE]
> **Co-authored with [Claude](https://claude.ai)** (Repo Claude, the Lentago Labs fleet steward). Auto-generated weekly from the fleet's public state (GitHub issues/PRs + `cloc` over public repo contents) — no personal, security, or on-prem-internal detail is included (on-prem: the machines in our own building). A prettier, editorialised copy renders on the on-prem LAN.

**Generated:** 2026-11-09 21:44 UTC · Scope: the **26 active** `lentago` repos (archived repos frozen &amp; excluded) · Activity window: last 30 days (since 2026-10-10).

## Snapshot

| Open issues | PRs merged (30d) | Issues closed (30d) | Code (incl. instructions) | Instruction-markdown |
|---:|---:|---:|---:|---:|
| **200** | 500 | 273 | **164,420** | 2,615 (20 files) |

The fleet's hand-maintained natural-language instruction surface (**2,615 lines** across 20 files) is among the largest "languages" in the code base — `reference-checker` alone is almost entirely prompt-program source.

---

## Open issues — 200 across 19 repos

### .github — 44 open

| # | Title |
|---|-------|
| [335](https://github.com/lentago/.github/issues/335) | Profile: review "a person always decides" after the ADR-0014 amendment |
| [331](https://github.com/lentago/.github/issues/331) | Adoption receipt: one recorded run of the lock-in ledger from a clean clone |
| [329](https://github.com/lentago/.github/issues/329) | Census: surface a failed cloc run instead of skipping the repo; add --timeout 0 to the hand-run language-census recipe |
| [319](https://github.com/lentago/.github/issues/319) | agent-pr-gate verdict: a per-check source in rulesets.tf and a main-only agent-pr-gate environment per gated repo (shared-workflows#97) |
| [318](https://github.com/lentago/.github/issues/318) | Security review 2026-11-02: fleet follow-through |
| [317](https://github.com/lentago/.github/issues/317) | Peer worker runtimes, fleet half: an ADR, disclosure wording for non-Claude agents, and the runtime-label question (claytonia#166) |
| [316](https://github.com/lentago/.github/issues/316) | ADR-0009: add an amendment note that the Ask box is now called source-linked, not grounded |
| [313](https://github.com/lentago/.github/issues/313) | Voice guide: the pull-request definition says "someone else reviews", which the solo-operator merge promise doesn't keep |
| [312](https://github.com/lentago/.github/issues/312) | fleet-reports.yml: arm the refresh PR on its pushed head and drop the immediate-merge fallback |
| [307](https://github.com/lentago/.github/issues/307) | Immutable releases for shared-workflows once the provider supports it |
| [304](https://github.com/lentago/.github/issues/304) | External review 2026-11-01: fleet follow-through |
| [286](https://github.com/lentago/.github/issues/286) | Fleet secrets handling (ADR-0011): the follow-through |
| [285](https://github.com/lentago/.github/issues/285) | Rename debt: the tier 3–4 renames still open across the fleet |
| [282](https://github.com/lentago/.github/issues/282) | brand: genus marks render with black-filled leaves in banners and social cards |
| [276](https://github.com/lentago/.github/issues/276) | Haiku replaces CodeRabbit as the fleet's PR reviewer |
| [271](https://github.com/lentago/.github/issues/271) | [renewal] FLEET_REPORTS_TOKEN — fine-grained PAT expiry — due 2026-10-30 |
| [253](https://github.com/lentago/.github/issues/253) | Offering: Offboarding drill — the access register made real |
| [252](https://github.com/lentago/.github/issues/252) | Offering: Backup with a receipt — object-locked copies and a drilled restore |
| [251](https://github.com/lentago/.github/issues/251) | Offering: Email trust receipt — SPF, DKIM and DMARC as code, an MFA audit, the phishing habit |
| [249](https://github.com/lentago/.github/issues/249) | Offering: Board pack — a one-page monthly operations report the board actually reads |
| [248](https://github.com/lentago/.github/issues/248) | Offering: EOL radar — support end dates open Issues before they bite |
| [247](https://github.com/lentago/.github/issues/247) | Offering: Accessible by default — every page checked, a receipt per build |
| [243](https://github.com/lentago/.github/issues/243) | Credential register: every fleet credential's store, scope, issuer and expiry (names only) |
| [242](https://github.com/lentago/.github/issues/242) | Re-mint two over-broad GitHub tokens: FLEET_REPORTS_TOKEN and the workstation PAT |
| [239](https://github.com/lentago/.github/issues/239) | brand: README header blocks drifted from brand/generated in monarda, osmunda, shared-workflows; coderabbit has none |
| [235](https://github.com/lentago/.github/issues/235) | Genus marks for the eight unmarked species |
| [225](https://github.com/lentago/.github/issues/225) | FLEET_ADMIN_TOKEN cannot resolve GitHub App node ids: merge-gate App allowances are unmanageable by Terraform |
| [201](https://github.com/lentago/.github/issues/201) | terraform: creating a repo from repos.json fails on GitHub's default labels (422 already_exists) |
| [200](https://github.com/lentago/.github/issues/200) | Offering: uvularia — client-owned records vault, grounded Ask, live compliance board (supersedes #128) |
| [196](https://github.com/lentago/.github/issues/196) | Offering: help-desk starter for a private repo — issue forms, labels, a board |
| [195](https://github.com/lentago/.github/issues/195) | Offering: sensor trip opens a work order — epigaea alert to GitHub Issue |
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

### kalmia — 20 open

| # | Title |
|---|-------|
| [304](https://github.com/lentago/kalmia/issues/304) | minecraft-lan: update the container description to the Servers join path |
| [290](https://github.com/lentago/kalmia/issues/290) | standing: repeatable test for the model-selection helpers (effective_model / claude_argv) |
| [286](https://github.com/lentago/kalmia/issues/286) | Host the Director and standing EMs on xubuntu-ws: resize VM 102 and provision it as the session host |
| [281](https://github.com/lentago/kalmia/issues/281) | Adoption receipt: a runbook of record and one recorded drill for the Ansible workstation layer |
| [277](https://github.com/lentago/kalmia/issues/277) | docs: record that standing and director start sessions with Remote Control by default, and the opt-out |
| [274](https://github.com/lentago/kalmia/issues/274) | docs: README's CI table and CLAUDE.md's CI section lag the workflows (pinned shared-workflows tags, five required checks, agent-pr-gate) |
| [262](https://github.com/lentago/kalmia/issues/262) | Downloads, part 2: rpm_key fingerprints, the forge substrate's installers, and fzf |
| [258](https://github.com/lentago/kalmia/issues/258) | standing: a running EM can't find a replacement Director; add a fallback order and `standing redirect` |
| [256](https://github.com/lentago/kalmia/issues/256) | standing: `standing up <repo> --runtime gemini\|codex` — an Engineering Manager on another CLI |
| [251](https://github.com/lentago/kalmia/issues/251) | site.yml: tagged runs skip the profile/family pre_tasks, so --tags shell renders .bashrc with role defaults |
| [247](https://github.com/lentago/kalmia/issues/247) | standing: concurrent first launches race on new-session; one EM silently not started |
| [231](https://github.com/lentago/kalmia/issues/231) | k3s install as a kalmia role: take the k3s guests (119, 122) to a joined cluster, with the unprivileged-LXC accommodations |
| [230](https://github.com/lentago/kalmia/issues/230) | containers: remove or refuse the docker snap, which takes over apt docker-ce's socket |
| [198](https://github.com/lentago/kalmia/issues/198) | pe-publish: close the job guard's cancellation window with a publish the runner can't trigger alone |
| [158](https://github.com/lentago/kalmia/issues/158) | Rename the Proxmox cluster "homelab-cluster" to "onprem" (tier 4) |
| [151](https://github.com/lentago/kalmia/issues/151) | OS stance for a nonprofit fleet; ChromeOS Flex as the first donated-hardware profile |
| [124](https://github.com/lentago/kalmia/issues/124) | Retire CT 113 (n8n LXC) after the osmunda burn-in window |
| [108](https://github.com/lentago/kalmia/issues/108) | Forge: golden images with receipts (checksums, SBOM, provenance) |
| [107](https://github.com/lentago/kalmia/issues/107) | Donated-hardware refresh profiles (new client class) |
| [51](https://github.com/lentago/kalmia/issues/51) | Guarantee vzdump coverage for every Terraform-enforced guest (CT 113 had none) |

### solidago — 19 open

| # | Title |
|---|-------|
| [278](https://github.com/lentago/solidago/issues/278) | docs/reference-notes.md: the resource-ID table predates the rebuild |
| [276](https://github.com/lentago/solidago/issues/276) | teardown: targets still use pre-#82 resource addresses and miss site_pondview |
| [269](https://github.com/lentago/solidago/issues/269) | Source the two Axiom ingest secrets from betula's state at their next planned rotation (betula#119) |
| [261](https://github.com/lentago/solidago/issues/261) | terraform: bump the AWS provider past 5.100.0 so GuardDuty's newer plans and sub-settings can be declared |
| [255](https://github.com/lentago/solidago/issues/255) | docs: ADOPTION.md line references into environments/dev/main.tf have drifted again |
| [240](https://github.com/lentago/solidago/issues/240) | Terraform CI roles can read every stack's state in the shared tfstate bucket (Bucket Key blocks per-object KMS scoping) |
| [239](https://github.com/lentago/solidago/issues/239) | uvularia-demo SSM slots use the aws/ssm key, which any ReadOnlyAccess principal can decrypt |
| [237](https://github.com/lentago/solidago/issues/237) | iam: one shared deploy role and task role span every site, so a trusted site repo can roll any service |
| [233](https://github.com/lentago/solidago/issues/233) | Adoption receipt: one supervised cold run in a fresh AWS account |
| [224](https://github.com/lentago/solidago/issues/224) | ECR tag immutability: deploys reference the image by digest, :latest retires, then IMMUTABLE flips (tf-lint AVD-AWS-0031) |
| [223](https://github.com/lentago/solidago/issues/223) | docs: list the betula and drosera cross-repo roles in ADOPTION.md, and scope BOOTSTRAP's locking note to solidago's own backend |
| [222](https://github.com/lentago/solidago/issues/222) | monitoring: pass the alert recipient as a sensitive variable, out of committed config and public plan output |
| [221](https://github.com/lentago/solidago/issues/221) | On or after 2026-11-06: retire the pre-rename drosera Terraform role and state key (drosera#169 Phase 3) |
| [220](https://github.com/lentago/solidago/issues/220) | iam: give the cross-repo Terraform pipeline roles a read-only plan path |
| [213](https://github.com/lentago/solidago/issues/213) | Fail the apply when an out-of-band secret still holds its placeholder |
| [184](https://github.com/lentago/solidago/issues/184) | CI plans are never clean: standing task-definition replacements and a recreating SNS email subscription |
| [167](https://github.com/lentago/solidago/issues/167) | DMARC posture on our own domains first (precondition for the Email Trust kit) |
| [149](https://github.com/lentago/solidago/issues/149) | Rotating a Lambda's Axiom token requires an unrelated apply to take effect |
| [144](https://github.com/lentago/solidago/issues/144) | Ask Lambda logs land in CloudWatch with no path to Axiom |

### drosera — 18 open

| # | Title |
|---|-------|
| [319](https://github.com/lentago/drosera/issues/319) | Pick up a betula token rotation without depending on a Terraform-touching merge |
| [309](https://github.com/lentago/drosera/issues/309) | Adoption receipt: one timed drill of the status page to a Pages target |
| [305](https://github.com/lentago/drosera/issues/305) | Live transcript for Gemini and Codex runner jobs (runner-transcript.alloy) |
| [304](https://github.com/lentago/drosera/issues/304) | pricing.json: Gemini and Codex price rows, so non-Claude runner jobs get a cost |
| [299](https://github.com/lentago/drosera/issues/299) | On or after 2026-11-06: remove LXC 105's pre-move Alloy volume and unit copies (#169) |
| [295](https://github.com/lentago/drosera/issues/295) | Map-keyed dynamic rule blocks rewrite every later rule when a new key sorts mid-list |
| [282](https://github.com/lentago/drosera/issues/282) | Migrate the cluster="lentago-lab" label value to "onprem" across emitters |
| [276](https://github.com/lentago/drosera/issues/276) | Change pipeline producer on LXC 105: logs:read token and deploy |
| [272](https://github.com/lentago/drosera/issues/272) | Notification-sink contract: one event shape, four sinks, "who gets the call" as a file |
| [264](https://github.com/lentago/drosera/issues/264) | terraform: cloud_usage rule group shows a perpetual repeat_interval diff (1d vs 24h) |
| [204](https://github.com/lentago/drosera/issues/204) | Main-branch workflow failures notify nobody — alert on red deploys/applies |
| [200](https://github.com/lentago/drosera/issues/200) | Queue SLO for the agent fleet (pickup latency) + burn alert |
| [199](https://github.com/lentago/drosera/issues/199) | Error-budget monthly section in the fleet report |
| [198](https://github.com/lentago/drosera/issues/198) | Threat Weather: anonymized daily network weather report |
| [197](https://github.com/lentago/drosera/issues/197) | "Are we open" single source of truth |
| [194](https://github.com/lentago/drosera/issues/194) | Adopt grafana-stack (LXC 105) guest capacity from kalmia |
| [169](https://github.com/lentago/drosera/issues/169) | Complete the homelab-observability → drosera rename through CI and hosts |
| [165](https://github.com/lentago/drosera/issues/165) | New-domain radar: alert when an IoT/smart-home device queries a never-before-seen domain (migrated from betula#11) |

### uvularia — 16 open

| # | Title |
|---|-------|
| [142](https://github.com/lentago/uvularia/issues/142) | Template READMEs carry no co-authorship disclosure |
| [141](https://github.com/lentago/uvularia/issues/141) | Intake hint: name every source kind, and test the whole block it tells you to paste |
| [140](https://github.com/lentago/uvularia/issues/140) | Update door: close the "Template update waiting" issue once the pull request opens |
| [139](https://github.com/lentago/uvularia/issues/139) | template-update.yml: "merge or close it and the next run opens a fresh one" is wrong for a closed update |
| [129](https://github.com/lentago/uvularia/issues/129) | Site template: scope the Pages and OIDC write permissions to the deploy job |
| [126](https://github.com/lentago/uvularia/issues/126) | demo: carry the public-at-once wording (#114) into the demo's own templates |
| [125](https://github.com/lentago/uvularia/issues/125) | template-sync: drift on push compares origin/main, so back-to-back merges fail the earlier run |
| [123](https://github.com/lentago/uvularia/issues/123) | Ask: make the unsourced-answer fallback reply a rules-side setting |
| [102](https://github.com/lentago/uvularia/issues/102) | Dependabot alert 27: http-cache-semantics in templates/site, no fix yet |
| [95](https://github.com/lentago/uvularia/issues/95) | Retention ledger as an obligation pack: the org's own retention policy evaluated against live retention |
| [92](https://github.com/lentago/uvularia/issues/92) | Phase 3 — consumers: the vault-side contract for the funder-report pipeline and Good-Standing reconciliation |
| [91](https://github.com/lentago/uvularia/issues/91) | templates/site: astro check fails on TypeScript 6 (28 strict-mode errors) |
| [85](https://github.com/lentago/uvularia/issues/85) | Template workflow action pins have no automated updater |
| [81](https://github.com/lentago/uvularia/issues/81) | http-cache-semantics GHSA-ch52-4w7c-c8xp: no patched release; not reachable in static builds |
| [57](https://github.com/lentago/uvularia/issues/57) | Records need an event time, and deadlines a local timezone, for lead rules to match the statute for evening meetings |
| [28](https://github.com/lentago/uvularia/issues/28) | Template repositories: sync on merge (shipped 2026-10-06), drift, and their upkeep — epic |

### claytonia — 14 open

| # | Title |
|---|-------|
| [233](https://github.com/lentago/claytonia/issues/233) | README § Auth still says installation tokens inherit the full App grant |
| [222](https://github.com/lentago/claytonia/issues/222) | n8n submit form and transcript-shipper comment still carry pre-rename and stale fleet facts |
| [181](https://github.com/lentago/claytonia/issues/181) | Pre-run failures (failed checkout, refused runtime) post nothing on the job's issue |
| [174](https://github.com/lentago/claytonia/issues/174) | Runtime disclosure on agent PRs: footer and preamble attribution written by run-job |
| [173](https://github.com/lentago/claytonia/issues/173) | Runtime and token fields in .meta and cr-emit; unknown cost as null |
| [172](https://github.com/lentago/claytonia/issues/172) | cr-update: a per-runtime CLI update path |
| [166](https://github.com/lentago/claytonia/issues/166) | Peer worker runtimes: Gemini CLI and Codex CLI behind the queue contract |
| [164](https://github.com/lentago/claytonia/issues/164) | A failed cr-update is visible only in the worker's journal |
| [157](https://github.com/lentago/claytonia/issues/157) | gitops: the loop never notices its own installed copy drifting from the checkout |
| [137](https://github.com/lentago/claytonia/issues/137) | brasenia on the fleet: share mount on the workers, pane command in the worker prompt, fleet beacons |
| [117](https://github.com/lentago/claytonia/issues/117) | Make never-merge a boundary: required check that blocks runner-App PRs without a human approval |
| [116](https://github.com/lentago/claytonia/issues/116) | Close the loop after the PR opens: a capped follow-up job for failing checks and review comments |
| [115](https://github.com/lentago/claytonia/issues/115) | An eval set for the fleet: replayable tasks, deterministic graders, and outcome measures |
| [99](https://github.com/lentago/claytonia/issues/99) | Second job type: batch document/report jobs through the queue contract |

### mitchella — 12 open

| # | Title |
|---|-------|
| [32](https://github.com/lentago/mitchella/issues/32) | StandingProvider: treat a standing row evaluated more than a day ago as degraded, not green |
| [31](https://github.com/lentago/mitchella/issues/31) | Roadmap to MVP: prove the desk, file on the user's behalf, run it unattended |
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

### brasenia — 9 open

| # | Title |
|---|-------|
| [145](https://github.com/lentago/brasenia/issues/145) | Producers: hold the eight copies of the bus helpers to one hash in a test |
| [144](https://github.com/lentago/brasenia/issues/144) | Pane bus: nothing clears leftovers from viewport/staging/ |
| [142](https://github.com/lentago/brasenia/issues/142) | README: the Roadmap and the "How it works today (Phase 1)" heading still describe Phase 2 as in progress |
| [139](https://github.com/lentago/brasenia/issues/139) | Compositor: a burst of new focus panes flips the wall 8–10 times in under a minute |
| [130](https://github.com/lentago/brasenia/issues/130) | Phase 3: the fleet on the display, and what stays open after ADR-0020 |
| [123](https://github.com/lentago/brasenia/issues/123) | Close out the 1280×720 pane contract once the external search panes move (ADR-0019) |
| [41](https://github.com/lentago/brasenia/issues/41) | Lobby-pane variant: a visitor-facing screen in a client's own front room |
| [31](https://github.com/lentago/brasenia/issues/31) | Focus producer: unauthenticated 304s spend the GitHub budget, so focus panes refresh every few minutes, not every minute |
| [15](https://github.com/lentago/brasenia/issues/15) | Adopt the display guest (LXC 118) capacity from kalmia |

### epigaea — 9 open

| # | Title |
|---|-------|
| [552](https://github.com/lentago/epigaea/issues/552) | Retired RDM001 office remote still registered in ZHA |
| [551](https://github.com/lentago/epigaea/issues/551) | Meeting button ESPHome config is not in git |
| [548](https://github.com/lentago/epigaea/issues/548) | Signage: cards, labels and sheets posted at the point of use |
| [546](https://github.com/lentago/epigaea/issues/546) | HA-side GitHub PAT returns 403 since the org transfer: version sync and context snapshot pipelines silent since 2026-06-24 |
| [544](https://github.com/lentago/epigaea/issues/544) | Sonos entity ids inverted: media_player.office is the Basement Arc, media_player.office_office is the Office Playbar |
| [542](https://github.com/lentago/epigaea/issues/542) | Proxmox VE integration no longer creates button entities (113 restored orphans; #376 regressed) |
| [541](https://github.com/lentago/epigaea/issues/541) | UPS monitoring blind since ~2026-08-31: NUT connection refused at the NAS |
| [533](https://github.com/lentago/epigaea/issues/533) | Rename the lentago-lab-status dashboard and the pitzilabs_homelab_observability sensor |
| [518](https://github.com/lentago/epigaea/issues/518) | Complete the epigaea rename through runtime (tiers 3–4) |

### betula — 8 open

| # | Title |
|---|-------|
| [148](https://github.com/lentago/betula/issues/148) | GitHub collector README: dry-run example puts secrets in argv |
| [147](https://github.com/lentago/betula/issues/147) | Cover the pe-publish runner (LXC 123) in the queued-jobs feed |
| [133](https://github.com/lentago/betula/issues/133) | GitHub Actions feed: carry the PR number so PR head SHAs join to merge commits (drosera ADR-0010) |
| [130](https://github.com/lentago/betula/issues/130) | GitHub collector: first-tick backfill ran 7.5 min against a 10 min TimeoutStartSec; checkpoint per repo and reuse connections |
| [126](https://github.com/lentago/betula/issues/126) | Liberation Pipeline: SaaS-export collectors + restore drills, as betula clients (lentago/.github#123) |
| [107](https://github.com/lentago/betula/issues/107) | Device drift self-report: deployed conf hash vs main |
| [106](https://github.com/lentago/betula/issues/106) | Third AWS emitter: CloudTrail → archive + weekly access digest |
| [89](https://github.com/lentago/betula/issues/89) | Complete the firewalla-axiom-pipeline → betula rename on-device |

### osmunda — 6 open

| # | Title |
|---|-------|
| [27](https://github.com/lentago/osmunda/issues/27) | n8n: music-curator's workflows fail on every run — Redis and their env were left in CT 113 |
| [26](https://github.com/lentago/osmunda/issues/26) | Adoption receipt: commit the 2026-08-17 EKS drill timings as a receipt under receipts/ |
| [22](https://github.com/lentago/osmunda/issues/22) | ci: run kube-linter on apps/ and clusters/, with the n8n securityContext as its baseline |
| [16](https://github.com/lentago/osmunda/issues/16) | Move n8n from n8n.lab.lentago.dev to n8n.onprem.lentago.dev |
| [12](https://github.com/lentago/osmunda/issues/12) | Decide how Flux-managed workloads receive secrets, before the n8n cutover |
| [4](https://github.com/lentago/osmunda/issues/4) | osmunda's node-provisioning disclaimer points at kalmia's k3s role by name (the install lives in kalmia#231) |

### shared-workflows — 6 open

| # | Title |
|---|-------|
| [109](https://github.com/lentago/shared-workflows/issues/109) | claude-review soft-fail notice drops the reported error text |
| [108](https://github.com/lentago/shared-workflows/issues/108) | site-deploy: optional platforms input so a caller can build linux/arm64 (or multi-arch) images |
| [104](https://github.com/lentago/shared-workflows/issues/104) | Arming rule: does a head that differs from the reviewed commit only by a rebase onto main count as checked? |
| [87](https://github.com/lentago/shared-workflows/issues/87) | Add `timeout-minutes` to every reusable workflow job (8 of 9 have none) |
| [85](https://github.com/lentago/shared-workflows/issues/85) | site-deploy: register a digest-pinned task-definition revision per deploy and stop pushing :latest |
| [57](https://github.com/lentago/shared-workflows/issues/57) | Rapid successive merges cancel site deploys, and `:latest`-pinned task defs make the survivor non-deterministic |

### site-icecreamtofightwith-com — 4 open

| # | Title |
|---|-------|
| [223](https://github.com/lentago/site-icecreamtofightwith-com/issues/223) | deploy: build the app image for ARM64 (multi-arch) so solidago can run it on Graviton Fargate |
| [217](https://github.com/lentago/site-icecreamtofightwith-com/issues/217) | deploy.yml header comment names site-deploy @ v1.2.3; the pin is @v1.5.1 |
| [198](https://github.com/lentago/site-icecreamtofightwith-com/issues/198) | Clear the npm security-alert backlog (45 open, 42 patchable) |
| [158](https://github.com/lentago/site-icecreamtofightwith-com/issues/158) | Tier accent swatches fail WCAG AA contrast as chip/step backgrounds (design decision needed) |

### site-lentago-dev — 4 open

| # | Title |
|---|-------|
| [121](https://github.com/lentago/site-lentago-dev/issues/121) | deploy.yml header names a stale site-deploy version |
| [112](https://github.com/lentago/site-lentago-dev/issues/112) | Front page: three need-based doors above the suite map (draft PR for review) |
| [86](https://github.com/lentago/site-lentago-dev/issues/86) | Remove committed .playwright-mcp/ scratch output and gitignore it |
| [67](https://github.com/lentago/site-lentago-dev/issues/67) | a11y gate ignores `color-contrast`: the Tidewater palette fails 4.5:1 at the design-token level |

### site-pondviewlane-com — 4 open

| # | Title |
|---|-------|
| [104](https://github.com/lentago/site-pondviewlane-com/issues/104) | deploy.yml header comment names site-deploy @ v1.2.3; the pin is @v1.5.1 |
| [100](https://github.com/lentago/site-pondviewlane-com/issues/100) | Ask widget: send a Cloudflare Turnstile token (enables solidago#241's bot check) |
| [99](https://github.com/lentago/site-pondviewlane-com/issues/99) | Sync the Ask handler reference copy: key read from SSM (solidago#230) |
| [46](https://github.com/lentago/site-pondviewlane-com/issues/46) | Flip Content-Security-Policy from Report-Only to enforcing |

### monarda — 3 open

| # | Title |
|---|-------|
| [18](https://github.com/lentago/monarda/issues/18) | Rung 2: the plain organization site, with a rescue import and editing without git — epic |
| [17](https://github.com/lentago/monarda/issues/17) | Processor presets in the donate block, each with a sandbox walkthrough; one of them is the #5 receipt |
| [11](https://github.com/lentago/monarda/issues/11) | Clear the npm security-alert backlog; add npm to dependabot.yml |

### lupinus — 2 open

| # | Title |
|---|-------|
| [42](https://github.com/lentago/lupinus/issues/42) | Define "rung" once in the guide; it is used across tiers, picker and stories without a definition |
| [40](https://github.com/lentago/lupinus/issues/40) | Epic: adoption guide — Phase 3 (receipts for the four near-Kits) |

### asclepias — 1 open

| # | Title |
|---|-------|
| [31](https://github.com/lentago/asclepias/issues/31) | pattern-catalog: claytonia's gitops loop is claytonia-gitops, not bullpen-gitops |

### uvularia-demo-records — 1 open

| # | Title |
|---|-------|
| [22](https://github.com/lentago/uvularia-demo-records/issues/22) | Obligation ma-corp-annual-report is red: the deadline passed |

## Activity — last 30 days

**773 events**, one stream, newest first — 🟣 500 PRs merged · 🟢 273 issues closed

- 🟢 2026-11-09 · [.github#338](https://github.com/lentago/.github/issues/338) — Claude OAuth token revoked 2026-11-09: PR reviewer and bullpen Claude runtime down
- 🟢 2026-11-09 · [kalmia#307](https://github.com/lentago/kalmia/issues/307) — ubuntu_laptop: codify GNOME Shell extensions (Dash to Panel)
- 🟣 2026-11-09 · [kalmia#308](https://github.com/lentago/kalmia/pull/308) — ubuntu_laptop: codify GNOME Shell extensions (Dash to Panel)
- 🟢 2026-11-08 · [kalmia#305](https://github.com/lentago/kalmia/issues/305) — minecraft-lan: builds far from a player are invisible (client-side chunk generation)
- 🟣 2026-11-08 · [kalmia#306](https://github.com/lentago/kalmia/pull/306) — minecraft-lan: send real chunks to the clients' render distance
- 🟢 2026-11-08 · [kalmia#299](https://github.com/lentago/kalmia/issues/299) — minecraft-lan: joining fails (InitialConnection-145) on NetherNet
- 🟣 2026-11-08 · [kalmia#303](https://github.com/lentago/kalmia/pull/303) — minecraft-lan docs: clients join it as an added server
- 🟢 2026-11-08 · [kalmia#302](https://github.com/lentago/kalmia/issues/302) — minecraft-lan: #300's RakNet transport is unsupported by 1.26 clients
- 🟣 2026-11-08 · [kalmia#301](https://github.com/lentago/kalmia/pull/301) — minecraft-lan: back to NetherNet (1.26 clients don't use RakNet)
- 🟣 2026-11-08 · [kalmia#300](https://github.com/lentago/kalmia/pull/300) — minecraft-lan: switch the transport to RakNet
- 🟢 2026-11-08 · [kalmia#297](https://github.com/lentago/kalmia/issues/297) — LXC 125 minecraft-lan: Bedrock Dedicated Server for the LAN
- 🟣 2026-11-08 · [kalmia#298](https://github.com/lentago/kalmia/pull/298) — LXC 125 minecraft-lan: Bedrock Dedicated Server for the LAN
- 🟣 2026-11-08 · [kalmia#296](https://github.com/lentago/kalmia/pull/296) — minecraft_runner: install make
- 🟢 2026-11-08 · [kalmia#293](https://github.com/lentago/kalmia/issues/293) — LXC 124 minecraft-runner: self-hosted Actions runner for cpitzi/minecraft-builds
- 🟣 2026-11-08 · [kalmia#294](https://github.com/lentago/kalmia/pull/294) — LXC 124 minecraft-runner: self-hosted Actions runner for cpitzi/minecraft-builds
- 🟣 2026-11-05 · [brasenia#148](https://github.com/lentago/brasenia/pull/148) — Family week: wrap instead of cutting text, and fit the type to the band (ADR-0023)
- 🟣 2026-11-05 · [brasenia#147](https://github.com/lentago/brasenia/pull/147) — Family pane: wrap instead of cutting text, and fit the type to the band (ADR-0023)
- 🟢 2026-11-05 · [kalmia#291](https://github.com/lentago/kalmia/issues/291) — standing: detect the Director and EMs running outside tmux
- 🟣 2026-11-05 · [kalmia#292](https://github.com/lentago/kalmia/pull/292) — standing: detect the Director and EMs running outside tmux
- 🟢 2026-11-05 · [solidago#277](https://github.com/lentago/solidago/issues/277) — cost: app service to one task on ARM64, Fargate Spot for the site tasks, WAF to two rule groups
- 🟣 2026-11-05 · [solidago#283](https://github.com/lentago/solidago/pull/283) — cost: remove the temporary bridge services; README cost after #277 (#277, Spot 3/3)
- 🟣 2026-11-05 · [solidago#282](https://github.com/lentago/solidago/pull/282) — cost: lentago and pondview site services on Fargate Spot; ADR-0010 (#277, Spot 2/3)
- 🟢 2026-11-05 · [drosera#320](https://github.com/lentago/drosera/issues/320) — SLO fast-burn page fires on a short Fargate Spot interruption of lentago.dev / pondviewlane.com
- 🟣 2026-11-05 · [drosera#321](https://github.com/lentago/drosera/pull/321) — Tolerate a short single-task gap on the Spot-backed sites' SLO fast-burn page
- 🟣 2026-11-05 · [solidago#281](https://github.com/lentago/solidago/pull/281) — cost: Fargate capacity providers and temporary bridge services for the sites (#277, Spot 1/3)
- 🟣 2026-11-05 · [solidago#280](https://github.com/lentago/solidago/pull/280) — cost: app service floor to one task (#277)
- 🟣 2026-11-05 · [solidago#279](https://github.com/lentago/solidago/pull/279) — cost: WAF to two rules — Common Rule Set and the rate limit (#277)
- 🟢 2026-11-05 · [solidago#271](https://github.com/lentago/solidago/issues/271) — cost: one NAT gateway, Container Insights off, Single-AZ RDS, and a budget that matches the bill
- 🟣 2026-11-05 · [solidago#275](https://github.com/lentago/solidago/pull/275) — cost: raise the dev budget to $175 and update the README cost section (#271, 4/4)
- 🟢 2026-11-05 · [kalmia#288](https://github.com/lentago/kalmia/issues/288) — standing: EMs default to Sonnet 5.5 (supersedes judgment #3)
- 🟣 2026-11-05 · [kalmia#289](https://github.com/lentago/kalmia/pull/289) — standing: make Sonnet 5.5 the default EM model; print the effective model
- 🟣 2026-11-05 · [solidago#274](https://github.com/lentago/solidago/pull/274) — cost: run the dev database Single-AZ (#271, 3/4)
- 🟣 2026-11-05 · [solidago#273](https://github.com/lentago/solidago/pull/273) — cost: turn Container Insights off (#271, 2/4)
- 🟣 2026-11-05 · [solidago#272](https://github.com/lentago/solidago/pull/272) — cost: one NAT gateway for dev (#271, 1/4)
- 🟢 2026-11-05 · [claytonia#213](https://github.com/lentago/claytonia/issues/213) — docs/adr/README.md says every ADR was reconstructed on 2026-08-13
- 🟣 2026-11-05 · [claytonia#225](https://github.com/lentago/claytonia/pull/225) — docs(adr): scope reconstruction note in README to ADR-0001 through ADR-0008
- 🟣 2026-11-05 · [kalmia#287](https://github.com/lentago/kalmia/pull/287) — Resize xubuntu-ws (VM 102) to 16 GiB and 6 vCPU (#286, step 1)
- 🟢 2026-11-04 · [claytonia#212](https://github.com/lentago/claytonia/issues/212) — provision/README.md step 1 keeps a manual PVE pool step that Terraform now does
- 🟣 2026-11-04 · [claytonia#223](https://github.com/lentago/claytonia/pull/223) — docs: remove manual PVE pool step from provision/README.md (#212)
- 🟢 2026-11-04 · [claytonia#210](https://github.com/lentago/claytonia/issues/210) — docs/roadmap.md names the dashboard by its pre-rename title
- 🟣 2026-11-04 · [claytonia#224](https://github.com/lentago/claytonia/pull/224) — docs(roadmap): retitle fleet dashboard to Claytonia — Runner Fleet (#210)
- 🟢 2026-11-04 · [claytonia#209](https://github.com/lentago/claytonia/issues/209) — README § Metrics names the dashboard by its pre-rename title
- 🟣 2026-11-04 · [claytonia#221](https://github.com/lentago/claytonia/pull/221) — docs: retitle fleet dashboard in README § Metrics
- 🟢 2026-11-04 · [claytonia#227](https://github.com/lentago/claytonia/issues/227) — ADR-0008's status line lost its reconstruction tag when it was retired
- 🟣 2026-11-04 · [claytonia#232](https://github.com/lentago/claytonia/pull/232) — docs: restore ADR-0008 acceptance and reconstruction dates
- 🟢 2026-11-04 · [claytonia#218](https://github.com/lentago/claytonia/issues/218) — ADR-0004 says installation tokens inherit the full App grant, which ended with #176
- 🟣 2026-11-04 · [claytonia#231](https://github.com/lentago/claytonia/pull/231) — docs: correct ADR-0004 token permission scope
- 🟢 2026-11-04 · [claytonia#217](https://github.com/lentago/claytonia/issues/217) — ADR-0010 states that jobs run with sudo, which ended with #177
- 🟣 2026-11-04 · [claytonia#230](https://github.com/lentago/claytonia/pull/230) — docs: correct historical sudo access in ADR-0010
- 🟢 2026-11-04 · [claytonia#216](https://github.com/lentago/claytonia/issues/216) — ADR-0009 gives the pre-#186 .meta format for an armed auto-merge
- 🟣 2026-11-04 · [claytonia#229](https://github.com/lentago/claytonia/pull/229) — docs: update ADR-0009 armed auto-merge metadata
- 🟢 2026-11-04 · [claytonia#215](https://github.com/lentago/claytonia/issues/215) — test/fixtures/runtimes/README.md: two capture notes that the adapters have since settled
- 🟣 2026-11-04 · [claytonia#228](https://github.com/lentago/claytonia/pull/228) — docs: refresh runtime capture notes
- 🟢 2026-11-04 · [claytonia#211](https://github.com/lentago/claytonia/issues/211) — test/README.md says the queue-tests workflow ships under test/ci/
- 🟣 2026-11-04 · [claytonia#226](https://github.com/lentago/claytonia/pull/226) — docs(test): update queue-tests workflow location
- 🟢 2026-11-04 · [.github#334](https://github.com/lentago/.github/issues/334) — ADR-0014: the Director may submit the runner-App approval
- 🟣 2026-11-04 · [shared-workflows#107](https://github.com/lentago/shared-workflows/pull/107) — PR-workflow: the Director may submit the runner-App approval
- 🟣 2026-11-04 · [.github#336](https://github.com/lentago/.github/pull/336) — ADR-0014 amendment: the Director may submit the runner-App approval
- 🟢 2026-11-04 · [claytonia#171](https://github.com/lentago/claytonia/issues/171) — rt-codex: Codex CLI adapter
- 🟢 2026-11-04 · [claytonia#170](https://github.com/lentago/claytonia/issues/170) — rt-gemini: Gemini CLI adapter
- 🟢 2026-11-04 · [shared-workflows#105](https://github.com/lentago/shared-workflows/issues/105) — Live-state table: betula now manages the Axiom consumer tokens (betula#119)
- 🟣 2026-11-04 · [shared-workflows#106](https://github.com/lentago/shared-workflows/pull/106) — Live-state table: betula now manages the Axiom consumer tokens
- 🟣 2026-11-04 · [claytonia#220](https://github.com/lentago/claytonia/pull/220) — rt-codex: hand the key to Codex as CODEX_API_KEY, the name exec reads
- 🟣 2026-11-04 · [betula#157](https://github.com/lentago/betula/pull/157) — Describe terraform/'s Axiom tokens and the rotation guard in CLAUDE.md (#119 follow-up)
- 🟣 2026-11-04 · [claytonia#214](https://github.com/lentago/claytonia/pull/214) — rt-gemini: keep the GitHub credential helper through Gemini's git overrides
- 🟢 2026-11-04 · [betula#119](https://github.com/lentago/betula/issues/119) — Terraform the Axiom tokens (exact import + rotation handoff)
- 🟣 2026-11-04 · [claytonia#219](https://github.com/lentago/claytonia/pull/219) — rt-codex: create Codex's home when a worker has none
- 🟢 2026-11-04 · [mitchella#1](https://github.com/lentago/mitchella/issues/1) — Exercise the real API path end to end
- 🟣 2026-11-04 · [mitchella#34](https://github.com/lentago/mitchella/pull/34) — Exercise the real API path end to end
- 🟢 2026-11-04 · [drosera#313](https://github.com/lentago/drosera/issues/313) — Read the Solidago Axiom datasource token from betula's state (betula#119)
- 🟣 2026-11-04 · [drosera#318](https://github.com/lentago/drosera/pull/318) — Take the Solidago Axiom token from betula's state only; drop the variable and the repo secret (#313)
- 🟣 2026-11-04 · [betula#156](https://github.com/lentago/betula/pull/156) — Record what the bootstrap Axiom token needs (#119 step 4)
- 🟣 2026-11-04 · [betula#155](https://github.com/lentago/betula/pull/155) — Narrow cjp-solidago-alb-query to the ALB dataset as a planned rotation (#119 step 3)
- 🟢 2026-11-04 · [.github#332](https://github.com/lentago/.github/issues/332) — Scoped label for betula's token rotation guard override (betula#119)
- 🟣 2026-11-04 · [.github#333](https://github.com/lentago/.github/pull/333) — Scoped label for betula's token rotation guard override (betula#119)
- 🟣 2026-11-04 · [drosera#317](https://github.com/lentago/drosera/pull/317) — Read the Solidago Axiom token from betula's state, falling back to the repo secret (#313, first half)
- 🟣 2026-11-04 · [drosera#316](https://github.com/lentago/drosera/pull/316) — Lift the #169 hold on runner-transcript.alloy: all five workers sync from /opt/drosera
- 🟢 2026-11-04 · [solidago#268](https://github.com/lentago/solidago/issues/268) — iam: let drosera's Terraform role read betula's state key (betula#119)
- 🟣 2026-11-04 · [solidago#270](https://github.com/lentago/solidago/pull/270) — iam: let drosera's Terraform role read betula's state key (betula#119)
- 🟢 2026-11-04 · [drosera#314](https://github.com/lentago/drosera/issues/314) — Stat and bar-gauge splits of a Loki instant query reduce to one value (Runner Fleet runtime split, uvularia demand loop)
- 🟣 2026-11-04 · [drosera#315](https://github.com/lentago/drosera/pull/315) — Show stat and bar-gauge splits of Loki instant queries as one value per row (#314)
- 🟢 2026-11-04 · [drosera#303](https://github.com/lentago/drosera/issues/303) — Claytonia — Runner Fleet: split jobs, failures, duration and cost by runtime, with an unknown cost state
- 🟣 2026-11-04 · [drosera#312](https://github.com/lentago/drosera/pull/312) — Runner Fleet: name stat values, drop the range zero fill, keep the Unpriced column (#303 follow-up)
- 🟣 2026-11-04 · [betula#154](https://github.com/lentago/betula/pull/154) — Export the Axiom token values for consumers to read from betula's state (#119 step 2)
- 🟣 2026-11-04 · [betula#153](https://github.com/lentago/betula/pull/153) — Terraform the Axiom tokens: exact import of the three consumer tokens (#119 step 1)
- 🟣 2026-11-04 · [drosera#310](https://github.com/lentago/drosera/pull/310) — Claytonia — Runner Fleet: split jobs, failures, duration and cost by runtime, with an unknown cost state
- 🟢 2026-11-04 · [brasenia#137](https://github.com/lentago/brasenia/issues/137) — PRs pane: checks, auto-merge and review state on open PRs (needs the ADR-0021 token)
- 🟣 2026-11-04 · [brasenia#146](https://github.com/lentago/brasenia/pull/146) — PRs pane: checks, auto-merge and review state on open PRs (needs the ADR-0021 token)
- 🟢 2026-11-04 · [uvularia#112](https://github.com/lentago/uvularia/issues/112) — Upgrade path: how a repository created from a template receives later template changes
- 🟢 2026-11-04 · [uvularia-demo-site#9](https://github.com/lentago/uvularia-demo-site/issues/9) — Template update waiting
- 🟣 2026-11-04 · [uvularia-demo-site#10](https://github.com/lentago/uvularia-demo-site/pull/10) — Template update: lentago/uvularia-site-template@f72f21f
- 🟢 2026-11-04 · [uvularia-demo-ask-rules#18](https://github.com/lentago/uvularia-demo-ask-rules/issues/18) — Template update waiting
- 🟣 2026-11-04 · [uvularia-demo-ask-rules#19](https://github.com/lentago/uvularia-demo-ask-rules/pull/19) — Template update: lentago/uvularia-rules-template@a4ac573
- 🟢 2026-11-04 · [uvularia-demo-records#24](https://github.com/lentago/uvularia-demo-records/issues/24) — Template update waiting
- 🟣 2026-11-04 · [uvularia-demo-records#25](https://github.com/lentago/uvularia-demo-records/pull/25) — Template update: lentago/uvularia-records-template@0d38258
- 🟣 2026-11-04 · [epigaea#577](https://github.com/lentago/epigaea/pull/577) — feat(signage): one shared stylesheet, copied into every piece and checked in CI
- 🟢 2026-11-04 · [kalmia#280](https://github.com/lentago/kalmia/issues/280) — pub: seed a public-repo read-only GitHub token for brasenia-prs and brasenia-focus (ADR-0021)
- 🟣 2026-11-04 · [kalmia#285](https://github.com/lentago/kalmia/pull/285) — docs(pub): record the first GitHub token seed in the rotation record
- 🟣 2026-11-04 · [epigaea#575](https://github.com/lentago/epigaea/pull/575) — feat(signage): add the label type, a label-maker strip and a sheet label, with the Tap Dial's label
- 🟣 2026-11-04 · [epigaea#571](https://github.com/lentago/epigaea/pull/571) — feat(signage): a QR code on every card and sheet that opens its own live page
- 🟣 2026-11-04 · [claytonia#208](https://github.com/lentago/claytonia/pull/208) — docs: the worker-runtime interface, as shipped for claude, gemini and codex (#47)
- 🟢 2026-11-04 · [claytonia#206](https://github.com/lentago/claytonia/issues/206) — shellcheck.yml: lint the runtime adapters (bin/rt-*)
- 🟣 2026-11-04 · [claytonia#203](https://github.com/lentago/claytonia/pull/203) — rt-codex: Codex CLI adapter (#171)
- 🟣 2026-11-04 · [epigaea#574](https://github.com/lentago/epigaea/pull/574) — feat(signage): render every piece to PDF in CI and publish it beside the HTML
- 🟣 2026-11-04 · [kalmia#284](https://github.com/lentago/kalmia/pull/284) — pub: load a shared GitHub token into brasenia-prs and brasenia-focus (ADR-0021)
- 🟣 2026-11-04 · [epigaea#576](https://github.com/lentago/epigaea/pull/576) — fix(gitops): treat scripts/*.py as a no-op instead of a full Core restart
- 🟢 2026-11-04 · [brasenia#51](https://github.com/lentago/brasenia/issues/51) — Pane bus: a producer's author check isn't atomic with its write, so a claim made in between gets overwritten
- 🟣 2026-11-04 · [brasenia#143](https://github.com/lentago/brasenia/pull/143) — Pane bus: make the author check atomic with the write (a new pane is renamed in whole; ADR-0022)
- 🟢 2026-11-04 · [brasenia#140](https://github.com/lentago/brasenia/issues/140) — Office Roku: nothing brings the brasenia channel back after a reboot or an exit
- 🟣 2026-11-04 · [epigaea#573](https://github.com/lentago/epigaea/pull/573) — feat(signage): an index page listing every piece by room
- 🟣 2026-11-04 · [kalmia#283](https://github.com/lentago/kalmia/pull/283) — Downloads, part 2: rpm_key fingerprints, fzf pinned to a tag, and the AWS CLI's PGP signature
- 🟢 2026-11-04 · [drosera#301](https://github.com/lentago/drosera/issues/301) — uvularia-pipeline: count unsourced Ask turns in the demand panel
- 🟣 2026-11-04 · [drosera#311](https://github.com/lentago/drosera/pull/311) — uvularia-pipeline: count unsourced Ask turns in the demand panel
- 🟣 2026-11-04 · [epigaea#572](https://github.com/lentago/epigaea/pull/572) — feat(signage): check signage meta tags against the files they name
- 🟢 2026-11-04 · [monarda#42](https://github.com/lentago/monarda/issues/42) — Document how a copy takes template updates
- 🟣 2026-11-04 · [monarda#44](https://github.com/lentago/monarda/pull/44) — Document how a copy takes template updates: adopt uvularia's update door
- 🟣 2026-11-04 · [epigaea#570](https://github.com/lentago/epigaea/pull/570) — feat(signage): add the sheet type with the hallway meeting-light placard; move cards under signage/
- 🟢 2026-11-04 · [kalmia#228](https://github.com/lentago/kalmia/issues/228) — forge: the egress check passes on DNS alone
- 🟣 2026-11-04 · [kalmia#282](https://github.com/lentago/kalmia/pull/282) — forge: the egress check passes on DNS alone
- 🟢 2026-11-04 · [brasenia#43](https://github.com/lentago/brasenia/issues/43) — README intro still calls the pane bus and compositor "the roadmap"; ADR-0008 says they run
- 🟣 2026-11-04 · [brasenia#141](https://github.com/lentago/brasenia/pull/141) — README intro: the pane bus and compositor run, they are not the roadmap
- 🟣 2026-11-04 · [uvularia-records-template#21](https://github.com/lentago/uvularia-records-template/pull/21) — Sync from lentago/uvularia@bf5b5b7
- 🟢 2026-11-04 · [lupinus#33](https://github.com/lentago/lupinus/issues/33) — Epic: adoption guide — Phase 2 (receipts for the near-Kits, and the template reconciled)
- 🟢 2026-11-04 · [lupinus#9](https://github.com/lentago/lupinus/issues/9) — Reconcile the single-file ADOPTION.md template with the INTAKE/DRY-RUN split the exemplar uses
- 🟣 2026-11-04 · [lupinus#43](https://github.com/lentago/lupinus/pull/43) — Reconcile the single-file ADOPTION.md template with the INTAKE/DRY-RUN split the exemplar uses
- 🟢 2026-11-04 · [shared-workflows#102](https://github.com/lentago/shared-workflows/issues/102) — Rename discipline: record claytonia#65 (on-host bullpen names) as paid
- 🟣 2026-11-04 · [shared-workflows#103](https://github.com/lentago/shared-workflows/pull/103) — Rename discipline: record claytonia#65 (on-host bullpen names) as paid
- 🟢 2026-11-04 · [uvularia#98](https://github.com/lentago/uvularia/issues/98) — Intake hint says "under library/" but validate resolves source.file from the repo root; first record fails the PR
- 🟣 2026-11-04 · [uvularia#138](https://github.com/lentago/uvularia/pull/138) — Intake hint and validator: source.file is a path from the repository root, library/ included
- 🟢 2026-11-04 · [claytonia#205](https://github.com/lentago/claytonia/issues/205) — rt-gemini: a root-owned Gemini system settings file, so a checkout cannot lift the turn cap or re-enable usage statistics
- 🟣 2026-11-04 · [claytonia#207](https://github.com/lentago/claytonia/pull/207) — Gemini system settings owned by root, and a checkout cannot lift a job's turn cap (#205)
- 🟢 2026-11-04 · [shared-workflows#90](https://github.com/lentago/shared-workflows/issues/90) — PR-workflow text: arm the checked head; a runner-App PR needs a human approval (.github ADR-0014)
- 🟣 2026-11-04 · [shared-workflows#91](https://github.com/lentago/shared-workflows/pull/91) — PR-workflow text: arm the checked head; a runner-App PR needs a human approval (.github ADR-0014)
- 🟢 2026-11-04 · [brasenia#136](https://github.com/lentago/brasenia/issues/136) — ADR-0021: a public-repo read-only GitHub token on pub for the PRs pane
- 🟣 2026-11-04 · [brasenia#138](https://github.com/lentago/brasenia/pull/138) — ADR-0021: a public-read-only GitHub token on pub for the PRs and focus producers
- 🟣 2026-11-04 · [epigaea#569](https://github.com/lentago/epigaea/pull/569) — docs(roku): name the relaunch automation by its live entity id
- 🟢 2026-11-04 · [lupinus#39](https://github.com/lentago/lupinus/issues/39) — Cite monarda's rung-2 receipt in the tiers.md monarda row
- 🟣 2026-11-04 · [lupinus#41](https://github.com/lentago/lupinus/pull/41) — Cite monarda's rung-2 receipt in the tiers.md monarda row
- 🟢 2026-11-04 · [monarda#39](https://github.com/lentago/monarda/issues/39) — Rung-2 drill: switch the rung-1 drill site to rung 2, time it, and record its receipt
- 🟣 2026-11-04 · [monarda#43](https://github.com/lentago/monarda/pull/43) — Rung-2 drill: switch the rung-1 drill site to rung 2, time it, and record its receipt
- 🟣 2026-11-04 · [claytonia#204](https://github.com/lentago/claytonia/pull/204) — rt-gemini: Gemini CLI adapter (#170)
- 🟣 2026-11-04 · [epigaea#568](https://github.com/lentago/epigaea/pull/568) — feat(roku): relaunch the brasenia channel when the office Roku sits on its home screen
- 🟢 2026-11-04 · [claytonia#65](https://github.com/lentago/claytonia/issues/65) — Complete the bullpen → claytonia rename on-host
- 🟣 2026-11-04 · [claytonia#202](https://github.com/lentago/claytonia/pull/202) — Finish the on-host rename: prevent_destroy back on, rebuild runbook in the repo (#65 PR C)
- 🟢 2026-11-04 · [brasenia#99](https://github.com/lentago/brasenia/issues/99) — Roku: on a switch, show the new pane's still image until the stream catches up
- 🟣 2026-11-04 · [claytonia#201](https://github.com/lentago/claytonia/pull/201) — Source the Claude token in rt-claude only (#170 prerequisite)
- 🟣 2026-11-04 · [uvularia-demo-site#8](https://github.com/lentago/uvularia-demo-site/pull/8) — Install the template update door (lentago/uvularia ADR-0003)
- 🟣 2026-11-04 · [uvularia-demo-ask-rules#17](https://github.com/lentago/uvularia-demo-ask-rules/pull/17) — Install the template update door (lentago/uvularia ADR-0003)
- 🟣 2026-11-04 · [uvularia-demo-records#23](https://github.com/lentago/uvularia-demo-records/pull/23) — Install the template update door (lentago/uvularia ADR-0003)
- 🟣 2026-11-04 · [uvularia-rules-template#13](https://github.com/lentago/uvularia-rules-template/pull/13) — Sync from lentago/uvularia@5189e45
- 🟣 2026-11-04 · [uvularia-site-template#20](https://github.com/lentago/uvularia-site-template/pull/20) — Sync from lentago/uvularia@5189e45
- 🟣 2026-11-04 · [uvularia-records-template#20](https://github.com/lentago/uvularia-records-template/pull/20) — Sync from lentago/uvularia@5189e45
- 🟣 2026-11-04 · [uvularia#137](https://github.com/lentago/uvularia/pull/137) — Update door: fail closed on a bad base, an uncommitted file in the way, or an unreadable branch list; recover a half-finished run
- 🟣 2026-11-04 · [claytonia#200](https://github.com/lentago/claytonia/pull/200) — terraform: rebuild claude-runner (110) from runner image v3 (#65 R5)
- 🟢 2026-11-04 · [.github#234](https://github.com/lentago/.github/issues/234) — Enable Dependabot security updates fleet-wide (codified in terraform)
- 🟣 2026-11-04 · [.github#330](https://github.com/lentago/.github/pull/330) — Enable Dependabot security updates fleet-wide (codified in terraform)
- 🟣 2026-11-04 · [uvularia-records-template#19](https://github.com/lentago/uvularia-records-template/pull/19) — Sync from lentago/uvularia@7d6baef
- 🟣 2026-11-04 · [uvularia-site-template#19](https://github.com/lentago/uvularia-site-template/pull/19) — Sync from lentago/uvularia@7d6baef
- 🟣 2026-11-04 · [uvularia-rules-template#12](https://github.com/lentago/uvularia-rules-template/pull/12) — Sync from lentago/uvularia@7d6baef
- 🟣 2026-11-04 · [uvularia#136](https://github.com/lentago/uvularia/pull/136) — Template upgrade path: an update door that opens a pull request in the client's repository (ADR-0003)
- 🟣 2026-11-04 · [claytonia#199](https://github.com/lentago/claytonia/pull/199) — terraform: rebuild claude-runner-2 (111) from runner image v3 (#65 R4)
- 🟢 2026-11-04 · [.github#327](https://github.com/lentago/.github/issues/327) — Weekly fleet-reports refresh fails: cloc's per-file timeout writes a notice after its JSON
- 🟣 2026-11-04 · [.github#328](https://github.com/lentago/.github/pull/328) — Weekly fleet-reports refresh fails: run cloc with --timeout 0 in the census
- 🟢 2026-11-04 · [.github#237](https://github.com/lentago/.github/issues/237) — Retire DeepWiki across the fleet
- 🟣 2026-11-03 · [claytonia#198](https://github.com/lentago/claytonia/pull/198) — terraform: rebuild claude-runner-3 (112) from runner image v3 (#65 R3)
- 🟣 2026-11-03 · [claytonia#197](https://github.com/lentago/claytonia/pull/197) — terraform: rebuild claude-runner-4 (116) from runner image v3 (#65 R2)
- 🟢 2026-11-02 · [kalmia#278](https://github.com/lentago/kalmia/issues/278) — pub: run brasenia's PRs producer (brasenia-prs.service)
- 🟣 2026-11-02 · [kalmia#279](https://github.com/lentago/kalmia/pull/279) — pub: run brasenia's PRs producer (brasenia-prs.service)
- 🟢 2026-11-02 · [brasenia#134](https://github.com/lentago/brasenia/issues/134) — PRs pane: a running list of the fleet's pull requests and their merge status
- 🟣 2026-11-02 · [brasenia#135](https://github.com/lentago/brasenia/pull/135) — PRs pane: a running list of the fleet's pull requests and their merge status
- 🟢 2026-11-02 · [kalmia#275](https://github.com/lentago/kalmia/issues/275) — standing and director: start every EM and the Director with Remote Control enabled
- 🟣 2026-11-02 · [kalmia#276](https://github.com/lentago/kalmia/pull/276) — standing, director: start sessions with Remote Control enabled
- 🟢 2026-11-02 · [claytonia#178](https://github.com/lentago/claytonia/issues/178) — cr-automerge: pin the reviewed head commit and re-check after later pushes (ADR-0014)
- 🟣 2026-11-02 · [claytonia#195](https://github.com/lentago/claytonia/pull/195) — terraform: rebuild claude-runner-5 (117) from runner image v3 (#65 R1)
- 🟣 2026-11-02 · [claytonia#194](https://github.com/lentago/claytonia/pull/194) — terraform: cut new workers from runner image v3 (part of #65)
- 🟣 2026-11-02 · [.github#326](https://github.com/lentago/.github/pull/326) — Require agent-pr-verdict from the gate App on shared-workflows; each required check's source App is set per check (#319)
- 🟢 2026-11-02 · [.github#289](https://github.com/lentago/.github/issues/289) — Require the agent-pr-gate context on every operating repo (claytonia#117 option A)
- 🟣 2026-11-02 · [.github#325](https://github.com/lentago/.github/pull/325) — Require agent-pr-gate on the kits, lupinus and monarda (#289)
- 🟢 2026-11-02 · [shared-workflows#99](https://github.com/lentago/shared-workflows/issues/99) — Run the ci/ unit tests in CI (nothing runs ci/test_*.py today)
- 🟣 2026-11-02 · [shared-workflows#100](https://github.com/lentago/shared-workflows/pull/100) — Run the ci/ unit tests in CI (nothing runs ci/test_*.py today)
- 🟢 2026-11-02 · [monarda#19](https://github.com/lentago/monarda/issues/19) — First run is red: deploy-pages triggers on the template's initial commit before Pages is enabled
- 🟣 2026-11-02 · [monarda#34](https://github.com/lentago/monarda/pull/34) — docs: explain the expected first deploy-pages run
- 🟣 2026-11-02 · [.github#324](https://github.com/lentago/.github/pull/324) — agent-pr-gate: set the gate App ID by hand beside the key, not by Terraform (#319)
- 🟢 2026-11-02 · [shared-workflows#97](https://github.com/lentago/shared-workflows/issues/97) — agent-pr-gate, part 2: a verdict check posted by a dedicated GitHub App and required by its integration ID
- 🟣 2026-11-02 · [shared-workflows#98](https://github.com/lentago/shared-workflows/pull/98) — agent-pr-gate, part 2: a verdict check posted by a dedicated GitHub App and required by its integration ID
- 🟢 2026-11-02 · [monarda#37](https://github.com/lentago/monarda/issues/37) — agent-pr-gate: check the script out from the base branch, not base.sha
- 🟣 2026-11-02 · [monarda#38](https://github.com/lentago/monarda/pull/38) — fix(agent-pr-gate): check the script out from base.ref, not base.sha
- 🟢 2026-11-02 · [lupinus#37](https://github.com/lentago/lupinus/issues/37) — agent-pr-gate: check the script out from the base branch, not base.sha
- 🟣 2026-11-02 · [lupinus#38](https://github.com/lentago/lupinus/pull/38) — ci(agent-pr-gate): check the script out from base.ref, not base.sha
- 🟣 2026-11-02 · [.github#323](https://github.com/lentago/.github/pull/323) — agent-pr-gate environment on shared-workflows: main only, no admin bypass, with the gate App ID (#319)
- 🟢 2026-11-02 · [monarda#35](https://github.com/lentago/monarda/issues/35) — Vendor the agent-pr-gate: a local workflow plus ci/agent_pr_gate.py, no cross-org caller (lentago/.github#289)
- 🟣 2026-11-02 · [monarda#36](https://github.com/lentago/monarda/pull/36) — ci: vendor the agent-pr-gate (shared-workflows v1.6.0)
- 🟢 2026-11-02 · [lupinus#35](https://github.com/lentago/lupinus/issues/35) — Vendor the agent-pr-gate: a local workflow plus ci/agent_pr_gate.py, no cross-org caller (lentago/.github#289)
- 🟣 2026-11-02 · [lupinus#36](https://github.com/lentago/lupinus/pull/36) — ci: vendor the agent-pr-gate from shared-workflows v1.6.0
- 🟣 2026-11-02 · [.github#322](https://github.com/lentago/.github/pull/322) — Require agent-pr-gate on the 17 repos whose callers report it (#289)
- 🟢 2026-11-02 · [kalmia#265](https://github.com/lentago/kalmia/issues/265) — standing: color each session by level and repo for at-a-glance switching
- 🟣 2026-11-02 · [kalmia#273](https://github.com/lentago/kalmia/pull/273) — standing: color each session by level and repo for at-a-glance switching
- 🟢 2026-11-02 · [solidago#265](https://github.com/lentago/solidago/issues/265) — ci: shared-workflows callers sit on three different tags, and the README says docs-check runs @main
- 🟣 2026-11-02 · [solidago#266](https://github.com/lentago/solidago/pull/266) — ci: move the responder, shellcheck and tf-lint callers to shared-workflows v1.6.0; README no longer says @main
- 🟣 2026-11-02 · [claytonia#193](https://github.com/lentago/claytonia/pull/193) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 🟣 2026-11-02 · [site-pondviewlane-com#103](https://github.com/lentago/site-pondviewlane-com/pull/103) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 🟣 2026-11-02 · [site-icecreamtofightwith-com#215](https://github.com/lentago/site-icecreamtofightwith-com/pull/215) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 🟣 2026-11-02 · [uvularia#135](https://github.com/lentago/uvularia/pull/135) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 🟣 2026-11-02 · [solidago#264](https://github.com/lentago/solidago/pull/264) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 🟣 2026-11-02 · [site-lentago-dev#123](https://github.com/lentago/site-lentago-dev/pull/123) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 🟣 2026-11-02 · [repo-template#33](https://github.com/lentago/repo-template/pull/33) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 🟣 2026-11-02 · [osmunda#24](https://github.com/lentago/osmunda/pull/24) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 🟣 2026-11-02 · [mitchella#33](https://github.com/lentago/mitchella/pull/33) — Add the agent-pr-gate caller (lentago/.github#289)
- 🟣 2026-11-02 · [kalmia#271](https://github.com/lentago/kalmia/pull/271) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 🟣 2026-11-02 · [epigaea#566](https://github.com/lentago/epigaea/pull/566) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 🟣 2026-11-02 · [drosera#307](https://github.com/lentago/drosera/pull/307) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 🟣 2026-11-02 · [brasenia#132](https://github.com/lentago/brasenia/pull/132) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 🟣 2026-11-02 · [betula#150](https://github.com/lentago/betula/pull/150) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 🟣 2026-11-02 · [asclepias#29](https://github.com/lentago/asclepias/pull/29) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 🟢 2026-11-02 · [site-pondviewlane-com#101](https://github.com/lentago/site-pondviewlane-com/issues/101) — Bump site-deploy caller to shared-workflows@v1.5.1
- 🟣 2026-11-02 · [site-pondviewlane-com#102](https://github.com/lentago/site-pondviewlane-com/pull/102) — ci: bump site-deploy shared workflow to v1.5.1
- 🟢 2026-11-02 · [site-icecreamtofightwith-com#214](https://github.com/lentago/site-icecreamtofightwith-com/issues/214) — Bump site-deploy caller to shared-workflows@v1.5.1
- 🟣 2026-11-02 · [site-icecreamtofightwith-com#216](https://github.com/lentago/site-icecreamtofightwith-com/pull/216) — ci: bump site-deploy reusable workflow pin to v1.5.1
- 🟢 2026-11-02 · [kalmia#255](https://github.com/lentago/kalmia/issues/255) — forge: the claytonia runner image carries the Gemini and Codex CLIs (claytonia-runner-v3)
- 🟣 2026-11-02 · [.github#320](https://github.com/lentago/.github/pull/320) — Add the agent-pr-gate caller and move docs-check to v1.6.0 (lentago/.github#289)
- 🟢 2026-11-02 · [site-lentago-dev#117](https://github.com/lentago/site-lentago-dev/issues/117) — Bump site-deploy caller to shared-workflows@v1.5.1
- 🟣 2026-11-02 · [site-lentago-dev#120](https://github.com/lentago/site-lentago-dev/pull/120) — Bump site-deploy caller to shared-workflows@v1.5.1
- 🟢 2026-11-02 · [kalmia#264](https://github.com/lentago/kalmia/issues/264) — forge: replace the runner image's blanket sudoers rule with claytonia#177's narrow entries
- 🟣 2026-11-02 · [kalmia#270](https://github.com/lentago/kalmia/pull/270) — forge: replace the runner image's blanket sudoers rule with claytonia#177's narrow entries
- 🟢 2026-11-02 · [claytonia#190](https://github.com/lentago/claytonia/issues/190) — gitops: a run that loses the lock reports success, and install.sh races its own first deploy
- 🟣 2026-11-02 · [claytonia#192](https://github.com/lentago/claytonia/pull/192) — gitops: a run that loses the lock waits instead of reporting success; install.sh deploys before enabling the timer
- 🟢 2026-11-02 · [claytonia#177](https://github.com/lentago/claytonia/issues/177) — Keep the App private key out of the agent's reach: root-owned token broker
- 🟣 2026-11-02 · [claytonia#191](https://github.com/lentago/claytonia/pull/191) — Keep the App private key out of the agent's reach: root-owned token broker
- 🟢 2026-11-02 · [solidago#260](https://github.com/lentago/solidago/issues/260) — budgets: the account budget ($100) sits below the ~$220 run rate, so it alerts every month; README cost figures are stale
- 🟣 2026-11-02 · [solidago#263](https://github.com/lentago/solidago/pull/263) — docs: correct the stated run rate to the observed $212–222/month; note the $100 budget is below it by choice
- 🟢 2026-11-02 · [kalmia#268](https://github.com/lentago/kalmia/issues/268) — forge: the claytonia layer races claytonia-gitops' own timer for its lock, so the forced deploy can exit 0 having deployed nothing (v3 attempt 2 failed)
- 🟣 2026-11-02 · [kalmia#269](https://github.com/lentago/kalmia/pull/269) — forge: the claytonia layer races claytonia-gitops' own timer for its lock, so the forced deploy can exit 0 having deployed nothing (v3 attempt 2 failed)
- 🟢 2026-11-02 · [solidago#262](https://github.com/lentago/solidago/issues/262) — guardduty: feature sub-settings force a replacement every plan, and RDS data-activity monitoring is on by default (+$6/month)
- 🟣 2026-11-02 · [solidago#259](https://github.com/lentago/solidago/pull/259) — guardduty: correct the header on the AI plans, stop a perpetual replace-diff, turn off RDS data-activity monitoring
- 🟢 2026-11-02 · [kalmia#266](https://github.com/lentago/kalmia/issues/266) — forge: build.sh feeds scripts to pct exec on stdin, so a command that reads stdin silently ends the substrate (v3 build failed)
- 🟣 2026-11-02 · [kalmia#267](https://github.com/lentago/kalmia/pull/267) — forge: build.sh feeds scripts to pct exec on stdin, so a command that reads stdin silently ends the substrate (v3 build failed)
- 🟣 2026-11-02 · [solidago#258](https://github.com/lentago/solidago/pull/258) — guardduty: enable the detector, email findings of severity 4+ to the alert topic, add a GuardDuty budget alarm (#243)
- 🟢 2026-11-02 · [solidago#245](https://github.com/lentago/solidago/issues/245) — waf logging and ECS deployment circuit breaker
- 🟣 2026-11-02 · [solidago#257](https://github.com/lentago/solidago/pull/257) — waf: log every request to a 30-day aws-waf-logs group, authorization and cookie redacted (#245, WAF-logging half)
- 🟢 2026-11-02 · [solidago#243](https://github.com/lentago/solidago/issues/243) — guardduty: enable the detector in Terraform (decision 2 on the epic)
- 🟣 2026-11-02 · [solidago#256](https://github.com/lentago/solidago/pull/256) — iam: let the apply role manage the GuardDuty detector and this stack's EventBridge rules (#243, step 1)
- 🟢 2026-11-02 · [claytonia#188](https://github.com/lentago/claytonia/issues/188) — cr-publish-share stamps every copy 'unknown': git refuses the root-owned gitops checkout
- 🟣 2026-11-02 · [claytonia#189](https://github.com/lentago/claytonia/pull/189) — cr-publish-share: read the stamp from the root-owned checkout
- 🟢 2026-11-02 · [claytonia#185](https://github.com/lentago/claytonia/issues/185) — Put the queue's NAS README under version control and publish it to the share from main
- 🟣 2026-11-02 · [claytonia#187](https://github.com/lentago/claytonia/pull/187) — Put the queue's NAS README under version control and publish it to the share from main
- 🟢 2026-11-02 · [shared-workflows#95](https://github.com/lentago/shared-workflows/issues/95) — docs-check: github.job_workflow_ref is empty, so callers run main's link resolver instead of the pinned tag's
- 🟣 2026-11-02 · [shared-workflows#96](https://github.com/lentago/shared-workflows/pull/96) — docs-check: run the resolver at the ref the caller pinned (github.job_workflow_ref is empty)
- 🟢 2026-11-02 · [shared-workflows#84](https://github.com/lentago/shared-workflows/issues/84) — agent-pr-gate: a required check that fails on runner-App PRs without a human approving review (claytonia#117 option A)
- 🟣 2026-11-02 · [shared-workflows#94](https://github.com/lentago/shared-workflows/pull/94) — agent-pr-gate: a required check that fails on runner-App PRs without a human approving review (claytonia#117 option A)
- 🟣 2026-11-02 · [claytonia#186](https://github.com/lentago/claytonia/pull/186) — cr-automerge: pin the reviewed head commit and re-check after later pushes
- 🟢 2026-11-02 · [claytonia#176](https://github.com/lentago/claytonia/issues/176) — gh-token: scope installation tokens to the job's repository and minimum permissions
- 🟣 2026-11-02 · [claytonia#184](https://github.com/lentago/claytonia/pull/184) — gh-token: scope installation tokens to the job's repository and minimum permissions
- 🟢 2026-11-02 · [claytonia#169](https://github.com/lentago/claytonia/issues/169) — Test stubs and bats for the runtime seam
- 🟣 2026-11-02 · [claytonia#183](https://github.com/lentago/claytonia/pull/183) — Test stubs and bats for the runtime seam
- 🟢 2026-11-02 · [claytonia#179](https://github.com/lentago/claytonia/issues/179) — run-job: two workers lack uuidgen, so ~45% of jobs record no session id and lose their transcript
- 🟣 2026-11-02 · [claytonia#182](https://github.com/lentago/claytonia/pull/182) — run-job: a session id is never empty, uuidgen or not
- 🟢 2026-11-02 · [claytonia#168](https://github.com/lentago/claytonia/issues/168) — Runtime key in the job spec, registry, runner.env and cr-submit, with runtime-scoped model precedence
- 🟣 2026-11-02 · [claytonia#180](https://github.com/lentago/claytonia/pull/180) — Runtime key in the job spec, registry, runner.env and cr-submit, with runtime-scoped model precedence
- 🟢 2026-11-02 · [shared-workflows#92](https://github.com/lentago/shared-workflows/issues/92) — site-deploy: fail the job when ECS rolls the deployment back (circuit breaker makes services-stable report green)
- 🟣 2026-11-02 · [shared-workflows#93](https://github.com/lentago/shared-workflows/pull/93) — site-deploy: fail the job when ECS rolls the deployment back (circuit breaker makes services-stable report green)
- 🟢 2026-11-02 · [solidago#246](https://github.com/lentago/solidago/issues/246) — logs: decide on a CMK for the CloudWatch log groups (default key today)
- 🟣 2026-11-02 · [solidago#254](https://github.com/lentago/solidago/pull/254) — logs: decide on a CMK for the CloudWatch log groups (default key, except the Ask log)
- 🟣 2026-11-02 · [solidago#253](https://github.com/lentago/solidago/pull/253) — ecs: deployment circuit breaker with rollback on every service (#245, circuit-breaker half)
- 🟢 2026-11-02 · [solidago#242](https://github.com/lentago/solidago/issues/242) — iam: scope the ECS task and execution roles' secret read to the one RDS secret in use
- 🟣 2026-11-02 · [solidago#249](https://github.com/lentago/solidago/pull/249) — iam: remove the shared ECS roles' database secret grants (no service uses the RDS secret)
- 🟢 2026-11-02 · [claytonia#167](https://github.com/lentago/claytonia/issues/167) — Extract the Claude invocation into bin/rt-claude with no behavior change
- 🟣 2026-11-02 · [claytonia#175](https://github.com/lentago/claytonia/pull/175) — Extract the Claude invocation into bin/rt-claude with no behavior change
- 🟢 2026-11-02 · [solidago#244](https://github.com/lentago/solidago/issues/244) — cloudtrail: metric filters and alarms for root use, no-MFA sign-in, IAM and trail changes, unauthorized calls
- 🟣 2026-11-02 · [solidago#252](https://github.com/lentago/solidago/pull/252) — cloudtrail: metric filters and alarms for root use, no-MFA sign-in, IAM and trail changes, unauthorized calls
- 🟢 2026-11-02 · [kalmia#259](https://github.com/lentago/kalmia/issues/259) — Downloads: checksums on every get_url and pinned releases instead of curl\|sh installers
- 🟣 2026-11-02 · [kalmia#263](https://github.com/lentago/kalmia/pull/263) — Downloads: checksums on every get_url and pinned releases instead of curl\|sh installers
- 🟢 2026-11-02 · [solidago#250](https://github.com/lentago/solidago/issues/250) — monitoring: alert topics' policies block CloudWatch alarms from publishing, so no alarm notifies
- 🟣 2026-11-02 · [solidago#251](https://github.com/lentago/solidago/pull/251) — monitoring: let CloudWatch alarms publish to the alert topics
- 🟢 2026-11-02 · [osmunda#20](https://github.com/lentago/osmunda/issues/20) — n8n: complete the pod securityContext (privilege escalation, capabilities, seccomp)
- 🟣 2026-11-02 · [osmunda#21](https://github.com/lentago/osmunda/pull/21) — fix(n8n): complete pod and container securityContext
- 🟢 2026-11-02 · [kalmia#260](https://github.com/lentago/kalmia/issues/260) — forge: the runner substrate installs uuid-runtime, so workers have uuidgen (claytonia#179)
- 🟣 2026-11-02 · [kalmia#261](https://github.com/lentago/kalmia/pull/261) — forge: the runner substrate installs uuid-runtime, so workers have uuidgen (claytonia#179)
- 🟣 2026-11-02 · [solidago#248](https://github.com/lentago/solidago/pull/248) — ask-lambda: harden the public Ask endpoint (durable cap, Turnstile, concurrency, timeout, alarms)
- 🟢 2026-11-02 · [site-lentago-dev#115](https://github.com/lentago/site-lentago-dev/issues/115) — CSP: enforce the policy; report-only with no report endpoint does nothing
- 🟣 2026-11-02 · [site-lentago-dev#116](https://github.com/lentago/site-lentago-dev/pull/116) — fix(nginx): enforce the Content-Security-Policy
- 🟢 2026-11-02 · [solidago#241](https://github.com/lentago/solidago/issues/241) — ask-lambda: harden the public Ask endpoint (shared cap, Turnstile, reserved concurrency, timeout, alarm)
- 🟣 2026-11-02 · [solidago#247](https://github.com/lentago/solidago/pull/247) — iam: let the apply role manage this stack's DynamoDB tables (#241 step 1 of 2)
- 🟣 2026-11-02 · [kalmia#257](https://github.com/lentago/kalmia/pull/257) — forge: the claytonia runner image carries the Gemini and Codex CLIs (claytonia-runner-v3)
- 🟢 2026-11-02 · [drosera#300](https://github.com/lentago/drosera/issues/300) — README: replace "humans own every merge" with the ADR-0014 wording
- 🟣 2026-11-02 · [drosera#302](https://github.com/lentago/drosera/pull/302) — docs(readme): replace merge-ownership sentence with ADR-0014 wording
- 🟢 2026-11-02 · [asclepias#26](https://github.com/lentago/asclepias/issues/26) — estate-atlas: replace "humans own every merge" with the ADR-0014 wording
- 🟣 2026-11-02 · [asclepias#27](https://github.com/lentago/asclepias/pull/27) — docs(estate-atlas): adopt ADR-0014 merge-promise wording
- 🟢 2026-11-02 · [lupinus#8](https://github.com/lentago/lupinus/issues/8) — Kit rows carry no receipt: mark them provisional or demote until a drill is recorded
- 🟣 2026-11-02 · [lupinus#34](https://github.com/lentago/lupinus/pull/34) — tiers: add Readiness column; mark unreceipted Kit/Platform rows provisional
- 🟢 2026-11-02 · [shared-workflows#88](https://github.com/lentago/shared-workflows/issues/88) — ADR-0005: 'immutable' is a convention until the tag ruleset lands; say so and reference it
- 🟣 2026-11-02 · [shared-workflows#89](https://github.com/lentago/shared-workflows/pull/89) — docs(adr): ADR-0005 addendum on tag immutability and SHA pinning
- 🟢 2026-11-02 · [uvularia#132](https://github.com/lentago/uvularia/issues/132) — README banner alt text still says "grounded Ask"
- 🟣 2026-11-02 · [uvularia#134](https://github.com/lentago/uvularia/pull/134) — Banner: source-linked Ask, regenerated from the brand output
- 🟢 2026-11-02 · [.github#310](https://github.com/lentago/.github/issues/310) — uvularia repo description and banner alt still say "grounded Ask"; align with the source-linked wording
- 🟣 2026-11-02 · [.github#315](https://github.com/lentago/.github/pull/315) — uvularia repo description and banner: source-linked Ask, not grounded
- 🟢 2026-11-02 · [.github#311](https://github.com/lentago/.github/issues/311) — Codify solidago's GitHub environments: terraform with a main-only branch policy, terraform-plan with no rules
- 🟣 2026-11-02 · [.github#314](https://github.com/lentago/.github/pull/314) — Codify solidago's GitHub environments: terraform with a main-only branch policy, terraform-plan with no rules
- 🟢 2026-11-02 · [solidago#156](https://github.com/lentago/solidago/issues/156) — Split plan/apply OIDC environments so the terraform environment can carry a branch policy
- 🟣 2026-11-02 · [solidago#227](https://github.com/lentago/solidago/pull/227) — ci(terraform): plan in the terraform-plan environment on the read-only role (#225 step 2 of 2)
- 🟢 2026-11-02 · [solidago#180](https://github.com/lentago/solidago/issues/180) — Hardening backlog from tf-lint's first trivy run (ECR immutability, CI-role least-privilege, SNS encryption)
- 🟢 2026-11-02 · [solidago#225](https://github.com/lentago/solidago/issues/225) — Split the Terraform CI role: read-only plan credentials on pull requests, write apply credentials on main (tf-lint AVD-AWS-0345)
- 🟣 2026-11-02 · [solidago#226](https://github.com/lentago/solidago/pull/226) — feat(iam): read-only Terraform plan role on the terraform-plan environment (#225 step 1 of 2)
- 🟢 2026-11-02 · [.github#306](https://github.com/lentago/.github/issues/306) — ADR: the merge promise, humans approve agent PRs, policy-owned merges for routines and session-armed PRs
- 🟣 2026-11-02 · [.github#309](https://github.com/lentago/.github/pull/309) — ADR-0014: the merge promise — humans approve agent PRs, policy-owned merges for routines and session-armed PRs
- 🟣 2026-11-02 · [uvularia#133](https://github.com/lentago/uvularia/pull/133) — README banner alt text: source-linked Ask, not grounded Ask
- 🟢 2026-11-02 · [solidago#230](https://github.com/lentago/solidago/issues/230) — ask-lambda: read the Anthropic key from SSM at runtime instead of a Terraform variable, then rotate it
- 🟣 2026-11-02 · [solidago#236](https://github.com/lentago/solidago/pull/236) — ask-lambda: read the Anthropic key from SSM at runtime instead of a Terraform variable
- 🟣 2026-11-02 · [uvularia-demo-ask-rules#16](https://github.com/lentago/uvularia-demo-ask-rules/pull/16) — Sync the 2026-11-01 review batch from lentago/uvularia@4b2226e
- 🟣 2026-11-02 · [uvularia-demo-site#7](https://github.com/lentago/uvularia-demo-site/pull/7) — Sync the 2026-11-01 review batch from lentago/uvularia@4b2226e
- 🟣 2026-11-02 · [uvularia-site-template#17](https://github.com/lentago/uvularia-site-template/pull/17) — Sync from lentago/uvularia@90aac48
- 🟣 2026-11-02 · [uvularia-site-template#18](https://github.com/lentago/uvularia-site-template/pull/18) — Sync from lentago/uvularia@99973ee
- 🟢 2026-11-02 · [uvularia#128](https://github.com/lentago/uvularia/issues/128) — Ask: README overstates the source rule; the question-log wiring test matches a commented line
- 🟣 2026-11-02 · [uvularia#131](https://github.com/lentago/uvularia/pull/131) — Ask: README states the source rule precisely; the question-log wiring test ignores commented lines
- 🟢 2026-11-02 · [uvularia#127](https://github.com/lentago/uvularia/issues/127) — Site home page counts lapsed standing rows as their colour
- 🟣 2026-11-02 · [uvularia#130](https://github.com/lentago/uvularia/pull/130) — Site home page: count lapsed standing rows as unknown
- 🟣 2026-11-02 · [uvularia-demo-records#21](https://github.com/lentago/uvularia-demo-records/pull/21) — Sync the 2026-11-01 review batch from lentago/uvularia@4b2226e
- 🟣 2026-11-02 · [uvularia-site-template#16](https://github.com/lentago/uvularia-site-template/pull/16) — Sync from lentago/uvularia@4b2226e
- 🟣 2026-11-02 · [uvularia-records-template#18](https://github.com/lentago/uvularia-records-template/pull/18) — Sync from lentago/uvularia@4b2226e
- 🟣 2026-11-02 · [uvularia-records-template#17](https://github.com/lentago/uvularia-records-template/pull/17) — Sync from lentago/uvularia@a08509d
- 🟣 2026-11-02 · [uvularia-rules-template#11](https://github.com/lentago/uvularia-rules-template/pull/11) — Sync from lentago/uvularia@4b2226e
- 🟢 2026-11-02 · [uvularia#117](https://github.com/lentago/uvularia/issues/117) — Ask function: require a valid source for an answered reply, call it source-linked, disclose question logging
- 🟣 2026-11-02 · [uvularia#122](https://github.com/lentago/uvularia/pull/122) — Ask: require a valid source for an answered reply; call it source-linked; disclose question logging
- 🟢 2026-11-02 · [uvularia#116](https://github.com/lentago/uvularia/issues/116) — Massachusetts pack: label proxy rules as operational reminders, add 2027 holidays, fail unknown on a missing holiday year
- 🟣 2026-11-02 · [uvularia#124](https://github.com/lentago/uvularia/pull/124) — Massachusetts pack: proxy labels, 2027 holidays, no-data on a missing holiday year, and a fixed-date rule kind
- 🟣 2026-11-02 · [uvularia-site-template#15](https://github.com/lentago/uvularia-site-template/pull/15) — Sync from lentago/uvularia@7ab8ddc
- 🟣 2026-11-02 · [uvularia-records-template#16](https://github.com/lentago/uvularia-records-template/pull/16) — Sync from lentago/uvularia@7ab8ddc
- 🟣 2026-11-02 · [uvularia-rules-template#10](https://github.com/lentago/uvularia-rules-template/pull/10) — Sync from lentago/uvularia@7ab8ddc
- 🟣 2026-11-02 · [uvularia-site-template#14](https://github.com/lentago/uvularia-site-template/pull/14) — Sync from lentago/uvularia@0390524
- 🟢 2026-11-02 · [uvularia#118](https://github.com/lentago/uvularia/issues/118) — Templates carry no license: add LICENSE to templates/records, templates/site and templates/ask-rules
- 🟣 2026-11-02 · [uvularia#119](https://github.com/lentago/uvularia/pull/119) — templates: add an MIT LICENSE to the three template subtrees
- 🟣 2026-11-02 · [uvularia-records-template#15](https://github.com/lentago/uvularia-records-template/pull/15) — Sync from lentago/uvularia@0390524
- 🟣 2026-11-02 · [uvularia-site-template#13](https://github.com/lentago/uvularia-site-template/pull/13) — Sync from lentago/uvularia@ee9fc33
- 🟣 2026-11-02 · [uvularia-records-template#14](https://github.com/lentago/uvularia-records-template/pull/14) — Sync from lentago/uvularia@ee9fc33
- 🟢 2026-11-02 · [uvularia#114](https://github.com/lentago/uvularia/issues/114) — Records template: say that issues, branches and attachments in the public repository are visible at once
- 🟣 2026-11-02 · [uvularia#120](https://github.com/lentago/uvularia/pull/120) — records template: say that issues, branches and attachments are public at once
- 🟢 2026-11-02 · [uvularia#115](https://github.com/lentago/uvularia/issues/115) — Board standing goes stale between publishes: re-evaluate on a schedule and show when it was evaluated
- 🟣 2026-11-02 · [uvularia#121](https://github.com/lentago/uvularia/pull/121) — Board standing: re-evaluate on a schedule and show when it was evaluated
- 🟢 2026-11-01 · [solidago#232](https://github.com/lentago/solidago/issues/232) — docs: BOOTSTRAP and ADOPTION drift from the code (backend file, state key, required check, role bootstrap order)
- 🟣 2026-11-01 · [solidago#238](https://github.com/lentago/solidago/pull/238) — docs: BOOTSTRAP and ADOPTION drift from the code (backend file, state key, required check, role bootstrap order)
- 🟢 2026-11-01 · [solidago#229](https://github.com/lentago/solidago/issues/229) — iam: drop Terraform state and KMS access from the app deploy role
- 🟣 2026-11-01 · [solidago#234](https://github.com/lentago/solidago/pull/234) — iam: drop Terraform state and KMS access from the app deploy role
- 🟢 2026-11-01 · [solidago#231](https://github.com/lentago/solidago/issues/231) — rds: module header says deletion protection is enabled; the code sets it off
- 🟣 2026-11-01 · [solidago#235](https://github.com/lentago/solidago/pull/235) — rds: module header says deletion protection is enabled; the code sets it off
- 🟢 2026-11-01 · [.github#305](https://github.com/lentago/.github/issues/305) — Tag ruleset for shared-workflows: forbid deleting or moving v* tags
- 🟣 2026-11-01 · [.github#308](https://github.com/lentago/.github/pull/308) — Tag ruleset for shared-workflows: forbid deleting or moving v* tags
- 🟢 2026-11-01 · [site-lentago-dev#111](https://github.com/lentago/site-lentago-dev/issues/111) — Copy: response-time and migration promises match the support page; form labels lead with the task
- 🟣 2026-11-01 · [site-lentago-dev#113](https://github.com/lentago/site-lentago-dev/pull/113) — Copy: response-time and migration promises match the support page; form labels lead with the task
- 🟢 2026-10-31 · [kalmia#252](https://github.com/lentago/kalmia/issues/252) — standing: a tmux-hosted Engineering Director and a 'director' command
- 🟣 2026-10-31 · [kalmia#253](https://github.com/lentago/kalmia/pull/253) — standing: a tmux-hosted Engineering Director and a 'director' command
- 🟢 2026-10-31 · [.github#300](https://github.com/lentago/.github/issues/300) — labels.json: drop the unread ensure field and its validator rule
- 🟣 2026-10-31 · [.github#302](https://github.com/lentago/.github/pull/302) — labels.json: drop the unread ensure field and its validator rule
- 🟢 2026-10-31 · [.github#298](https://github.com/lentago/.github/issues/298) — fleet-apply.sh: retire or fence the legacy settings flags that race terraform/
- 🟣 2026-10-31 · [.github#301](https://github.com/lentago/.github/pull/301) — fleet-apply.sh: remove the legacy settings flags that race terraform/
- 🟣 2026-10-31 · [epigaea#564](https://github.com/lentago/epigaea/pull/564) — feat(tap-dial): kitchen follows another first-floor room's music; one gesture scheme
- 🟢 2026-10-31 · [.github#297](https://github.com/lentago/.github/issues/297) — fleet-apply.sh: check-mode summary still says to re-run with --apply for merge/topic drift
- 🟣 2026-10-31 · [.github#299](https://github.com/lentago/.github/pull/299) — fleet-apply.sh: check-mode summary still says to re-run with --apply for merge/topic drift
- 🟢 2026-10-31 · [.github#295](https://github.com/lentago/.github/issues/295) — fleet-apply.sh: end-of-run hint still points at --require-checks
- 🟣 2026-10-31 · [.github#296](https://github.com/lentago/.github/pull/296) — fleet-apply.sh: end-of-run hint still points at --require-checks
- 🟢 2026-10-31 · [.github#293](https://github.com/lentago/.github/issues/293) — fleet-ops: the read-only check does not run the required-context preflight the README describes
- 🟣 2026-10-31 · [.github#294](https://github.com/lentago/.github/pull/294) — fleet-ops: run the required-context preflight in the read-only check
- 🟢 2026-10-31 · [.github#291](https://github.com/lentago/.github/issues/291) — epigaea: make the Bats check required
- 🟣 2026-10-31 · [.github#292](https://github.com/lentago/.github/pull/292) — epigaea: make the Bats check required
- 🟢 2026-10-31 · [epigaea#560](https://github.com/lentago/epigaea/issues/560) — Instruction cards print taller than the 7 by 5 inch contract
- 🟣 2026-10-31 · [epigaea#563](https://github.com/lentago/epigaea/pull/563) — fix(cards): fit every card in 7 by 5 inches and check it in CI
- 🟣 2026-10-31 · [epigaea#562](https://github.com/lentago/epigaea/pull/562) — fix(cards): draw the Tap Dial's buttons as the hardware marks them
- 🟣 2026-10-31 · [epigaea#561](https://github.com/lentago/epigaea/pull/561) — feat(tap-dial): limit Sonos grouping to the first floor; drop the Basement
- 🟢 2026-10-31 · [kalmia#249](https://github.com/lentago/kalmia/issues/249) — standing: show\|hide <repo> and provision the Director /em skill
- 🟣 2026-10-31 · [kalmia#250](https://github.com/lentago/kalmia/pull/250) — standing: show\|hide <repo> and provision the Director /em skill
- 🟢 2026-10-31 · [kalmia#246](https://github.com/lentago/kalmia/issues/246) — standing: one terminal window per EM, launched on demand
- 🟣 2026-10-31 · [kalmia#248](https://github.com/lentago/kalmia/pull/248) — standing: one terminal window per EM, launched on demand
- 🟢 2026-10-31 · [claytonia#162](https://github.com/lentago/claytonia/issues/162) — cr-update: every scheduled run fails because claude is not on cron's PATH
- 🟣 2026-10-31 · [claytonia#163](https://github.com/lentago/claytonia/pull/163) — cr-update: every scheduled run has failed; call claude by absolute path
- 🟢 2026-10-31 · [epigaea#559](https://github.com/lentago/epigaea/issues/559) — github_custom sensors still query retired pitzilabs/* repos and fail every update
- 🟢 2026-10-31 · [epigaea#556](https://github.com/lentago/epigaea/issues/556) — Sonoff Button 1 is registered in area office; it sits in the kitchen/family room
- 🟣 2026-10-31 · [epigaea#558](https://github.com/lentago/epigaea/pull/558) — feat(cards): instruction card for the meeting button
- 🟣 2026-10-31 · [epigaea#555](https://github.com/lentago/epigaea/pull/555) — feat(cards): instruction card for the downstairs lights button (Sonoff Button 1)
- 🟢 2026-10-31 · [epigaea#550](https://github.com/lentago/epigaea/issues/550) — gitops-sync: non-runtime paths (cards/, tests/, …) trigger a full HA Core restart
- 🟣 2026-10-31 · [epigaea#557](https://github.com/lentago/epigaea/pull/557) — fix(gitops-sync): route cards/ and other non-runtime paths to no reload
- 🟣 2026-10-31 · [epigaea#554](https://github.com/lentago/epigaea/pull/554) — feat(cards): instruction card for the office scene button (Sonoff Button 2)
- 🟣 2026-10-31 · [epigaea#553](https://github.com/lentago/epigaea/pull/553) — feat(cards): instruction card for the office wall switch (ZEN77)
- 🟣 2026-10-31 · [epigaea#549](https://github.com/lentago/epigaea/pull/549) — docs(roadmap): replace § Instruction cards with § Signage
- 🟣 2026-10-31 · [epigaea#547](https://github.com/lentago/epigaea/pull/547) — feat(cards): adopt printable instruction cards; first card is the Kitchen Speaker Dial
- 🟣 2026-10-31 · [epigaea#545](https://github.com/lentago/epigaea/pull/545) — feat(tap-dial): long and multi-presses group the Kitchen Sonos
- 🟣 2026-10-31 · [epigaea#543](https://github.com/lentago/epigaea/pull/543) — feat(dashboard): move clock-weather-card to its v3 config
- 🟣 2026-10-31 · [epigaea#540](https://github.com/lentago/epigaea/pull/540) — fix(tap-dial): CCW turns lower Kitchen Sonos volume again
- 🟣 2026-10-31 · [epigaea#539](https://github.com/lentago/epigaea/pull/539) — feat(tap-dial): buttons 2-4 set Kitchen Sonos volume presets
- 🟢 2026-10-30 · [kalmia#243](https://github.com/lentago/kalmia/issues/243) — standing: `up` exits 1 under set -e when no window lacks a terminal; no way to clear the remembered Director
- 🟣 2026-10-30 · [kalmia#245](https://github.com/lentago/kalmia/pull/245) — shell/standing: `up` exits 0 when no window lacks a terminal; --no-director forgets the Director
- 🟣 2026-10-30 · [epigaea#538](https://github.com/lentago/epigaea/pull/538) — feat(tap-dial): repurpose the Hue Tap Dial as the Kitchen Sonos volume knob
- 🟢 2026-10-30 · [kalmia#242](https://github.com/lentago/kalmia/issues/242) — standing: restart keeps the Director, says it starts fresh; trust polls before warning (#241 review)
- 🟣 2026-10-30 · [kalmia#244](https://github.com/lentago/kalmia/pull/244) — shell/standing: restart keeps the Director, says it starts fresh; trust polls before warning
- 🟢 2026-10-30 · [kalmia#239](https://github.com/lentago/kalmia/issues/239) — standing: minor hardening from the #238 review (trust success check, untagged-pane columns, open without a terminal)
- 🟢 2026-10-30 · [kalmia#240](https://github.com/lentago/kalmia/issues/240) — shell/standing: default model, in-place restart, #239 hardening
- 🟣 2026-10-30 · [kalmia#241](https://github.com/lentago/kalmia/pull/241) — shell/standing: default model, in-place restart, #239 hardening
- 🟢 2026-10-30 · [kalmia#236](https://github.com/lentago/kalmia/issues/236) — standing trust: tighten dialog detection and show what will be accepted
- 🟢 2026-10-30 · [kalmia#237](https://github.com/lentago/kalmia/issues/237) — shell/standing: windows of eight with a terminal each; harden `trust`
- 🟣 2026-10-30 · [kalmia#238](https://github.com/lentago/kalmia/pull/238) — shell/standing: windows of eight with a terminal each; harden `trust` (#237)
- 🟢 2026-10-30 · [kalmia#234](https://github.com/lentago/kalmia/issues/234) — shell/standing: add the folder-trust state and `trust` command
- 🟣 2026-10-30 · [kalmia#235](https://github.com/lentago/kalmia/pull/235) — shell/standing: add the folder-trust state and `trust` command (#234)
- 🟢 2026-10-30 · [kalmia#232](https://github.com/lentago/kalmia/issues/232) — shell: install `standing`, the tiled standing-sessions launcher
- 🟣 2026-10-30 · [kalmia#233](https://github.com/lentago/kalmia/pull/233) — shell: install `standing`, the tiled standing-sessions launcher (#232)
- 🟢 2026-10-30 · [claytonia#24](https://github.com/lentago/claytonia/issues/24) — Branch hygiene across overlapping sessions: clean-desk session-end + prefer fleet dispatch
- 🟢 2026-10-30 · [solidago#21](https://github.com/lentago/solidago/issues/21) — Evaluate migration from ElastiCache node-based to serverless
- 🟢 2026-10-30 · [brasenia#17](https://github.com/lentago/brasenia/issues/17) — Live-ingest pane: concept + ADR, acceptance spec, and VideoScene repoint to `live` with board fallback
- 🟣 2026-10-30 · [.github#288](https://github.com/lentago/.github/pull/288) — Epics report refresh after the epic label landed
- 🟣 2026-10-30 · [.github#287](https://github.com/lentago/.github/pull/287) — Epics report: epics, sub-issue progress, and where the merged work went
- 🟣 2026-10-30 · [kalmia#229](https://github.com/lentago/kalmia/pull/229) — docs: name drosera as the owner of the pve-host alert rules
- 🟣 2026-10-30 · [drosera#298](https://github.com/lentago/drosera/pull/298) — Docs: the rename's state after the LXC 105 move (#169 Phase 7)
- 🟣 2026-10-30 · [claytonia#161](https://github.com/lentago/claytonia/pull/161) — Transcript shipper: check drosera out at /opt/drosera (drosera#169 Phase 5a)
- 🟣 2026-10-30 · [drosera#297](https://github.com/lentago/drosera/pull/297) — Prepare the host checkouts for /opt/drosera (#169 Phases 4a and 6)
- 🟢 2026-10-30 · [solidago#172](https://github.com/lentago/solidago/issues/172) — SNS alert email subscription is recreated on every apply — alerts may be reaching nobody
- 🟣 2026-10-30 · [drosera#296](https://github.com/lentago/drosera/pull/296) — Move Terraform state and the CI role to the drosera name (#169 Phase 2)
- 🟣 2026-10-30 · [solidago#219](https://github.com/lentago/solidago/pull/219) — iam: add the drosera Terraform pipeline role (drosera#169 Phase 1)
- 🟣 2026-10-30 · [claytonia#160](https://github.com/lentago/claytonia/pull/160) — claude-review: point the gitops rule at claytonia-gitops (part of #65)
- 🟣 2026-10-30 · [claytonia#159](https://github.com/lentago/claytonia/pull/159) — terraform: per-worker rebuild triggers, and create workers in the claytonia pool (part of #65)
- 🟢 2026-10-30 · [kalmia#227](https://github.com/lentago/kalmia/issues/227) — forge: build claytonia-runner-v2 under the claytonia names (claytonia#65, step 3)
- 🟣 2026-10-30 · [kalmia#226](https://github.com/lentago/kalmia/pull/226) — forge: build the v2 runner image under the claytonia names, with cluster-checked VMIDs
- 🟣 2026-10-30 · [claytonia#158](https://github.com/lentago/claytonia/pull/158) — Rename the on-host gitops loop to claytonia-gitops (part of #65)
- 🟢 2026-10-30 · [brasenia#127](https://github.com/lentago/brasenia/issues/127) — Review prompt still describes the multi-band, rotation-era pane contract
- 🟣 2026-10-30 · [brasenia#129](https://github.com/lentago/brasenia/pull/129) — Review prompt: describe the one-band contract and the strict order (ADR-0020)
- 🟢 2026-10-30 · [brasenia#121](https://github.com/lentago/brasenia/issues/121) — Compositor: a strict total order, no rotation (ADR-0020: "There should not be ties")
- 🟣 2026-10-30 · [brasenia#128](https://github.com/lentago/brasenia/pull/128) — Compositor: a strict total order, no rotation (ADR-0020: "There should not be ties")
- 🟢 2026-10-30 · [drosera#292](https://github.com/lentago/drosera/issues/292) — Alert when a self-hosted Actions runner goes offline or a job sits queued
- 🟣 2026-10-30 · [drosera#294](https://github.com/lentago/drosera/pull/294) — Alert when a self-hosted Actions job sits queued
- 🟣 2026-10-30 · [betula#146](https://github.com/lentago/betula/pull/146) — feat(github): sample queued jobs in queue_watch repos (drosera#292)
- 🟢 2026-10-30 · [brasenia#118](https://github.com/lentago/brasenia/issues/118) — Band paging after ADR-0020: the contract's multi-band surfaces (blocked until accepted)
- 🟣 2026-10-30 · [brasenia#126](https://github.com/lentago/brasenia/pull/126) — Band paging after ADR-0020: retire the contract's multi-band surfaces
- 🟢 2026-10-30 · [brasenia#122](https://github.com/lentago/brasenia/issues/122) — Retire the `live` rubric class (RTMP ingest is retired, kalmia#224)
- 🟣 2026-10-30 · [brasenia#125](https://github.com/lentago/brasenia/pull/125) — Retire the live rubric class (RTMP ingest is retired, kalmia#224)
- 🟢 2026-10-30 · [kalmia#217](https://github.com/lentago/kalmia/issues/217) — brasenia: stop preferring detail.html once the family brief is on the 1920 canvas (brasenia ADR-0019)
- 🟢 2026-10-30 · [kalmia#223](https://github.com/lentago/kalmia/issues/223) — brasenia-render: stop rotating a multi-band pane's bands on a timer (brasenia ADR-0020, blocked until accepted)
- 🟣 2026-10-30 · [kalmia#225](https://github.com/lentago/kalmia/pull/225) — brasenia-render: a pane is one band, nothing rotates; stop preferring detail.html (brasenia ADR-0020)
- 🟢 2026-10-30 · [brasenia#115](https://github.com/lentago/brasenia/issues/115) — Migrate the family brief to one 1920×1080 band and retire its desk editions (ADR-0019, ADR-0020)
- 🟣 2026-10-30 · [brasenia#124](https://github.com/lentago/brasenia/pull/124) — Migrate the family brief to one 1920×1080 band and retire its desk editions (ADR-0019, ADR-0020)
- 🟢 2026-10-30 · [brasenia#117](https://github.com/lentago/brasenia/issues/117) — ADR-0020: only the rubric and the remote change what the wall shows
- 🟣 2026-10-30 · [brasenia#119](https://github.com/lentago/brasenia/pull/119) — ADR-0020: only the rubric and the remote change what the wall shows
- 🟣 2026-10-30 · [brasenia#120](https://github.com/lentago/brasenia/pull/120) — docs: record the RTMP live-ingest retirement on ADR-0007
- 🟢 2026-10-30 · [kalmia#213](https://github.com/lentago/kalmia/issues/213) — docs/brasenia.md: the RTMP fallback notes describe a board path the stream no longer feeds
- 🟣 2026-10-30 · [kalmia#224](https://github.com/lentago/kalmia/pull/224) — brasenia: retire RTMP live ingest and remove mediamtx
- 🟢 2026-10-30 · [drosera#290](https://github.com/lentago/drosera/issues/290) — tf-drift.sh flags onprem_availability after every update: notification_settings null vs []
- 🟣 2026-10-30 · [drosera#293](https://github.com/lentago/drosera/pull/293) — Stop tf-drift.sh reporting null vs [] as live drift
- 🟢 2026-10-30 · [kalmia#206](https://github.com/lentago/kalmia/issues/206) — pe-publish job guard: fail closed when no Runner.Worker is found; tighten event check
- 🟣 2026-10-30 · [kalmia#222](https://github.com/lentago/kalmia/pull/222) — pe-publish job guard: fail closed when no Runner.Worker is found; tighten event check
- 🟢 2026-10-30 · [brasenia#113](https://github.com/lentago/brasenia/issues/113) — Migrate the producers and the status card to the 1920×1080 pane canvas (ADR-0019)
- 🟣 2026-10-30 · [brasenia#116](https://github.com/lentago/brasenia/pull/116) — Move fleet, focus, grafana, home, pipeline and the status card to the 1920×1080 canvas (ADR-0019)
- 🟢 2026-10-30 · [kalmia#220](https://github.com/lentago/kalmia/issues/220) — brasenia-render: a 1920-canvas pane laid out by an inline script keeps its 1280 layout
- 🟣 2026-10-30 · [kalmia#221](https://github.com/lentago/kalmia/pull/221) — brasenia-render: load a 1920-canvas pane again at its canvas instead of resizing it
- 🟢 2026-10-30 · [drosera#287](https://github.com/lentago/drosera/issues/287) — Viewer service account for brasenia's Grafana panes (render API)
- 🟢 2026-10-30 · [kalmia#202](https://github.com/lentago/kalmia/issues/202) — brasenia-grafana unit on pub: Grafana dashboards as panes
- 🟣 2026-10-30 · [kalmia#219](https://github.com/lentago/kalmia/pull/219) — brasenia-grafana unit on pub: Grafana dashboards as panes
- 🟣 2026-10-30 · [drosera#289](https://github.com/lentago/drosera/pull/289) — Viewer service account for brasenia's Grafana panes (render API)
- 🟢 2026-10-30 · [kalmia#216](https://github.com/lentago/kalmia/issues/216) — brasenia-render: render panes that declare the 1920×1080 canvas at 2× (brasenia ADR-0019)
- 🟣 2026-10-30 · [kalmia#218](https://github.com/lentago/kalmia/pull/218) — brasenia-render: render panes that declare the 1920×1080 canvas at 2× (brasenia ADR-0019)
- 🟢 2026-10-30 · [brasenia#112](https://github.com/lentago/brasenia/issues/112) — ADR-0019: panes on a 1920×1080 canvas at 2×, a 30 px text floor, and "band" for the screenful
- 🟣 2026-10-30 · [brasenia#114](https://github.com/lentago/brasenia/pull/114) — ADR-0019: panes on a 1920×1080 canvas at 2×, a 30 px text floor, and "band" for the screenful
- 🟢 2026-10-30 · [.github#283](https://github.com/lentago/.github/issues/283) — Retire lentago/coderabbit (step 3 of #276)
- 🟣 2026-10-30 · [.github#284](https://github.com/lentago/.github/pull/284) — Retire lentago/coderabbit (ADR-0013 step 3)
- 🟢 2026-10-30 · [kalmia#209](https://github.com/lentago/kalmia/issues/209) — pub: brasenia-home unit has the same trim_blocks hazard as #207 (latent)
- 🟣 2026-10-30 · [kalmia#215](https://github.com/lentago/kalmia/pull/215) — pub: brasenia-home builds its --hide flags inline (trim_blocks hazard)
- 🟢 2026-10-30 · [brasenia#110](https://github.com/lentago/brasenia/issues/110) — Roku: sideload to every screen (the basement TV joins the office)
- 🟣 2026-10-30 · [brasenia#111](https://github.com/lentago/brasenia/pull/111) — Roku: sideload to every screen (the basement TV joins the office)
- 🟣 2026-10-30 · [brasenia#109](https://github.com/lentago/brasenia/pull/109) — claude-review: point the ownership rule at roles/brasenia
- 🟣 2026-10-30 · [shared-workflows#83](https://github.com/lentago/shared-workflows/pull/83) — Rename discipline: kalmia#63 (lunaria runtime) is paid
- 🟣 2026-10-30 · [brasenia#108](https://github.com/lentago/brasenia/pull/108) — Docs: the runtime carries the brasenia name since kalmia#63
- 🟢 2026-10-30 · [kalmia#63](https://github.com/lentago/kalmia/issues/63) — Complete the lunaria → brasenia rename through runtime
- 🟣 2026-10-30 · [kalmia#214](https://github.com/lentago/kalmia/pull/214) — claude-review: name the brasenia playbook in the review prompt
- 🟣 2026-10-29 · [kalmia#211](https://github.com/lentago/kalmia/pull/211) — Rename lunaria to brasenia through runtime: rebuild LXC 118 as brasenia
- 🟣 2026-10-29 · [kalmia#212](https://github.com/lentago/kalmia/pull/212) — terraform: add the LXC 118 rebuild trigger ahead of the brasenia rename
- 🟢 2026-10-29 · [brasenia#106](https://github.com/lentago/brasenia/issues/106) — Roku: show the brasenia logo on the home screen
- 🟣 2026-10-29 · [brasenia#107](https://github.com/lentago/brasenia/pull/107) — Roku: show the brasenia logo on the home screen
- 🟢 2026-10-29 · [.github#280](https://github.com/lentago/.github/issues/280) — brand: generate a Roku home-screen poster for repos that ship a Roku channel
- 🟣 2026-10-29 · [.github#281](https://github.com/lentago/.github/pull/281) — brand: generate a Roku home-screen poster for repos that ship a Roku channel
- 🟣 2026-10-29 · [claytonia#156](https://github.com/lentago/claytonia/pull/156) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 🟣 2026-10-29 · [uvularia#111](https://github.com/lentago/uvularia/pull/111) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 🟣 2026-10-29 · [solidago#218](https://github.com/lentago/solidago/pull/218) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 🟣 2026-10-29 · [site-pondviewlane-com#96](https://github.com/lentago/site-pondviewlane-com/pull/96) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 🟣 2026-10-29 · [site-lentago-dev#110](https://github.com/lentago/site-lentago-dev/pull/110) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 🟣 2026-10-29 · [site-icecreamtofightwith-com#211](https://github.com/lentago/site-icecreamtofightwith-com/pull/211) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 🟣 2026-10-29 · [shared-workflows#82](https://github.com/lentago/shared-workflows/pull/82) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 🟣 2026-10-29 · [osmunda#19](https://github.com/lentago/osmunda/pull/19) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 🟣 2026-10-29 · [mitchella#29](https://github.com/lentago/mitchella/pull/29) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 🟣 2026-10-29 · [kalmia#210](https://github.com/lentago/kalmia/pull/210) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 🟣 2026-10-29 · [.github#279](https://github.com/lentago/.github/pull/279) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 🟣 2026-10-29 · [epigaea#537](https://github.com/lentago/epigaea/pull/537) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 🟣 2026-10-29 · [drosera#288](https://github.com/lentago/drosera/pull/288) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 🟣 2026-10-29 · [brasenia#105](https://github.com/lentago/brasenia/pull/105) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 🟣 2026-10-29 · [betula#145](https://github.com/lentago/betula/pull/145) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 🟣 2026-10-29 · [asclepias#25](https://github.com/lentago/asclepias/pull/25) — ci: add the advisory Claude PR reviewer (ADR-0013)
- 🟢 2026-10-29 · [brasenia#98](https://github.com/lentago/brasenia/issues/98) — Grafana panes, rendered on pub with a viewer service account
- 🟣 2026-10-29 · [brasenia#103](https://github.com/lentago/brasenia/pull/103) — Grafana panes: dashboards rendered on pub with a Viewer service account (#98)
- 🟢 2026-10-29 · [kalmia#207](https://github.com/lentago/kalmia/issues/207) — pub: brasenia-compositor fails to start, Restart= line joined onto ExecStart
- 🟣 2026-10-29 · [kalmia#208](https://github.com/lentago/kalmia/pull/208) — pub: keep the compositor unit's Restart= line off ExecStart
- 🟣 2026-10-29 · [repo-template#30](https://github.com/lentago/repo-template/pull/30) — ci: pin the PR reviewer to shared-workflows v1.5.0 (posts the review)
- 🟢 2026-10-29 · [shared-workflows#80](https://github.com/lentago/shared-workflows/issues/80) — claude-review never posts the review to the PR
- 🟣 2026-10-29 · [shared-workflows#81](https://github.com/lentago/shared-workflows/pull/81) — claude-review: post the review as a PR comment; soft-fail on any result-less run (v1.5.0)
- 🟣 2026-10-29 · [kalmia#205](https://github.com/lentago/kalmia/pull/205) — lunaria: brasenia-render, one renderer for the stream and the peek, rendering every pane ahead
- 🟣 2026-10-29 · [repo-template#28](https://github.com/lentago/repo-template/pull/28) — ci: add the advisory Claude PR reviewer (ADR-0013 reference copy)
- 🟢 2026-10-29 · [shared-workflows#79](https://github.com/lentago/shared-workflows/issues/79) — Fleet PR-workflow: write down the review-before-arming rule
- 🟣 2026-10-29 · [shared-workflows#78](https://github.com/lentago/shared-workflows/pull/78) — Fleet PR-workflow: don't arm until the AI review is in and triaged
- 🟢 2026-10-29 · [.github#278](https://github.com/lentago/.github/issues/278) — ADR-0013 and the review labels (step 1 of #276)
- 🟣 2026-10-29 · [.github#277](https://github.com/lentago/.github/pull/277) — ADR-0013: Haiku reviews every PR in the operating repos; CodeRabbit retires
- 🟢 2026-10-29 · [brasenia#97](https://github.com/lentago/brasenia/issues/97) — Link panes: put any web page in a slot (pane claim --url, standing slots in the configurator)
- 🟣 2026-10-29 · [brasenia#104](https://github.com/lentago/brasenia/pull/104) — Standing slots: keep any web page on the wall from the configurator
- 🟣 2026-10-29 · [brasenia#102](https://github.com/lentago/brasenia/pull/102) — pane claim --url: claim a web page as a link pane
- 🟣 2026-10-29 · [kalmia#203](https://github.com/lentago/kalmia/pull/203) — pub: run brasenia's links producer (standing slots as link panes)
- 🟢 2026-10-29 · [kalmia#194](https://github.com/lentago/kalmia/issues/194) — lunaria: one renderer for the stream and the peek, rendering every pane ahead
- 🟣 2026-10-29 · [kalmia#201](https://github.com/lentago/kalmia/pull/201) — lunaria: Chromium's sandbox (nesting on LXC 118), an allowed-sites gate, and the emoji font
- 🟢 2026-10-29 · [kalmia#199](https://github.com/lentago/kalmia/issues/199) — CLAUDE.md says main doesn't require up-to-date branches; the ruleset does
- 🟣 2026-10-29 · [kalmia#200](https://github.com/lentago/kalmia/pull/200) — CLAUDE.md: main requires up-to-date branches; tf-lint is a required check
- 🟢 2026-10-29 · [brasenia#96](https://github.com/lentago/brasenia/issues/96) — Contracts: a content revision per pane, and link panes (a pane whose source is a web page)
- 🟣 2026-10-29 · [brasenia#101](https://github.com/lentago/brasenia/pull/101) — Contracts: a content revision per pane, and link panes (a pane whose source is a web page)
- 🟢 2026-10-29 · [kalmia#195](https://github.com/lentago/kalmia/issues/195) — pe-publish: runner-side guard — refuse every job but professional-endeavors' Publish on main
- 🟣 2026-10-29 · [kalmia#196](https://github.com/lentago/kalmia/pull/196) — pe-publish: runner-side guard — refuse every job but professional-endeavors' Publish on main
- 🟢 2026-10-29 · [kalmia#193](https://github.com/lentago/kalmia/issues/193) — lunaria/pub: shorter Roku lag and fresher frames (playlist window, 60 s re-render, 1 s polls)
- 🟣 2026-10-29 · [kalmia#197](https://github.com/lentago/kalmia/pull/197) — lunaria/pub: shorter Roku lag and fresher frames (3-segment playlist, 60 s re-render, 1 s polls)
- 🟢 2026-10-29 · [brasenia#95](https://github.com/lentago/brasenia/issues/95) — Roku: the office Roku plays about 20 s behind the live stream
- 🟣 2026-10-29 · [brasenia#100](https://github.com/lentago/brasenia/pull/100) — Roku: rejoin the stream when it drifts behind live (about 20 s down to 6 s)
- 🟣 2026-10-29 · [brasenia#94](https://github.com/lentago/brasenia/pull/94) — CLAUDE.md: drop the derivable layout table
- 🟢 2026-10-29 · [betula#143](https://github.com/lentago/betula/issues/143) — CI: github-client-tests test (3.9) fails on ubuntu-latest (now 26.04)
- 🟣 2026-10-29 · [betula#144](https://github.com/lentago/betula/pull/144) — ci(github-client): raise Python floor from 3.9 to 3.10
- 🟣 2026-10-29 · [shared-workflows#77](https://github.com/lentago/shared-workflows/pull/77) — docs: enforced-surfaces row — personal-repo wiki publish on merge (LXC 123)
- 🟣 2026-10-29 · [uvularia-site-template#11](https://github.com/lentago/uvularia-site-template/pull/11) — Sync from lentago/uvularia@3dafa7a
- 🟣 2026-10-29 · [site-lentago-dev#108](https://github.com/lentago/site-lentago-dev/pull/108) — chore(deps): Bump the npm-routine group across 1 directory with 2 updates
- 🟣 2026-10-29 · [site-pondviewlane-com#95](https://github.com/lentago/site-pondviewlane-com/pull/95) — Bump the astro-stack group with 2 updates
- 🟣 2026-10-29 · [site-lentago-dev#109](https://github.com/lentago/site-lentago-dev/pull/109) — chore(deps): Bump nginx from `f9ea18b` to `4c41e2d`
- 🟣 2026-10-29 · [site-pondviewlane-com#94](https://github.com/lentago/site-pondviewlane-com/pull/94) — Bump the actions-routine group with 3 updates
- 🟣 2026-10-29 · [site-lentago-dev#107](https://github.com/lentago/site-lentago-dev/pull/107) — chore(deps): Bump the astro-stack group with 2 updates
- 🟣 2026-10-29 · [site-icecreamtofightwith-com#210](https://github.com/lentago/site-icecreamtofightwith-com/pull/210) — Bump the actions-routine group across 1 directory with 5 updates
- 🟣 2026-10-29 · [claytonia#149](https://github.com/lentago/claytonia/pull/149) — chore(deps): bump the actions-routine group across 1 directory with 4 updates
- 🟣 2026-10-29 · [uvularia-site-template#12](https://github.com/lentago/uvularia-site-template/pull/12) — Sync from lentago/uvularia@ff7b583
- 🟣 2026-10-29 · [.github#274](https://github.com/lentago/.github/pull/274) — build(deps): bump the actions-routine group across 1 directory with 7 updates
- 🟣 2026-10-29 · [site-icecreamtofightwith-com#209](https://github.com/lentago/site-icecreamtofightwith-com/pull/209) — Bump nginx from `f9ea18b` to `4c41e2d`
- 🟣 2026-10-29 · [uvularia#110](https://github.com/lentago/uvularia/pull/110) — build(deps): bump the actions-routine group across 1 directory with 5 updates
- 🟣 2026-10-29 · [kalmia#162](https://github.com/lentago/kalmia/pull/162) — build(deps): bump the actions-routine group across 1 directory with 5 updates
- 🟣 2026-10-29 · [uvularia#109](https://github.com/lentago/uvularia/pull/109) — build(deps-dev): bump the site-routine group across 1 directory with 2 updates
- 🟣 2026-10-29 · [solidago#217](https://github.com/lentago/solidago/pull/217) — build(deps): bump the actions-routine group with 4 updates
- 🟣 2026-10-29 · [site-pondviewlane-com#93](https://github.com/lentago/site-pondviewlane-com/pull/93) — Bump nginx from `f9ea18b` to `332d0be`
- 🟣 2026-10-29 · [site-lentago-dev#106](https://github.com/lentago/site-lentago-dev/pull/106) — chore(deps): Bump the actions-routine group with 4 updates
- 🟣 2026-10-29 · [site-icecreamtofightwith-com#207](https://github.com/lentago/site-icecreamtofightwith-com/pull/207) — Bump the astro-stack group with 2 updates
- 🟣 2026-10-29 · [shared-workflows#75](https://github.com/lentago/shared-workflows/pull/75) — chore(deps): Bump the actions-routine group across 1 directory with 5 updates
- 🟣 2026-10-29 · [repo-template#27](https://github.com/lentago/repo-template/pull/27) — build(deps): bump the actions-routine group with 2 updates
- 🟣 2026-10-29 · [osmunda#18](https://github.com/lentago/osmunda/pull/18) — build(deps): Bump the actions-routine group with 3 updates
- 🟣 2026-10-29 · [epigaea#536](https://github.com/lentago/epigaea/pull/536) — build(deps): bump the actions-routine group across 1 directory with 4 updates
- 🟣 2026-10-29 · [drosera#286](https://github.com/lentago/drosera/pull/286) — chore(deps): Bump the actions-routine group across 1 directory with 5 updates
- 🟣 2026-10-29 · [coderabbit#9](https://github.com/lentago/coderabbit/pull/9) — build(deps): bump the actions-routine group across 1 directory with 2 updates
- 🟣 2026-10-29 · [betula#142](https://github.com/lentago/betula/pull/142) — chore(deps): bump the actions-routine group across 1 directory with 5 updates
- 🟣 2026-10-29 · [asclepias#24](https://github.com/lentago/asclepias/pull/24) — build(deps): bump the actions-routine group with 2 updates
- 🟣 2026-10-29 · [kalmia#192](https://github.com/lentago/kalmia/pull/192) — pe-publish follow-ups: declare tzdata, document the Firewalla quarantine step
- 🟢 2026-10-29 · [kalmia#190](https://github.com/lentago/kalmia/issues/190) — Pipeline-attached NAS bind mounts (restricted SSH mount hook) + LXC 123 pe-publish runner
- 🟣 2026-10-29 · [kalmia#191](https://github.com/lentago/kalmia/pull/191) — Pipeline-attached NAS bind mounts (restricted SSH mount hook) + LXC 123 pe-publish runner
- 🟢 2026-10-29 · [kalmia#188](https://github.com/lentago/kalmia/issues/188) — docs/pub.md: the Family Brief Doc is shared with Rachel as a commenter, not a reader
- 🟣 2026-10-29 · [kalmia#189](https://github.com/lentago/kalmia/pull/189) — docs/pub.md: the Family Brief Doc is shared with Rachel as a commenter, not a reader
- 🟢 2026-10-29 · [brasenia#92](https://github.com/lentago/brasenia/issues/92) — Family Brief Doc: paragraphs run together after the Google Docs import
- 🟣 2026-10-29 · [brasenia#93](https://github.com/lentago/brasenia/pull/93) — Family Brief Doc: give each paragraph explicit spacing
- 🟢 2026-10-29 · [kalmia#186](https://github.com/lentago/kalmia/issues/186) — pub: publish the Family Brief as a Google Doc (updated in place, shared with the household)
- 🟣 2026-10-29 · [kalmia#187](https://github.com/lentago/kalmia/pull/187) — pub: publish the Family Brief as a Google Doc (updated in place, shared with the household)
- 🟢 2026-10-29 · [brasenia#90](https://github.com/lentago/brasenia/issues/90) — Family Brief as a Google Doc: a document rendition for sharing beyond the LAN
- 🟣 2026-10-29 · [brasenia#91](https://github.com/lentago/brasenia/pull/91) — Family Brief as a Google Doc: a document rendition for sharing beyond the LAN
- 🟢 2026-10-29 · [kalmia#184](https://github.com/lentago/kalmia/issues/184) — pub: hide the kids' bedroom door sensors from the brasenia home pane
- 🟣 2026-10-29 · [kalmia#185](https://github.com/lentago/kalmia/pull/185) — pub: hide the kids' bedroom door sensors from the brasenia home pane
- 🟢 2026-10-29 · [kalmia#182](https://github.com/lentago/kalmia/issues/182) — docs/pub.md: the HA token seeding command should print a prompt
- 🟣 2026-10-29 · [kalmia#183](https://github.com/lentago/kalmia/pull/183) — docs/pub.md: the HA token seeding command should print a prompt
- 🟢 2026-10-29 · [brasenia#88](https://github.com/lentago/brasenia/issues/88) — Home producer: connect to Home Assistant over IPv4 (local-only users get 401 over global IPv6)
- 🟣 2026-10-29 · [brasenia#89](https://github.com/lentago/brasenia/pull/89) — Home producer: connect to Home Assistant over IPv4 (local-only users get 401 over global IPv6)
- 🟢 2026-10-29 · [kalmia#180](https://github.com/lentago/kalmia/issues/180) — pub: run brasenia's home and fleet producers (HA token credential, read-only claude-jobs mount)
- 🟣 2026-10-29 · [kalmia#181](https://github.com/lentago/kalmia/pull/181) — pub: run brasenia's home and fleet producers (HA token credential, read-only claude-jobs mount)
- 🟢 2026-10-29 · [brasenia#86](https://github.com/lentago/brasenia/issues/86) — More resting panes: Home, Weather and Fleet
- 🟣 2026-10-29 · [brasenia#87](https://github.com/lentago/brasenia/pull/87) — More resting panes: Home, Weather and Fleet
- 🟢 2026-10-29 · [brasenia#83](https://github.com/lentago/brasenia/issues/83) — Resting panes: a default the household picks with the remote (Left/Right), and a Family "This week" pane
- 🟣 2026-10-29 · [brasenia#85](https://github.com/lentago/brasenia/pull/85) — Roku remote: Left/Right sets the household's default resting pane
- 🟣 2026-10-29 · [brasenia#84](https://github.com/lentago/brasenia/pull/84) — Resting panes: a household default (default.pane) and a Family "This week" pane
- 🟢 2026-10-28 · [brasenia#80](https://github.com/lentago/brasenia/issues/80) — Roku remote: step through the panes with Up/Down (instant peek over the live view)
- 🟣 2026-10-28 · [brasenia#82](https://github.com/lentago/brasenia/pull/82) — Roku remote: step through the panes with Up/Down (instant peek over the live view)
- 🟣 2026-10-28 · [kalmia#179](https://github.com/lentago/kalmia/pull/179) — lunaria: pre-render the viewport line-up for the Roku remote's peek (lunaria-peek, /peek/)
- 🟣 2026-10-28 · [brasenia#81](https://github.com/lentago/brasenia/pull/81) — Compositor: publish viewport/lineup.json, what a client may step through (for the Roku remote's peek)
- 🟢 2026-10-28 · [brasenia#78](https://github.com/lentago/brasenia/issues/78) — Focus producer: no pane for a quiet repo; household time on panes; drop the doubled "main:" label
- 🟣 2026-10-28 · [brasenia#79](https://github.com/lentago/brasenia/pull/79) — Focus producer: no pane for a quiet repo; household time on panes; drop the doubled "main:" label
- 🟣 2026-10-28 · [kalmia#178](https://github.com/lentago/kalmia/pull/178) — lunaria: briefing rotation is the Family Brief from brasenia's briefing slot; drop the praxis graph
- 🟢 2026-10-28 · [brasenia#76](https://github.com/lentago/brasenia/issues/76) — Briefing fallback: the Family Brief, from a briefing slot the producer keeps, instead of the old morning brief
- 🟣 2026-10-28 · [brasenia#77](https://github.com/lentago/brasenia/pull/77) — Briefing fallback: the Family Brief, from a briefing slot the producer keeps, instead of the old morning brief
- 🟣 2026-10-28 · [brasenia#75](https://github.com/lentago/brasenia/pull/75) — ADR-0010: note that cast-app/ was deleted (#73)
- 🟢 2026-10-28 · [brasenia#73](https://github.com/lentago/brasenia/issues/73) — Delete cast-app/: the Cast receiver is no longer published
- 🟣 2026-10-28 · [brasenia#74](https://github.com/lentago/brasenia/pull/74) — Delete cast-app/: the Cast receiver is no longer published
- 🟢 2026-10-28 · [kalmia#174](https://github.com/lentago/kalmia/issues/174) — pub: stop publishing the retired Cast receiver; keep the daily brasenia pull under an honest name
- 🟣 2026-10-28 · [kalmia#177](https://github.com/lentago/kalmia/pull/177) — pub: split the daily brasenia pull into brasenia-update; retire the Cast receiver publishing
- 🟢 2026-10-28 · [brasenia#58](https://github.com/lentago/brasenia/issues/58) — Family brief rows: "where" is appended after a trailing period ("assembly., Harborlight")
- 🟣 2026-10-28 · [brasenia#72](https://github.com/lentago/brasenia/pull/72) — Family brief rows: drop a trailing full stop before the place ("assembly., Harborlight")
- 🟢 2026-10-28 · [kalmia#99](https://github.com/lentago/kalmia/issues/99) — Cast client runtime for brasenia: watchdog sender, receiver hosting, then HLS-stack turn-down (brasenia ADR-0006)
- 🟢 2026-10-28 · [brasenia#12](https://github.com/lentago/brasenia/issues/12) — Second functional path: Cast-native rendering, then deprecate and turn down the Roku/HLS chain
- 🟢 2026-10-28 · [brasenia#70](https://github.com/lentago/brasenia/issues/70) — Rubric configurator: household overrides on the share, edited beside the rubric board
- 🟣 2026-10-28 · [brasenia#71](https://github.com/lentago/brasenia/pull/71) — Rubric configurator: household overrides on the share, edited beside the rubric board
- 🟣 2026-10-28 · [kalmia#176](https://github.com/lentago/kalmia/pull/176) — pub-signals: allow the brasenia rubric configurator (rubric namespace, set action)
- 🟢 2026-10-28 · [brasenia#68](https://github.com/lentago/brasenia/issues/68) — Raise the Python floor from 3.9 to 3.11 and drop the ubuntu-24.04 pin
- 🟣 2026-10-28 · [brasenia#69](https://github.com/lentago/brasenia/pull/69) — Raise the Python floor from 3.9 to 3.11 and drop the ubuntu-24.04 pin
- 🟣 2026-10-28 · [brasenia#50](https://github.com/lentago/brasenia/pull/50) — build(deps): bump the actions-routine group across 1 directory with 4 updates
- 🟢 2026-10-28 · [brasenia#49](https://github.com/lentago/brasenia/issues/49) — CI: Python 3.9 jobs fail on ubuntu-latest (now 26.04)
- 🟣 2026-10-28 · [brasenia#67](https://github.com/lentago/brasenia/pull/67) — ci: pin the Python test workflows to ubuntu-24.04 so the 3.9 leg can start
- 🟢 2026-10-28 · [brasenia#65](https://github.com/lentago/brasenia/issues/65) — Compositor pages show pub's UTC clock as if it were local time
- 🟣 2026-10-28 · [brasenia#66](https://github.com/lentago/brasenia/pull/66) — Compositor: show times in the household's zone (--tz), not pub's UTC
- 🟢 2026-10-28 · [brasenia#63](https://github.com/lentago/brasenia/issues/63) — Viewport rubric board: a web page showing what the compositor picked and why
- 🟣 2026-10-28 · [brasenia#64](https://github.com/lentago/brasenia/pull/64) — Viewport rubric board: a web page showing what the compositor picked and why
- 🟢 2026-10-28 · [brasenia#61](https://github.com/lentago/brasenia/issues/61) — Retire the Cast client; Roku is the client platform (ADR-0010)
- 🟣 2026-10-28 · [brasenia#62](https://github.com/lentago/brasenia/pull/62) — Retire the Cast client; Roku is the client platform (ADR-0010)
- 🟣 2026-10-28 · [kalmia#175](https://github.com/lentago/kalmia/pull/175) — lunaria: retire the Cast receiver watchdog (the role now ensures it is absent)
- 🟢 2026-10-28 · [brasenia#59](https://github.com/lentago/brasenia/issues/59) — The office Roku becomes the viewport: follow the compositor pointer, preferring a pane's desk edition
- 🟣 2026-10-28 · [brasenia#60](https://github.com/lentago/brasenia/pull/60) — The office Roku becomes the viewport: follow the pointer, preferring a pane's desk edition
- 🟣 2026-10-28 · [kalmia#173](https://github.com/lentago/kalmia/pull/173) — lunaria: the office Roku follows the viewport pointer, preferring a pane's desk rendition
- 🟣 2026-10-28 · [kalmia#172](https://github.com/lentago/kalmia/pull/172) — lunaria: pin the office Roku to the Family Brief's desk edition (detail.html)
- 🟢 2026-10-28 · [brasenia#56](https://github.com/lentago/brasenia/issues/56) — Family brief: a desk-distance 4K edition (detail.html) with all decisions and to-dos
- 🟣 2026-10-28 · [brasenia#57](https://github.com/lentago/brasenia/pull/57) — Family brief: a desk-distance 4K edition (detail.html) with all decisions and to-dos
- 🟣 2026-10-28 · [kalmia#171](https://github.com/lentago/kalmia/pull/171) — docs(lunaria): the office Roku's dev channel is now titled "brasenia"
- 🟢 2026-10-28 · [brasenia#54](https://github.com/lentago/brasenia/issues/54) — Rename the Roku dev channel from "HLS Pipeline Test" to "brasenia"
- 🟣 2026-10-28 · [brasenia#55](https://github.com/lentago/brasenia/pull/55) — Rename the Roku dev channel from "HLS Pipeline Test" to "brasenia"
- 🟢 2026-10-28 · [kalmia#169](https://github.com/lentago/kalmia/issues/169) — lunaria-stream: the encoder locks its output size to whichever frame.png it starts on
- 🟣 2026-10-28 · [kalmia#170](https://github.com/lentago/kalmia/pull/170) — lunaria-stream: scale frames to the configured size so a stale frame.png cannot lock the stream's resolution
- 🟢 2026-10-28 · [brasenia#52](https://github.com/lentago/brasenia/issues/52) — Office Roku: 4K family-brief client (HEVC over HLS); retire the play-room Roku client
- 🟣 2026-10-28 · [brasenia#53](https://github.com/lentago/brasenia/pull/53) — Office Roku: 4K family-brief client (HEVC over HLS); retire the play-room Roku client
- 🟢 2026-10-28 · [kalmia#167](https://github.com/lentago/kalmia/issues/167) — lunaria: 4K HEVC family-brief stream for the office Roku; retire the 720p board stream
- 🟣 2026-10-28 · [kalmia#168](https://github.com/lentago/kalmia/pull/168) — lunaria: 4K HEVC family-brief stream for the office Roku; retire the 720p board stream
- 🟢 2026-10-28 · [claytonia#154](https://github.com/lentago/claytonia/issues/154) — Let a project keep its job narration off Grafana Cloud
- 🟣 2026-10-28 · [claytonia#155](https://github.com/lentago/claytonia/pull/155) — Let a project keep its job narration off Grafana Cloud
- 🟢 2026-10-28 · [claytonia#152](https://github.com/lentago/claytonia/issues/152) — Record that the runner App is public, and why
- 🟣 2026-10-28 · [claytonia#153](https://github.com/lentago/claytonia/pull/153) — Record that the runner App is public, and why
- 🟢 2026-10-28 · [claytonia#150](https://github.com/lentago/claytonia/issues/150) — Run scheduled routines on the fleet: schedules as data, a policy-gated merge step, per-repo App tokens, read-only Google access
- 🟣 2026-10-28 · [claytonia#151](https://github.com/lentago/claytonia/pull/151) — Run scheduled routines on the fleet: schedules as data, a policy-gated merge step, per-repo App tokens, read-only Google access
- 🟢 2026-10-28 · [kalmia#165](https://github.com/lentago/kalmia/issues/165) — pub: a signal sink for checkbox actions on pages served from pub.lan
- 🟣 2026-10-28 · [kalmia#166](https://github.com/lentago/kalmia/pull/166) — pub: a signal sink for checkbox actions on pages served from pub.lan
- 🟣 2026-10-26 · [.github#275](https://github.com/lentago/.github/pull/275) — Weekly fleet reports refresh — 2026-10-26
- 🟢 2026-10-26 · [kalmia#163](https://github.com/lentago/kalmia/issues/163) — pub: publish the Family Brief JSON and run brasenia's family-brief producer
- 🟣 2026-10-26 · [kalmia#164](https://github.com/lentago/kalmia/pull/164) — pub: publish the Family Brief JSON and run brasenia's family-brief producer
- 🟣 2026-10-26 · [brasenia#48](https://github.com/lentago/brasenia/pull/48) — Family brief producer: today and tomorrow on the wall
- 🟣 2026-10-25 · [drosera#285](https://github.com/lentago/drosera/pull/285) — Pve storage alerts
- 🟣 2026-10-25 · [kalmia#161](https://github.com/lentago/kalmia/pull/161) — PVE storage hardening; xubuntu-ws as always-on primary
- 🟣 2026-10-19 · [.github#273](https://github.com/lentago/.github/pull/273) — Weekly fleet reports refresh — 2026-10-19
- 🟢 2026-10-14 · [.github#269](https://github.com/lentago/.github/issues/269) — Scrub "homelab" and kin: the on-prem half of the estate is "on-prem"
- 🟣 2026-10-14 · [.github#270](https://github.com/lentago/.github/pull/270) — voice: the on-prem half of the estate is "on-prem"; retire "homelab" and "lab"
- 🟣 2026-10-14 · [epigaea#534](https://github.com/lentago/epigaea/pull/534) — epigaea: retire "homelab"/"lab" wording for on-prem
- 🟣 2026-10-14 · [solidago#216](https://github.com/lentago/solidago/pull/216) — solidago: retire "homelab"/"lab" wording for on-prem
- 🟣 2026-10-14 · [lupinus#32](https://github.com/lentago/lupinus/pull/32) — Retire "homelab"/"the lab" wording for on-prem
- 🟣 2026-10-14 · [brasenia#46](https://github.com/lentago/brasenia/pull/46) — Retire "homelab" and "household" wording for on-prem
- 🟣 2026-10-14 · [betula#140](https://github.com/lentago/betula/pull/140) — Retire "homelab"/"lab" wording for on-prem
- 🟣 2026-10-14 · [drosera#283](https://github.com/lentago/drosera/pull/283) — Retire "homelab"/"lab" wording for on-prem
- 🟣 2026-10-14 · [osmunda#17](https://github.com/lentago/osmunda/pull/17) — osmunda: retire "homelab"/"lab" wording for on-prem
- 🟣 2026-10-14 · [claytonia#148](https://github.com/lentago/claytonia/pull/148) — Retire "homelab"/"lab" wording for on-prem
- 🟣 2026-10-14 · [shared-workflows#76](https://github.com/lentago/shared-workflows/pull/76) — Replace the household-presence PR-body example
- 🟣 2026-10-14 · [asclepias#23](https://github.com/lentago/asclepias/pull/23) — Estate atlas: the on-prem half is "on-prem"
- 🟣 2026-10-14 · [kalmia#159](https://github.com/lentago/kalmia/pull/159) — Retire "homelab"/"lab" and "household" wording for on-prem
- 🟣 2026-10-14 · [mitchella#28](https://github.com/lentago/mitchella/pull/28) — Retire "the lab estate" wording
- 🟣 2026-10-14 · [claytonia#147](https://github.com/lentago/claytonia/pull/147) — provision: NodeSource source and pin written unconditionally
- 🟢 2026-10-14 · [kalmia#156](https://github.com/lentago/kalmia/issues/156) — Runner image: install Node 22 LTS in forge/runner/substrate.sh
- 🟣 2026-10-14 · [kalmia#157](https://github.com/lentago/kalmia/pull/157) — Runner image: install Node 22 LTS from NodeSource
- 🟢 2026-10-13 · [claytonia#140](https://github.com/lentago/claytonia/issues/140) — Runner default Node 18.20 is below Astro's minimum; workers switch by hand
- 🟣 2026-10-13 · [claytonia#146](https://github.com/lentago/claytonia/pull/146) — provision: pin worker Node to 22 LTS (Astro 7 minimum)
- 🟣 2026-10-13 · [brasenia#45](https://github.com/lentago/brasenia/pull/45) — docs(concept): document internet-outage degraded mode
- 🟢 2026-10-13 · [shared-workflows#72](https://github.com/lentago/shared-workflows/issues/72) — claude-responder: a 40-turn cap fails runs that finished successfully
- 🟣 2026-10-13 · [shared-workflows#74](https://github.com/lentago/shared-workflows/pull/74) — feat(claude-responder): raise the max_turns default to 80
- 🟢 2026-10-13 · [claytonia#143](https://github.com/lentago/claytonia/issues/143) — cr-submit -w: let unattended callers opt in to waiting
- 🟣 2026-10-13 · [claytonia#145](https://github.com/lentago/claytonia/pull/145) — cr-submit: -W/--wait-unattended opt-in to wait without a tty
- 🟢 2026-10-13 · [monarda#32](https://github.com/lentago/monarda/issues/32) — Deploy to GitHub Pages fails on every push: no Pages site on this repo
- 🟣 2026-10-13 · [monarda#33](https://github.com/lentago/monarda/pull/33) — deploy-pages: skip the deploy until Pages is enabled
- 🟢 2026-10-13 · [asclepias#21](https://github.com/lentago/asclepias/issues/21) — Pattern catalog: tiered automation trust needs an org example or a reword
- 🟣 2026-10-13 · [asclepias#22](https://github.com/lentago/asclepias/pull/22) — manual: reword tiered automation trust to grouped Dependabot
- 🟢 2026-10-13 · [drosera#279](https://github.com/lentago/drosera/issues/279) — Runner Fleet dashboard: attribute jobs by submitter
- 🟣 2026-10-13 · [drosera#281](https://github.com/lentago/drosera/pull/281) — feat(dashboards): attribute Runner Fleet jobs by submitter
- 🟢 2026-10-13 · [.github#266](https://github.com/lentago/.github/issues/266) — Decide: require PR branches to be up to date before merge (ruleset strict checks)
- 🟣 2026-10-13 · [.github#267](https://github.com/lentago/.github/pull/267) — rulesets: require up-to-date branches on the CI-enforced repos
- 🟢 2026-10-13 · [.github#176](https://github.com/lentago/.github/issues/176) — Codify org settings in Terraform — default_repository_permission is live-only
- 🟣 2026-10-13 · [.github#268](https://github.com/lentago/.github/pull/268) — docs: org settings stay human-applied, outside terraform
- 🟣 2026-10-13 · [uvularia-site-template#10](https://github.com/lentago/uvularia-site-template/pull/10) — Sync from lentago/uvularia@5e49315
- 🟢 2026-10-13 · [uvularia#104](https://github.com/lentago/uvularia/issues/104) — site template: scheduled deploy-pages fails in the template repo itself
- 🟣 2026-10-13 · [uvularia#106](https://github.com/lentago/uvularia/pull/106) — site template: deploy-pages skips when Pages isn't enabled
- 🟢 2026-10-13 · [claytonia#139](https://github.com/lentago/claytonia/issues/139) — Runners have no browser: Chrome for render.sh, Chromium libs for pa11y
- 🟣 2026-10-13 · [epigaea#532](https://github.com/lentago/epigaea/pull/532) — build(deps): bump the actions-routine group with 3 updates
- 🟣 2026-10-13 · [site-lentago-dev#105](https://github.com/lentago/site-lentago-dev/pull/105) — chore(deps-dev): Bump pa11y-ci from 4.1.1 to 5.0.0 in the npm-major group
- 🟣 2026-10-13 · [site-lentago-dev#104](https://github.com/lentago/site-lentago-dev/pull/104) — chore(deps): Bump the astro-stack group with 2 updates
- 🟣 2026-10-13 · [uvularia-site-template#9](https://github.com/lentago/uvularia-site-template/pull/9) — Sync from lentago/uvularia@73cf4ce
- 🟣 2026-10-13 · [site-lentago-dev#103](https://github.com/lentago/site-lentago-dev/pull/103) — chore(deps): Bump the actions-routine group with 4 updates
- 🟣 2026-10-13 · [site-lentago-dev#102](https://github.com/lentago/site-lentago-dev/pull/102) — chore(deps): Bump nginx from `abe4772` to `f9ea18b`
- 🟣 2026-10-13 · [uvularia#105](https://github.com/lentago/uvularia/pull/105) — templates/site: adopt TypeScript 6 with explicit types
- 🟣 2026-10-13 · [site-icecreamtofightwith-com#205](https://github.com/lentago/site-icecreamtofightwith-com/pull/205) — Bump the actions-routine group across 1 directory with 5 updates
- 🟣 2026-10-13 · [solidago#214](https://github.com/lentago/solidago/pull/214) — build(deps): bump the actions-routine group across 1 directory with 4 updates
- 🟣 2026-10-13 · [osmunda#15](https://github.com/lentago/osmunda/pull/15) — build(deps): Bump the actions-routine group across 1 directory with 3 updates
- 🟣 2026-10-13 · [drosera#280](https://github.com/lentago/drosera/pull/280) — chore(deps): Bump the actions-routine group across 1 directory with 4 updates
- 🟣 2026-10-13 · [claytonia#138](https://github.com/lentago/claytonia/pull/138) — chore(deps): bump the actions-routine group across 1 directory with 4 updates
- 🟣 2026-10-13 · [brasenia#42](https://github.com/lentago/brasenia/pull/42) — build(deps): bump the actions-routine group across 1 directory with 3 updates
- 🟣 2026-10-13 · [betula#136](https://github.com/lentago/betula/pull/136) — chore(deps): bump the actions-routine group across 1 directory with 4 updates
- 🟣 2026-10-13 · [asclepias#18](https://github.com/lentago/asclepias/pull/18) — build(deps): bump the actions-routine group across 1 directory with 2 updates
- 🟣 2026-10-13 · [site-icecreamtofightwith-com#204](https://github.com/lentago/site-icecreamtofightwith-com/pull/204) — Bump pa11y-ci from 4.1.1 to 5.0.0 in the npm-major group across 1 directory
- 🟣 2026-10-13 · [uvularia-site-template#8](https://github.com/lentago/uvularia-site-template/pull/8) — Sync from lentago/uvularia@3d73c7d
- 🟣 2026-10-13 · [monarda#30](https://github.com/lentago/monarda/pull/30) — Bump actions/setup-node from 7.0.0 to 7.1.0 in the actions-routine group
- 🟢 2026-10-13 · [claytonia#22](https://github.com/lentago/claytonia/issues/22) — Fleet PR lane separation: rebase-before-merge + dispatch-time overlap check (no two writers on one file/panel)
- 🟣 2026-10-13 · [claytonia#144](https://github.com/lentago/claytonia/pull/144) — Fleet PR lane separation: rebase-before-merge + overlap check
- 🟢 2026-10-13 · [claytonia#21](https://github.com/lentago/claytonia/issues/21) — Queue admission control: job ownership, fleet occupancy, and capacity awareness at submit time
- 🟣 2026-10-13 · [claytonia#142](https://github.com/lentago/claytonia/pull/142) — Queue admission control: ownership, occupancy, capacity at submit
- 🟢 2026-10-13 · [shared-workflows#68](https://github.com/lentago/shared-workflows/issues/68) — claude-responder: skip events initiated by bots instead of failing the `claude / claude` check
- 🟣 2026-10-13 · [shared-workflows#73](https://github.com/lentago/shared-workflows/pull/73) — fix(claude-responder): skip bot-initiated events instead of failing
- 🟣 2026-10-13 · [drosera#278](https://github.com/lentago/drosera/pull/278) — fix(alerts): write the cloud-usage repeat interval as 1d
- 🟢 2026-10-13 · [drosera#234](https://github.com/lentago/drosera/issues/234) — GitHub — Actions dashboard: fleet-wide run history, queue time, and failure trends (feed: betula#113)
- 🟣 2026-10-13 · [drosera#277](https://github.com/lentago/drosera/pull/277) — feat(dashboards): GitHub — Actions dashboard over the Actions feed
- 🟢 2026-10-13 · [lupinus#4](https://github.com/lentago/lupinus/issues/4) — Epic: adoption guide — Phase 1 (launch set: solidago + monarda)
- 🟢 2026-10-13 · [drosera#251](https://github.com/lentago/drosera/issues/251) — Change pipeline: see every merge travel from push to live, keyed by commit SHA
- 🟢 2026-10-13 · [brasenia#26](https://github.com/lentago/brasenia/issues/26) — Phase 2: pane bus, compositor, and the first live panes (Cast-first)
- 🟢 2026-10-13 · [.github#257](https://github.com/lentago/.github/issues/257) — Adopt the six-promise map (ADR-0012) — rollout epic
- 🟢 2026-10-13 · [.github#264](https://github.com/lentago/.github/issues/264) — music-curator leaves the org for cpitzi/music-curator
- 🟣 2026-10-13 · [kalmia#155](https://github.com/lentago/kalmia/pull/155) — chore: repoint the music-curator harvest pointer in a Terraform comment
- 🟣 2026-10-13 · [asclepias#20](https://github.com/lentago/asclepias/pull/20) — manual: cite org repos for drift detection and non-deadlocking checks
- 🟣 2026-10-13 · [.github#265](https://github.com/lentago/.github/pull/265) — chore(fleet): remove music-curator from fleet settings ahead of transfer
- 🟣 2026-10-13 · [drosera#275](https://github.com/lentago/drosera/pull/275) — chore: drop the music-curator mention from a Terraform comment
- 🟢 2026-10-13 · [lupinus#28](https://github.com/lentago/lupinus/issues/28) — check_product_list: compare picker Tier values with the registry
- 🟣 2026-10-13 · [.github#263](https://github.com/lentago/.github/pull/263) — Weekly fleet reports refresh — 2026-10-13
- 🟣 2026-10-13 · [lupinus#31](https://github.com/lentago/lupinus/pull/31) — check_product_list: compare picker Tier values with the registry
- 🟢 2026-10-13 · [.github#260](https://github.com/lentago/.github/issues/260) — Plain-words pass on two brand taglines flagged in the banner rollout
- 🟣 2026-10-13 · [coderabbit#7](https://github.com/lentago/coderabbit/pull/7) — Exempt README banner alt text from the define-on-first-use rule
- 🟣 2026-10-13 · [uvularia#103](https://github.com/lentago/uvularia/pull/103) — brand: re-copy the banner after the eyebrow kind change
- 🟣 2026-10-13 · [osmunda#14](https://github.com/lentago/osmunda/pull/14) — brand: re-copy the banner after the eyebrow kind change
- 🟣 2026-10-13 · [monarda#31](https://github.com/lentago/monarda/pull/31) — brand: re-copy the banner after the eyebrow kind change
- 🟣 2026-10-13 · [lupinus#29](https://github.com/lentago/lupinus/pull/29) — brand: re-copy the banner after the eyebrow kind change
- 🟣 2026-10-13 · [asclepias#19](https://github.com/lentago/asclepias/pull/19) — brand: re-copy the banner after the eyebrow kind change
- 🟢 2026-10-13 · [.github#261](https://github.com/lentago/.github/issues/261) — Banner eyebrow kinds KIT and PLATFORM read as tiers (ADR-0012 audit)
- 🟣 2026-10-13 · [.github#262](https://github.com/lentago/.github/pull/262) — Stop using tier words in the banner eyebrow kind
- 🟢 2026-10-12 · [lupinus#26](https://github.com/lentago/lupinus/issues/26) — Picker grouped by promise, each row keeping its need-shaped wording
- 🟣 2026-10-12 · [lupinus#27](https://github.com/lentago/lupinus/pull/27) — picker: regroup by promise, each row keeping its need-shaped wording
- 🟢 2026-10-12 · [monarda#23](https://github.com/lentago/monarda/issues/23) — Rescue import: WordPress and Squarespace exports to rung-2 Markdown; Wayback as the last resort
- 🟣 2026-10-12 · [monarda#28](https://github.com/lentago/monarda/pull/28) — feat: rescue import for WordPress and Squarespace exports
- 🟣 2026-10-12 · [brasenia#44](https://github.com/lentago/brasenia/pull/44) — Brand header: tagline leads with the role (ADR-0012)
- 🟣 2026-10-12 · [uvularia#101](https://github.com/lentago/uvularia/pull/101) — Brand header: tagline leads with the role (ADR-0012)
- 🟣 2026-10-12 · [claytonia#141](https://github.com/lentago/claytonia/pull/141) — Brand header: tagline leads with the role (ADR-0012)
- 🟣 2026-10-12 · [drosera#274](https://github.com/lentago/drosera/pull/274) — Brand header: tagline leads with the role (ADR-0012)
- 🟣 2026-10-12 · [monarda#29](https://github.com/lentago/monarda/pull/29) — Brand header: tagline leads with the role (ADR-0012)
- 🟣 2026-10-12 · [epigaea#531](https://github.com/lentago/epigaea/pull/531) — Brand header: tagline leads with the role (ADR-0012)
- 🟣 2026-10-12 · [kalmia#154](https://github.com/lentago/kalmia/pull/154) — Brand header: tagline leads with the role (ADR-0012)
- 🟣 2026-10-12 · [mitchella#27](https://github.com/lentago/mitchella/pull/27) — Brand header: tagline leads with the role (ADR-0012)
- 🟣 2026-10-12 · [osmunda#13](https://github.com/lentago/osmunda/pull/13) — Brand header: tagline leads with the role (ADR-0012)
- 🟣 2026-10-12 · [betula#139](https://github.com/lentago/betula/pull/139) — Brand header: tagline leads with the role (ADR-0012)
- 🟣 2026-10-12 · [solidago#215](https://github.com/lentago/solidago/pull/215) — Brand header: tagline leads with the role (ADR-0012)
- 🟣 2026-10-12 · [site-lentago-dev#101](https://github.com/lentago/site-lentago-dev/pull/101) — Suite: uvularia gets its Kit chip from the tier registry
- 🟢 2026-10-12 · [lupinus#24](https://github.com/lentago/lupinus/issues/24) — Tier registry: uvularia has no row
- 🟢 2026-10-12 · [lupinus#10](https://github.com/lentago/lupinus/issues/10) — One canonical product list; support/README.md is missing claytonia, epigaea, and brasenia
- 🟢 2026-10-12 · [lupinus#19](https://github.com/lentago/lupinus/issues/19) — Stories: one spine, three rungs, one map; a six-row coverage matrix
- 🟣 2026-10-12 · [lupinus#25](https://github.com/lentago/lupinus/pull/25) — Stories: one spine, three rungs, one map; one canonical product list
- 🟢 2026-10-12 · [monarda#24](https://github.com/lentago/monarda/issues/24) — Editing without git: a git-backed editor (Sveltia CMS or Pages CMS) in front of the organization's own repository
- 🟣 2026-10-12 · [monarda#27](https://github.com/lentago/monarda/pull/27) — docs: editing without git (Sveltia CMS, off by default)
- 🟣 2026-10-12 · [uvularia#100](https://github.com/lentago/uvularia/pull/100) — ADOPTION: the one-repository rung has a time, 6 min 09 s
- 🟢 2026-10-12 · [monarda#20](https://github.com/lentago/monarda/issues/20) — npm run a11y: the pinned 127.0.0.1 URL fails when run against the live site as the runbooks say
- 🟢 2026-10-12 · [monarda#22](https://github.com/lentago/monarda/issues/22) — Rung 2: the plain organization site page set (home, about, programs, events, donate, contact)
- 🟣 2026-10-12 · [monarda#26](https://github.com/lentago/monarda/pull/26) — feat: rung 2, the plain organization site page set
- 🟢 2026-10-12 · [site-lentago-dev#99](https://github.com/lentago/site-lentago-dev/issues/99) — Suite section becomes the six-promise map
- 🟣 2026-10-12 · [site-lentago-dev#100](https://github.com/lentago/site-lentago-dev/pull/100) — Suite: redraw #systems as the six-promise map (ADR-0012)
- 🟣 2026-10-12 · [.github#259](https://github.com/lentago/.github/pull/259) — Regroup the profile suite table by promise; taglines lead with role
- 🟣 2026-10-12 · [monarda#25](https://github.com/lentago/monarda/pull/25) — ADR-0004: a second rung, the plain organization site
- 🟣 2026-10-12 · [.github#258](https://github.com/lentago/.github/pull/258) — ADR-0012: the offering is six promises; codenames are parts
- 🟣 2026-10-12 · [lupinus#23](https://github.com/lentago/lupinus/pull/23) — Cite the two 2026-10-12 receipts: monarda timed, uvularia rung 1 timed
- 🟣 2026-10-12 · [uvularia#99](https://github.com/lentago/uvularia/pull/99) — Receipts: one-repository rung timed (6 min 09 s); Ask box's first live answer
- 🟢 2026-10-12 · [lupinus#21](https://github.com/lentago/lupinus/issues/21) — Tier registry: brasenia row is stale since 2026-10-07; mitchella has no row
- 🟢 2026-10-12 · [lupinus#20](https://github.com/lentago/lupinus/issues/20) — Picker: "What we are not" names phones, printers and Wi-Fi
- 🟣 2026-10-12 · [lupinus#22](https://github.com/lentago/lupinus/pull/22) — Tiers: refresh brasenia, add mitchella; picker: phones, printers, Wi-Fi
- 🟣 2026-10-12 · [.github#256](https://github.com/lentago/.github/pull/256) — Weekly fleet reports refresh — 2026-10-12
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

---

## Code census

**The lens:** a `CLAUDE.md` (and its kin — `AGENTS.md`, skill `SKILL.md`, and the LLM prompt-programs that *are* a tool's logic) is an instruction set maintained for hygiene, so it's counted as **natural-language code**. Documentation, content/data, and community-health markdown are tallied separately and excluded from the code total, as are data payloads and generated files. This is a deliberate re-cut of the canonical [`metrics/language-census.md`](../metrics/language-census.md), which instead counts all Markdown/JSON/HTML as code.

### Languages

cloc *code* lines (blank + comment excluded). Shell folds Bourne + Bash. Instruction-markdown is promoted into the count (**bold**); the excluded buckets sit below the total.

| # | Language | Code | Files | Share |
|---|----------|-----:|------:|------:|
| 1 | JSON | 50,233 | 486 | 30.6% |
| 2 | Python | 47,372 | 319 | 28.8% |
| 3 | YAML | 21,663 | 377 | 13.2% |
| 4 | HCL | 10,334 | 147 | 6.3% |
| 5 | Shell (Bourne + Bash) | 8,832 | 114 | 5.4% |
| 6 | JavaScript | 5,984 | 60 | 3.6% |
| 7 | Text | 4,667 | 230 | 2.8% |
| 8 | Astro | 4,338 | 56 | 2.6% |
| 9 | **Instructions (CLAUDE.md family + prompt-programs)** | 2,615 | 20 | 1.6% |
| 10 | HTML | 2,442 | 10 | 1.5% |
| 11 | CSS | 1,611 | 11 | 1.0% |
| 12 | JSX | 1,232 | 12 | 0.7% |
| 13 | Jinja Template | 1,209 | 35 | 0.7% |
| 14 | TypeScript | 964 | 42 | 0.6% |
| 15 | XML | 635 | 8 | 0.4% |
| 16 | TOML | 259 | 22 | 0.2% |
| 17 | Other (TOML / Dockerfile / …) | 30 | 4 | 0.0% |
| | **CODE TOTAL** | **164,420** | **1953** | 100% |
| — | _Data / exports — excluded_ | 0 | 0 | — |
| — | _Generated (lockfiles, SVG, brand artefacts) — excluded_ | 47,205 | 131 | — |

### Instruction-markdown as code

- **Hygiene family** (20 files · `CLAUDE.md`, `AGENTS.md`, `SKILL.md`): **2,615 lines**
- **Prompt-programs** (0 files · reference-checker auditors): **0 lines**

#### Hygiene surface — each file is a maintenance obligation

| Repo | File | Lines |
|------|------|------:|
| epigaea | `CLAUDE.md` | 414 |
| shared-workflows | `CLAUDE.md` | 299 |
| .github | `CLAUDE.md` | 253 |
| site-pondviewlane-com | `CLAUDE.md` | 224 |
| betula | `CLAUDE.md` | 203 |
| kalmia | `CLAUDE.md` | 168 |
| site-lentago-dev | `CLAUDE.md` | 108 |
| drosera | `CLAUDE.md` | 107 |
| solidago | `CLAUDE.md` | 99 |
| site-icecreamtofightwith-com | `CLAUDE.md` | 98 |
| brasenia | `CLAUDE.md` | 91 |
| uvularia | `CLAUDE.md` | 79 |
| lupinus | `CLAUDE.md` | 74 |
| asclepias | `CLAUDE.md` | 70 |
| claytonia | `CLAUDE.md` | 69 |
| drosera | `AGENTS.md` | 68 |
| mitchella | `CLAUDE.md` | 62 |
| monarda | `CLAUDE.md` | 54 |
| osmunda | `CLAUDE.md` | 53 |
| repo-template | `CLAUDE.md` | 22 |
| **20 files** | | **2,615** |

### Per-repo

| Repo | Code | Instr | Doc-md | Content-md | Data |
|------|-----:|------:|-------:|-----------:|-----:|
| epigaea | 27,275 | 414 | 1,947 | 0 | 0 |
| drosera | 24,957 | 175 | 2,759 | 0 | 0 |
| uvularia | 19,056 | 79 | 6,859 | 0 | 0 |
| brasenia | 12,442 | 91 | 4,190 | 0 | 0 |
| uvularia-demo-records | 9,011 | 0 | 3,850 | 0 | 0 |
| solidago | 8,308 | 99 | 2,842 | 0 | 0 |
| kalmia | 7,583 | 168 | 2,440 | 0 | 0 |
| site-pondviewlane-com | 7,542 | 224 | 2,898 | 0 | 0 |
| uvularia-records-template | 6,313 | 0 | 1,042 | 0 | 0 |
| .github | 4,579 | 253 | 2,918 | 4,445 | 0 |
| betula | 4,055 | 203 | 2,036 | 0 | 0 |
| claytonia | 4,004 | 69 | 2,174 | 0 | 0 |
| mitchella | 3,752 | 62 | 731 | 0 | 0 |
| uvularia-demo-ask-rules | 3,589 | 0 | 517 | 0 | 0 |
| monarda | 3,578 | 54 | 1,693 | 0 | 0 |
| site-icecreamtofightwith-com | 3,551 | 98 | 893 | 6,004 | 0 |
| site-lentago-dev | 3,088 | 108 | 671 | 0 | 0 |
| uvularia-site-template | 2,817 | 0 | 245 | 0 | 0 |
| uvularia-demo-site | 2,815 | 0 | 245 | 0 | 0 |
| shared-workflows | 2,585 | 299 | 1,257 | 0 | 0 |
| uvularia-rules-template | 1,538 | 0 | 270 | 0 | 0 |
| lupinus | 918 | 74 | 1,468 | 0 | 0 |
| osmunda | 474 | 53 | 454 | 0 | 0 |
| asclepias | 245 | 70 | 736 | 0 | 0 |
| coderabbit _(arch)_ | 201 | 0 | 38 | 0 | 0 |
| repo-template | 144 | 22 | 271 | 0 | 0 |

### Markdown taxonomy

The fleet carries **58,977 lines of Markdown across 812 files**; only 4.4% is instruction-code.

| Class | Lines | Files | Disposition |
|-------|------:|------:|-------------|
| **Instructions** | 2,615 | 20 | **counted as code** |
| Content / data | 10,449 | 95 | payload (vault notes, recipes, test-sets) — excluded |
| Documentation | 45,444 | 681 | READMEs, docs, ADRs, runbooks — excluded |
| Community-health | 469 | 16 | CONTRIBUTING/SECURITY/templates — excluded |
| **All Markdown** | **58,977** | **812** | |

---

## Method

- **Issues:** open issues via `gh search issues --owner lentago --state open`; activity from `gh search prs --owner lentago --merged` and closed issues filtered to the 30-day window. Public metadata only — no transcript harvest, ops items, or on-prem detail (those live in the LAN copy).
- **Census tool:** `cloc`, run per-repo as `cloc --by-file --vcs=git` so only git-tracked files count (build output, `node_modules`, `.terraform`, venvs never enter). Lines are cloc *code* lines.
- **Scope:** the active repos owned by the `lentago` org, derived at runtime — personal repos and third-party clones are out of scope; archived repos are frozen and excluded.
- **Markdown classifier:** instruction-code = `CLAUDE.md`/`AGENTS.md`/`SKILL.md` or a versioned `prompts/*-auditor.md`; community-health = governance filenames + issue/PR templates; content = repo-scoped payload paths (ice-cream `recipes/`·manuscript, reference-checker `test-sets/`·`reports/`, dotgithub `fleet-reports/`); everything else = documentation.
- **Data / generated carve-outs:** exported payloads under the declared data dirs (homeassistant-config `context/`) count as data whatever their serialisation — JSON, JSONL, CSV/TSV, XML, YAML — as does reference-checker's rendered `reports/*.html`; lockfiles, SVG and `.github/brand/generated/` (emitted from `brand/fleet.json`) are generated. drosera's `dashboards/*.json` stay in code as Terraform-enforced dashboards-as-code.
- **Regenerating:** `python3 metrics/generate-fleet-reports.py --out-dir .`

_Generated with Claude Code (Repo Claude)._
