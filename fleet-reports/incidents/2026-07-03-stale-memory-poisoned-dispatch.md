# Incident Digest — A stale memory steers a worker to regress correct code, 2026-07-03

*The dispatch prompt said "keep `pitzilabs-claude-runner`, it's still correct."
It wasn't. The worker obeyed, un-fixed a fixed dashboard, and the PR it opened
was authored by an App whose very name disproved the instruction it had been
given.*
Compiled 2026-07-13 by Home Claude from local session transcripts in
`~/.claude/projects/` (harvested by the `/incident-digest` full-history scan).
All times **America/New_York (EDT, UTC-4)**; raw transcript timestamps are UTC.

**Deployment-caused:** no

---

## TL;DR

Two days into the PitziLabs→Lentago rebrand, Home Claude dispatched
rebrand-reconciliation jobs to the bullpen fleet. The drosera job carried a
protective guardrail: *fix the stale references, but keep the Runner-Fleet
dashboard's Open-agent-PRs author filter at `app/pitzilabs-claude-runner` —
that's still correct.* The guardrail came from a **stale rebrand-era memory**,
not from reading the repo — where the filter had already been corrected to
`app/lentago-claude-runner`. The worker did exactly as told and **regressed
the already-correct filter**. The tell was on the PR itself: it was authored by
`app/lentago-claude-runner` — the renamed App the guardrail claimed didn't
exist yet. PR **#123** was caught in review, declared must-not-merge, and
closed; the poisoned memories were corrected in-session; the clean sibling PR
**#124** superseded it 26 minutes later. Zero damage reached main.

1. **The poisoning** — a "don't change X" constraint built from memory instead
   of ground truth, injected into an autonomous worker's prompt.
2. **The obedient regression** — the worker had no way to know better; a hard
   instruction beat the evidence in its own checkout.
3. **The catch** — the fleet's review gate (workers never merge) did its job;
   the regression died in the PR queue.

The damage was **one wasted worker run and one closed PR**. The lesson is
about **memory hygiene at org-rename boundaries and the asymmetric danger of
wrong constraints**: an autonomous agent can recover from a missing
instruction, but not from a false one delivered with authority.

---

## Timeline (EDT)

| Time | Event | Ground truth |
|---|---|---|
| 06-29 → 07-03 | The PitziLabs→Lentago rebrand rolls across repos, the Grafana stack, and the runner GitHub App (`pitzilabs-claude-runner` → `lentago-claude-runner`). Session memories from mid-rebrand freeze various "current state" claims that immediately start aging | rebrand cutover sessions; org audit |
| 07-03 ~16:45 | Evening session (the same one hunting the faro-collector DNS flood) turns to rebrand cleanup: reconcile-jobs drafted for drosera and betula, dispatched to the bullpen | transcript |
| ~16:50 | **The poisoned guardrail ships**: the drosera job is told to keep `author:app/pitzilabs-claude-runner` in the Open-agent-PRs panel — *"based on a stale memory"* — despite the panel already being correct on main | transcript 21:08Z (retrospective) |
| 17:08 | Worker's PR **#123** opens. Its author field reads **`app/lentago-claude-runner`** — *"the runner App itself got renamed too, which my dispatch didn't account for"* — the instruction is disproven by the PR that followed it | gh: PR #123 author |
| 17:11 | Diff review: the worker *"dutifully regressed the already-correct author filter."* Verdict in-session: **"PR #123 must not merge"** — its dashboard change breaks the panel; only a trivial comment-freshening is salvageable. *"That's on me: I trusted rebrand-era memory instead of grepping the actual repo before dispatching"* | transcript 21:11Z |
| 17:11 | Poller stopped; **the stale memories are corrected at the source** (runner-fleet panel memory → `lentago-claude-runner` / `org:lentago`; a lesson appended to the rebrand memory: grep the repo before dispatching rebrand edits) | transcript |
| 17:12 | **PR #123 closed, unmerged** | gh: closed 21:12:39Z |
| 17:38 | Clean sibling **PR #124** (stack URL, datasource names, org URLs, alloy healthcheck — superseding #123's salvageable parts) merges, alongside betula's #69 from the same dispatch batch. En route, a separate known gap resurfaces: the runner App lacks the `workflows` permission, so it can't push workflow-file changes | gh: #124 merged 21:38:41Z; betula#69 21:38:48Z |

---

## The failure — memory as ground truth, at the worst possible time

Fleet memories exist to carry context across sessions, and most days they're
right. An **org rename is the day they're wrong in bulk**: every memory that
names an org, an App, a URL, or a datasource silently flips from asset to
hazard, and each one *reads* exactly as trustworthy as before. This dispatch
compounded the staleness three ways:

- **It converted a stale fact into a hard constraint.** "Keep X, it's correct"
  is far more dangerous in a worker prompt than silence — the worker treats it
  as operator intent and will override what its own checkout shows. The
  instruction manufactured certainty the dispatcher didn't have.
- **It skipped the 30-second verification.** A `grep` of the dashboard JSON
  before dispatch would have shown the filter already fixed. The session's own
  verdict: *"I trusted rebrand-era memory instead of grepping the actual repo."*
- **It ignored that the memory's subject was itself mid-rename.** The very App
  named in the guardrail had been renamed — the instruction was stale about
  the one entity most guaranteed to be in flux during a rebrand.

There is an irony worth preserving: the job existed to *remove* stale
`pitzilabs` references, and its one hard instruction *protected* a stale
`pitzilabs` reference.

## The catch — the review gate as designed

The fleet's standing rule — **workers never merge; every worker PR waits for
local review** — is usually described as protection against a worker's own
misjudgment. Here it protected against the *dispatcher's* misjudgment, which
the worker had faithfully executed. The regression was identified in the diff,
the PR closed, and the memory corrected, all inside four minutes of the PR
opening. This is the same gate that contained the [06-19 collision](2026-06-19-multi-claude-collision.md)'s
redundant work; it is earning its keep.

## What did NOT happen (the reassuring part)

- **Nothing reached main.** #123 died in the queue; the panel on the live
  dashboard was never wrong (its correct state was already deployed).
- **The rest of the dispatch batch was clean** — #124 (drosera) and #69
  (betula) merged normally; the poisoning was scoped to the one instruction,
  not the batch mechanism.
- **The stale memories were corrected at the source, in-session** — the same
  failure can't fire from those memories again.
- **What the cost actually WAS:** one worker run, one closed PR, ~30 minutes
  of review/salvage — and the erosion of a small illusion: that memory
  precision equals memory freshness.

## CTO lessons — where governance was missing

1. **Verify before you constrain.** Any "keep X / don't touch Y" guardrail in
   a dispatch prompt must be checked against the repo *at dispatch time* — a
   wrong constraint is strictly worse than no constraint, because the worker
   will obey it over the evidence in front of it.
2. **Rename events should trigger a memory audit.** An org/App/domain rename
   invalidates a whole class of memories at once. The corrective applied here
   was reactive (fix the two that bit); the systemic version is a sweep of
   memory files for the old names as a standard rebrand-cutover step —
   candidate item for the claytonia governance backlog, alongside the rebrand
   runbook.
3. **Prefer pointers over facts in dispatch prompts.** "The panel's author
   filter must match the current runner App name — verify in the repo" travels
   safely across renames; "keep `pitzilabs-claude-runner`" does not.
   Instructions that tell the worker *how to find* the truth age better than
   instructions that *assert* it.
4. **The review gate is load-bearing — keep it.** This incident is a second
   independent proof (after 06-19) that no-worker-merges catches whole
   categories of upstream error that no amount of worker capability would
   avoid.

---

## Appendix — sources

```
Transcript:  ~/.claude/projects/-home-cpitzi/092c74a6-*.jsonl
             (evening segment, 2026-07-03 ~16:45–17:45 EDT; same session as the
             faro-collector DNS investigation)
Ground truth: lentago/drosera PR #123 (closed unmerged 21:12:39Z, author
             app/lentago-claude-runner), PR #124 (merged 21:38:41Z);
             lentago/betula PR #69 (merged 21:38:48Z) — via gh
Aftermath:   runner-fleet panel memory + rebrand memory corrected in-session;
             "grep the repo before dispatching rebrand edits" recorded
```
