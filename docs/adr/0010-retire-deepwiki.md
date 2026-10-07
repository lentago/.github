# ADR-0010: Retire DeepWiki across the fleet

**Status:** Accepted (2026-10-07)

## Context

Since the 2026-07 brand-header round every public Lentago repo has carried
DeepWiki — Cognition's AI-generated wiki over public GitHub repos — on its front
door: an "Ask DeepWiki" badge in the generated header block, an "Ask this
codebase" section with good-first-questions, a "read this repo on DeepWiki"
clause in the canonical README footer ([`docs/voice.md`](../voice.md)), a
"DeepWiki ↗" sublink on each product row of the org profile, and
`deepwiki.com/lentago/<repo>` as the GitHub homepage of 17 repos
([`fleet-ops/repos.json`](../../fleet-ops/repos.json)). asclepias built its
first lab (Lab 00, "Ask the fleet") on it, and its ADRs 0001 and 0002 cite free
public indexing as one reason to keep the guide public and plain-Markdown. The
`devin-ai-integration` GitHub App that backs it has been installed org-wide
since 2026-07-04 with permissions well beyond what indexing needs (contents,
workflows, members).

Three months in it has not earned its place. The fleet's documentation is
written to be read directly — self-contained pages with stable headings — and
the grounded Ask surface the practice actually stands behind is mitchella's,
which checks live state before answering from documentation in git. Sending
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
- Lab 00 is gone, not stubbed. If a browser-only "question an AI about a
  working system, then check it" exercise is wanted again, it is rebuilt on
  mitchella once that has a public surface.
- One fewer org app with write-class permissions.
