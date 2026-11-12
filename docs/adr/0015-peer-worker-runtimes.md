# ADR-0015: Peer worker runtimes run behind the queue contract, and every runner PR names the runtime that wrote it

**Status:** Proposed (2026-11-12). Records the decisions the maintainer made on
2026-11-01 for [claytonia#166](https://github.com/lentago/claytonia/issues/166)
(judgments A–D and the code-review decisions), and the disclosure strings and
label question that judgment D handed to this repository
([#317](https://github.com/lentago/.github/issues/317)).

## Context

- **The bullpen.** claytonia's workers take jobs from a queue on the NAS, work
  them in a clean checkout and open pull requests as the runner App
  (`lentago-claude-runner[bot]`). Until November 2026 every job ran Claude Code.
  [claytonia#47](https://github.com/lentago/claytonia/issues/47) says the queue
  contract is the product and Claude Code is one runtime behind it. A second
  runtime is the proof.
- **Two peers, built and gated.** claytonia#166 adds Gemini CLI and Codex CLI.
  Phase 0, the adapter seam, merged on 2026-11-02 with Claude jobs' `.meta` and
  raw output byte-identical before and after. Phase 1 passed its live gate on
  2026-11-04
  ([gate record](https://github.com/lentago/claytonia/issues/166#issuecomment-6642605354)):
  five documentation jobs per runtime on `claytonia`, each an in-scope PR that
  got the AI review. Phase 2, which includes disclosure, started on 2026-11-12.
- **What the PRs say today.** Claude Code writes its own disclosure: a
  `🤖 Generated with [Claude Code](https://claude.com/claude-code)` line at the
  end of the PR body, and a `Co-Authored-By: Claude <model> <noreply@anthropic.com>`
  trailer that GitHub links to Anthropic's `claude` account (for example
  [kalmia#276](https://github.com/lentago/kalmia/pull/276) and
  [monarda#38](https://github.com/lentago/monarda/pull/38)). The ten Phase 1
  PRs from Gemini CLI and Codex carried neither (for example
  [claytonia#221](https://github.com/lentago/claytonia/pull/221) and
  [claytonia#228](https://github.com/lentago/claytonia/pull/228)). The App
  authorship says an agent wrote them; nothing says which one.
- **The fleet's instructions name Claude.** Repo `CLAUDE.md` files and the fleet
  PR-workflow text ask for a Claude trailer. A Gemini or Codex agent that
  follows them would credit its commits to Claude.
- **A trailer's email picks the account.** GitHub links a `Co-Authored-By:`
  trailer to the account that owns its email address, so an address chosen by
  guess can credit a stranger. Checked on 2026-11-12 with GitHub commit search
  (`author-email:`) and the users and apps APIs:
  - `gemini-cli@google.com` links to an individual's personal account.
  - `noreply@google.com` links to an account named `a-googler` whose profile
    returns 404.
  - The `gemini` login is an unrelated organization (a cryptocurrency exchange).
  - The `gemini-cli` user account shows no owner, organization or profile.
  - `218312386+gemini-cli[bot]@users.noreply.github.com` links to
    `gemini-cli[bot]`, the bot of the `gemini-cli` GitHub App, which the
    `google-gemini` organization owns.
  - `noreply@openai.com` and `codex@openai.com` link to `codex`, whose profile
    names OpenAI and openai.com/codex.
- **Labels are enforced from here.** Org repo labels are Terraform-enforced from
  [`fleet-ops/labels.json`](../../fleet-ops/labels.json) on every org repo, so
  claytonia never creates a label live. The palette's `model:*` labels are
  routing inputs: they pick the tier `@claude` runs at.

## Decision

1. **The seam.** Claude Code is one runtime behind the queue contract, not the
   product.
   - `bin/run-job` gains one adapter per runtime (`bin/rt-<runtime>`). The job
     spec and the project registry gain one optional `runtime` key, defaulting
     to `claude`.
   - claytonia#47's acceptance test asks for no change to the dispatch spec. An
     additive, optional key whose absence means exactly today's behavior counts
     as no change.
   - Adding a runtime changes no line of an existing runtime's adapter (the
     fleet principle of 2026-07-04: adding a client must not touch existing
     clients).
   - Never-merge stays enforced by run-job code after the run, whichever runtime
     ran. Nothing here changes never-merge, the auto-merge policy or the review
     gate ([ADR-0013](0013-haiku-reviews-every-pr-coderabbit-retires.md),
     [ADR-0014](0014-merge-promise-humans-own-the-policy.md)).
2. **Gemini auth.** Vertex AI in an existing GCP project, through a
   least-privilege service account that holds only *Vertex AI User*. No new
   project.
3. **Codex auth.** An OpenAI API key. No ChatGPT seat login on workers.
4. **Worker shape.** Every worker carries every runtime. The poller does no
   capability matching.
5. **Disclosure is owned here.** This repository sets the PR footer, the commit
   trailer and any runtime label for every runtime. claytonia implements them
   ([claytonia#174](https://github.com/lentago/claytonia/issues/174)).
6. **The PR footer.** run-job's code, not the agent, writes one line at the end
   of every runner-App PR body after the run, whatever the runtime:

   > 🤖 Generated with [Gemini CLI](https://github.com/google-gemini/gemini-cli),
   > model `gemini-3.8-flash`, in [claytonia](https://github.com/lentago/claytonia) run `<runid>`.

   - The runtime's name and link come from this table:

     | `runtime` | Name | Link |
     | :-- | :-- | :-- |
     | `claude` | Claude Code | `https://claude.com/claude-code` |
     | `gemini` | Gemini CLI | `https://github.com/google-gemini/gemini-cli` |
     | `codex` | Codex CLI | `https://github.com/openai/codex` |

   - The model clause names the model the job asked for. It is dropped when the
     job named none, because the adapters then report no model.
   - A PR carries exactly one such line. On a Claude PR, run-job's line replaces
     the `🤖 Generated with [Claude Code](https://claude.com/claude-code)` line
     the agent wrote, rather than sitting beside it.
   - The line is best-effort, like run-job's other GitHub calls: a failed edit
     is logged and never changes the job's outcome.
7. **The commit trailer.** Each runtime's commits carry its own trailer. The
   run-job preamble names the running runtime and the trailer it should use, and
   that instruction overrides any repo `CLAUDE.md` or fleet text that asks for a
   Claude trailer.

   | `runtime` | Trailer | GitHub links it to |
   | :-- | :-- | :-- |
   | `claude` | `Co-Authored-By: Claude <model> <noreply@anthropic.com>` (Claude Code's own, unchanged) | `claude`, Anthropic's account |
   | `gemini` | `Co-Authored-By: Gemini CLI <218312386+gemini-cli[bot]@users.noreply.github.com>` | `gemini-cli[bot]`, the App bot owned by `google-gemini` |
   | `codex` | `Co-Authored-By: Codex <noreply@openai.com>` | `codex`, OpenAI's account |

   - A trailer's address links to the vendor's own account or to no account at
     all, never to a third party's. Before a runtime is added, its address is
     checked the way the Context records.
   - The footer is the disclosure run-job writes. The trailer depends on the
     agent following the preamble. Enforcement does not rely on the runtime
     obeying, so the footer is the record of which runtime ran when the two
     disagree.
8. **No runtime label.** No `runtime:*` label is defined. The footer and the
   trailer are the disclosure.
   - The footer and trailer already say which runtime wrote a PR, and the
     runner dashboard (drosera) splits jobs by runtime.
   - A descriptive `runtime:*` label beside the routing `model:*` labels could
     be mistaken for one that routes.
   - A label set would add three labels to every org repo for a feature that
     touches only runner PRs.
   - If someone later needs to filter PRs by runtime, the label set is defined
     in `fleet-ops/labels.json`, and run-job applies a label only where the repo
     already has it. The bullpen's projects outside the org are outside that
     Terraform.

## Alternatives

- **A separate run-job per runtime.** Rejected on claytonia#166. A copy would
  fork the preamble, the limit handling and the merge guard, and the copies
  would drift.
- **Capability matching in the poller, with workers specialized by runtime.**
  Rejected (judgment C).
- **A new GCP project for the bullpen's Gemini use.** Rejected (judgment A).
- **A ChatGPT seat login for Codex on workers.** Rejected (judgment B).

  The record on claytonia#166 gives the three choices above without further
  reasons, so none is added here.
- **Let each agent write its own footer, as Claude Code does.** Rejected. The
  Phase 1 PRs show that Gemini CLI and Codex write none, and a disclosure the
  agent may skip is not one the fleet can promise.
- **Guess each vendor's address for the trailer.** Rejected. Two of the obvious
  Google addresses link to accounts Google does not visibly own.
- **A fleet-wide `runtime:*` label set.** Not adopted, for the reasons in
  Decision 8. It stays available if a need appears.

## Consequences

- claytonia#174 builds the footer and the preamble attribution with the strings
  above. It consumes this record and is not part of it.
- Several surfaces still say the fleet's code is co-written with Claude, and
  none of them changes here:
  - the org profile and `CONTRIBUTING.md`'s "co-written with Claude" passage
    (`CONTRIBUTING.md`'s attribution rule already says the trailer names the
    agent, and needs no change);
  - this repository's footer-attribution branding invariant in `CLAUDE.md`;
  - the fleet's co-authorship-disclosure convention in
    `shared-workflows/CLAUDE.md` and its `~/repos/CLAUDE.md` mirror.

  A follow-up issue owns them.
- Each vendor credential can be spent by any job on any worker (claytonia
  ADR-0010's consequence). Both keys carry a $25-a-month cap, decided on
  2026-11-04 on claytonia#166.
- **Revisit** when someone needs to filter PRs by runtime (Decision 8), when a
  vendor's own co-author convention changes or one of the linked accounts
  changes hands (Decision 7), or when a runtime is added: it takes a row in both
  tables, with its address checked first.
