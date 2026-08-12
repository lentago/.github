# Incident Digest — ECS app logs silently dark for 16 days behind a placeholder credential, 2026-07-08→24

*A rename migration recreated a secret with its Terraform placeholder still
inside, and every layer that touched it — Secrets Manager, ECS, FireLens, the
sidecar — treated "present and plausible" as "working."*
Compiled 2026-08-12 from a multi-session transcript harvest, cross-checked
against GitHub, AWS, and Axiom ground truth. All times **America/New_York
(EDT, UTC-4)** unless marked UTC.

---

## TL;DR

The ECS application log stream to Axiom (`cjp-solidago-ecs`) received **no
events from 2026-07-08 01:46 UTC to 2026-07-24** — a 16-day silent gap with no
alert, masked by the healthy ALB stream beside it. Root cause: the 07-08
foundry→solidago AWS rename/tfstate migration recreated the Secrets Manager
secret `solidago-dev-axiom-ingest-header` with the Terraform literal
`PLACEHOLDER-set-out-of-band` as its value; the FireLens sidecars had been
401-ing against api.axiom.co ever since. The remediation itself misfired once —
the first `put-secret-value` paste went in with the `<axiom-ingest-token>`
placeholder still in the command — before the real token landed, all three ECS
services were force-redeployed, and ingest resumed the same evening. The gap is
**permanent telemetry loss**: FireLens chunks cannot be retried.

The same evening surfaced a third variant of the identical failure shape in
drosera's secret-backed Terraform vars (guards that accepted empty strings),
making it a pattern, not an accident: *a credential that is present,
structurally plausible, and wrong is invisible to every system that touches
it.*

---

## Timeline

| Time | Event |
|---|---|
| 07-08 01:46–01:58 UTC | foundry→solidago rename applies (solidago#102–#105) recreate the ingest-header secret with its placeholder value. Last event lands in `cjp-solidago-ecs`; 401s begin, logged only inside the FireLens sidecars |
| 07-08 → 07-24 | 16 days of silence. No ingest-gap alert exists for the dataset; the ALB stream stays green beside it |
| 07-24 ~18:15 | While wiring the pondviewlane analytics pane, an APL query finds the dataset dead: 43,468 events, then nothing since 07-08 |
| 18:31 | solidago#143 drafted: "no events since 2026-07-08 01:46 UTC" |
| 19:35 | Sidecar logs confirm continuous `401 "auth token not provided"`; secret value read back: `PLACEHOLDER-set-out-of-band` |
| 19:44 | First remediation paste misfires — the 401 *changes* to `"token not supported"`: the secret now holds the literal `<axiom-ingest-token>`, angle brackets and all |
| 19:47 | Second attempt lands the real token; three `aws ecs update-service --force-new-deployment` runs roll the services |
| ~19:50 | Ingest resumes; solidago#143 closed with full provenance |
| 21:27 | Third instance of the pattern found in drosera TF vars ("illusory" guards accepting empty strings); real `validation` blocks added and harness-proven |

---

## What did NOT happen

- **The applications never stopped serving.** Only log *shipping* was dark;
  ALB telemetry, metrics, and the sites themselves were healthy throughout.
- **No credential was exposed.** The failure was a placeholder where a secret
  should be — the inverse of a leak.
- **The rename migration itself was correct** — resources, state, and CI all
  moved cleanly. The placeholder was the one out-of-band step with no
  verification attached.
- **Detection wasn't luck-free but wasn't blind either**: the gap was found by
  deliberate instrumentation work (the analytics pane), the same
  coverage-not-spot-check pattern that found the 07-10 Firewalla outage.

## CTO lessons

1. **Alert on absence — again.** This is the third register entry (after
   07-05→08 and 07-10→13) where the only failure signal was silence. Ingest-gap
   alerts must cover *every* load-bearing stream, not just the ones that have
   already burned you. → drosera#150 (heartbeat caveat), drosera#170, solidago#144
2. **"Set out of band" is an unfinished migration step.** Any apply that
   recreates a secret with a placeholder needs a post-apply verification that
   the real value has landed — a smoke read, a canary event, anything that
   turns "present" into "works."
3. **Placeholder-shaped values deserve structural rejection.** Secrets and TF
   vars should refuse values matching `PLACEHOLDER*`, `<...>`, or empty string
   at write time. The same shape misfired three times in one evening through
   three different layers.
4. **Rename migrations have a blast radius beyond names.** The rename was
   verified against resource names, not against every secret it recycled —
   out-of-band values are exactly what a state migration can't carry.

---

## Sources

Session `2bdac642` (2026-07-24, `~/repos`); solidago#143 (opened and closed
07-24), #144; drosera#170; FireLens sidecar 401 logs 2026-07-24 23:30–23:43 UTC;
Axiom APL last-event queries; solidago commits `c4fffca`/`611558c`/`76c9f2d`.
