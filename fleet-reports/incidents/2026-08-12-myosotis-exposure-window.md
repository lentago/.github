# Incident Digest — The watcher readable by the watched: closing the myosotis exposure window on org-opening day, 2026-08-12

*Opening the org to colleagues while it still held one private repo — the
agent-context ledger — and GitHub's default base permission quietly granted
every member read on it. Caught by a risk question, closed inside half an
hour, and made structurally unrepeatable.*
Compiled 2026-08-12 from a multi-session transcript harvest, cross-checked
against live GitHub state. All times **America/New_York (EDT, UTC-4)**.

**Deployment-caused:** no

---

## TL;DR

The lentago org was repurposed on 08-12 as a learning lab for IT-ops
colleagues — invites out, one already accepted. The org still held one
**private** repo: `myosotis`, the agent context ledger (standing instructions,
permission allowlists, host-side agent context — the fleet's own audit trail),
and the org's `default_repository_permission` was still GitHub's default
`read`. That combination gave an accepted member **implicit read on the one
repo whose purpose is defeated by being readable by the population it
watches**. The risk had been flagged as a recommendation in the org-opening
issue (.github#91) but was not a precondition gate; the trigger to act was the
operator asking "define the risk in read access to myosotis" (12:52).
Remediation was two-pronged and same-hour: base permission flipped
`read`→`none` with access rebuilt as an explicit team scoped to public repos
(13:01), and the repo **transferred out of the org entirely** to the personal
account (~13:04) — an org that *cannot* hold the ledger can't regress into
exposing it. Propagation (fleet config purge, worker committer repoint,
dashboard repoint) completed and was verified by 13:19; one missed reference
in the committer repoint was caught and fixed one minute later. GitHub
provides no read audit, so "was it ever accessed" is unprovable — but the org
now contains zero private repos, making the class unrepeatable.

---

## Timeline

| Time | Event |
|---|---|
| (prior) | Colleague invites issued; one accepted while `default_repository_permission=read` and `myosotis` private in-org — the window opens. Flagged in .github#91 as a recommendation |
| 12:52 | Operator: "define the risk in read access to myosotis" |
| 12:53 | Risk articulated: the ledger is "the operating map of your agent fleet … the one repo whose *purpose* is defeated by being readable by the population it guards against" |
| 13:01 | Base permission `read`→`none`; explicit `players` team created (triage, public repos only) |
| ~13:04 | Operator transfers the repo to the personal account: "do it all - the transfer is done" |
| 13:05–13:19 | Propagation: fleet config purged (.github#93), worker committer repointed (claytonia#93; a missed reference caught one minute later by #94), dashboard repointed (drosera#190), ledger verified writing to the new home |
| 13:19 | "the org now contains **zero private repos**"; invites cancelled and reissued team-scoped (old invite links died — cosmetic) |

---

## What did NOT happen

- **No evidence the access was exercised** — and none can exist either way:
  GitHub keeps no read audit. The honest claim is "window open, exploitation
  unknowable, window now closed."
- **The two concurrent sessions mutating org state did not collide** — both
  posted execution records to the same tracking issue and partitioned cleanly.
- **No secret was ever in the ledger** — it holds context and configuration,
  not credentials. The exposure was operational intelligence, not keys.

## CTO lessons

1. **Sequencing is the control.** Flip the base permission and place private
   repos *before* the first invite, not after the first accept. The
   remediation existed as a written recommendation while the window was open —
   a recommendation is not a gate. Org-opening needs a preflight checklist
   whose items block the invites.
2. **Structural fixes beat access rules.** The permission flip closed the
   window; the transfer removed the wall it was cut in. An org that holds no
   private repos cannot leak one through any future permission regression,
   team misconfiguration, or default reset. When a repo's threat model
   excludes a population, don't share a container with that population.
3. **Defaults are decisions someone else made.** `read` as the org base
   permission is GitHub's choice, inherited silently. Every org-level default
   deserves an explicit pass at adoption — this one had survived since the org
   was created.
4. **Propagation sweeps need a grep-everything pass.** The committer repoint
   missed one provisioning reference; the one-minute catch-and-fix (#94) is
   the pattern working, and the reminder that a relocation isn't done until a
   full-text search says so.

---

## Sources

Sessions `4bb5cada` and `9b48f756` (2026-08-12, concurrent); .github#91
(recommendation + execution records), #93; claytonia#93/#94; drosera#190;
live verification: org base permission `none`, zero private org repos, ledger
committing at its new home.
