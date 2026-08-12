# The merge gate: who can update `main` at all.
#
# The org is a shared learning lab — colleagues on the Players team hold triage
# on every active repo. Triage cannot push or merge today, but this resource
# turns that from a side-effect of permission levels into a declared invariant:
# every merge to `main` lands through an org owner/admin, and a future write
# grant to anyone else still cannot reach `main` directly.
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
