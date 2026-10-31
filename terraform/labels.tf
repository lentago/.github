# The Tidewater issue-label palette, per repo.
#
# Colors and descriptions come from fleet-ops/labels.json — the same file the
# since-removed fleet-apply.sh --apply-labels read (lentago/.github#298),
# mirroring site-lentago-dev/BRAND.md.
#
# labels.json once carried an `ensure` flag (dropped in lentago/.github#300)
# that this module never read: it encoded "align this label only where it
# already exists," which is an imperative sweep's way of saying "some repos opt
# out." Terraform states the opt-in directly instead — a repo's model_labels list
# in repos.json — so the routing labels a repo carries are declared rather than
# discovered.
#
# Colors are passed through verbatim rather than lower-cased: GitHub stores the
# case it is given, and `help wanted` is live as `E0A81C`.
resource "github_issue_label" "fleet" {
  for_each = local.repo_labels

  repository  = github_repository.fleet[each.value.repository].name
  name        = each.value.name
  color       = each.value.color
  description = each.value.description
}
