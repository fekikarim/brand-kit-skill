#!/usr/bin/env python3
"""
QOVRI Brand Kit — PWA Icon Generator
Standard icons (purpose: any) can safely touch the edges since the OS does
not mask them. Maskable icons are built as SEPARATE artwork: full-bleed
brand-color background with the symbol scaled to sit inside the ~80%-diameter
safe zone that Android/iOS masks are guaranteed not to crop.
"""
import os
import cairosvg

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG_DIR = os.path.join(ROOT, "assets", "logos", "svg")
PWA_DIR = os.path.join(ROOT, "assets", "icons", "pwa")
WEB_DIR = os.path.join(ROOT, "assets", "icons", "web")
os.makedirs(PWA_DIR, exist_ok=True)

INK = "#10131B"
LIME = "#C9FF55"

# Read the plain ring+tail geometry (no background) to recompose at a safe
# scale ourselves, rather than reusing a master that already has its own
# background baked in at a different safe-zone ratio.
with open(os.path.join(SVG_DIR, "symbol-full-color.svg")) as f:
    import re
    m = re.search(r'>(.*)</svg>', f.read(), re.S)
    SYMBOL_INNER = m.group(1)


def maskable_svg():
    # Safe zone: Android maskable spec = icon is 108x108dp with a 72x72dp
    # safe zone circle (centered). That is 66.6% of full bleed. We target
    # the symbol's 200x200 viewbox to occupy ~62% of the canvas, comfortably
    # inside the safe zone with margin to spare.
    canvas = 200
    scale = 0.60
    sym_size = canvas * scale
    offset = (canvas - sym_size) / 2
    inner_scale = sym_size / 200
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {canvas} {canvas}">'
        f'<rect x="0" y="0" width="{canvas}" height="{canvas}" fill="{INK}"/>'
        f'<g transform="translate({offset:.2f},{offset:.2f}) scale({inner_scale:.4f})">'
        f'{SYMBOL_INNER.replace(INK, "#F5F7FC")}'
        f'</g></svg>'
    )


mask_svg_path = os.path.join(PWA_DIR, "maskable-source.svg")
with open(mask_svg_path, "w") as f:
    f.write(maskable_svg())

for size in [192, 512]:
    cairosvg.svg2png(url=mask_svg_path, write_to=os.path.join(PWA_DIR, f"maskable-{size}.png"),
                      output_width=size, output_height=size)

# Standard (purpose: any) icons — reuse the transparent full-color symbol,
# safe to touch edges since no OS mask is applied.
for size in [192, 512]:
    cairosvg.svg2png(url=os.path.join(SVG_DIR, "symbol-full-color.svg"),
                      write_to=os.path.join(PWA_DIR, f"standard-{size}.png"),
                      output_width=size, output_height=size)

print("PWA icons (standard + maskable, 192 & 512) generated.")
