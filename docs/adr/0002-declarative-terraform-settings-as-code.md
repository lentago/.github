# ADR-0002: Settings-as-code migrated from imperative sweep to declarative Terraform, incrementally

**Status:** Accepted (2026-08-11; reconstructed 2026-08-13)

## Context

Fleet settings — repo existence and identity, merge options, the topic spine, per-repo
`main` rulesets, required status checks, and the label palette — were applied by
`fleet-ops/fleet-apply.sh`, an **imperative sweep**: a script that reads the JSON
manifests and pushes each setting via `gh api`. It works, but drift is invisible until
the next run, and "what is the declared state" is only answerable by reading the script.

The GitHub Terraform provider models all of those surfaces declaratively: the declared
end state lives in code, drift becomes a `plan`, and a change becomes a reviewable diff.

## Decision

**Adopt Terraform (the GitHub provider) as the declarative owner of fleet settings,
incrementally — no big-bang cutover.** PR #82 ("Manage the fleet's GitHub settings with
the Terraform GitHub provider", merged 2026-08-11).

- **Adoption acceptance test.** `imports.tf` adopts every live resource, and the test
  was a plan that touched nothing it should not: `Plan: 189 to import, 0 to add, 25 to
  change, 0 to destroy` — 16 repositories, 15 rulesets, 158 labels — with every public
  repo planning clean. Of the 25 changes, 16 were provider-only flags
  (`archive_on_destroy`, delete-branch-on-merge), not identity or spine topics.
- **Division of labor, recorded.** Terraform owns the *declarable* surfaces above. The
  script keeps the two things Terraform structurally cannot do: `--prune-branches` (an
  imperative sweep over live branch/PR state) and the **required-context preflight**
  (proof that a check-run context actually reports before anything requires it —
  requiring a context that never reports deadlocks the repo).
- **apply-on-merge deliberately deferred** to phase 2 (issue #81, still open), per the
  fleet's own rollout-order doctrine: adopt and prove the plans clean first; wire the
  OIDC role, admin-token secret, plan-on-PR, and apply-on-merge second. In phase 1,
  applies are operator-run and CI does `fmt` + `validate` only.
- **Four blast-radius rails**, all recorded in `terraform/README.md` § Rails:
  1. the admin token is minted **without `delete_repo`** — a destroy cannot reach the
     delete API;
  2. `archive_on_destroy = true` — a destroyed repo archives instead of vanishing;
  3. `prevent_destroy = true` on every repository — Terraform refuses to *plan* a repo
     deletion;
  4. retirement is **archive + same-PR `state rm`**, so a removal is a reviewable diff
     that names itself before anyone merges.

## Alternatives

- **Keep the imperative `fleet-apply.sh` sweep (recorded — the prior state).**
  Rejected as the sole mechanism. Drift is not a plan and a change is not a diff; the
  declared state is only readable by reading the script. It survives for exactly the
  two jobs Terraform cannot do.
- **Big-bang cutover — rewrite everything as Terraform and flip in one PR (recorded,
  implicitly rejected).** Rejected in favor of import-and-adopt: the acceptance test
  was precisely that the first plan changed nothing of substance, which a big-bang
  rewrite could not have demonstrated.
- **A different IaC tool — Pulumi, or hand-rolled `gh api` idempotency
  (retrospective — not considered at the time).** *Lateral-to-worse.* The GitHub
  Terraform provider is the natural fit for GitHub resources and already models
  rulesets, required checks, repos, and labels; a general-purpose alternative would add
  a runtime and a state story without covering the surface any better.
- **apply-on-merge from day one (retrospective — not considered at the time).**
  *Worse.* Automating apply before the blast-radius rails were proven live would put
  destructive mutations one merge away with no operator in the loop — the exact reason
  the doctrine sequences adoption before automation.

## Consequences

- The fleet's GitHub settings are now declarative and version-controlled; drift shows
  up as a plan.
- Phase 1 is operator-run: a merge here does **not** yet mutate GitHub settings, which
  is a documented expectation (`terraform/README.md`, and the README's "Make a change
  yourself" note).
- The `terraform.yml` `gate` check already reports on every PR (`fmt` + `validate`) but
  is not yet *required*; it becomes required in phase 2, at which point a red plan
  blocks the merge — a one-line flip.
- The script and Terraform coexist by design; `CLAUDE.md` records that the script's
  settings-applying flags are superseded while its prune + preflight roles are not.
