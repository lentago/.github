#!/usr/bin/env python3
"""Generate the Lentago Labs fleet report as GitHub-rendered Markdown.

Produces one file under the output tree:
  fleet-reports/fleet-report.md — a single combined report: open issues by repo +
                                  a 30-day activity snapshot, followed by a code census
                                  in which CLAUDE.md-family instruction markdown is
                                  counted as natural-language code (docs / content /
                                  data reported separately, excluded). Public data only.

Scope: every active repo whose owner is the `lentago` org (derived at runtime — new/
renamed repos are picked up automatically; archived repos are excluded). Third-party
clones and personal repos are excluded by construction. Run locally over an existing
working tree, or in CI where it shallow-clones each repo itself.

Usage:
  gen.py --out-dir <dotgithub-checkout> [--source-dir <dir-of-clones>] [--work-dir <tmp>]

If --source-dir is given and contains the clones, they're reused (fast local runs).
Otherwise every lentago repo is shallow-cloned into --work-dir (default: a temp dir).
Requires: git, gh (authenticated), cloc.
"""
import argparse, json, os, re, subprocess, sys, tempfile, shutil
from collections import defaultdict
from datetime import datetime, timezone, timedelta

# Activity window for the merged-PRs / closed-issues snapshot. The search limits in
# get_issue_data() are sized for this window — widen them if you widen it further.
ACTIVITY_WINDOW_DAYS = 30

# ---------------------------------------------------------------- helpers
def sh(cmd, cwd=None, check=True):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"cmd failed ({r.returncode}): {' '.join(cmd)}\n{r.stderr[:500]}")
    return r.stdout

def gh_json(args):
    return json.loads(sh(["gh"] + args))

def ensure_cloc():
    if shutil.which("cloc"): return
    for inst in (["apt-get","install","-y","-q","cloc"],
                 ["sudo","apt-get","install","-y","-q","cloc"]):
        try:
            sh(["bash","-c","apt-get update -q >/dev/null 2>&1 || sudo apt-get update -q >/dev/null 2>&1 || true"], check=False)
            r = subprocess.run(inst, capture_output=True, text=True)
            if r.returncode == 0 and shutil.which("cloc"): return
        except Exception:
            pass
    raise RuntimeError("cloc is required but not installed and auto-install failed.")

def get_repos():
    """Active (non-archived) PUBLIC lentago-org repos.

    Scope note: GitHub's org-listing/search endpoints do not surface archived repos
    for this account, so the reliable, self-maintaining scope is the active fleet.
    Archived repos are frozen code anyway — no reason to re-count them weekly. The
    endpoint returns non-archived repos; we carry the flag for forward-compatibility.

    Private repos are excluded: these reports publish in a public repo, and the
    census clone stage is deliberately unauthenticated — it can only see what the
    public can see.
    """
    raw = sh(["gh","api","orgs/lentago/repos","--paginate",
              "--jq",".[] | {name:.name, isArchived:.archived, isPrivate:.private}"])
    data = [json.loads(line) for line in raw.splitlines() if line.strip()]
    return sorted((r for r in data if not r["isPrivate"]), key=lambda r: r["name"])

def ensure_clones(repos, source_dir, work_dir):
    """Bind each repo name to a local checkout. Reuse source_dir clones (matched by
    origin remote, since e.g. `.github` clones as `dotgithub`); shallow-clone the rest."""
    mapping = {}
    if source_dir and os.path.isdir(source_dir):
        for d in os.listdir(source_dir):
            p = os.path.join(source_dir, d)
            if not os.path.isdir(os.path.join(p, ".git")): continue
            url = sh(["git","-C",p,"remote","get-url","origin"], check=False).strip()
            for r in repos:
                if url.endswith(f"lentago/{r['name']}.git") or url.endswith(f"lentago/{r['name']}"):
                    mapping[r["name"]] = p
    for r in repos:
        if r["name"] in mapping: continue
        dest = os.path.join(work_dir, r["name"])
        if not os.path.isdir(dest):
            sh(["git","clone","--depth","1","--quiet",
                f"https://github.com/lentago/{r['name']}.git", dest])
        mapping[r["name"]] = dest
    return mapping

# ---------------------------------------------------------------- census (ported, validated logic)
GEN_BASENAMES = {"package-lock.json","yarn.lock","pnpm-lock.yaml","poetry.lock",
                 "Cargo.lock","composer.lock","Gemfile.lock"}
GEN_EXT = {".svg"}
# Directories holding machine-generated artefacts committed for reproducibility.
# Curated per-repo like DATA_DIR_PREFIX, because only the path distinguishes these
# from hand-written source of the same format. `.github/brand/generated/` is emitted
# by brand/generate.py from brand/fleet.json and is asserted reproducible by CI's
# `brand` check — counting it as authored code would credit the fleet with source it
# regenerates from a config file.
GEN_DIR_PREFIX = {".github": ("brand/generated/",)}
# Directories that hold exported payloads rather than source. Curated per-repo, so the
# rule below can be format-agnostic: anything under one of these prefixes carrying a
# data-serialisation extension is a payload, whatever format the export happens to use.
# (Markdown is deliberately absent — a README.md describing a data dir is documentation,
# and classify_md() already routes it.)
DATA_DIR_PREFIX = {"music-curator":("data/",), "homeassistant-config":("context/",)}
DATA_EXT = {".json",".jsonl",".ndjson",".csv",".tsv",".xml",".yaml",".yml",".parquet"}

def is_generated(repo, path):
    base = os.path.basename(path)
    if base in GEN_BASENAMES: return True
    if os.path.splitext(base)[1] in GEN_EXT: return True
    if ".min." in base: return True
    p = path[2:] if path.startswith("./") else path
    if any(p.startswith(x) for x in GEN_DIR_PREFIX.get(repo, ())): return True
    return False

def is_data(repo, path):
    p = path[2:] if path.startswith("./") else path
    low = p.lower()
    if (os.path.splitext(low)[1] in DATA_EXT
            and any(p.startswith(x) for x in DATA_DIR_PREFIX.get(repo,()))):
        return True
    if repo=="reference-checker" and low.startswith("reports/") and low.endswith(".html"):
        return True
    return False

def classify_md(repo, path):
    p = path[2:] if path.startswith("./") else path
    base, low = os.path.basename(p), p.lower()
    if base in ("CLAUDE.md","AGENTS.md","GEMINI.md","SKILL.md"): return "instructions"
    if base==".cursorrules" or "copilot-instructions" in base: return "instructions"
    if low.startswith("prompts/") and "auditor" in low: return "instructions"
    if base in ("CONTRIBUTING.md","SECURITY.md","CODE_OF_CONDUCT.md","SUPPORT.md","GOVERNANCE.md"):
        return "community"
    if "issue_template" in low or base=="pull_request_template.md": return "community"
    if repo=="music-curator" and (low.startswith("vault/") or low.startswith("examples/")): return "content"
    if repo=="reference-checker" and (low.startswith("test-sets/") or low.startswith("reports/")): return "content"
    if repo=="site-icecreamtofightwith-com" and (low.startswith("recipes/") or low.startswith("front_matter/")
        or low.startswith("back_matter/") or low.startswith("canonical_samples/") or low.startswith("images/")
        or low.startswith("example_") or "complete.md" in low): return "content"
    if repo in ("dotgithub",".github") and low.startswith("fleet-reports/"): return "content"
    return "documentation"

def hygiene_kind(path):
    b = os.path.basename(path)
    if b in ("CLAUDE.md","AGENTS.md","SKILL.md"): return "hygiene"
    low = (path[2:] if path.startswith("./") else path).lower()
    if low.startswith("prompts/") and "auditor" in low: return "prompt"
    return None

def run_census(repos, clones):
    ensure_cloc()
    fleet = {"code":defaultdict(lambda:{"files":0,"lines":0}),
             "generated":{"files":0,"lines":0}, "data":{"files":0,"lines":0},
             "md":{b:{"files":0,"lines":0} for b in ("instructions","documentation","community","content")}}
    per_repo, instr_files = {}, []
    INSTR_LABEL = "Instructions (CLAUDE.md family + prompt-programs)"
    for r in repos:
        repo = r["name"]; d = clones[repo]
        out = subprocess.run(["cloc","--by-file","--vcs=git","--json","--quiet"],
                             cwd=d, capture_output=True, text=True)
        if out.returncode!=0 or not out.stdout.strip(): continue
        data = json.loads(out.stdout)
        rr = {"code":defaultdict(lambda:{"files":0,"lines":0}),
              "generated":{"files":0,"lines":0}, "data":{"files":0,"lines":0},
              "md":{b:{"files":0,"lines":0} for b in fleet["md"]}}
        for path,v in data.items():
            if path in ("header","SUM"): continue
            lang, code = v["language"], v["code"]
            base = os.path.basename(path)
            if lang=="Markdown":
                bucket = classify_md(repo, path)
                if bucket=="instructions":
                    rr["code"][INSTR_LABEL]["files"]+=1; rr["code"][INSTR_LABEL]["lines"]+=code
                    k = hygiene_kind(path)
                    instr_files.append((repo, (path[2:] if path.startswith("./") else path), code, k))
                rr["md"][bucket]["files"]+=1; rr["md"][bucket]["lines"]+=code
            elif is_generated(repo, path):
                rr["generated"]["files"]+=1; rr["generated"]["lines"]+=code
            elif is_data(repo, path):
                rr["data"]["files"]+=1; rr["data"]["lines"]+=code
            else:
                rr["code"][lang]["files"]+=1; rr["code"][lang]["lines"]+=code
        per_repo[repo]=rr
        for lang,s in rr["code"].items():
            fleet["code"][lang]["files"]+=s["files"]; fleet["code"][lang]["lines"]+=s["lines"]
        for k in ("generated","data"):
            fleet[k]["files"]+=rr[k]["files"]; fleet[k]["lines"]+=rr[k]["lines"]
        for b in rr["md"]:
            fleet["md"][b]["files"]+=rr["md"][b]["files"]; fleet["md"][b]["lines"]+=rr["md"][b]["lines"]
    return fleet, per_repo, instr_files, INSTR_LABEL

def fold_langs(code):
    """Fold Bourne+Bash into Shell and tiny (<50) langs into Other; return sorted rows."""
    rows = defaultdict(lambda:{"files":0,"lines":0})
    for lang,s in code.items():
        key = lang
        if lang in ("Bourne Shell","Bourne Again Shell"): key="Shell (Bourne + Bash)"
        rows[key]["files"]+=s["files"]; rows[key]["lines"]+=s["lines"]
    other = {"files":0,"lines":0}
    keep = {}
    for lang,s in rows.items():
        if s["lines"]<50 and not lang.startswith("Instructions"):
            other["files"]+=s["files"]; other["lines"]+=s["lines"]
        else:
            keep[lang]=s
    if other["files"]: keep["Other (TOML / Dockerfile / …)"]=other
    return sorted(keep.items(), key=lambda x:-x[1]["lines"])

# ---------------------------------------------------------------- issue data
def get_issue_data(cutoff_iso, fleet_names):
    open_issues = gh_json(["search","issues","--owner","lentago","--state","open","--limit","200",
                           "--json","repository,number,title,createdAt,updatedAt"])
    closed = gh_json(["search","issues","--owner","lentago","--state","closed","--closed",f">={cutoff_iso[:10]}",
                      "--limit","500","--json","repository,number,title,closedAt"])
    prs = gh_json(["search","prs","--owner","lentago","--merged","--merged-at",f">={cutoff_iso[:10]}",
                   "--limit","500","--json","repository,number,title,closedAt"])
    # The org-wide search sees whatever the running token sees — CI's scoped PAT
    # can't read private repos, but a local regen with an account-wide token can,
    # and this report is public. Clamp to the public fleet.
    def scoped(items): return [i for i in items if i["repository"]["name"] in fleet_names]
    open_issues, closed, prs = scoped(open_issues), scoped(closed), scoped(prs)
    recent_closed = [i for i in closed if i.get("closedAt","") >= cutoff_iso]
    recent_open = [i for i in open_issues if i.get("createdAt","") >= cutoff_iso]
    return open_issues, recent_closed, prs, recent_open

# ---------------------------------------------------------------- report sections
def _esc(s):
    return s.replace("|", "\\|")

def issue_section(open_issues, recent_closed, merged_prs, recent_open):
    by_repo = defaultdict(list)
    for i in open_issues: by_repo[i["repository"]["name"]].append(i)
    L = []
    L.append(f"## Open issues — {len(open_issues)} across {len(by_repo)} repos")
    L.append("")
    if not open_issues:
        L.append("_No open issues across the fleet._"); L.append("")
    for repo in sorted(by_repo, key=lambda r:(-len(by_repo[r]), r)):
        items = sorted(by_repo[repo], key=lambda i:-i["number"])
        L.append(f"### {repo} — {len(items)} open")
        L.append("")
        L.append("| # | Title |")
        L.append("|---|-------|")
        for i in items:
            url = f"https://github.com/lentago/{repo}/issues/{i['number']}"
            L.append(f"| [{i['number']}]({url}) | {_esc(i['title'])} |")
        L.append("")
    L.append(f"## Activity — last {ACTIVITY_WINDOW_DAYS} days")
    L.append("")
    L.append(f"**{len(merged_prs) + len(recent_closed)} events**, one stream, newest first — "
             f"🟣 {len(merged_prs)} PRs merged · 🟢 {len(recent_closed)} issues closed")
    L.append("")
    # Color-coded by GitHub's own iconography: purple = merged PR, green = issue.
    events = ([("🟣", "pull", p) for p in merged_prs] +
              [("🟢", "issues", i) for i in recent_closed])
    for mark, path, e in sorted(events, key=lambda t: t[2].get("closedAt",""), reverse=True):
        repo=e["repository"]["name"]; url=f"https://github.com/lentago/{repo}/{path}/{e['number']}"
        L.append(f"- {mark} {e.get('closedAt','')[:10]} · [{repo}#{e['number']}]({url}) — {_esc(e['title'])}")
    L.append("")
    return L

def census_section(fleet, per_repo, instr_files, INSTR_LABEL, repos):
    code_total = sum(s["lines"] for s in fleet["code"].values())
    code_files = sum(s["files"] for s in fleet["code"].values())
    instr = fleet["code"].get(INSTR_LABEL, {"files":0,"lines":0})
    hyg = [f for f in instr_files if f[3]=="hygiene"]
    prm = [f for f in instr_files if f[3]=="prompt"]
    hyg_l = sum(f[2] for f in hyg); prm_l = sum(f[2] for f in prm)
    md = fleet["md"]; md_total = sum(md[b]["lines"] for b in md); md_files = sum(md[b]["files"] for b in md)
    arch = {r["name"] for r in repos if r["isArchived"]}
    L = []
    L.append("## Code census")
    L.append("")
    L.append("**The lens:** a `CLAUDE.md` (and its kin — `AGENTS.md`, skill `SKILL.md`, and the LLM prompt-programs "
             "that *are* a tool's logic) is an instruction set maintained for hygiene, so it's counted as "
             "**natural-language code**. Documentation, content/data, and community-health markdown are tallied "
             "separately and excluded from the code total, as are data payloads and generated files. This is a "
             "deliberate re-cut of the canonical [`metrics/language-census.md`](../metrics/language-census.md), which "
             "instead counts all Markdown/JSON/HTML as code.")
    L.append("")
    L.append("### Languages")
    L.append("")
    L.append("cloc *code* lines (blank + comment excluded). Shell folds Bourne + Bash. Instruction-markdown is "
             "promoted into the count (**bold**); the excluded buckets sit below the total.")
    L.append("")
    L.append("| # | Language | Code | Files | Share |")
    L.append("|---|----------|-----:|------:|------:|")
    for i,(lang,s) in enumerate(fold_langs(fleet["code"]),1):
        pct = 100*s["lines"]/code_total if code_total else 0
        name = f"**{lang}**" if lang.startswith("Instructions") else lang
        L.append(f"| {i} | {name} | {s['lines']:,} | {s['files']} | {pct:.1f}% |")
    L.append(f"| | **CODE TOTAL** | **{code_total:,}** | **{code_files}** | 100% |")
    L.append(f"| — | _Data / exports — excluded_ | {fleet['data']['lines']:,} | {fleet['data']['files']} | — |")
    L.append(f"| — | _Generated (lockfiles, SVG, brand artefacts) — excluded_ | {fleet['generated']['lines']:,} | {fleet['generated']['files']} | — |")
    L.append("")
    L.append("### Instruction-markdown as code")
    L.append("")
    L.append(f"- **Hygiene family** ({len(hyg)} files · `CLAUDE.md`, `AGENTS.md`, `SKILL.md`): **{hyg_l:,} lines**")
    L.append(f"- **Prompt-programs** ({len(prm)} files · reference-checker auditors): **{prm_l:,} lines**")
    L.append("")
    L.append("#### Hygiene surface — each file is a maintenance obligation")
    L.append("")
    L.append("| Repo | File | Lines |")
    L.append("|------|------|------:|")
    for repo,path,code,_ in sorted(hyg, key=lambda x:-x[2]):
        tag = " _(archived)_" if repo in arch else ""
        L.append(f"| {repo}{tag} | `{os.path.basename(path)}` | {code} |")
    L.append(f"| **{len(hyg)} files** | | **{hyg_l:,}** |")
    L.append("")
    if prm:
        L.append("#### Prompt-programs — natural language *is* the logic")
        L.append("")
        L.append("| Repo | File | Lines |")
        L.append("|------|------|------:|")
        for repo,path,code,_ in sorted(prm, key=lambda x:-x[2]):
            L.append(f"| {repo} | `{path}` | {code} |")
        L.append(f"| **{len(prm)} files** | | **{prm_l:,}** |")
        L.append("")
        L.append("_Judgement call: these prompt files are counted as instruction-code because they're versioned "
                 "natural-language instruction sets. Scope to only the CLAUDE.md hygiene family and the instruction "
                 f"figure is **{hyg_l:,}**, not {instr['lines']:,}._")
        L.append("")
    L.append("### Per-repo")
    L.append("")
    L.append("| Repo | Code | Instr | Doc-md | Content-md | Data |")
    L.append("|------|-----:|------:|-------:|-----------:|-----:|")
    order = sorted(repos, key=lambda r:-sum(s["lines"] for s in per_repo.get(r["name"],{"code":{}})["code"].values()) if r["name"] in per_repo else 0)
    for r in order:
        repo=r["name"]
        if repo not in per_repo: continue
        rr=per_repo[repo]; ct=sum(s["lines"] for s in rr["code"].values())
        tag=" _(arch)_" if r["isArchived"] else ""
        L.append(f"| {repo}{tag} | {ct:,} | {rr['code'].get(INSTR_LABEL,{'lines':0})['lines']:,} | "
                 f"{rr['md']['documentation']['lines']:,} | {rr['md']['content']['lines']:,} | {rr['data']['lines']:,} |")
    L.append("")
    L.append("### Markdown taxonomy")
    L.append("")
    L.append(f"The fleet carries **{md_total:,} lines of Markdown across {md_files} files**; only "
             f"{100*md['instructions']['lines']/md_total:.1f}% is instruction-code.")
    L.append("")
    L.append("| Class | Lines | Files | Disposition |")
    L.append("|-------|------:|------:|-------------|")
    L.append(f"| **Instructions** | {md['instructions']['lines']:,} | {md['instructions']['files']} | **counted as code** |")
    L.append(f"| Content / data | {md['content']['lines']:,} | {md['content']['files']} | payload (vault notes, recipes, test-sets) — excluded |")
    L.append(f"| Documentation | {md['documentation']['lines']:,} | {md['documentation']['files']} | READMEs, docs, ADRs, runbooks — excluded |")
    L.append(f"| Community-health | {md['community']['lines']:,} | {md['community']['files']} | CONTRIBUTING/SECURITY/templates — excluded |")
    L.append(f"| **All Markdown** | **{md_total:,}** | **{md_files}** | |")
    L.append("")
    return L

def render_report(fleet, per_repo, instr_files, LBL, repos, ts, cutoff,
                  open_issues, recent_closed, merged_prs, recent_open):
    code_total = sum(s["lines"] for s in fleet["code"].values())
    instr = fleet["code"].get(LBL, {"files":0,"lines":0})
    L = []
    L.append("# Lentago Labs Fleet Report")
    L.append("")
    L.append("> [!NOTE]")
    L.append("> **Co-authored with [Claude](https://claude.ai)** (Repo Claude, the Lentago Labs fleet steward). "
             "Auto-generated weekly from the fleet's public state (GitHub issues/PRs + `cloc` over public repo "
             "contents) — no personal, security, or homelab-internal detail is included. A prettier, editorialised "
             "copy renders on the Lentago lab LAN.")
    L.append("")
    L.append(f"**Generated:** {ts} · Scope: the **{len(repos)} active** `lentago` repos "
             f"(archived repos frozen &amp; excluded) · Activity window: last {ACTIVITY_WINDOW_DAYS} days "
             f"(since {cutoff[:10]}).")
    L.append("")
    L.append("## Snapshot")
    L.append("")
    L.append(f"| Open issues | PRs merged ({ACTIVITY_WINDOW_DAYS}d) | Issues closed ({ACTIVITY_WINDOW_DAYS}d) | Code (incl. instructions) | Instruction-markdown |")
    L.append("|---:|---:|---:|---:|---:|")
    L.append(f"| **{len(open_issues)}** | {len(merged_prs)} | {len(recent_closed)} | **{code_total:,}** | "
             f"{instr['lines']:,} ({instr['files']} files) |")
    L.append("")
    L.append(f"The fleet's hand-maintained natural-language instruction surface (**{instr['lines']:,} lines** across "
             f"{instr['files']} files) is among the largest \"languages\" in the code base — `reference-checker` alone "
             "is almost entirely prompt-program source.")
    L.append("")
    L.append("---")
    L.append("")
    L += issue_section(open_issues, recent_closed, merged_prs, recent_open)
    L.append("---")
    L.append("")
    L += census_section(fleet, per_repo, instr_files, LBL, repos)
    L.append("---")
    L.append("")
    L.append("## Method")
    L.append("")
    L.append("- **Issues:** open issues via `gh search issues --owner lentago --state open`; activity from "
             f"`gh search prs --owner lentago --merged` and closed issues filtered to the {ACTIVITY_WINDOW_DAYS}-day "
             "window. Public metadata only — no transcript harvest, ops items, or homelab detail (those live in "
             "the LAN copy).")
    L.append("- **Census tool:** `cloc`, run per-repo as `cloc --by-file --vcs=git` so only git-tracked files count "
             "(build output, `node_modules`, `.terraform`, venvs never enter). Lines are cloc *code* lines.")
    L.append("- **Scope:** the active repos owned by the `lentago` org, derived at runtime — personal repos and "
             "third-party clones are out of scope; archived repos are frozen and excluded.")
    L.append("- **Markdown classifier:** instruction-code = `CLAUDE.md`/`AGENTS.md`/`SKILL.md` or a versioned "
             "`prompts/*-auditor.md`; community-health = governance filenames + issue/PR templates; content = "
             "repo-scoped payload paths (music-curator `vault/`, ice-cream `recipes/`·manuscript, reference-checker "
             "`test-sets/`·`reports/`, dotgithub `fleet-reports/`); everything else = documentation.")
    L.append("- **Data / generated carve-outs:** exported payloads under the declared data dirs (music-curator "
             "`data/`, homeassistant-config `context/`) count as data whatever their serialisation — JSON, JSONL, "
             "CSV/TSV, XML, YAML — as does reference-checker's rendered `reports/*.html`; lockfiles, SVG and "
             "`.github/brand/generated/` (emitted from `brand/fleet.json`) are "
             "generated. drosera's `dashboards/*.json` stay in code as Terraform-enforced dashboards-as-code.")
    L.append("- **Regenerating:** `python3 metrics/generate-fleet-reports.py --out-dir .`")
    L.append("")
    L.append("_Generated with Claude Code (Repo Claude)._")
    L.append("")
    return "\n".join(L)

# ---------------------------------------------------------------- incident register
# Incident reports are harvested from local Lentago lab activity (the /incident-digest
# playbook) and dropped into fleet-reports/incidents/<YYYY-MM-DD>-<slug>.md out-of-band
# (by a local session, not this generator). This builds the public register that indexes
# them — the incident sibling of fleet-report.md. It reads only local files, so it needs
# neither gh nor cloc and runs under --incidents-only.
INCIDENTS_DIR = ("fleet-reports", "incidents")

def _strip_md(s):
    s = re.sub(r"`([^`]*)`", r"\1", s)
    s = re.sub(r"\*\*([^*]*)\*\*", r"\1", s)
    s = re.sub(r"\*([^*]*)\*", r"\1", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)  # [text](url) -> text
    return s.replace("&amp;", "&").strip()

def _first_sentence(text, limit=240):
    text = re.sub(r"\s+", " ", text).strip()
    m = re.search(r"(.+?[.!?])(\s|$)", text)
    s = m.group(1) if m else text
    if len(s) > limit:
        s = s[:limit].rsplit(" ", 1)[0].rstrip(",.;:") + "…"
    return s

def parse_incident(path):
    """Extract (title, summary) from an incident report. Robust to the /incident-digest
    template: '# Incident Digest — <Title>, YYYY-MM-DD' then a '## TL;DR' or '## Summary'."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    title = os.path.basename(path)
    for line in text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break
    title = re.sub(r"^Incident (Digest|Report)\s*[—:-]\s*", "", title)
    title = re.sub(r",?\s*\d{4}-\d{2}-\d{2}\s*$", "", title).strip()
    summary = ""
    m = re.search(r"^#{2,}\s*(TL;DR|Summary)\s*$", text, re.M | re.I)
    body = text[m.end():] if m else text
    for para in re.split(r"\n\s*\n", body):
        p = para.strip()
        if not p or p[0] in "#>|-*!" or p[:2].rstrip().isdigit():
            continue
        summary = _first_sentence(_strip_md(p))
        break
    return title, summary

def build_incident_register(out_dir, ts):
    inc_dir = os.path.join(out_dir, *INCIDENTS_DIR)
    entries = []
    if os.path.isdir(inc_dir):
        for fn in os.listdir(inc_dir):
            if not fn.endswith(".md") or fn.lower() in ("readme.md", "index.md"):
                continue
            m = re.match(r"(\d{4}-\d{2}-\d{2})-.+\.md$", fn)
            date = m.group(1) if m else "—"
            title, summary = parse_incident(os.path.join(inc_dir, fn))
            entries.append((date, title, summary, fn))
    entries.sort(key=lambda e: (e[0], e[3]), reverse=True)
    n = len(entries)
    L = []
    L.append("# Lentago Labs Incident Register")
    L.append("")
    L.append("> [!NOTE]")
    L.append("> **Co-authored with [Claude](https://claude.ai)** (the `/incident-digest` playbook). "
             "A chronological register of incident reports harvested from local Lentago lab activity "
             "and published as a periodic fleet report. Each row links to the full write-up under "
             "[`fleet-reports/incidents/`](incidents/). Unlike the "
             "[fleet report](fleet-report.md), these are published **verbatim** and *do* include "
             "homelab-internal architecture detail — but never credentials, keys, or secrets.")
    L.append("")
    L.append(f"**Generated:** {ts} · **{n} incident{'' if n == 1 else 's'} logged.**")
    L.append("")
    if not entries:
        L.append("_No incident reports logged yet._")
        L.append("")
    else:
        L.append("| Date | Incident | Summary |")
        L.append("|------|----------|---------|")
        for date, title, summary, fn in entries:
            L.append(f"| {date} | [{_esc(title)}](incidents/{fn}) | {_esc(summary)} |")
        L.append("")
    L.append("_Generated with Claude Code (Repo Claude)._")
    L.append("")
    return "\n".join(L)

# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", required=True, help="dotgithub checkout root to write into")
    ap.add_argument("--source-dir", default=None, help="dir of existing repo clones to reuse")
    ap.add_argument("--work-dir", default=None, help="scratch dir for shallow clones")
    ap.add_argument("--incidents-only", action="store_true",
                    help="regenerate only fleet-reports/incidents.md from local report files "
                         "(no gh/cloc needed — used when a new incident report is filed)")
    args = ap.parse_args()

    now = datetime.now(timezone.utc)
    ts = now.strftime("%Y-%m-%d %H:%M UTC")
    cutoff = (now - timedelta(days=ACTIVITY_WINDOW_DAYS)).strftime("%Y-%m-%dT%H:%M:%SZ")

    out = args.out_dir
    os.makedirs(os.path.join(out, "fleet-reports"), exist_ok=True)

    # Incident register — cheap (local files only), so always regenerated first.
    with open(os.path.join(out, "fleet-reports", "incidents.md"), "w") as f:
        f.write(build_incident_register(out, ts))
    print(f"wrote fleet-reports/incidents.md into {out}")
    if args.incidents_only:
        return

    repos = get_repos()
    work_dir = args.work_dir or tempfile.mkdtemp(prefix="fleet-census-")
    clones = ensure_clones(repos, args.source_dir, work_dir)

    fleet, per_repo, instr_files, LBL = run_census(repos, clones)
    open_issues, recent_closed, merged_prs, recent_open = get_issue_data(
        cutoff, {r["name"] for r in repos})
    report = render_report(fleet, per_repo, instr_files, LBL, repos, ts, cutoff,
                           open_issues, recent_closed, merged_prs, recent_open)

    path = os.path.join(out,"fleet-reports","fleet-report.md")
    with open(path,"w") as f: f.write(report)
    code_total = sum(s["lines"] for s in fleet["code"].values())
    print(f"wrote fleet-reports/fleet-report.md into {out}")
    print(f"  {len(open_issues)} open issues · {code_total:,} code lines")

if __name__ == "__main__":
    main()
