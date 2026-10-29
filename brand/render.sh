#!/usr/bin/env bash
# Rasterize brand/generated/<repo>/og.html -> og.png (1280x640) with headless
# Chrome, so the social-preview cards carry the real self-hosted Space Grotesk /
# JetBrains Mono rather than a system fallback. A repo that ships a Roku channel
# also gets roku-poster.html -> roku-poster-fhd.png (540x405) and
# roku-poster-hd.png (290x218), the channel's home-screen posters.
#
# Same harness lineage as site-pitzilabs-dev/lab/brand-assets/.
#
#   ./brand/render.sh              # every repo under generated/
#   ./brand/render.sh solidago     # one repo
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT="$HERE/generated"

CHROME="${CHROME:-}"
if [ -z "$CHROME" ]; then
  for c in google-chrome chromium chromium-browser google-chrome-stable; do
    if command -v "$c" >/dev/null 2>&1; then CHROME="$(command -v "$c")"; break; fi
  done
fi
[ -n "$CHROME" ] || { echo "render.sh: no Chrome/Chromium on PATH (set CHROME=)" >&2; exit 1; }

targets=()
if [ $# -gt 0 ]; then
  for r in "$@"; do targets+=("$OUT/$r"); done
else
  while IFS= read -r d; do targets+=("$d"); done < <(find "$OUT" -mindepth 1 -maxdepth 1 -type d | sort)
fi

profile="$(mktemp -d)"
trap 'rm -rf "$profile"' EXIT

# shoot <repo-dir> <page.html> <out.png> <width,height>
shoot() {
  local d="$1" page="$2" png="$3" size="$4" repo
  repo="$(basename "$d")"
  rm -f "${d:?}/$png"
  "$CHROME" --headless --disable-gpu --no-sandbox --hide-scrollbars \
    --user-data-dir="$profile/$repo-${png%.png}" \
    --force-device-scale-factor=1 --window-size="$size" \
    --virtual-time-budget=4000 \
    --screenshot="$d/$png" "file://$d/$page" >/dev/null 2>&1
  # Chrome exits 0 even when it writes nothing useful; check the artifact.
  if [ ! -s "$d/$png" ]; then
    echo "render.sh: $repo produced no $png" >&2
    exit 1
  fi
  printf '  %-30s %-22s %s\n' "$repo" "$png" "$(du -h "$d/$png" | cut -f1)"
}

for d in "${targets[@]}"; do
  repo="$(basename "$d")"
  [ -f "$d/og.html" ] || { echo "  skip $repo (no og.html)" >&2; continue; }
  shoot "$d" og.html og.png 1280,640
  if [ -f "$d/roku-poster.html" ]; then
    shoot "$d" roku-poster.html roku-poster-fhd.png 540,405
    shoot "$d" roku-poster.html roku-poster-hd.png 290,218
  fi
done

echo
echo "Social previews are a MANUAL upload — GitHub exposes no API for them."
echo "For each repo: Settings -> General -> Social preview -> Edit -> Upload og.png"
echo "Roku posters are copied into the channel repo by PR (roku-app/images/)."
