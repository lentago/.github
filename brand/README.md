# brand — Lentago Labs identity assets

Two things live here: the **org identity marks** (`avatars/`, `marks/`) and the
**per-repo brand generator** that turns them into the header every fleet repo
carries. Canonical palette, mark rationale, and typography rules are the
[brand contract](https://github.com/lentago/site-lentago-dev/blob/main/BRAND.md)
in `site-lentago-dev`; the design-system CSS there wins on any disagreement.

```
brand/
  avatars/      Org + personal GitHub avatars (manual upload — see avatars/README.md)
  marks/        The 64-grid genus marks, one per system, plus the lentago blossom
  fonts/        Space Grotesk + JetBrains Mono woff2, vendored for OG rasterizing
  fleet.json    Per-repo identity: mark, category, tagline, prompt line, badges
  generate.py   fleet.json -> generated/<repo>/{banner.svg, og.html, readme.md}
  render.sh     generated/<repo>/og.html -> og.png via headless Chrome
  generated/    Committed output. Generated — never hand-edit (CI enforces this).
```

## What each repo gets

| Artifact | Where it lands | How |
|---|---|---|
| `banner.svg` | the repo's `assets/banner.svg`, shown at the top of its README | copied in by PR |
| badge row | the repo's README, under the banner | copied in by PR |
| `og.png` | the repo's **social preview** | **manual upload — GitHub has no API for it** |

`generated/<repo>/readme.md` holds the exact header block a repo should carry,
so applying it is mechanical rather than a matter of taste.

## Regenerating

```bash
python3 brand/generate.py          # all repos
python3 brand/generate.py --repo solidago
./brand/render.sh                  # og.html -> og.png (needs Chrome/Chromium)
./brand/render.sh solidago
```

`ci/validate.py`'s **brand** check regenerates `banner.svg` and `readme.md` into
memory and diffs them against what's committed, so a hand-edit fails CI. It
skips `og.png` — rasterizing needs a browser, which CI has no reason to carry.
**Re-run `render.sh` yourself whenever `fleet.json` changes**, or the cards drift
from the banners without CI noticing.

## Design notes

- **Banners keep the font *stack*, not outlined text.** GitHub proxies README
  images through camo and will not load a webfont, so banner text renders in the
  viewer's `system-ui` / monospace. That's accepted — the org profile banner has
  always worked this way. The **OG cards are rasterized here** with the real
  self-hosted Space Grotesk and JetBrains Mono, so the typeface is baked in
  exactly where it survives: link unfurls, which are images anyway.
- **One genus mark per system.** `solidago`, `drosera`, `kalmia`, `claytonia`,
  and `betula` have their own; every other repo falls back to the lentago
  blossom. A repo that earns a mark gets its `fleet.json` entry repointed —
  drawing one is a design task, not a config change.
- **Gold is an accent, never a fill.** Per the brand contract, each banner spends
  its gold on exactly three things: the eyebrow diamond, the field-prompt ▲, and
  the bottom rule. The watermark and contour lines stay under 15% opacity.
- **The field prompt is `▲ lentago`** — never `$`, `>`, or the retired `:>`.

## Adding a repo

1. Add an entry to `fleet.json` (`mark`, `kind`, `tagline`, `prompt`, `badges`).
   Keep the tagline under ~58 characters; the generator uppercases it.
2. `python3 brand/generate.py --repo <name> && ./brand/render.sh <name>`
3. Commit `generated/<name>/`, then copy `banner.svg` into the target repo as
   `assets/banner.svg` and its `readme.md` block into that README.
4. Upload `og.png` by hand: repo **Settings → General → Social preview**.

## Issue labels

The fleet's Tidewater **issue-label palette** is not here — it's settings, not
assets, so it lives with the rest of the settings-as-code in
[`fleet-ops/labels.json`](../fleet-ops/labels.json) and is applied with
`fleet-ops/fleet-apply.sh --apply-labels`.
