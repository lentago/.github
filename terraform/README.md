# Fleet repo settings — Terraform

This layer owns **what the Lentago Labs GitHub org contains and how each repo is
configured**, via the [`integrations/github`](https://registry.terraform.io/providers/integrations/github/latest/docs)
provider. It is the declarative successor to `fleet-ops/fleet-apply.sh`: the same
settings the script swept imperatively, expressed as resources so drift shows up
as a plan rather than as a sweep's console output.

Suite boundary: **kalmia = local infra, solidago = cloud infra, `.github` = the
org itself.** This module manages GitHub, nothing else.

## What it owns

| Surface | Resource | Source of truth |
|---|---|---|
| Repo existence, description, homepage, visibility, template flag | `github_repository` | `../fleet-ops/repos.json` |
| Features (issues/projects/wiki/discussions), branch-update suggestion | `github_repository` | `../fleet-ops/repos.json` |
| Merge-button options — squash-only, auto-merge, delete-branch | `github_repository` | policy in `locals.tf` |
| Topic spine + signature topics | `github_repository` | spine in `locals.tf`, signature in `repos.json` |
| `main` branch ruleset — PR-required, squash-only, no force-push/deletion | `github_repository_ruleset` | `rulesets.tf` |
| Required status checks | `github_repository_ruleset` | `../fleet-ops/required-checks.json` |
| Tidewater issue-label palette | `github_issue_label` | `../fleet-ops/labels.json` |

Terraform reads the **same** `fleet-ops/*.json` the script reads rather than
forking a second copy — one file per concern. `ci/validate.py` shape-checks all
of them and cross-checks that they agree on which repos exist.

### What stays in `fleet-apply.sh`

Two things the script does are not settings and have no resource to hold them:

- **`--prune-branches`** — deleting merged-residue branches is an imperative
  sweep over live branch/PR state, not a declared end state.
- **The boilerplate review-prompt warning** — a content scan of each repo's
  workflow file.

A third is worth keeping deliberately: the script's **read-only check** still
preflights required-check contexts against live check runs. Terraform cannot do
this, and the constraint it guards is the one that deadlocks repos — see
[Required checks](#required-checks--the-one-rule-terraform-cannot-enforce).

## Auth

Two identities, neither of them stored in this tree.

**GitHub** — the provider reads `$GITHUB_TOKEN`. It needs repo administration on
every fleet repo (settings, topics, rulesets, labels) plus permission to create
repositories in the org. Mint a fine-grained PAT scoped to `lentago`, all repos:

| Permission | Level |
|---|---|
| Repository → Administration | Read and write |
| Repository → Metadata | Read |
| Repository → Issues | Read and write |
| Organization → Administration | Read and write (repo creation only) |

Deliberately **not** `delete_repo`. Without it the token physically cannot
delete a repository, which is the outermost rail below.

```bash
export GITHUB_TOKEN='github_pat_…'
```

**AWS** — state lives in solidago's S3 backend. Local runs authenticate as the
`cpitzi-iac` IAM user; the usual `aws sts get-caller-identity` should report
account `365184644049`.

## Phases

Adoption follows kalmia's precedent: prove the model against live state before
handing it a trigger.

**Phase 1 — operator-applied (current).** CI runs `fmt` + `validate` only. Plan
and apply are run locally by the operator. There is no OIDC role and no admin
token in Actions, so a merge here changes nothing on its own.

**Phase 2 — apply-on-merge (tracked, not yet done).** Needs, in order:

1. A `dotgithub-github-actions-terraform` OIDC role in solidago — S3 r/w on the
   `dotgithub/terraform.tfstate` key plus the lock table, nothing else.
2. The admin PAT as the repo secret `FLEET_ADMIN_TOKEN`.
3. `plan`-on-PR and `apply`-on-merge jobs added to
   `../.github/workflows/terraform.yml`.
4. `"gate"` added to this repo's entry in `required-checks.json`, so a red plan
   blocks the merge. The `gate` job already exists and reports on every PR
   precisely so this step is one line.

Until step 4, this repo's own CI cannot block a bad plan — which is the reason
applies stay manual through phase 1 rather than being wired up half-way.

## Rails

This module can create and configure repositories, so it is the highest
blast-radius code in the fleet. Four independent guards, outermost first:

1. **The token has no `delete_repo`.** A destroy that somehow reached the API
   would fail at GitHub.
2. **`archive_on_destroy = true`.** If the resource is destroyed, the repository
   is archived, not deleted.
3. **`prevent_destroy = true` on every repository.** Terraform refuses to *plan*
   a destroy. Deleting an entry from `repos.json` therefore errors — loudly,
   before anything happens — instead of proposing to remove a live repo.
4. **Required checks gate the merge (phase 2).** A plan that fails blocks the
   PR rather than landing and applying.

Rail 3 is the one you will actually meet, and it is deliberate friction: see
[Retiring a repo](#retiring-a-repo).

## Runbook

### Adding a repo to the fleet

Add an entry to `../fleet-ops/repos.json`, then the two files `ci/validate.py`
will insist on:

```jsonc
"new-repo": {
  "description": "…",            // the GitHub About blurb
  "homepage": null,
  "visibility": "public",
  "template": false,
  "template_source": { "owner": "lentago", "repository": "repo-template" },
  "features": { "issues": true, "projects": true, "wiki": false, "discussions": false },
  "suggest_branch_update": false,
  "topics": ["…"],               // signature topics only — the spine is added for you
  "model_labels": []
}
```

- `../fleet-ops/required-checks.json` — required contexts. Mandatory for a
  public repo, and **respect the rollout order below**.
- `../brand/fleet.json` — banner identity, then regenerate `brand/generated/`.

`template_source` is what makes this a scaffold rather than an empty repo:
GitHub applies it at creation, so a new entry pointing at `lentago/repo-template`
lands with the fleet's README/CLAUDE/LICENSE/CI skeleton already in place.

Then `plan`, review, `apply`. The repo is created wired to fleet policy — squash
-only, auto-merge, spine topics, branch ruleset, Tidewater labels — rather than
drifting until someone remembers to sweep it.

### Changing fleet-wide policy

Edit `locals.tf`. `merge_policy`, `spine_topics`, and the squash commit-message
mode are single values that move all fifteen repos in one reviewable diff. That
is the point of keeping them out of `repos.json`.

### Retiring a repo

`prevent_destroy` means you cannot do this by deleting the entry. Archiving is
the fleet's actual retirement path anyway (`office-presence`,
`workstation-bootstrap`, `site-pitzilabs-dev` all went that way), and an
archived repo is read-only — Terraform can no longer manage its settings.

So: archive the repo, then remove it from `repos.json`, `required-checks.json`
and `brand/fleet.json`, and `terraform state rm` its resources in the same PR.
The state removal is the deliberate step that says "this is intentional."

### Required checks — the one rule Terraform cannot enforce

**Never require a context whose workflow is path-filtered at the `on:` level.**
A required check whose workflow never triggers is held "Expected" forever and
deadlocks every non-matching PR. Contexts must be the exact check-run names, and
the producing workflow must be **merged to `main` and observed green on a real
PR before** it is required here.

`fleet-apply.sh --require-checks` preflighted every context against live check
runs and refused to require an unproven one. Terraform has no equivalent — it
will happily apply a context that never reports. Keep using the script's
read-only check as the preflight:

```bash
../fleet-ops/fleet-apply.sh --repo NAME     # reports req-checks drift both ways
```

What Terraform *does* fix is the other half of that history
(lentago/.github#71): the script PUT a wholesale replacement, so a live context
missing from the file vanished silently. Here a dropped context is a line
disappearing from `required-checks.json` in a reviewable diff, and the plan
names the removal before anyone merges it.

## Adoption record

Adopted 2026-08-11 against the live fleet. `import` blocks in `imports.tf` cover
every existing resource; the acceptance test was a plan that changed nothing it
was not meant to:

```
Plan: 189 to import, 0 to add, 25 to change, 0 to destroy.
```

189 imports = 16 repositories + 15 rulesets + 158 labels, all resolved. Of the
25 changes, 16 were the provider-only flags `archive_on_destroy` and
`ignore_vulnerability_alerts_during_read` materialising in state (no API call).
The remaining 9 labels and 1 repository were all **`myosotis`** — the one repo
`fleet-apply.sh` had never successfully swept, because it is private:

- stock GitHub label colors, never recolored to Tidewater
- merge commits and rebase merges still enabled; no delete-branch-on-merge
- no `lentago`/`claude` spine topics

Every public repo planned clean. That delta is the module's first apply, and it
is a drift correction rather than a policy change.

> **Update 2026-08-12:** `myosotis` was transferred out of the org to a personal
> account before the module's first apply, and its rows were removed from
> `repos.json` — the first-apply plan is now 15 repositories, and the myosotis
> drift-correction delta described above no longer applies.

## Known asymmetries

Three things are seeded live-faithful rather than normalised, so that adoption
plans clean. Each is a one-line follow-up, not a migration:

- **`model_labels`** — four repos (betula, drosera, homeassistant-config,
  reference-checker) carry `model:haiku` + `model:opus` but not `model:sonnet`,
  which routes most work. Looks like an artefact of when each was set up.
- **`suggest_branch_update`** — true on 7 of 16 repos with no visible pattern.
- **`squash_commit_message = COMMIT_MESSAGES`** — the squash commit body is the
  concatenated branch commits, not the PR body. The fleet PR convention says the
  PR body "becomes the squash-merge commit message," which this setting does not
  actually deliver; `PR_BODY` would.

Making any of them uniform is an edit to `repos.json` or `locals.tf` and a plan
that says exactly which repos move.
