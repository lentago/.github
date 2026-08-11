terraform {
  required_version = ">= 1.7.0" # `import` blocks with for_each land in 1.7

  required_providers {
    github = {
      # Pinned to a minor, in the same spirit as the fleet's bpg/proxmox pin:
      # this provider gates repo existence and branch protection, so a surprise
      # schema change should be a deliberate bump rather than a fresh `init`.
      source  = "integrations/github"
      version = "~> 6.13"
    }
  }
}
