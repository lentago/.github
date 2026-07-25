#!/usr/bin/env python3
"""Repo validator for lentago/.github — the check that gates PRs here.

This repo carries no application code, so "does it build" is meaningless. What it
*does* carry is operator tooling the rest of the fleet depends on, plus the public
org landing page. Those have real failure modes, and this asserts against them:

  configs   fleet-ops/*.json parse and hold the shape fleet-apply.sh expects. A
            malformed required-checks.json breaks a fleet-wide settings sweep
            partway through, leaving the fleet half-applied.
  census    metrics/generate-fleet-reports.py imports, and its data/code classifier
            still routes known paths correctly (regression cover for #59, where a
            JSON-only carve-out counted 15,595 lines of CSV exports as source).
  links     relative markdown links resolve. The fleet's most common change class is
            renames and removals, which is exactly what silently breaks these — see
            #57, where a deliberate rename audit edited a broken image line on a
            public README without noticing it pointed at nothing.
  register  fleet-reports/incidents.md is reproducible from fleet-reports/incidents/.
            It is generated, not hand-authored; a hand-edit here is a change that the
            next weekly refresh silently reverts.

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

        if os.path.basename(rel) != "required-checks.json":
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

    for repo, path, want in MD_CASES:
        got = gen.classify_md(repo, path)
        if got != want:
            fail("census", f"classify_md({repo!r}, {path!r}) returned {got!r}, expected {want!r}")


# ------------------------------------------------------------------ links
# Inline markdown links/images. Reference-style definitions are not used in this repo;
# if that changes, extend here rather than loosening the resolver.
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
SKIP_SCHEME = re.compile(r"^(https?|mailto|tel|ftp|data):", re.I)


def check_relative_links():
    for rel in tracked("*.md"):
        path = os.path.join(ROOT, rel)
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()

        in_fence = False
        for lineno, line in enumerate(lines, 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue

            for target in LINK_RE.findall(line):
                if SKIP_SCHEME.match(target) or target.startswith("#"):
                    continue
                if target.startswith("//"):
                    continue
                # Site-absolute routes are resolved by a site router, not the
                # filesystem. This repo has none; skip rather than false-positive.
                if target.startswith("/"):
                    continue

                bare = target.split("#", 1)[0].split("?", 1)[0]
                if not bare:
                    continue
                resolved = os.path.normpath(
                    os.path.join(os.path.dirname(path), bare))
                if not os.path.exists(resolved):
                    fail("links", f"{rel}:{lineno} → {target} (no such path)")


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
    ("census", check_census_classifier),
    ("links", check_relative_links),
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
