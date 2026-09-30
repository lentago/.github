# The merge gate: who can update `main` at all.
#
# The org is a shared learning lab — colleagues hold org-base `write` on every
# repo (2026-08-27; previously `none` plus a triage-only Players team, which was
# retired the same day as redundant once the base grant exceeded it). Write is
# exactly the grant this resource was built to survive: the gate is an allowlist
# on the ref, not a consequence of permission levels, so every merge to `main`
# still lands through an org owner/admin and a write grant to anyone else does
# not reach `main` directly.
#
# Why classic branch protection and not a ruleset `update` rule: rulesets gate
# by BYPASS, and GitHub's async auto-merge path does not honor bypass_actors —
# a PR whose merge depends on a bypass sits BLOCKED forever (see
# github/orgs/community discussions #162623 and #113172). That would silently
# kill the fleet's arm-auto-merge-on-every-PR convention. Classic protection's
# push restriction is an ALLOWLIST: allowed users push, merge, and auto-merge
# transparently; everyone else is refused. The two layers compose — the `main`
# ruleset keeps owning PR-required / squash-only / required checks /
# no-force-push; this resource owns only who may update the ref.
#
# trivy:ignore:AVD-GIT-0004 — signed commits are not required fleet-wide. That
# is an open policy decision (tracked in the issue filed alongside tf-lint
# adoption), not something to flip silently from a lint fix: requiring
# signatures would break every merge path (bots, runner App, squash-merge
# authorship) until keys and signing are rolled out deliberately.
#trivy:ignore:AVD-GIT-0004
resource "github_branch_protection" "merge_gate" {
  for_each = local.ruleset_repos

  repository_id = github_repository.fleet[each.key].node_id
  pattern       = "main"

  # Deliberately no checks, reviews, or history rules here — everything else
  # about `main` is the ruleset's job (rulesets.tf).
  restrict_pushes {
    blocks_creations = false
    push_allowances = concat(
      local.gate_allowlist,
      lookup(local.gate_extra_allowances, each.key, [])
    )
  }
}
