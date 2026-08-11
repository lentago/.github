# The per-repo `main` branch ruleset: PR-required, squash-only, no force-push,
# no branch deletion — plus the required status checks layered on top.
#
# fleet-apply.sh split these across two flags (--apply created the base ruleset,
# --require-checks edited its required_status_checks rule in place) because it
# had to mutate live JSON. Terraform declares the whole ruleset at once, which
# removes the failure mode behind lentago/.github#71: a wholesale PUT that
# silently dropped a live context missing from the file. Here a dropped context
# is a line disappearing from required-checks.json in a reviewable diff, and the
# plan spells out the removal before anyone merges it.
#
# The other hard rule from that history still applies and Terraform CANNOT
# enforce it: never require a context whose workflow is path-filtered at the
# `on:` level, or every non-matching PR deadlocks on a check that never reports.
# fleet-apply.sh preflighted contexts against live check runs; that preflight is
# retained as a read-only cross-check (see fleet-ops/README.md).
resource "github_repository_ruleset" "main" {
  for_each = local.ruleset_repos

  name        = "main"
  repository  = github_repository.fleet[each.key].name
  target      = "branch"
  enforcement = "active"

  conditions {
    ref_name {
      include = ["~DEFAULT_BRANCH"]
      exclude = []
    }
  }

  rules {
    deletion         = true
    non_fast_forward = true

    pull_request {
      required_approving_review_count   = 0
      dismiss_stale_reviews_on_push     = false
      require_code_owner_review         = false
      require_last_push_approval        = false
      required_review_thread_resolution = false
      allowed_merge_methods             = ["squash"]
    }

    # A repo with no mapped contexts gets no required_status_checks rule at all,
    # rather than an empty one — an empty rule reads as "clean" to GitHub and
    # blocks `gh pr merge --auto` from arming (lentago/.github#27).
    dynamic "required_status_checks" {
      for_each = length(lookup(local.checks_cfg, each.key, [])) > 0 ? [1] : []

      content {
        strict_required_status_checks_policy = false
        do_not_enforce_on_create             = false

        dynamic "required_check" {
          for_each = local.checks_cfg[each.key]
          content {
            context        = required_check.value
            integration_id = local.actions_app_id
          }
        }
      }
    }
  }
}
