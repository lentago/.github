# The Lentago Labs voice

How every reader-facing page in the fleet is written. This is the canon that
[ADR-0008](adr/0008-pro-bono-practice-one-reader.md) points at. Guides, labs,
onboarding, adoption runbooks, READMEs, the org profile, and lentago.dev all
follow it. If you are writing prose someone outside the fleet will read, read
this first.

## Who we are, in one line

> Lentago Labs is a pro-bono operations practice for organizations that run on
> volunteers, donations, and one overworked tech person. Everything here is
> free to take. We practice what we publish.

## Who you are writing for

One reader. Write every page to them.

> **The one tech person.** A nonprofit's tech director, or the volunteer who
> "does the computers," or a single paid technician covering an entire org
> alone. A competent generalist, not a site-reliability engineer. No time,
> no budget, no backup. Wants to own what they run and stop renting it. Will
> read your page once, at 9 pm, while something is broken.

Not a peer colleague, not a trainee, not a hiring manager. If a sentence only
makes sense to someone who already works in a platform team, rewrite it.

## The voice

Think *DIY-SaaS for Dummies, first edition*: friendly, plain, relentlessly
practical, and never talking down.

### Do

- **Second person, present tense, conversational.** Contractions are fine.
  Short sentences. Say it the way you would say it in the room.
- **Open every guide page with three things:** what you're about to do, why
  bother, and how long it takes. **Close every procedure with:** how you know
  it worked.
- **Define every term of art the first time it appears, in the sentence.** Not
  in a glossary the reader has to go find. *"A pull request, which is a
  proposed change someone else reviews before it lands."*
- **Name the trap before the step.** Use a **Heads up** callout. Give
  permission to skip with **Skip this if…**
- **Be honest about cost, time, and what's unfinished, in plain words.** A
  receipt that says two hours and forty minutes beats "takes an afternoon."
  Tier labels, swap lists, and unexercised markers stay exactly as they are.
- **Point at where it's live.** Every claim about the fleet links to the repo,
  file, or PR that proves it. That rule predates this guide and survives it.

### Don't

- **Don't be cute for its own sake, and never condescend.** Friendly is not
  the same as chummy. No emoji soup. No exclamation points doing work a
  sentence should do.
- **Don't hedge.** If we don't know, say we don't know.
- **Don't cast the reader as a student.** No "training," "curriculum," "prove
  you can," "what you just practiced." Those words position us as the teacher
  and them as the pupil. We're the neighbor who's done this before.
- **Don't say "dogfooding."** Ever. The phrase is *practice what we publish*.
- **Don't reintroduce the retired framing.** See the word list below.

### Where the voice does not apply

Not everything gets this register, and that is deliberate:

- **ADRs, incident reports, fleet reports** keep their neutral, factual voice.
  They are records.
- **PR bodies** follow the fleet PR-workflow rule (neutral, objective,
  professional). Unchanged.
- **Code comments, Terraform, workflow YAML** stay terse and technical.
- **Evidence tables** in READMEs (the `🧭 What this repo demonstrates` rows)
  stay terse. The prose around them gets the voice; the rows do not.

## The two halves of the estate

The estate is everything we run. It has two halves, and every page says which
one it means: **on-prem**, the machines in our own building (a Proxmox cluster,
a NAS, the network gear), and **the cloud**, a real AWS environment in our own
account, as code. *On-prem* is the word the reader already hears from every
vendor, so it is the one we use; define it the first time it appears on a page.
In identifiers (labels, dashboard titles, DNS) the token is `onprem`. Decided
2026-10-14 ([#269](https://github.com/lentago/.github/issues/269)); the words
it retires are in the table below.

## Word swaps

| Retire | Use instead |
|---|---|
| the lab, the learning lab, the team learning lab | our shop, our own estate, the fleet; **on-prem** when "the lab" meant the hardware |
| the homelab, home lab, the home network, hobbyist | **on-prem**: "the on-prem cluster", "our on-prem estate". Define it on first use: *the machines in your own building* |
| the household (as the wall display's audience) | the room, the lobby screen, whoever's in the room |
| the crew, colleagues, IT-ops colleagues, members, the day job | you, your org, the one tech person |
| trainee, curriculum, training ground, "prove you can" | (rewrite the sentence) |
| dogfooding | practice what we publish |
| "Evaluating the operator" | "Kick the tires" |
| "Book a consult" | "Get in touch" |
| "Access needed: org membership" | "You'll need: a free GitHub account" |

## Canonical blocks

These are copied verbatim into every fleet README. Change them here first, then
swap everywhere.

### README footer

```markdown
> 🌱 **Lentago Labs** is a pro-bono operations practice for organizations that
> run on volunteers, donations, and one overworked tech person. Everything here
> is free to take, and we practice what we publish: our own estate runs this
> way, in the open. Start at the [org profile](https://github.com/lentago).
```


### `🛠️ Make a change yourself` opener

```markdown
These systems are real, and nothing critical rides on them. That makes this a
safe place to try a change before you make the same kind of change in your own
shop. Pick one:
```

### The six promises

The offering, in the words every surface copies ([ADR-0012](adr/0012-six-promises-codenames-are-parts.md)).
Codenames never appear in a headline; they appear in the parts list under their
promise.

```markdown
- **Your site and giving page** — a campaign page you own outright, with a
  donate button that goes straight to your payment processor.
- **Your records and your proof** — minutes, policies, and filings in one vault,
  the posting rules beside them, and a public board that shows what went up on
  time. When the board, the auditor, the funder, or the insurer asks, you send
  a link.
- **Your machines and logins** — every laptop set up the same way, every login
  with a named owner, and leaving is a pull request, a proposed change someone
  else reviews before it lands.
- **Your alarms and status** — know when something breaks before the executive
  director does, and a file that says who gets the call.
- **Your help desk and runbooks** — requests land in a list, answers come from
  runbooks you wrote once, and the front desk answers at 9 pm.
- **Your data and your exit** — every export you'd need to leave a vendor, on a
  schedule, into a repo you own, with a restore you've drilled.

When you need them: **your building** (sensors, and a lobby screen that says
whether you're open), **cloud you own** (a real AWS environment in your account,
as code), **AI with receipts** (agents that open pull requests and never merge).
```

### The pledge (unchanged)

```markdown
> **The pledge** — We will never host your systems for you. You'll own every
> piece, we'll show your people how to run it, and firing us is a runbook.
```

## A worked example

**Before** (a lab's opening, written for a peer colleague):

> **Goal:** feel the fleet's change gate end to end — branch, PR, required
> checks, review, squash merge — on a change that cannot break anything.
> **Access needed:** a GitHub account. Org members can branch in this repo; a
> fork works identically.

**After** (the same lab, written for the one tech person):

> **What you're about to do:** make one tiny change to a file in this repo and
> watch it travel the whole way to live: branch, pull request, automatic
> checks, a human review, merge. It can't break anything. That's the point.
>
> **You'll need:** a free GitHub account. Nothing else.
>
> **Time:** about twenty minutes, most of it waiting for a human to click merge.
>
> **Why bother:** this exact flow is how you'll want changes to happen in your
> own org. Every change reviewed, every change recorded, nobody editing the
> live thing by hand at 9 pm. Doing it once here, where it's free and safe, is
> the fastest way to understand what you're about to set up at home.
>
> > **Heads up.** You'll fork this repo rather than editing it directly. A
> > *fork* is your own copy on GitHub; a *pull request* from it is you saying
> > "here's a change, please take it." That's the whole mechanism, and it's
> > the same one you'll use for everything else here.

Same facts, same honesty about access. Different reader, so a different page.

## Checklist for a PR that touches reader-facing prose

- [ ] Opens with what / why / how long (guide pages) or states plainly what the
      thing is (READMEs).
- [ ] Every term of art defined on first use.
- [ ] No word from the retire column above.
- [ ] Costs, times, and unfinished bits stated plainly.
- [ ] Every fleet claim links to where it is live.
- [ ] Records (ADRs, incidents, reports) left alone.
