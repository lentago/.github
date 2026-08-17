# Repository existence, identity, and merge-button options.
#
# This is the resource that made "everything, including repo creation" the
# chosen scope: adding an entry to fleet-ops/repos.json and merging creates the
# repository, wired to fleet policy from its first second rather than drifting
# until someone runs a sweep.
#
# It is also the highest-blast-radius resource in the fleet, so read
# README.md § Rails before changing anything here.
#
# trivy:ignore:AVD-GIT-0001 — public visibility is the fleet's premise (learning
# lab + public portfolio), set per-repo in repos.json, not an oversight.
#trivy:ignore:AVD-GIT-0001
resource "github_repository" "fleet" {
  for_each = local.repos

  name         = each.key
  description  = each.value.description
  homepage_url = each.value.homepage
  visibility   = each.value.visibility
  is_template  = each.value.template

  # Dependabot vulnerability alerts, fleet-wide. Live state was inconsistent
  # when tf-lint's trivy gate first flagged this (GIT-0003): some repos had
  # alerts on, solidago did not. Declared here so every repo gets it.
  vulnerability_alerts = true

  has_issues          = each.value.features.issues
  has_projects        = each.value.features.projects
  has_wiki            = each.value.features.wiki
  has_discussions     = each.value.features.discussions
  allow_update_branch = each.value.suggest_branch_update

  # Creation-only on GitHub's side, but declaring it is what lets a new entry in
  # repos.json be scaffolded from lentago/repo-template rather than starting
  # empty. Existing repos keep whatever they were born from.
  dynamic "template" {
    for_each = each.value.template_source == null ? [] : [each.value.template_source]
    content {
      owner                = template.value.owner
      repository           = template.value.repository
      include_all_branches = false
    }
  }

  # Signature topics + the fleet spine, as one set.
  topics = sort(distinct(concat(local.spine_topics, each.value.topics)))

  allow_squash_merge     = local.merge_policy.allow_squash_merge
  allow_merge_commit     = local.merge_policy.allow_merge_commit
  allow_rebase_merge     = local.merge_policy.allow_rebase_merge
  delete_branch_on_merge = local.merge_policy.delete_branch_on_merge

  # Auto-merge is unavailable on private repos on the Free plan, and asking for
  # it there is a permanent diff rather than a setting. `gh pr merge --auto`
  # simply cannot be the convention on those repos.
  allow_auto_merge = each.value.visibility == "public"

  squash_merge_commit_title   = local.squash_commit_title
  squash_merge_commit_message = local.squash_commit_message

  # Rail: if this resource is ever destroyed despite everything below, archive
  # the repository instead of deleting it.
  archive_on_destroy = true

  lifecycle {
    # Rail: refuse to plan a destroy at all. Removing a repo from repos.json
    # therefore errors rather than proposing deletion of a live repository —
    # retiring one is a deliberate two-step (see README.md § Retiring a repo).
    prevent_destroy = true
  }
}
