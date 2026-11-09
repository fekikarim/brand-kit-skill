# Brand Identity Kit — Reference Architecture

This document is a reference for the agent. It captures the exact structure and
pattern used by the QOVRI Brand Kit as the gold-standard template for all
brand kit generation.

---

## Symbol Generation Pattern (generate_masters.py)

```python
#!/usr/bin/env python3
"""
{BRAND_NAME} Brand Kit — Master Symbol Generator
Generates all vector master SVGs (symbol, favicon variants, all color treatments)
from parametric geometry. This is the single source of truth — every other
export is derived FROM these masters.

Run from the {BRAND_SLUG}-Brand-Kit/scripts directory:
    python3 generate_masters.py
"""
import math, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG_DIR = os.path.join(ROOT, "assets", "logos", "svg")
os.makedirs(SVG_DIR, exist_ok=True)

# ── BRAND PALETTE ───────────────────────────────────────────────────────────
DARK    = "{DARK_HEX}"    # {DARK_NAME}  — primary dark anchor
ACCENT  = "{ACCENT_HEX}"  # {ACCENT_NAME} — primary accent/energy
LIGHT   = "{LIGHT_HEX}"   # {LIGHT_NAME}  — primary light
MID     = "{MID_HEX}"     # {MID_NAME}    — mid-dark neutral
SLATE   = "{SLATE_HEX}"   # Muted Slate   — secondary text / borders
WHITE   = "#FFFFFF"
BLACK   = "#000000"

# ── SYMBOL GEOMETRY ─────────────────────────────────────────────────────────
# {SYMBOL_CONCEPT_DESCRIPTION}
# Coordinate system: 200×200 viewBox, center at (100,100)
CX, CY  = 100, 100   # center
R       = 64          # primary radius
SW      = 24          # ring stroke width
# ... additional shape-specific params

def pt(cx, cy, r, deg):
    rad = math.radians(deg)
    return cx + r * math.cos(rad), cy + r * math.sin(rad)

def ring_path(gap_start, gap_end, radius=R):
    sx, sy = pt(CX, CY, radius, gap_end)
    ex, ey = pt(CX, CY, radius, gap_start)
    return f"M {sx:.3f} {sy:.3f} A {radius} {radius} 0 1 1 {ex:.3f} {ey:.3f}"

def symbol_svg(ring_color, accent_color, background=None, bg_shape=None):
    bg = ""
    if background:
        rx = {"square": 0, "rounded": 40, "circle": None}[bg_shape]
        if bg_shape == "circle":
            bg = f'<circle cx="100" cy="100" r="100" fill="{background}"/>'
        else:
            bg = f'<rect x="0" y="0" width="200" height="200" rx="{rx}" fill="{background}"/>'
    # ... symbol body elements
    body = "<!-- symbol paths here -->"
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">'
        f'{bg}{body}</svg>'
    )

def write(name, content):
    path = os.path.join(SVG_DIR, name)
    with open(path, "w") as f:
        f.write(content)
    print("wrote", os.path.relpath(path, ROOT))

# ── SYMBOL VARIANTS ──────────────────────────────────────────────────────────
write("symbol-full-color.svg",         symbol_svg(DARK, ACCENT))
write("symbol-light-bg.svg",           symbol_svg(DARK, DARK))
write("symbol-dark-bg.svg",            symbol_svg(LIGHT, ACCENT))
write("symbol-black.svg",              symbol_svg(BLACK, BLACK))
write("symbol-white.svg",              symbol_svg(WHITE, WHITE))
write("symbol-monochrome-accent.svg",  symbol_svg(ACCENT, ACCENT))
write("symbol-reversed.svg",           symbol_svg(LIGHT, ACCENT, background=DARK, bg_shape="square"))
write("symbol-reversed-rounded.svg",   symbol_svg(LIGHT, ACCENT, background=DARK, bg_shape="rounded"))
write("symbol-on-accent.svg",          symbol_svg(DARK, DARK,  background=ACCENT, bg_shape="rounded"))

# ── FAVICON VARIANT (bolder weight for small sizes) ──────────────────────────
# Increase stroke weight ~40%, reduce radius slightly for legibility at 16px
def favicon_symbol_svg(ring_color, accent_color, background=None, bg_shape=None):
    fav_sw = int(SW * 1.42)   # heavier stroke
    fav_r  = R - 6            # slightly tighter to allow heavier stroke
    # ... same structure as symbol_svg but with fav_sw / fav_r
    pass

write("symbol-favicon-color.svg", favicon_symbol_svg(LIGHT, ACCENT, background=DARK, bg_shape="rounded"))
write("symbol-favicon-mono.svg",  favicon_symbol_svg(DARK, DARK))

print("Symbol masters generated.")
```

---

## Color Palette Reference

For palette generation, follow these contrast rules:

```
REQUIRED CONTRAST PAIRS (WCAG AA — 4.5:1 minimum for graphical marks):
  DARK on LIGHT   → verify ≥ 4.5:1
  ACCENT on DARK  → verify ≥ 4.5:1 (accent mark on dark bg)
  LIGHT on DARK   → verify ≥ 4.5:1 (light mark on dark bg)
  DARK on ACCENT  → verify ≥ 4.5:1 (dark mark on accent bg)
```

Python contrast check:
```python
def luminance(hex_color):
    r, g, b = int(hex_color[1:3],16)/255, int(hex_color[3:5],16)/255, int(hex_color[5:7],16)/255
    def linearize(c):
        return c/12.92 if c <= 0.04045 else ((c+0.055)/1.055)**2.4
    return 0.2126*linearize(r) + 0.7152*linearize(g) + 0.0722*linearize(b)

def contrast_ratio(hex1, hex2):
    l1, l2 = luminance(hex1), luminance(hex2)
    bright, dark = max(l1,l2), min(l1,l2)
    return (bright + 0.05) / (dark + 0.05)

# Example:
print(contrast_ratio("#10131B", "#F5F7FC"))  # → ~16.7:1 ✓
print(contrast_ratio("#C9FF55", "#10131B"))  # → ~12.4:1 ✓
```

---

## Typography Pairing Reference

| Pairing | Display Font | Body Font | Best for |
|---|---|---|---|
| **Power Tech** | Space Grotesk | Inter | Software, SaaS, Engineering |
| **Editorial** | Syne | DM Sans | Creative, Agency, Media |
| **Modern Rounded** | Urbanist | Plus Jakarta Sans | Consumer App, Startup |
| **Premium Minimal** | DM Serif Display | DM Sans | Luxury, Finance, Professional Services |
| **Bold Contemporary** | Clash Display | Satoshi | Fashion, Entertainment, Gaming |
| **Scientific** | IBM Plex Sans | IBM Plex Mono | Research, Data, Developer Tools |
| **Friendly Human** | Nunito | Work Sans | Healthcare, Education, Community |

Google Fonts download URLs follow this pattern:
```
https://fonts.gstatic.com/s/{fontname}/{hash}/{filename}.ttf
```
Use the `urllib.request` module to download fonts programmatically without
any external tools.

---

## Lockup Scaling Reference

Optimal proportions for combination marks (from QOVRI Kit):

```
HORIZONTAL LOCKUP:
  Symbol target height:  220px (in lockup canvas)
  Wordmark cap-height:   220 × 0.82 = 180px (optically balanced)
  Symbol–wordmark gap:   48px
  Outer padding:         36px all sides

STACKED LOCKUP:
  Symbol target height:  260px
  Wordmark target width: 260 × 2.6 = 676px (keeps proportions)
  Symbol–wordmark gap:   44px
  Outer padding:         40px all sides
```

---

## Site Webmanifest Template

```json
{
  "name": "{BRAND_NAME}",
  "short_name": "{BRAND_SLUG}",
  "description": "{BRAND_TAGLINE}",
  "start_url": "/",
  "display": "standalone",
  "background_color": "{DARK_HEX}",
  "theme_color": "{DARK_HEX}",
  "icons": [
    {"src": "/assets/icons/pwa/standard-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
    {"src": "/assets/icons/pwa/standard-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
    {"src": "/assets/icons/pwa/maskable-192.png", "sizes": "192x192", "type": "image/png", "purpose": "maskable"},
    {"src": "/assets/icons/pwa/maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}
  ]
}
```

---

## Android Adaptive Icon XML Template

`mipmap-anydpi-v26/ic_launcher.xml`:
```xml
<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background"/>
    <foreground android:drawable="@drawable/ic_launcher_foreground"/>
    <monochrome android:drawable="@drawable/ic_launcher_monochrome"/>
</adaptive-icon>
```

`values/ic_launcher_background.xml`:
```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="ic_launcher_background">{DARK_HEX}</color>
</resources>
```

---

## iOS Asset Catalog Template

`Assets.xcassets/AppIcon.appiconset/Contents.json`:
```json
{
  "images": [
    {
      "filename": "AppIcon-1024.png",
      "idiom": "universal",
      "platform": "ios",
      "size": "1024x1024"
    }
  ],
  "info": {
    "author": "xcode",
    "version": 1
  }
}
```

---

## Common Pitfalls to Avoid

1. **Never** scale down the standard-weight symbol for favicons — always use the
   heavier favicon variant.
2. **Never** place the full-color mark on the accent color background —
   the accent tail disappears. Use the monochrome-on-accent variant.
3. **Never** embed live text in SVG deliverables — always convert to paths.
4. **Never** hardcode absolute paths in scripts — always derive from `__file__`.
5. **Always** run scripts in the correct dependency order (masters → wordmark →
   lockups → all derived assets).
6. **Always** mathematically verify contrast ratios before shipping.
7. The `cairosvg.svg2png` function accepts either `url=` (file path) or
   `bytestring=` (encoded SVG string) — use whichever avoids a temp file.
8. For `favicon.ico`, use `Pillow`'s `Image.save(..., format="ICO", sizes=[...])`
   — not `cairosvg` which only does PNG.
