# ADR-0007: Kits ship into client-owned estates; the practice never operates a multi-tenant service

**Status:** Accepted (2026-08-17)

## Context

Lentago Labs's positioning is **digital sovereignty for mission-driven
organizations** — the practice helps clients *leave* vendor lock-in rather than
becoming a new instance of it. That positioning has a structural credibility
problem baked in: an anti-lock-in consultant is only believable if firing them is
trivial. A client who cannot walk away without losing their data, their tooling, or
their ability to operate has simply swapped one lock-in for another, and the pitch
collapses. The trust cannot rest on a promise ("we'd never hold you hostage") — it
has to be true **by construction**.

The tempting shape for a consultancy is the opposite one: build a hosted service —
even a free or self-service tier — that many client organizations sign into. It is
the default SaaS growth story, it produces recurring revenue, and it feels like
leverage. But for *this* practice it is self-negating. The moment Lentago operates
one system serving many clients, Lentago *is* the dependency it sells against: it
custodies client data, it carries an implicit uptime obligation, and leaving it
means a migration rather than a fork.

This ADR records the standing delivery model as the practice's constitution for
every client-facing offering, so the boundary is a documented rule rather than a
case-by-case judgment call.

## Decision

**The consultancy never builds or hosts a SaaS — not even a free or self-service
one.** Every client-facing offering is delivered *into the client's own estate*, and
the practice never operates a system that serves many client organizations at once.

Concretely:

1. **Client-owned repos.** Every client-facing offering ships as a repository the
   **client owns** — a template plus an engagement, in open formats. The artifact is
   theirs from day one, not a tenancy on ours.
2. **Runs in the client's own accounts, on free primitives.** Anything that must run
   continuously runs in the **client's** accounts on free primitives — their Actions
   cron, their Pages/S3, their hardware, their Grafana free tier. Lentago does not
   host the running system.
3. **Multi-tenancy is the bright line.** Lentago **never** operates one system
   serving many client organizations: no shared endpoints, no pooled client data, no
   custody of client records. (Lentago's own estate serving Lentago's own *public*
   artifacts — the org profile, the fleet reports — is not client service and is
   unaffected by this rule.)
4. **Ongoing help is a fireable retainer, not a subscription.** Continuing support is
   a retainer performed **on the client's estate**, with a hand-off runbook standing
   from **day one** — never a subscription to a Lentago-operated service. Firing the
   retainer leaves the client with a working, documented, self-operable system.
5. **Shared logic ships as open source.** Reusable logic is published open source;
   **forkable is the exit path.** The client's ability to fork and self-maintain is
   the guarantee, not a courtesy.
6. **Every kit documents its own dependencies and exits — including ours.** Each kit
   names what it depends on and how to leave each dependency, and **GitHub/Actions is
   a vendor too**: the kit says how to exit it, not just the third parties.

The through-line: the anti-lock-in claim is made **true by construction**. Firing
Lentago — retainer, tooling, or the whole engagement — is a fork and a runbook, not
a migration off a service we run.

## Alternatives

- **Operate a hosted multi-tenant service — even free, even self-serve (the rejected
  default).** *Rejected.* This is the option the whole positioning exists to refute.
  It would make the practice the very dependency it sells against; it would pool
  client data under Lentago's custody; and it would create an implicit uptime
  obligation that a one-operator shop cannot honestly carry. Every dollar of
  "recurring software revenue" it earned would be bought by becoming the lock-in the
  client hired us to escape. The convenience of one system to maintain is not worth
  negating the pitch.
- **A shared platform hosting several client organizations (parked, not permitted as
  stated).** Hosting a common platform for multiple member organizations is **not**
  permitted under this rule *while Lentago is the operator* — that is landlordship,
  and it re-creates the pooled-custody and uptime problems above. It becomes
  permissible only in a specific shape: a genuinely **member-governed entity** owns
  and operates the platform, with Lentago contracted to it as a **fireable
  maintainer** rather than acting as landlord. That inverts the dependency — the
  members can fire Lentago without losing the platform — which is the whole point.
  Parked here so the boundary is explicit rather than rediscovered per deal.

## Consequences

Be honest about the costs — they are the point, not incidental:

- **No recurring software revenue.** Income is engagements, retainers, and grants —
  not subscriptions. The practice forgoes the SaaS revenue curve deliberately.
- **Kits must be boring-simple to operate**, because the **client** operates them.
  Wherever possible the whole runtime is **Actions cron + Issues + email** — no
  server to run, nothing that assumes a Lentago-hosted control plane. Cleverness that
  the client cannot maintain is a defect, not a feature.
- **The scale path is more templates and more trained people — not more tenants.**
  Growth is horizontal in kits and practitioners; it is never "add another org to the
  shared system." That caps one growth vector on purpose.
- **A broken client kit pages the client, not Lentago** — because it runs in the
  client's estate. This is a **deliberate property**, not a coverage gap: the client
  owns and operates their system, and the day-one hand-off runbook is what makes that
  ownership real. Lentago's fireability and the client's operational ownership are two
  faces of the same design; you cannot have the first without accepting the second.

This ADR is the constitution for client-facing offerings: any new offering is
checked against the six points above before it ships, and the parked shared-platform
case above marks the one boundary where a hosted-looking arrangement is allowed —
only when a member-governed entity, not Lentago, is the operator.
