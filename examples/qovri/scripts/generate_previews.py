#!/usr/bin/env python3
"""
QOVRI Brand Kit — Preview Contact Sheets
Builds the overview images in previews/: logo-overview, icon-overview,
color-palette, social-preview. Individual original assets are untouched —
these are supplementary contact sheets only.
"""
import os
import cairosvg
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG_DIR = os.path.join(ROOT, "assets", "logos", "svg")
PREVIEW_DIR = os.path.join(ROOT, "previews")
os.makedirs(PREVIEW_DIR, exist_ok=True)

INK = (16, 19, 27)
PORCELAIN = (245, 247, 252)
LIME = (201, 255, 85)
GRAPHITE = (35, 40, 53)
SLATE = (168, 176, 192)

FONT_PATH = "/home/claude/fonts_dl/Inter-SemiBold-renamed.ttf"
FONT_PATH_REG = "/home/claude/fonts_dl/Inter-Regular-renamed.ttf"


def load_svg(path, w, h=None):
    png_bytes = cairosvg.svg2png(url=path, output_width=w, output_height=h)
    import io
    return Image.open(io.BytesIO(png_bytes)).convert("RGBA")


def label(draw, xy, text, size=22, color=(35, 40, 53), font_path=FONT_PATH):
    font = ImageFont.truetype(font_path, size)
    draw.text(xy, text, fill=color, font=font)


# --- 1. logo-overview.png -------------------------------------------------
cell_w, cell_h = 420, 320
cols = 4
pad_x, pad_y = 60, 130
rows_needed = 2
canvas_w = pad_x * 2 + cols * cell_w + (cols - 1) * 20
canvas_h = pad_y + rows_needed * (cell_h + 60) + 20
canvas = Image.new("RGB", (canvas_w, canvas_h), PORCELAIN)
draw = ImageDraw.Draw(canvas)
label(draw, (50, 40), "QOVRI — Logo System Overview", size=38, color=INK)

cells = [
    ("symbol-full-color.svg", "Symbol — Full Color"),
    ("symbol-reversed.svg", "Symbol — Reversed"),
    ("symbol-black.svg", "Symbol — Black"),
    ("symbol-white.svg", "Symbol — White (on dark)"),
    ("wordmark-ink.svg", "Wordmark — Ink"),
    ("lockup-horizontal-color.svg", "Horizontal Lockup"),
    ("lockup-stacked-color.svg", "Stacked Lockup"),
    ("lockup-horizontal-tagline.svg", "Horizontal + Tagline"),
]
for i, (fname, title) in enumerate(cells):
    col = i % cols
    row = i // cols
    x = pad_x + col * (cell_w + 20)
    y = pad_y + row * (cell_h + 60)
    card = Image.new("RGBA", (cell_w, cell_h), (255, 255, 255, 255))
    cdraw = ImageDraw.Draw(card)
    cdraw.rectangle([0, 0, cell_w - 1, cell_h - 1], outline=(220, 222, 228), width=2)
    needs_dark = "white" in fname or "reversed" in fname and "rounded" not in fname
    if "white" in fname:
        cdraw.rectangle([10, 10, cell_w - 10, cell_h - 50], fill=(16, 19, 27))
    asset = load_svg(os.path.join(SVG_DIR, fname), 360)
    asset.thumbnail((cell_w - 60, cell_h - 90))
    ax = (cell_w - asset.width) // 2
    ay = 20 + (cell_h - 90 - asset.height) // 2
    card.paste(asset, (ax, ay), asset)
    canvas.paste(card, (x, y), card)
    label(draw, (x + 10, y + cell_h + 8), title, size=18, color=GRAPHITE, font_path=FONT_PATH_REG)

canvas.save(os.path.join(PREVIEW_DIR, "logo-overview.png"))
print("wrote previews/logo-overview.png")

# --- 2. icon-overview.png --------------------------------------------------
icon_items = [
    (os.path.join(ROOT, "assets", "icons", "favicon", "favicon-32x32.png"), "Favicon 32×32"),
    (os.path.join(ROOT, "assets", "icons", "web", "icon-192.png"), "Web Icon 192"),
    (os.path.join(ROOT, "assets", "icons", "pwa", "maskable-192.png"), "PWA Maskable 192"),
    (os.path.join(ROOT, "assets", "icons", "ios", "AppIcon-1024.png"), "iOS AppIcon 1024"),
    (os.path.join(ROOT, "assets", "icons", "android", "drawable-xxxhdpi", "ic_launcher_foreground.png"), "Android Foreground"),
    (os.path.join(ROOT, "assets", "icons", "desktop", "linux", "256x256", "qovri.png"), "Desktop Linux 256"),
]
cell = 260
pad_x2, pad_y2 = 60, 130
canvas2_w = pad_x2 * 2 + len(icon_items) * cell + (len(icon_items) - 1) * 40
canvas2_h = pad_y2 + cell + 60
canvas2 = Image.new("RGB", (canvas2_w, canvas2_h), PORCELAIN)
draw2 = ImageDraw.Draw(canvas2)
label(draw2, (50, 40), "QOVRI — Icon System Overview", size=38, color=INK)
for i, (path, title) in enumerate(icon_items):
    x = pad_x2 + i * (cell + 40)
    y = pad_y2
    bg = Image.new("RGBA", (cell, cell), (255, 255, 255, 255))
    bdraw = ImageDraw.Draw(bg)
    bdraw.rectangle([0, 0, cell - 1, cell - 1], outline=(220, 222, 228), width=2)
    try:
        im = Image.open(path).convert("RGBA")
        im.thumbnail((cell - 40, cell - 40))
        bg.paste(im, ((cell - im.width) // 2, (cell - im.height) // 2), im)
    except Exception as e:
        print("skip", path, e)
    canvas2.paste(bg, (x, y), bg)
    label(draw2, (x, y + cell + 10), title, size=17, color=GRAPHITE, font_path=FONT_PATH_REG)

canvas2.save(os.path.join(PREVIEW_DIR, "icon-overview.png"))
print("wrote previews/icon-overview.png")

# --- 3. color-palette.png --------------------------------------------------
canvas3 = Image.new("RGB", (1400, 420), (255, 255, 255))
draw3 = ImageDraw.Draw(canvas3)
label(draw3, (50, 30), "QOVRI — Color Palette", size=34, color=INK)

palette = [
    ("Midnight Ink", "#10131B", INK),
    ("Electric Lime", "#C9FF55", (201, 255, 85)),
    ("Porcelain", "#F5F7FC", (245, 247, 252)),
    ("Graphite", "#232835", GRAPHITE),
    ("Muted Slate", "#A8B0C0", SLATE),
]
sw = 240
for i, (name, hexv, rgb) in enumerate(palette):
    x = 50 + i * (sw + 20)
    y = 100
    draw3.rectangle([x, y, x + sw, y + sw], fill=rgb, outline=(210, 210, 210))
    txt_color = (255, 255, 255) if name in ("Midnight Ink", "Graphite") else (16, 19, 27)
    label(draw3, (x + 12, y + sw - 56), name, size=18, color=txt_color, font_path=FONT_PATH)
    label(draw3, (x + 12, y + sw - 30), hexv, size=16, color=txt_color, font_path=FONT_PATH_REG)

canvas3.save(os.path.join(PREVIEW_DIR, "color-palette.png"))
print("wrote previews/color-palette.png")

# --- 4. social-preview.png --------------------------------------------------
og_path = os.path.join(ROOT, "assets", "social", "og-preview-1200x630.png")
img = Image.open(og_path).convert("RGB")
img.save(os.path.join(PREVIEW_DIR, "social-preview.png"))
print("wrote previews/social-preview.png (copy of OG preview)")
