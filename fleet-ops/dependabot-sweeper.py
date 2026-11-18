#!/usr/bin/env python3
"""Dependabot sweeper: merges Dependabot patch and minor PRs across the fleet.

ADR-0016 (docs/adr/0016-dependabot-patch-minor-routine.md) is the rule; this
file is its implementation. It runs from .github's `main` only, through
.github/workflows/dependabot-sweeper.yml, with the operator's fine-grained PAT
from the main-only `dependabot-merge` environment (GH_TOKEN). It never checks
out or runs a pull request's content: everything it judges comes from the API.

For each open Dependabot PR in every repo in fleet-ops/repos.json, the gate is:
  - author dependabot[bot]; head branch in the same repo; base is the default
    branch; not a draft; every commit authored by dependabot[bot] and verified;
  - every entry of the head commit's `updated-dependencies` block is a
    semver-patch or semver-minor update, and no minor is below 1.0.0;
  - the PR changes none of the sweeper's own files;
  - mergeStateStatus is CLEAN.
A PR that passes everything but is BEHIND gets `@dependabot rebase` (once per
head). A CLEAN one is merged with --match-head-commit, never --admin, after a
comment that names the run, and with a `Merged-by-routine` trailer. At most one
merge per repo per run, so in a strict repo the rest of the batch is rebased
first rather than merged stale.

Every run also audits the last 30 days: a commit on a repo's main that carries
the trailer must belong to a PR authored by dependabot[bot]. A mismatch, or a
repo the token cannot read, fails the run.

Usage: dependabot-sweeper.py --mode dry-run|merge [--run-url URL]
Requires: gh (authenticated through GH_TOKEN), Python 3 stdlib only.
"""
import argparse
import functools
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone

OWNER = "lentago"
DEPENDABOT = "dependabot[bot]"
TRAILER = "Merged-by-routine: dependabot-sweeper"
ALLOWED_TYPES = {"version-update:semver-patch", "version-update:semver-minor"}
# Files the sweeper runs. A PR that changes one of them stays manual (ADR-0016
# Decision 2): otherwise the sweeper could merge a change to its own code,
# unread, and run it with the token on the next run.
SELF_FILES = {
    ".github": {".github/workflows/dependabot-sweeper.yml", "fleet-ops/dependabot-sweeper.py"},
}
AUDIT_DAYS = 30
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ------------------------------------------------------------------ pure gate
# These take plain data and never call the API, so ci/validate.py can test them.

def parse_updated_dependencies(message):
    """The `updated-dependencies` entries of a Dependabot commit message, as a
    list of dicts, or None when the block is missing or doesn't parse.

    Dependabot writes it as a YAML front-matter block after the body:
        ---
        updated-dependencies:
        - dependency-name: x
          dependency-version: 1.2.3
          update-type: version-update:semver-patch
        ...
    Only that flat shape is read. Anything else returns None (fail closed)."""
    lines = message.splitlines()
    try:
        start = lines.index("updated-dependencies:")
    except ValueError:
        return None
    entries, cur = [], None
    for line in lines[start + 1:]:
        if line in ("...", "---"):
            break
        m = re.fullmatch(r"(- |  )([a-z-]+): ?(.*)", line)
        if not m:
            return None
        lead, key, value = m.groups()
        if lead == "- ":
            cur = {}
            entries.append(cur)
        elif cur is None:
            return None
        cur[key] = value.strip().strip("'\"")
    else:
        return None  # no terminator: truncated or not Dependabot's block
    if not entries or any("dependency-name" not in e for e in entries):
        return None
    return entries


def _major(version):
    m = re.match(r"v?(\d+)(\.|$)", version or "")
    return int(m.group(1)) if m else None


def update_problem(entries):
    """None when every update is in scope; otherwise the reason it isn't."""
    if entries is None:
        return "no readable updated-dependencies block"
    for e in entries:
        name, kind = e["dependency-name"], e.get("update-type")
        if kind not in ALLOWED_TYPES:
            return f"{name}: update-type {kind or 'missing'}"
        if kind.endswith("semver-minor"):
            major = _major(e.get("dependency-version"))
            if major is None:
                return f"{name}: minor update with no readable dependency-version"
            if major == 0:
                return f"{name}: minor update below 1.0.0 ({e['dependency-version']})"
    return None


def pr_problem(pr, commits, files, repo):
    """None when the PR's shape passes the gate (merge state aside)."""
    if pr["user"]["login"] != DEPENDABOT:
        return "not authored by Dependabot"
    if pr.get("draft"):
        return "draft"
    if (pr["head"]["repo"] or {}).get("full_name") != pr["base"]["repo"]["full_name"]:
        return "head branch is not in this repository"
    if pr["base"]["ref"] != pr["base"]["repo"]["default_branch"]:
        return f"base is {pr['base']['ref']}, not the default branch"
    if not commits:
        return "no commits"
    for c in commits:
        if (c.get("author") or {}).get("login") != DEPENDABOT:
            return f"commit {c['sha'][:7]} not authored by Dependabot"
        if not c["commit"]["verification"]["verified"]:
            return f"commit {c['sha'][:7]} not verified"
    if commits[-1]["sha"] != pr["head"]["sha"]:
        return "head moved while reading"
    touched = SELF_FILES.get(repo, set()) & {f["filename"] for f in files}
    touched |= SELF_FILES.get(repo, set()) & {f.get("previous_filename") for f in files}
    if touched:
        return f"changes the sweeper's own file {sorted(touched)[0]}"
    return update_problem(parse_updated_dependencies(commits[-1]["commit"]["message"]))


def has_trailer(message):
    """True when TRAILER is a line of the message's last paragraph, which is
    where git trailers live. A PR body that merely quotes the string in prose
    does not count."""
    paras = [p for p in re.split(r"\n[ \t]*\n", message.strip()) if p.strip()]
    return bool(paras) and TRAILER in (line.strip() for line in paras[-1].splitlines())


def audit_findings(repo, marked):
    """`marked` is [(commit, pulls)] for commits that carry the trailer. Returns
    one line per commit whose PR Dependabot did not author (or that has none)."""
    bad = []
    for c, pulls in marked:
        if not pulls or any(p["user"]["login"] != DEPENDABOT for p in pulls):
            who = ", ".join(f"#{p['number']} by {p['user']['login']}" for p in pulls) or "no PR"
            bad.append(f"{repo}@{c['sha'][:7]} ({who})")
    return bad


def commented_since(comments, login, since, match):
    """Has `login` posted a comment matching `match` at or after `since`?"""
    return any(c["user"]["login"] == login and c["created_at"] >= since and match(c["body"])
               for c in comments)


def merge_body(message, run_url):
    """The squash commit body: Dependabot's own message (minus its subject) with
    the routine's trailers added to its trailer block, or as a new one."""
    body = message.split("\n", 1)[1].strip() if "\n" in message else ""
    last = body.splitlines()[-1] if body else ""
    sep = "\n" if re.match(r"[A-Za-z][A-Za-z-]*: ", last) else "\n\n"
    return f"{body}{sep}{TRAILER}\nMerged-by-run: {run_url}\n".lstrip("\n")


def merge_comment(head, run_url):
    return (f"Merging under [ADR-0016](https://github.com/{OWNER}/.github/blob/main/docs/adr/"
            f"0016-dependabot-patch-minor-routine.md), the Dependabot patch and minor routine. "
            f"Evaluated head `{head}`. Run: {run_url}")


# ------------------------------------------------------------------ GitHub I/O

class ApiError(Exception):
    pass


def gh(*args, input_text=None):
    out = subprocess.run(["gh", *args], capture_output=True, text=True, input=input_text)
    if out.returncode != 0:
        raise ApiError(out.stderr.strip().splitlines()[-1] if out.stderr.strip() else f"gh exited {out.returncode}")
    return out.stdout


def api(path, paginate=False):
    args = ["api", "-H", "Accept: application/vnd.github+json", path]
    if paginate:
        args[1:1] = ["--paginate", "--slurp"]
        pages = json.loads(gh(*args))
        return [item for page in pages for item in page]
    return json.loads(gh(*args))


def merge_state(repo, number, tries=3, wait=5):
    """GitHub computes mergeStateStatus lazily: the first read of a PR nobody
    has looked at lately is often UNKNOWN. Ask again a few times before giving up
    on this run (the next run asks again)."""
    for attempt in range(tries):
        data = json.loads(gh("pr", "view", str(number), "-R", f"{OWNER}/{repo}",
                             "--json", "mergeStateStatus,headRefOid"))
        if data["mergeStateStatus"] != "UNKNOWN" or attempt == tries - 1:
            return data["mergeStateStatus"], data["headRefOid"]
        time.sleep(wait)


@functools.lru_cache(maxsize=None)
def token_login():
    return api("user")["login"]


def pr_comments(repo, number):
    return api(f"repos/{OWNER}/{repo}/issues/{number}/comments?per_page=100", paginate=True)


def audit(repo, since):
    """Trailer-marked merges on main whose PR Dependabot did not author."""
    commits = api(f"repos/{OWNER}/{repo}/commits?sha=main&since={since}&per_page=100", paginate=True)
    marked = [(c, api(f"repos/{OWNER}/{repo}/commits/{c['sha']}/pulls"))
              for c in commits if has_trailer(c["commit"]["message"])]
    return audit_findings(repo, marked)


# ------------------------------------------------------------------ the sweep

def sweep_repo(repo, mode, run_url, log):
    prs = [p for p in api(f"repos/{OWNER}/{repo}/pulls?state=open&per_page=100", paginate=True)
           if p["user"]["login"] == DEPENDABOT]
    merged = False
    for pr in sorted(prs, key=lambda p: p["number"]):
        n = pr["number"]
        commits = api(f"repos/{OWNER}/{repo}/pulls/{n}/commits?per_page=100", paginate=True)
        files = api(f"repos/{OWNER}/{repo}/pulls/{n}/files?per_page=100", paginate=True)
        problem = pr_problem(pr, commits, files, repo)
        if problem:
            log(repo, n, "skip", problem)
            continue
        head = pr["head"]["sha"]
        state, live_head = merge_state(repo, n)
        if live_head != head:
            log(repo, n, "skip", "head moved while evaluating")
            continue
        head_date = commits[-1]["commit"]["committer"]["date"]
        if state == "BEHIND":
            if commented_since(pr_comments(repo, n), token_login(), head_date,
                               lambda b: b.strip() == "@dependabot rebase"):
                log(repo, n, "wait", "behind main; rebase already requested")
            elif mode == "merge":
                gh("pr", "comment", str(n), "-R", f"{OWNER}/{repo}", "--body", "@dependabot rebase")
                log(repo, n, "rebase", "behind main; asked Dependabot to rebase")
            else:
                log(repo, n, "rebase", "behind main; would ask Dependabot to rebase")
            continue
        if state != "CLEAN":
            log(repo, n, "skip", f"mergeStateStatus {state}")
            continue
        if merged:
            log(repo, n, "wait", "eligible; one merge per repo per run")
            continue
        if mode != "merge":
            log(repo, n, "merge", f"eligible at {head[:7]}; dry run, not merged")
            merged = True
            continue
        # Once per head: a merge GitHub refuses is retried next run without
        # posting the comment again.
        if not commented_since(pr_comments(repo, n), token_login(), head_date,
                               lambda b: f"Evaluated head `{head}`" in b):
            gh("pr", "comment", str(n), "-R", f"{OWNER}/{repo}", "--body", merge_comment(head, run_url))
        body = merge_body(commits[-1]["commit"]["message"], run_url)
        try:
            gh("pr", "merge", str(n), "-R", f"{OWNER}/{repo}", "--squash",
               "--match-head-commit", head, "--body", body)
        except ApiError as exc:
            log(repo, n, "failed", f"merge refused: {exc}")
            continue
        log(repo, n, "merge", f"merged at {head[:7]}")
        merged = True


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument("--mode", choices=["dry-run", "merge"], default="dry-run")
    ap.add_argument("--run-url", default="(local run)")
    args = ap.parse_args()

    with open(os.path.join(ROOT, "fleet-ops", "repos.json")) as fh:
        repos = sorted(json.load(fh)["repos"])

    rows, errors = [], []

    def log(repo, n, action, reason):
        rows.append((repo, n, action, reason))
        print(f"{repo}#{n}: {action}: {reason}")

    since = (datetime.now(timezone.utc) - timedelta(days=AUDIT_DAYS)).strftime("%Y-%m-%dT%H:%M:%SZ")
    for repo in repos:
        try:
            sweep_repo(repo, args.mode, args.run_url, log)
            for bad in audit(repo, since):
                errors.append(f"audit: trailer-marked merge not authored by Dependabot: {bad}")
        except ApiError as exc:
            errors.append(f"{repo}: {exc}")
        except Exception as exc:                              # noqa: BLE001
            # An API shape this script doesn't expect is a failure for this repo,
            # not a reason to skip the other repos, the audit and the summary.
            errors.append(f"{repo}: unexpected {type(exc).__name__}: {exc}")

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as fh:
            fh.write(f"## Dependabot sweep ({args.mode})\n\n")
            if rows:
                fh.write("| PR | Action | Reason |\n|---|---|---|\n")
                for repo, n, action, reason in rows:
                    fh.write(f"| [{repo}#{n}](https://github.com/{OWNER}/{repo}/pull/{n}) | {action} | {reason} |\n")
            else:
                fh.write("No open Dependabot PRs.\n")
            for e in errors:
                fh.write(f"\n**Error:** {e}\n")
    for e in errors:
        print(f"::error::{e}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
