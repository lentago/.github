# ADR-0008: Lentago Labs is a pro-bono practice with one reader; the estate is the demonstration

**Status:** Accepted (2026-09-30)

## Context

From 2026-08-12 the org's public surfaces carried two positionings at once.
The first, added that day
([#88](https://github.com/lentago/.github/issues/88),
[#89](https://github.com/lentago/.github/issues/89),
[#90](https://github.com/lentago/.github/issues/90),
[#103](https://github.com/lentago/.github/pull/103)), described Lentago Labs
as a **shared learning lab for IT-operations colleagues**: a real estate that
invited peers could explore, exercise, and "carry back to the day job." The
second, added 2026-08-16/17 with the lentago.dev landing site and
[ADR-0007](0007-client-owned-delivery-no-multi-tenant-saas.md), described a
**practice building modern operations for mission-driven organizations**.

Every downstream surface inherited one or both: the README footer on sixteen
repos, the *"This is a lab — the systems are real, the stakes are not"* opener
on seventeen, the org profile's "crew" line, the whole premise of the
`asclepias` field guide (an org invite as step one, a member roster, labs
whose access lines assume membership), and the two-audience split written into
`lupinus` (ADR-0001 there: "asclepias onboards invited colleagues into the
maintainer's live fleet; different audience, different voice, different repo").

The learning-lab audience never arrived. As of 2026-09-30 the org has two
members, both the maintainer; the roster has one row; the `Players` team was
retired 2026-08-28; no lab-run issue was ever opened. Nothing external depends
on the membership on-ramp.

Meanwhile the practice framing was incomplete in the other direction: nothing
on lentago.dev or the profile said the help is free, and the contact section
read as paid consulting ("book a consult", "one-off audits").

The two voice conventions also contradicted each other. asclepias ADR-0004
(2026-08-15) mandates a *collegial, never instructive* voice because its
readers were assumed to be professional peers; lupinus's `CLAUDE.md`
(2026-08-19) mandates an *instructive, addressed-to-you* voice for a competent
generalist. Two front doors, two voices, for what turned out to be one reader.

## Decision

1. **Lentago Labs is a pro-bono operations practice** for organizations that
   run on volunteers, donations, and one overworked tech person: the nonprofit
   with one tech director, the all-volunteer org with one person who does the
   computers, the single technician covering a whole shop on dirt pay. Help is
   free for those organizations; anyone else asks. Everything published here
   is free to take and use.

2. **The estate is the demonstration.** The homelab cluster and the AWS
   platform are run exactly the way the practice would tell a client to run
   theirs, in the open, so the method can be watched working before it is
   trusted. The recurring phrase for this is **"practice what we publish."**
   The word "dogfooding" is not used on any Lentago Labs surface.

3. **One reader, one voice.** All reader-facing documentation, guides, labs,
   onboarding, and adoption material is written for that one reader, in the
   voice specified in [`docs/voice.md`](../voice.md): conversational,
   instructive, friendly, jargon defined inline, every procedure opening with
   what/why/how-long and closing with how you know it worked. The
   learning-lab premise of asclepias ADR-0004 is superseded; its mechanics
   (evidence links, honest access statements, historical records untouched)
   stay. The two-audience premise in lupinus ADR-0001's alternatives section
   is superseded; its hub-and-spoke decision stays. Each repo records that in
   its own ADR.

4. **asclepias and lupinus stay two repos, recast as two volumes of one
   guide**: Vol. 1 *how it works, try it on ours* (asclepias) and Vol. 2
   *make it yours* (lupinus), cross-linked, same voice.

5. **The org-membership on-ramp is retired.** Labs are fork-first; nobody
   needs an invite. The org base repository permission returns from `write`
   (set 2026-08-27 for the colleague plan) to `none`. The roster becomes a
   guestbook of people who have run Lab 01 and remains that lab's target.

6. **Historical records are untouched.** ADRs that cite the learning lab as
   context (solidago 0002/0005, drosera 0002, osmunda 0001, asclepias
   0001–0004, this repo's 0003), the incident register and reports, fleet
   reports, and merged PR titles keep the vocabulary of their time, consistent
   with [ADR-0005](0005-incident-register-publishes-verbatim.md). New ADRs
   supersede; old ones stay.

7. **The voice guide lives in this repo** at `docs/voice.md`, referenced from
   each guide repo's `CLAUDE.md`. One file, no mirrors to keep in sync.

## Live settings changed under this decision

Two org-level settings are not Terraform-managed (the `terraform/` module owns
repositories, not the organization record) and were changed by hand on
2026-09-30, recorded here as the change record:

| Setting | Before | After |
|---|---|---|
| Org base repository permission | `write` | `none` |
| Org description | "Infrastructure operations — bare metal through cloud-native. Build it, break it, operate it." | "Free ops help for the nonprofit with one tech person. We practice what we publish." |

## Alternatives

- **Keep both positionings side by side.** Rejected. The lab framing was
  written for an audience that did not materialize, and every page that
  carries it addresses the wrong reader.
- **Merge asclepias into lupinus.** Rejected for this pass. It is a
  rename-tier operation (fleet settings-as-code, DeepWiki index, brand assets,
  ADR trail, inbound links) and is not needed to fix the audience problem.
  Two volumes under one voice gets the same result.
- **Keep the org-membership on-ramp for future contributors.** Rejected.
  Fork-first works for everyone today, and a `write` base grant with no members
  using it is surface area with no purpose.
- **Rewrite the historical ADRs in the new vocabulary.** Rejected, for the
  reasons ADR-0005 and asclepias ADR-0004 already give.

## Consequences

- `docs/voice.md` is the canon; every repositioning PR across the fleet is
  reviewed against it, and bullpen jobs that touch reader-facing prose carry it
  in the prompt.
- The canonical README footer and the canonical `🛠️ Make a change yourself`
  opener are defined in `docs/voice.md` and swapped into every fleet README.
- lentago.dev states plainly that help is free for mission-driven
  organizations. Availability and response-time copy stays; free does not mean
  unlimited.
- asclepias's labs are re-audited for the fork-first access model, per the
  re-audit rule its ADR-0003 already carries.
- [#90](https://github.com/lentago/.github/issues/90) (the engagement ladder
  for new members) is closed as overtaken by events; the ladder itself
  survives, fork-first, in asclepias.
