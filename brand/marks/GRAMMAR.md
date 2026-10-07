# Genus marks — the grammar

Every codenamed Lentago product carries a **genus mark**: a small drawing of the
plant it is named for, on the same grid and in the same hand as the lentago
blossom ([`fleet.json`](../fleet.json) records which mark each repo carries).
This file records the rules the existing marks follow, so the next one
can be drawn to match. It was written down when the set grew from six marks to
fourteen (#235, 2026-10-06); the rules themselves were read off the first six.

This directory is the canonical home of the marks. The first six (`lentago`,
`solidago`, `drosera`, `kalmia`, `claytonia`, `betula`) were pulled in verbatim
from the Claude Design "Lentago Labs Design System" project and are kept as
literal SVG. The eight added in #235 are emitted by [`draw.py`](draw.py); edit
the drawing there and re-run it rather than hand-editing the SVG.

## The grid

- The canvas is a **64 × 64 viewBox** — the SVG's own coordinate space, which
  stays the same whatever size the mark renders at — rendered here at 512 px.
  Coordinates are in grid units; keep the drawing inside roughly `6..58` on
  both axes so nothing touches the chip's rounded corners.
- The chip is a `#0e2b1a` square with `rx="12"` corners. The marks are drawn
  for this dark ground; the inline/limestone rendering swaps the colors (see
  *Colorways*).
- Marks are drawn as **strokes, not fills**. The SVG root carries
  `fill="none"`; the only filled shapes are the gold accent dots and an
  optional center disc.

## Strokes

| Role | Color | Width | Used for |
|---|---|---|---|
| Outline | cream `#f3f0e8` | `2.2` | the plant's silhouette — petals, leaves, stems, pods |
| Filament | `#cdd6d0` | `1.4` | the fine structure — veins, stamens, stalks, ripples |
| Center disc (optional) | ring `#f3f0e8` at `1.4`, fill `#0e2b1a` | `r="4.4"` | a flower's center when the mark is radial |

Line caps and joins are `round`. Nothing is thinner than `1.4` or thicker than
`2.2`.

## Gold

Anther gold `#E0A81C` is the one accent, and each mark spends it on **exactly one
kind of element**: the anthers, the dew, the seeds, the stalk-points, the berry
eyes. Never two kinds, never a fill larger than a dot (`r` ≤ about `3`). If you
cannot name the one thing the gold stands for, the mark is not finished.

## What a mark shows

- **A field feature.** Each mark shows the thing you would use to identify the
  plant on a walk: solidago's panicle (the branching flower spike), drosera's
  dewed tentacles, betula's lenticels (the horizontal breathing slits in birch
  bark), brasenia's stalk-point in a floating leaf, uvularia's bell on an
  arching stem. Not a generic flower with the right petal count.
- **A silhouette of its own.** The set has to read as a set, so every mark
  shares the grid and the strokes; but at 22 px the shapes must still tell
  apart. Before adding a radial five-part flower, check how many the set
  already has.
- **No letters, no icon-library shapes, no emoji.** The brand's glyph vocabulary
  is the plant plus the survey marks (▲ ◆ ●) used elsewhere.

## Legibility

Check a new mark at **16, 22, 40, 128 px** on the dark chip and at **22 and
56 px** on limestone before it lands. The 22 px size is what the org profile
README uses; the banner shows the mark at 80 px and as a huge ghosted
watermark, so stray detail that is invisible small will be very visible large.

## Colorways

- **Chip** (this directory): cream and filament strokes, gold dots, on the
  `#0e2b1a` ground. This is what `generate.py` consumes.
- **Inline / limestone**: the same geometry with the chip removed and the
  strokes recolored — cream → ink `#12311f`, filament → `#6b8576`. Gold stays
  gold. A center disc's fill becomes the paper color. Consumers do this swap
  themselves; there is no second set of files.

## Files and consumers

- `marks/<genus>-mark-square.svg` — one per codenamed product plus `lentago`.
  Template and demo repos do not get their own; their entries in
  [`fleet.json`](../fleet.json) point at their product's mark.
- [`fleet.json`](../fleet.json) → [`generate.py`](../generate.py) — the banner
  chip, the banner watermark, and the social-preview card.
- `profile/assets/marks/` — a verbatim copy, referenced by the org profile
  README's product rows.
- `site-lentago-dev/public/marks/` — the same marks, square-cornered, anchoring
  the Suite section on lentago.dev.

## Adding a mark

1. Draw it in `draw.py` (or, for a hand-drawn SVG, match the header and strokes
   above exactly) and run `python3 brand/marks/draw.py <genus>`.
2. Check it at the sizes listed under *Legibility*.
3. Copy it to `profile/assets/marks/`, repoint the repo's `mark` in
   `fleet.json`, then `python3 brand/generate.py && ./brand/render.sh`.
4. Commit the mark and the regenerated `generated/<repo>/`; upload the new
   `og.png` by hand (repo Settings → Social preview).
