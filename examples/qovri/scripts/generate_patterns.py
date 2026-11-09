#!/usr/bin/env python3
"""
QOVRI Brand Kit — Patterns & Backgrounds Generator
A small, restrained set of reusable backgrounds built from the symbol's own
geometry (the ring-arc + node), kept subtle so the logo stays the focus
whenever it's placed on top.
"""
import os
import re
import math
import cairosvg

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG_DIR = os.path.join(ROOT, "assets", "logos", "svg")
BG_DIR = os.path.join(ROOT, "assets", "backgrounds")
PATTERN_DIR = os.path.join(ROOT, "assets", "brand-patterns")
os.makedirs(BG_DIR, exist_ok=True)
os.makedirs(PATTERN_DIR, exist_ok=True)

INK = "#10131B"
LIME = "#C9FF55"
PORCELAIN = "#F5F7FC"
GRAPHITE = "#232835"


def write(path, content):
    with open(path, "w") as f:
        f.write(content)
    print("wrote", os.path.relpath(path, ROOT))


def png(svg_path, out_path, w, h=None):
    cairosvg.svg2png(url=svg_path, write_to=out_path, output_width=w, output_height=h)


# 1. Primary dark background — flat Midnight Ink, no pattern, for maximum
#    legibility behind light logo lockups
dark_bg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900"><rect width="1600" height="900" fill="{INK}"/></svg>'
write(os.path.join(BG_DIR, "primary-dark-1600x900.svg"), dark_bg)
png(os.path.join(BG_DIR, "primary-dark-1600x900.svg"), os.path.join(BG_DIR, "primary-dark-1600x900.png"), 1600, 900)

# 2. Primary light background — flat Porcelain
light_bg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900"><rect width="1600" height="900" fill="{PORCELAIN}"/></svg>'
write(os.path.join(BG_DIR, "primary-light-1600x900.svg"), light_bg)
png(os.path.join(BG_DIR, "primary-light-1600x900.svg"), os.path.join(BG_DIR, "primary-light-1600x900.png"), 1600, 900)

# 3. Subtle geometric brand pattern — a tiled grid of thin open-ring arcs
#    (the symbol's ring motif only, no tail), very low opacity, on ink.
tile = 160
r = 46
sw = 6
gap_start, gap_end = 12, 78


def pt(cx, cy, rr, deg):
    rad = math.radians(deg)
    return cx + rr * math.cos(rad), cy + rr * math.sin(rad)


sx, sy = pt(tile / 2, tile / 2, r, gap_end)
ex, ey = pt(tile / 2, tile / 2, r, gap_start)
ring_d = f"M {sx:.2f} {sy:.2f} A {r} {r} 0 1 1 {ex:.2f} {ey:.2f}"

pattern_svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {tile} {tile}">'
    f'<path d="{ring_d}" fill="none" stroke="{GRAPHITE}" stroke-width="{sw}" stroke-linecap="square"/>'
    f'</svg>'
)
write(os.path.join(PATTERN_DIR, "ring-motif-tile.svg"), pattern_svg)

# Build a full tiled pattern sheet (used directly as a CSS/HTML background,
# and exported flat for previews)
cols, rows = 10, 6
full_w, full_h = tile * cols, tile * rows
tiles = []
for row in range(rows):
    for col in range(cols):
        tiles.append(f'<g transform="translate({col*tile},{row*tile})"><path d="{ring_d}" fill="none" stroke="{GRAPHITE}" stroke-width="{sw}" stroke-linecap="square"/></g>')
# Transparent version — for use as a CSS/HTML decorative overlay, where a
# solid background rect would create a visible seam against the page's own
# background at any opacity other than 1.
pattern_sheet_transparent = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {full_w} {full_h}">'
    f'{"".join(tiles)}'
    f'</svg>'
)
write(os.path.join(PATTERN_DIR, "ring-motif-pattern-sheet-transparent.svg"), pattern_sheet_transparent)

# Opaque version — for use as a standalone deliverable/preview asset.
pattern_sheet = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {full_w} {full_h}">'
    f'<rect width="{full_w}" height="{full_h}" fill="{INK}"/>'
    f'{"".join(tiles)}'
    f'</svg>'
)
write(os.path.join(PATTERN_DIR, "ring-motif-pattern-sheet.svg"), pattern_sheet)
png(os.path.join(PATTERN_DIR, "ring-motif-pattern-sheet.svg"), os.path.join(PATTERN_DIR, "ring-motif-pattern-sheet.png"), full_w)

# 4. Minimal presentation background — dark with a single oversized, very
#    faint ring motif bleeding off the bottom-right corner (restrained,
#    doesn't compete with slide content)
with open(os.path.join(SVG_DIR, "symbol-full-color.svg")) as f:
    sym_content = f.read()
m = re.search(r'>(.*)</svg>', sym_content, re.S)
sym_inner = m.group(1).replace(INK, GRAPHITE).replace(LIME, GRAPHITE)

pres_bg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080">'
    f'<rect width="1920" height="1080" fill="{INK}"/>'
    f'<g opacity="0.35" transform="translate(1350,380) scale(3.2)">{sym_inner}</g>'
    f'</svg>'
)
write(os.path.join(BG_DIR, "presentation-background-1920x1080.svg"), pres_bg)
png(os.path.join(BG_DIR, "presentation-background-1920x1080.svg"), os.path.join(BG_DIR, "presentation-background-1920x1080.png"), 1920, 1080)

# 5. Social-media background — square, subtle corner motif, lime accent dot
social_bg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080">'
    f'<rect width="1080" height="1080" fill="{INK}"/>'
    f'<g opacity="0.3" transform="translate(680,680) scale(2.4)">{sym_inner}</g>'
    f'</svg>'
)
write(os.path.join(BG_DIR, "social-background-1080x1080.svg"), social_bg)
png(os.path.join(BG_DIR, "social-background-1080x1080.svg"), os.path.join(BG_DIR, "social-background-1080x1080.png"), 1080, 1080)

# 6. Website hero background — wide, dark, faint pattern strip at the
#    bottom edge only, keeps the top two-thirds clear for headline text
hero_bg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080">'
    f'<rect width="1920" height="1080" fill="{INK}"/>'
    f'<g opacity="0.22" transform="translate(-40,760)">'
    + "".join(
        f'<g transform="translate({col*tile},0)"><path d="{ring_d}" fill="none" stroke="{PORCELAIN}" stroke-width="{sw}" stroke-linecap="square"/></g>'
        for col in range(14)
    )
    + '</g></svg>'
)
write(os.path.join(BG_DIR, "website-hero-1920x1080.svg"), hero_bg)
png(os.path.join(BG_DIR, "website-hero-1920x1080.svg"), os.path.join(BG_DIR, "website-hero-1920x1080.png"), 1920, 1080)

print("Backgrounds and patterns generated.")
