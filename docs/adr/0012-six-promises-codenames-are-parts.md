# ADR-0012: The offering is told as six promises; codenames are parts

**Status:** Accepted (2026-10-12)

## Context

By 2026-10-12 the fleet carried fourteen botanical codenames, and the public
surfaces told the offering four different ways: four receipt-linked offerings on
lentago.dev and the org profile, five "named systems" in the site's Suite
section, eleven rows in the profile's suite table, and fourteen pieces threaded
through the five adoption stories in `lentago/lupinus`. The offerings epic
([#134](https://github.com/lentago/.github/issues/134)) already held a second,
outcome-named layer (Good-Standing, Liberation Pipeline, Digital Custody,
Insurance-Receipts, Board pack and the rest), deliberately unadvertised until
each has a receipt.

The reader [ADR-0008](0008-pro-bono-practice-one-reader.md) names is the one
tech person at an organization that runs on volunteers and donations. The
2026-10-12 research pass found that the most common answer such shops give to
"which tool do you need" is "we are unsure what we need." A front door made of
fourteen Latin names reads as complexity to that reader, while the practice's
whole claim is the opposite: simpler operations, under the organization's own
control.

## Decision

1. **The offering is six promises every shop needs, plus three for when you need
   them.** The canonical wording lives in [`docs/voice.md`](../voice.md) under
   *Canonical blocks* and is copied, not paraphrased:
   - Your site and giving page
   - Your records and your proof
   - Your machines and logins
   - Your alarms and status
   - Your help desk and runbooks
   - Your data and your exit
   - When you need them: your building · cloud you own · AI with receipts
2. **Every codename is a part under exactly one promise.** A part carries its
   codename, its genus mark, a plain-words role, and its tier from the lupinus
   registry. Codenames never appear in a headline on a reader-facing surface;
   they appear in the parts list. The roles, which are descriptions and not
   renames:

   | Part | Role | Promise |
   |---|---|---|
   | monarda | campaign page | site and giving page |
   | uvularia | records and deadlines | records and proof |
   | kalmia | machine setup | machines and logins |
   | drosera | alerts and status | alarms and status |
   | betula | capture and keep | alarms and status |
   | mitchella | front desk | help desk and runbooks |
   | lock-in ledger | what you'd lose | data and exit |
   | epigaea | building sensors | your building |
   | brasenia | lobby screen | your building |
   | solidago, osmunda | cloud you own | cloud you own |
   | claytonia | AI with receipts | AI with receipts |

   betula is the one part that serves two promises (logs under alarms, exports
   under data and exit); it is listed once, under alarms and status, and data and
   exit cross-references it for exports.
3. **The guide is the spine, not a product.** asclepias (vol. 1) and lupinus
   (vol. 2) sit under the map as the manual, and the adopter's ops vault is part of
   promise five. The pledge ([ADR-0007](0007-client-owned-delivery-no-multi-tenant-saas.md))
   sits under all nine promises.
4. **The map has a third band: what is free and not ours.** The stories' *Free
   tier* tag made visible on every surface: a free GitHub organization, Grafana
   Cloud's free tier, a payment processor's hosted page, the nonprofit tiers of
   Google Workspace and Microsoft 365, Apple Business, Slack for Nonprofits, and
   the rest. Honesty about what runs for nothing is part of the promise.
5. **"Nothing on this list is advertised" still holds.** Projected parts appear on
   public surfaces only the way the Suite section already shows roadmap lines,
   and in the stories only with their Projected tag and open issue.
6. **One map, every surface.** lentago.dev's Suite section, the org profile's
   suite table, the lupinus stories' coverage matrix and picker, and the banner
   taglines in `brand/fleet.json` all use the same promises in the same words.
   The rollout is tracked in the epic this record links from.

## Alternatives

- **Keep the four surfaces as they are.** Rejected: four counts of the same thing
  is the complexity the reader sees first.
- **Rename the repositories to plain names.** Rejected: the rename discipline's
  four tiers make that a months-long debt for no gain; the codenames are the
  parts' names, and the plain words are their roles.
- **Organize by who is asking** (the board, the funder, the insurer, the
  auditor). Rejected as the primary frame, kept as the cross-cut inside *your
  records and your proof*, where every proof kit lives.
- **Fold the three "when you need them" into the six.** Rejected: a building, an
  AWS account, and an agent fleet are not every shop's week, and saying so is
  what keeps the six credible.

## Consequences

- `docs/voice.md` gains a canonical block for the promises; every surface copies it.
- lentago/site-lentago-dev#99 rewrites the Suite section as the map;
  lentago/lupinus#19 re-cuts the stories (one spine, three rungs, one map) and
  pivots the coverage matrix to promise rows; the org profile's suite table is
  regrouped by promise; `brand/fleet.json` taglines lead with each part's role.
  Each is an item on the rollout epic.
- The lupinus tier registry stays the only place a part's tier is asserted; the
  map links to it rather than restating it.
- The LAN brainstorm page that proposed the map is working material, not a
  surface, and is not cited from any repo.
