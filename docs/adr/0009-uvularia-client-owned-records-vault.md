# ADR-0009: uvularia — a client-owned records vault with a grounded Ask box and a live compliance board, as three repos and three pipelines

**Status:** Accepted (2026-10-03)

## Context

The public-record pattern the practice has been pointing at as a receipt —
a fact base with per-page provenance, a grounded Ask box that answers only
from the records, privacy tripwires in CI — runs today as
`site-pondviewlane-com`. That site serves one specific community and is not
available as a reference, demonstration, or advertisement for the practice,
even at no cost. On 2026-10-03 its receipt link was removed from the org
profile ([#198](https://github.com/lentago/.github/pull/198)); the same link
on lentago.dev is pending removal. The practice therefore has an offering
with no receipt it can show.

Three open offering issues already depend on that pattern:
[#128](https://github.com/lentago/.github/issues/128) (Ask-the-Records kit:
generalize the pattern into a client-owned template),
[#130](https://github.com/lentago/.github/issues/130) (funder-report fact
pipeline: numbers committed once, cited everywhere), and
[#122](https://github.com/lentago/.github/issues/122) (Good-Standing Kit:
obligations-as-code with a standing panel). The lupinus adoption stories
(`guide/stories/03-stillwater-brook-watershed-alliance.md`) name the same
need from the reader's side.

The fleet already holds most of the parts, in separate repos that have never
been joined:

- **mitchella** has a corpus engine with a `wiki` loader that reads a
  Markdown tree in place, a four-outcome structured answer schema with a
  code-level citation gate, a signals-before-corpus incident rule
  (mitchella ADR-0001), whole-corpus-in-prompt behind one cache breakpoint
  (ADR-0002), no tools and no write access (ADR-0005), an append-only turn
  log, and a job that clusters unanswered questions into work orders. It has
  never made a live API call.
- **site-pondviewlane-com** has a library manifest with sha256 per source
  file, base-plus-overlay content with a facts-parity check, privacy
  tripwires, and an Ask widget. Its endpoint is a Lambda in solidago's paid
  hosting, uncached, with an in-memory rate cap and citations rendered from
  the passages sent rather than the ones cited.
- **theoria**, **essex-crossing-hoa**, and the **lupinus** ops vault share a
  Markdown-vault convention: relative links, minimal YAML frontmatter, one
  index page, explicit sources, one fact in one place, dated visible
  corrections, append-only journals, a tracked `.obsidian/` folder the repo
  does not depend on.
- **drosera** has a stdlib status-page builder that never shows a fake
  green, dashboards-as-JSON applied by Terraform, and HTTPS push into Grafana
  Cloud Loki, but no path from GitHub Actions into Loki.
- **monarda** has template delivery by "Use this template", an intake
  questionnaire mapped to one config file, and a timed dry-run with a receipt.

The reader (ADR-0008) is the one tech person at an organization with
**posting obligations**: a condo or HOA board, a nonprofit with a board, a
town committee under the Massachusetts Open Meeting Law, a land trust. They
must be able to add a record or correct one in minutes, with a small blast
radius, and must be able to show, live, that what had to be posted was
posted on time.

## Decision

1. **A new product, codename `uvularia`** (bellwort, a New England native;
   the bell is the announcement). It is the records layer: a client-owned
   vault that a grounded Ask box, a public site, an announcement feed, and
   later the funder-report and good-standing pipelines all consume.
   [#128](https://github.com/lentago/.github/issues/128) is retired into it.

2. **Three repositories per client, three pipelines, three blast radii**,
   all created in the client's own GitHub organization from templates:
   - `<org>-records` — the Obsidian-compatible vault. One record per file
     with provenance frontmatter; originals in `library/` with sha256;
     `obligations/*.yaml` declaring posting rules next to the records that
     satisfy them; `intake/` that is never built; `receipts/` that is
     append-only. CI validates schema, links, privacy tripwires, and
     obligations, and runs the golden question set read-only against the
     candidate corpus. Merge publishes a digest-named corpus bundle, a
     standing file, a feed, a receipt with a server-side timestamp, and a
     provenance attestation.
   - `<org>-ask-rules` — governance. The frozen instructions, the allowed
     subjects and refusal policy, the model pin and caps, a kill switch,
     manual incident overrides, and the golden evals. A PR must pass the
     evals against the currently published corpus. Versioned releases,
     pinned by the Ask function.
   - `<org>-site` — presentation only. Builds from the published corpus
     bundle, never from the vault checkout. Carries the Ask widget and the
     public "Is it posted?" board built from the standing file. Deploys to
     the client's GitHub Pages.

   A corpus change cannot alter a rule; a rule change cannot alter a fact;
   a site change cannot smuggle either.

3. **The Ask box is mitchella's engine**, with two new signal providers: one
   that turns any obligation in breach into an incident on that obligation's
   subjects, and one that surfaces active announcements. The box therefore
   cannot assert compliance the board denies. It runs as a function in the
   client's own cloud account, model pinned to the mid-tier, prompt caching
   on, key in a secret store, a durable daily cap, a bot check in front, and
   citations rendered only from ids the gate verified. Turn events go to the
   client's own Grafana Cloud free tier over HTTPS push.

4. **Visibility is two panes.** The public board on Pages has zero
   dependencies beyond the standing file. The operator pane is a drosera
   dashboard in the client's Grafana Cloud free tier, left to right: intake,
   reviewed, published, served, asked, with a stale-digest alert when the
   function is not serving what was published. Alerts open GitHub Issues
   first (ADR-0007's preferred runtime); Grafana alert rules are optional.
   The reusable Actions-to-Loki push step this requires is a drosera
   deliverable and drosera's first non-estate source.

5. **Phase 0 ships first and contains no AI**: the vault template, the
   validator, the obligation evaluator, Issue-form intake, publish receipts
   and attestation, the public board, an `ADOPTION.md`, and a timed dry-run.
   That phase alone satisfies the add-quickly, correct-quickly,
   low-blast-radius requirement and is where the Kit tier is earned. The
   Ask box (Phase 1), the operator pane (Phase 2), and the downstream
   consumers (Phase 3) attach to a vault that already works.

6. **The demonstration client is fictional and renameable by construction.**
   Stillwater Brook Watershed Alliance, from the lupinus stories, is seeded
   with two years of realistic public records. Its identity (name, short
   name, domain, contact, accent, logo) lives in exactly one file,
   `org.yaml`, consumed by the vault index, the site, the rules persona, and
   the obligation pack's organization fields. Seed records are **generated
   from templates by a seed script that reads `org.yaml`**, never
   hand-written with the name in them, so renaming or rebranding the demo
   is one edit and one re-run. CI fails on any occurrence of the
   organization's name outside `org.yaml` and the generated seed output. A
   real client starts from an empty vault; the seed is a demonstration and
   a lab fixture, not a starting point.

7. **Core and clients**, per the fleet principle. The core owns the record
   schema, the obligation schema, the bundle and standing and receipt
   formats, the validator, and the evaluator. The first clients are: GitHub
   Issue forms for intake, Obsidian as the editor, an AWS Lambda Function
   URL as the Ask runtime, GitHub Pages as the site host, Grafana Cloud via
   drosera as the operator pane, and Massachusetts as the first obligation
   pack. Adding a client never touches another.

8. **Boundaries.** Public records only in v1; the vault is public and the
   `visibility` field exists so a mistake fails CI rather than ships. Not
   legal advice; obligation packs encode posting mechanics and the
   disclaimer lives in policy. "Posted at" is the publish workflow's
   server-side time, never the author's commit time. No multi-tenancy
   (ADR-0007): one org, one set of repos, one function, one key.

## Alternatives

- **One repository with path-scoped reviewers.** Simpler to create, but
  GitHub rulesets and required checks are per-repo, so the three gates would
  share one ruleset and one reviewer set, and a corpus PR could carry a rule
  change. Rejected; the separation is the feature.
- **Generalize pondviewlane in place** (the shape of #128 as written). Its
  Ask endpoint lives in solidago's paid hosting, has no structured output
  or citation gate, and its privacy checks are tied to one HOA. Rejected in
  favour of mitchella's engine behind pondviewlane's content checks.
- **A vector store behind the Ask box.** mitchella ADR-0002 already decided
  whole-corpus-in-prompt with a documented step to keyword prefilter when a
  corpus passes the ceiling. Adopted as-is; the bundle carries an `archived`
  flag from day one so old records can leave the prompt without leaving the
  record.
- **Grafana as the compliance board.** Requires a login and a stack the
  reader may never set up. Rejected for the public board; kept for the
  operator pane.
- **A real community as the demonstration.** Not available, and would
  recreate the problem this ADR starts from. Rejected; the fictional client
  is renameable so that constraint never binds again.

## Consequences

- A new org repo `lentago/uvularia` is created from `repo-template` by the
  fleet Terraform on merge of this ADR, with the standard required check.
  It is registered as a bullpen project.
- [#128](https://github.com/lentago/.github/issues/128) is closed as
  superseded by the uvularia offering issue. [#130](https://github.com/lentago/.github/issues/130)
  and [#122](https://github.com/lentago/.github/issues/122) gain a stated
  dependency on the Phase 0 vault rather than on pondviewlane.
- mitchella gains two signal providers and a serverless packaging; its first
  live API call happens here. drosera gains an Actions-to-Loki step and a
  pipeline dashboard. solidago's `ask-lambda` module is hardened or
  superseded by uvularia's.
- The practice regains a receipt it can show for the public-record offering,
  on lentago.dev and the org profile, once Phase 0 is live for the
  demonstration client.
- The org profile and lentago.dev describe the public-record offering with
  this receipt and no other.
