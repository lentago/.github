#!/usr/bin/env python3
"""Generate the Lentago Labs fleet report as GitHub-rendered Markdown.

Produces one file under the output tree:
  fleet-reports/fleet-report.md — a single combined report: open issues by repo +
                                  a 30-day activity snapshot, followed by a code census
                                  in which CLAUDE.md-family instruction markdown is
                                  counted as natural-language code (docs / content /
                                  data reported separately, excluded). Public data only.
  fleet-reports/epics.md        — the epics report: every tracking issue (labelled
                                  `epic`, or an open parent of sub-issues) with its
                                  sub-issue progress, the merged PRs of the window
                                  attributed to each, and the open issues no epic covers.
  fleet-reports/incidents.md    — the incident register, from the local report files.

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
DATA_DIR_PREFIX = {"homeassistant-config":("context/",)}
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
             "contents) — no personal, security, or on-prem-internal detail is included (on-prem: the machines in our own building). A prettier, editorialised "
             "copy renders on the on-prem LAN.")
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
             "window. Public metadata only — no transcript harvest, ops items, or on-prem detail (those live in "
             "the LAN copy).")
    L.append("- **Census tool:** `cloc`, run per-repo as `cloc --by-file --vcs=git` so only git-tracked files count "
             "(build output, `node_modules`, `.terraform`, venvs never enter). Lines are cloc *code* lines.")
    L.append("- **Scope:** the active repos owned by the `lentago` org, derived at runtime — personal repos and "
             "third-party clones are out of scope; archived repos are frozen and excluded.")
    L.append("- **Markdown classifier:** instruction-code = `CLAUDE.md`/`AGENTS.md`/`SKILL.md` or a versioned "
             "`prompts/*-auditor.md`; community-health = governance filenames + issue/PR templates; content = "
             "repo-scoped payload paths (ice-cream `recipes/`·manuscript, reference-checker "
             "`test-sets/`·`reports/`, dotgithub `fleet-reports/`); everything else = documentation.")
    L.append("- **Data / generated carve-outs:** exported payloads under the declared data dirs (homeassistant-config `context/`) count as data whatever their serialisation — JSON, JSONL, "
             "CSV/TSV, XML, YAML — as does reference-checker's rendered `reports/*.html`; lockfiles, SVG and "
             "`.github/brand/generated/` (emitted from `brand/fleet.json`) are "
             "generated. drosera's `dashboards/*.json` stay in code as Terraform-enforced dashboards-as-code.")
    L.append("- **Regenerating:** `python3 metrics/generate-fleet-reports.py --out-dir .`")
    L.append("")
    L.append("_Generated with Claude Code (Repo Claude)._")
    L.append("")
    return "\n".join(L)

# ---------------------------------------------------------------- incident register
# Incident reports are harvested from local session activity (the /incident-digest
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

# Deployment-causation marker: a bold labelled line, '**Deployment-caused:** yes|no|unknown',
# read by DORA's change-failure-rate / failed-deployment-recovery-time math. Missing or
# unparseable defaults to "unknown" — a silently wrong yes/no would corrupt those metrics,
# an "unknown" just leaves the question open.
DEPLOY_RE = re.compile(r"^\*\*Deployment-caused:\*\*\s*(yes|no|unknown)\s*$", re.M | re.I)
DEPLOY_LABEL = {"yes": "Yes", "no": "No", "unknown": "Unknown"}

def parse_incident(path):
    """Extract (title, summary, deploy_caused) from an incident report. Robust to the
    /incident-digest template: '# Incident Digest — <Title>, YYYY-MM-DD' then a
    '## TL;DR' or '## Summary', plus a '**Deployment-caused:** yes|no|unknown' marker."""
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
    dm = DEPLOY_RE.search(text)
    deploy = dm.group(1).lower() if dm else "unknown"
    return title, summary, deploy

def build_incident_register(out_dir, ts):
    inc_dir = os.path.join(out_dir, *INCIDENTS_DIR)
    entries = []
    if os.path.isdir(inc_dir):
        for fn in os.listdir(inc_dir):
            if not fn.endswith(".md") or fn.lower() in ("readme.md", "index.md"):
                continue
            m = re.match(r"(\d{4}-\d{2}-\d{2})-.+\.md$", fn)
            date = m.group(1) if m else "—"
            title, summary, deploy = parse_incident(os.path.join(inc_dir, fn))
            entries.append((date, title, summary, fn, deploy))
    entries.sort(key=lambda e: (e[0], e[3]), reverse=True)
    n = len(entries)
    yes_n = sum(1 for e in entries if e[4] == "yes")
    no_n = sum(1 for e in entries if e[4] == "no")
    unk_n = sum(1 for e in entries if e[4] == "unknown")
    L = []
    L.append("# Lentago Labs Incident Register")
    L.append("")
    L.append("> [!NOTE]")
    L.append("> **Co-authored with [Claude](https://claude.ai)** (the `/incident-digest` playbook). "
             "A chronological register of incident reports harvested from local session activity "
             "and published as a periodic fleet report. Each row links to the full write-up under "
             "[`fleet-reports/incidents/`](incidents/). Unlike the "
             "[fleet report](fleet-report.md), these are published **verbatim** and *do* include "
             "on-prem-internal architecture detail (on-prem: the machines in our own building) — but never credentials, keys, or secrets.")
    L.append("")
    L.append(f"**Generated:** {ts} · **{n} incident{'' if n == 1 else 's'} logged.**")
    L.append("")
    if not entries:
        L.append("_No incident reports logged yet._")
        L.append("")
    else:
        L.append(f"**Deployment-caused:** {yes_n} yes · {no_n} no · {unk_n} unknown — the DORA "
                 "change-failure-rate / failed-deployment-recovery-time inputs; each report's "
                 "`Deployment-caused` marker feeds this line.")
        L.append("")
        L.append("| Date | Incident | Deploy-caused | Summary |")
        L.append("|------|----------|:---:|---------|")
        for date, title, summary, fn, deploy in entries:
            L.append(f"| {date} | [{_esc(title)}](incidents/{fn}) | {DEPLOY_LABEL[deploy]} | {_esc(summary)} |")
        L.append("")
    L.append("_Generated with Claude Code (Repo Claude)._")
    L.append("")
    return "\n".join(L)

# ---------------------------------------------------------------- epics report
# The third periodic fleet report: fleet-reports/epics.md. An *epic* is a tracking
# issue — one labelled `epic`, or an open issue that has sub-issues and no parent
# of its own. Progress is GitHub's own sub-issue count (native parent/child links,
# which cross repos inside the org) plus the body checklist. The report also
# attributes the window's merged PRs to epics, so the share of real work an epic
# accounts for is visible — and so is the complement: the work no epic describes.
# Public metadata only, like fleet-report.md. Needs gh, not cloc (--epics-only).
EPIC_LABEL = "epic"
EPIC_CLOSED_WINDOW_DAYS = 90   # closed epics stay on the report this long
TREE_DEPTH = 3                 # sub-issue nesting followed below an epic
DEFACTO_MIN_PRS = 4            # a loose issue this many merged PRs cite is a de-facto epic
LIST_CAP = 500                 # per-repo issue listings
SEARCH_CAP = 1000              # org-wide searches (gh's maximum)

def _issues_disabled(exc):
    return "disabled issues" in str(exc)

def _check_cap(items, cap, what):
    """A capped listing that fills its cap may have dropped rows; the report must not
    publish a silently thinner picture, so stop instead."""
    if len(items) >= cap:
        raise RuntimeError(f"{what}: {len(items)} rows hit the cap of {cap}; raise the cap")

def gh_api(path):
    out = sh(["gh", "api", path])
    return json.loads(out) if out.strip() else []

def _repo_of(repository_url):
    return repository_url.rstrip("/").rsplit("/", 1)[1]

CHECK_RE = re.compile(r"^\s*[-*]\s+\[([ xX])\]", re.M)
def checklist(body):
    marks = CHECK_RE.findall(body or "")
    return sum(1 for m in marks if m in "xX"), len(marks)

# Issue/PR references in free text: a github.com URL, `repo#N` / `lentago/repo#N`
# (a repo name may start with a dot, as `.github` does), or a bare `#N` in the
# text's own repo. Numbers alone cannot tell an issue from a PR; callers resolve
# that against the sets they hold.
REF_RE = re.compile(r"https://github\.com/lentago/([\w.-]+)/(?:issues|pull)/(\d+)"
                    r"|(?<![\w/])(?:lentago/)?([\w.-]+)#(\d+)"
                    r"|(?<![\w/#])#(\d+)")
def refs(text, repo):
    out = set()
    for m in REF_RE.finditer(text or ""):
        if m.group(1): out.add((m.group(1), int(m.group(2))))
        elif m.group(3): out.add((m.group(3).rstrip("."), int(m.group(4))))
        else: out.add((repo, int(m.group(5))))
    return out

def _first_para(body, limit=320):
    for para in re.split(r"\n\s*\n", body or ""):
        p = para.strip()
        if not p or p[0] in "#>|-*!<[" or p.startswith("```"):
            continue
        return _first_sentence(_strip_md(p), limit)
    return ""

def list_open_issues(repos):
    """Every open issue in the public fleet, with its parent and sub-issue summary."""
    out = []
    for r in repos:
        try:
            data = gh_json(["issue", "list", "--repo", f"lentago/{r['name']}", "--state", "open",
                            "--limit", str(LIST_CAP), "--json",
                            "number,title,labels,createdAt,updatedAt,url,parent,subIssuesSummary"])
        except RuntimeError as exc:
            if _issues_disabled(exc):
                continue   # the uvularia templates have issues disabled: nothing to list
            raise          # a rate limit or auth failure must stop the run, not thin the report
        _check_cap(data, LIST_CAP, f"open issues of {r['name']}")
        for i in data:
            i["repo"] = r["name"]
            out.append(i)
    return out

def fetch_tree(repo, number, depth=0):
    kids = gh_api(f"repos/lentago/{repo}/issues/{number}/sub_issues?per_page=100")
    nodes = []
    for k in kids:
        kr = _repo_of(k["repository_url"])
        node = {"repo": kr, "number": k["number"], "title": k["title"], "state": k["state"],
                "url": k["html_url"], "closed_at": (k.get("closed_at") or "")[:10], "children": []}
        if (k.get("sub_issues_summary") or {}).get("total", 0) and depth < TREE_DEPTH:
            node["children"] = fetch_tree(kr, k["number"], depth + 1)
        nodes.append(node)
    return nodes

def flatten(nodes):
    for n in nodes:
        yield n
        yield from flatten(n["children"])

def discover_epics(repos, open_issues, cutoff_closed):
    """Labelled epics (open, or closed inside the window) plus unlabelled parents:
    open issues with sub-issues and no parent. Scoped to the public fleet."""
    names = {r["name"] for r in repos}
    found = set()
    for state, extra in (("open", []), ("closed", ["--closed", f">={cutoff_closed[:10]}"])):
        hits = gh_json(["search", "issues", "--owner", "lentago", "--label", EPIC_LABEL,
                        "--state", state, "--limit", str(SEARCH_CAP), "--json", "repository,number"] + extra)
        _check_cap(hits, SEARCH_CAP, f"{state} epics")
        for i in hits:
            if i["repository"]["name"] in names:
                found.add((i["repository"]["name"], i["number"]))
    has_parent = {(i["repo"], i["number"]) for i in open_issues if i.get("parent")}
    for i in open_issues:
        if (i.get("subIssuesSummary") or {}).get("total", 0) and not i.get("parent"):
            found.add((i["repo"], i["number"]))
    # Closed parents inside the window count too, label or not: an epic that closed
    # with sub-issues still open is a hand-off the report should show.
    for r in repos:
        try:
            closed = gh_json(["issue", "list", "--repo", f"lentago/{r['name']}", "--state", "closed",
                              "--limit", str(LIST_CAP), "--search", f"closed:>={cutoff_closed[:10]}",
                              "--json", "number,parent,subIssuesSummary"])
        except RuntimeError as exc:
            if _issues_disabled(exc):
                continue
            raise
        _check_cap(closed, LIST_CAP, f"closed issues of {r['name']}")
        for i in closed:
            if (i.get("subIssuesSummary") or {}).get("total", 0) and not i.get("parent"):
                found.add((r["name"], i["number"]))
    # A labelled *open* epic that itself sits under a parent renders there, not at top
    # level. has_parent is built from the open listing only, so a closed labelled epic
    # under a parent would still surface at top level — acceptable for a hand-off view.
    return sorted(k for k in found if k not in has_parent)

def build_epic(repo, number):
    iss = gh_api(f"repos/lentago/{repo}/issues/{number}")
    body = iss.get("body") or ""
    comments = sh(["gh", "api", f"repos/lentago/{repo}/issues/{number}/comments",
                   "--paginate", "--jq", ".[].body"], check=False)
    tree = fetch_tree(repo, number)
    kids = list(flatten(tree))
    done, total = checklist(body)
    return {"repo": repo, "number": number, "title": iss["title"], "state": iss["state"],
            "url": iss["html_url"], "created": iss["created_at"][:10],
            "updated": iss["updated_at"][:10], "closed": (iss.get("closed_at") or "")[:10],
            "summary": _first_para(body), "check": (done, total), "tree": tree, "kids": kids,
            "kids_open": sum(1 for k in kids if k["state"] == "open"),
            "kids_closed": sum(1 for k in kids if k["state"] != "open"),
            "cites_body": refs(body, repo), "cites_comments": refs(comments, repo)}

def get_merged_prs(cutoff_iso, fleet_names):
    prs = gh_json(["search", "prs", "--owner", "lentago", "--merged", "--merged-at",
                   f">={cutoff_iso[:10]}", "--limit", str(SEARCH_CAP),
                   "--json", "repository,number,title,closedAt,body,author,url"])
    _check_cap(prs, SEARCH_CAP, "merged PRs in the window")
    return [p for p in prs if p["repository"]["name"] in fleet_names
            and p.get("closedAt", "") >= cutoff_iso]

def attribute_prs(prs, epics):
    """Each merged PR lands in exactly one place: an epic (several, if it serves
    several), or one of four loose buckets. A PR counts toward an epic when the
    epic's body or comments cite it, or when its own body references an issue in
    the epic's sub-issue tree (or the epic itself)."""
    issue_to_epic, pr_cited = {}, {}
    for e in epics:
        key = (e["repo"], e["number"])
        issue_to_epic[key] = key
        for k in e["kids"]:
            issue_to_epic[(k["repo"], k["number"])] = key
        for ref in e["cites_body"]:
            pr_cited.setdefault(ref, set()).add((key, "body"))
        for ref in e["cites_comments"]:
            pr_cited.setdefault(ref, set()).add((key, "comments"))
    prset = {(p["repository"]["name"], p["number"]) for p in prs}
    per_epic = defaultdict(list)
    comments_only = defaultdict(int)
    buckets = {"deps": [], "automation": [], "loose_issue": [], "no_issue": []}
    loose_hits = defaultdict(list)
    for p in prs:
        key = (p["repository"]["name"], p["number"])
        login = (p.get("author") or {}).get("login", "")
        if login == "dependabot[bot]" or p["title"].startswith(("build(deps)", "chore(deps)")):
            buckets["deps"].append(p); continue
        if (login.endswith("[bot]") and login != "lentago-claude-runner[bot]") \
                or p["title"].startswith("Weekly fleet reports refresh"):
            buckets["automation"].append(p); continue
        hits = set()
        if key in pr_cited:
            wheres = {w for _, w in pr_cited[key]}
            for ek, _ in pr_cited[key]:
                hits.add(ek)
                if wheres == {"comments"}: comments_only[ek] += 1
        irs = [r for r in refs(p.get("body"), key[0]) if r not in prset]
        for r in irs:
            if r in issue_to_epic: hits.add(issue_to_epic[r])
        if hits:
            for ek in hits: per_epic[ek].append(p)
        elif irs:
            buckets["loose_issue"].append(p)
            for r in irs: loose_hits[r].append(p)
        else:
            buckets["no_issue"].append(p)
    return per_epic, buckets, loose_hits, comments_only, issue_to_epic

def _bar(done, total, width=10):
    if not total: return "·" * width
    filled = round(width * done / total)
    return "█" * filled + "░" * (width - filled)

def _ref(repo, number, url=None):
    url = url or f"https://github.com/lentago/{repo}/issues/{number}"
    return f"[{repo}#{number}]({url})"

def _render_tree(nodes, L, indent=0):
    for n in sorted(nodes, key=lambda n: (n["state"] != "open", n["repo"], n["number"])):
        mark = "⬜" if n["state"] == "open" else "✅"
        sub = ""
        if n["children"]:
            c = list(flatten(n["children"]))
            sub = f" — {sum(1 for k in c if k['state'] != 'open')}/{len(c)} sub-issues closed"
        L.append(f"{'  ' * indent}- {mark} {_ref(n['repo'], n['number'], n['url'])} {_esc(n['title'])}{sub}")
        if n["children"]:
            _render_tree(n["children"], L, indent + 1)

def build_epics_report(ts, cutoff, repos, open_issues, epics, prs, attribution):
    per_epic, buckets, loose_hits, comments_only, issue_to_epic = attribution
    open_epics = [e for e in epics if e["state"] == "open"]
    closed_epics = [e for e in epics if e["state"] != "open"]
    epic_keys = {(e["repo"], e["number"]) for e in epics}
    covered = {k for k in issue_to_epic if k not in epic_keys}
    outside = [i for i in open_issues
               if (i["repo"], i["number"]) not in covered and (i["repo"], i["number"]) not in epic_keys]
    n_open_issues = len(open_issues)
    n_epic_issues = sum(1 for i in open_issues if (i["repo"], i["number"]) in epic_keys)
    n_under = n_open_issues - n_epic_issues - len(outside)
    n_prs = len(prs)
    n_epic_prs = len({(p["repository"]["name"], p["number"]) for l in per_epic.values() for p in l})
    n_bots = len(buckets["deps"]) + len(buckets["automation"])
    n_work = n_prs - n_bots
    pct = lambda a, b: f"{100 * a / b:.0f}%" if b else "—"

    L = []
    L.append("# Lentago Labs Epics Report")
    L.append("")
    L.append("> [!NOTE]")
    L.append("> **Co-authored with [Claude](https://claude.ai)** (Repo Claude, the Lentago Labs fleet steward). "
             "Auto-generated weekly from the fleet's public state. An **epic** here is a tracking issue: one "
             f"labelled `{EPIC_LABEL}`, or an open issue with sub-issues and no parent of its own. Progress is "
             "GitHub's own sub-issue count plus the issue's checklist, so an epic that is not kept up to date "
             "shows as not moving — that is the point. The sibling [fleet report](fleet-report.md) lists every "
             "open issue; this one asks what the issues add up to, and how much of the merged work they describe.")
    L.append("")
    L.append(f"**Generated:** {ts} · Scope: the **{len(repos)} active** `lentago` repos · "
             f"Merged-PR window: last {ACTIVITY_WINDOW_DAYS} days (since {cutoff[:10]}) · "
             f"closed epics shown for {EPIC_CLOSED_WINDOW_DAYS} days.")
    L.append("")
    L.append("## Snapshot")
    L.append("")
    L.append("| Open epics | Closed epics (90d) | Open issues under an epic | Merged PRs (30d) | …that trace to an epic | …loose, with an issue | …loose, no issue | …bots |")
    L.append("|---:|---:|---:|---:|---:|---:|---:|---:|")
    n_rest = n_open_issues - n_epic_issues
    L.append(f"| **{len(open_epics)}** | {len(closed_epics)} | **{n_under} / {n_rest}** ({pct(n_under, n_rest)}) | "
             f"{n_prs} | **{n_epic_prs}** ({pct(n_epic_prs, n_work)} of non-bot) | {len(buckets['loose_issue'])} | "
             f"{len(buckets['no_issue'])} | {n_bots} |")
    L.append("")
    L.append("The *trace to an epic* share is the headline: how much of the month's merged work the epics describe. "
             "The two loose columns are work that happened outside any epic — tracked by a stand-alone issue, or by "
             "nothing but the PR. Bots are Dependabot and the fleet's own automation, excluded from the share. "
             "*Open issues under an epic* counts the issues other than the epics themselves; its complement is the "
             "list at the end.")
    L.append("")
    L.append("---")
    L.append("")
    # ---- open epics table
    L.append(f"## Open epics — {len(open_epics)}")
    L.append("")
    L.append("| Epic | Since | Sub-issues closed | Checklist | PRs (30d) | Last activity |")
    L.append("|------|-------|-------------------|-----------|----------:|---------------|")
    for e in sorted(open_epics, key=lambda e: (-len(per_epic.get((e["repo"], e["number"]), [])), e["repo"], e["number"])):
        key = (e["repo"], e["number"])
        kc, kt = e["kids_closed"], len(e["kids"])
        cd, ct = e["check"]
        subs = f"`{_bar(kc, kt)}` {kc}/{kt}" if kt else "—"
        chk = f"{cd}/{ct}" if ct else "—"
        note = ""
        if comments_only.get(key):
            note = f" ⚠︎ {comments_only[key]} known from comments only"
        L.append(f"| {_ref(*key, e['url'])} {_esc(e['title'])} | {e['created']} | {subs} | {chk} | "
                 f"{len(per_epic.get(key, []))}{note} | {e['updated']} |")
    L.append("")
    L.append("*Sub-issues closed* is GitHub's native parent/child count (it crosses repos). *Checklist* is the "
             "`- [ ]` boxes in the epic's body. ⚠︎ counts merged PRs this report could attribute to the epic only "
             "because a comment on the epic cites them: neither the body nor a sub-issue names them, so a reader "
             "of the epic's face would miss that work.")
    L.append("")
    # ---- per-epic detail
    for e in sorted(open_epics, key=lambda e: (e["repo"], e["number"])):
        key = (e["repo"], e["number"])
        L.append(f"### {_esc(e['title'])}")
        L.append("")
        L.append(f"{_ref(*key, e['url'])} · open since {e['created']} · last activity {e['updated']}")
        L.append("")
        if e["summary"]:
            L.append(f"> {_esc(e['summary'])}")
            L.append("")
        kc, kt = e["kids_closed"], len(e["kids"])
        cd, ct = e["check"]
        bits = []
        if kt: bits.append(f"**{kc}/{kt}** sub-issues closed")
        if ct: bits.append(f"checklist **{cd}/{ct}**")
        n = len(per_epic.get(key, []))
        bits.append(f"**{n}** PR{'s' if n != 1 else ''} merged in the window")
        L.append("Progress: " + " · ".join(bits))
        L.append("")
        if e["tree"]:
            L.append("<details><summary>Sub-issues</summary>")
            L.append("")
            _render_tree(e["tree"], L)
            L.append("")
            L.append("</details>")
            L.append("")
        else:
            L.append("_No sub-issues linked — progress is visible only through the checklist and cited PRs._")
            L.append("")
        if per_epic.get(key):
            L.append("<details><summary>Merged PRs attributed (30d)</summary>")
            L.append("")
            for p in sorted(per_epic[key], key=lambda p: p["closedAt"], reverse=True):
                r = p["repository"]["name"]
                L.append(f"- {p['closedAt'][:10]} · [{r}#{p['number']}]({p['url']}) — {_esc(p['title'])}")
            L.append("")
            L.append("</details>")
            L.append("")
    L.append("---")
    L.append("")
    # ---- closed epics
    L.append(f"## Closed in the last {EPIC_CLOSED_WINDOW_DAYS} days — {len(closed_epics)}")
    L.append("")
    if not closed_epics:
        L.append("_None._")
        L.append("")
    else:
        L.append("| Closed | Epic | Sub-issues | Still open underneath | PRs (30d) |")
        L.append("|--------|------|-----------:|----------------------:|----------:|")
        for e in sorted(closed_epics, key=lambda e: e["closed"], reverse=True):
            key = (e["repo"], e["number"])
            left = e["kids_open"]
            L.append(f"| {e['closed']} | {_ref(*key, e['url'])} {_esc(e['title'])} | {len(e['kids'])} | "
                     f"{'**' + str(left) + '**' if left else '0'} | {len(per_epic.get(key, []))} |")
        L.append("")
        L.append("A closed epic with open sub-issues is a hand-off: the work was spun out and still owes a result.")
        L.append("")
    L.append("---")
    L.append("")
    # ---- coverage
    L.append(f"## Where the last {ACTIVITY_WINDOW_DAYS} days went")
    L.append("")
    L.append(f"**{n_prs} PRs merged** across the fleet. Each is attributed once (an epic, or one loose bucket); "
             "a PR that serves two epics counts for both.")
    L.append("")
    L.append("| Destination | PRs | Share |")
    L.append("|-------------|----:|------:|")
    rows = sorted(per_epic.items(), key=lambda kv: -len(kv[1]))
    for key, l in rows:
        e = next(x for x in epics if (x["repo"], x["number"]) == key)
        tag = "" if e["state"] == "open" else " _(closed)_"
        L.append(f"| {_ref(*key, e['url'])} {_esc(e['title'])}{tag} | {len(l)} | {pct(len(l), n_prs)} |")
    L.append(f"| **All epics** | **{n_epic_prs}** | **{pct(n_epic_prs, n_prs)}** |")
    L.append(f"| Loose — closes or cites an issue outside any epic | {len(buckets['loose_issue'])} | {pct(len(buckets['loose_issue']), n_prs)} |")
    L.append(f"| Loose — no issue reference at all | {len(buckets['no_issue'])} | {pct(len(buckets['no_issue']), n_prs)} |")
    L.append(f"| Dependabot | {len(buckets['deps'])} | {pct(len(buckets['deps']), n_prs)} |")
    L.append(f"| Fleet automation (report refreshes, template sync) | {len(buckets['automation'])} | {pct(len(buckets['automation']), n_prs)} |")
    L.append("")
    # de-facto epics
    defacto = [(r, l) for r, l in loose_hits.items() if len(l) >= DEFACTO_MIN_PRS]
    if defacto:
        L.append("### De-facto epics")
        L.append("")
        L.append(f"Issues outside any epic that at least {DEFACTO_MIN_PRS} merged PRs reference. Each is a campaign "
                 "that ran on a single issue; if it is still open, it is a candidate for the `epic` label or a parent.")
        L.append("")
        L.append("| Issue | PRs | Repos touched | State |")
        L.append("|-------|----:|--------------:|-------|")
        for (r, n), l in sorted(defacto, key=lambda kv: -len(kv[1])):
            try:
                iss = gh_api(f"repos/lentago/{r}/issues/{n}")
                title, state = iss["title"], iss["state"]
            except Exception:
                title, state = "(not readable)", "?"
            repos_touched = len({p["repository"]["name"] for p in l})
            L.append(f"| {_ref(r, n)} {_esc(title)} | {len(l)} | {repos_touched} | {state} |")
        L.append("")
    # untracked by repo
    loose_all = buckets["loose_issue"] + buckets["no_issue"]
    if loose_all:
        by_repo = defaultdict(lambda: [0, 0])
        for p in buckets["loose_issue"]: by_repo[p["repository"]["name"]][0] += 1
        for p in buckets["no_issue"]: by_repo[p["repository"]["name"]][1] += 1
        L.append("### Loose work by repo")
        L.append("")
        L.append("Where the merged work that no epic describes landed. A tall row is either a program that deserves "
                 "an epic, or a repo whose convention is direct PRs.")
        L.append("")
        L.append("| Repo | With an issue | No issue | Total |")
        L.append("|------|--------------:|---------:|------:|")
        for r, (a, b) in sorted(by_repo.items(), key=lambda kv: -(kv[1][0] + kv[1][1])):
            L.append(f"| {r} | {a} | {b} | **{a + b}** |")
        L.append("")
    L.append("---")
    L.append("")
    # ---- outside any epic
    by_repo = defaultdict(list)
    for i in outside: by_repo[i["repo"]].append(i)
    L.append(f"## Open issues outside any epic — {len(outside)}")
    L.append("")
    L.append("The backlog the epics do not describe. Some of it is deliberately small and stand-alone; the rest is "
             "either a program without a parent or an issue that should be linked under one.")
    L.append("")
    for r in sorted(by_repo, key=lambda r: (-len(by_repo[r]), r)):
        L.append(f"**{r}** — {len(by_repo[r])}")
        L.append("")
        for i in sorted(by_repo[r], key=lambda i: -i["number"]):
            L.append(f"- [{r}#{i['number']}]({i['url']}) {_esc(i['title'])} _(since {i['createdAt'][:10]})_")
        L.append("")
    L.append("---")
    L.append("")
    L.append("## Method")
    L.append("")
    L.append(f"- **Epics:** `gh search issues --owner lentago --label {EPIC_LABEL}` (open, plus closed within "
             f"{EPIC_CLOSED_WINDOW_DAYS} days) ∪ every issue with sub-issues and no parent that is open or closed "
             f"within those {EPIC_CLOSED_WINDOW_DAYS} days. A labelled open epic that sits under a parent renders "
             "there, not at top level; a closed one is taken at top level, since the closed listing carries no "
             "parent field this report reads.")
    L.append(f"- **Sub-issues:** GitHub's native parent/child links, read through the REST `sub_issues` endpoint "
             f"and followed {TREE_DEPTH} levels deep. They cross repos inside the org. Link one with "
             "`gh api -X POST repos/lentago/<repo>/issues/<epic>/sub_issues -F sub_issue_id=<child id>`.")
    L.append("- **Attribution:** a merged PR counts toward an epic when the epic's body or comments cite the PR, or "
             "when the PR's body references an issue in the epic's tree (or the epic itself). Otherwise it is loose: "
             "with an issue, or without one. Dependabot and the fleet's own bots are set aside.")
    L.append("- **Limits:** a citation is a citation — an epic that mentions a PR as an example counts it as work. "
             "An issue cannot have two parents, so a piece of work that serves two programs sits under one; the "
             "other may still cite it.")
    L.append("- **Regenerating:** `python3 metrics/generate-fleet-reports.py --out-dir . --epics-only` "
             "(needs `gh`, not `cloc`).")
    L.append("")
    L.append("_Generated with Claude Code (Repo Claude)._")
    L.append("")
    return "\n".join(L)

def run_epics(out_dir, ts, cutoff, repos):
    cutoff_closed = (datetime.now(timezone.utc) - timedelta(days=EPIC_CLOSED_WINDOW_DAYS)).strftime("%Y-%m-%dT%H:%M:%SZ")
    names = {r["name"] for r in repos}
    open_issues = list_open_issues(repos)
    keys = discover_epics(repos, open_issues, cutoff_closed)
    epics = [build_epic(r, n) for r, n in keys]
    prs = get_merged_prs(cutoff, names)
    attribution = attribute_prs(prs, epics)
    report = build_epics_report(ts, cutoff, repos, open_issues, epics, prs, attribution)
    path = os.path.join(out_dir, "fleet-reports", "epics.md")
    with open(path, "w") as f: f.write(report)
    print(f"wrote fleet-reports/epics.md into {out_dir}")
    print(f"  {sum(1 for e in epics if e['state']=='open')} open epics · {len(prs)} merged PRs attributed")


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", required=True, help="dotgithub checkout root to write into")
    ap.add_argument("--source-dir", default=None, help="dir of existing repo clones to reuse")
    ap.add_argument("--work-dir", default=None, help="scratch dir for shallow clones")
    ap.add_argument("--incidents-only", action="store_true",
                    help="regenerate only fleet-reports/incidents.md from local report files "
                         "(no gh/cloc needed — used when a new incident report is filed)")
    ap.add_argument("--epics-only", action="store_true",
                    help="regenerate only fleet-reports/epics.md (needs gh, not cloc)")
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
    if args.epics_only:
        run_epics(out, ts, cutoff, repos)
        return
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
    run_epics(out, ts, cutoff, repos)

if __name__ == "__main__":
    main()
