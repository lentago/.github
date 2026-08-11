terraform {
  # Remote state in solidago's S3 backend — shared account, isolated key, the
  # same pattern as drosera/kalmia/claytonia. The key is `dotgithub/` (the clone
  # directory name) rather than `.github/`: a state key beginning with a dot is
  # legal in S3 but reads as a hidden path in every listing and console view.
  #
  # Local applies authenticate as the cpitzi-iac IAM user. A dotgithub-scoped
  # OIDC role (S3 r/w on this key + the lock table) arrives with the
  # apply-on-merge phase — see README.md § Phases.
  backend "s3" {
    bucket         = "solidago-tfstate-365184644049"
    key            = "dotgithub/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "solidago-tfstate-lock"
    encrypt        = true
  }
}
