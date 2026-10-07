# ADR-0010: Retire DeepWiki across the fleet

**Status:** Accepted (2026-10-07)

## Context

Since the 2026-07 brand-header round every public Lentago repo has carried
DeepWiki — Cognition's AI-generated wiki over public GitHub repos — on its front
door: an "Ask DeepWiki" badge in the generated header block
([`brand/generate.py` before this change](https://github.com/lentago/.github/blob/7c9d96189d8b80df6afe52121e97884187df7a58/brand/generate.py#L251-L255)),
an "Ask this codebase" section with good-first-questions
([solidago's README, for one](https://github.com/lentago/solidago/blob/74ff2b5fdbb0926a76d6cb99df08643e8e63abc7/README.md)),
a "read this repo on DeepWiki" clause in the canonical README footer
([`docs/voice.md`](../voice.md)), a "DeepWiki ↗" sublink on each product row of
the [org profile before this change](https://github.com/lentago/.github/blob/7c9d96189d8b80df6afe52121e97884187df7a58/profile/README.md),
and `deepwiki.com/lentago/<repo>` as the GitHub homepage of 17 repos
([`fleet-ops/repos.json`](../../fleet-ops/repos.json)). asclepias built its
first lab on it ([Lab 00, "Ask the fleet"](https://github.com/lentago/asclepias/blob/da611661dae73aaac8872a2ce15e2e0fd47916a1/labs/00-ask-the-fleet.md)),
and its ADRs [0001](https://github.com/lentago/asclepias/blob/da611661dae73aaac8872a2ce15e2e0fd47916a1/docs/adr/0001-dedicated-training-repo.md)
and [0002](https://github.com/lentago/asclepias/blob/da611661dae73aaac8872a2ce15e2e0fd47916a1/docs/adr/0002-plain-markdown-zero-cost.md)
cite free public indexing as one reason to keep the guide public and
plain-Markdown. The `devin-ai-integration` GitHub App that backs it has been
installed org-wide since 2026-07-04 with permissions well beyond what indexing
needs — contents, workflows, members — as the
[org's installed-apps page](https://github.com/organizations/lentago/settings/installations)
shows.

Three months in it has not earned its place. The fleet's documentation is
written to be read directly — [self-contained pages with stable headings](https://github.com/lentago/asclepias/blob/da611661dae73aaac8872a2ce15e2e0fd47916a1/CLAUDE.md) —
and the grounded Ask surface the practice actually stands behind is
[mitchella](https://github.com/lentago/mitchella)'s, which checks live state
before answering from documentation in git. Sending
readers to a third-party wiki that is neither of those things dilutes the
pitch, and keeps an app with broad org permissions installed for no return.

## Decision

Remove DeepWiki from every Lentago surface: the generated badge, the README
sections and footer clause, the org-profile badge, blurb, sublinks and step,
the 17 repo homepages (cleared, not replaced), asclepias Lab 00 (deleted; the
labs stay numbered from 01) and its day-one step, the solidago MCP
registration, and the local MCP server. Uninstall the `devin-ai-integration`
app from the org.

Historical records keep their mentions: the ADRs that cite DeepWiki as context
at the time (asclepias 0001, 0002, 0005; this repo's
[0008](0008-pro-bono-practice-one-reader.md)), the generated fleet reports, and
the archived repos. This ADR supersedes them on that one point; their other
reasoning stands.

## Consequences

- The canonical footer in [`docs/voice.md`](../voice.md) now ends at the
  org-profile link. Each repo swaps to it in the per-repo sweep tracked on
  [#237](https://github.com/lentago/.github/issues/237).
- Where the practice promises "ask the codebase", it points at mitchella.
  asclepias keeps its *AI-queryable docs by default* pattern — docs structured
  so an answer can be grounded in them — with mitchella as the thing doing the
  answering.
- Lab 00 goes, not stubbed — deleted in the asclepias PR tracked on
  [#237](https://github.com/lentago/.github/issues/237). If a browser-only "question an AI about a
  working system, then check it" exercise is wanted again, it is rebuilt on
  mitchella once that has a public surface.
- One fewer org app with write-class permissions, once the uninstall on
  [#237](https://github.com/lentago/.github/issues/237) is done; it is a
  settings-page action with no API, so it is tracked there rather than here.
