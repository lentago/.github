# Incident Digest — GitHub's immutable OIDC subjects break a launch-day deploy pipeline, 2026-07-17

*The fleet's OIDC trust pattern assumed subjects are spelled with names.
GitHub started issuing them with numbers — but only for new repos, so every
existing pipeline kept working while the brand-new one failed on launch day.*
Compiled 2026-08-12 from a multi-session transcript harvest, cross-checked
against GitHub and AWS ground truth. All times **America/New_York (EDT, UTC-4)**.

---

## TL;DR

On pondviewlane.com launch day (2026-07-17), the freshly created
`site-pondviewlane-com` repo's first deploys failed at AWS OIDC auth
(`Not authorized to perform sts:AssumeRoleWithWebIdentity`) despite the
dual-trust PR (solidago#132) being applied and verified live. The first theory
— an STS propagation race — was wrong; a re-run failed identically. A throwaway
debug workflow captured the actual token claim and found the root cause:
**GitHub now forces immutable numeric-ID subject claims on freshly created
repos** (`repo:lentago@297986315/site-pondviewlane-com@1304395322:…`), a form
no fleet trust policy anticipated — and the repo-level
`use_immutable_subject=false` opt-out API accepted the PUT without changing the
behavior. Fix: solidago#133 added the immutable-form trust entry; deploys went
green ~20 minutes after the first failure. The debug commit was then removed
from the minutes-old repo's history deliberately and disclosed.

The same trap bit again on 07-25 in a different guise — removing a job's
`environment:` also rewrites the subject claim (solidago#155, caught pre-merge
by required checks) — confirming this is a *class*: the OIDC subject is a
composite of platform state, and anything that changes its inputs silently
breaks trust.

---

## Timeline

| Time | Event |
|---|---|
| 17:19 | First deploy of the new repo fails at "Configure AWS credentials" |
| 17:20 | Theory 1: STS/IAM propagation race; wait and re-run |
| ~17:23 | Re-run fails identically — race theory dead |
| 17:25 | Debug workflow pushed to the new repo captures the live token: immutable numeric-ID subject form |
| 17:28 | `use_immutable_subject=false` PUT applied at repo level — accepted, but the token keeps its immutable form |
| 17:31 | solidago#133: immutable-form subject added to the trust policy; applied |
| ~17:39 | Deploy green end-to-end |
| 17:32–17:55 | Debug commit removed via reset + force-with-lease on the minutes-old, unprotected repo (disclosed history hygiene, nothing else discarded); the old repo's redundant deploy workflow frozen to remove a two-repos-push-one-ECS-service race |

---

## What did NOT happen

- **The launch was not delayed.** The site went live the same evening; total
  auth downtime was ~20 minutes on a repo minutes old, with zero users.
- **No trust was over-granted.** The fix added the one immutable-form subject,
  not a wildcard; the debug workflow read claims, not secrets.
- **The force-push discarded only the throwaway debug commit** — verified
  before the reset, on an unprotected repo with no other contributors.

## CTO lessons

1. **Platform defaults drift underneath IaC patterns.** The fleet's trust
   policies encode an assumption ("subjects are name-spelled") that GitHub
   changed for new repos only — so the pattern kept passing everywhere it was
   already deployed and failed exactly where it was newest. New-repo bring-up
   checklists must include capturing a real token's claims, not assuming the
   pattern.
2. **When auth fails on something brand-new, read the actual claim.** One
   debug workflow ended a theory cycle that had already burned two runs. The
   claim is ground truth; everything else is inference.
3. **An opt-out API that accepts your PUT is not an opt-out.** The
   `use_immutable_subject=false` setting changed nothing for this repo;
   behavior, not acceptance, is the verification.
4. **The subject claim is a composite** — org identity, repo identity, ref,
   *and* job environment (as 07-25 proved). Treat any change to its inputs as
   a trust-policy change and stage dual-trust first. Recorded in memory
   `oidc-immutable-subject-claim.md`.

---

## Sources

Session `22faf8d8` (2026-07-17, `~/repos` multi-cwd); solidago#132 (merged
21:16Z), #133 (merged 21:33Z); failed run 29614401857; solidago#155/#156
(07-25 recurrence); pondviewlane launch PR solidago#135.
