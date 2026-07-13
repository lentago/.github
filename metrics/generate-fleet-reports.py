#!/usr/bin/env python3
"""Generate the Lentago Labs fleet reports as GitHub-rendered Markdown.

Produces two files under the output tree:
  metrics/code-census.md        — languages across the fleet, with CLAUDE.md-family
                                   instruction markdown counted as natural-language code
                                   (docs / content / data reported separately, excluded).
  fleet-reports/fleet-issue-report.md — open issues by repo + a 7-day activity snapshot,
                                   from public GitHub metadata only.

Scope: every repo whose owner is the `lentago` org (derived at runtime — new/renamed
repos are picked up automatically). Third-party clones and personal repos are excluded
by construction. Run locally over an existing working tree, or in CI where it shallow-
clones each repo itself.

Usage:
  gen.py --out-dir <dotgithub-checkout> [--source-dir <dir-of-clones>] [--work-dir <tmp>]

If --source-dir is given and contains the clones, they're reused (fast local runs).
Otherwise every lentago repo is shallow-cloned into --work-dir (default: a temp dir).
Requires: git, gh (authenticated), cloc.
"""
import argparse, json, os, subprocess, sys, tempfile, shutil
from collections import defaultdict
from datetime import datetime, timezone, timedelta

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
    """Active (non-archived) lentago-org repos.

    Scope note: GitHub's org-listing/search endpoints do not surface archived repos
    for this account, so the reliable, self-maintaining scope is the active fleet.
    Archived repos are frozen code anyway — no reason to re-count them weekly. The
    endpoint returns non-archived repos; we carry the flag for forward-compatibility.
    """
    raw = sh(["gh","api","orgs/lentago/repos","--paginate",
              "--jq",".[] | {name:.name, isArchived:.archived}"])
    data = [json.loads(line) for line in raw.splitlines() if line.strip()]
    return sorted(data, key=lambda r: r["name"])

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
DATA_JSON_PREFIX = {"music-curator":("data/",), "homeassistant-config":("context/",)}

def is_generated(base):
    if base in GEN_BASENAMES: return True
    if os.path.splitext(base)[1] in GEN_EXT: return True
    if ".min." in base: return True
    return False

def is_data(repo, path):
    p = path[2:] if path.startswith("./") else path
    low = p.lower()
    if low.endswith(".json") and any(p.startswith(x) for x in DATA_JSON_PREFIX.get(repo,())):
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
            elif is_generated(base):
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

# ---------------------------------------------------------------- census markdown
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

def render_census(fleet, per_repo, instr_files, INSTR_LABEL, repos, ts):
    code_total = sum(s["lines"] for s in fleet["code"].values())
    code_files = sum(s["files"] for s in fleet["code"].values())
    instr = fleet["code"].get(INSTR_LABEL, {"files":0,"lines":0})
    hyg = [f for f in instr_files if f[3]=="hygiene"]
    prm = [f for f in instr_files if f[3]=="prompt"]
    hyg_l = sum(f[2] for f in hyg); prm_l = sum(f[2] for f in prm)
    md = fleet["md"]; md_total = sum(md[b]["lines"] for b in md); md_files = sum(md[b]["files"] for b in md)
    arch = {r["name"] for r in repos if r["isArchived"]}
    L = []
    L.append("# Lentago Labs Fleet — Code Census")
    L.append("")
    L.append("> [!NOTE]")
    L.append("> **Co-authored with [Claude](https://claude.ai)** (Repo Claude, the Lentago Labs fleet steward). "
             "Auto-generated weekly from public repo contents — no personal or security detail is included. "
             "A companion, prettier copy renders on the Lentago lab LAN.")
    L.append("")
    L.append(f"**Generated:** {ts} · Tool: `cloc` · Scope: the **{len(repos)} active** `lentago` repos, measured over their default branches. "
             "The 3 archived repos (`office-presence`, `site-pitzilabs-dev`, `workstation-bootstrap`) are frozen and excluded.")
    L.append("")
    L.append("**The lens:** a `CLAUDE.md` (and its kin — `AGENTS.md`, skill `SKILL.md`, and the LLM prompt-programs "
             "that *are* a tool's logic) is an instruction set maintained for hygiene, so it's counted as "
             "**natural-language code**. Documentation, content/data, and community-health markdown are tallied "
             "separately and excluded from the code total, as are data payloads and generated files. This is a "
             "deliberate re-cut of the canonical [`metrics/language-census.md`](language-census.md), which instead "
             "counts all Markdown/JSON/HTML as code.")
    L.append("")
    L.append(f"**Headline:** the fleet's hand-maintained natural-language instruction surface "
             f"(**{instr['lines']:,} lines**) is among the largest \"languages\" in the code base. One repo — "
             f"`reference-checker` — is almost entirely natural-language source: its auditor is a prompt program.")
    L.append("")
    # KPIs
    L.append("| Code (incl. instructions) | Instruction-markdown | Repos | Data excluded | Generated excluded |")
    L.append("|---:|---:|---:|---:|---:|")
    L.append(f"| **{code_total:,}** | **{instr['lines']:,}** ({instr['files']} files) | {len(repos)} | "
             f"{fleet['data']['lines']:,} | {fleet['generated']['lines']:,} |")
    L.append("")
    # language table
    L.append("## 1 — Languages")
    L.append("")
    L.append("cloc *code* lines (blank + comment excluded). Shell folds Bourne + Bash. Instruction-markdown is "
             "promoted into the count (**bold**); the excluded buckets sit below the total.")
    L.append("")
    L.append("| # | Language | Code | Files | Share |")
    L.append("|---|----------|-----:|------:|------:|")
    rows = fold_langs(fleet["code"])
    for i,(lang,s) in enumerate(rows,1):
        pct = 100*s["lines"]/code_total if code_total else 0
        name = f"**{lang}**" if lang.startswith("Instructions") else lang
        L.append(f"| {i} | {name} | {s['lines']:,} | {s['files']} | {pct:.1f}% |")
    L.append(f"| | **CODE TOTAL** | **{code_total:,}** | **{code_files}** | 100% |")
    L.append(f"| — | _Data / exports — excluded_ | {fleet['data']['lines']:,} | {fleet['data']['files']} | — |")
    L.append(f"| — | _Generated (lockfiles, SVG) — excluded_ | {fleet['generated']['lines']:,} | {fleet['generated']['files']} | — |")
    L.append("")
    # instruction deep dive
    L.append("## 2 — Instruction-markdown as code")
    L.append("")
    L.append(f"- **Hygiene family** ({len(hyg)} files · `CLAUDE.md`, `AGENTS.md`, `SKILL.md`): **{hyg_l:,} lines**")
    L.append(f"- **Prompt-programs** ({len(prm)} files · reference-checker auditors): **{prm_l:,} lines**")
    L.append("")
    L.append("### 2a — The hygiene surface (each file is a maintenance obligation)")
    L.append("")
    L.append("| Repo | File | Lines |")
    L.append("|------|------|------:|")
    for repo,path,code,_ in sorted(hyg, key=lambda x:-x[2]):
        tag = " _(archived)_" if repo in arch else ""
        L.append(f"| {repo}{tag} | `{os.path.basename(path)}` | {code} |")
    L.append(f"| **{len(hyg)} files** | | **{hyg_l:,}** |")
    L.append("")
    if prm:
        L.append("### 2b — Prompt-programs (natural language *is* the logic)")
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
    # per-repo
    L.append("## 3 — Per-repo")
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
    # markdown taxonomy
    L.append("## 4 — Markdown taxonomy")
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
    # method
    L.append("## Method & reproducibility")
    L.append("")
    L.append("- **Tool:** `cloc`, run per-repo as `cloc --by-file --vcs=git` so only git-tracked files count "
             "(build output, `node_modules`, `.terraform`, venvs never enter). Lines are cloc *code* lines.")
    L.append("- **Scope:** the active repos owned by the `lentago` org, derived at runtime — personal repos and "
             "third-party clones are out of scope by construction; archived repos are frozen and excluded.")
    L.append("- **Markdown classifier:** instruction-code = `CLAUDE.md`/`AGENTS.md`/`SKILL.md` or a versioned "
             "`prompts/*-auditor.md`; community-health = the standard governance filenames + issue/PR templates; "
             "content = repo-scoped payload paths (music-curator `vault/`, ice-cream `recipes/`·manuscript, "
             "reference-checker `test-sets/`·`reports/`, dotgithub `fleet-reports/`); everything else = documentation.")
    L.append("- **Data / generated carve-outs:** large exported JSON (music-curator `data/`, homeassistant-config "
             "`context/`) and reference-checker's rendered `reports/*.html` are data/output, not code; lockfiles and "
             "SVG are generated. drosera's `dashboards/*.json` stay in code as Terraform-enforced dashboards-as-code.")
    L.append("- **Regenerating:** `python3 metrics/generate-fleet-reports.py --out-dir .` (see the script header).")
    L.append("")
    L.append("_Generated with Claude Code (Repo Claude)._")
    L.append("")
    return "\n".join(L)

# ---------------------------------------------------------------- issue report
def get_issue_data(cutoff_iso):
    open_issues = gh_json(["search","issues","--owner","lentago","--state","open","--limit","200",
                           "--json","repository,number,title,createdAt,updatedAt"])
    closed = gh_json(["search","issues","--owner","lentago","--state","closed","--limit","100",
                      "--json","repository,number,title,closedAt"])
    prs = gh_json(["search","prs","--owner","lentago","--merged","--merged-at",f">={cutoff_iso[:10]}",
                   "--limit","150","--json","repository,number,title,closedAt"])
    recent_closed = [i for i in closed if i.get("closedAt","") >= cutoff_iso]
    recent_open = [i for i in open_issues if i.get("createdAt","") >= cutoff_iso]
    return open_issues, recent_closed, prs, recent_open

def render_issue_report(open_issues, recent_closed, merged_prs, recent_open, ts, cutoff_iso):
    by_repo = defaultdict(list)
    for i in open_issues: by_repo[i["repository"]["name"]].append(i)
    L = []
    L.append("# Lentago Labs Fleet — Issue Report")
    L.append("")
    L.append("> [!NOTE]")
    L.append("> **Co-authored with [Claude](https://claude.ai)** (Repo Claude, the Lentago Labs fleet steward). "
             "Auto-generated weekly from public GitHub metadata (issues + merged PRs) — no personal, security, or "
             "homelab-internal detail is included. A prettier, editorialised copy renders on the Lentago lab LAN.")
    L.append("")
    L.append(f"**Generated:** {ts} · Scope: all issues across the `lentago` org · Activity window: last 7 days "
             f"(since {cutoff_iso[:10]}).")
    L.append("")
    L.append("| Open issues | Repos with open issues | PRs merged (7d) | Issues closed (7d) | Issues opened (7d) |")
    L.append("|---:|---:|---:|---:|---:|")
    L.append(f"| **{len(open_issues)}** | {len(by_repo)} | {len(merged_prs)} | {len(recent_closed)} | {len(recent_open)} |")
    L.append("")
    L.append("## Open issues by repo")
    L.append("")
    if not open_issues:
        L.append("_No open issues across the fleet._")
        L.append("")
    for repo in sorted(by_repo, key=lambda r:(-len(by_repo[r]), r)):
        items = sorted(by_repo[repo], key=lambda i:-i["number"])
        L.append(f"### {repo} — {len(items)} open")
        L.append("")
        L.append("| # | Title |")
        L.append("|---|-------|")
        for i in items:
            url = f"https://github.com/lentago/{repo}/issues/{i['number']}"
            title = i["title"].replace("|","\\|")
            L.append(f"| [{i['number']}]({url}) | {title} |")
        L.append("")
    L.append("## Activity — last 7 days")
    L.append("")
    L.append(f"**{len(merged_prs)} PRs merged**")
    L.append("")
    if merged_prs:
        for p in sorted(merged_prs, key=lambda p:p.get("closedAt",""), reverse=True):
            repo=p["repository"]["name"]; url=f"https://github.com/lentago/{repo}/pull/{p['number']}"
            title=p["title"].replace("|","\\|")
            L.append(f"- {p.get('closedAt','')[:10]} · [{repo}#{p['number']}]({url}) — {title}")
        L.append("")
    L.append(f"**{len(recent_closed)} issues closed**")
    L.append("")
    if recent_closed:
        for i in sorted(recent_closed, key=lambda i:i.get("closedAt",""), reverse=True):
            repo=i["repository"]["name"]; url=f"https://github.com/lentago/{repo}/issues/{i['number']}"
            title=i["title"].replace("|","\\|")
            L.append(f"- {i.get('closedAt','')[:10]} · [{repo}#{i['number']}]({url}) — {title}")
        L.append("")
    L.append("## Method")
    L.append("")
    L.append("- Open issues: `gh search issues --owner lentago --state open`. Activity: merged PRs via "
             "`gh search prs --owner lentago --merged`, closed issues filtered to the 7-day window.")
    L.append("- Only public GitHub metadata is surfaced; no transcript harvest, ops items, or homelab detail "
             "(those live in the LAN-only editorial copy).")
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
    args = ap.parse_args()

    now = datetime.now(timezone.utc)
    ts = now.strftime("%Y-%m-%d %H:%M UTC")
    cutoff = (now - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ")

    repos = get_repos()
    work_dir = args.work_dir or tempfile.mkdtemp(prefix="fleet-census-")
    clones = ensure_clones(repos, args.source_dir, work_dir)

    fleet, per_repo, instr_files, LBL = run_census(repos, clones)
    census_md = render_census(fleet, per_repo, instr_files, LBL, repos, ts)

    open_issues, recent_closed, merged_prs, recent_open = get_issue_data(cutoff)
    issue_md = render_issue_report(open_issues, recent_closed, merged_prs, recent_open, ts, cutoff)

    out = args.out_dir
    os.makedirs(os.path.join(out,"metrics"), exist_ok=True)
    os.makedirs(os.path.join(out,"fleet-reports"), exist_ok=True)
    with open(os.path.join(out,"metrics","code-census.md"),"w") as f: f.write(census_md)
    with open(os.path.join(out,"fleet-reports","fleet-issue-report.md"),"w") as f: f.write(issue_md)
    print(f"wrote metrics/code-census.md and fleet-reports/fleet-issue-report.md into {out}")
    code_total = sum(s["lines"] for s in fleet["code"].values())
    print(f"  census: {code_total:,} code lines · {len(open_issues)} open issues")

if __name__ == "__main__":
    main()
