#!/usr/bin/env python3
"""Generate per-repo Lentago Labs brand assets from brand/fleet.json.

For every repo in fleet.json this emits, under brand/generated/<repo>/:

  banner.svg   1280x300 README hero — genus mark chip, repo name, mono tagline,
               field-prompt line, on the Tidewater hero gradient. Pure SVG
               geometry; safe to commit into the target repo as assets/banner.svg.
  og.html      1280x640 social-preview card, fonts inlined as base64 woff2.
               render.sh turns this into og.png via headless Chrome.
  readme.md    The exact README header block (banner + badge row) the target
               repo should carry, so applying it is mechanical.

Banners deliberately keep the font *stack* rather than converting text to
paths: GitHub proxies README SVGs through camo and will not load a webfont, so
they render in the viewer's system-ui/mono. The OG cards are rasterized here
with the real self-hosted Space Grotesk / JetBrains Mono, so the typeface is
baked in where it matters (link unfurls, which are images anyway).

Usage:  python3 brand/generate.py [--repo NAME]
"""

from __future__ import annotations

import argparse
import base64
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
MARKS = ROOT / "marks"
OUT = ROOT / "generated"
ORG = "lentago"

# Vendored from site-lentago-dev/public/design-system/tokens/fonts/ (that repo is
# the canonical home of the design system) so this generator runs anywhere — CI,
# a bullpen worker — without a sibling checkout. Only OG rasterization needs
# them; banners degrade to the system stack by design.
FONT_DIR = ROOT / "fonts"

# Tidewater — mirrors site-lentago-dev/BRAND.md. The CSS there is authoritative.
INK_STRONG = "#0e2b1a"
BRAND = "#1b4b2e"
ACCENT = "#E0A81C"
LIMESTONE = "#f3f0e8"
MUTED = "#9fb0aa"
DIM = "#748983"
STAMEN = "#cdd6d0"

DISPLAY = "'Space Grotesk', system-ui, -apple-system, Segoe UI, sans-serif"
MONO = "'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace"

# Space Grotesk 700 runs ~0.58em average advance; keeps long names clear of the
# watermark without hand-tuning each one.
NAME_MAX_PX = 48
NAME_MIN_PX = 28
NAME_BUDGET_PX = 700

BADGE = "https://img.shields.io/badge"
SHIELD_STYLE = f"style=flat-square&labelColor={INK_STRONG.lstrip('#')}"


def die(msg: str) -> None:
    sys.exit(f"generate.py: {msg}")


def mark_svg(name: str) -> str:
    path = MARKS / f"{name}-mark-square.svg"
    if not path.exists():
        die(f"no mark {path.name} — add it to brand/marks/ or fall back to 'lentago'")
    return path.read_text()


def mark_inner(svg: str, *, drop_chip: bool) -> str:
    """Body of a 64-grid mark, optionally without its background chip rect."""
    body = re.sub(r"^.*?<svg[^>]*>", "", svg, flags=re.S)
    body = re.sub(r"</svg>\s*$", "", body, flags=re.S)
    if drop_chip:
        body = re.sub(r"\s*<rect\b[^>]*(?:/>|></rect>)", "", body, count=1)
    return body.strip()


def name_size(name: str) -> int:
    fitted = int(NAME_BUDGET_PX / (max(len(name), 1) * 0.58))
    return max(NAME_MIN_PX, min(NAME_MAX_PX, fitted))


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


HERO_DEFS = f"""  <defs>
    <linearGradient id="hero" x1="0.08" y1="0" x2="0.86" y2="1">
      <stop offset="0" stop-color="{INK_STRONG}"></stop>
      <stop offset="1" stop-color="{BRAND}"></stop>
    </linearGradient>
    <clipPath id="frame"><rect width="{{w}}" height="{{h}}"></rect></clipPath>
  </defs>"""


def contours(x: float, y: float, scale: float) -> str:
    """Faint gold topographic curves — the dark-surface texture from BRAND.md."""
    paths = [
        ("M0 100 C 120 -10, 260 -10, 400 70", "0.10"),
        ("M0 80 C 130 -45, 270 -45, 420 40", "0.12"),
        ("M10 62 C 145 -78, 280 -78, 435 12", "0.14"),
        ("M25 46 C 160 -110, 290 -110, 448 -14", "0.11"),
    ]
    lines = "\n".join(
        f'      <path d="{d}" stroke-opacity="{o}"></path>' for d, o in paths
    )
    return (
        f'    <g transform="translate({x},{y}) scale({scale})" fill="none" '
        f'stroke="{ACCENT}" stroke-width="1.5">\n{lines}\n    </g>'
    )


def banner(repo: str, cfg: dict) -> str:
    w, h = 1280, 300
    inner_chip = mark_inner(mark_svg(cfg["mark"]), drop_chip=False)
    inner_ghost = mark_inner(mark_svg(cfg["mark"]), drop_chip=True)

    size = name_size(repo)
    # Optically centre the name/tagline pair against the 80px chip (y 110..190).
    name_y = 158 if size >= 40 else 154
    label = f'{ORG} labs — {repo}: {cfg["tagline"]}'

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(label)}">
{HERO_DEFS.format(w=w, h=h)}

  <g clip-path="url(#frame)">
    <rect width="{w}" height="{h}" fill="url(#hero)"></rect>

    <!-- Topographic contour lines, hugging the corner under the watermark -->
{contours(858, 214, 1.0)}

    <!-- Genus watermark, bleeding off the right edge -->
    <g transform="translate(896,-46) scale(6)" opacity="0.085">
{inner_ghost}
    </g>

    <!-- Eyebrow: gold diamond + category -->
    <text x="80" y="84" font-family="{MONO}" font-size="14" letter-spacing="4.5"><tspan fill="{ACCENT}">◆</tspan><tspan fill="{MUTED}">  {ORG.upper()} LABS · {cfg["kind"]}</tspan></text>

    <!-- Genus mark chip -->
    <g transform="translate(80,110) scale(1.25)">
{inner_chip}
    </g>

    <text x="184" y="{name_y}" font-family="{DISPLAY}" font-weight="700" font-size="{size}" fill="{LIMESTONE}" letter-spacing="-1.6">{esc(repo)}</text>
    <text x="186" y="186" font-family="{MONO}" font-size="14" fill="{STAMEN}" letter-spacing="1.6">{esc(cfg["tagline"].upper())}</text>

    <!-- Field prompt: triangulation marker, never $ or > -->
    <text x="80" y="250" font-family="{MONO}" font-size="14"><tspan fill="{ACCENT}">▲</tspan><tspan fill="{MUTED}"> {ORG}</tspan><tspan fill="{DIM}">  {esc(cfg["prompt"])}</tspan></text>

    <rect x="0" y="296" width="{w}" height="4" fill="{ACCENT}"></rect>
  </g>
</svg>
"""


def font_face(family: str, filename: str, weight: str) -> str:
    path = FONT_DIR / filename
    if not path.exists():
        die(f"missing font {path} — OG rasterization needs the site repo checked out alongside")
    b64 = base64.b64encode(path.read_bytes()).decode()
    return (
        f"@font-face{{font-family:'{family}';font-style:normal;font-weight:{weight};"
        f"font-display:block;src:url(data:font/woff2;base64,{b64}) format('woff2');}}"
    )


def og_html(repo: str, cfg: dict) -> str:
    w, h = 1280, 640
    inner_chip = mark_inner(mark_svg(cfg["mark"]), drop_chip=False)
    inner_ghost = mark_inner(mark_svg(cfg["mark"]), drop_chip=True)
    faces = "".join(
        [
            font_face("Space Grotesk", "space-grotesk-latin.woff2", "400 700"),
            font_face("JetBrains Mono", "jetbrains-mono-latin.woff2", "400 600"),
        ]
    )
    size = max(46, min(84, int(1180 / (max(len(repo), 1) * 0.58))))

    return f"""<!doctype html>
<meta charset="utf-8">
<title>{esc(repo)} — og</title>
<style>
{faces}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{w}px;height:{h}px;overflow:hidden}}
.card{{position:relative;width:{w}px;height:{h}px;
  background:linear-gradient(150deg,{INK_STRONG} 0%,{BRAND} 100%);
  font-family:'Space Grotesk',system-ui,sans-serif;overflow:hidden}}
.bg{{position:absolute;inset:0}}
.body{{position:relative;padding:88px 96px}}
.eyebrow{{font-family:'JetBrains Mono',monospace;font-size:20px;letter-spacing:.34em;color:{MUTED}}}
.eyebrow b{{color:{ACCENT};font-weight:400}}
.chip{{margin:56px 0 34px;width:132px;height:132px;display:block}}
.name{{font-weight:700;font-size:{size}px;letter-spacing:-.035em;color:{LIMESTONE};line-height:1}}
.tagline{{font-family:'JetBrains Mono',monospace;font-size:22px;letter-spacing:.1em;
  color:{STAMEN};margin-top:22px;text-transform:uppercase}}
.prompt{{position:absolute;left:96px;bottom:74px;font-family:'JetBrains Mono',monospace;
  font-size:20px;color:{DIM};white-space:nowrap}}
.prompt .m{{color:{ACCENT}}} .prompt .o{{color:{MUTED}}}
.rule{{position:absolute;left:0;right:0;bottom:0;height:8px;background:{ACCENT}}}
</style>
<div class="card">
  <svg class="bg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
{contours(706, 436, 1.6)}
    <g transform="translate(792,44) scale(9.5)" opacity="0.085">
{inner_ghost}
    </g>
  </svg>
  <div class="body">
    <div class="eyebrow"><b>◆</b>&nbsp;&nbsp;{ORG.upper()} LABS · {cfg["kind"]}</div>
    <svg class="chip" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
{inner_chip}
    </svg>
    <div class="name">{esc(repo)}</div>
    <div class="tagline">{esc(cfg["tagline"])}</div>
  </div>
  <div class="prompt"><span class="m">▲</span><span class="o"> {ORG}</span>&nbsp;&nbsp;{esc(cfg["prompt"])}</div>
  <div class="rule"></div>
</div>
"""


def badge(label: str, logo: str | None, color: str = BRAND) -> str:
    slug = label.replace("-", "--").replace("_", "__").replace(" ", "%20")
    url = f"{BADGE}/{slug}-{color.lstrip('#')}?{SHIELD_STYLE}"
    if logo:
        url += f"&logo={logo}&logoColor={ACCENT.lstrip('#')}"
    return f"![{label}]({url})"


def readme_block(repo: str, cfg: dict) -> str:
    """The exact header the target repo should carry. Mechanical to apply."""
    checks = (
        f"[![main](https://img.shields.io/github/check-runs/{ORG}/{repo}/main"
        f"?{SHIELD_STYLE}&color={BRAND.lstrip('#')}&label=main)]"
        f"(https://github.com/{ORG}/{repo}/actions)"
    )
    license_badge = (
        f"[![License](https://img.shields.io/github/license/{ORG}/{repo}"
        f"?{SHIELD_STYLE}&color={BRAND.lstrip('#')})]"
        f"(https://github.com/{ORG}/{repo}/blob/main/LICENSE)"
    )
    deepwiki = (
        f"[![Ask DeepWiki]({BADGE}/Ask-DeepWiki-{BRAND.lstrip('#')}?{SHIELD_STYLE}"
        f"&logo=readthedocs&logoColor={ACCENT.lstrip('#')})]"
        f"(https://deepwiki.com/{ORG}/{repo})"
    )
    stack = " ".join(badge(b["label"], b.get("logo")) for b in cfg["badges"])

    return f"""<!-- Lentago Labs brand header — generated by lentago/.github → brand/generate.py.
     Regenerate there; do not hand-edit the banner or badge URLs. -->
<a href="https://lentago.dev"><img src="./assets/banner.svg" alt="{esc(repo)} — {esc(cfg['tagline'])}" width="100%"></a>

{checks} {license_badge} {deepwiki}

{stack}
"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", help="generate a single repo instead of the fleet")
    args = ap.parse_args()

    fleet = {
        k: v for k, v in json.loads((ROOT / "fleet.json").read_text()).items()
        if not k.startswith("_")
    }
    if args.repo:
        if args.repo not in fleet:
            die(f"{args.repo} is not in fleet.json")
        fleet = {args.repo: fleet[args.repo]}

    for repo, cfg in fleet.items():
        d = OUT / repo
        d.mkdir(parents=True, exist_ok=True)
        (d / "banner.svg").write_text(banner(repo, cfg))
        (d / "og.html").write_text(og_html(repo, cfg))
        (d / "readme.md").write_text(readme_block(repo, cfg))
        print(f"  {repo:<30} mark={cfg['mark']:<10} {cfg['kind']}")

    print(f"\n{len(fleet)} repo(s) → {OUT.relative_to(ROOT.parent)}/")
    print("Next: ./brand/render.sh   (og.html → og.png via headless Chrome)")


if __name__ == "__main__":
    main()
