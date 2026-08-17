# Incident Digest — Incidental context became recorded content: a personal-information overstep in a private wiki, 2026-08-01

*The operator mentioned a personal fact about third parties only so a name
would be spelled right. The agent recorded the fact itself — in prose and in a
pushed commit message — and scrubbing it required deliberately breaking the
repo's own history rules.*
Compiled 2026-08-12 from a multi-session transcript harvest. All times
**America/New_York (EDT, UTC-4)**. Details are deliberately generalized: the
repo is a private community wiki, and the incident is precisely about not
propagating personal information about private individuals — this entry
practices what it files.

**Deployment-caused:** no

---

## TL;DR

During roster corrections in a private community wiki, the operator mentioned a
personal life event concerning third parties, solely so their surname would be
recorded correctly. The session corrected the surname across sixteen files —
and **also recorded the life event itself** as a fact in the wiki *and twice in
the commit message* of a commit already pushed on an open PR branch. The
operator caught it within three minutes ("NEVER record personal information …
that is not [wiki]-related. Add to project instructions"). Remediation:
wiki prose scrubbed; then — because a commit message is as permanent as a
page — the pushed-but-unmerged branch was **rewritten and force-pushed**
(`--force-with-lease`), knowingly breaking the repo's "no force-push, no
amending pushed commits" convention, disclosed in the same turn; the PR body
carrying the fact forward was rewritten; a standing no-personal-information
rule was added to the repo's instructions; and an audit grep swept for any
other overreach (clean). The superseded commit remains resolvable only in the
local clone.

---

## Timeline

| Time | Event |
|---|---|
| ~20:09 | Roster correction requested; personal fact supplied as naming context |
| 20:12 | Surname corrected across 16 files — and the fact recorded in prose + commit message; commit pushed on the open PR branch |
| 20:15 | Operator catches it: "NO NO. … I ONLY mentioned it in service of a correct roster" |
| 20:16 | Scrub begins; audit grep for other non-wiki personal facts (marriage/medical/etc. patterns) — clean |
| 20:17 | The fact found in the pushed commit's message; decision to rewrite rather than leave it in the permanent record |
| 20:17–20:18 | Branch rewritten, force-pushed with lease; convention break disclosed unprompted ("a commit message is as permanent as a page") |
| 20:19 | PR body rewritten; standing rule committed to the repo's instructions |

---

## What did NOT happen

- **Nothing left the private repo.** The branch was unmerged, the repo is
  private with a single writer; the exposure was to the repo's own permanent
  history, not to any audience.
- **No other personal overreach existed** — the audit grep came back clean.
- **No collaborator history was harmed by the rewrite** — single-writer repo,
  unmerged branch, lease-protected push.

## CTO lessons

1. **Incidental context is not content.** Facts supplied *in service of* a
   task (a name, a date, a reason) are inputs, not material to record. For
   agents, personal information about third parties is radioactive unless
   recording it *is* the task — now a standing rule in that repo's
   instructions, and worth adopting as fleet doctrine for any repo that
   touches people.
2. **Redaction review includes commit messages and PR bodies.** The prose
   scrub alone would have left the fact in two places the wiki's readers never
   see but git never forgets. Any personal-info audit must sweep the full
   permanent record: tracked files, messages, PR text.
3. **Conventions need a documented exception path.** The no-force-push rule
   was correctly broken — leaving the fact in history would have defeated the
   correction — and the break was disclosed in the same turn. That is the
   right shape: rules bend for redaction, with disclosure, never silently.
4. **Codify the correction at correction time.** The standing rule landed in
   the same remediation window, which is why later sessions (the 08-09/08-10
   name-scrub PRs in the same repo family) inherited it instead of repeating
   the mistake.

---

## Sources

Single local session, 2026-08-01 evening (private repo; identifiers withheld
by design). Ground truth verified in the local clone: the forced-update range,
the superseded commit still resolvable locally, the rewritten PR, and the
standing rule in the repo's instruction file.
