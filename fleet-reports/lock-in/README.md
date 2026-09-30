# Lock-in Ledger — template + renewal-calendar-as-code

**What you're about to do:** pick up two reusable pieces — a blank scoring
template and a renewal calendar you keep as code — so you can build your own
Lock-in Ledger for every vendor your org depends on.

**Why bother:** a Lock-in Ledger answers one question for each vendor: *how
hard would it be to leave?* It scores each dependency on four fixed axes, so
the answers are comparable across vendors and stay honest over time. The
point isn't to leave — it's to know the exit exists **before** you need it.
That's the receipt behind our delivery pledge (*"firing us is a runbook"*).

**Time:** an afternoon for a whole estate, honestly scored. Half an hour gets
your first few vendors down; wiring up the renewal calendar is another ten
minutes.

This directory holds the reusable pieces. Our own filled-in ledger — the
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

1. Copy `TEMPLATE.md` and fill in a row per vendor. Be honest about the bad
   scores — a self-audit that only tells you good news is worthless.
2. Copy `renewals.yml` and list your own dated obligations. **Public-safe
   only:** no credential values, no account identifiers, no cost figures —
   name the obligation and its date, nothing more.
3. Adapt the workflow to your repo. It runs on `GITHUB_TOKEN`, the token
   GitHub Actions hands every workflow run automatically, so there's no extra
   secret to create — it just needs the `issues: write` permission turned on.

Test the calendar locally without creating anything:

```bash
python3 fleet-reports/lock-in/check-renewals.py --check          # validate shape
python3 fleet-reports/lock-in/check-renewals.py --today 2026-10-20   # preview what would fire
```
