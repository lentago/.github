#!/usr/bin/env python3
"""Emit the renewals from renewals.yml that are due for a reminder.

Renewal-calendar-as-code: this reads the machine-readable calendar next to it and
prints, as JSON, every entry whose reminder window is open on a given date — i.e.
today is within `lead_days` of `next_due`, or `next_due` is already past (an
overdue obligation should shout, not go quiet). The scheduled workflow
(.github/workflows/renewal-calendar.yml) feeds that JSON into `gh issue create`,
deduping on the per-item marker so an already-open reminder is never re-filed.

It does no network I/O and creates nothing — it's a pure date filter, so it can be
unit-tested and dry-run locally:

    python3 fleet-reports/lock-in/check-renewals.py --today 2026-10-20
    python3 fleet-reports/lock-in/check-renewals.py --check     # validate only

`--today` overrides the reference date (default: today, UTC). `--check` validates
the file's shape and exits non-zero on any problem, emitting nothing.
"""
import argparse
import datetime as dt
import json
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("check-renewals: PyYAML is required (pip install pyyaml)")

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_PATH = os.path.join(HERE, "renewals.yml")
CATEGORIES = {"domain", "cert", "subscription", "credential", "other"}
REQUIRED = ("id", "name", "category", "next_due")


def _parse_date(value, where, errors):
    """A date may arrive as a datetime.date (YAML) or an ISO string."""
    if isinstance(value, dt.date):
        return value
    if isinstance(value, str):
        try:
            return dt.date.fromisoformat(value.strip())
        except ValueError:
            errors.append(f"{where}: next_due {value!r} is not an ISO date (YYYY-MM-DD)")
            return None
    errors.append(f"{where}: next_due must be an ISO date, got {type(value).__name__}")
    return None


def load(path):
    """Parse and validate the calendar. Returns (entries, default_lead, errors)."""
    errors = []
    try:
        with open(path, encoding="utf-8") as fh:
            doc = yaml.safe_load(fh) or {}
    except (OSError, yaml.YAMLError) as exc:
        return [], 30, [f"{path} is unreadable — {exc}"]

    default_lead = 30
    defaults = doc.get("defaults") or {}
    if "lead_days" in defaults:
        if isinstance(defaults["lead_days"], int) and defaults["lead_days"] >= 0:
            default_lead = defaults["lead_days"]
        else:
            errors.append("defaults.lead_days must be a non-negative integer")

    raw = doc.get("renewals")
    if not isinstance(raw, list) or not raw:
        errors.append("top-level 'renewals' must be a non-empty list")
        return [], default_lead, errors

    entries, seen = [], set()
    for i, entry in enumerate(raw):
        where = f"renewals[{i}]"
        if not isinstance(entry, dict):
            errors.append(f"{where} is not a mapping")
            continue
        for key in REQUIRED:
            if not entry.get(key):
                errors.append(f"{where} is missing required key '{key}'")
        rid = entry.get("id")
        if rid:
            where = f"renewals['{rid}']"
            if rid in seen:
                errors.append(f"{where}: duplicate id — the second reminder would collide")
            seen.add(rid)
        cat = entry.get("category")
        if cat and cat not in CATEGORIES:
            errors.append(f"{where}: category {cat!r} not one of {sorted(CATEGORIES)}")
        due = _parse_date(entry.get("next_due"), where, errors) if entry.get("next_due") else None
        lead = entry.get("lead_days", default_lead)
        if not (isinstance(lead, int) and lead >= 0):
            errors.append(f"{where}: lead_days must be a non-negative integer")
            lead = default_lead
        if rid and due:
            entries.append({
                "id": rid,
                "name": entry.get("name", rid),
                "category": cat,
                "next_due": due,
                "lead_days": lead,
                "owner": entry.get("owner"),
                "notes": (entry.get("notes") or "").strip(),
            })
    return entries, default_lead, errors


def due_items(entries, today):
    """The entries whose reminder window is open on `today`, soonest first."""
    out = []
    for e in entries:
        remaining = (e["next_due"] - today).days
        if remaining <= e["lead_days"]:  # window open, including overdue (negative)
            iso = e["next_due"].isoformat()
            overdue = remaining < 0
            marker = f"renewal:{e['id']}:{iso}"
            state = "OVERDUE" if overdue else f"due in {remaining}d"
            title = f"[renewal] {e['name']} — due {iso}"
            body_lines = [
                f"Automated renewal reminder from `fleet-reports/lock-in/renewals.yml` (`{e['id']}`).",
                "",
                f"- **What:** {e['name']}",
                f"- **Category:** {e['category']}",
                f"- **Due:** {iso} ({state})",
            ]
            if e["owner"]:
                body_lines.append(f"- **Owner:** {e['owner']}")
            if e["notes"]:
                body_lines += ["", e["notes"]]
            body_lines += [
                "",
                "When the renewal is done, update `next_due` in `renewals.yml` and close this issue.",
                "",
                f"<!-- {marker} -->",
            ]
            out.append({
                "id": e["id"],
                "title": title,
                "marker": marker,
                "overdue": overdue,
                "days_remaining": remaining,
                "body": "\n".join(body_lines),
            })
    out.sort(key=lambda x: x["days_remaining"])
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--renewals", default=DEFAULT_PATH, help="path to renewals.yml")
    ap.add_argument("--today", help="reference date YYYY-MM-DD (default: today UTC)")
    ap.add_argument("--check", action="store_true",
                    help="validate the calendar and exit non-zero on any problem; emit nothing")
    args = ap.parse_args()

    entries, _, errors = load(args.renewals)
    if errors:
        print("renewals.yml has problems:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    if args.check:
        print(f"ok — {len(entries)} renewal(s) parsed", file=sys.stderr)
        return 0

    if args.today:
        try:
            today = dt.date.fromisoformat(args.today)
        except ValueError:
            return f"--today {args.today!r} is not an ISO date"
    else:
        today = dt.datetime.now(dt.timezone.utc).date()

    print(json.dumps(due_items(entries, today), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
