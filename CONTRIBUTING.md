# Contributing to Lentago Labs

Thanks for stopping by. These are the org-wide defaults for every
[Lentago Labs](https://github.com/lentago) repository; if a repo has its own
`CONTRIBUTING.md`, that one wins.

## What these repos are

Lentago Labs is a pro-bono operations practice for organizations that run on
volunteers, donations, and one overworked tech person. Most repos here are our
own working estate — a homelab cluster, an AWS platform, and the tooling that
runs them — published because we practice what we publish: you can watch the
method working before you decide to use it. A few repos are kits built to be
copied into your own accounts.

That means these are not community projects with a roadmap looking for
maintainers. Contributions are very welcome; just size them accordingly. Small,
focused changes land easily. Big ones need a conversation first, and the
conversation is free.

The code is co-written with [Claude](https://claude.com/claude-code)
(Anthropic). The operator directs the work and owns every merge; Claude writes
most of the code. Each repo says so in its README.

## The most useful thing you can send us

A runbook that let you down. Which step, what you expected, what happened
instead. Adoption docs can only be tested by people adopting, so a "step 7
didn't work on my machine" issue is worth more than most code.

## How to contribute

1. **Open an issue first** for anything beyond a typo or doc fix. Work here is
   issue-driven, and a large PR that arrives with no issue is hard to review
   cold.
2. **Fork and branch.** Branch from `main`; keep branches short-lived. You do
   not need to be a member of anything — a fork is the front door.
3. **Keep PRs scoped.** One concern per PR. If you notice an adjacent problem,
   file it as its own issue rather than folding it in.
4. **Write a plain PR body** — what changed and why, for someone reading it
   months from now. Reference the issue (`Closes #N`).
5. **Squash merges only.** The PR body becomes the merge commit message, so
   branch commits can stay light. Required status checks gate the merge, and
   a human clicks it.

## Conventions

- **Voice:** reader-facing prose follows
  [`docs/voice.md`](docs/voice.md) — plain, friendly, written for the one tech
  person keeping an org running. Records (ADRs, incident reports) stay neutral.
- **Attribution:** commits authored or co-authored by an AI agent carry a
  `Co-Authored-By:` trailer naming it. Human contributors don't need one.
- **No secrets, ever** — no credentials, tokens, private keys, or LAN
  topology in code, config, tests, or fixtures. See [SECURITY.md](SECURITY.md)
  for reporting anything that slipped through.
- **License:** everything here is MIT unless a repo says otherwise. By
  contributing you agree your contribution is licensed the same way.

## Questions

Open a discussion or issue in the relevant repo, or email
**chris@lentago.dev**. Call when you need to, if you need to.
