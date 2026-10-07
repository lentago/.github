#!/usr/bin/env python3
"""Draw the code-generated genus marks onto the lentago 64-grid.

The original six marks (lentago, solidago, drosera, kalmia, claytonia, betula)
were hand-drawn and are kept as literal SVG. The eight added in .github#235 are
drawn here, so a mark can be adjusted and re-emitted instead of hand-edited.
The rules every mark follows are in GRAMMAR.md next to this file.

Usage:  python3 brand/marks/draw.py            # rewrite every generated mark in place
        python3 brand/marks/draw.py osmunda    # one mark
"""

from __future__ import annotations

import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent

CREAM, FILAMENT, GOLD, CHIP = "#f3f0e8", "#cdd6d0", "#E0A81C", "#0e2b1a"
OUTLINE, FINE = 2.2, 1.4


# ---------------------------------------------------------------- primitives
def f(v: float) -> str:
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return "0" if s == "-0" else s


def P(d: str, w: float = OUTLINE, c: str = CREAM) -> str:
    return (f'<path d="{d}" stroke="{c}" stroke-width="{f(w)}" '
            f'stroke-linecap="round" stroke-linejoin="round"></path>')


def Fl(d: str) -> str:
    """A filament: the fine, paler line used for veins, stalks, and stamens."""
    return P(d, FINE, FILAMENT)


def dot(x: float, y: float, r: float = 2) -> str:
    """The gold accent. One kind per mark."""
    return f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{GOLD}"></circle>'


def ring(x: float, y: float, r: float, w: float = OUTLINE) -> str:
    return f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" stroke="{CREAM}" stroke-width="{f(w)}"></circle>'


def ell(x: float, y: float, rx: float, ry: float, rot: float = 0, w: float = OUTLINE, c: str = CREAM) -> str:
    t = f' transform="rotate({f(rot)} {f(x)} {f(y)})"' if rot else ""
    return (f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rx)}" ry="{f(ry)}" '
            f'stroke="{c}" stroke-width="{f(w)}"{t}></ellipse>')


def polar(cx: float, cy: float, r: float, deg: float) -> tuple[float, float]:
    """Point at distance r from (cx, cy); 0° is up, degrees run clockwise."""
    a = math.radians(deg)
    return (cx + r * math.sin(a), cy - r * math.cos(a))


def smooth(pts: list[tuple[float, float]], closed: bool = False) -> str:
    """Catmull-Rom spline through pts, emitted as cubic béziers."""
    if closed:
        pts = pts + pts[:3]
    d = f"M{f(pts[0][0])} {f(pts[0][1])}" if not closed else f"M{f(pts[1][0])} {f(pts[1][1])}"
    rng = range(len(pts) - 1) if not closed else range(1, len(pts) - 2)
    for i in rng:
        p0 = pts[max(i - 1, 0)]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[min(i + 2, len(pts) - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f"C{f(c1[0])} {f(c1[1])} {f(c2[0])} {f(c2[1])} {f(p2[0])} {f(p2[1])}"
    return d + ("Z" if closed else "")


def lobed(cx: float, cy: float, R: float, r: float, n: int, rot: float = 0, w: float = FINE) -> str:
    """A corolla seen face-on: n rounded lobes out to R, notched in to r."""
    pts = []
    for i in range(n):
        a = rot + 360 * i / n
        pts.append(polar(cx, cy, r, a - 180 / n))
        pts.append(polar(cx, cy, R * 0.92, a - 60 / n))
        pts.append(polar(cx, cy, R, a))
        pts.append(polar(cx, cy, R * 0.92, a + 60 / n))
    return P(smooth(pts, closed=True), w)


def leaf(x: float, y: float, L: float, W: float, ang: float, midrib: bool = True) -> list[str]:
    """An ovate leaf with its base at (x, y), pointing along ang."""
    tip = polar(x, y, L, ang)
    spread = math.degrees(math.atan2(W, L * 0.45))
    l1 = polar(x, y, L * 0.45, ang - spread)
    r1 = polar(x, y, L * 0.45, ang + spread)
    out = [P(smooth([(x, y), l1, tip, r1, (x, y)]))]
    if midrib:
        m = polar(x, y, L * 0.8, ang)
        out.append(Fl(f"M{f(x)} {f(y)}L{f(m[0])} {f(m[1])}"))
    return out


def leaflet(cx: float, cy: float, r0: float, r1: float, half: float, ang: float, k: float = 1.0) -> list[str]:
    """A lanceolate leaflet radiating from (cx, cy) between radii r0 and r1.

    k < 1 squashes the y axis, which tilts a whole rosette toward the viewer.
    """
    def pt(r: float, da: float) -> tuple[float, float]:
        x, y = polar(cx, cy, r, ang + da)
        return (x, cy + (y - cy) * k)

    def side(frac: float, width: float, sgn: int) -> tuple[float, float]:
        r = r0 + (r1 - r0) * frac
        return pt(r, sgn * math.degrees(math.atan2(width, r)))

    pts = [pt(r0, 0), side(0.3, half * 0.6, -1), side(0.62, half, -1), side(0.88, half * 0.55, -1),
           pt(r1, 0), side(0.88, half * 0.55, 1), side(0.62, half, 1), side(0.3, half * 0.6, 1), pt(r0, 0)]
    return [P(smooth(pts))]


def spiral(cx: float, cy: float, r0: float, r1: float, turns: float, start_deg: float, n: int = 64) -> list[tuple[float, float]]:
    """Points along an Archimedean spiral, winding clockwise from r0 out to r1."""
    pts = []
    for i in range(n + 1):
        t = i / n
        pts.append(polar(cx, cy, r0 + (r1 - r0) * t, start_deg + 360 * turns * t))
    return pts


# ---------------------------------------------------------------- marks
MARKS: dict[str, callable] = {}


def mark(name: str):
    def deco(fn):
        MARKS[name] = fn
        return fn
    return deco


@mark("asclepias")
def _asclepias() -> list[str]:
    """Milkweed: one seed adrift, low on the right, its floss fanning up and to the left."""
    sx, sy = 45, 47
    out = [ell(sx, sy, 6.5, 4.2, rot=45)]
    ox, oy = sx - 4.6, sy - 4.6
    for da in range(-40, 41, 10):
        L = 31 - abs(da) * 0.16
        m = polar(ox, oy, L * 0.5, -(45 + da * 1.2))
        e = polar(ox, oy, L, -(45 + da))
        out.append(Fl(smooth([(ox, oy), m, e])))
    out.append(dot(sx, sy, 2.4))
    return out


@mark("brasenia")
def _brasenia() -> list[str]:
    """Watershield: a colony of floating leaves, each with the stalk-point at its center."""
    out = []
    for (x, y, rx, ry) in ((23, 21, 14, 8.5), (44, 39, 12.5, 7.5), (22, 50, 9, 5.5)):
        out.append(ell(x, y, rx, ry))
        out.append(dot(x, y, 2))
    out.append(Fl("M42 14C47 11 53 12 58 16"))
    out.append(Fl("M5 36C8 33 12 33 15 35"))
    out.append(Fl("M40 54C45 52 51 53 57 57"))
    return out


@mark("epigaea")
def _epigaea() -> list[str]:
    """Trailing arbutus: a close cluster of salverform flowers over two leathery leaves."""
    out = []
    out += leaf(32, 50, 20, 7.5, -62)
    out += leaf(32, 50, 20, 7.5, 62)
    out.append(Fl("M32 50V58"))
    for (x, y, R) in ((32, 20, 9), (19, 31, 7.5), (45, 31, 7.5)):
        out.append(lobed(x, y, R, R * 0.5, 5, w=OUTLINE))
        out.append(dot(x, y, 1.8))
    return out


@mark("lupinus")
def _lupinus() -> list[str]:
    """Sundial lupine: the nine-leaflet palmate leaf, tilted, holding a drop at its center."""
    cx, cy = 32, 25
    out = [P(f"M{cx} {cy + 3}V60")]
    for i in range(9):
        out += leaflet(cx, cy, 3.5, 27, 4.2, 40 * i, k=0.58)
    out.append(dot(cx, cy, 2.6))
    return out


@mark("mitchella")
def _mitchella() -> list[str]:
    """Partridgeberry: the twin flowers face-on, two four-lobed corollas sharing one ovary."""
    out = [P("M32 60V46"), ring(32, 43, 3.2)]
    for x in (21, 43):
        out.append(Fl(f"M{f(x + (32 - x) * 0.15)} 39C{f(x + (32 - x) * 0.5)} 41 {f(x + (32 - x) * 0.8)} 42 32 43"))
        out.append(lobed(x, 27, 11, 7, 4, w=OUTLINE))
        for a in (0, 90, 180, 270):
            b, e = polar(x, 27, 4.5, a), polar(x, 27, 7.5, a)
            out.append(Fl(f"M{f(b[0])} {f(b[1])}L{f(e[0])} {f(e[1])}"))
        out.append(dot(x, 27, 2))
    return out


@mark("monarda")
def _monarda() -> list[str]:
    """Bee balm: a compact head on a bract ruff, hooked upper lips, stamens tipped gold."""
    out = [P("M21 40C24 34 40 34 43 40")]
    for s in (-1, 1):
        out.append(P(f"M32 41C{f(32 + s * 8)} 42 {f(32 + s * 15)} 46 {f(32 + s * 22)} 52"
                     f"C{f(32 + s * 14)} 52 {f(32 + s * 7)} 48 32 44"))
    out.append(Fl("M32 44V60"))
    for a in (-70, -46, -23, 0, 23, 46, 70):
        b = polar(32, 40, 7, a)
        e = polar(32, 40, 19, a)
        hook = polar(e[0], e[1], 4, a + 120)
        out.append(P(f"M{f(b[0])} {f(b[1])}L{f(e[0])} {f(e[1])}L{f(hook[0])} {f(hook[1])}"))
        st = polar(32, 40, 24, a - 7)
        out.append(Fl(f"M{f(e[0])} {f(e[1])}L{f(st[0])} {f(st[1])}"))
        out.append(dot(st[0], st[1], 1.5))
    return out


@mark("osmunda")
def _osmunda() -> list[str]:
    """Royal fern: a whole frond, feather-wise, its tip still unrolling."""
    sx, sy = 12, 58
    pts = spiral(44, 15, 1.2, 7.8, 1.3, 112)
    end = pts[-1]
    out = [P(f"M{sx} {sy}L{f(end[0])} {f(end[1])}"), P(smooth(pts))]
    ang = math.degrees(math.atan2(end[0] - sx, sy - end[1]))
    for frac, L in ((0.18, 8), (0.36, 10), (0.54, 10), (0.72, 8)):
        x, y = sx + (end[0] - sx) * frac, sy + (end[1] - sy) * frac
        for s in (-1, 1):
            out += leaflet(x, y, 0, L, 1.9, ang + 72 * s)
    out.append(dot(44, 15, 2))
    return out


@mark("uvularia")
def _uvularia() -> list[str]:
    """Bellwort: an arching stem through a perfoliate leaf, a single bell hanging at the tip."""
    out = [P("M16 60C14 42 20 18 38 11C45 8.5 50 12 50 19")]
    out.append(ell(18.2, 41, 11, 4.4, rot=-62))
    out.append(ell(28, 17.5, 9, 3.6, rot=-38))
    out.append(P("M50 20C44.5 25 42.5 35 43.5 45.5"))
    out.append(P("M50 20C55.5 25 57.5 35 56.5 45.5"))
    out.append(Fl("M50 21C48.5 30 51.5 38 50 47"))
    for x, y in ((45.5, 50.5), (50, 51.5), (54.5, 50.5)):
        out.append(dot(x, y, 1.6))
    return out


# ---------------------------------------------------------------- emit
def chip(name: str, body: list[str]) -> str:
    inner = "\n  ".join(body)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="512" height="512" '
            f'fill="none" role="img" aria-label="{name.capitalize()}">\n'
            f'  <rect width="64" height="64" rx="12" ry="12" fill="{CHIP}"></rect>\n'
            f'  {inner}\n</svg>\n')


def main(argv: list[str]) -> int:
    names = argv or sorted(MARKS)
    unknown = [n for n in names if n not in MARKS]
    if unknown:
        sys.exit(f"draw.py: no such mark {', '.join(unknown)} (have {', '.join(sorted(MARKS))})")
    for name in names:
        path = HERE / f"{name}-mark-square.svg"
        path.write_text(chip(name, MARKS[name]()))
        print(f"  {path.relative_to(HERE.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
