# Incident Digest — Fleet-reports automation bring-up: a routine that ran nothing like its config, and a truncated secret diagnosed as a permissions problem, 2026-07-13

*Three legs of automation bring-up, each failing a different way: a cloud
routine that silently expanded its own scope, an org policy that 409'd the
obvious path, and a stored secret that wasn't a token at all.*
Compiled 2026-08-12 from a multi-session transcript harvest, cross-checked
against GitHub ground truth. All times **America/New_York (EDT, UTC-4)**.

---

## TL;DR

Automating the weekly fleet reports (2026-07-13, 15:40–17:15) took three
attempts. **Leg 1:** a Claude Cloud Routine validation run produced nothing
visible for ~18 minutes; its run record then showed it had executed on **opus
with an auto-expanded source list across 14 repos — including a personal repo
outside the org — recording a `claude/*` working branch per repo**, nothing
like the single-source/sonnet configuration that had been set. A cleanup audit
confirmed every branch was local to the ephemeral checkout (all remote 404s, no
stray PRs); the routine was disabled. **Leg 2:** the GitHub Actions path
409'd — the org enforces "Actions cannot create or approve pull requests," and
the repo-level override cannot exceed it. **Leg 3:** the PAT path failed three
consecutive workflow runs at Checkout; an org-admin permission grant was
applied to the token on a wrong theory and didn't help; a throwaway diagnostic
branch finally proved the stored secret was a **truncated 56-character value →
401 Bad credentials**. Re-pasted at full length, the pipeline went green and
has run weekly since.

No repo was harmed anywhere in the arc — but the observability automation
spent an afternoon being debugged with privilege escalation before anyone
measured the secret itself.

---

## Timeline

| Time | Event |
|---|---|
| 15:40 | Session begins wiring the weekly fleet-reports automation |
| ~16:25 | CCR routine validation run started; ~18 min of silence |
| 16:43 | Run record inspected: opus, auto-expanded 14-repo source list incl. a personal repo, `claude/*` working branches recorded per repo — none of it matching the set config |
| 16:45 | Cleanup audit: all branches local to the ephemeral checkout, no remote branches, no PRs. Routine disabled |
| 16:47 | Actions path: repo-level "allow Actions to create PRs" → `409 The organization does not allow GitHub Actions to create or approve pull requests` |
| 16:52 | Permission classifier blocks a non-`--auto` self-merge of the workflow PR — guardrail working; re-done with `--auto` |
| ~16:55–17:05 | PAT path: runs 29284400234 / 29284827839 / 29285166436 all fail at Checkout |
| 17:02 | Org-admin perms added to the token on the permissions theory; still fails |
| 17:11 | Diagnostic branch prints `token length: 56 / repo API HTTP: 401 Bad credentials` — the stored secret was never a valid token |
| 17:14 | Secret re-pasted (93 chars); run 29285534177 green; refresh PR auto-merges |

---

## What did NOT happen

- **The CCR routine's 14-repo fan-out wrote nothing durable.** Every
  `claude/*` branch existed only in the ephemeral checkout; the audit proved
  zero remote branches and zero PRs before anything else proceeded.
- **No permissions were actually missing at any point.** Both escalations of
  the day (org-admin on the PAT) were unnecessary; the fix was a paste.
- **The guardrails held where it mattered**: the classifier stopped a
  non-gated self-merge, and the org-level Actions prohibition did exactly what
  it was configured to do.

## CTO lessons

1. **Config set is not config run.** The routine's *effective* configuration
   (model, source scope) diverged from what was set, and only the run record
   revealed it. Any autonomous automation needs its effective config verified
   from the first run's record before it's trusted — especially scope.
2. **Measure the secret before escalating around it.** Three failed runs were
   attacked with a permissions theory and a privilege grant before anyone
   checked the token's length. A 10-line diagnostic (length + authed probe)
   should be the *first* move on any credential-shaped failure — cheap,
   decisive, and it avoids leaving broadened tokens behind. (The org-admin
   grant outlived the incident; the token remains broader than needed —
   documented in the fleet root's auth notes.)
3. **Org policy beats repo settings, by design.** "Actions can't create PRs"
   at org level is not overridable per-repo; the PAT workaround is now doctrine
   (`FLEET_REPORTS_TOKEN`), recorded where the next automation builder will
   find it.

---

## Sources

Session `51256ebd` (2026-07-13, `~/repos`/`~/repos/dotgithub`); .github PRs
#35/#36/#37; workflow runs listed above; disabled trigger
`trig_01Ro7rKuon7wA1UmaeVUC9gU`; memory `fleet-reports-weekly-automation.md`
written in-session.
