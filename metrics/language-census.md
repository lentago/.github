# Lentago Labs Language Census

A periodic census of the programming/markup/config languages represented across
the **Lentago Labs org repositories**, ordered by prominence (lines of code). This
file is meant to be **regenerated periodically** — see
[Regenerating](#regenerating) for the exact, reproducible command, and log each
refresh in the [Update log](#update-log).

> **Scope.** The **active** repositories of the `lentago` org: those that
> `gh repo list lentago --no-archived` returns (25 on 2026-11-19), measured from
> fresh clones of each repo's default branch. This replaces the earlier rule of
> measuring whichever clones sat in the maintainer's `~/repos` tree and matching
> `origin` against `github.com/lentago/`: that tree holds clones on in-flight
> feature branches, and a fresh clone is the repo as published. Personal repos
> under `cpitzi/` (including `reference-checker`, `music-curator` and
> `myosotis`, all outside the org) and archived repos are **excluded**.
> Generated artifacts and vendored dependencies are excluded (see
> [Methodology](#methodology)). Each repo is measured on its own, so a file
> that exists in several repos (the `uvularia` template and demo repos share
> code, as do the mirrored `CLAUDE.md` files) is counted once per repo.
>
> **Repos in scope (25):** `asclepias`, `betula`, `brasenia`, `claytonia`,
> `.github`, `drosera`, `epigaea`, `kalmia`, `lupinus`, `mitchella`, `monarda`,
> `osmunda`, `repo-template`, `shared-workflows`,
> `site-icecreamtofightwith-com`, `site-lentago-dev`,
> `site-pondviewlane-com`, `solidago`, `uvularia`, `uvularia-demo-ask-rules`,
> `uvularia-demo-records`, `uvularia-demo-site`, `uvularia-records-template`,
> `uvularia-rules-template`, `uvularia-site-template`.
>
> Membership churn since the 2026-08-30 census: `uvularia` and its six template
> and demo repos joined (born 2026-10-03, ADR-0009); `music-curator` left the
> org for the personal account on 2026-10-13 (.github#264), taking its two
> Spotify exports and its credits and inventory JSON with it; the three
> archived repos (`office-presence`, `site-pitzilabs-dev`,
> `workstation-bootstrap`) now carry `cjpitzi` origins and are out of scope;
> `coderabbit` was archived on 2026-10-29. Archived repos were frozen out of the
> active-only `fleet-reports/fleet-report.md` already; the census now matches.

---

## Last updated: 2026-11-19

**Headline:** the census changed shape when `music-curator` left the org.
Its two Spotify exports and credit/inventory JSON were most of the data
weight; with them gone, JSON fell from ~53% to ~23% and CSV disappeared, and
Markdown (~27%) now leads. Python is third at ~22% and has grown nearly tenfold since
July (5,219 to 48,331 lines), driven by `brasenia` and the `uvularia` family.
Code that executes (Python, Terraform, Shell, the JavaScript family, Astro,
Jinja, TypeScript) is now ~36% of the fleet, ahead of Markdown and well ahead
of the JSON.

### By lines of code

Tool: `cloc 2.06`, over **git-tracked files only** (see Methodology). Total:
**224,154 lines of code** across **2,738 unique files**.

| # | Language | Code | Comment | Blank | Files | Share of code |
|---|----------|-----:|--------:|------:|------:|--------------:|
| 1 | Markdown | 60,126 | 288 | 16,673 | 813 | 26.8% |
| 2 | JSON | 51,196 | 0 | 6 | 476 | 22.8% |
| 3 | Python | 48,331 | 10,560 | 11,421 | 322 | 21.6% |
| 4 | YAML | 21,262 | 7,023 | 2,131 | 375 | 9.5% |
| 5 | HCL / Terraform | 10,176 | 3,935 | 2,054 | 150 | 4.5% |
| 6 | Shell (Bourne + Bash) | 9,588 | 3,809 | 1,278 | 119 | 4.3% |
| 7 | JavaScript | 4,847 | 1,290 | 551 | 46 | 2.2% |
| 8 | Text | 4,672 | 0 | 1,710 | 230 | 2.1% |
| 9 | HTML | 4,440 | 17 | 102 | 36 | 2.0% |
| 10 | Astro | 3,730 | 426 | 300 | 48 | 1.7% |
| 11 | CSS | 1,611 | 414 | 164 | 11 | 0.7% |
| 12 | JSX (React) | 1,232 | 105 | 67 | 12 | 0.5% |
| 13 | Jinja Template | 1,211 | 945 | 195 | 35 | 0.5% |
| 14 | TypeScript | 827 | 495 | 156 | 33 | 0.4% |
| 15 | XML | 623 | 7 | 39 | 7 | 0.3% |
| 16 | TOML | 252 | 332 | 55 | 21 | 0.1% |
| 17 | Dockerfile | 17 | 43 | 11 | 3 | 0.01% |
| 18 | BrightScript | 13 | 0 | 0 | 1 | 0.006% |

(`cloc` splits Shell into "Bourne Shell" 6,808 + "Bourne Again Shell" 2,780;
folded above.)

### Programming / scripting languages only

Stripping docs (Markdown, Text), data (JSON, XML), config (YAML/TOML), and
markup (HTML/CSS), the code that actually executes ranks:

| # | Language | Code |
|---|----------|-----:|
| 1 | Python | 48,331 |
| 2 | Terraform / HCL *(infra-as-code)* | 10,176 |
| 3 | Shell / Bash | 9,588 |
| 4 | JavaScript family (JS + JSX) | 6,079 |
| 5 | Astro | 3,730 |
| 6 | Jinja Template | 1,211 |
| 7 | TypeScript | 827 |
| 8 | BrightScript | 13 |

### Notes

- **JSON fell by 88k lines and still leads the data** — `music-curator`'s
  credits and inventory exports (104,513 lines at the last census) left with
  the repo. What remains is `drosera`'s Grafana dashboard JSON (20,059),
  `epigaea`'s HA registry snapshots (17,594) and `uvularia` (3,877), about 81%
  of the total. CSV is gone entirely: it was only the two Spotify exports.
- **Python is the new executing spine** — 9,784 lines at the last census,
  48,331 now. `brasenia` holds 10,820 and `uvularia` 9,701; the
  `uvularia-records-template` and `uvularia-demo-records` repos each carry
  4,506 lines of the same records code, counted once per repo (see Scope).
  Without that duplication Python would still be roughly 43,800 lines.
- **Shell no longer leads, and no longer ranks with Python** — it held first
  place in August; it is now third among executing code at 9,588 lines, behind
  Python and Terraform. `claytonia` holds the most (3,549).
- **Markdown now leads** — 60,126 lines, up from 49,195, while the file count
  fell from 1,051 to 813; the scope change (`music-curator` and the three
  archived repos out, seven `uvularia` repos in) moved both numbers, so the
  two are not a like-for-like trend. The largest holders are this repo (8,652),
  `site-icecreamtofightwith-com` (6,995) and `uvularia` (6,693).
- **HTML rose from 2,947 to 4,440 lines** — `epigaea` (2,143) and this repo
  (1,998) hold most of it. Still mostly output-like, not hand-authored markup.
- **The web-stack double count is retired** — `site-pitzilabs-dev` (archived) is
  out of scope, so the JS/JSX/Astro/CSS figures no longer count both it and its
  successor `site-lentago-dev`.
- **Shell is again the most-commented** — 3,809 comment lines against 9,588 of
  code (~40%), with Python at ~22% (10,560 against 48,331). Both are consistent
  with ops code written to be audited; the Python ratio dilutes as repos like
  `uvularia` and `brasenia` bring much code with little commentary.

---

---

## Methodology

Membership rule: a repo is in scope iff `gh repo list lentago --no-archived`
returns it. Measure fresh clones of each default branch, not the working
clones in `~/repos`, which sit on feature branches and carry other sessions'
uncommitted work. Use `cloc` 2.06. Exclusions, and why:

- **VCS / dependencies / build output:** `.git`, `node_modules`, `.venv`, `venv`,
  `__pycache__`, `dist`, `build`, `.next`, `vendor`, `target`, `.terraform`,
  `.astro` (build cache), and `package-lock.json` (generated lockfile).
- **Generated artifacts:** `*/wiki-site/site/*` (MkDocs-rendered HTML) and
  `*/.playwright-mcp/*` (Playwright accessibility snapshots) — both belong to
  out-of-scope personal repos now, but the excludes are kept for safety.
- **Untracked and gitignored files, categorically** — the census counts
  **git-tracked files only** (`cloc --vcs=git`, per repo). Earlier cycles scanned
  the raw working tree and patched around the consequences one directory at a time:
  the `archive` exclude exists because dotgithub's gitignored portfolio mockup was
  adding ~2,144 HTML lines. That approach does not hold. At the 2026-07-25 refresh
  an untracked personal Spotify export sitting in `music-curator/data/` measured
  **1.6 million JSON lines** — nineteen times the entire previous census — and a
  working-tree scan would have published it as fleet source. Scanning what git
  tracks is the durable form of the same intent: a file no repo carries is not part
  of the fleet's code, whatever happens to be on the maintainer's disk.
- **Binary / asset extensions:** `docx, png, pdf, woff2, psd, jpeg, jpg, gz, svg, map`.

`cloc`'s default skipping of byte-identical duplicate files is kept on purpose —
that's what dedups the mirrored `CLAUDE.md` / PR-workflow text.

### Regenerating

```bash
# Fresh clones of every active org repo's default branch, in a scratch dir.
mkdir -p "$SCRATCH/clones" && cd "$SCRATCH/clones"
for r in $(gh repo list lentago --no-archived --limit 100 --json name -q '.[].name'); do
  gh repo clone "lentago/$r" "$r" -- --depth 1 -q
done

# --vcs=git resolves the file list per repo, so cloc must be run inside each one
# and the per-language totals summed. This is why it is a loop, not one cloc call.
# --timeout 0 matters: the default 10 s per-file limit aborts a repo's JSON
# (drosera's alerts.tf did, 2026-11-19) and silently drops that repo from the sum.
for d in .github */; do d="${d%/}"
  ( cd "$d" && cloc . --vcs=git --quiet --json --timeout 0 \
      --exclude-dir=.git,node_modules,.venv,venv,__pycache__,dist,build,.next,vendor,target,.terraform,.astro,.playwright-mcp,site,archive \
      --fullpath --not-match-f='package-lock\.json' \
      --exclude-ext=docx,png,pdf,woff2,psd,jpeg,jpg,gz,svg,map > "$SCRATCH/out/${d#.}.json" )
done
```

Sum the per-repo JSON by language (`code`, `comment`, `blank`, `nFiles`), skipping
the `header` and `SUM` keys. Note `--vcs=git` also means a file staged but never
committed is out of scope, which is intended.

Then update the table, the "Last updated" date, and add a row to the log below.
(`cloc` install: fetch the pinned v2.06 script and verify its sha256, as
`fleet-reports.yml` does. The apt archive's 1.98 drops `.astro` and Jinja files.)

---

## Update log

| Date | Total LOC | Files | Notes |
|------|----------:|------:|-------|
| 2026-06-17 | 114,713 | 1,054 | Initial census over the **full `~/repos` working tree** (22 dirs, incl. third-party + personal). Superseded same day. |
| 2026-06-17 | 76,388 | 519 | **Re-scoped to Lentago Labs org repos only** (14 repos). cloc 2.06. |
| 2026-06-29 | 88,063 | 589 | Refresh after the Lentago Labs rebrand. **+`lentagolabs-dev`** brought into scope (now 15 repos, alongside the legacy `pitzilabs-dev` clone); **`archive/` excluded** as a gitignored local-only mockup that was adding ~2,144 HTML lines. cloc 2.06. |
| 2026-07-25 | 242,774 | 1,499 | **Methodology change — git-tracked files only** (`cloc --vcs=git`), so totals are NOT comparable with rows above. Prompted by an untracked 1.6M-line personal Spotify export in `music-curator/data/` that a working-tree scan would have published as fleet source. Scope refreshed to 18 repos and the 2026-07-04 renames picked up (the list derives from remotes; it had just not been rerun). +`brasenia`, +`kalmia`, +`site-pondviewlane-com`. cloc 2.06. Closes .github#31. |
| 2026-08-30 | 262,696 | 1,821 | Scope 18 → **22 repos**: +`asclepias`, +`lupinus`, +`mitchella`, +`monarda`, +`osmunda` (the August wave); −`reference-checker` (out of the org since 2026-08-16, .github#146 — its committed HTML reports drop HTML from 7,628 to 2,947); `homeassistant-config`→`epigaea` rename picked up. Regeneration recipe updated for the owner-grouped `~/repos` layout (two-level walk); log rows reordered chronologically. cloc 2.06. |
| 2026-11-19 | 224,154 | 2,738 | Scope 22 → **25 repos**, now defined as `gh repo list lentago --no-archived` and measured from fresh default-branch clones rather than the `~/repos` working tree. +`uvularia` and its six template and demo repos; −`music-curator` (left the org 2026-10-13, .github#264: JSON 138,893 → 51,196, CSV gone); the three archived repos (`cjpitzi` origins) out. Total falls 262,696 → 224,154 on the scope change, not a decline. Added `--timeout 0` to the recipe after drosera's `alerts.tf` hit cloc's per-file limit. cloc 2.06. Refs .github#361. |
