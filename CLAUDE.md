# CLAUDE.md — .github (Lentago Labs org defaults)

> Read [README.md](README.md) for the repo's purpose and
> [profile/README.md](profile/README.md) for what renders publicly at
> github.com/lentago. This file is operational notes for Claude: what the
> artifacts are, the branding invariants, and how to regenerate the census.
> Fleet-wide rules (PR workflow, attribution) live in `~/repos/CLAUDE.md`
> (canonical: `shared-workflows/CLAUDE.md`) and are **NOT** restated here — this
> repo has no deviations from them.

## Persona — introduce yourself

When Claude initializes in this directory, open the first response with a brief
self-introduction as **Org Claude** — keeper of Lentago Labs's org-level GitHub
presence: the public profile that renders at github.com/lentago and the
org-wide community-health defaults that this special repo can supply to the
fleet. One sentence is plenty; don't make a meal of it.

(The fleet-wide steward at `~/repos` is **Repo Claude**, who works *across* every
clone. Org Claude is scoped to this one special repo — the org's front door.)

## What this repo is

`lentago/.github` is GitHub's **special org-defaults repository** (the local
clone dir is named `dotgithub`). It carries no *application* code — it's the
org's **meta-repo**: the content + branding GitHub surfaces org-wide, plus the
org-level operator tooling that governs the rest of the fleet.

- **`profile/README.md`** renders as the public org landing page at
  **github.com/lentago**. `profile/assets/banner.svg` is its header image.
- **Community-health defaults** — `CONTRIBUTING.md`, `SECURITY.md`, and
  `CODE_OF_CONDUCT.md` live at the repo root (seeded 2026-07-01, issue #18) and
  apply org-wide to any Lentago Labs repo that doesn't define its own.
  Issue/PR templates are still unset. Changing these is a fleet-wide change;
  confirm scope before editing. Security contact + CoC enforcement address is
  `chris@lentago.dev`.
- **`metrics/language-census.md`** is a periodically-regenerated report (see below).
- **`fleet-ops/`** — settings-as-code for the whole fleet: `fleet-apply.sh`
  (the merge-button/topic-spine/ruleset drift checker) plus the ruleset JSON.
  This is **Repo Claude's** fleet-governance tooling, housed in the org meta-repo
  because that's its natural home — and so it finally has version control. Run it
  from here: `dotgithub/fleet-ops/fleet-apply.sh`. See `fleet-ops/README.md`.
- **`archive/`** — local-only holding pen, **`.gitignore`d so it is never
  published**. Holds relocated scratchpads (e.g. the interactive Lentago Labs
  portfolio mockup) that embed Lentago lab LAN topology and therefore must not land
  in this **public** repo. Keep this dir out of git.

Note: only `profile/`, the root community-health files, `ISSUE_TEMPLATE/`,
`workflow-templates/`, and `FUNDING.yml` are special-cased by GitHub. The
`fleet-ops/` and `archive/` subdirs are ordinary directories GitHub ignores —
they don't affect what renders org-wide.

Two things that look like they'd belong here but **don't**: reusable CI
workflows live in the `shared-workflows` repo, and the fleet-wide PR workflow is
defined in the parent `~/repos/CLAUDE.md` mirror (canonical source:
`shared-workflows/CLAUDE.md`). Per fleet convention, **do not restate the PR
workflow here** — this repo has no deviations from it.

## CI — `ci/validate.py`

There's no build or test suite in the application sense — this is Markdown, one
hand-authored SVG, a Python generator and a shell tool. What CI asserts instead
are this repo's real invariants, via `ci/validate.py` (run it locally exactly as
CI does: `python3 ci/validate.py`):

| Check | Asserts |
|---|---|
| `configs` | `fleet-ops/*.json` parse and match the shape `fleet-apply.sh` consumes |
| `brand` | `brand/generated/` is reproducible from `brand/fleet.json` — the banners are copied verbatim into 15 repos, so a hand-edit forks the identity |
| `census` | `metrics/generate-fleet-reports.py` imports; its data/code and markdown classifiers route known paths correctly |
| `register` | `fleet-reports/incidents.md` is reproducible from `fleet-reports/incidents/` — it is generated, never hand-edited |

**Relative markdown links are not checked here.** That check lived in `validate.py`
until #66; it was promoted into the shared reusable (shared-workflows#28) and this
repo now calls it like the rest of the fleet. Two implementations of one check would
have drifted, with this repo gated by the staler copy. What remains in `validate.py`
is the set genuinely specific to this repo.

Three workflows gate PRs here, all **unconditional** (no `on:`-level path filter — a
path-filtered required check deadlocks every non-matching PR):

| Workflow | Context | What it runs |
|---|---|---|
| `.github/workflows/ci.yml` | `validate` | `ci/validate.py` |
| `.github/workflows/shellcheck.yml` | `shellcheck / shellcheck` | shared reusable over `fleet-ops/fleet-apply.sh` |
| `.github/workflows/docs-check.yml` | `docs-check / docs-check` | shared reusable, relative markdown links |

All are required on `main` via `fleet-ops/required-checks.json`, so `gh pr merge
--auto` arms here rather than merging on the spot.

Adding a check means adding it to `ci/validate.py` — and prove it can fail before
trusting it: break the thing deliberately, confirm a red run, restore. A check that
cannot fail is worse than no check, because it reads as coverage.

Still true, and not something CI can catch: the org profile only renders from
`profile/README.md` on the **default branch**, so profile changes aren't visible at
github.com/lentago until merged. Previewing the rendered Markdown and confirming the
banner displays remains a manual step.

## Branding invariants

The profile badges (shields.io), the banner, and the org avatar share one
palette — the Lentago Labs **"Tidewater"** system. Keep new badges/assets
consistent with it:

- Deep hero `#0e2b1a` → brand forest-teal `#1b4b2e`, anther gold accent
  `#E0A81C`, limestone `#f3f0e8`. Gold is an accent — **one element per region,
  never a fill**; text on a gold fill is dark `#241d08`, never white. (Canonical
  token values: `lentago/site-lentago-dev` → `BRAND.md` and
  `public/design-system/tokens/` — those win. The 2026-07 recolor warmed the
  original slate-teal toward green and replaced the copper accent with gold;
  don't reintroduce `#0e2b28` / `#1c4a44` / `#c2643c`.)
- Brand mark: the **blossom** (five limestone petals on teal contour outlines,
  gold-tipped stamens, a pale center, in a deep-teal chip) — the org avatar in
  `brand/avatars/`. It replaced the former benchmark disk in "Tidewater". The
  field-prompt glyph is the gold **▲** + `lentago`; **never** the retired
  `:>` / `$` / `>` prompt.
- Per-repo identity is generated, not hand-drawn: `brand/fleet.json` +
  `brand/generate.py` emit each repo's README banner, badge row, and social-preview
  card. See `brand/README.md`; `ci/validate.py`'s **brand** check fails on a
  hand-edited `brand/generated/`.
- Tagline: **"Production that shows up when the need does."** (carries over from
  the former Pitzi Labs — same business, same voice; only name/palette/mark
  changed).
- Footer attribution discloses Claude co-authorship (Anthropic), framed as
  operator-directed, not SWE-authored — preserve that framing in any rewrite.

## Regenerating the language census

`metrics/language-census.md` measures languages across Lentago Labs org repos. The
**scope rule** is mechanical: a repo is in scope iff its `origin` remote matches
`github.com/lentago/` — third-party clones and personal repos are excluded.

Critically, the regeneration command runs from the **fleet root `~/repos`**, not
from inside this repo, because it scans every sibling clone:

```bash
cd ~/repos
ORG_REPOS=$(for d in */; do d="${d%/}"; \
  git -C "$d" remote get-url origin 2>/dev/null \
    | grep -q 'github.com[:/]lentago/' && printf '%s ' "$d"; done)

# --vcs=git resolves the file list per repo, so cloc runs inside each one and the
# per-language totals are summed (skip the `header` and `SUM` keys).
for d in $ORG_REPOS; do
  ( cd "$d" && cloc . --vcs=git --quiet --json \
      --exclude-dir=.git,node_modules,.venv,venv,__pycache__,dist,build,.next,vendor,target,.terraform,.astro,.playwright-mcp,site,archive \
      --fullpath --not-match-f='package-lock\.json' \
      --exclude-ext=docx,png,pdf,woff2,psd,jpeg,jpg,gz,svg,map )
done
```

**`--vcs=git` is load-bearing, not a style choice.** `cloc` does not honor
`.gitignore`, so a raw working-tree scan counts whatever happens to sit on the
maintainer's disk. At the 2026-07-25 refresh an untracked personal Spotify export
in `music-curator/data/` measured 1.6 million JSON lines — nineteen times the whole
previous census — and would have been published as fleet source. Counting only what
git tracks is the durable fix; the per-directory excludes that predate it are kept
for belt and braces.

The full methodology (exclusions and why, `cloc`'s byte-identical dedup that
collapses the mirrored `CLAUDE.md` text) lives in the report's Methodology
section. When refreshing, update **all three** together: the table, the
"Last updated" date, and a new row in the Update log.

## Weekly fleet reports (automated)

`metrics/generate-fleet-reports.py` regenerates a single GitHub-rendered report,
**`fleet-reports/fleet-report.md`**, linked from the org profile under **Fleet in
numbers**. It has two parts from the fleet's public state:

- **Issues** — open issues by repo + a 30-day merge/close activity snapshot, from
  public GitHub metadata only. The public, auto-generated sibling of the LAN-only
  editorial report (the older `fleet-reports/2026-07-01-*.md` archive is the
  hand-written kind).
- **Code census** — a *re-cut* of the language census that counts `CLAUDE.md`-family
  instruction markdown (+ reference-checker prompt-programs) as natural-language
  code, and reports documentation / content / data separately. Distinct from the
  canonical `metrics/language-census.md`; the two intentionally differ.

Scope is the **active** `lentago` repos (archived repos are frozen and excluded;
GitHub's listing endpoints don't surface archived repos anyway). Regenerate with
`python3 metrics/generate-fleet-reports.py --out-dir .` (needs `git`, `gh`, `cloc`
**pinned to v2.06** — see below; an unpinned/older `cloc` silently drops `.astro`
and Jinja template files from the census instead of miscategorizing them, so a
local regen on a different `cloc` version will not match CI).

**Weekly automation:** `.github/workflows/fleet-reports.yml` runs the generator on
a schedule (Mondays) and opens an auto-merging refresh PR — reports overwrite in
place, git history is the archive. Because the org disallows `GITHUB_TOKEN` from
creating PRs, the workflow authenticates with a **fine-grained PAT** stored as the
repo secret **`FLEET_REPORTS_TOKEN`** (owner `lentago`, repo `.github`, Contents +
Pull requests: write). The generator's cross-repo reads work over the public repos
regardless of PAT scope. If the secret is missing the workflow fails fast with a
setup hint. Rotate/replace the token by resetting that secret.

**`cloc` is pinned to v2.06**, not installed from the runner's apt archive — `ubuntu-latest`
(noble) currently ships `cloc` 1.98, which doesn't recognise `.astro` or Jinja templates
and drops both from the census entirely rather than miscategorizing them (issue #78).
The workflow fetches the tagged `cloc-2.06.pl` release script and verifies it against a
recorded sha256 before installing it to `/usr/local/bin/cloc`. Bump the version pin (and
the checksum) deliberately, not via an archive upgrade, so CI and local regenerations stay
reproducible against each other.

## Incident register (the second periodic fleet report)

`fleet-reports/incidents.md` is the incident sibling of `fleet-report.md`: a
chronological register of post-mortems, linked from the org profile under **Fleet
in numbers**. The full write-ups live under `fleet-reports/incidents/` as
`<YYYY-MM-DD>-<slug>.md`, produced by the local **`/incident-digest`** playbook
(harvested from `~/.claude/projects/` session transcripts — they cannot be
generated in CI). The same `metrics/generate-fleet-reports.py` builds the register
by scanning that dir (title from the `# ` H1, summary from the first `## TL;DR`/
`## Summary` sentence); the weekly workflow refreshes `incidents.md` in place, and
a new report drops in via a local PR that runs
`python3 metrics/generate-fleet-reports.py --out-dir . --incidents-only` (a cheap
mode that needs neither `gh` nor `cloc`).

**Policy exception — incident reports are published verbatim.** Unlike
`fleet-report.md` (public metadata only, *"no homelab-internal detail"*), the
incident reports **deliberately keep their homelab-internal architecture detail**
(container IDs, Proxmox/`pct`/`root@pam`/`vzdump`, hostnames) — that specificity
*is* the CTO-methodology value, and this is a **public** repo by design (Chris's
call, 2026-07-13). The one hard line: **never** a credential, key, private IP-plus-
purpose map, or secret. When filing a new report, eyeball it for those before it
lands — that guard, not sanitising the architecture, is the review.
