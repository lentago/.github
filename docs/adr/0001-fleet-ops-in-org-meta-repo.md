# ADR-0001: Fleet governance tooling lives in the org `.github` meta-repo

**Status:** Accepted (2026-06-20; reconstructed 2026-08-13)

## Context

The fleet's governance tooling — the scripts and JSON that apply settings across
every Lentago Labs repo — began life as a loose directory in the operator's local
`~/repos` working root. It was never a repository: no history, no review, no CI, no
remote. A change to fleet-wide policy was an edit to an untracked file on one
machine's disk.

Meanwhile `lentago/.github` already had to exist. It is GitHub's **special
org-defaults repository**: the one repo GitHub reads org-wide for the public profile
(`profile/README.md` → github.com/lentago) and the community-health defaults
(`CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`) that any repo without its own
inherits. That repo was already versioned, already reviewed, already the org's front
door.

## Decision

**Fold the fleet-governance tooling into `lentago/.github`.** PR #4 ("Adopt fleet-ops
as versioned tooling in the org meta-repo", 2026-06-20) moved the loose `~/repos`
scripts under `fleet-ops/` in this repo — in the recorded phrasing, *"so it finally
has version control."*

This makes the repo deliberately **dual-role**:

- **GitHub reads it** for org defaults — profile, community-health files, and the
  other GitHub-special surfaces (`ISSUE_TEMPLATE/`, `workflow-templates/`,
  `FUNDING.yml`).
- **The fleet reads it** for settings-as-code — `fleet-ops/` (and later `terraform/`)
  govern the rest of the fleet from here.

`fleet-ops/` and `archive/` are ordinary directories GitHub ignores; only the special
surfaces above affect what renders org-wide. The two roles coexist without
interfering.

## Alternatives

- **Keep the tooling loose in `~/repos` (recorded — the prior state).** Rejected. It
  had no history, no reviewable diff, no CI to assert the JSON manifests parse, and it
  lived on exactly one machine. The whole point of the move was to end that.
- **A dedicated `fleet-ops` repo (retrospective — not considered at the time).**
  *Lateral.* It buys a cleaner separation of concerns — governance tooling would not
  share a repo with the public profile — but it costs one more repo to govern, and the
  `.github` repo has to exist anyway. The dual-role framing is documented rather than
  accidental, so the "separation" a split would buy is already legible from
  `CLAUDE.md`. A wash: worth doing only if the tooling grew large enough to warrant its
  own release cadence, which it has not.
- **Vendor the tooling into each repo (retrospective — not considered at the time).**
  *Worse.* Fleet-wide governance is inherently a one-place concern; copying it into 15
  repos is the exact duplication settings-as-code exists to eliminate, and every fix
  would need mirroring by hand.

## Consequences

- `lentago/.github` carries no application code but two distinct responsibilities;
  `CLAUDE.md` documents both (Org Claude for the profile/defaults face, Repo Claude for
  the fleet-governance face).
- The tooling is now versioned, reviewed, and CI-gated (`ci/validate.py` asserts the
  `fleet-ops/*.json` manifests stay well-formed).
- Later work — the `terraform/` module (ADR-0002) and the weekly reports — landed in
  the same repo for the same reason: it is the natural home for anything that governs
  the fleet as a whole.
