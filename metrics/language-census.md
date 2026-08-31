# Lentago Labs Language Census

A periodic census of the programming/markup/config languages represented across
the **Lentago Labs org repositories**, ordered by prominence (lines of code). This
file is meant to be **regenerated periodically** — see
[Regenerating](#regenerating) for the exact, reproducible command, and log each
refresh in the [Update log](#update-log).

> **Scope.** Only repositories whose `origin` remote is under
> `github.com/lentago/`. Measured over the maintainer's `~/repos` working tree
> (owner-grouped into `lentago/`, `cpitzi/`, `applause/` subdirs since
> 2026-08-12, so the scan walks two levels), so it counts what's checked out
> locally for each org repo (not a GitHub API query). Personal repos under
> `cpitzi/` — including `reference-checker` and `myosotis`, both outside the org
> with repointed remotes — and the `applause/` work tree are **excluded**, as
> are local-only scratch dirs that aren't git repos. Generated artifacts and
> vendored dependencies are excluded (see [Methodology](#methodology)); `cloc`
> additionally **deduplicates byte-identical files**, so the deliberately-mirrored
> `CLAUDE.md` / PR-workflow text is counted once, not once per repo.
>
> **Repos in scope (22):** `asclepias`, `betula`, `brasenia`, `claytonia`,
> `.github`, `drosera`, `epigaea`, `kalmia`, `lupinus`, `mitchella`, `monarda`,
> `music-curator`, `office-presence`, `osmunda`, `repo-template`,
> `shared-workflows`, `site-icecreamtofightwith-com`, `site-lentago-dev`,
> `site-pitzilabs-dev`, `site-pondviewlane-com`, `solidago`,
> `workstation-bootstrap`.
>
> Membership churn since the 2026-07-25 census: five August-born repos joined
> (`asclepias`, `lupinus`, `mitchella`, `monarda`, `osmunda`);
> `homeassistant-config` was renamed to `epigaea` (same repo, .github#147); and
> `reference-checker` left the org for the personal account on 2026-08-16
> (.github#146), its local remote repointed 2026-08-23 — taking its committed
> `reports/*.html` with it. The three archived repos (`office-presence`,
> `site-pitzilabs-dev`, `workstation-bootstrap`) were rehomed to the personal
> `cjpitzi` account in August, but their local clones' origins still carry
> `github.com/lentago/` URLs (GitHub 301-redirects them), so the remote rule
> keeps them in scope — consistent with earlier cycles, where archive state
> never affected membership, unlike the active-only
> `fleet-reports/fleet-report.md`.

---

## Last updated: 2026-08-30

**Headline:** data still dominates — JSON is ~53% and, with CSV, exported
payloads still outweigh every line of executing code in the fleet combined.
Markdown is second at ~19% and its file count broke a thousand: the five
August-born repos are documentation-first, which *is* the fleet's character.
The executing spine is now a three-way tie — Shell, Python, and the JavaScript
family sit within ~400 lines of each other — with Python nearly doubling again
as `mitchella` arrives Python-first. HTML fell by almost two-thirds when
`reference-checker` left the org and took its committed report renders with it.

### By lines of code

Tool: `cloc 2.06`, over **git-tracked files only** (see Methodology). Total:
**262,696 lines of code** across **1,821 unique files**.

| # | Language | Code | Comment | Blank | Files | Share of code |
|---|----------|-----:|--------:|------:|------:|--------------:|
| 1 | JSON | 138,893 | 0 | 2 | 66 | 52.9% |
| 2 | Markdown | 49,195 | 209 | 15,448 | 1,051 | 18.7% |
| 3 | CSV | 15,595 | 0 | 0 | 2 | 5.9% |
| 4 | YAML | 11,194 | 2,824 | 1,122 | 227 | 4.3% |
| 5 | Shell (Bourne + Bash) | 9,927 | 3,047 | 1,733 | 90 | 3.8% |
| 6 | Python | 9,784 | 4,168 | 2,192 | 72 | 3.7% |
| 7 | HCL / Terraform | 6,721 | 2,466 | 1,358 | 113 | 2.6% |
| 8 | JSX (React) | 5,412 | 595 | 365 | 42 | 2.1% |
| 9 | JavaScript | 4,094 | 746 | 439 | 21 | 1.6% |
| 10 | Text | 3,621 | 0 | 987 | 27 | 1.4% |
| 11 | HTML | 2,947 | 4 | 85 | 30 | 1.1% |
| 12 | Astro | 2,364 | 311 | 187 | 29 | 0.9% |
| 13 | CSS | 1,716 | 430 | 177 | 13 | 0.7% |
| 14 | Jinja Template | 560 | 0 | 82 | 15 | 0.2% |
| 15 | TypeScript | 441 | 211 | 62 | 11 | 0.2% |
| 16 | TOML | 159 | 70 | 31 | 6 | 0.06% |
| 17 | XML | 39 | 0 | 3 | 1 | 0.01% |
| 18 | Dockerfile | 21 | 53 | 15 | 4 | 0.01% |
| 19 | BrightScript | 13 | 0 | 0 | 1 | 0.005% |

(`cloc` splits Shell into "Bourne Shell" 8,358 + "Bourne Again Shell" 1,569;
folded above.)

### Programming / scripting languages only

Stripping docs (Markdown, Text), data (JSON, CSV, XML), config (YAML/TOML), and
markup (HTML/CSS), the code that actually executes ranks:

| # | Language | Code |
|---|----------|-----:|
| 1 | Shell / Bash | 9,927 |
| 2 | Python | 9,784 |
| 3 | JavaScript family (JS + JSX) | 9,506 |
| 4 | Terraform / HCL *(infra-as-code)* | 6,721 |
| 5 | Astro | 2,364 |
| 6 | Jinja Template | 560 |
| 7 | TypeScript | 441 |
| 8 | BrightScript | 13 |

### Notes

- **JSON leads but carries no logic** — `music-curator`'s credits and inventory
  exports (104,513 lines), `epigaea`'s HA entity/device/dashboard registry
  snapshots (17,453), and `drosera`'s Grafana dashboard JSON (14,098) are ~52%
  of the whole census on their own. With CSV (two Spotify collection exports,
  15,595 lines) the exported-data share is ~59%. Discount it and the picture is
  Markdown documentation over a Shell/Python/JS → Terraform code base.
- **Markdown broke a thousand files** — 1,051 against 66 JSON, +11k lines since
  July. The five August-born repos are documentation-first (~3.4k lines between
  them, `asclepias` and `osmunda` carrying no executing code at all beyond a few
  shell lines). The breadth of this hand-maintained surface is what makes the
  relative-link checker adopted fleet-wide in .github#57 worth its cost.
- **HTML fell from 7,628 to 2,947 lines** — `reference-checker`'s committed
  `reports/*.html` (rendered analysis outputs) left with the repo when it moved
  to the personal account (2026-08-16). What remains is spread across this repo
  and the site repos; still mostly output-like, not hand-authored markup.
- **The web stack is still double-counted**, though less than before. Both
  `site-pitzilabs-dev` (archived) and its successor `site-lentago-dev` carry
  `github.com/lentago/` origins and remain cloned locally, so the JS/JSX/Astro/CSS
  figures reflect both. They are not byte-identical, so `cloc`'s dedup does not
  collapse them. Deleting the archived clone locally is what retires that overlap.
- **Python nearly doubled again** — 5,219 lines at the last census, 9,784 now.
  `mitchella` arrives as the fleet's most Python-forward repo (1,295 lines, its
  largest language), and `music-curator` (4,227) remains the biggest holder.
- **Python has taken Shell's most-commented crown** — 4,168 comment lines
  against 9,784 of code (~43%), with Shell holding at ~31% (3,047 against
  9,927). Both are consistent with ops code written to be audited.

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

# Derive the in-scope repo list from actual remotes (don't hand-maintain it).
# Clones are owner-grouped (lentago/, cpitzi/, applause/) since 2026-08-12, so
# walk both levels — the flat `*/` glob alone now finds nothing:
ORG_REPOS=$(for d in */ */*/; do d="${d%/}"; \
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
| 2026-06-29 | 88,063 | 589 | Refresh after the Lentago Labs rebrand. **+`lentagolabs-dev`** brought into scope (now 15 repos, alongside the legacy `pitzilabs-dev` clone); **`archive/` excluded** as a gitignored local-only mockup that was adding ~2,144 HTML lines. cloc 2.06. |
| 2026-07-25 | 242,774 | 1,499 | **Methodology change — git-tracked files only** (`cloc --vcs=git`), so totals are NOT comparable with rows above. Prompted by an untracked 1.6M-line personal Spotify export in `music-curator/data/` that a working-tree scan would have published as fleet source. Scope refreshed to 18 repos and the 2026-07-04 renames picked up (the list derives from remotes; it had just not been rerun). +`brasenia`, +`kalmia`, +`site-pondviewlane-com`. cloc 2.06. Closes .github#31. |
| 2026-08-30 | 262,696 | 1,821 | Scope 18 → **22 repos**: +`asclepias`, +`lupinus`, +`mitchella`, +`monarda`, +`osmunda` (the August wave); −`reference-checker` (out of the org since 2026-08-16, .github#146 — its committed HTML reports drop HTML from 7,628 to 2,947); `homeassistant-config`→`epigaea` rename picked up. Regeneration recipe updated for the owner-grouped `~/repos` layout (two-level walk); log rows reordered chronologically. cloc 2.06. |
