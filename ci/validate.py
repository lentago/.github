#!/usr/bin/env python3
"""Repo validator for lentago/.github — the check that gates PRs here.

This repo carries no application code, so "does it build" is meaningless. What it
*does* carry is operator tooling the rest of the fleet depends on, plus the public
org landing page. Those have real failure modes, and this asserts against them:

  configs   fleet-ops/*.json parse and hold the shape fleet-apply.sh and the
            terraform module expect. A malformed required-checks.json breaks a
            fleet-wide settings sweep partway through, leaving the fleet
            half-applied; a malformed repos.json is a repository.
  fleet     the three fleet-ops manifests and brand/fleet.json agree on which
            repos exist. Each is edited separately, and a repo present in one
            but missing from another fails quietly somewhere else later.
  brand     brand/generated/ is reproducible from brand/fleet.json — the banners
            get copied verbatim into 15 repos, so a hand-edit forks the identity.
  census    metrics/generate-fleet-reports.py imports, and its data/code classifier
            still routes known paths correctly (regression cover for #59, where a
            JSON-only carve-out counted 15,595 lines of CSV exports as source).
  register  fleet-reports/incidents.md is reproducible from fleet-reports/incidents/.
            It is generated, not hand-authored; a hand-edit here is a change that the
            next weekly refresh silently reverts.

Relative markdown links are NOT checked here. That check lived in this file as
`check_relative_links` until #66; it was promoted into the shared reusable
lentago/shared-workflows/.github/workflows/docs-check.yml (shared-workflows#28) and
this repo now calls it like the rest of the fleet, via .github/workflows/docs-check.yml.
Keeping a second copy here would have meant two implementations of one check drifting
apart, with this repo gated by the staler one. What remains above is the set that is
genuinely specific to this repo and does not generalise.

Run it locally exactly as CI does:  python3 ci/validate.py
Exit status is 0 only when every check passes; failures are listed, not raised, so
one run reports everything wrong rather than the first thing wrong.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAILURES = []
CHECKS_RUN = []


def fail(check, msg):
    FAILURES.append(f"{check}: {msg}")


def tracked(*patterns):
    """git-tracked files matching pathspecs — untracked scratch never enters CI."""
    out = subprocess.run(["git", "-C", ROOT, "ls-files", *patterns],
                         capture_output=True, text=True, check=True)
    return [p for p in out.stdout.splitlines() if p.strip()]


# ------------------------------------------------------------------ configs
def check_fleet_ops_configs():
    """fleet-ops JSON must parse and match what fleet-apply.sh consumes."""
    for rel in tracked("fleet-ops/*.json"):
        path = os.path.join(ROOT, rel)
        try:
            with open(path, encoding="utf-8") as fh:
                doc = json.load(fh)
        except json.JSONDecodeError as exc:
            fail("configs", f"{rel} is not valid JSON — {exc}")
            continue

        base = os.path.basename(rel)

        if base == "labels.json":
            check_label_palette(rel, doc)
            continue

        if base == "repos.json":
            check_repos_manifest(rel, doc)
            continue

        if base != "required-checks.json":
            continue

        checks = doc.get("checks")
        if not isinstance(checks, dict):
            fail("configs", f"{rel} has no top-level 'checks' object")
            continue
        if not checks:
            fail("configs", f"{rel} maps no repos — fleet-apply --require-checks "
                            "would silently enforce nothing")
        for repo, contexts in sorted(checks.items()):
            if not isinstance(contexts, list) or not contexts:
                fail("configs", f"{rel}: '{repo}' must map to a non-empty array")
                continue
            for ctx in contexts:
                if not isinstance(ctx, str) or not ctx.strip():
                    fail("configs", f"{rel}: '{repo}' has a non-string/empty context")
            if len(set(contexts)) != len(contexts):
                fail("configs", f"{rel}: '{repo}' lists a duplicate context")


HEX6 = re.compile(r"^[0-9a-fA-F]{6}$")


def check_label_palette(rel, doc):
    """labels.json drives `gh label edit` across every repo in one sweep.

    A bad hex or a missing key fails partway through, leaving the fleet
    half-recolored — cheaper to catch here than to unpick afterwards.
    """
    labels = doc.get("labels")
    if not isinstance(labels, list) or not labels:
        fail("configs", f"{rel} has no non-empty top-level 'labels' array")
        return

    seen = set()
    for i, label in enumerate(labels):
        where = f"{rel}[{i}]"
        if not isinstance(label, dict):
            fail("configs", f"{where} is not an object")
            continue

        name = label.get("name")
        if not isinstance(name, str) or not name.strip():
            fail("configs", f"{where} has no usable 'name'")
        elif name in seen:
            fail("configs", f"{where}: duplicate label '{name}' — the second edit wins silently")
        else:
            seen.add(name)

        color = label.get("color")
        if not isinstance(color, str) or not HEX6.match(color):
            fail("configs", f"{where} ('{name}'): color must be 6 hex digits without '#', got {color!r}")

        if not isinstance(label.get("description"), str):
            fail("configs", f"{where} ('{name}') has no string 'description'")

        if not isinstance(label.get("ensure"), bool):
            fail("configs", f"{where} ('{name}') needs an explicit boolean 'ensure'")


SPINE_TOPICS = {"lentago", "claude"}
VISIBILITIES = {"public", "private"}
REPO_KEYS = {"description", "homepage", "visibility", "template", "template_source",
             "features", "suggest_branch_update", "topics", "model_labels"}
FEATURE_KEYS = {"issues", "projects", "wiki", "discussions"}


def check_repos_manifest(rel, doc):
    """repos.json is the input to `github_repository` — a typo here is a repo.

    Terraform will happily act on a malformed-but-parseable manifest: a repo
    silently renamed by an edited key plans as a create (the old one is held by
    prevent_destroy), and a mistyped visibility flips a repo public. Shape is
    asserted here rather than discovered in a plan.
    """
    repos = doc.get("repos")
    if not isinstance(repos, dict) or not repos:
        fail("configs", f"{rel} has no non-empty top-level 'repos' object")
        return

    for name, repo in sorted(repos.items()):
        where = f"{rel}['{name}']"
        if not isinstance(repo, dict):
            fail("configs", f"{where} is not an object")
            continue

        extra = set(repo) - REPO_KEYS
        missing = REPO_KEYS - set(repo)
        if extra:
            fail("configs", f"{where} has unknown key(s): {sorted(extra)}")
        if missing:
            fail("configs", f"{where} is missing key(s): {sorted(missing)}")
            continue

        if not isinstance(repo["description"], str) or not repo["description"].strip():
            fail("configs", f"{where} needs a non-empty 'description'")
        if repo["homepage"] is not None and not isinstance(repo["homepage"], str):
            fail("configs", f"{where}: 'homepage' must be a string or null")
        if repo["visibility"] not in VISIBILITIES:
            fail("configs", f"{where}: 'visibility' must be one of {sorted(VISIBILITIES)}, "
                            f"got {repo['visibility']!r}")
        for key in ("template", "suggest_branch_update"):
            if not isinstance(repo[key], bool):
                fail("configs", f"{where}: '{key}' must be a boolean")

        src = repo["template_source"]
        if src is not None:
            if not isinstance(src, dict) or set(src) != {"owner", "repository"} \
                    or not all(isinstance(v, str) and v.strip() for v in src.values()):
                fail("configs", f"{where}: 'template_source' must be null or "
                                "{owner, repository} of non-empty strings")

        features = repo["features"]
        if not isinstance(features, dict) or set(features) != FEATURE_KEYS \
                or not all(isinstance(v, bool) for v in features.values()):
            fail("configs", f"{where}: 'features' must be exactly "
                            f"{sorted(FEATURE_KEYS)} of booleans")

        topics = repo["topics"]
        if not isinstance(topics, list) or not all(isinstance(t, str) and t.strip() for t in topics):
            fail("configs", f"{where}: 'topics' must be an array of non-empty strings")
        else:
            if len(set(topics)) != len(topics):
                fail("configs", f"{where}: 'topics' lists a duplicate")
            # The spine is added by terraform/locals.tf. Listing it here reads as
            # if a repo could opt out of it, which it cannot.
            if SPINE_TOPICS & set(topics):
                fail("configs", f"{where}: 'topics' must not repeat the "
                                f"{sorted(SPINE_TOPICS)} spine — terraform adds it")

        if not isinstance(repo["model_labels"], list):
            fail("configs", f"{where}: 'model_labels' must be an array")


# ------------------------------------------------------------------- fleet
def check_fleet_coverage():
    """The three fleet-ops manifests plus brand/fleet.json must agree on membership.

    Each is edited on its own, and a repo present in one but absent from another
    fails quietly in a different place every time: no required checks means
    `gh pr merge --auto` cannot arm (lentago/.github#27), a stale required-checks
    key means terraform renders a ruleset for a repo that no longer exists, and a
    missing brand entry means a repo with no banner. Cheaper to assert once.
    """
    def load(path, key):
        try:
            with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
                return json.load(fh).get(key) or {}
        except (OSError, json.JSONDecodeError):
            fail("fleet", f"{path} is unreadable — cannot cross-check fleet membership")
            return None

    repos = load("fleet-ops/repos.json", "repos")
    checks = load("fleet-ops/required-checks.json", "checks")
    labels = load("fleet-ops/labels.json", "labels")
    if repos is None or checks is None or labels is None:
        return

    try:
        with open(os.path.join(ROOT, "brand/fleet.json"), encoding="utf-8") as fh:
            brand = {k for k in json.load(fh) if not k.startswith("_")}
    except (OSError, json.JSONDecodeError):
        fail("fleet", "brand/fleet.json is unreadable — cannot cross-check fleet membership")
        return

    public = {n for n, r in repos.items() if isinstance(r, dict) and r.get("visibility") == "public"}
    private = set(repos) - public

    for name in sorted(public - set(checks)):
        fail("fleet", f"'{name}' is public in repos.json but has no required-checks.json "
                      "entry — its ruleset would require nothing and auto-merge could not arm")
    for name in sorted(set(checks) - set(repos)):
        fail("fleet", f"required-checks.json maps '{name}', which is not in repos.json")
    for name in sorted(private & set(checks)):
        fail("fleet", f"'{name}' is private, so it gets no ruleset (rulesets need GitHub Pro), "
                      "but required-checks.json maps it — the contexts would never be applied")
    for name in sorted(brand - set(repos)):
        fail("fleet", f"brand/fleet.json carries '{name}', which is not in repos.json")
    for name in sorted(public - brand):
        fail("fleet", f"'{name}' is public in repos.json but has no brand/fleet.json entry "
                      "— it would ship without a README banner")

    # model_labels names a model:* label that labels.json must actually define.
    tiers = {lb["name"].split(":", 1)[1] for lb in labels
             if isinstance(lb, dict) and isinstance(lb.get("name"), str)
             and lb["name"].startswith("model:")}
    for name, repo in sorted(repos.items()):
        if not isinstance(repo, dict):
            continue
        for tier in repo.get("model_labels") or []:
            if tier not in tiers:
                fail("fleet", f"repos.json['{name}'] routes model tier '{tier}', but "
                              f"labels.json defines no 'model:{tier}' label")


# ------------------------------------------------------------------- brand
def check_brand_assets():
    """brand/generated/ must be reproducible from brand/fleet.json.

    The banners carry a 'generated — do not hand-edit' header and get copied
    verbatim into 15 repos, so a hand-tweak here silently forks the fleet's
    identity from its source. Regenerate into a temp tree and diff. og.png is
    skipped: rasterizing needs Chrome, which CI has no reason to carry.
    """
    brand = os.path.join(ROOT, "brand")
    fleet_path = os.path.join(brand, "fleet.json")
    if not os.path.exists(fleet_path):
        fail("brand", "brand/fleet.json is missing")
        return

    try:
        with open(fleet_path, encoding="utf-8") as fh:
            fleet = {k: v for k, v in json.load(fh).items() if not k.startswith("_")}
    except json.JSONDecodeError as exc:
        fail("brand", f"brand/fleet.json is not valid JSON — {exc}")
        return

    if not fleet:
        fail("brand", "brand/fleet.json describes no repos")
        return

    before = len(FAILURES)
    for repo, cfg in sorted(fleet.items()):
        for key in ("mark", "kind", "tagline", "prompt", "badges"):
            if key not in cfg:
                fail("brand", f"brand/fleet.json: '{repo}' is missing '{key}'")
        mark = cfg.get("mark")
        if mark and not os.path.exists(os.path.join(brand, "marks", f"{mark}-mark-square.svg")):
            fail("brand", f"brand/fleet.json: '{repo}' points at unknown mark '{mark}'")

    # generate.py exits the process on a bad mark and raises on a missing key,
    # either of which would kill this run before the failures above are printed.
    # Report the config problems instead of regenerating on top of them.
    if len(FAILURES) > before:
        return

    sys.path.insert(0, brand)
    try:
        import generate  # noqa: PLC0415 — deliberately late, brand/ isn't a package
    except Exception as exc:  # pragma: no cover - import shape varies by breakage
        fail("brand", f"brand/generate.py does not import — {exc}")
        return
    finally:
        sys.path.pop(0)

    stale = []
    for repo, cfg in sorted(fleet.items()):
        for filename, produce in (("banner.svg", generate.banner),
                                  ("readme.md", generate.readme_block)):
            path = os.path.join(brand, "generated", repo, filename)
            if not os.path.exists(path):
                stale.append(f"{repo}/{filename} (missing)")
                continue
            with open(path, encoding="utf-8") as fh:
                if fh.read() != produce(repo, cfg):
                    stale.append(f"{repo}/{filename}")

    if stale:
        fail("brand", "brand/generated is stale or hand-edited: "
                      + ", ".join(stale) + " — run `python3 brand/generate.py`")


# ------------------------------------------------------------------ census
# Each case is (repo, path, expected_is_data). The negatives matter more than the
# positives: they pin the carve-outs that must NOT widen — drosera's dashboards are
# Terraform-enforced dashboards-as-code, and homeassistant-config's root
# automations.yaml is real config, not the context/ snapshot dir.
CLASSIFIER_CASES = [
    ("music-curator", "data/music-collection-tunemymusic.csv", True),
    ("music-curator", "data/music-collection-spotify-misses.csv", True),
    ("music-curator", "data/harvests/follow-events.jsonl", True),
    ("music-curator", "./data/inventory.json", True),
    ("music-curator", "data/harvests/README.md", False),
    ("music-curator", "scripts/harvest_merge.py", False),
    ("music-curator", "vault/notes/foo.csv", False),
    ("homeassistant-config", "context/entities.json", True),
    ("homeassistant-config", "context/automations-ui.yaml", True),
    ("homeassistant-config", "automations.yaml", False),
    ("drosera", "dashboards/fleet.json", False),
    ("reference-checker", "reports/run.html", True),
    ("solidago", "terraform/main.tf", False),
]

# is_generated() is path- and repo-aware, not basename-only: brand/generated/ holds
# committed machine output that CI asserts is reproducible from brand/fleet.json, so
# counting it as authored source would inflate the census. Negatives guard the blast
# radius — the rule must not swallow the generator itself or same-format source elsewhere.
GENERATED_CASES = [
    (".github", "brand/generated/betula/og.html", True),
    (".github", "./brand/generated/.github/og.html", True),
    (".github", "brand/generate.py", False),
    (".github", "brand/fleet.json", False),
    ("site-lentago-dev", "public/index.html", False),
    ("drosera", "package-lock.json", True),
    ("brasenia", "docs/diagram.svg", True),
]

MD_CASES = [
    ("kalmia", "CLAUDE.md", "instructions"),
    ("drosera", "docs/adr/0001-metrics-only.md", "documentation"),
    ("music-curator", "vault/artists/foo.md", "content"),
    ("kalmia", "CONTRIBUTING.md", "community"),
    (".github", "fleet-reports/fleet-report.md", "content"),
]


def load_generator():
    path = os.path.join(ROOT, "metrics", "generate-fleet-reports.py")
    spec = importlib.util.spec_from_file_location("fleet_report_gen", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def check_census_classifier():
    try:
        gen = load_generator()
    except Exception as exc:                                  # noqa: BLE001
        fail("census", f"metrics/generate-fleet-reports.py failed to import — {exc}")
        return

    for repo, path, want in CLASSIFIER_CASES:
        got = gen.is_data(repo, path)
        if got != want:
            fail("census", f"is_data({repo!r}, {path!r}) returned {got}, expected {want}")

    for repo, path, want in GENERATED_CASES:
        got = gen.is_generated(repo, path)
        if got != want:
            fail("census", f"is_generated({repo!r}, {path!r}) returned {got}, expected {want}")

    for repo, path, want in MD_CASES:
        got = gen.classify_md(repo, path)
        if got != want:
            fail("census", f"classify_md({repo!r}, {path!r}) returned {got!r}, expected {want!r}")


# ------------------------------------------------------------------ register
GENERATED_LINE = re.compile(r"^\*\*Generated:\*\*")


def _strip_timestamp(text):
    return [ln for ln in text.splitlines() if not GENERATED_LINE.match(ln)]


def check_incident_register_reproducible():
    committed_path = os.path.join(ROOT, "fleet-reports", "incidents.md")
    if not os.path.exists(committed_path):
        fail("register", "fleet-reports/incidents.md is missing")
        return

    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(os.path.join(tmp, "fleet-reports"), exist_ok=True)
        # The generator reads the incident sources from --out-dir, so mirror them in.
        src = os.path.join(ROOT, "fleet-reports", "incidents")
        dst = os.path.join(tmp, "fleet-reports", "incidents")
        if os.path.isdir(src):
            os.symlink(src, dst)

        proc = subprocess.run(
            [sys.executable, os.path.join(ROOT, "metrics", "generate-fleet-reports.py"),
             "--out-dir", tmp, "--incidents-only"],
            capture_output=True, text=True)
        if proc.returncode != 0:
            fail("register", "generator --incidents-only failed — "
                             f"{proc.stderr.strip() or proc.stdout.strip()}")
            return

        regenerated_path = os.path.join(tmp, "fleet-reports", "incidents.md")
        if not os.path.exists(regenerated_path):
            fail("register", "generator --incidents-only wrote no incidents.md")
            return

        with open(committed_path, encoding="utf-8") as fh:
            committed = _strip_timestamp(fh.read())
        with open(regenerated_path, encoding="utf-8") as fh:
            regenerated = _strip_timestamp(fh.read())

    if committed != regenerated:
        fail("register",
             "fleet-reports/incidents.md does not match a regeneration from "
             "fleet-reports/incidents/ — it is generated, not hand-authored. "
             "Run: python3 metrics/generate-fleet-reports.py --out-dir . --incidents-only")


# ------------------------------------------------------------------ main
CHECKS = [
    ("configs", check_fleet_ops_configs),
    ("fleet", check_fleet_coverage),
    ("brand", check_brand_assets),
    ("census", check_census_classifier),
    ("register", check_incident_register_reproducible),
]


def main():
    for name, fn in CHECKS:
        before = len(FAILURES)
        fn()
        CHECKS_RUN.append((name, len(FAILURES) - before))

    width = max(len(n) for n, _ in CHECKS_RUN)
    for name, n in CHECKS_RUN:
        print(f"  {name.ljust(width)}  {'FAIL' if n else 'ok'}"
              f"{f' ({n})' if n else ''}")

    if FAILURES:
        print(f"\n{len(FAILURES)} failure(s):\n", file=sys.stderr)
        for f in FAILURES:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("\nall checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
