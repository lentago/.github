# GitHub deployment environments, and the branches allowed to deploy to them.
#
# These matter because the fleet's cloud roles trust environments, not
# branches: a role whose trust policy names `environment:terraform` accepts any
# job that GitHub lets into `terraform`. The deployment branch policy is
# therefore the control that keeps a full-write role off feature branches. The
# hole it closes was found on 2026-11-01: any branch whose workflow declared
# `environment: terraform` received solidago's apply role.
#
# `can_admins_bypass` is declared per environment rather than left to the
# provider default. Every branch in this fleet is pushed by the one admin, so
# an admin bypass that reached the branch policy would reopen the hole.
#
# The environments below existed live before this file did; imports.tf adopts
# them, so the first apply is a no-op against what was set by hand.
resource "github_repository_environment" "fleet" {
  for_each = local.environments

  repository        = github_repository.fleet[each.value.repository].name
  environment       = each.value.environment
  can_admins_bypass = each.value.can_admins_bypass

  dynamic "deployment_branch_policy" {
    for_each = length(each.value.branches) > 0 ? [true] : []
    content {
      protected_branches     = false
      custom_branch_policies = true
    }
  }
}

resource "github_repository_environment_deployment_policy" "fleet" {
  for_each = merge([
    for key, env in local.environments : {
      for branch in env.branches : "${key}:${branch}" => { env = key, branch = branch }
    }
  ]...)

  repository     = github_repository_environment.fleet[each.value.env].repository
  environment    = github_repository_environment.fleet[each.value.env].environment
  branch_pattern = each.value.branch
}
