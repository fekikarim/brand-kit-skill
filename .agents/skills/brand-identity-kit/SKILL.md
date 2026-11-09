---
name: brand-identity-kit
description: >-
  Full end-to-end brand identity kit generator. Given a natural-language brand
  description, the agent designs a bespoke SVG logo symbol, confirms it with the
  user, then generates the complete brand identity system: wordmark, lockups,
  color palette, typography, icons (favicon, PWA, iOS, Android, desktop),
  backgrounds, brand patterns, social assets (avatar, OG, LinkedIn, email
  signature, business card), an interactive brand showcase (index.html),
  BRAND-GUIDELINES.md, README.md, and a full asset-validation script — all
  derived from parametric Python scripts, mirroring the QOVRI Brand Kit
  architecture. Delivers a production-ready {brand-name}-brand-kit.zip.
ide_compatibility:
  - Antigravity (AGY)     # native — auto-loaded from .agents/skills/*/SKILL.md
  - Claude Code           # paste contents into CLAUDE.md or attach as context
  - Cursor                # add to .cursor/rules/*.mdc
  - Windsurf              # add to .windsurfrules
  - GitHub Copilot        # add to .github/copilot-instructions.md
  - Gemini CLI            # add to ~/.gemini/SYSTEM.md
  - Any AI with system prompt support   # paste as system prompt
python_dependencies:
  - cairosvg>=2.7
  - Pillow>=10.0
  - fonttools>=4.40
---

# Brand Identity Kit — End-to-End Generator Skill

> [!IMPORTANT]
> Read this entire file before starting. Every step is mandatory. Never skip
> confirmation gates. Quality over speed — this skill produces production-ready
> brand deliverables. The final output is a fully-packaged
> `{brand-name}-brand-kit.zip` containing every file the user needs.

## Compatibility

This skill works with **any AI IDE or agent** that can read a markdown system
prompt. No IDE-specific tooling is required — only Python 3.9+ and the
dependencies below.

**Required Python packages (install once):**
```bash
pip install cairosvg pillow fonttools
# macOS only: brew install cairo  (if cairosvg fails to install)
# Linux only: sudo apt install libcairo2-dev  (if cairosvg fails)
```

---

## Overview of the Workflow

```
Phase 0 → Brand Discovery & Briefing (gather requirements)
Phase 1 → Logo Symbol Design (parametric SVG, confirm with user)
Phase 2 → Color Palette & Typography Selection (confirm with user)
Phase 3 → Wordmark Design (font-based or geometric)
Phase 4 → Full Asset Pipeline (scripts generate every deliverable)
Phase 5 → Interactive Showcase (index.html)
Phase 6 → Documentation (BRAND-GUIDELINES.md, README.md, CHANGELOG.md, LICENSES.md)
Phase 7 → Validation, ZIP Packaging & Final Delivery
```

---

## Phase 0 — Brand Discovery & Briefing

**Goal:** Extract everything needed to design an original, tailored identity.

Ask the user (or mine from their description) for:

| Field | Purpose |
|---|---|
| **Brand name** | Used in wordmark and all file naming |
| **Industry / sector** | Shapes symbol metaphor and palette tone |
| **Target audience** | Influences personality (friendly vs corporate vs edgy) |
| **Brand personality** | 3–5 adjectives (e.g. "minimal, premium, forward-thinking") |
| **Tagline** (optional) | Included in lockup-tagline variant |
| **Color preferences** | Any "must haves", "must avoids", or existing colors |
| **Logo feel** | Geometric / organic / lettermark / abstract / icon-based |
| **Industry competitors** | To differentiate, not copy |
| **Primary use contexts** | App icon, website, print, social media, all of the above |
| **Output directory** | Where to place the brand kit folder |

If the user provides a free-form description, extract these fields yourself.
Summarize your extraction and ask the user to confirm or correct before
proceeding to Phase 1.

---

## Phase 1 — Logo Symbol Design

### 1a. Design Thinking

Based on the brand brief, design a **bespoke geometric symbol** that:

1. **Tells a visual story** rooted in the brand's core concept (do not use
   generic circles, generic checkmarks, or literal icons of the product).
2. **Survives reduction to 16px** — built from arcs, straight lines, and simple
   polygons only. No thin hairlines, no fine detail that disappears at small
   sizes.
3. **Works in a single flat color** (the monochrome version must be just as
   recognizable as the full-color version).
4. **Has a distinctive "open" or "signature" detail** that makes it unmistakably
   custom (a deliberate gap, a unique terminal, an asymmetric tension).
5. **Scales from favicon to billboard** without modification.

### 1b. Symbol Geometry Parameters

Define the following constants (all in a 200×200 viewBox coordinate system):

```python
# Core geometry — tune these to your brand concept
CX, CY = 100, 100          # Center of primary shape
R      = 64                # Primary radius / half-size
SW     = 24                # Stroke weight (ring/outline)
# Shape-specific params (gap angles, offsets, node size, etc.)
# Document what each means in a comment
```

**Symbol archetypes to consider** (pick one, then customize):

| Archetype | Geometric primitives | Good for |
|---|---|---|
| Open Arc / "Compass Ring" | Arc (270–300°) + diagonal bar + terminal node | Tech, engineering, navigation |
| Hexagon Aperture | Hexagon with one face open + inward stroke | B2B, enterprise, precision |
| Cross-Cut Circle | Full circle + two intersecting rectangles cutting through | Health, plus, intersection |
| Ascending Staircase | 3–4 stacked rectangles of increasing height + angle | Finance, growth, progress |
| Interlocked Arcs | Two overlapping arcs sharing a focal point | Partnership, duality, flow |
| Angular Shield | Pentagon/shield outline with inner notch | Security, protection, trust |
| Dynamic Slash | Bold diagonal bar through a containing shape | Speed, disruption, media |

**Choose the archetype** that best fits the brand brief, then customize angles,
proportions, and terminals to make it distinctive.

### 1c. Generate the Symbol SVG Preview

Write a Python script that generates an SVG of the symbol and display it to the
user as an inline image in chat (using generative UI or by embedding the SVG
content in a code block they can open in a browser).

The preview must show:
1. Full-color version (primary + accent color)
2. Monochrome version (single dark color, no background)
3. Reversed version (light mark on dark background)

> [!IMPORTANT]
> **CONFIRMATION GATE #1 — Do not proceed to Phase 2 until the user explicitly
> approves the logo symbol.** Show the symbol and ask:
> - "Does this symbol capture the essence of your brand?"
> - "Would you like any adjustments to the shape, weight, proportions, or concept?"
> Iterate on the geometry until the user says "looks good" or similar approval.

---

## Phase 2 — Color Palette & Typography

### 2a. Color Palette Design

Design a **minimal, disciplined palette** (3 primaries + 3–4 neutrals):

```
PRIMARY PALETTE (3 colors):
  • Dark anchor   — deep, near-black or very dark brand tone
  • Accent/energy — the brand's "electric" pop color (high saturation)
  • Light/air     — near-white or very light neutral

NEUTRAL PALETTE (3–4 colors):
  • Mid-dark  — a slightly lighter version of the dark anchor
  • Slate/muted — a desaturated mid-tone (for secondary text, borders)
  • White      — #FFFFFF
  • Black      — #000000
```

**Rules:**
- Every combination shipped in the final lockups must meet WCAG AA 4.5:1 contrast for the graphical mark against its background.
- Provide HEX, RGB, and approximate CMYK values for each primary.
- Name each color evocatively (e.g. "Midnight Ink", "Electric Lime", "Porcelain").

### 2b. Typography Selection

Select **two typefaces** from Google Fonts (OFL-licensed, free for commercial use):

| Role | Typeface | Weights needed |
|---|---|---|
| Logo / wordmark / headlines | A geometric or humanist sans serif with strong character | Bold, Medium |
| Body / UI / secondary text | A highly legible workhorse sans serif | Regular, SemiBold, (Bold optional) |

**Strong pairing options:**
- Space Grotesk + Inter (geometric + humanist, proven for tech brands)
- Syne + DM Sans (editorial + friendly, good for creative brands)
- Urbanist + Plus Jakarta Sans (modern rounded + versatile)
- DM Serif Display + DM Sans (editorial contrast pair)
- Clash Display + Satoshi (bold premium + clean body)

> [!IMPORTANT]
> **CONFIRMATION GATE #2 — Confirm colors and typography before proceeding.**
> Present:
> - A color swatch table (name, hex, RGB, role)
> - The font pairing with sample text in both faces
> - Ask "Does this palette and type pairing feel right for your brand?"
> Adjust until approved.

---

## Phase 3 — Wordmark Design

### 3a. Approach

The wordmark must be **pure vector paths** (text outlines, not live text) so it
displays correctly without font installation. Two approaches:

**Option A — Font-outline wordmark (recommended):**
Use `fonttools` to extract glyph outlines from the brand typeface, then:
1. Set the brand name in the display typeface at Bold weight.
2. Apply custom tracking (+20 to +40 font units for a premium, spaced feel).
3. **Modify one glyph** to visually connect the wordmark to the symbol — the
   most distinctive letter (usually the initial) gets a custom terminal, aperture
   cut, or added element that echoes the symbol's signature detail.
4. Convert all text to paths and output as SVG with no font dependency.

**Option B — Geometric letterforms:**
Build each letter from pure geometric primitives (rects, arcs, lines). Use only
when the brand brief explicitly calls for a fully custom typeface.

### 3b. Wordmark Script Requirements

The `generate_wordmark.py` script must:
- Import the font TTF via `fontTools.ttLib.TTFont`
- Extract glyph outlines via `fontTools.pens.svgPathPen.SVGPathPen`
- Apply custom tracking between letters
- Modify the signature glyph to echo the symbol
- Output: `wordmark-{color}.svg` for each of: ink (dark), black, white, accent

---

## Phase 4 — Full Asset Pipeline

### 4a. Project Directory Structure

Create the following directory tree at `{OUTPUT_DIR}/{BRAND_NAME}-Brand-Kit/`:

```
{BRAND_NAME}-Brand-Kit/
├── README.md
├── BRAND-GUIDELINES.md
├── LICENSES.md
├── CHANGELOG.md
├── index.html                        ← interactive brand showcase
├── assets/
│   ├── logos/
│   │   ├── svg/                      ← vector masters (source of truth)
│   │   ├── png/                      ← raster exports (256, 512, 1024, 2048px)
│   │   └── pdf/                      ← vector PDF exports for sharing/print
│   ├── icons/
│   │   ├── favicon/                  ← favicon.ico, favicon.svg, PNGs, manifest
│   │   ├── web/                      ← icon-192.png, icon-512.png
│   │   ├── pwa/                      ← standard + maskable PWA icons
│   │   ├── ios/                      ← Xcode asset catalog
│   │   ├── android/                  ← adaptive icon drawables
│   │   └── desktop/                  ← Windows .ico, Linux PNGs, macOS .iconset
│   ├── social/                       ← avatars, covers, OG, business card, etc.
│   ├── backgrounds/                  ← presentation / hero / social backgrounds
│   ├── brand-patterns/               ← pattern tile + tiled sheet
│   └── fonts/                        ← downloaded TTF + WOFF2 + OFL licenses
├── previews/                         ← overview contact-sheet images
└── scripts/
    ├── generate_masters.py           ← symbol SVG masters
    ├── generate_wordmark.py          ← wordmark paths from font
    ├── generate_lockups.py           ← horizontal + stacked combination marks
    ├── export_raster.py              ← PNG + PDF from SVG masters
    ├── generate_favicons.py          ← favicon.ico/.svg, apple-touch-icon
    ├── generate_pwa_icons.py         ← standard + maskable PWA icons
    ├── generate_social_assets.py     ← avatars, covers, OG, business card
    ├── generate_patterns.py          ← backgrounds + brand pattern
    └── validate_assets.py            ← comprehensive asset integrity checker
```

### 4b. Script: `generate_masters.py`

Generates all symbol SVG variants. Must produce:

```
symbol-full-color.svg          dark ring + accent tail, no background
symbol-light-bg.svg            all-dark on transparent (for light backgrounds)
symbol-dark-bg.svg             light + accent on transparent (for dark backgrounds)
symbol-black.svg               pure black, no background
symbol-white.svg               pure white, no background
symbol-monochrome-accent.svg   accent color only
symbol-reversed.svg            light + accent on dark square background
symbol-reversed-rounded.svg    light + accent on dark rounded-rect background
symbol-on-accent.svg           dark mark on accent background
symbol-favicon-color.svg       bolder-weight variant for favicon sizes
symbol-favicon-mono.svg        monochrome favicon variant
```

Each variant is built by calling a parameterized `symbol_svg(ring_color, tail_color, background, bg_shape)` function. The geometry constants (`CX`, `CY`, `R`, `SW`, gap angles, node size) must be defined once at the top — no magic numbers scattered through the code.

**Favicon variant:** Increase stroke weight by ~40% and radius slightly to compensate for anti-aliasing blur at 16px. The symbol must remain legible down to 16×16.

### 4c. Script: `generate_wordmark.py`

See Phase 3 for the approach. The script must:
1. Use `fonttools` to extract outlines from the brand font TTF.
2. Build letter advance/tracking table.
3. Modify the signature glyph terminal.
4. Output four color variants: ink (dark), black, white, accent.

### 4d. Script: `generate_lockups.py`

Composites symbol + wordmark into combination marks. Must produce:

**Horizontal lockups** (symbol left, wordmark right):
```
lockup-horizontal-color.svg        default: full-color symbol + dark wordmark
lockup-horizontal-dark-bg.svg      dark background, light + accent symbol + white wordmark
lockup-horizontal-light-bg.svg     light/porcelain background, all-dark
lockup-horizontal-black.svg        all black
lockup-horizontal-white.svg        all white on dark background
lockup-horizontal-tagline.svg      full-color + tagline below wordmark
```

**Stacked lockups** (symbol top, wordmark bottom, centered):
```
lockup-stacked-color.svg
lockup-stacked-dark-bg.svg
lockup-stacked-light-bg.svg
lockup-stacked-tagline.svg
lockup-stacked-white.svg
lockup-stacked-black.svg
```

**Key proportions:**
- Symbol height target: 220px (horizontal) / 260px (stacked) in the lockup canvas
- Wordmark cap-height: ~82% of symbol height for optical balance
- Gap between symbol and wordmark: ~48px horizontal / ~44px stacked
- Padding around entire lockup: 36–40px all sides

### 4e. Script: `export_raster.py`

Derives PNG and PDF from all SVG masters using `cairosvg`:
- Square symbols: exported at 256, 512, 1024, 2048px (width = height)
- Wide lockups/wordmarks: exported at 512, 1024, 2048px wide (height auto)
- PDF: all masters exported for print/sharing

### 4f. Script: `generate_favicons.py`

Favicon pipeline (all from the `symbol-favicon-color.svg` master):
- `favicon.svg` — scalable, modern browsers
- `favicon-16x16.png`, `favicon-32x32.png`, `favicon-48x48.png`
- `apple-touch-icon.png` — 180×180 (flattened, iOS expects opaque)
- `favicon.ico` — multi-size ICO containing 16, 24, 32, 48, 64, 128, 256px
- `icon-192.png`, `icon-512.png` — standard web icons
- `site.webmanifest` — referencing standard + maskable PWA icons

### 4g. Script: `generate_pwa_icons.py`

- `standard-192.png`, `standard-512.png` — purpose: any, may touch edges
- `maskable-192.png`, `maskable-512.png` — full-bleed brand background,
  symbol scaled to 60% canvas (inside Android/iOS safe zone circle)
- `maskable-source.svg` — SVG source of the maskable composition

### 4h. Script: `generate_social_assets.py`

Must produce (all pixel-perfect at exact platform dimensions):

| Asset | Size | Notes |
|---|---|---|
| `avatar-square-800.png` | 800×800 | Symbol on dark background, 56% scale, centered |
| `github-org-avatar.svg` | vector | Same composition as avatar |
| `github-org-avatar-460.png` | 460×460 | Raster version |
| `linkedin-company-logo-300.png` | 300×300 | Symbol on light background (LinkedIn dark-on-light guidance) |
| `linkedin-cover-1128x191.png` | 1128×191 | Horizontal lockup centered, tagline below |
| `og-preview-1200x630.png` | 1200×630 | Stacked composition: symbol + wordmark + tagline |
| `email-signature-logo.svg` | 60px tall | Compact horizontal, transparent, no background |
| `email-signature-logo.png` | @3× | 3× raster for email clients |
| `document-header-logo.svg` | 90px tall | Horizontal, ink-on-transparent |
| `document-header-logo.png` | @3× | For office document embedding |
| `presentation-title-slide-logo.png` | 900px wide | Stacked dark-bg lockup |
| `business-card-front-1050x600.png` | 1050×600 | Print-ready 3.5"×2" @300dpi |
| `business-card-front.svg` | vector | Same composition |

**Business card layout:**
- Dark background (brand anchor color)
- Symbol (small) top-left corner
- Wordmark below symbol
- Tagline in muted color
- Horizontal divider line
- Name + title bottom-left
- Email + website bottom-right

**Replace placeholder name/email** with actual brand contact info if provided, or use `[Name]`, `[Title]`, `[email@domain.com]`, `[website.com]` placeholders.

### 4i. Script: `generate_patterns.py`

Produces backgrounds and brand pattern:

1. **Primary dark background** — flat dark anchor color, 1600×900 SVG + PNG
2. **Primary light background** — flat light/porcelain color, 1600×900 SVG + PNG
3. **Brand pattern tile** — ring/arc motif from symbol geometry, tiled 160px grid, very low opacity
4. **Pattern sheet (transparent)** — 10×6 tile grid, no background (CSS overlay use)
5. **Pattern sheet (opaque)** — same with solid dark background, PNG export
6. **Presentation background** — 1920×1080, dark, single oversized ghost symbol (35% opacity) bleeding off bottom-right corner
7. **Social square background** — 1080×1080, dark, corner ghost symbol (30% opacity)
8. **Website hero background** — 1920×1080, dark, faint pattern strip along bottom edge only

> [!TIP]
> The brand pattern motif should be derived from the symbol's own geometry —
> if the symbol uses arcs, the pattern uses mini-arcs. This creates a cohesive
> system where every surface has DNA traceable to the logo.

### 4j. iOS & Android Icon Packages

**iOS (Xcode Asset Catalog):**
Create `assets/icons/ios/Assets.xcassets/AppIcon.appiconset/`:
- `AppIcon-1024.png` — 1024×1024 (universal, modern Xcode)
- `Contents.json` — Xcode manifest pointing to the 1024px image

**Android Adaptive Icons:**
Create the full drawable resource tree:
```
assets/icons/android/
├── ic_launcher_background.svg            ← solid accent color square
├── mipmap-anydpi-v26/
│   ├── ic_launcher.xml                   ← references background + foreground
│   └── ic_launcher_round.xml
├── values/
│   └── ic_launcher_background.xml        ← color resource
├── drawable-{mdpi,hdpi,xhdpi,xxhdpi,xxxhdpi}/
│   ├── ic_launcher_background.png
│   ├── ic_launcher_foreground.png        ← symbol on transparent
│   └── ic_launcher_monochrome.png        ← single-color version
└── legacy/mipmap-{mdpi,hdpi,xhdpi,xxhdpi,xxxhdpi}/
    └── ic_launcher.png                   ← flat pre-API26 icon
```

**Desktop icons:**
- `assets/icons/desktop/{BRAND_SLUG}.ico` — Windows, multi-size (16–256px)
- `assets/icons/desktop/linux/{size}/` — 16, 32, 48, 64, 128, 256, 512px PNGs
- `assets/icons/desktop/{BRAND_SLUG}.iconset/` — macOS iconset folder

### 4k. Font Downloads

Download the brand fonts from Google Fonts using Python `urllib` (no external
tools required):
- Display/wordmark font: TTF + WOFF2, Bold + Medium weights
- Body font: TTF + WOFF2, Regular + SemiBold weights
- Include OFL license text files

Place all in `assets/fonts/`.

### 4l. Run Order

Always run scripts in this order (later scripts depend on earlier outputs):

```bash
python3 generate_masters.py        # must run first — produces SVG sources
python3 generate_wordmark.py       # depends on font TTFs in assets/fonts/
python3 generate_lockups.py        # depends on symbol + wordmark SVGs
python3 export_raster.py           # depends on all SVG masters
python3 generate_favicons.py       # depends on symbol-favicon-color.svg
python3 generate_pwa_icons.py      # depends on symbol-full-color.svg
python3 generate_social_assets.py  # depends on symbol + wordmark SVGs
python3 generate_patterns.py       # depends on symbol-full-color.svg
```

**Always check for errors** after each script. If a script fails, fix the issue before running the next one.

---

## Phase 5 — Interactive Showcase (`index.html`)

Build a beautiful, self-contained HTML file that showcases every asset without
any server or build step (open directly in a browser from the filesystem).

### Required Sections

```
1. Sticky navigation bar with brand name + all section links
2. Hero section — large lockup on brand background with tagline
3. The Symbol — symbol variants grid (all color treatments)
4. Wordmark — all wordmark color variants
5. Logo Lockups — horizontal grid + stacked grid
6. Color Palette — swatches with name, hex, RGB, copy-to-clipboard
7. Typography — specimen showing both typefaces at multiple weights/sizes
8. Icons & Favicons — icon overview grid
9. Social Media Assets — preview grid with platform labels
10. Backgrounds & Patterns — full-width previews
11. Usage Guidelines — do/don't visual rules summary
12. Download/Files reference section
```

### Technical Requirements

- **Fully self-contained** — all images referenced by relative path from the
  `index.html` location. No CDN, no external fonts (use `@font-face` with the
  local `assets/fonts/*.woff2` files).
- **Dark mode aware** — the page should look premium on both light and dark OS
  preferences (use `prefers-color-scheme` or a manual toggle).
- **Responsive** — works on mobile to 4K. Use CSS Grid and fluid sizing.
- **Color swatch click-to-copy** — clicking a swatch copies the hex value.
- **No JS frameworks** — vanilla JS only for swatch copy, smooth scroll, any
  minimal interactions. No React, Vue, etc.
- **Semantic HTML** — use `<section>`, `<nav>`, `<figure>`, `<figcaption>` etc.
- **Brand colors as CSS custom properties** in `:root`.

---

## Phase 6 — Documentation

### `BRAND-GUIDELINES.md`

Write a comprehensive brand manual covering:

1. Brand Overview & Positioning
2. Mission, Audience, Personality
3. The Symbol — name, concept, construction description, do/don't rules
4. The Wordmark — typeface, tracking, modified glyph, honesty note (custom vs modified)
5. Logo Variants & When to Use Them (table)
6. Clear Space & Minimum Size rules
7. Correct & Incorrect Usage (do/don't lists)
8. Color Palette (primary + supporting, HEX, RGB, CMYK approximations)
9. Typography (role, typeface, weight, license)
10. Backgrounds & Contrast Rules (which logo variant on which background)
11. Icon & Favicon Usage
12. Social Media & Document Applications
13. Recommended Export Formats (table)
14. File-Naming Conventions
15. Asset Regeneration Instructions (exact commands)
16. Accessibility Considerations (contrast ratios, color-independent legibility, language coverage)
17. Known Limitations & Outstanding Verification Tasks (trademark caveat, CMYK caveat, macOS .icns caveat)

### `README.md`

Cover:
- Project description + tagline
- Directory tree (copy the structure from Phase 4a)
- Asset categories at a glance
- Recommended logo variant by use case (table)
- Favicon installation (HTML code snippet)
- Web/PWA integration
- iOS integration (Xcode steps)
- Android integration (resource copy steps)
- Desktop integration (Windows/Linux/macOS)
- Social media asset recommendations (table)
- Regenerating assets (run order + pip install line)
- Validating assets (`python3 validate_assets.py`)
- Required software & dependencies
- Known platform-specific limitations
- Licensing notes (brand artwork vs fonts)
- Trademark & domain verification disclaimer

### `LICENSES.md`

Include:
- Brand identity artwork license statement (copyright, usage terms)
- Each font's OFL 1.1 license excerpt + link to full text

### `CHANGELOG.md`

```markdown
# Changelog

## 1.0.0 — {date}

### Added
- Initial release of the {Brand Name} Brand Identity System
- Complete symbol, wordmark, and lockup suite
- Full icon platform packages (favicon, PWA, iOS, Android, desktop)
- Social media and business assets
- Brand patterns and backgrounds
- Interactive brand showcase (index.html)
- Brand guidelines and documentation
```

---

## Phase 7 — Validation, ZIP Packaging & Final Delivery

### `validate_assets.py`

Write a comprehensive validator that checks:

1. **SVG files** — parse as XML, confirm `viewBox` present, no external URL dependencies
2. **PNG files** — decode with Pillow, verify mode/alpha, check dimensions are sane (not 1×1 or zero-byte)
3. **JSON/webmanifest files** — parse as JSON, confirm valid
4. **XML files** (Android resources) — parse, confirm valid
5. **ICO files** — verify genuine multi-size ICO header, not a renamed PNG
6. **Required files presence** — check all mandatory files exist
7. **Empty files / zero-byte files** — flag any
8. Exit 0 if no errors, exit 1 with error list if any checks fail

### Run Validation

After running all generation scripts, run:
```bash
python3 validate_assets.py
```
Fix any errors reported before delivering to the user.

### ZIP Packaging (MANDATORY)

> [!IMPORTANT]
> **Always package the final brand kit as a ZIP file.** The user expects to
> receive a single, ready-to-use archive — not a folder they have to find and
> compress themselves.

After validation passes with no errors:

```bash
# Navigate to the OUTPUT_DIR (parent of the {BRAND_NAME}-Brand-Kit/ folder)
cd {OUTPUT_DIR}

# Create the zip — the kit folder is the top-level entry
zip -r "{BRAND_SLUG}-brand-kit.zip" "{BRAND_NAME}-Brand-Kit/" --exclude "*/__pycache__/*" --exclude "*/.DS_Store"

# Confirm it exists
ls -lh "{BRAND_SLUG}-brand-kit.zip"
```

**Tell the user the exact path to the zip file** so they can find it immediately.

### Final Summary to User

Present a clear, friendly delivery message:

```
✅  Your brand kit is ready!

📦  ZIP: {OUTPUT_DIR}/{BRAND_SLUG}-brand-kit.zip
🌐  Preview: Open {BRAND_NAME}-Brand-Kit/index.html in a browser

What's inside ({N} files):
  • {N} logos & combination marks (SVG + PNG + PDF)
  • {N} icons (favicon, PWA, iOS, Android, desktop)
  • {N} social & marketing assets
  • {N} backgrounds & brand patterns
  • {N} fonts (TTF + WOFF2)
  • Interactive brand showcase (index.html)
  • Full brand guidelines (BRAND-GUIDELINES.md)

To regenerate assets:
  cd "{BRAND_NAME}-Brand-Kit/scripts"
  python3 generate_masters.py && python3 generate_wordmark.py && ...

Known caveats:
  • CMYK values are approximations (use a print specialist for offset printing)
  • macOS .icns requires Xcode iconutil (documented in BRAND-GUIDELINES.md)
  • Trademark availability has NOT been verified — check before filing
```

---

## Implementation Notes & Quality Standards

### Python Script Standards

Every Python script must:
- Begin with a docstring describing its purpose and run instructions
- Define all brand constants (colors, dimensions) at the top in a clearly labeled block
- Use only `cairosvg`, `Pillow`, and `fonttools` as external dependencies
- Write to paths derived from the script's own `__file__` location (never hardcode absolute paths)
- Print a progress message for each file written
- Handle missing dependency gracefully with an informative error message

### SVG Quality Standards

Every SVG file must:
- Have a `viewBox` attribute
- Use no external `href` or `url()` dependencies
- Render identically at any scale (all geometry is relative to the viewBox)
- Be valid, parseable XML

### Logo Design Quality Bar

- The symbol must be **completely original** — not a reskin of an emoji, not a clip-art shape
- The wordmark modification must look intentional, not like a typographic error
- Every lockup must have correct optical centering (not mathematical centering — the eye perceives weight differently)
- The favicon variant must be clearly readable at 32×32 and recognizable at 16×16

### Naming Conventions

All file names follow:
```
{mark-type}-{variant}[-{size-or-context}].{ext}
```
Examples: `symbol-full-color.svg`, `lockup-horizontal-dark-bg-1024.png`, `wordmark-ink.svg`

Platform-specific icons follow their platform's required naming (documented in README).

---

## Dependency Installation

```bash
pip install cairosvg pillow fonttools --break-system-packages
```

If `cairosvg` fails to install (requires `libcairo2`):
- **macOS:** `brew install cairo` then retry pip
- **Ubuntu/Debian:** `sudo apt install libcairo2-dev` then retry pip

---

## Confirmation Gate Summary

| Gate | Phase | What to show | What to ask |
|---|---|---|---|
| **Gate 1** | After Phase 1 | Symbol SVG (3 variants: color, mono, reversed) | "Does this symbol capture your brand? Any adjustments?" |
| **Gate 2** | After Phase 2 | Color swatch table + font specimen | "Does this palette and typography feel right?" |
| **Gate 3** | After Phase 4 (optional) | A sample lockup PNG embedded in chat | "Happy with the full lockup before we generate all 200+ assets?" |

Always respect the user's feedback and iterate before moving on. The goal is a brand identity the user is proud of, not just a fast output.
