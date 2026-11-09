#!/usr/bin/env python3
"""
QOVRI Brand Kit — Wordmark Generator

Builds the QOVRI wordmark as pure vector path data (text converted to paths,
no font dependency in the shipped SVG). Letterforms are drawn from Space
Grotesk Bold glyph outlines, with the Q's stock descender removed and
replaced by a bespoke diagonal connector + node terminal, matching the
language of the standalone brand symbol. This makes the wordmark a genuine
customization of Space Grotesk Bold (tracking, spacing, and a modified Q
terminal) rather than a fully custom-drawn typeface — documented as such in
BRAND-GUIDELINES.md.
"""
import math
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "fonts_dl", "SpaceGrotesk-Bold-renamed.ttf")
FONT_PATH = os.path.abspath(FONT_PATH)
SVG_DIR = os.path.join(ROOT, "assets", "logos", "svg")

INK = "#10131B"
LIME = "#C9FF55"
PORCELAIN = "#F5F7FC"
WHITE = "#FFFFFF"
BLACK = "#000000"

f = TTFont(FONT_PATH)
glyphSet = f.getGlyphSet()
cmap = f.getBestCmap()
hmtx = f['hmtx']
UPM = f['head'].unitsPerEm  # 1000


def glyph_path(ch):
    gid = cmap[ord(ch)]
    pen = SVGPathPen(glyphSet)
    glyphSet[gid].draw(pen)
    adv, lsb = hmtx[gid]
    return pen.getCommands(), adv


def rect_bar(ax, ay, bx, by, width):
    dx, dy = bx - ax, by - ay
    length = math.hypot(dx, dy)
    ux, uy = dx / length, dy / length
    px, py = -uy, ux
    hw = width / 2
    p1 = (ax + px * hw, ay + py * hw)
    p2 = (ax - px * hw, ay - py * hw)
    p3 = (bx - px * hw, by - py * hw)
    p4 = (bx + px * hw, by + py * hw)
    return f"M{p1[0]:.1f} {p1[1]:.1f} L{p2[0]:.1f} {p2[1]:.1f} L{p3[0]:.1f} {p3[1]:.1f} L{p4[0]:.1f} {p4[1]:.1f} Z"


def _signed_area(pts):
    s = 0.0
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return s / 2.0


def diamond(cx, cy, size, match_winding_of=None):
    h = size / 2
    pts = [(cx, cy + h), (cx + h, cy), (cx, cy - h), (cx - h, cy)]
    if match_winding_of is not None:
        target_sign = _signed_area(match_winding_of) >= 0
        this_sign = _signed_area(pts) >= 0
        if target_sign != this_sign:
            pts = list(reversed(pts))
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z"


def custom_q_path():
    """Space Grotesk Bold 'Q' ring (two subpaths: outer + inner counter),
    with the stock bottom stub subpath dropped and a bespoke diagonal
    tail + node appended in its place."""
    full, adv = glyph_path("Q")
    # The stock Q is three subpaths: outer ring, inner counter, tiny tail stub.
    # Split on 'M' command boundaries.
    parts = []
    cur = ""
    for token in full.replace("M", "\nM").split("\n"):
        if token:
            parts.append(token)
    ring_only = "".join(parts[:2])  # outer + inner counter, drop stock tail stub
    # Start well inside the ring band (not at its outer edge) so the straight
    # bar fully overlaps the curved stroke with no sliver gap at the seam.
    start = (520, 40)
    end = (700, -210)
    bar_pts = [start, end]
    bar = rect_bar(start[0], start[1], end[0], end[1], 112)
    node = diamond(end[0], end[1], 112, match_winding_of=bar_pts)
    return ring_only + bar + node, adv


LETTER_PATHS = {}
LETTER_PATHS["Q"], adv_q = custom_q_path()
for ch in "OVRI":
    LETTER_PATHS[ch], _ = glyph_path(ch)

ADVANCES = {"Q": 676, "O": 676, "V": 618, "R": 632, "I": 264}
TRACKING = 28  # extra units between letters (custom, slightly opened up for premium feel)


def build_word_paths(word, x0=0):
    """Return list of (translate_x, path_d) and total width."""
    x = x0
    out = []
    for ch in word:
        d = LETTER_PATHS[ch]
        out.append((x, d))
        x += ADVANCES[ch] + TRACKING
    total_w = x - TRACKING
    return out, total_w


def wordmark_svg(color, pad=40):
    letters, width = build_word_paths("QOVRI")
    # glyph y-up, font ascent/descent approx -200..720 for our custom Q tail
    y_top = 720
    y_bot = -230
    height = y_top - y_bot
    vb_w = width + pad * 2
    vb_h = height + pad * 2
    groups = []
    for x, d in letters:
        groups.append(
            f'<g transform="translate({x+pad},{pad}) scale(1,-1) translate(0,{y_bot})">'
            f'<path d="{d}" fill="{color}" fill-rule="nonzero"/></g>'
        )
    # flip trick: easier to just transform whole canvas once. Rebuild cleanly:
    inner = "".join(
        f'<path d="{d}" fill="{color}" fill-rule="nonzero" '
        f'transform="translate({x},0)"/>'
        for x, d in letters
    )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w:.0f} {vb_h:.0f}">'
        f'<g transform="translate({pad},{pad+y_top}) scale(1,-1)">{inner}</g>'
        f'</svg>'
    )
    return svg, vb_w, vb_h


def write(name, content):
    path = os.path.join(SVG_DIR, name)
    with open(path, "w") as fh:
        fh.write(content)
    print("wrote", os.path.relpath(path, ROOT))


for name, color in [
    ("wordmark-ink.svg", INK),
    ("wordmark-black.svg", BLACK),
    ("wordmark-white.svg", WHITE),
    ("wordmark-lime.svg", LIME),
]:
    svg, w, h = wordmark_svg(color)
    write(name, svg)

print("Wordmark masters generated. Aspect ratio ~%.2f:1" % (w / h))
