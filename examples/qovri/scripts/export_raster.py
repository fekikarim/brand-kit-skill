#!/usr/bin/env python3
"""
QOVRI Brand Kit — Raster & PDF Exporter
Derives PNG (multiple sizes, true transparency) and PDF exports from the
SVG vector masters. Never edits the masters themselves.
"""
import os
import cairosvg

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG_DIR = os.path.join(ROOT, "assets", "logos", "svg")
PNG_DIR = os.path.join(ROOT, "assets", "logos", "png")
PDF_DIR = os.path.join(ROOT, "assets", "logos", "pdf")
os.makedirs(PNG_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

# Square-ish marks: full size range. Wide lockups: sized by width to avoid
# stretching (height derives from the SVG's own aspect ratio).
SQUARE_SIZES = [256, 512, 1024, 2048]
WIDE_WIDTHS = [512, 1024, 2048]

SQUARE_FILES = [
    "symbol-full-color", "symbol-light-bg", "symbol-dark-bg", "symbol-black",
    "symbol-white", "symbol-monochrome-lime", "symbol-reversed",
    "symbol-reversed-rounded", "symbol-on-lime",
]

WIDE_FILES = [
    "lockup-horizontal-color", "lockup-horizontal-dark-bg", "lockup-horizontal-light-bg",
    "lockup-horizontal-black", "lockup-horizontal-white", "lockup-horizontal-tagline",
    "lockup-stacked-color", "lockup-stacked-dark-bg", "lockup-stacked-light-bg",
    "lockup-stacked-tagline", "lockup-stacked-white", "lockup-stacked-black",
    "wordmark-ink", "wordmark-black", "wordmark-white", "wordmark-lime",
]

PDF_FILES = SQUARE_FILES + WIDE_FILES

count = 0
for name in SQUARE_FILES:
    src = os.path.join(SVG_DIR, name + ".svg")
    for size in SQUARE_SIZES:
        out = os.path.join(PNG_DIR, f"{name}-{size}.png")
        cairosvg.svg2png(url=src, write_to=out, output_width=size, output_height=size)
        count += 1

for name in WIDE_FILES:
    src = os.path.join(SVG_DIR, name + ".svg")
    for w in WIDE_WIDTHS:
        out = os.path.join(PNG_DIR, f"{name}-{w}.png")
        cairosvg.svg2png(url=src, write_to=out, output_width=w)
        count += 1

print(f"Exported {count} PNG files to assets/logos/png/")

for name in PDF_FILES:
    src = os.path.join(SVG_DIR, name + ".svg")
    out = os.path.join(PDF_DIR, f"{name}.pdf")
    cairosvg.svg2pdf(url=src, write_to=out)

print(f"Exported {len(PDF_FILES)} PDF files to assets/logos/pdf/")
