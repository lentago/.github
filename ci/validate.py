#!/usr/bin/env python3
"""Repo validator for lentago/.github — the check that gates PRs here.

This repo carries no application code, so "does it build" is meaningless. What it
*does* carry is operator tooling the rest of the fleet depends on, plus the public
org landing page. Those have real failure modes, and this asserts against them:

  configs   fleet-ops/*.json parse and hold the shape the terraform module and
            fleet-apply.sh's read-only check expect. A malformed
            required-checks.json fails the terraform plan for every repo at
            once; a malformed repos.json is a repository.
  fleet     the three fleet-ops manifests and brand/fleet.json agree on which
            repos exist. Each is edited separately, and a repo present in one
            but missing from another fails quietly somewhere else later.
  brand     brand/generated/ is reproducible from brand/fleet.json — the banners
            get copied verbatim into 15 repos, so a hand-edit forks the identity.
  census    metrics/generate-fleet-reports.py imports, and its data/code classifier
            still routes known paths correctly (regression cover for #59, where a
            JSON-only carve-out counted 15,595 lines of CSV exports as source).
  budget    the site error-budget section counts burn stretches correctly, sends
            the PromQL pinned below (a copy of drosera's SLO board and burn rules:
            CI does not read drosera, so this catches a change to the generator,
            not a change upstream), and degrades to one "Unavailable" line, never
            an exception, on a missing token, a failed query or a response in any
            shape it doesn't read.
  sweeper   fleet-ops/dependabot-sweeper.py's gate (ADR-0016) still decides known
            cases right: it reads Dependabot's updated-dependencies block, refuses
            majors, 0.x minors, missing or unreadable metadata, foreign authors,
            unverified commits, other-repo heads and the sweeper's own files, and
            passes a green patch/minor group. A wrong "pass" here is a merge. Its
            audit matches the trailer only where the sweeper writes it, never a
            quoted copy, and flags a marked merge that Dependabot didn't author.
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
from datetime import datetime, timezone

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
    """fleet-ops JSON must parse and match what terraform/ and fleet-apply.sh consume."""
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
            fail("configs", f"{rel} maps no repos — terraform/ "
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

        # `sources`: context -> the GitHub App integration ID it must come from
        # (terraform/rulesets.tf, fleet-apply.sh). A source for a context no repo
        # requires is a typo or a leftover, and would silently do nothing.
        sources = doc.get("sources", {})
        if not isinstance(sources, dict):
            fail("configs", f"{rel}: 'sources' must be an object")
            continue
        required = {c for cs in checks.values() if isinstance(cs, list) for c in cs}
        for ctx, app_id in sorted(sources.items()):
            if not isinstance(app_id, int) or isinstance(app_id, bool) or app_id <= 0:
                fail("configs", f"{rel}: source for '{ctx}' must be a positive integer "
                                "integration ID")
            if ctx not in required:
                fail("configs", f"{rel}: 'sources' names '{ctx}', which no repo requires")


HEX6 = re.compile(r"^[0-9a-fA-F]{6}$")
LABEL_KEYS = {"name", "color", "description", "repos"}


def check_label_palette(rel, doc):
    """labels.json drives terraform/labels.tf across every repo in one apply.

    The GitHub API rejects a bad hex partway through the apply, leaving the fleet
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

        # An unknown key is most likely a misspelt 'repos', and terraform reads a
        # label without 'repos' as fleet-wide: a typo would put a scoped override
        # label on every repo in one apply.
        for key in sorted(set(label) - LABEL_KEYS):
            fail("configs", f"{where} ('{name}'): unknown key '{key}' — "
                            f"allowed: {', '.join(sorted(LABEL_KEYS))}")

        if "repos" in label:
            scope = label["repos"]
            if (not isinstance(scope, list) or not scope
                    or not all(isinstance(r, str) and r for r in scope)):
                fail("configs", f"{where} ('{name}'): 'repos' must be a non-empty array of "
                                "repo names — omit it for a fleet-wide label")
            elif len(set(scope)) != len(scope):
                fail("configs", f"{where} ('{name}'): 'repos' lists a repo twice")


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

    # A scoped label's 'repos' must name repos that exist: terraform would
    # otherwise drop the stray name without a word and the label would be
    # missing exactly where its guard expects it.
    for lb in labels:
        if not isinstance(lb, dict) or not isinstance(lb.get("repos"), list):
            continue
        for name in sorted({r for r in lb["repos"] if isinstance(r, str)} - set(repos)):
            fail("fleet", f"labels.json scopes '{lb.get('name')}' to '{name}', "
                          "which is not in repos.json")


# ------------------------------------------------------------------- brand
def check_brand_assets():
    """brand/generated/ must be reproducible from brand/fleet.json.

    The banners carry a 'generated — do not hand-edit' header and get copied
    verbatim into 15 repos, so a hand-tweak here silently forks the fleet's
    identity from its source. Regenerate into a temp tree and diff. og.png and
    the Roku poster PNGs are skipped: rasterizing needs Chrome, which CI has no
    reason to carry. The poster's source page is checked, since its PNGs are
    copied verbatim into the channel repo the same way the banners are.
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

    stale, orphaned = [], []
    for repo, cfg in sorted(fleet.items()):
        outputs = [("banner.svg", generate.banner),
                   ("readme.md", generate.readme_block)]
        if cfg.get("roku"):
            outputs.append(("roku-poster.html", generate.roku_poster_html))
        else:
            # generate.py never deletes, so a poster left after the key is
            # dropped would still read as current output.
            for leftover in ("roku-poster.html", "roku-poster-fhd.png", "roku-poster-hd.png"):
                if os.path.exists(os.path.join(brand, "generated", repo, leftover)):
                    orphaned.append(f"{repo}/{leftover}")
        for filename, produce in outputs:
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
    if orphaned:
        fail("brand", "brand/generated has Roku posters for repos without \"roku\": true: "
                      + ", ".join(orphaned) + " — delete them")


# ------------------------------------------------------------------ census
# Each case is (repo, path, expected_is_data). The negatives matter more than the
# positives: they pin the carve-outs that must NOT widen — drosera's dashboards are
# Terraform-enforced dashboards-as-code, and homeassistant-config's root
# automations.yaml is real config, not the context/ snapshot dir.
CLASSIFIER_CASES = [
    ("homeassistant-config", "./context/devices.json", True),
    ("homeassistant-config", "context/README.md", False),
    ("homeassistant-config", "scripts/foo.py", False),
    ("homeassistant-config", "packages/foo.csv", False),
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
    ("site-icecreamtofightwith-com", "recipes/foo.md", "content"),
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


# ------------------------------------------------------------------ budget
# A copy of lentago/drosera dashboards/sites-slo-error-budget.json (stat panels) and
# terraform/alerts.tf (burn rules), for lentago.dev. CI does not read drosera, so this
# pins the generator to the copy and cannot see drosera drift. If drosera changes them,
# update the generator and these together — the report must show the board's numbers.
BUDGET_EXPRS = {
    "attainment": 'avg_over_time(probe_success{job="integrations/blackbox/lentago.dev"}[30d])',
    "remaining": '1 - (1 - avg_over_time(probe_success{job="integrations/blackbox/lentago.dev"}[30d])) / 0.001',
    "minutes": '(0.001 - (1 - avg_over_time(probe_success{job="integrations/blackbox/lentago.dev"}[30d]))) * 43200',
}
BURN_1H = '(1 - avg_over_time(probe_success{job="integrations/blackbox/lentago.dev"}[1h])) / 0.001'

# (long points, short points, threshold, step, expected (episodes, last ts)).
# The second case is the one that matters: the long window alone is hot for a
# stretch, but only steps where the short window agrees count, and a gap splits
# them into two episodes.
BURN_CASES = [
    ([(0, 0.0), (300, 0.0)], [(0, 0.0), (300, 0.0)], 14.4, 300, (0, None)),
    ([(0, 20), (300, 20), (600, 20), (900, 20), (1200, 20)],
     [(0, 20), (300, 1), (600, 20), (900, 20), (1200, 1)], 14.4, 300, (2, 900)),
    ([(0, 14.4)], [(0, 99)], 14.4, 300, (0, None)),       # gt, not ge — as the rules
]


def check_error_budget_section():
    try:
        gen = load_generator()
    except Exception as exc:                                  # noqa: BLE001
        fail("budget", f"metrics/generate-fleet-reports.py failed to import — {exc}")
        return

    if gen.slo_exprs("lentago.dev") != BUDGET_EXPRS:
        fail("budget", "slo_exprs() no longer matches the pinned copy of drosera's SLO-board PromQL")
    if gen.burn_expr("lentago.dev", "1h") != BURN_1H:
        fail("budget", "burn_expr() no longer matches the pinned copy of drosera's burn-rule PromQL")

    for long_pts, short_pts, thr, step, want in BURN_CASES:
        got = gen.burn_episodes(long_pts, short_pts, thr, step)
        if got != want:
            fail("budget", f"burn_episodes(…, {thr}, {step}) returned {got}, expected {want}")

    check_error_budget_degrades(gen)


# Fake Grafana responses for the degrade cases. Each entry is (label, token, responder);
# the responder takes (endpoint, call number) and returns a JSON-able body, raw bytes,
# or an exception instance to raise from urlopen. Every case must come back as
# (None, reason) and render one "Unavailable" line: a missing secret, a failed query or
# an unexpected shape must never fail the weekly run.
def _ok_instant(endpoint, n):
    if endpoint == "query":
        return {"status": "success", "data": {"result": [{"metric": {}, "value": [0, "0.9995"]}]}}
    return {"status": "success", "data": {"result": [{"metric": {}, "values": [[0, "0"], [300, "0"]]}]}}


def _http_error(code):
    import urllib.error
    return urllib.error.HTTPError("https://example.invalid", code, "error", {}, None)


def _url_error():
    import urllib.error
    return urllib.error.URLError("unreachable")


def _instant(result):
    return lambda endpoint, n: ({"status": "success", "data": {"result": result}}
                                if endpoint == "query" else _ok_instant(endpoint, n))


def _range(values):
    return lambda endpoint, n: (_ok_instant(endpoint, n) if endpoint == "query" else
                                {"status": "success", "data": {"result": [{"metric": {}, "values": values}]}})


def _incomplete(endpoint, n):
    # attainment answers, remaining and minutes come back empty for the first site
    if endpoint == "query" and n in (1, 2):
        return {"status": "success", "data": {"result": []}}
    return _ok_instant(endpoint, n)


DEGRADE_CASES = [
    ("token unset", None, None),
    ("token empty (secret unset in Actions)", "", None),
    ("token whitespace", "  \n", None),
    ("HTTP 401", "t", lambda e, n: _http_error(401)),
    ("host unreachable", "t", lambda e, n: _url_error()),
    ("body not JSON", "t", lambda e, n: b"<html>gateway</html>"),
    ("status error", "t", lambda e, n: {"status": "error", "errorType": "bad_data"}),
    ("body a JSON list", "t", lambda e, n: []),
    ("no data field", "t", lambda e, n: {"status": "success"}),
    ("result not a list", "t", lambda e, n: {"status": "success", "data": {"result": "x"}}),
    ("result null", "t", lambda e, n: {"status": "success", "data": {"result": None}}),
    ("sample without value", "t", _instant([{"metric": {}}])),
    ("sample value not numeric", "t", _instant([{"metric": {}, "value": [0, "abc"]}])),
    ("sample value NaN", "t", _instant([{"metric": {}, "value": [0, "NaN"]}])),
    ("sample value +Inf", "t", _instant([{"metric": {}, "value": [0, "+Inf"]}])),
    ("stat results incomplete", "t", _incomplete),
    ("range series without values", "t", lambda e, n: (_ok_instant(e, n) if e == "query" else
                                                       {"status": "success", "data": {"result": [{"metric": {}}]}})),
    ("range point malformed", "t", _range([[0]])),
    ("range timestamp out of range", "t", _range([["1e20", "99"]])),
]


def _run_budgets(gen, token, responder):
    import io
    import urllib.request
    calls = {"n": 0}

    def fake_urlopen(req, timeout=None):
        endpoint = req.full_url.split("/api/v1/", 1)[1].split("?", 1)[0]
        out = responder(endpoint, calls["n"])
        calls["n"] += 1
        if isinstance(out, BaseException):
            raise out
        return io.BytesIO(out if isinstance(out, bytes) else json.dumps(out).encode())

    saved_env = os.environ.pop(gen.GRAFANA_TOKEN_ENV, None)
    saved_urlopen = urllib.request.urlopen
    if token is not None:
        os.environ[gen.GRAFANA_TOKEN_ENV] = token
    urllib.request.urlopen = fake_urlopen if responder else saved_urlopen
    try:
        return gen.collect_error_budgets(datetime.now(timezone.utc))
    finally:
        urllib.request.urlopen = saved_urlopen
        os.environ.pop(gen.GRAFANA_TOKEN_ENV, None)
        if saved_env is not None:
            os.environ[gen.GRAFANA_TOKEN_ENV] = saved_env


def check_error_budget_degrades(gen):
    # The fake must be able to produce a table, or every degrade below proves nothing.
    try:
        rows, reason = _run_budgets(gen, "t", _ok_instant)
    except Exception as exc:                                  # noqa: BLE001
        fail("budget", f"well-formed fake responses raised {type(exc).__name__}: {exc}")
        return
    if rows is None or len(rows) != len(gen.SLO_SITES):
        fail("budget", f"well-formed fake responses did not produce a table: {(rows, reason)!r}")
        return
    if not any(ln.startswith("| lentago.dev |") for ln in gen.error_budget_section(rows, reason)):
        fail("budget", "well-formed fake responses rendered no lentago.dev row")

    for label, token, responder in DEGRADE_CASES:
        try:
            rows, reason = _run_budgets(gen, token, responder)
            body = [ln for ln in gen.error_budget_section(rows, reason)
                    if ln and not ln.startswith("## ")]
        except Exception as exc:                              # noqa: BLE001
            fail("budget", f"{label}: raised {type(exc).__name__} instead of degrading")
            continue
        if rows is not None or not reason:
            fail("budget", f"{label}: expected (None, reason), got {(rows, reason)!r}")
        elif len(body) != 1 or not body[0].startswith("_Unavailable this run:"):
            fail("budget", f"{label}: expected one 'Unavailable this run' line, got {body!r}")
        elif token is not None and token.strip() and "not configured" in reason:
            fail("budget", f"{label}: a set token was reported as not configured")


# ------------------------------------------------------------------ sweeper
def _dep_msg(*entries, terminator="..."):
    body = ["build(deps): bump things", "", "Bumps things.", "", "---", "updated-dependencies:"]
    for e in entries:
        first = True
        for k, v in e.items():
            body.append(("- " if first else "  ") + f"{k}: {v}")
            first = False
    if terminator:
        body.append(terminator)
    body += ["", "Signed-off-by: dependabot[bot] <support@github.com>"]
    return "\n".join(body)


def _dep(name, kind, version="1.2.3"):
    e = {"dependency-name": name}
    if version is not None:
        e["dependency-version"] = version
    e["dependency-type"] = "direct:production"
    if kind is not None:
        e["update-type"] = f"version-update:semver-{kind}"
    return e


def _pr(author="dependabot[bot]", head_repo="lentago/x", base="main", draft=False, sha="a" * 40):
    return {"user": {"login": author}, "draft": draft, "number": 1,
            "head": {"repo": {"full_name": head_repo}, "sha": sha},
            "base": {"ref": base, "repo": {"full_name": "lentago/x", "default_branch": "main"}}}


def _commit(msg, author="dependabot[bot]", verified=True, sha="a" * 40):
    return {"sha": sha, "author": {"login": author},
            "commit": {"message": msg, "verification": {"verified": verified}}}


_GREEN = _dep_msg(_dep("actions/checkout", "patch", "7.0.2"), _dep("lentago/sw/x.yml", "minor", "1.6.0"))

# (label, pr, commits, files, repo, passes?)
SWEEPER_CASES = [
    ("green patch+minor group", _pr(), [_commit(_GREEN)], [{"filename": ".github/workflows/ci.yml"}], "x", True),
    ("a major in the group", _pr(), [_commit(_dep_msg(_dep("a", "patch"), _dep("b", "major", "2.0.0")))], [], "x", False),
    ("0.x minor", _pr(), [_commit(_dep_msg(_dep("a", "minor", "0.4.0")))], [], "x", False),
    ("0.x patch", _pr(), [_commit(_dep_msg(_dep("a", "patch", "0.4.1")))], [], "x", True),
    ("v-prefixed 1.x minor", _pr(), [_commit(_dep_msg(_dep("a", "minor", "v1.4.0")))], [], "x", True),
    ("minor without version", _pr(), [_commit(_dep_msg(_dep("a", "minor", None)))], [], "x", False),
    ("missing update-type", _pr(), [_commit(_dep_msg(_dep("a", None)))], [], "x", False),
    ("no metadata block", _pr(), [_commit("build(deps): bump a\n\nno block here")], [], "x", False),
    ("unterminated block", _pr(), [_commit(_dep_msg(_dep("a", "patch"), terminator=None))], [], "x", False),
    ("not Dependabot's PR", _pr(author="cpitzi"), [_commit(_GREEN)], [], "x", False),
    ("foreign commit on the PR", _pr(), [_commit(_GREEN), _commit(_GREEN, author="lentago-claude-runner[bot]")], [], "x", False),
    ("unverified commit", _pr(), [_commit(_GREEN, verified=False)], [], "x", False),
    ("head in another repo", _pr(head_repo="someone/x"), [_commit(_GREEN)], [], "x", False),
    ("base not default branch", _pr(base="release"), [_commit(_GREEN)], [], "x", False),
    ("draft", _pr(draft=True), [_commit(_GREEN)], [], "x", False),
    ("touches the sweeper workflow", _pr(), [_commit(_GREEN)],
     [{"filename": ".github/workflows/dependabot-sweeper.yml"}], ".github", False),
    ("touches the sweeper script", _pr(), [_commit(_GREEN)],
     [{"filename": "fleet-ops/dependabot-sweeper.py"}], ".github", False),
    ("same path in another repo is fine", _pr(), [_commit(_GREEN)],
     [{"filename": "fleet-ops/dependabot-sweeper.py"}], "x", True),
    ("head moved while reading", _pr(sha="b" * 40), [_commit(_GREEN)], [], "x", False),
]


def check_sweeper_gate():
    path = os.path.join(ROOT, "fleet-ops", "dependabot-sweeper.py")
    try:
        spec = importlib.util.spec_from_file_location("dependabot_sweeper", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    except Exception as exc:                                  # noqa: BLE001
        fail("sweeper", f"fleet-ops/dependabot-sweeper.py failed to import — {exc}")
        return
    entries = mod.parse_updated_dependencies(_GREEN)
    if not entries or [e["dependency-name"] for e in entries] != ["actions/checkout", "lentago/sw/x.yml"]:
        fail("sweeper", f"parse_updated_dependencies() misread a two-entry block: {entries!r}")
    check_sweeper_audit(mod)
    for label, pr, commits, files, repo, passes in SWEEPER_CASES:
        try:
            problem = mod.pr_problem(pr, commits, files, repo)
        except Exception as exc:                              # noqa: BLE001
            fail("sweeper", f"{label}: pr_problem raised {type(exc).__name__}: {exc}")
            continue
        if passes and problem is not None:
            fail("sweeper", f"{label}: expected to pass, refused with {problem!r}")
        elif not passes and problem is None:
            fail("sweeper", f"{label}: expected a refusal, but it passed (that would be a merge)")


def check_sweeper_audit(mod):
    """The audit (ADR-0016 Decision 5) must recognise exactly what the sweeper
    writes, and nothing a person merely quotes. A miss here either hides a
    misuse or turns every run red for 30 days."""
    run = "https://github.com/lentago/.github/actions/runs/1"
    for label, msg in [("Dependabot message with Signed-off-by", _GREEN),
                       ("message with no trailer block", "build(deps): bump a\n\nBumps a.\n...")]:
        body = mod.merge_body(msg, run)
        if not mod.has_trailer("bump a (#1)\n\n" + body):
            fail("sweeper", f"merge_body() output is not seen by has_trailer() ({label}): {body[-120:]!r}")
    quoted = ("Adds the sweeper.\n\nEach merge ends with the `Merged-by-routine: dependabot-sweeper` "
              "trailer.\n\nCo-authored-by: Claude <noreply@anthropic.com>")
    middle = "Subject\n\nMerged-by-routine: dependabot-sweeper\n\nCo-authored-by: x <x@example.com>"
    for label, msg in [("trailer quoted in prose", quoted), ("trailer line outside the last paragraph", middle)]:
        if mod.has_trailer(msg):
            fail("sweeper", f"has_trailer() matched a {label}; the audit would flag a non-sweeper merge")

    dep = {"number": 1, "user": {"login": "dependabot[bot]"}}
    person = {"number": 2, "user": {"login": "cpitzi"}}
    commit = {"sha": "c" * 40}
    for label, marked, want in [("Dependabot's PR", [(commit, [dep])], 0),
                                ("someone else's PR", [(commit, [person])], 1),
                                ("no PR at all", [(commit, [])], 1),
                                ("mixed", [(commit, [dep, person])], 1)]:
        got = len(mod.audit_findings("x", marked))
        if got != want:
            fail("sweeper", f"audit_findings() on {label}: {got} findings, expected {want}")

    me, since = "cpitzi", "2026-11-18T00:00:00Z"
    rebase = lambda b: b.strip() == "@dependabot rebase"                    # noqa: E731
    for label, comments, want in [
            ("own comment after the head", [{"user": {"login": me}, "created_at": "2026-11-18T01:00:00Z",
                                             "body": "@dependabot rebase"}], True),
            ("own comment before the head", [{"user": {"login": me}, "created_at": "2026-11-17T23:00:00Z",
                                              "body": "@dependabot rebase"}], False),
            ("someone else's comment", [{"user": {"login": "other"}, "created_at": "2026-11-18T01:00:00Z",
                                         "body": "@dependabot rebase"}], False)]:
        if mod.commented_since(comments, me, since, rebase) != want:
            fail("sweeper", f"commented_since() on {label}: expected {want}")


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
    ("budget", check_error_budget_section),
    ("sweeper", check_sweeper_gate),
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
