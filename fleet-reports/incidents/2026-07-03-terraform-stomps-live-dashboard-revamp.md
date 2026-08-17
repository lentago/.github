# Incident Digest — Terraform silently reverts the uncommitted dashboard revamp, 2026-07-03

*The 17-minute incident that wrote a fleet-wide law: an infra-health dashboard
revamp pushed live through the Grafana API — but never committed — was stomped
back to repo JSON by the Terraform apply of five completely unrelated bug-fix
merges.*
Compiled 2026-07-13 by Home Claude from local session transcripts in
`~/.claude/projects/` (harvested by the `/incident-digest` full-history scan).
All times **America/New_York (EDT, UTC-4)**; raw transcript timestamps are UTC.

**Deployment-caused:** yes

---

## TL;DR

On the evening of 07-02, the Infrastructure Health dashboard got a substantial
revamp — a six-node Fleet Scoreboard (finally covering pve3/4/5), per-host
drill-downs, a NAS root-usage fix — applied to Grafana Cloud **via the API
only, never committed to the repo**. The next afternoon, an unrelated
dashboard bug-fix batch (five bullpen PRs, all legitimate, none touching
infra-health) merged into the observability repo; **each merge triggers the
repo's Terraform apply, which enforces `dashboards/*.json` as the source of
truth** — and the first apply (13:11) silently reverted the revamp. The
operator caught it at 13:24 (*"wait — something regressed. what happened to my
other pve hosts?"*); by 13:28 the revamp was recovered from Grafana's version
history (v7), pulled through the API into the repo, and re-landed as PR #119 —
this time repo-enforced, so it can never be stomped again. PR #120 codified
the anti-drift rule minutes later.

1. **The stomp** — IaC enforcement working exactly as designed against work
   that never entered the code path.
2. **The recovery** — Grafana's version history held the full v7 JSON; total
   regression window 17 minutes, zero loss.
3. **The law** — this incident is the origin of the fleet-wide **"Live-state
   vs. code discipline"** rule (never mutate an enforced surface without
   codifying in the same session; live-ahead-of-repo state is a fire).

The damage was **17 minutes of a degraded dashboard and one adrenaline spike**;
nothing was lost. The lesson — now standing policy — is that **on an
IaC-enforced surface, uncommitted work is already deleted; it just hasn't
happened yet.**

---

## Timeline (EDT)

| Time | Event | Ground truth |
|---|---|---|
| 07-02 evening | Infra-health revamp built and pushed to Grafana Cloud **via API only** (Fleet Scoreboard with all 6 nodes, per-host repeating rows, neptune root-usage fix). Not committed — the session moved on | Grafana version history (v7); absence from repo JSON |
| 07-03 12:32 | Next-day session starts: *"traverse all Lentago Labs grafana dashboards and note bugs… File issues as bugs are found"* | transcript first prompt |
| ~12:45 | Live-verified audit files 6 issues (#108–#113): `Value #A` table columns, legacy legend schema, one-slice pie chart, dead dropdown variable, etc. Five dispatched to the bullpen | drosera issues #108–#113 |
| 13:11–13:13 | Worker PRs reviewed and merged: **#114, #115, #117, #118, #116** (the last repaired locally first — the worker had wrapped a correct fix in a whole-file reformat, +976/−254, violating scope) | merge timestamps 17:11:35–17:13:16Z |
| **13:11** | **First Terraform apply fires on merge — and enforces repo JSON over the live dashboards, silently reverting the uncommitted infra-health revamp.** Four more applies follow as the batch lands | terraform workflow runs on each merge |
| 13:14 | Applies verified green; the five *intended* fixes confirmed live, panel by panel. Nothing yet suggests collateral damage | rendered panels in-session |
| **13:24** | **Operator:** *"wait - something regressed. what happened to my other pve hosts? the infra dash?"* | transcript |
| 13:24 | Cause hypothesized within one message: *"Nothing we merged touched `infra-health.json` — but every merge triggered a full Terraform apply, which would stomp any live UI-only edits back to repo JSON"* | transcript |
| 13:25–13:27 | Grafana **version history** checked → full v7 JSON (the revamp) recovered; pulled via API directly into the repo file | transcript |
| **13:28** | **PR #119 merged**: *"infra-health: restore fleet-scoreboard revamp lost to IaC drift stomp"* — the revamp is now repo-enforced | merged 17:28:43Z |
| 13:31 | **PR #120 merged**: repo CLAUDE.md anti-drift rule with the recovery recipe (check version history before declaring live-only work lost) | merged 17:31:39Z |
| 13:33 | Verified live: Fleet Scoreboard back with all 6 hosts. Wrap-up states the standing rule | transcript |
| aftermath | Rule generalized fleet-wide: `~/repos/CLAUDE.md` § *"Live-state vs. code discipline"* — enforced-surface table, "live-ahead-of-repo is a fire," recovery-trail checklist — citing this incident as origin | fleet CLAUDE.md (canonical: shared-workflows) |

---

## The failure — enforcement working as designed, against undesigned work

Nothing malfunctioned. The Terraform workflow did precisely its job: on every
merge to main, make live Grafana match `dashboards/*.json`. The revamp existed
only on the live side, so the machinery classified it — correctly, by its own
lights — as drift, and removed it. Five times in a row, for good measure.

What makes this register-worthy is the *shape* of the hazard:

- **The trigger was unrelated work.** None of the five merges touched
  `infra-health.json`. On an enforce-everything apply, *any* merge anywhere in
  the repo is a loaded gun pointed at *all* uncommitted live state.
- **The gap was invisible at merge time.** The PRs were reviewed carefully —
  one was even repaired for scope violations — but review looks at what a PR
  *changes*, not at what the apply it triggers will *revert*.
- **The window was long-fused.** The revamp survived the evening because no
  merge happened overnight. Uncommitted live work on an enforced surface
  doesn't fail when you make it; it fails when anyone else does anything.

## The recovery — why this was 17 minutes and not a rebuild

Grafana keeps dashboard version history server-side; the pre-stomp revamp was
sitting there as v7. Recovery was: fetch v7 JSON via the API → write it into
the repo → PR #119 → the same enforcement machinery that destroyed the work
now guarantees it. The recovery recipe (version history first, then re-land
through the repo) went straight into the repo's CLAUDE.md via #120 so the next
session doesn't rediscover it under pressure.

## What did NOT happen (the reassuring part)

- **Nothing was lost.** Grafana's version history held the complete revamp;
  the restored dashboard is byte-equivalent in effect and now safer than
  before (repo-enforced instead of live-only).
- **The five bug fixes were all legitimate and all survived** — audit, dispatch,
  review, merge, verify all worked; the batch itself was a success story.
- **No other dashboard carried uncommitted live edits** at stomp time — the
  blast radius was exactly one dashboard's revamp.
- **What the cost actually WAS:** a 17-minute regression window, one recovery
  detour, and the operator having to be the detection mechanism.

## CTO lessons — where governance was missing

*All three were codified within the hour — this incident's distinguishing
feature is that its lessons shipped as standing policy the same day.*

1. **Never mutate an enforced surface without codifying in the same session.**
   A live-only edit survives exactly until the next apply, and the next apply
   is triggered by anyone. → **drosera#120** (repo rule) and the fleet-wide
   *Live-state vs. code discipline* section (enforced-surface table) in
   `~/repos/CLAUDE.md` / `shared-workflows`.
2. **Live-ahead-of-repo state is a fire, not a curiosity.** If live doesn't
   match repo, someone's un-codified work is one merge from destruction —
   recover it into a PR *before* merging anything else. (Standing rule #2 of
   the same section.)
3. **Check the recovery trail before declaring loss.** Grafana version
   history, Route 53 change logs, ruleset audit logs — enforced systems
   usually keep one. It turned this from a rebuild into a 4-minute restore.
4. **Make the apply announce what it reverts.** A terraform plan diff that
   shows live-vs-repo drift being overwritten — posted to the PR before apply
   — would have turned silent destruction into a visible warning.
   → **drosera#153** (filed 2026-07-13 from this report).

The register through-line: the [06-19 collision](2026-06-19-multi-claude-collision.md)
was *sessions* crossing on shared repos; this is a *pipeline* crossing an
operator on a shared surface. Same governance root — shared mutable state with
two writers and no fencing — different pair of hands on the state.

---

## Appendix — sources

```
Transcript:  ~/.claude/projects/-home-cpitzi-repos/a861ef1e-*.jsonl
             (session 2026-07-03 12:32 EDT; duplicate transcript 06e9ae69 is
             the same session content)
Ground truth: lentago/drosera issues #108–#113; PRs #114–#118 (merged
             17:11–17:13Z), #119 (17:28:43Z), #120 (17:31:39Z) — via gh;
             Grafana dashboard version history (v7); terraform workflow runs
Aftermath:   fleet-wide "Live-state vs. code discipline" rule
             (~/repos/CLAUDE.md, canonical in shared-workflows/CLAUDE.md)
```
