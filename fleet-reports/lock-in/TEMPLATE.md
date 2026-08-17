# Lock-in Ledger — <ORGANIZATION>

**Compiled:** <YYYY-MM-DD> · **Scope:** <every external vendor this
organization depends on to operate> · **Method:** self-assessment against the
four-axis rubric below; comparative, not audited.

> A Lock-in Ledger is a vendor-dependency self-audit. For each vendor you rely
> on, it asks one question — *how hard would it be to leave?* — and answers it on
> four fixed axes so the answers are comparable across vendors and honest over
> time. The point is not to leave; the point is to know the exit exists **before**
> you need it. Fill a row in badly and the row itself is the finding.
>
> Pair this file with a [`renewals.yml`](renewals.yml) so that the one lock-in no
> vendor causes — a lapsed domain, cert, or subscription — can't sneak up on you.
> A worked example of both, auditing a real fleet, lives one level up at
> [`../lock-in-ledger.md`](../lock-in-ledger.md).

---

## The rubric

Score every dependency on all four axes. The axes are about **exit**, not about
how pleasant the vendor is day-to-day — a vendor can be excellent to use and
still be a trap to leave.

| Axis | The question it answers |
|---|---|
| **Export fidelity** | Can you get *everything* out, and in what form — the config, the data, the history? |
| **Format openness** | Once it's out, is it usable somewhere else, or is it a proprietary dump that only re-imports to the same vendor? |
| **Identity / custody** | Who actually holds the keys and the names — the namespace, the account, the issuer identity? |
| **Documented exit** | Is there a *written* exit path, and where does it live? An exit that lives only in someone's head is not an exit. |

**Rating scale** (comparative, self-assessed — not a correctness claim):

| | Meaning |
|---|---|
| **Strong** | Exit is a runbook: standard tools/protocols, definitions in version control, no vendor gate. |
| **Moderate** | Exit is doable but lossy or partial — some rework, some data left behind. |
| **Limited** | Exit is possible only for part of the surface; the rest is coupled or non-portable. |
| **Weak** | The vendor holds something you cannot take with you. |

Keep this file public-safe: no credentials, no account identifiers, no cost
figures. The ledger is a posture document, not a secrets store.

---

## Summary

Fill one row per dependency. Order by whatever matters most to you — we sort by
how load-bearing the dependency is.

| Dependency | Export fidelity | Format openness | Identity / custody | Documented exit |
|---|:--:|:--:|:--:|:--:|
| **<vendor / service>** | <Strong/Moderate/Limited/Weak> | <…> | <…> | <…> |
| **<vendor / service>** | | | | |
| **<vendor / service>** | | | | |

> **Tip:** custody usually runs strongest where *you* hold the names (your
> domain registrar, and anything that rides on a domain you own) and weakest
> where the vendor mints an identity you can't reproduce elsewhere (a proprietary
> dataset, an issuer identity, a managed account). Everything else is downstream
> of that — so audit the name-holders first.

---

## The ledger

Repeat this block once per dependency. Write the *reason* for each score, not
just the word — the reason is what a reader (or a future you) needs.

### <vendor / service> — <what it does for you>

- **Export fidelity — <rating>.** <Can you get the config, the data, and the
  history out? By what mechanism — API, standard protocol, a clone? What's left
  behind?>
- **Format openness — <rating>.** <Once exported, does it run/import elsewhere,
  or only back into this vendor?>
- **Identity / custody — <rating>.** <Who holds the namespace, the account, the
  issuer identity? What of *yours* sits underneath it?>
- **Documented exit — <rating>.** <Is the exit written down? Where? If it isn't,
  say so — an undocumented exit scores Limited at best.>

---

## What the ledger tells you to do

Read down the **Documented exit** column: the Limited/Weak cells are your backlog.
Turn each into a concrete follow-up — usually one of:

1. **Write the missing runbook** for an exit that exists only in principle.
2. **Decide, explicitly,** that some retained data isn't worth an exit path — and
   record that decision rather than leaving it implied.
3. **Move a name you don't hold** under one you do (e.g. put a service behind a
   domain you own so custody is inherited, not rented).
4. **Keep the root healthy** — track every renewal that could lapse as code (see
   [`renewals.yml`](renewals.yml)).

## Update log

Re-audit on a cadence (annually, or whenever a vendor changes materially). Each
pass gets a dated line — the ledger is only useful if its scores stay current.

| Date | Change |
|---|---|
| <YYYY-MM-DD> | First publication. |
