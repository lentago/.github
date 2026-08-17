# Lock-in Ledger — template + renewal-calendar-as-code

A **Lock-in Ledger** answers one question for every vendor you depend on: *how
hard would it be to leave?* It scores each dependency on four fixed axes so the
answers are comparable across vendors and stay honest over time. The point isn't
to leave — it's to know the exit exists **before** you need it. That's the
receipt behind the fleet's delivery pledge (*"firing us is a runbook"*).

This directory holds the reusable pieces. The fleet's own filled-in ledger — the
worked example — lives one level up at
[`../lock-in-ledger.md`](../lock-in-ledger.md).

| File | What it is |
|---|---|
| [`TEMPLATE.md`](TEMPLATE.md) | The blank four-axis rubric, ready to copy per organization. |
| [`renewals.yml`](renewals.yml) | Renewal-calendar-as-code — every dated obligation that lapses if nobody acts. This is the fleet's real calendar, kept public-safe. |
| [`check-renewals.py`](check-renewals.py) | Pure date filter over `renewals.yml`: emits, as JSON, the entries whose reminder window is open. No network, no side effects — testable and dry-runnable. |
| `../../.github/workflows/renewal-calendar.yml` | Runs the checker daily and opens a tracking issue ahead of each due date, deduped so a reminder is filed once. |

## Why a renewal calendar belongs in a lock-in ledger

Most vendor lock-in is about getting your data and config *out*. A lapsed
domain, expired certificate, or cancelled subscription is the opposite failure —
lock-*out* — and no export plan protects against it. It's the one flavour of
lock-in no vendor causes on purpose, so it's the easiest to forget. Tracking it
as code, with a scheduled reminder, closes that gap the same way everything else
in the fleet is closed: in git, reviewed, automated.

## Using it for your own org

1. Copy `TEMPLATE.md`, fill a row per vendor, and be honest about the bad scores
   — a flattering self-audit is worthless.
2. Copy `renewals.yml` and list your dated obligations. **Public-safe only:** no
   credential values, no account identifiers, no cost figures — name the
   obligation and its date, nothing more.
3. Adapt the workflow to your repo (it uses the default `GITHUB_TOKEN` and needs
   only `issues: write`).

Test the calendar locally without creating anything:

```bash
python3 fleet-reports/lock-in/check-renewals.py --check          # validate shape
python3 fleet-reports/lock-in/check-renewals.py --today 2026-10-20   # preview what would fire
```
