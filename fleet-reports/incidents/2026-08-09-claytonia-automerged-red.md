# Incident Digest — Auto-merged red: a dropped brace, a non-required check, and four minutes of broken main, 2026-08-09

*Two parallel PRs appended tests to the same file. The rebase resolution
dropped one closing brace, the test suite died at parse — and the PR merged
anyway, because the check that failed was never in the required set.*
Compiled 2026-08-12 from a multi-session transcript harvest, cross-checked
against GitHub ground truth. All times **America/New_York (EDT, UTC-4)**.

**Deployment-caused:** yes

---

## TL;DR

During the myosotis visibility-layer work, claytonia PRs #86 and #87 both
appended tests to the tail of `test/context-ledger.bats`. After #87 merged,
#86 was rebased; the predicted conflict was resolved by deleting the markers
to "keep both sides" — but git had commonized the shared trailing `}` of the
two sides, so the resolution **dropped one closing brace**. bats died at parse
(`syntax error: unexpected end of file`). The governance finding is the second
half: **PR #86 auto-merged anyway with `queue-core` failing**, because
`queue-core` is not a *required* status check on claytonia — the fleet's
"required checks live on all 15 repos" posture (2026-07-25) is a per-context
claim, and this context wasn't in the map. Main carried a broken test suite
for ~4 minutes until the one-character fix-forward (#88) merged green at
39/39. The session adopted manual gating on `queue-core` for the rest of the
evening and flagged a fleet-ops required-checks pass. The same evening
provided the control group: music-curator's *required* `integrity` check
correctly held a failing PR open until fixed.

---

## Timeline

| Time | Event |
|---|---|
| ~16:45 | #87 (Loki emitter) merges; #86 (ledger-report CLI) rebased onto it |
| ~16:50 | Conflict at the bats-file seam resolved by stripping markers; the shared trailing brace is lost in the resolution |
| 16:52 | **Discovery moment**: check run shows `queue-core fail … MERGED` — the PR auto-merged red |
| 16:52–16:56 | Main red: bats parse error, `setup_file failed`, 16 of 39 tests unreachable |
| 16:55 | Fix-forward PR #88 (restore the closing brace) up, parse verified locally; armed — and manually gated on `queue-core` this time |
| 16:56 | #88 merges green, 39/39 |
| 16:58 | Post-mortem in-session: mechanism + "it auto-merged red anyway because `queue-core` isn't a *required* status check" |
| 22:10 | Contrast case: music-curator's required `integrity` check holds PR #76 open on failure until fixed — the correct behavior claytonia lacked |

---

## What did NOT happen

- **No runtime impact.** The broken file was the test suite; the workers and
  queue never saw it. Blast radius was CI truthfulness on main for ~4 minutes.
- **The failure did not hide.** The very next check-run read surfaced it; the
  fix was one character and merged within four minutes.
- **The fleet posture wasn't absent — it was incomplete.** Required checks
  exist on claytonia; this *context* wasn't among them. The map, not the
  mechanism, had the hole.

## CTO lessons

1. **"Required checks everywhere" is a per-context claim.** A new or renamed
   CI job does not inherit required status; it reports, fails, and gates
   nothing until added to the required set. Shipping a check and requiring a
   check must be one motion (fleet-ops `required-checks.json` + the preflight
   that proves the context reports).
2. **Auto-merge is exactly as safe as the required set.** An armed PR merges
   the instant the required subset is green — failing non-required checks are
   decoration. Arming a PR is an assertion that the required set covers
   everything you care about; if it doesn't, gate by hand (as the session did
   for the rest of the evening).
3. **Conflict-seam resolutions need a parse before push.** Git's merge
   machinery commonizes shared lines, so "keep both sides" can be subtractive
   at the seam. A syntax/parse pass on any hand-resolved file is cheap
   insurance — the failure here was findable locally in one second.
4. **The systemic answer shipped three days later**: the 08-12 fleet merge
   gate (owner/admin push allowlists on every main — see the companion entry)
   exists in part because this incident demonstrated the merge surface's
   remaining softness.

---

## Sources

Session `608b854e` (2026-08-09, `~`/`~/repos/claytonia`); claytonia#86 (merge
`4e6d7da`), #87, #88 (branch `fix/bats-seam-brace`); failing run 31335306592,
green run 31335496601; music-curator#76 (the control case).
