# Runtime Inventory — Lentago Labs Estate

**Snapshot date:** 2026-07-21 · **Scope:** every enumerable, versionable runtime
across local, hypervisor, VM, container, appliance, and cloud tiers.
**Method:** live-probed (operator workstation + five parallel sweeps); no values
assumed. This is a point-in-time snapshot, not an auto-regenerated report.

Components are grouped under the **Lentago product line** they serve. Anything
that spans products is listed under its primary line with the others noted in
the **Also** column — the suite's agnosticism principle in practice (each
product is a source-agnostic core plus per-source clients).

**Totals:** 1 workstation · 5 hypervisor nodes · 5 VMs · 10 LXCs · 2 appliances · 3 cloud surfaces.

---

## solidago — AWS cloud platform
*us-east-1 · workload account `365184644049`*

| Component | Runtime / version | Location | Also |
|---|---|---|---|
| ECS · solidago-dev-app ×2 | Fargate PV `1.4.0` · 256/512 · private ECR `:latest` + FireLens sidecar | solidago-dev-cluster | betula |
| ECS · solidago-dev-pondview | Fargate PV `1.4.0` · 256/512 · app + FireLens | solidago-dev-cluster | betula |
| ECS · solidago-dev-lentago | Fargate PV `1.4.0` · 256/512 · app + FireLens | solidago-dev-cluster | betula |
| Lambda · alb-log-shipper | `python3.12` | us-east-1 | betula |
| Lambda · pondview-ask | `nodejs22.x` | us-east-1 | — |
| RDS · postgres | PostgreSQL `16.13` | us-east-1 | — |

*As a client:* solidago is betula's next log collector (FireLens + ALB shipper → Axiom) and drosera's next telemetry source (Solidago CloudWatch datasource).

## drosera — observability suite / live Grafana pane

| Component | Runtime / version | Location | Also |
|---|---|---|---|
| Grafana Cloud | lentago.grafana.net · v`13.2.0` (Enterprise) · 13 datasources (Mimir, 4× Loki, Tempo, Pyroscope, Graphite…) | SaaS | — |
| Solidago CloudWatch datasource | cloudwatch (Grafana assume-role bridge) | Grafana Cloud | solidago |
| LXC 105 · grafana-stack | Ubuntu 22.04 · Docker 29.3.1 → `grafana/alloy:v1.6.1` (push shipper) | pve5 | kalmia |

*Sources:* homelab first (per-host Alloy → Grafana Cloud), solidago next.

## betula — log capture-and-archive → Axiom

| Component | Runtime / version | Location | Also |
|---|---|---|---|
| Axiom | 5 datasets · production sinks `cjp-solidago-alb` + `cjp-solidago-ecs` | SaaS | solidago |
| Firewalla collector | Docker 24.0.2 → `fluent/fluent-bit:latest` (first collector client) | Firewalla Gold SE | lentago |
| solidago collector | ECS FireLens `aws-for-fluent-bit:stable` sidecars + ALB-log Lambda | AWS us-east-1 | solidago |

*Collectors:* Firewalla (first), solidago (next). betula owns capture + archive; drosera owns the live pane.

## claytonia — agent fleet (the bullpen)

| Component | Runtime / version | Location | Also |
|---|---|---|---|
| LXC 110–112 · claude-runner ×3 | Debian 12 · Claude Code `2.1.177` · Node 20.18.1 | pve4 | — |
| LXC 116–117 · claude-runner-4/5 | Debian 12 · Claude Code `2.1.202` | pve4 | — |
| Job queue | NAS drop-file queue (`/srv/jobs`) | Neptune NAS | lentago |
| Terraform apply agent | 2nd runner agent on LXC 115 (runner-pool lifecycle) | pve4 · LXC 115 | kalmia |

*Carve-out:* the runner pool is the one guest class kalmia does not own — claytonia's own terraform manages LXC 110–112 / 116–117.

## kalmia — provisioning (workstations, VMs & container guest layer)

| Component | Runtime / version | Location | Also |
|---|---|---|---|
| Operator workstation | Ubuntu 26.04 · k7.0.0-27 · Node 24.15 · Python 3.14.4 · Go 1.23.6 · Java 25 · Claude Code 2.1.197 (ubuntu_laptop) | ThinkPad T14 | lentago |
| VM 102 · xubuntu-ws | Ubuntu 26.04 LTS · k7.0.0-27 · Python 3.14.4 · Docker 29.6.1 (xubuntu) | pve5 | — |
| VM 104 · fedora-ws | Fedora 43 KDE · k6.19.12 · Node 24.15 · Go 1.23.6 · OpenJDK 25 (fedora) | pve5 | — |
| VM 120 / 121 · testbeds | xubuntu-test + fedora-xfce-test (pristine-snapshot targets, stopped) | pve5 | — |
| LXC 115 · gha-runner | Debian 12 · terraform apply-on-merge agent (kalmia guest layer) | pve4 | claytonia |

*Guest-lifecycle owner:* kalmia terraform owns the existence & shape of every cluster guest except the claytonia runner pool — so it also stands behind the pub, lunaria, grafana-stack, n8n, and HAOS guests listed under their own lines.

## brasenia — shared viewport / wall display (Roku HLS)

| Component | Runtime / version | Location | Also |
|---|---|---|---|
| LXC 118 · lunaria | Debian 12 · lunaria-frames + lunaria-stream + `mediamtx v1.19.2` + `ffmpeg 5.1.9` (Chromium → H.264 HLS) | pve4 | kalmia |
| Roku dev channel | BrightScript HLS player → `board/index.m3u8` | play-room TV | — |
| Content source | renders the runtime-inventory page served by pub | LXC 114 pub | lentago |

*Now showing:* this inventory (kalmia#65). Guest shape + role provisioning owned by kalmia; renders whatever pub serves.

## lentago — shared substrate & org infra
*Not owned by a single product line.*

| Component | Runtime / version | Location | Also |
|---|---|---|---|
| Proxmox cluster ×5 | PVE `9.2.2` · kernel `7.0.2-6-pve` · quorate 5/5 (i7-5557U / i3-6100U / 3× i5-8500T) | homelab-cluster | — |
| Neptune NAS | Intel N100 · Debian 12 · k`6.12.30` · btrfs on md-RAID1 3.89 TB — storage, web drop, queue, backups | LAN | claytonia, brasenia |
| Firewalla Gold SE | ARM A55 · Ubuntu 22.04 aarch64 · k`5.10.110` · app 1.983 — gateway/DHCP/DNS | LAN edge | betula |
| LXC 114 · pub | Debian 12 · `Caddy v2.11.4` — the LAN web drop (`pub.lan`) | pve4 | brasenia, kalmia |
| VM 100 · HAOS | Home Assistant OS `18.1` · k6.18.37-haos (homeassistant-config) | pve3 | kalmia |
| LXC 113 · n8n | Debian 12 · Docker 29.6.1 → `n8nio/n8n:2.27.3` (workflow automation) | pve4 | kalmia |

---

## Cross-cutting components (carried under more than one line)

| Component | Primary | Also |
|---|---|---|
| ECS services / FireLens / ALB Lambda | solidago | betula |
| Solidago CloudWatch datasource | drosera | solidago |
| Axiom `cjp-solidago-*` sinks | betula | solidago |
| LXC 105 grafana-stack | drosera | kalmia |
| LXC 115 gha-runner | kalmia | claytonia |
| LXC 118 lunaria | brasenia | kalmia |
| LXC 114 pub | lentago | brasenia, kalmia |
| Neptune NAS | lentago | claytonia, brasenia |
| Firewalla | lentago | betula |
| Operator ThinkPad | kalmia | lentago |
| HAOS · n8n | lentago | kalmia |

---

## Notes

1. **AWS accounts (reconciled).** `365184644049` is the sole solidago workload
   account — all ECS/Lambda/RDS, the `solidago-tfstate-365184644049` bucket, and
   the KMS CMK live there. `008923505280` is **Grafana Cloud's own AWS account**,
   a federated third-party principal that assumes the read-only
   `solidago-dev-grafana-cloudwatch` role (gated by an External ID) to back the
   CloudWatch datasource. There is no second workload account and nothing is
   misconfigured.
2. **claytonia CLI drift.** Runners split `2.1.177` (110–112) vs `2.1.202`
   (116–117); operator laptop on 2.1.197.
3. **brasenia ↔ kalmia rename debt.** LXC 118 still named `lunaria` live
   (kalmia#63).
4. **Mutable image tags.** solidago ECS apps and the Firewalla fluent-bit run
   `:latest`, not digest-pinned.

---

*Generated with Claude Code (Opus 4.8), Home Claude session. Also served live on
the LAN at `http://pub.lan/runtime-inventory/` and streamed to the play-room
wall display via brasenia.*
