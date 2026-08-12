locals {
  org = "lentago"

  # ---------------------------------------------------------------------------
  # Source of truth. Terraform reads the same fleet-ops JSON that fleet-apply.sh
  # reads, rather than forking a second copy of the fleet's settings — one file
  # per concern, one place to change it.
  # ---------------------------------------------------------------------------
  repos      = jsondecode(file("${path.module}/../fleet-ops/repos.json")).repos
  labels_cfg = jsondecode(file("${path.module}/../fleet-ops/labels.json")).labels
  checks_cfg = jsondecode(file("${path.module}/../fleet-ops/required-checks.json")).checks

  # ---------------------------------------------------------------------------
  # Uniform fleet policy. These are deliberately NOT per-repo knobs in
  # repos.json: they are the fleet's merge convention, so changing one here
  # moves all fifteen repos in a single reviewable diff.
  # ---------------------------------------------------------------------------

  # The topic spine every repo carries, unioned with each repo's signature
  # topics. fleet-apply.sh added the spine and left signature topics alone;
  # keeping the split here preserves that behaviour under a resource that
  # otherwise owns the whole topic list.
  spine_topics = ["lentago", "claude"]

  # Squash-only. The fleet PR workflow squashes every PR, and the ruleset's
  # allowed_merge_methods below enforces the same thing at the branch layer.
  merge_policy = {
    allow_squash_merge     = true
    allow_merge_commit     = false
    allow_rebase_merge     = false
    delete_branch_on_merge = true
  }

  # Live-faithful as of adoption. Worth knowing: COMMIT_MESSAGES means the
  # squash commit body is the concatenated branch commits, NOT the PR body —
  # which is not quite what the fleet PR convention describes. Left as-is so
  # adoption plans clean; changing it is a one-line policy PR, not a migration.
  squash_commit_title   = "COMMIT_OR_PR_TITLE"
  squash_commit_message = "COMMIT_MESSAGES"

  # GitHub Actions' app id — the integration that owns every required check
  # context in required-checks.json.
  actions_app_id = 15368

  # ---------------------------------------------------------------------------
  # The merge gate (protection.tf): the push allowlist on `main`. Every merge
  # lands through an org owner/admin — colleagues (Players team, triage)
  # contribute via PRs that an owner reviews and arms, and a future write grant
  # still cannot update `main`. "/username" is the provider's user syntax.
  # ---------------------------------------------------------------------------
  gate_allowlist = ["/cpitzi"]

  # Repo-scoped additions to the allowlist. music-curator's follow-fold
  # workflow performs its documented bot merge (`gh pr merge --squash` under
  # GITHUB_TOKEN — see music-curator#9), so the GitHub Actions app is allowed
  # there, and only there: fleet-wide, a workflow must not be able to update
  # `main`.
  # The id MUST be the next-format global node id (`A_…`). The legacy base64
  # form (`MDM6QXBwMTUzNjg=`) still resolves in queries, but the branch
  # protection mutation SILENTLY DROPS it from pushAllowances — the first apply
  # (2026-08-12) landed music-curator's rule with no app actor and no error.
  # Resolve with:  gh api graphql -f query='{ node(id:"<legacy>") { id } }'
  # and read next_global_id from the deprecation warning in extensions.
  gate_extra_allowances = {
    "music-curator" = ["A_kwHNJr_NPAg"] # the GitHub Actions app (id 15368)
  }

  # ---------------------------------------------------------------------------
  # Free-plan carve-outs. Both are plan limits, not policy choices, and both
  # were already special-cased in fleet-apply.sh.
  # ---------------------------------------------------------------------------

  # Branch rulesets on a private repo need GitHub Pro (the API 403s otherwise),
  # so private repos are simply out of scope for the ruleset resource.
  ruleset_repos = { for name, repo in local.repos : name => repo if repo.visibility == "public" }

  # ---------------------------------------------------------------------------
  # Derived: the repo x label matrix.
  #
  # Only labels named in labels.json are managed. Everything else a repo carries
  # — `zha`, `phase-1`, `governance` and the rest — is absent from this map and
  # therefore never touched, preserving fleet-apply.sh's never-delete rule.
  #
  # The model:* @claude routing labels are opt-in per repo via model_labels,
  # because they are functional on some repos and meaningless on others.
  # ---------------------------------------------------------------------------
  repo_labels = merge([
    for repo_name, repo in local.repos : {
      for label in local.labels_cfg :
      "${repo_name}:${label.name}" => {
        repository  = repo_name
        name        = label.name
        color       = label.color
        description = label.description
      }
      if !startswith(label.name, "model:") ||
      contains(repo.model_labels, trimprefix(label.name, "model:"))
    }
  ]...)
}
