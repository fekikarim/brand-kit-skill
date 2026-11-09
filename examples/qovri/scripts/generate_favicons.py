#!/usr/bin/env python3
"""
QOVRI Brand Kit — Favicon & Web Icon Generator
Builds favicon.ico, favicon.svg, PNG favicons, apple-touch-icon, and the
web manifest, all from the favicon-optimized symbol master (bolder weight,
tuned for 16px legibility).
"""
import os
import shutil
from PIL import Image
import cairosvg

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG_DIR = os.path.join(ROOT, "assets", "logos", "svg")
FAVICON_DIR = os.path.join(ROOT, "assets", "icons", "favicon")
WEB_DIR = os.path.join(ROOT, "assets", "icons", "web")
os.makedirs(FAVICON_DIR, exist_ok=True)
os.makedirs(WEB_DIR, exist_ok=True)

SRC_SVG = os.path.join(SVG_DIR, "symbol-favicon-color.svg")  # dark rounded bg, lime/porcelain mark

# 1. Copy favicon.svg (scalable, modern-browser favicon)
shutil.copy(SRC_SVG, os.path.join(FAVICON_DIR, "favicon.svg"))

# 2. PNG favicons at required sizes
sizes = {
    "favicon-16x16.png": 16,
    "favicon-32x32.png": 32,
    "favicon-48x48.png": 48,
}
for fname, size in sizes.items():
    out = os.path.join(FAVICON_DIR, fname)
    cairosvg.svg2png(url=SRC_SVG, write_to=out, output_width=size, output_height=size)

# 3. apple-touch-icon.png (180x180, no transparency expected by iOS — flatten
#    onto the brand's dark rounded background, which the source already has)
apple_tmp = os.path.join(FAVICON_DIR, "apple-touch-icon.png")
cairosvg.svg2png(url=SRC_SVG, write_to=apple_tmp, output_width=180, output_height=180)

# 4. favicon.ico containing multiple embedded sizes
ico_sizes = [16, 24, 32, 48, 64, 128, 256]
imgs = []
for s in ico_sizes:
    tmp = f"/tmp/fav_{s}.png"
    cairosvg.svg2png(url=SRC_SVG, write_to=tmp, output_width=s, output_height=s)
    imgs.append(Image.open(tmp).convert("RGBA"))
base = imgs[-1]
base.save(
    os.path.join(FAVICON_DIR, "favicon.ico"),
    format="ICO",
    sizes=[(s, s) for s in ico_sizes],
)

# 5. Web icons (192 / 512, standard square PNGs used by the manifest + README)
for size in [192, 512]:
    out = os.path.join(WEB_DIR, f"icon-{size}.png")
    cairosvg.svg2png(url=SRC_SVG, write_to=out, output_width=size, output_height=size)

print("Favicon + web icon assets generated.")
