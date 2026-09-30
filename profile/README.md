<div align="center">

![Lentago Labs — Production that shows up when the need does.](./assets/banner.svg)

**Lentago Labs is a pro-bono operations practice for the organizations nobody builds tools for** — the nonprofit with one tech director, the all-volunteer org with one person who does the computers, the single technician covering a whole shop alone.

We help you own your systems outright: the same free tiers you already use, but in your accounts, as code you can fork, run by people we've shown how. Everything here is free to take and use. Call when you need to, if you need to.

<sub>What you're looking at is our own estate — a Proxmox homelab cluster and a production-grade AWS platform — run exactly the way we'd tell you to run yours: everything as code, every change a pull request, in the open. We publish it because a method you can watch working is worth more than one you're asked to trust. <b>We practice what we publish.</b></sub>

<br/>

**The practice** &nbsp;·&nbsp; Free help for mission-driven orgs. Own your systems. Exit-ready by construction.<br/>
**The estate** &nbsp;·&nbsp; Real systems, survivable stakes, receipts in git.<br/>
<sub>Modern operations, sized for organizations that run on volunteers and donations. The emphatic free-tier discipline is deliberate operating practice for exactly those constraints — not thrift.</sub>

<br/>

<a href="https://deepwiki.com/lentago"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki" height="32"></a>

</div>

> **The pledge** — We will never host your systems for you. You'll own every piece, we'll show your people how to run it, and firing us is a runbook.

> [DeepWiki](https://deepwiki.com/lentago) maintains an AI-generated wiki over every public Lentago Labs repo — architecture pages, diagrams, and a Q&A box grounded in the actual code. It's the fastest way to orient before reading source. It is AI-generated: trust it to orient you, verify against the code before you act on it.

> **Heard the enterprise words but never seen them done small?** The [asclepias glossary](https://github.com/lentago/asclepias/blob/main/manual/glossary.md) translates CAB, CMDB, PIR and the rest into what we actually do here — and what you can do too.

### 🔁 &nbsp; How everything moves

Everything is code. Every change is a pull request. Merges apply automatically. A self-hosted Claude agent fleet does directed work. **Humans own every merge.** That is the whole operating model — nothing here changes except through a reviewed PR, and the merged PR *is* the change record.

### ⚡ &nbsp; Every merge changes something real

<sub>This is not a sandbox of toy YAML. Merge a PR in one of these repos and a live surface moves:</sub>

| Merge here… | …and it moves |
| :-- | :-- |
| [**drosera**](https://github.com/lentago/drosera) | your Grafana Cloud dashboards and alerts |
| [**kalmia**](https://github.com/lentago/kalmia) | every Proxmox VM and LXC in the homelab |
| [**claytonia**](https://github.com/lentago/claytonia) | the agent runner pool itself |
| [**osmunda**](https://github.com/lentago/osmunda) | the k3s cluster's workloads — Flux pulls the merge |
| [**solidago**](https://github.com/lentago/solidago) | the AWS platform |
| site repos | the live sites |
| [**.github**](https://github.com/lentago/.github) | every repo's rulesets, required checks, and labels, via `terraform/` |

### 🧰 &nbsp; What the estate is built on

<sub><b>Emphatically free-tier, wherever possible.</b> When a service offers a free tier, that's the one we run — caps and retention windows are treated as real operating constraints to be managed, not something to buy past.</sub>

<sub>Cloud & containers</sub><br/>
![AWS](https://img.shields.io/badge/AWS-1b4b2e?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0iI0UwQTgxQyIgZD0iTTE4LjcgMTAuMmE2LjYgNi42IDAgMCAwLTEyLjktMS4yQTUuMSA1LjEgMCAwIDAgNi4xIDE5aDExLjZhNC42IDQuNiAwIDAgMCAxLTguOHoiLz48L3N2Zz4K)
![ECS Fargate](https://img.shields.io/badge/ECS%20Fargate-1b4b2e?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0iI0UwQTgxQyIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMTIgMS41IDIxLjUgN3YxMEwxMiAyMi41IDIuNSAxN1Y3TDEyIDEuNXptMCAyLjNMNC41IDguMnY3LjZsNy41IDQuNCA3LjUtNC40VjguMkwxMiAzLjh6Ii8%2BPHBhdGggZmlsbD0iI0UwQTgxQyIgZD0iTTguNSA5LjVoN3Y3aC03eiIvPjwvc3ZnPgo%3D)
![Docker](https://img.shields.io/badge/Docker-1b4b2e?style=flat-square&logo=docker&logoColor=E0A81C)

<sub>Bare metal & virtualization</sub><br/>
![Proxmox](https://img.shields.io/badge/Proxmox-1b4b2e?style=flat-square&logo=proxmox&logoColor=E0A81C)
![Linux](https://img.shields.io/badge/Linux-1b4b2e?style=flat-square&logo=linux&logoColor=E0A81C)

<sub>Infrastructure as code</sub><br/>
![Terraform](https://img.shields.io/badge/Terraform-1b4b2e?style=flat-square&logo=terraform&logoColor=E0A81C)
![Ansible](https://img.shields.io/badge/Ansible-1b4b2e?style=flat-square&logo=ansible&logoColor=E0A81C)

<sub>CI/CD & supply chain</sub><br/>
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-1b4b2e?style=flat-square&logo=githubactions&logoColor=E0A81C)
![OIDC](https://img.shields.io/badge/OIDC-E0A81C?style=flat-square&logoColor=white)

<sub>Observability & on-call</sub><br/>
![Grafana](https://img.shields.io/badge/Grafana-1b4b2e?style=flat-square&logo=grafana&logoColor=E0A81C)
![Prometheus](https://img.shields.io/badge/Prometheus-1b4b2e?style=flat-square&logo=prometheus&logoColor=E0A81C)
![CloudWatch](https://img.shields.io/badge/CloudWatch-1b4b2e?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPGcgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjRTBBODFDIiBzdHJva2Utd2lkdGg9IjIiPjxjaXJjbGUgY3g9IjEwLjUiIGN5PSIxMC41IiByPSI2LjciLz48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIGQ9Im0xNS42IDE1LjYgNSA1Ii8%2BPHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNNi44IDEwLjVoMS45bDEuMi0yLjYgMS43IDUgMS4yLTIuNGgxLjUiLz48L2c%2BPC9zdmc%2BCg%3D%3D)

### 🌿 &nbsp; The suite

<sub>Each system splits a platform-agnostic core from per-source clients — the current build is always <i>the first client</i>, a working reference rather than a finished product.</sub>

<table>
<tr>
<td><img src="./assets/marks/solidago-mark-square.svg" width="22" height="22" align="absmiddle" alt="" />&nbsp; <a href="https://github.com/lentago/solidago"><b>solidago</b></a><br/><sub><a href="https://deepwiki.com/lentago/solidago">DeepWiki&nbsp;↗</a></sub></td>
<td>Reference three-tier AWS platform — 100% Terraform: VPC, ECS Fargate, RDS, WAF.</td>
</tr>
<tr>
<td><img src="./assets/marks/lentago-mark-square.svg" width="22" height="22" align="absmiddle" alt="" />&nbsp; <a href="https://github.com/lentago/osmunda"><b>osmunda</b></a><br/><sub><a href="https://deepwiki.com/lentago/osmunda">DeepWiki&nbsp;↗</a></sub></td>
<td>Kubernetes platform — standing k3s on homelab guests, an ephemeral EKS overlay, Flux GitOps throughout.</td>
</tr>
<tr>
<td><img src="./assets/marks/drosera-mark-square.svg" width="22" height="22" align="absmiddle" alt="" />&nbsp; <a href="https://github.com/lentago/drosera"><b>drosera</b></a><br/><sub><a href="https://deepwiki.com/lentago/drosera">DeepWiki&nbsp;↗</a></sub></td>
<td>Git-driven observability into Grafana Cloud — one Alloy container, Terraform-provisioned dashboards.</td>
</tr>
<tr>
<td><img src="./assets/marks/kalmia-mark-square.svg" width="22" height="22" align="absmiddle" alt="" />&nbsp; <a href="https://github.com/lentago/kalmia"><b>kalmia</b></a><br/><sub><a href="https://deepwiki.com/lentago/kalmia">DeepWiki&nbsp;↗</a></sub></td>
<td>Idempotent provisioning for workstations, VMs, and containers.</td>
</tr>
<tr>
<td><img src="./assets/marks/claytonia-mark-square.svg" width="22" height="22" align="absmiddle" alt="" />&nbsp; <a href="https://github.com/lentago/claytonia"><b>claytonia</b></a><br/><sub><a href="https://deepwiki.com/lentago/claytonia">DeepWiki&nbsp;↗</a></sub></td>
<td>Self-hosted agent fleet — drop a job, get a reviewed PR back.</td>
</tr>
<tr>
<td><img src="./assets/marks/betula-mark-square.svg" width="22" height="22" align="absmiddle" alt="" />&nbsp; <a href="https://github.com/lentago/betula"><b>betula</b></a><br/><sub><a href="https://deepwiki.com/lentago/betula">DeepWiki&nbsp;↗</a></sub></td>
<td>Full-volume log capture &amp; archive → Axiom, at zero query cost.</td>
</tr>
<tr>
<td><img src="./assets/marks/lentago-mark-square.svg" width="22" height="22" align="absmiddle" alt="" />&nbsp; <a href="https://github.com/lentago/monarda"><b>monarda</b></a><br/><sub><a href="https://deepwiki.com/lentago/monarda">DeepWiki&nbsp;↗</a></sub></td>
<td>Campaign-site kit — an Astro template, intake, and a timed dry-run, deploying to the client's own GitHub Pages or S3.</td>
</tr>
<tr>
<td><img src="./assets/marks/lentago-mark-square.svg" width="22" height="22" align="absmiddle" alt="" />&nbsp; <a href="https://github.com/lentago/mitchella"><b>mitchella</b></a><br/><sub><a href="https://deepwiki.com/lentago/mitchella">DeepWiki&nbsp;↗</a></sub></td>
<td>Estate front desk — a chat assistant that checks live state before answering from the docs, and drafts a ticket for a human when it can't.</td>
</tr>
<tr>
<td><img src="./assets/marks/lentago-mark-square.svg" width="22" height="22" align="absmiddle" alt="" />&nbsp; <a href="https://github.com/lentago/asclepias"><b>asclepias</b></a><br/><sub><a href="https://deepwiki.com/lentago/asclepias">DeepWiki&nbsp;↗</a></sub></td>
<td>The guide, vol. 1 — how it all works, with labs you can run against our estate before building your own.</td>
</tr>
<tr>
<td><img src="./assets/marks/lentago-mark-square.svg" width="22" height="22" align="absmiddle" alt="" />&nbsp; <a href="https://github.com/lentago/lupinus"><b>lupinus</b></a><br/><sub><a href="https://deepwiki.com/lentago/lupinus">DeepWiki&nbsp;↗</a></sub></td>
<td>The guide, vol. 2 — pick a product, stand it up in your own accounts, and run it from an ops vault you own.</td>
</tr>
</table>

<sub>📖 &nbsp;Every public repo is indexed on <a href="https://deepwiki.com/lentago"><b>DeepWiki</b></a> — browse the wikis or ask the codebases anything.</sub>

### 🧭 &nbsp; Start here

Three doors, depending on what you came for.

**You run a nonprofit's tech and want something you can use today**

1. [**The picker**](https://github.com/lentago/lupinus/blob/main/guide/picker.md) — start from what you need, not from what we built. Every row says what it costs and how ready it is.
2. [**Your first kit**](https://github.com/lentago/lupinus/blob/main/guide/first-kit.md) — a fundraising site in about an hour, deployed into *your* GitHub account, for free.
3. **The pledge** (above) — you own every piece, we show your people how, firing us is a runbook.
4. Stuck? **chris@lentago.dev**. No invoice.

**You want to see it working before you trust it**

1. Pick a product repo above and read its **🛠️ Make a change yourself** section. Every vector links to a real merged PR.
2. Ask that repo's **DeepWiki** a question about how it works, then check the answer against the source.
3. Run a [lab](https://github.com/lentago/asclepias/tree/main/labs) against our estate — they start with a browser and a question and ladder up to breaking something on purpose. A free GitHub account is all you need.
4. Mention `@claude` on any issue or PR and watch the agent fleet respond.

**You want to kick the tires on us**

1. [**solidago**](https://github.com/lentago/solidago) — the reference AWS platform, 100% Terraform.
2. [**claytonia**](https://github.com/lentago/claytonia) — the self-hosted agent fleet that does the directed work, and never merges.
3. [**Incident register**](https://github.com/lentago/.github/blob/main/fleet-reports/incidents.md) — our post-mortems, published verbatim, including the embarrassing ones.
4. [**Lock-in ledger**](https://github.com/lentago/.github/blob/main/fleet-reports/lock-in-ledger.md) — every vendor we depend on, scored on how hard it would be to leave. The receipt behind *"firing us is a runbook."*

### 📊 &nbsp; Fleet in numbers

<sub>Regenerated weekly from the repos themselves — we practice what we publish.</sub>

- **[Fleet report](https://github.com/lentago/.github/blob/main/fleet-reports/fleet-report.md)** — open issues by repo, a 30-day activity snapshot, and a code census that counts the `CLAUDE.md`-family instruction files as natural-language code.
- **[Language census](https://github.com/lentago/.github/blob/main/metrics/language-census.md)** — the canonical all-languages breakdown.
- **[Incident register](https://github.com/lentago/.github/blob/main/fleet-reports/incidents.md)** — post-mortems from running our own estate, with what broke, what did *not*, and the governance lessons.
- **[Lock-in ledger](https://github.com/lentago/.github/blob/main/fleet-reports/lock-in-ledger.md)** — our own vendor dependencies, each scored on export fidelity, format openness, custody, and a documented exit. The receipt behind *"firing us is a runbook."*

<div align="center">
<sub><b>chris@lentago.dev</b> &nbsp;·&nbsp; New England, US</sub>
</div>
