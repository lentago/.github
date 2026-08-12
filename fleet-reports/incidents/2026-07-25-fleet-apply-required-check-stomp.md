# Incident Digest — The enforcement tool stomped the thing it enforces: required-checks rollout day, 2026-07-25

*Settings-as-code is only as safe as its apply semantics. The fleet's own
governance tool wholesale-replaced a ruleset and silently deleted a live
required check — caught minutes later by the same session, fixed by a different
Claude, and validated that evening when the new gates caught their first real
regression.*
Compiled 2026-08-12 from a multi-session transcript harvest, cross-checked
against GitHub ground truth. All times **America/New_York (EDT, UTC-4)**.

---

## TL;DR

Completing fleet-wide required status checks (2026-07-25, 15:34–18:57), the
`fleet-apply.sh --require-checks` tool PUT each repo's
`required_status_checks` rule **wholesale from `required-checks.json`** — and
for one site repo the JSON listed only one of the two live-required contexts,
so the apply **silently deleted a live required check** (`Compile and commit`),
weakening that repo's merge gate. The same session caught it minutes later
during its audit, restored the check live, codified it (.github#70), audited
the other 14 repos (clean), and filed the tool defect (.github#71) — which was
then fixed by a *cloud* Claude session while the local one reviewed and merged
the fix (.github#74: "refuse to silently delete live required checks"). Two
more defects fell out of the same sweep: the deadlock-guard preflight sampled
only the single most recent PR (wrongly refusing 5 repos), and one refusal
aborted the whole sweep.

The rollout also shipped a bug of its own: all 13 external adoption PRs went
red because the shared reusable resolved its tooling checkout from
`github.workflow_ref` — the **caller's** ref, not the reusable's. A first
race-theory diagnosis was tested and killed by evidence before the real bug
was found and fixed (shared-workflows#30), turning 14 repos green within a
minute. And the evening delivered the payoff: the brand-new gates held
solidago#155 out of main when an "environment grants nothing" cleanup broke
OIDC on the PR plan — the first live save by the checks shipped hours earlier.

---

## Timeline

| Time | Event |
|---|---|
| 15:34 | 13 docs-check adoption PRs batch-opened fleet-wide; all external runs red: `couldn't find remote ref refs/pull/N/merge` |
| 15:38–15:43 | Race theory tested (merge refs exist; re-runs still fail) — theory killed |
| 15:43 | Real bug: `workflow_ref` resolves to the caller; fix is `job_workflow_ref` (shared-workflows#30, merged directly to unblock 14 red PRs — a disclosed deviation from let-checks-gate) |
| 15:45 | All 14 callers green within a minute |
| 15:50 | `--require-checks` sweep runs; preflight wrongly refuses 5 repos (samples one PR); one refusal aborts the sweep |
| 15:58 | **The stomp found**: "One regression I caused… the apply replaces the rule wholesale, so `Compile and commit` was dropped" |
| 15:58–16:01 | Check restored live + codified (.github#70); 14-repo audit finds no other drops |
| 16:02 | Tool defect filed (.github#71) |
| ~16:20 | A cloud Claude works #71 on its own branch; local session reviews, verifies the refuse-to-delete property against live, merges .github#74 (16:40) |
| 18:44–18:57 | solidago#155: env-scoping cleanup breaks OIDC on the PR plan; **auto-merge correctly holds** (required `gate` red); PR closed unmerged, corrected sequence filed as #156. The coupling was documented in the repo's own CLAUDE.md — queried APIs, didn't read the doc |

---

## What did NOT happen

- **The weakened gate was never exploited** — the window was minutes, on one
  repo, with no merges through it.
- **No other repo lost a check**: the immediate 14-repo audit proved the stomp
  was singular before the rollout continued.
- **Main was never touched by the #155 near-miss** — that's the new gates
  doing their job the same day they shipped.

## CTO lessons

1. **Replace-semantics tools must refuse to subtract silently.** A
   settings-as-code apply that PUTs wholesale will eventually delete live
   state its JSON never knew about — the exact live-vs-code stomp the fleet's
   discipline exists to prevent, committed by the discipline's own tool.
   "Refuse to silently delete live required checks" (.github#74) is now the
   tool's contract; the same review question applies to every declarative
   apply in the fleet.
2. **Kill your first theory with evidence before acting on it.** The race
   diagnosis was plausible, testable, and wrong — and it was *tested*, which
   is why the real bug was found in four minutes instead of after a batch of
   pointless re-runs.
3. **Preflight guards need representative samples.** A deadlock guard that
   looks at one PR refuses healthy repos and (worse) teaches operators to
   override it. Guards earn trust by being right.
4. **Read the repo's own context file before touching its couplings.** The
   #155 near-miss was documented in solidago's CLAUDE.md all along. APIs
   answer the question you asked; docs answer the one you should have.

---

## Sources

Session `3c927161` (2026-07-25, `~/repos`/`~/repos/dotgithub`), cloud branch
`claude/issue-71-20260725-2019`; .github#68/#70/#71/#74;
shared-workflows#28/#29/#30; the 13 adoption PRs (betula#97 … solidago#152);
solidago#155 (closed unmerged)/#156; `required-checks.json` NOTE dated
2026-07-25.
