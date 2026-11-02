# Adoption of the live fleet into state.
#
# Every repository, ruleset, and palette label below already existed when this
# module was written — nothing here creates anything. The acceptance test for
# adoption was therefore a plan with no changes, which is what proves the module
# describes the fleet as it actually is rather than as it was assumed to be.
#
# These blocks are idempotent: once a resource is in state the import is a
# no-op. They stay for the same reason drosera's do — a fresh-state bootstrap
# (state lost, or a rebuild in a new backend) recovers by re-importing with no
# code changes.

# What exists live right now, so imports can be intersected against reality.
# Discovered the hard way on the first true birth (osmunda/monarda, PR #157):
# an import block for an object that does not exist is a hard plan error, so
# importing unconditionally over local.repos meant the module could ADOPT a
# fleet but never GROW one — every new repos.json entry failed the plan before
# creation was even considered. The ruleset import below always had this guard
# (via its hardcoded id map); these two now get the same treatment from a live
# query. Search-API lag on a seconds-old repo is harmless when terraform itself
# is creating that repo: the import is skipped and creation is the intended
# path. A repo created *outside* terraform seconds before a plan can be missed
# the same way; its create then fails loudly with a 422 "name already exists",
# and a re-run (once search catches up) imports it.
data "github_repositories" "live" {
  query = "org:lentago"
}

locals {
  live_repo_names = toset(data.github_repositories.live.names)
}

import {
  # Intersected with what exists live — a repo new to repos.json is created,
  # not imported (see data block note above).
  for_each = { for name in keys(local.repos) : name => name if contains(local.live_repo_names, name) }
  to       = github_repository.fleet[each.key]
  id       = each.key
}

# The same lesson one level down (ADR-0013's labels, PR #277): guarding label
# imports on the *repo* existing meant the palette could be adopted but never
# grown — a label newly added to labels.json has no live object on any repo,
# so every import failed with a 404 before creation was considered. Imports are
# now intersected with the labels each live repo actually carries; a new
# palette label is created, an existing one is adopted. Names compare
# case-insensitively, as GitHub's do, so a live "Bug" is adopted for a
# configured "bug" (and then re-cased) rather than skipped into a 422 create.
data "github_issue_labels" "live" {
  for_each   = { for name in keys(local.repos) : name => name if contains(local.live_repo_names, name) }
  repository = each.key
}

locals {
  live_label_keys = toset(flatten([
    for repo, d in data.github_issue_labels.live : [for l in d.labels : lower("${repo}:${l.name}")]
  ]))
}

import {
  for_each = { for k, v in local.repo_labels : k => v if contains(local.live_label_keys, lower(k)) }
  to       = github_issue_label.fleet[each.key]
  id       = "${each.value.repository}:${each.value.name}"
}

# Ruleset ids are server-assigned and are the one piece of live state this
# module has to hard-code — a ruleset has no natural key to import by. Captured
# 2026-08-11 (asclepias: 2026-08-12, created live with its ruleset before its
# rows landed here — a repo born outside terraform must have its ruleset id
# added to this map, or the next apply creates a duplicate "main" ruleset).
# A ruleset recreated by hand gets a new id, so refresh this map if an import
# ever fails with "not found" for a ruleset that plainly exists.
locals {
  live_ruleset_ids = {
    ".github"                      = 17933796
    "asclepias"                    = 20758046
    "betula"                       = 14521264
    "brasenia"                     = 19323889
    "claytonia"                    = 17713398
    "drosera"                      = 14522520
    "epigaea"                      = 14718477
    "kalmia"                       = 18293648
    "repo-template"                = 17671511
    "shared-workflows"             = 15538975
    "site-icecreamtofightwith-com" = 13559020
    "site-lentago-dev"             = 18237308
    "site-pondviewlane-com"        = 19125050
    "solidago"                     = 13837390
  }
}

import {
  # Intersected with ruleset_repos so a newly added repo — which has no live
  # ruleset yet — is created rather than failing an import for an id that does
  # not exist.
  for_each = { for name, id in local.live_ruleset_ids : name => id if contains(keys(local.ruleset_repos), name) }
  to       = github_repository_ruleset.main[each.key]
  id       = "${each.key}:${each.value}"
}

# Deployment environments (environments.tf, lentago/.github#311) were created
# live before this module managed them. Imports are intersected with what each
# repo actually carries, the same lesson as the labels above: an environment new
# to local.environments is created, an existing one is adopted. The map key
# "<repo>:<env>" is also the provider's import id.
data "github_repository_environments" "live" {
  for_each   = toset([for e in values(local.environments) : e.repository])
  repository = each.key
}

locals {
  live_environment_keys = toset(flatten([
    for repo, d in data.github_repository_environments.live : [for e in d.environments : "${repo}:${e.name}"]
  ]))
}

import {
  for_each = { for k, v in local.environments : k => v if contains(local.live_environment_keys, k) }
  to       = github_repository_environment.fleet[each.key]
  id       = each.key
}

# Deployment branch policy ids are server-assigned, like the ruleset ids above,
# and the provider's data source does not return them. Captured from
# GET /repos/lentago/<repo>/environments/<env>/deployment-branch-policies on
# the day the policy was set live (2026-11-01). A policy recreated by hand gets
# a new id, so refresh this map if an import fails with "not found".
locals {
  live_deployment_policy_ids = {
    "solidago:terraform:main" = 65166776
  }
}

import {
  for_each = local.live_deployment_policy_ids
  to       = github_repository_environment_deployment_policy.fleet[each.key]
  id       = "${join(":", slice(split(":", each.key), 0, 2))}:${each.value}"
}
