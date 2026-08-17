# Incident Digest — Merged is not deployed: the Spotify harvester that never ran, 2026-07-12→22

*Ten days of daily listening snapshots never captured, because the harvester
everyone believed was running had never been deployed at all — and nothing in
the system could tell the difference.*
Compiled 2026-08-12 from a multi-session transcript harvest, cross-checked
against GitHub and on-host ground truth. All times **America/New_York (EDT,
UTC-4)**.

**Deployment-caused:** no

---

## TL;DR

The music-curator Spotify harvester was merged on 2026-07-12 (music-curator#32)
and believed operational. On 07-22, an unrelated NAS inventory found its
landing zone empty — zero daily snapshots since setup — and an issue was filed
on the premise of a *stalled* harvester. The evening session ground-truthed the
runtime and overturned the premise entirely: **it was never deployed.** No
workflow existed in n8n, no Redis container, no secrets provisioned, no NAS
bind-mount on the container — and the repo's two READMEs described two
different architectures. Because Spotify's recently-played API is a rolling
window, the ~10 days of listening history are **permanently unrecoverable**.
The same evening it was actually deployed for the first time: compose rebuilt
with Redis, secrets provisioned (OAuth bootstrap run by the operator),
producer and consumer workflows imported and activated, first successful
harvest verified, and the issue closed.

---

## Timeline

| Time | Event |
|---|---|
| 07-12 | Harvester merged (music-curator#32); believed set up; landing zone created on the NAS |
| 07-12 → 07-22 | Zero snapshots land. Nothing alerts — an absent collector is indistinguishable from a quiet one |
| 07-22 16:44 | NAS inventory (an unrelated cleanup session) notices the empty landing zone |
| 17:01 | music-curator#47 filed on the "stalled harvester" premise, including an error-notification ask "so a silent stall can't run ten days again" |
| 18:38 | Runtime ground-truthed: the container has no NAS mount at all — "the file-based path *cannot* work as deployed" |
| 18:41 | Root cause declared: "it was never deployed — not a regression" |
| 18:45–20:52 | Actual first deploy: compose + Redis, secrets, OAuth bootstrap (operator), workflows imported and activated; operator self-reports breaking a GUI step mid-setup ("I accidentally messed up the harvest step"), repaired; first harvest verified; #47 closed |

---

## What did NOT happen

- **No deployed system failed.** Nothing regressed, nothing crashed — the gap
  between "merged" and "running" was never closed, and no process existed to
  notice.
- **Nothing else on the runtime was affected**; the deploy gap was scoped to
  the harvester.
- **The eventual deploy was same-evening once the premise was corrected** —
  the ten-day cost was entirely in the belief, not the work.

## CTO lessons

1. **"Merged" is a statement about the repo; "deployed" is a statement about
   the world.** The fleet's discipline verifies the first rigorously (PRs,
   checks, auto-merge) and verified the second not at all. A deploy isn't done
   without a first-run artifact — a log line, a landed file, a heartbeat —
   attached to the closing comment.
2. **Absence alerting, fourth verse.** Like the ECS gap and the Firewalla
   outage, the only failure signal was silence — but here silence dated from
   birth. A landing zone that expects dailies should alert on "no new files in
   48h" from the day it's created, which also catches never-started.
3. **Docs that disagree are a deployment smell.** Two READMEs describing two
   architectures (files-to-share vs Redis queue) meant the design had moved
   after the docs — and nobody following either document could have verified
   the real system. The ground-truth pass that broke the case started by
   ignoring both.
4. **Rolling-window data sources make deploy gaps permanent.** For any
   collector whose upstream forgets (API windows, rotating logs), deploy
   verification isn't hygiene — it's the difference between a delay and a
   loss. This register now holds three examples.

---

## Sources

Sessions `1c84200b` (discovery, `~`) and `8b232b9d` (diagnosis + deploy,
`~/repos/music-curator`), 2026-07-22; music-curator#32, #47 (filed 20:59Z,
closed 00:52Z 07-23); n8n runtime on the automation LXC; NAS
`spotify-harvest/` landing zone.
