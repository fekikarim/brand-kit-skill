#!/usr/bin/env python3
"""
QOVRI Brand Kit — Master Generator
Generates all vector master SVGs (symbol, wordmark, lockups, color variants)
from parametric geometry. This is the single source of truth: every other
export (PNG, PDF, favicons, platform icons) is derived FROM these masters.

Run from the QOVRI-Brand-Kit/scripts directory:
    python3 generate_masters.py
"""
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG_DIR = os.path.join(ROOT, "assets", "logos", "svg")
os.makedirs(SVG_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# BRAND PALETTE (final, selected after exploration — see BRAND-GUIDELINES.md)
# ---------------------------------------------------------------------------
INK = "#10131B"      # Midnight Ink — primary dark
LIME = "#C9FF55"      # Electric Lime — primary accent
PORCELAIN = "#F5F7FC"  # Porcelain — primary light
GRAPHITE = "#232835"
SLATE = "#A8B0C0"
WHITE = "#FFFFFF"
BLACK = "#000000"

FONT_WORD = "Space Grotesk"   # wordmark / headlines
FONT_BODY = "Inter"           # body / UI

# ---------------------------------------------------------------------------
# SYMBOL GEOMETRY — "The Open Node"
# A 290-degree precision ring (engineering compass arc) left intentionally
# open at the lower right, with a diagonal connector bar completing the Q
# through the gap and terminating in a small square "node" — reading as a
# geometric Q while evoking connection, forward motion and engineering
# precision. Built entirely from arcs and straight edges so it survives
# reduction to favicon scale.
# ---------------------------------------------------------------------------
CX, CY = 100, 100
R = 64
SW = 24          # ring stroke width
GAP_START = 12   # degrees
GAP_END = 78      # degrees
NODE = 20         # node square half-diagonal size (edge length)


def pt(cx, cy, r, deg):
    rad = math.radians(deg)
    return cx + r * math.cos(rad), cy + r * math.sin(rad)


def ring_path():
    sx, sy = pt(CX, CY, R, GAP_END)
    ex, ey = pt(CX, CY, R, GAP_START)
    return f"M {sx:.3f} {sy:.3f} A {R} {R} 0 1 1 {ex:.3f} {ey:.3f}"


def tail_group(color):
    """Diagonal connector bar through the gap + terminal node square."""
    mid = (GAP_START + GAP_END) / 2.0  # 45 degrees: south-east
    inner_r = R - SW / 2 + 4
    outer_r = R + 30
    ix, iy = pt(CX, CY, inner_r, mid)
    ox, oy = pt(CX, CY, outer_r, mid)
    node_cx, node_cy = pt(CX, CY, outer_r + 2, mid)
    return (
        f'<line x1="{ix:.3f}" y1="{iy:.3f}" x2="{ox:.3f}" y2="{oy:.3f}" '
        f'stroke="{color}" stroke-width="{SW}" stroke-linecap="square"/>'
        f'<rect x="{node_cx-NODE/2:.3f}" y="{node_cy-NODE/2:.3f}" width="{NODE}" height="{NODE}" '
        f'transform="rotate(45 {node_cx:.3f} {node_cy:.3f})" fill="{color}"/>'
    )


def symbol_svg(ring_color, tail_color, background=None, bg_shape=None):
    bg = ""
    if background and bg_shape == "square":
        bg = f'<rect x="0" y="0" width="200" height="200" rx="0" fill="{background}"/>'
    elif background and bg_shape == "rounded":
        bg = f'<rect x="0" y="0" width="200" height="200" rx="40" fill="{background}"/>'
    elif background and bg_shape == "circle":
        bg = f'<circle cx="100" cy="100" r="100" fill="{background}"/>'
    body = (
        f'<path d="{ring_path()}" fill="none" stroke="{ring_color}" '
        f'stroke-width="{SW}" stroke-linecap="square"/>'
        f'{tail_group(tail_color)}'
    )
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">'
        f'{bg}{body}</svg>'
    )


def write(name, content):
    path = os.path.join(SVG_DIR, name)
    with open(path, "w") as f:
        f.write(content)
    print("wrote", os.path.relpath(path, ROOT))


# --- Standalone symbol, full set of color treatments -----------------------
write("symbol-full-color.svg", symbol_svg(INK, LIME))
write("symbol-light-bg.svg", symbol_svg(INK, INK))           # for porcelain/white bg, all-ink
write("symbol-dark-bg.svg", symbol_svg(PORCELAIN, LIME))      # for midnight bg
write("symbol-black.svg", symbol_svg(BLACK, BLACK))
write("symbol-white.svg", symbol_svg(WHITE, WHITE))
write("symbol-monochrome-lime.svg", symbol_svg(LIME, LIME))
write("symbol-reversed.svg", symbol_svg(PORCELAIN, LIME, background=INK, bg_shape="square"))
write("symbol-reversed-rounded.svg", symbol_svg(PORCELAIN, LIME, background=INK, bg_shape="rounded"))
write("symbol-on-lime.svg", symbol_svg(INK, INK, background=LIME, bg_shape="rounded"))


# --- Favicon-optimized variant: bolder ring, larger node, simplified for
#     recognizability at 16x16 / 32x32. Same geometry family, different
#     weight so the mark doesn't fade into a gray smudge at tiny sizes.
def favicon_symbol_svg(ring_color, tail_color, background=None, bg_shape=None):
    fav_sw = 34
    fav_r = 58
    bg = ""
    if background and bg_shape == "square":
        bg = f'<rect x="0" y="0" width="200" height="200" fill="{background}"/>'
    elif background and bg_shape == "rounded":
        bg = f'<rect x="0" y="0" width="200" height="200" rx="44" fill="{background}"/>'
    sx, sy = pt(CX, CY, fav_r, GAP_END)
    ex, ey = pt(CX, CY, fav_r, GAP_START)
    ring = (f'<path d="M {sx:.3f} {sy:.3f} A {fav_r} {fav_r} 0 1 1 {ex:.3f} {ey:.3f}" '
            f'fill="none" stroke="{ring_color}" stroke-width="{fav_sw}" stroke-linecap="square"/>')
    mid = (GAP_START + GAP_END) / 2.0
    inner_r = fav_r - fav_sw / 2 + 6
    outer_r = fav_r + 34
    ix, iy = pt(CX, CY, inner_r, mid)
    ox, oy = pt(CX, CY, outer_r, mid)
    node_cx, node_cy = pt(CX, CY, outer_r + 4, mid)
    node = 30
    tail = (
        f'<line x1="{ix:.3f}" y1="{iy:.3f}" x2="{ox:.3f}" y2="{oy:.3f}" '
        f'stroke="{tail_color}" stroke-width="{fav_sw}" stroke-linecap="square"/>'
        f'<rect x="{node_cx-node/2:.3f}" y="{node_cy-node/2:.3f}" width="{node}" height="{node}" '
        f'transform="rotate(45 {node_cx:.3f} {node_cy:.3f})" fill="{tail_color}"/>'
    )
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">{bg}{ring}{tail}</svg>'


write("symbol-favicon-color.svg", favicon_symbol_svg(PORCELAIN, LIME, background=INK, bg_shape="rounded"))
write("symbol-favicon-mono.svg", favicon_symbol_svg(INK, INK))

print("Symbol masters generated.")
