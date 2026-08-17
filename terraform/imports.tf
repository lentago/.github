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

import {
  for_each = local.repos
  to       = github_repository.fleet[each.key]
  id       = each.key
}

import {
  for_each = local.repo_labels
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
    "music-curator"                = 17669624
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
