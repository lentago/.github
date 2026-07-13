# Lentago Labs Fleet — Code Census

> [!NOTE]
> **Co-authored with [Claude](https://claude.ai)** (Repo Claude, the Lentago Labs fleet steward). Auto-generated weekly from public repo contents — no personal or security detail is included. A companion, prettier copy renders on the Lentago lab LAN.

**Generated:** 2026-07-13 19:55 UTC · Tool: `cloc` · Scope: the **13 active** `lentago` repos, measured over their default branches. The 3 archived repos (`office-presence`, `site-pitzilabs-dev`, `workstation-bootstrap`) are frozen and excluded.

**The lens:** a `CLAUDE.md` (and its kin — `AGENTS.md`, skill `SKILL.md`, and the LLM prompt-programs that *are* a tool's logic) is an instruction set maintained for hygiene, so it's counted as **natural-language code**. Documentation, content/data, and community-health markdown are tallied separately and excluded from the code total, as are data payloads and generated files. This is a deliberate re-cut of the canonical [`metrics/language-census.md`](language-census.md), which instead counts all Markdown/JSON/HTML as code.

**Headline:** the fleet's hand-maintained natural-language instruction surface (**3,055 lines**) is among the largest "languages" in the code base. One repo — `reference-checker` — is almost entirely natural-language source: its auditor is a prompt program.

| Code (incl. instructions) | Instruction-markdown | Repos | Data excluded | Generated excluded |
|---:|---:|---:|---:|---:|
| **35,904** | **3,055** (18 files) | 13 | 85,159 | 12,645 |

## 1 — Languages

cloc *code* lines (blank + comment excluded). Shell folds Bourne + Bash. Instruction-markdown is promoted into the count (**bold**); the excluded buckets sit below the total.

| # | Language | Code | Files | Share |
|---|----------|-----:|------:|------:|
| 1 | JSON | 8,581 | 25 | 23.9% |
| 2 | YAML | 8,063 | 126 | 22.5% |
| 3 | HCL | 5,425 | 99 | 15.1% |
| 4 | Shell (Bourne + Bash) | 4,569 | 54 | 12.7% |
| 5 | **Instructions (CLAUDE.md family + prompt-programs)** | 3,055 | 18 | 8.5% |
| 6 | Python | 2,402 | 18 | 6.7% |
| 7 | Astro | 1,325 | 11 | 3.7% |
| 8 | JSX | 851 | 10 | 2.4% |
| 9 | JavaScript | 773 | 7 | 2.2% |
| 10 | TypeScript | 304 | 7 | 0.8% |
| 11 | Jinja Template | 261 | 4 | 0.7% |
| 12 | CSS | 258 | 7 | 0.7% |
| 13 | Other (TOML / Dockerfile / …) | 37 | 5 | 0.1% |
| | **CODE TOTAL** | **35,904** | **391** | 100% |
| — | _Data / exports — excluded_ | 85,159 | 19 | — |
| — | _Generated (lockfiles, SVG) — excluded_ | 12,645 | 25 | — |

## 2 — Instruction-markdown as code

- **Hygiene family** (14 files · `CLAUDE.md`, `AGENTS.md`, `SKILL.md`): **1,604 lines**
- **Prompt-programs** (4 files · reference-checker auditors): **1,451 lines**

### 2a — The hygiene surface (each file is a maintenance obligation)

| Repo | File | Lines |
|------|------|------:|
| homeassistant-config | `CLAUDE.md` | 399 |
| shared-workflows | `CLAUDE.md` | 181 |
| betula | `CLAUDE.md` | 156 |
| site-lentago-dev | `CLAUDE.md` | 108 |
| solidago | `CLAUDE.md` | 99 |
| site-icecreamtofightwith-com | `CLAUDE.md` | 98 |
| drosera | `CLAUDE.md` | 95 |
| kalmia | `CLAUDE.md` | 94 |
| .github | `CLAUDE.md` | 92 |
| reference-checker | `CLAUDE.md` | 76 |
| drosera | `AGENTS.md` | 66 |
| music-curator | `CLAUDE.md` | 61 |
| claytonia | `CLAUDE.md` | 57 |
| repo-template | `CLAUDE.md` | 22 |
| **14 files** | | **1,604** |

### 2b — Prompt-programs (natural language *is* the logic)

| Repo | File | Lines |
|------|------|------:|
| reference-checker | `prompts/v6-auditor.md` | 583 |
| reference-checker | `prompts/v5-auditor.md` | 462 |
| reference-checker | `prompts/v4-auditor.md` | 337 |
| reference-checker | `prompts/v3-auditor.md` | 69 |
| **4 files** | | **1,451** |

_Judgement call: these prompt files are counted as instruction-code because they're versioned natural-language instruction sets. Scope to only the CLAUDE.md hygiene family and the instruction figure is **1,604**, not 3,055._

## 3 — Per-repo

| Repo | Code | Instr | Doc-md | Content-md | Data |
|------|-----:|------:|-------:|-----------:|-----:|
| drosera | 9,298 | 161 | 667 | 0 | 0 |
| homeassistant-config | 6,495 | 399 | 1,090 | 0 | 17,420 |
| solidago | 5,831 | 99 | 1,690 | 0 | 0 |
| site-icecreamtofightwith-com | 3,232 | 98 | 594 | 6,008 | 0 |
| kalmia | 2,243 | 94 | 463 | 0 | 0 |
| claytonia | 1,736 | 57 | 520 | 0 | 0 |
| music-curator | 1,618 | 61 | 866 | 7,909 | 62,565 |
| reference-checker | 1,587 | 1,527 | 731 | 669 | 5,174 |
| site-lentago-dev | 1,555 | 108 | 360 | 0 | 0 |
| betula | 1,288 | 156 | 923 | 0 | 0 |
| shared-workflows | 571 | 181 | 83 | 0 | 0 |
| .github | 385 | 92 | 366 | 165 | 0 |
| repo-template | 65 | 22 | 46 | 0 | 0 |

## 4 — Markdown taxonomy

The fleet carries **26,557 lines of Markdown across 725 files**; only 11.5% is instruction-code.

| Class | Lines | Files | Disposition |
|-------|------:|------:|-------------|
| **Instructions** | 3,055 | 18 | **counted as code** |
| Content / data | 14,751 | 623 | payload (vault notes, recipes, test-sets) — excluded |
| Documentation | 8,399 | 69 | READMEs, docs, ADRs, runbooks — excluded |
| Community-health | 352 | 15 | CONTRIBUTING/SECURITY/templates — excluded |
| **All Markdown** | **26,557** | **725** | |

## Method & reproducibility

- **Tool:** `cloc`, run per-repo as `cloc --by-file --vcs=git` so only git-tracked files count (build output, `node_modules`, `.terraform`, venvs never enter). Lines are cloc *code* lines.
- **Scope:** the active repos owned by the `lentago` org, derived at runtime — personal repos and third-party clones are out of scope by construction; archived repos are frozen and excluded.
- **Markdown classifier:** instruction-code = `CLAUDE.md`/`AGENTS.md`/`SKILL.md` or a versioned `prompts/*-auditor.md`; community-health = the standard governance filenames + issue/PR templates; content = repo-scoped payload paths (music-curator `vault/`, ice-cream `recipes/`·manuscript, reference-checker `test-sets/`·`reports/`, dotgithub `fleet-reports/`); everything else = documentation.
- **Data / generated carve-outs:** large exported JSON (music-curator `data/`, homeassistant-config `context/`) and reference-checker's rendered `reports/*.html` are data/output, not code; lockfiles and SVG are generated. drosera's `dashboards/*.json` stay in code as Terraform-enforced dashboards-as-code.
- **Regenerating:** `python3 metrics/generate-fleet-reports.py --out-dir .` (see the script header).

_Generated with Claude Code (Repo Claude)._
