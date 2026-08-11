# The provider authenticates from $GITHUB_TOKEN — never a token in this tree.
#
# The token needs repo administration on every fleet repo (settings, topics,
# rulesets, labels) plus org repo-creation. Deliberately NOT `delete_repo`:
# without it, even a runaway plan physically cannot delete a repository, which
# is the outermost of the rails described in README.md § Rails.
#
# See README.md § Auth for how to mint it and which identity each run context
# uses.
provider "github" {
  owner = local.org
}
