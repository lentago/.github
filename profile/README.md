<div align="center">

![Lentago Labs — Production that shows up when the need does.](./assets/banner.svg)

**Lentago Labs is a shared learning lab, run by IT-operations people.**

The estate is real — a Proxmox homelab cluster and a production-grade AWS platform — but the stakes are deliberately non-critical. **Build it, break it, operate it**, entirely through modern operations patterns, out in the open.

<sub>It's a place for the crew — IT-ops colleagues — to explore the estate, exercise the patterns, and carry the automation and agentic ideas back to the day job. Nothing here is claimed to be correct or unique — the patterns are compared against today's industry standards, on adoption and feature usage, to spot the ones that might be useful.</sub>

<br/>

**The lab** &nbsp;·&nbsp; Real systems, survivable stakes, receipts in git.<br/>
**The practice** &nbsp;·&nbsp; Own your systems. Exit-ready by construction.<br/>
<sub>Modern operations, sized for mission-driven organizations.</sub>

<sub>The lab tests patterns in the open on real systems with survivable stakes; the practice puts the ones that earn their keep to work for organizations that run on volunteers and donations. The emphatic free-tier discipline is deliberate operating practice for exactly those constraints — not thrift.</sub>

<br/>

<a href="https://deepwiki.com/lentago"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki" height="32"></a>

</div>

> **The pledge** — We will never host your systems for you. You'll own every piece, we'll teach your people, and firing us is a runbook.

> [DeepWiki](https://deepwiki.com/lentago) maintains an AI-generated wiki over every public Lentago Labs repo — architecture pages, diagrams, and a Q&A box grounded in the actual code. It's the fastest way to orient before reading source. It is AI-generated: trust it to orient you, verify against the code before you act on it.

> **New to how any of this maps to enterprise practice?** The [asclepias glossary](https://github.com/lentago/asclepias/blob/main/manual/glossary.md) translates enterprise practice — CAB, CMDB, PIR and the rest — into what the lab actually does. It's the fastest orientation for either audience.

### 🔁 &nbsp; How everything moves

Everything is code. Every change is a pull request. Merges apply automatically. A self-hosted Claude agent fleet does directed work. **Humans own every merge.** That is the whole operating model — nothing here changes except through a reviewed PR, and the merged PR *is* the change record.

### ⚡ &nbsp; Every merge changes something real

<sub>This is not a sandbox of toy YAML. Merge a PR in one of these repos and a live surface moves:</sub>

| Merge here… | …and it moves |
| :-- | :-- |
| [**drosera**](https://github.com/lentago/drosera) | your Grafana Cloud dashboards and alerts |
| [**kalmia**](https://github.com/lentago/kalmia) | every Proxmox VM and LXC in the homelab |
| [**claytonia**](https://github.com/lentago/claytonia) | the agent runner pool itself |
| [**solidago**](https://github.com/lentago/solidago) | the AWS platform |
| site repos | the live sites |
| [**.github**](https://github.com/lentago/.github) | repo settings and rulesets, via `fleet-ops` |

### 🧰 &nbsp; What the estate is built on

<sub><b>Emphatically free-tier, wherever possible.</b> When a service offers a free tier, that's the one the lab runs — caps and retention windows are treated as real operating constraints to be managed, not something to buy past.</sub>

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
<td><img src="./assets/marks/lentago-mark-square.svg" width="22" height="22" align="absmiddle" alt="" />&nbsp; <a href="https://github.com/lentago/asclepias"><b>asclepias</b></a><br/><sub><a href="https://deepwiki.com/lentago/asclepias">DeepWiki&nbsp;↗</a></sub></td>
<td>The field guide — operations manual, day-one path, hands-on labs.</td>
</tr>
</table>

<sub>📖 &nbsp;Every public repo is indexed on <a href="https://deepwiki.com/lentago"><b>DeepWiki</b></a> — browse the wikis or ask the codebases anything.</sub>

### 🧭 &nbsp; Start here

Three ways in, depending on why you're here.

**Taking part** &nbsp;<sub>(the crew — this is what the lab is for)</sub>

1. Pick a product repo above and read its **🛠️ Make a change yourself** section.
2. Ask that repo's **DeepWiki** a question about how it works.
3. Run a [lab](https://github.com/lentago/asclepias/tree/main/labs) — they ladder from *ask the fleet* up to owning a pattern.
4. Open your first PR — small is fine; the required checks will guide you.
5. Mention `@claude` on any issue or PR and watch the agent fleet respond.

**Evaluating the operator** &nbsp;<sub>(technical)</sub>

1. [**solidago**](https://github.com/lentago/solidago) — the reference AWS platform, 100% Terraform.
2. [**claytonia**](https://github.com/lentago/claytonia) — the self-hosted agent fleet that does the directed work.
3. [**homeassistant-config**](https://github.com/lentago/homeassistant-config) — physical-world monitoring, version-controlled.

Then the [incident register](https://github.com/lentago/.github/blob/main/fleet-reports/incidents.md) for how things break, and the [field-guide glossary](https://github.com/lentago/asclepias/blob/main/manual/glossary.md) to map it all onto enterprise practice.

**Evaluating the practice** &nbsp;<sub>(mission-driven organizations)</sub>

1. **The pledge** (above) — you own every piece, we teach your people, firing us is a runbook.
2. [**site-pondviewlane-com**](https://github.com/lentago/site-pondviewlane-com) — a community organization's public-record fact base with a grounded Ask box.
3. [**homeassistant-config**](https://github.com/lentago/homeassistant-config) — physical-world monitoring on a donated-scale budget.
4. [**Incident register**](https://github.com/lentago/.github/blob/main/fleet-reports/incidents.md) — post-mortems published verbatim.

### 📊 &nbsp; Fleet in numbers

<sub>Regenerated weekly from the repos themselves — we operate in the open.</sub>

- **[Fleet report](https://github.com/lentago/.github/blob/main/fleet-reports/fleet-report.md)** — open issues by repo, a 7-day activity snapshot, and a code census that counts the `CLAUDE.md`-family instruction files as natural-language code.
- **[Language census](https://github.com/lentago/.github/blob/main/metrics/language-census.md)** — the canonical all-languages breakdown.
- **[Incident register](https://github.com/lentago/.github/blob/main/fleet-reports/incidents.md)** — post-mortems from lab operations, with what broke, what did *not*, and the governance lessons.

<div align="center">
<sub><b>chris@lentago.dev</b> &nbsp;·&nbsp; New England, US</sub>
</div>
