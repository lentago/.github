# Lentago Labs Language Census

A periodic census of the programming/markup/config languages represented across
the **Lentago Labs org repositories**, ordered by prominence (lines of code). This
file is meant to be **regenerated periodically** — see
[Regenerating](#regenerating) for the exact, reproducible command, and log each
refresh in the [Update log](#update-log).

> **Scope.** Only repositories whose `origin` remote is under
> `github.com/lentago/`. Measured over the maintainer's `~/repos` working tree,
> so it counts what's checked out locally for each org repo (not a GitHub API
> query). Third-party clones (`firewalla-mcp`, `firewalla-tools`) and the
> personal repo (`professional-endeavors`) are **excluded**, as are local-only
> scratch dirs that aren't git repos. Generated artifacts and vendored
> dependencies are excluded (see [Methodology](#methodology)); `cloc`
> additionally **deduplicates byte-identical files**, so the deliberately-mirrored
> `CLAUDE.md` / PR-workflow text is counted once, not once per repo.
>
> **Repos in scope (18):** `betula`, `brasenia`, `claytonia`, `.github`,
> `drosera`, `homeassistant-config`, `kalmia`, `music-curator`,
> `office-presence`, `reference-checker`, `repo-template`, `shared-workflows`,
> `site-icecreamtofightwith-com`, `site-lentago-dev`, `site-pitzilabs-dev`,
> `site-pondviewlane-com`, `solidago`, `workstation-bootstrap`.
>
> Six of those carry names that changed in the 2026-07-04 rebrand wave —
> `bullpen`→`claytonia`, `firewalla-axiom-pipeline`→`betula`,
> `foundry-platform-demo`→`solidago`, `ice-cream-book`→`site-icecreamtofightwith-com`,
> `lentagolabs-dev`→`site-lentago-dev`, `pitzilabs-dev`→`site-pitzilabs-dev`. The
> list is derived from remotes at regeneration time, so it tracks renames on its
> own; it had simply not been regenerated since. Three (`office-presence`,
> `site-pitzilabs-dev`, `workstation-bootstrap`) are archived but still cloned
> locally, and the membership rule is about the remote, not repo state — so they
> remain in scope, unlike the active-only `fleet-reports/fleet-report.md`.

---

## Last updated: 2026-07-25

**Headline:** data still dominates — JSON is ~56% and, with CSV, exported payloads
alone outweigh every line of executing code in the fleet combined. Markdown is
second at ~16%, which is the fleet's real character: it ships documentation and
instructions. The executing spine is now a near-tie between the JavaScript family
and Shell, with Terraform and Python close behind. Python has quadrupled since the
last census, on the back of `music-curator`'s productization and the report
generators in this repo.

### By lines of code

Tool: `cloc 2.06`, over **git-tracked files only** (see Methodology — this changed
this cycle and makes the totals non-comparable with earlier rows). Total:
**242,774 lines of code** across **1,499 unique files**.

| # | Language | Code | Comment | Blank | Files | Share of code |
|---|----------|-----:|--------:|------:|------:|--------------:|
| 1 | JSON | 135,512 | 0 | 6 | 56 | 55.8% |
| 2 | Markdown | 38,245 | 110 | 13,255 | 877 | 15.8% |
| 3 | CSV | 15,595 | 0 | 0 | 2 | 6.4% |
| 4 | Shell (Bourne + Bash) | 9,206 | 2,804 | 1,639 | 82 | 3.8% |
| 5 | YAML | 9,180 | 1,944 | 896 | 167 | 3.8% |
| 6 | HTML | 7,628 | 261 | 674 | 36 | 3.1% |
| 7 | HCL / Terraform | 5,749 | 1,743 | 1,201 | 101 | 2.4% |
| 8 | JSX (React) | 5,240 | 576 | 356 | 40 | 2.2% |
| 9 | Python | 5,219 | 1,854 | 1,284 | 40 | 2.1% |
| 10 | JavaScript | 3,992 | 702 | 426 | 20 | 1.6% |
| 11 | Text | 3,377 | 0 | 967 | 24 | 1.4% |
| 12 | Astro | 1,979 | 275 | 154 | 21 | 0.8% |
| 13 | CSS | 1,181 | 212 | 101 | 12 | 0.5% |
| 14 | TypeScript | 310 | 94 | 43 | 8 | 0.1% |
| 15 | Jinja Template | 277 | 0 | 48 | 6 | 0.1% |
| 16 | XML | 39 | 0 | 3 | 1 | 0.02% |
| 17 | Dockerfile | 18 | 42 | 15 | 4 | 0.01% |
| 18 | TOML | 14 | 5 | 3 | 1 | 0.01% |
| 19 | BrightScript | 13 | 0 | 0 | 1 | 0.01% |

(`cloc` splits Shell into "Bourne Shell" 8,196 + "Bourne Again Shell" 1,010; folded
above. "Text" was omitted as not-a-language in earlier cycles, when it was 14 lines;
at 3,377 it is now listed rather than silently dropped.)

### Programming / scripting languages only

Stripping docs (Markdown, Text), data (JSON, CSV, XML), config (YAML/TOML), and
markup (HTML/CSS), the code that actually executes ranks:

| # | Language | Code |
|---|----------|-----:|
| 1 | JavaScript family (JS + JSX) | 9,232 |
| 2 | Shell / Bash | 9,206 |
| 3 | Terraform / HCL *(infra-as-code)* | 5,749 |
| 4 | Python | 5,219 |
| 5 | Astro | 1,979 |
| 6 | TypeScript | 310 |
| 7 | Jinja Template | 277 |
| 8 | BrightScript | 13 |

### Notes

- **JSON leads but carries no logic** — it is `music-curator`'s credits and
  inventory exports, HA entity/device/dashboard registry snapshots
  (`homeassistant-config`), Grafana dashboard JSON (`drosera`), and
  `package.json`-style config. With CSV (two Spotify collection exports, 15,595
  lines) the exported-data share is ~62%. Discount it and the picture is Markdown
  documentation over a JS/Shell → Terraform/Python code base.
- **Markdown's file count is the real story** — 877 files against 56 JSON. The
  fleet's documentation surface is broad and hand-maintained, which is what makes
  the relative-link checker adopted fleet-wide in .github#57 worth its cost.
- **HTML is output, not source** — dominated by `reference-checker`'s committed
  `reports/*.html` (rendered analysis outputs); like JSON, treat it as data the
  repo carries rather than hand-authored markup.
- **The web stack is still double-counted**, though less than before. Both
  `site-pitzilabs-dev` (archived) and its successor `site-lentago-dev` carry
  `github.com/lentago/` origins and remain cloned locally, so the JS/JSX/Astro/CSS
  figures reflect both. They are not byte-identical, so `cloc`'s dedup does not
  collapse them. Deleting the archived clone locally is what retires that overlap.
- **Python has quadrupled** — 1,218 lines at the last census, 5,219 now. The
  growth is `music-curator`'s productization plus this repo's report generator and
  validator.
- **Shell remains the most-commented code in the fleet** — 2,804 comment lines
  against 9,206 of code (~30%), consistent with ops scripts written to be audited.

---

## Methodology

Membership rule: a repo is in scope iff its `origin` remote matches
`github.com/lentago/`. Run from the fleet root (`~/repos`) with `cloc`.
Exclusions, and why:

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
cd ~/repos

# Derive the in-scope repo list from actual remotes (don't hand-maintain it):
ORG_REPOS=$(for d in */; do d="${d%/}"; \
  git -C "$d" remote get-url origin 2>/dev/null \
    | grep -q 'github.com[:/]lentago/' && printf '%s ' "$d"; done)

# --vcs=git resolves the file list per repo, so cloc must be run inside each one
# and the per-language totals summed. This is why it is a loop, not one cloc call.
for d in $ORG_REPOS; do
  ( cd "$d" && cloc . --vcs=git --quiet --json \
      --exclude-dir=.git,node_modules,.venv,venv,__pycache__,dist,build,.next,vendor,target,.terraform,.astro,.playwright-mcp,site,archive \
      --fullpath --not-match-f='package-lock\.json' \
      --exclude-ext=docx,png,pdf,woff2,psd,jpeg,jpg,gz,svg,map )
done
```

Sum the per-repo JSON by language (`code`, `comment`, `blank`, `nFiles`), skipping
the `header` and `SUM` keys. Note `--vcs=git` also means a file staged but never
committed is out of scope, which is intended.

Then update the table, the "Last updated" date, and add a row to the log below.
(`cloc` install: `sudo apt-get install -y cloc`.)

---

## Update log

| Date | Total LOC | Files | Notes |
|------|----------:|------:|-------|
| 2026-06-17 | 114,713 | 1,054 | Initial census over the **full `~/repos` working tree** (22 dirs, incl. third-party + personal). Superseded same day. |
| 2026-06-17 | 76,388 | 519 | **Re-scoped to Lentago Labs org repos only** (14 repos). cloc 2.06. |
| 2026-07-25 | 242,774 | 1,499 | **Methodology change — git-tracked files only** (`cloc --vcs=git`), so totals are NOT comparable with rows above. Prompted by an untracked 1.6M-line personal Spotify export in `music-curator/data/` that a working-tree scan would have published as fleet source. Scope refreshed to 18 repos and the 2026-07-04 renames picked up (the list derives from remotes; it had just not been rerun). +`brasenia`, +`kalmia`, +`site-pondviewlane-com`. cloc 2.06. Closes .github#31. |
| 2026-06-29 | 88,063 | 589 | Refresh after the Lentago Labs rebrand. **+`lentagolabs-dev`** brought into scope (now 15 repos, alongside the legacy `pitzilabs-dev` clone); **`archive/` excluded** as a gitignored local-only mockup that was adding ~2,144 HTML lines. cloc 2.06. |
