# ADR-0011: How the fleet handles secrets

**Status:** Accepted (2026-10-07)

## Context

Until this record the fleet had no single statement of how it handles secrets
(credentials, tokens, private keys). The practice was largely consistent, but
it lived in a dozen places:

- **Workload identity instead of stored keys.** The Terraform pipelines and site
  deploys reach AWS through GitHub OIDC, with no stored AWS keys
  ([solidago ADR-0002](https://github.com/lentago/solidago/blob/50f89767e77d264823ccbae4b0661b020cf46fb0/docs/decisions/0002-github-oidc-only-dual-role-trust-split.md),
  [kalmia ADR-0004](https://github.com/lentago/kalmia/blob/103f953b03934fcbe2d6a7209f7980587bc7bbea/docs/adr/0004-lan-apply-on-merge.md#L55-L58)).
  The bullpen authenticates as the `lentago-claude-runner` GitHub App, whose
  installation tokens are short-lived and never written to disk
  ([claytonia ADR-0004](https://github.com/lentago/claytonia/blob/51a7ce947f72040d3ba17caa3ffed2a658d905c1/docs/adr/0004-github-app-identity-scoped-tokens.md)).
- **Slots in Terraform, values set by hand.** solidago creates its Secrets
  Manager entries holding the literal `PLACEHOLDER-set-out-of-band`, with
  `ignore_changes` on the value
  ([`modules/secrets/main.tf`](https://github.com/lentago/solidago/blob/50f89767e77d264823ccbae4b0661b020cf46fb0/modules/secrets/main.tf#L92-L100)).
  The uvularia demo sandbox does not create its SSM parameter at all, "so it
  never lands in Terraform state or a repo"
  ([README](https://github.com/lentago/solidago/blob/50f89767e77d264823ccbae4b0661b020cf46fb0/modules/uvularia-demo-sandbox/README.md#L70-L90)).
- **Bootstrap credentials outside the config they drive.** kalmia's
  `terraform@pve` identity and betula's Axiom token are deliberately not managed
  by the Terraform that authenticates with them, so a bad apply cannot lock the
  pipeline out
  ([kalmia ADR-0004](https://github.com/lentago/kalmia/blob/103f953b03934fcbe2d6a7209f7980587bc7bbea/docs/adr/0004-lan-apply-on-merge.md#L49-L53),
  [betula `terraform/README.md`](https://github.com/lentago/betula/blob/bdac96e1be58041ad5adb361e9d33473dfcd99ce/terraform/README.md#L26-L32)).
- **Host-local files for on-host agents.** For example `/etc/default/alloy` at
  mode 0600
  ([drosera `scripts/deploy-alloy.sh`](https://github.com/lentago/drosera/blob/4d6f75d6c7606288822d00cfcbdac9f9f5d0759f/scripts/deploy-alloy.sh#L252-L269))
  and the bullpen's `/etc/claude-runner/`
  ([claytonia `provision/README.md`](https://github.com/lentago/claytonia/blob/51a7ce947f72040d3ba17caa3ffed2a658d905c1/provision/README.md#L37-L41)).
- **Example files in git, real files ignored.** This is the convention lupinus
  gives every adopter
  ([`guide/conventions.md`](https://github.com/lentago/lupinus/blob/93526fe98ad17dc4844a7eea1ac7c7f08dea29e7/guide/conventions.md#L43-L54)).
- **One line in this repo's [`CONTRIBUTING.md`](../../CONTRIBUTING.md):** "No
  secrets, ever."

None of it said which stores are approved, what Terraform may hold, what
detection runs, or what happens on a leak. Two gaps were concrete:

- **Detection.** GitHub secret scanning and push protection were disabled on
  all 27 fleet repos. Every one of them is public, where both features are free.
  The only scan was CodeRabbit's gitleaks run
  ([`.coderabbit.yaml`](https://github.com/lentago/coderabbit/blob/9de26bf68d9f2d8c684cb06fe876f139e7ceaeb6/.coderabbit.yaml#L129-L130)),
  which is never a gate.
- **Verification.** Two incidents in the register turn on credential handling.
  In the
  [2026-07-08 placeholder-credential incident](../../fleet-reports/incidents/2026-07-08-ecs-axiom-placeholder-credential.md),
  ECS logs were dark for 16 days because a secret still held its placeholder.
  In the
  [2026-07-13 fleet-reports bring-up](../../fleet-reports/incidents/2026-07-13-fleet-reports-automation-bringup.md),
  a truncated token was diagnosed as a permissions problem, and a privilege grant
  added on that wrong theory was never removed. Both reports recorded lessons,
  and only some of them were adopted.

Since [ADR-0008](0008-pro-bono-practice-one-reader.md) the estate is the
demonstration. The practice gives adopters a secrets convention, so its own
rules belong in one place, stated as plainly.

## Decision

The fleet handles secrets by the nine rules below. Rules 1–6 record practice
that already holds; rules 7–9 are adopted now. Every fleet repo follows them. A
repo that needs an exception records it in its own ADR and links here.

1. **Identity before secrets.** Where a platform offers workload identity, use
   it instead of a stored credential. For AWS that means GitHub OIDC, with one
   role per repo scoped to that repo's own state key. For automation that acts on
   GitHub it means a GitHub App with short-lived installation tokens. A new
   long-lived credential needs a reason identity cannot serve.

2. **Least scope, and widened grants are reverted.** Each credential is scoped
   to one job. Examples: ingest-only Axiom tokens
   ([betula `clients/aws/README.md`](https://github.com/lentago/betula/blob/bdac96e1be58041ad5adb361e9d33473dfcd99ce/clients/aws/README.md#L25)),
   `logs:write`-only Grafana tokens
   ([drosera `clients/README.md`](https://github.com/lentago/drosera/blob/4d6f75d6c7606288822d00cfcbdac9f9f5d0759f/clients/README.md#L31)),
   RBAC-trimmed Proxmox tokens, and fine-grained PATs limited to the repos they
   serve. A grant widened while debugging is reverted when the debugging ends. On
   a credential-shaped failure the first move is to measure the secret (its
   length, an authenticated probe), not to widen it.

3. **Values live only in an approved store.**

   | Store | Holds | Examples |
   | :-- | :-- | :-- |
   | GitHub Actions secrets | Credentials a workflow needs | `FLEET_ADMIN_TOKEN`, `PROXMOX_VE_API_TOKEN`, `AXIOM_TF_API_TOKEN`, `CLAUDE_CODE_OAUTH_TOKEN` |
   | AWS Secrets Manager (KMS) or SSM SecureString | Runtime credentials for AWS workloads, with IAM read scoped to the specific ARN | The ECS FireLens Axiom header, the uvularia demo's Anthropic key |
   | Host-local file, mode 0600 or 0640, owned by the service or operator that reads it, outside any checkout | Credentials for an agent on a host the fleet runs | `/etc/default/alloy`, `/etc/claude-runner/`, the Firewalla's `log_shipping.env`, `~/.config/kalmia/proxmox.env` |
   | Terraform state | Only the values rule 4 allows | — |

   Values go nowhere else. Not:

   - git, in any repo, branch or history, public or private;
   - issue, PR or commit text;
   - CI logs;
   - incident reports ([ADR-0005](0005-incident-register-publishes-verbatim.md));
   - `pub.lan`, Drive, or chat.

4. **Terraform holds slots, not values.**

   - Terraform may create a secret's slot and grant read on it. The value is set
     out of band: either `ignore_changes` covers it, or Terraform never creates
     the slot at all.
   - If a value is issued outside Terraform and its consumer can read the store
     at runtime, the value does not pass through Terraform: no `TF_VAR` and no
     data-source read.
   - Where Terraform is itself the issuer, or the only delivery path (a Grafana
     data source's credential, for example), the value does land in state. That
     is why state is treated as a store: it sits in the shared S3 backend with
     `encrypt = true`, is reached only through each repo's OIDC role, and is
     never committed. Plan files are never committed either.
   - The credential Terraform authenticates with stays outside the config it
     drives.

5. **"Set out of band" is unfinished until verified.** A change that creates or
   recreates a slot carries a check that the real value landed and works.
   Secret-backed Terraform variables carry a non-empty `validation`
   ([drosera `terraform/README.md`](https://github.com/lentago/drosera/blob/4d6f75d6c7606288822d00cfcbdac9f9f5d0759f/terraform/README.md#L86-L104)).
   Placeholder-shaped values (`PLACEHOLDER*`, `<…>`, empty) are rejected wherever
   the tooling allows.

6. **Example files in git, real files ignored.** Every product that takes
   configuration ships a committed `*.example` naming each value and where to get
   it. The real file is gitignored. It is the same convention lupinus gives
   adopters.

7. **Detection is on everywhere.** Secret scanning and push protection are
   enabled on every fleet repo, declared in
   [`terraform/repos.tf`](../../terraform/repos.tf)
   ([#240](https://github.com/lentago/.github/issues/240)). A repo born from
   `fleet-ops/repos.json` gets both at creation. Push protection is bypassed only
   for a confirmed false positive, with the reason given. CodeRabbit's gitleaks
   run stays as an advisory second look.

8. **A leak is rotated, not scrubbed.** A value that reaches a public surface (a
   push, a log, a rendered artifact) is exposed the moment it lands, however
   fast it is removed.

   - Revoke or rotate it at the issuer first, then remove it from the tip.
   - Rewriting history is optional and never a substitute for rotation.
   - If the value reached a public surface, the leak gets an incident report. The
     value itself never appears in the report.
   - Outside reports arrive through [`SECURITY.md`](../../SECURITY.md).

9. **A new kind of store amends this record.** Adopting a store not listed in
   rule 3 means amending this record before it ships, so the table stays the
   complete list. Examples: SOPS or Sealed Secrets ciphertext in git, an external
   password manager as a source of truth, or an operator that syncs from one.

## Where the fleet stands (2026-10-07)

Gaps against the rules, each with its tracking issue:

| Gap | Rule | Tracking |
| :-- | :-: | :-- |
| Secret scanning and push protection disabled on all 27 repos | 7 | [#240](https://github.com/lentago/.github/issues/240) |
| solidago's ALB shipper reads its Axiom token through a Terraform data source, and the Ask Lambda takes its Anthropic key as a Terraform variable. Both values land in state and in the function's environment ([`alb-log-shipper/main.tf`](https://github.com/lentago/solidago/blob/50f89767e77d264823ccbae4b0661b020cf46fb0/modules/alb-log-shipper/main.tf#L64-L66), [`ask-lambda/main.tf`](https://github.com/lentago/solidago/blob/50f89767e77d264823ccbae4b0661b020cf46fb0/modules/ask-lambda/main.tf#L18-L22)) | 4 | [solidago#149](https://github.com/lentago/solidago/issues/149) |
| solidago's Axiom secrets are created holding `PLACEHOLDER-set-out-of-band`, and no check confirms the real value replaced it | 5 | [solidago#213](https://github.com/lentago/solidago/issues/213) |
| `FLEET_REPORTS_TOKEN` keeps the org-admin grant from 2026-07-13, and the workstation's cross-repo PAT is classic and account-wide | 2 | [#242](https://github.com/lentago/.github/issues/242) |
| No register of fleet credentials, their scopes or their expiry dates; rotation is described per secret, when at all | 2, 5 | [#243](https://github.com/lentago/.github/issues/243) |
| osmunda has no way to deliver a Kubernetes Secret through Flux, and n8n's cutover needs one ([`apps/n8n/README.md`](https://github.com/lentago/osmunda/blob/f576fc5637692406c93eb016fa2fa74e7a639f6b/apps/n8n/README.md#L19-L23)) | 3, 9 | [osmunda#12](https://github.com/lentago/osmunda/issues/12) |
| Axiom ingest and query tokens are issued by hand, outside Terraform. Moving issuance into Terraform puts the values in state, which rule 4 allows | 4 | [betula#119](https://github.com/lentago/betula/issues/119) |

## Consequences

- **This record is canonical.** The per-repo `CLAUDE.md` lines that restate a
  secrets rule (claytonia, kalmia, drosera) stay as local reminders; where they
  differ from this record, this record wins.
- **Alerts from the first scan.** After #240 applies, GitHub scans each repo's
  full history, and any alert it raises is handled by rule 8.
- **New Lambdas fetch at runtime from the start.** The solidago Lambda pattern is
  a known exception to rule 4 until solidago#149 lands.
- **osmunda#12's choice may come back here.** If it picks SOPS or Sealed
  Secrets, rule 3 needs an amendment first. External Secrets reading from
  Secrets Manager needs none.
- **The adopter-facing form stays in lupinus.** Its conventions page is what
  adopters read; this record is the practice's own. Where the two disagree, fix
  the guide.
- **Cost.** No money: scanning is free on public repos. Two new obligations:
  rule 5's verification step on any change that creates a slot, and a reason for
  every push-protection bypass.

## Alternatives

Weighed when this record was written:

- **Leave the rules distributed.** Rejected. The gaps above existed because
  nothing stated the baseline. Scanning was off for the fleet's whole life, and
  no document said it should be on.
- **One secrets manager for everything** (a password manager with CLI
  injection, or Vault). Rejected for now. It adds a paid or self-hosted
  dependency for a single operator. GitHub secrets, the AWS stores and host files
  are each native to where their values are consumed, and the credential
  register (#243) gives the single view without centralising storage.
- **A CI secret scanner as a required check instead of GitHub's native
  scanning.** Rejected for now. Push protection blocks a secret at push time,
  before it is public. A PR check runs after the push has already published the
  value. Native scanning also covers full history with no workflow to maintain.
  A CI scanner can be added later as a second layer if a gap shows. The obvious
  candidate gap is non-provider patterns, which the pinned provider cannot
  declare.
