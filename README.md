# .github — Lentago Labs org defaults and fleet governance

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/lentago/.github)

This is the Lentago Labs organization's special `.github` repository. It serves
two roles: GitHub reads org-level defaults from here, and it houses the
settings-as-code tooling that governs the rest of the fleet.

## Org profile

[`profile/README.md`](profile/README.md) renders as the organization profile page
at **[github.com/lentago](https://github.com/lentago)**.
[`profile/assets/banner.svg`](profile/assets/banner.svg) is its header.

## Community-health defaults

`CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, and `LICENSE` live at the
repo root and apply org-wide to any Lentago Labs repo that doesn't define its own.
Issue and PR templates are not yet set.

## Fleet governance

### [`fleet-ops/`](fleet-ops/)

Settings-as-code for the whole fleet.

- **`fleet-apply.sh`** — drift checker and enforcer. Verifies (and with `--apply`
  fixes) per-repo branch rulesets, required status checks, merge-button options
  (squash-only, auto-merge, delete-branch-on-merge), and the `lentago`+`claude`
  topic spine across all non-archived org repos.
- **`repo-ruleset.json`** — per-repo branch-protection ruleset template (PR
  required, squash-only, no force-push/deletion).
- **`labels.json`** — the Tidewater issue-label palette, applied with
  `--apply-labels`. Aligns color and description on the labels it names and
  never deletes the ones it doesn't.
- **`org-ruleset.json`** — org-level ruleset definition.
- **`required-checks.json`** — per-repo map of the status checks that must pass
  before merge.

### [`fleet-reports/`](fleet-reports/)

Periodically regenerated reports published in this repo.

- **`fleet-report.md`** — the weekly fleet report: open issues by repo, a 30-day
  merge/close activity snapshot, and an instruction-as-code language census. Auto-
  refreshed every Monday by a GitHub Actions workflow.
- **`incidents.md`** — the public incident register, linking to post-mortems under
  `fleet-reports/incidents/`. New reports are harvested from session transcripts
  via the local `/incident-digest` playbook.

### [`metrics/`](metrics/)

- **`generate-fleet-reports.py`** — generates both `fleet-report.md` and
  `incidents.md`.
- **`language-census.md`** — a periodic `cloc`-based language breakdown across
  all in-scope org repos.

### [`ci/`](ci/)

- **`validate.py`** — the check that gates PRs here. Asserts that `fleet-ops/*.json`
  match the shape `fleet-apply.sh` consumes, that `brand/generated/` is reproducible
  from `brand/fleet.json` rather than hand-edited, that the report generator's
  classifiers route known paths correctly, that relative markdown links resolve, and that
  `fleet-reports/incidents.md` is reproducible from its sources rather than
  hand-edited. Run it the way CI does: `python3 ci/validate.py`.

### [`brand/`](brand/)

Brand assets, and the generator that turns them into per-repo identity.

- **`avatars/`** — the Lentago Labs mark in SVG and PNG variants (square and
  circular, teal and limestone colourways).
- **`marks/`** — the 64-grid genus marks, one per fleet system, plus the
  lentago blossom that every other repo falls back to.
- **`fleet.json` + `generate.py`** — per-repo identity as config: emits each
  repo's README banner, badge row, and 1280×640 social-preview card into
  `brand/generated/`. `render.sh` rasterizes the cards with the real brand
  typefaces. Generated output is CI-enforced against hand-editing.

Social previews are the one surface with no API — they're uploaded per repo
under **Settings → General → Social preview**.

---

> Fleet CI *conventions* and the reusable workflows other repos call live in
> [shared-workflows](https://github.com/lentago/shared-workflows), not here. The
> workflows under `.github/workflows/` are this repo's own — they gate its PRs and
> refresh the fleet reports.

---

*Built in collaboration with [Claude](https://claude.ai) (Anthropic) — directed and reviewed by an infrastructure operator, not a software engineer.*
