# Lock-in Ledger — Lentago Labs' own vendor dependencies

**Compiled:** 2026-08-17 · **Scope:** every external vendor the fleet actually
depends on to operate. · **Method:** self-assessment against a fixed four-axis
rubric; comparative, not audited.

This is the fleet auditing *itself* before it audits anyone. The delivery pledge
— *"you'll own every piece, we'll teach your people, and firing us is a
runbook"* — is a claim, and a claim about exit-readiness is only worth the
receipt behind it. **This file is that receipt.** If our own scores are bad, the
honest move is to publish the bad scores and the reason, not to launder them; an
audit that flatters the auditor is worthless.

The client-facing version of this exercise — the blank rubric plus the
renewal-calendar-as-code that keeps a custody lapse from being the thing that
locks you in — lives under [`lock-in/`](lock-in/). Our own renewal calendar
([`lock-in/renewals.yml`](lock-in/renewals.yml)) is the working example.

---

## The rubric

Every dependency is scored on four axes. The axes are deliberately about *exit*,
not about how good the vendor is day-to-day — a vendor can be excellent to use
and still be a trap to leave.

| Axis | The question it answers |
|---|---|
| **Export fidelity** | Can we get *everything* out, and in what form — the config, the data, the history? |
| **Format openness** | Once it's out, is it usable somewhere else, or is it a proprietary dump that only re-imports to the same vendor? |
| **Identity / custody** | Who actually holds the keys and the names — the namespace, the account, the issuer identity? |
| **Documented exit** | Is there a *written* exit path, and where does it live? An exit that only exists in someone's head is not an exit. |

**Rating scale** (comparative, self-assessed):

| | Meaning |
|---|---|
| **Strong** | Exit is a runbook: standard tools/protocols, definitions in git, no vendor gate. |
| **Moderate** | Exit is doable but lossy or partial — some rework, some data left behind. |
| **Limited** | Exit is possible only for part of the surface; the rest is coupled or non-portable. |
| **Weak** | The vendor holds something we cannot take with us. |

No score here is a claim that our position is *correct* or *best practice* — only
where we sit relative to a clean, portable baseline. Costs, account identifiers,
and credentials are deliberately absent: this is a public repo.

---

## Summary

| Dependency | Export fidelity | Format openness | Identity / custody | Documented exit |
|---|:--:|:--:|:--:|:--:|
| **Domain registrar** | Strong | Strong | Strong | Strong |
| **Fastmail** (MX) | Strong | Strong | Strong | Moderate |
| **GitHub** (repos / Actions / attestations) | Moderate | Moderate | Limited | Moderate |
| **AWS** (solidago) | Strong | Moderate | Limited | Moderate |
| **Grafana Cloud** (drosera) | Moderate | Strong | Limited | Moderate |
| **Axiom** (betula) | Moderate | Strong | Weak | Limited |
| **Anthropic / Claude Code** (the AI-assistant dependency) | Strong | Strong | Limited | Limited |

The shape of that table is the whole point: **custody runs strongest where we
hold the names ourselves** (the registrar, and Fastmail *because* the domain is
ours) and weakest where the vendor holds an identity we can't mint elsewhere
(Axiom datasets, GitHub's OIDC issuer, the model provider). Everything else is
downstream of that. The registrar row is the root — which is exactly why its one
real failure mode (a lapsed renewal) gets its own calendar-as-code, below.

---

## The ledger

### Domain registrar — the root of custody

- **Export fidelity — Strong.** A domain is portable by construction: the
  registrar holds a registration, not the name. An EPP/auth code plus an ICANN
  transfer moves it to any other registrar. The DNS zone exports as a plain zone
  file.
- **Format openness — Strong.** DNS is an open standard; registrar-to-registrar
  transfer is an ICANN-mandated process, not a favour the current registrar does
  us.
- **Identity / custody — Strong.** This is the one place we hold the actual
  name. Every other custody position in this ledger is downstream of it — email
  survives a provider change because the domain is ours, sites survive a host
  change for the same reason.
- **Documented exit — Strong.** Transfer is standardized. The *only* real risk
  is not eviction but **lapse**: an expired domain is a custody failure with no
  villain. That risk is what [`lock-in/renewals.yml`](lock-in/renewals.yml) and
  its scheduled workflow exist to close.

### Fastmail — mail, riding on a domain we own

- **Export fidelity — Strong.** Mailboxes come out over IMAP as mbox/maildir;
  contacts and calendars over CardDAV/CalDAV as vCard/ICS. Nothing is trapped in
  a proprietary store.
- **Format openness — Strong.** IMAP/JMAP, mbox, vCard, ICS — all open
  standards that any competing provider ingests.
- **Identity / custody — Strong.** The address is `@lentago.dev`, and MX is just
  a record in a zone we control. Re-pointing MX to another provider changes the
  backend without changing a single address. Custody here is inherited from the
  registrar row — which is exactly why owning the domain matters more than
  choosing the mail host well.
- **Documented exit — Moderate.** The mechanics (re-point MX, bulk-migrate over
  IMAP) are well-trodden and low-risk, but the step-by-step isn't yet written
  down as a fleet runbook — so it scores Moderate, not Strong, honestly.

### GitHub — repos, Actions, attestations

- **Export fidelity — Moderate.** The code is Strong on its own: a git clone is
  the full history, distributed by design, and every mirror is a complete copy.
  The score drops to Moderate because the *platform layer around* the code —
  issues, PR reviews, Actions run logs, rulesets, build attestations — only
  comes out through the API, and reconstructing it on another forge is lossy.
- **Format openness — Moderate.** git is fully portable. Actions workflows are
  GitHub-flavoured YAML — the *idea* ports, the files don't run verbatim
  elsewhere. Issue/PR exports are JSON with no cross-forge standard.
- **Identity / custody — Limited.** We hold every line of code; we do **not**
  hold the `github.com/lentago` namespace, nor the OIDC issuer identity that our
  Actions use to assume AWS roles and sign build attestations. Move forges and
  those identities are re-minted, not carried — every consumer that trusts the
  old issuer has to be re-pointed.
- **Documented exit — Moderate.** A full git mirror is trivial and could be
  automated tomorrow. The platform-metadata and CI-identity side of the exit was
  *not* written down anywhere until this ledger named it — so this row is a
  to-do as much as a score.

### AWS — the solidago platform

- **Export fidelity — Strong.** The platform is 100% Terraform, so its shape is
  in git in full. The live data comes out with standard tools — `pg_dump` for
  RDS, straight object copies for S3. Nothing about the running system is
  un-exportable.
- **Format openness — Moderate.** The *data* is fully open (Postgres dumps, S3
  objects go anywhere). The *definitions* are HCL bound to the AWS provider —
  every resource maps to an AWS API, so the Terraform rebuilds solidago on AWS
  faithfully but does not port to another cloud without a rewrite. Portable data,
  coupled infrastructure.
- **Identity / custody — Limited.** The account, its IAM, and the OIDC trust that
  lets CI assume roles are all AWS-held. We hold the definitions and the data,
  not the account identity.
- **Documented exit — Moderate.** "Terraform apply + `pg_dump` restore" is a
  documented rebuild *within* AWS. A cross-cloud exit is a rewrite, and that path
  isn't written down — so Moderate, not Strong.

### Grafana Cloud — the drosera observability stack

- **Export fidelity — Moderate.** The source of truth is Strong: dashboards and
  alert rules are Terraform-provisioned, so the definitions live in the drosera
  repo, not in the vendor. The stored *metric and log history* behind them is the
  Moderate part — bulk export of long-range TSDB data is bounded and lossy.
- **Format openness — Strong.** Dashboard JSON is the same schema that
  self-hosted Grafana OSS reads, so the panels drop straight into an
  open-source Grafana with no translation.
- **Identity / custody — Limited.** The stack URL and org are Grafana-held; the
  dashboards-as-code are ours.
- **Documented exit — Moderate.** Because the config is Terraform, standing up
  self-hosted Grafana and re-applying is a real, partly-documented path (drosera
  is built config-first for exactly this reason). Historical data does not follow.

### Axiom — the betula log sink

- **Export fidelity — Moderate.** The ingestion pipeline is ours (the shipper
  and its config live in betula), so *new* logs can be re-pointed at another sink
  the day we decide to. Getting the *already-stored* logs back out is
  query-and-export, bounded by retention — a backfill, not a clean dump.
- **Format openness — Strong.** Logs are JSON/NDJSON — about as portable as data
  gets. Whatever comes out is immediately usable elsewhere.
- **Identity / custody — Weak.** The dataset and org identity are Axiom-held, and
  there's no name of ours underneath them to inherit custody from — unlike mail,
  which rides on our domain. This is the weakest custody row in the ledger, and
  it's marked Weak on purpose.
- **Documented exit — Limited.** Re-pointing the shipper is easy and half the
  exit; recovering the retained history is the half with no clean, documented
  path.

### Anthropic / Claude Code — the AI-assistant dependency

The honest one, because it's the dependency least like the others: we don't
store data *in* it, we depend on a *capability*.

- **Export fidelity — Strong.** The work product is not held by the vendor at
  all — every change the agent fleet makes lands as a reviewed PR in a repo we
  own, and the session transcripts sit on local disk. There is nothing to
  "export back" because the output was ours the whole time.
- **Format openness — Strong.** What the assistant produces is plain
  code and markdown, and the instruction layer (the `CLAUDE.md` family, the
  prompt-programs) is portable natural language. None of it is a proprietary
  artifact.
- **Identity / custody — Limited.** The *harness* — the claytonia agent fleet —
  is ours and self-hosted, but it is coupled to Claude Code specifically, and the
  capability behind it is Anthropic-held. We own the orchestration; we rent the
  intelligence.
- **Documented exit — Limited.** The theoretical exit is "swap the model behind
  the harness," but the harness is provider-coupled, so a real substitution means
  reworking claytonia, not flipping a config key. That rework isn't written down
  as a runbook — which makes this, alongside Axiom, one of the two rows where the
  score reflects a genuine gap rather than an inherent vendor trap.

---

## What the ledger tells us to do

Reading down the *Documented exit* column, the pattern is that our **config**
custody is consistently strong (everything that matters is in git) while our
**data** custody and our **written exit paths** are where the gaps are. The
concrete follow-ups this self-audit surfaces, in rough priority:

1. **Write the GitHub platform-exit runbook** — automated git mirroring plus the
   CI-identity re-pointing steps. Today the exit exists in principle, not on
   paper.
2. **Write the Fastmail migration runbook** so the Strong custody position has a
   Strong exit to match.
3. **Close the two Limited-exit rows honestly** (Axiom history, Anthropic
   substitution) — either by documenting the partial exit as *partial*, or by
   deciding the retained data isn't worth an exit path and saying so.
4. **Keep the root healthy.** Every custody position downstream of the domain is
   only as safe as the domain's renewal. That is now tracked as code —
   [`lock-in/renewals.yml`](lock-in/renewals.yml) — with a scheduled workflow
   that files an issue ahead of every due date.

The scores will move as those get done. When they do, this file gets the new
scores and a dated line below — same discipline as the other fleet reports:
published, versioned, honest.

## Update log

| Date | Change |
|---|---|
| 2026-08-17 | First publication. Seven dependencies scored; follow-ups filed against the two Limited-exit rows and the two missing runbooks. |
