# QOVRI Brand Kit

Complete visual identity system for **QOVRI** — digital engineering,
software, and AI-powered products. "Engineered for What's Next."

Open `index.html` directly in a browser for an interactive showcase of
every asset in this kit, or browse the directories below.

## Directory Structure

```
QOVRI-Brand-Kit/
├── README.md                   ← you are here
├── BRAND-GUIDELINES.md         ← full brand manual
├── LICENSES.md                 ← font & asset licensing
├── CHANGELOG.md
├── index.html                  ← interactive brand showcase (open locally)
├── assets/
│   ├── logos/
│   │   ├── svg/                ← vector masters (source of truth)
│   │   ├── png/                ← raster exports, transparent, multiple sizes
│   │   └── pdf/                ← vector PDF exports for sharing/print
│   ├── icons/
│   │   ├── favicon/            ← favicon.ico, favicon.svg, manifest
│   │   ├── web/                ← icon-192.png, icon-512.png
│   │   ├── pwa/                ← standard + maskable PWA icons
│   │   ├── ios/                ← Xcode asset catalog
│   │   ├── android/            ← adaptive icon resources
│   │   └── desktop/            ← Windows .ico, Linux PNGs, macOS .iconset
│   ├── social/                 ← avatars, covers, OG image, business card, etc.
│   ├── backgrounds/            ← presentation / hero / social backgrounds
│   ├── brand-patterns/         ← subtle ring-motif pattern tile + sheet
│   └── fonts/                  ← Space Grotesk & Inter, .ttf + .woff2 + OFL licenses
├── scripts/                    ← the full regeneration + validation pipeline
└── previews/                   ← overview contact-sheet images
```

## Asset Categories at a Glance

- **Logos** (`assets/logos/`): the symbol ("The Open Node"), the wordmark
  (customized Space Grotesk Bold with a bespoke Q terminal), and horizontal
  / stacked combination lockups — each in full-color, light-background,
  dark-background, black, white, and (where applicable) tagline variants.
- **Icons** (`assets/icons/`): everything needed to ship an app icon or
  favicon on every major platform.
- **Social** (`assets/social/`): ready-sized assets for avatars, covers,
  link previews, email signatures, documents, and business cards.
- **Backgrounds & patterns**: restrained, logo-geometry-derived surfaces for
  presentations, social posts, and website heroes.
- **Fonts**: the two typefaces used across the system, as real font files
  with their open-source licenses.

## Recommended Logo Variant by Use Case

| Use case | Recommended file |
|---|---|
| Website header (light background) | `assets/logos/svg/lockup-horizontal-color.svg` |
| Website header (dark/footer) | `assets/logos/svg/lockup-horizontal-dark-bg.svg` |
| App icon / favicon | `assets/icons/favicon/favicon.svg` or the platform package in `assets/icons/` |
| Social avatar | `assets/social/avatar-square-800.png` |
| Slide deck title slide | `assets/logos/svg/lockup-stacked-dark-bg.svg` or `assets/social/presentation-title-slide-logo.png` |
| Printed document header | `assets/social/document-header-logo.svg` |
| Email signature | `assets/social/email-signature-logo.svg` |

## Favicon Installation

Copy `assets/icons/favicon/*` and `assets/icons/web/*` to your site root (or
adjust paths below to wherever you host them), then add to your HTML
`<head>`:

```html
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#10131B">
```

(`favicon.ico` is also included and will be picked up automatically by
browsers that look for `/favicon.ico` with no `<link>` tag at all.)

## Web / PWA Integration

`assets/icons/favicon/site.webmanifest` already references the standard and
maskable PWA icons in `assets/icons/pwa/`. Update the `icons[].src` paths to
match wherever you deploy the `assets/` folder, then link the manifest as
shown above.

## iOS Integration

1. Drag `assets/icons/ios/Assets.xcassets/AppIcon.appiconset` into your
   Xcode project's `Assets.xcassets` (or replace your existing `AppIcon`
   appiconset with it).
2. The appiconset uses the modern single-size **universal** 1024×1024
   configuration — Xcode 14+ generates all device-specific sizes from it
   automatically. If you're on an older Xcode that requires explicit
   per-size slots, re-export from `assets/icons/ios/AppIcon-1024.png` using
   Xcode's "New iOS App Icon" asset and Apple's current size table.

## Android Integration

1. Copy the `drawable-*dpi/` folders from `assets/icons/android/` into your
   project's `app/src/main/res/`.
2. Copy `mipmap-anydpi-v26/ic_launcher.xml` and `ic_launcher_round.xml` into
   `app/src/main/res/mipmap-anydpi-v26/`.
3. Copy `values/ic_launcher_background.xml` into `app/src/main/res/values/`.
4. For apps still supporting pre-API-26 devices, also copy the per-density
   PNGs from `assets/icons/android/legacy/mipmap-*/` into
   `app/src/main/res/mipmap-*/`.
5. Reference `@mipmap/ic_launcher` and `@mipmap/ic_launcher_round` in your
   `AndroidManifest.xml` as usual.

## Desktop Integration

- **Windows**: use `assets/icons/desktop/qovri.ico` directly (embedded
  sizes: 16/24/32/48/64/128/256px).
- **Linux**: install the PNGs under `assets/icons/desktop/linux/<size>/` into
  your platform's `hicolor` icon theme path (e.g.
  `/usr/share/icons/hicolor/<size>/apps/qovri.png`), or point an Electron
  `BrowserWindow`'s `icon` option at the 512px PNG directly.
- **macOS**: a ready `assets/icons/desktop/qovri.iconset/` folder is
  included with all required sizes correctly named. On a Mac, run:
  ```bash
  iconutil -c icns assets/icons/desktop/qovri.iconset -o assets/icons/desktop/qovri.icns
  ```
  This step could not be performed in the Linux environment this kit was
  built in (no `iconutil` available) — see `BRAND-GUIDELINES.md` §17.
- **Electron**: point `icon:` in your `BrowserWindow`/builder config at
  `qovri.ico` (Windows), `qovri.icns` (macOS, once compiled), and the 512px
  Linux PNG.

## Social Media Asset Recommendations

| Platform | Asset |
|---|---|
| GitHub org avatar | `assets/social/github-org-avatar-460.png` |
| LinkedIn company logo | `assets/social/linkedin-company-logo-300.png` |
| LinkedIn cover image | `assets/social/linkedin-cover-1128x191.png` |
| X / general social avatar | `assets/social/avatar-square-800.png` |
| Link previews (Open Graph) | `assets/social/og-preview-1200x630.png` |

## Regenerating Assets

All derived assets are generated from the SVG masters by Python scripts.
From `scripts/`, with Python 3.9+ and the dependencies below installed, run
in this order:

```bash
pip install cairosvg pillow fonttools --break-system-packages   # if not already installed

python3 generate_masters.py       # symbol SVG masters
python3 generate_wordmark.py      # wordmark SVG (paths, from font outlines)
python3 generate_lockups.py       # horizontal/stacked combination marks
python3 export_raster.py          # PNG + PDF exports of all logo masters
python3 generate_favicons.py      # favicon.ico/.svg, apple-touch-icon, web icons
python3 generate_pwa_icons.py     # standard + maskable PWA icons
python3 generate_social_assets.py # avatars, covers, OG image, business card, etc.
python3 generate_patterns.py      # backgrounds + brand pattern
```

(The Android drawable/mipmap PNGs and iOS catalog were produced by
one-off generation steps during this kit's creation rather than a single
script; see the inline comments in `generate_pwa_icons.py` for the pattern
used, which is straightforward to extend if you change the source symbol.)

## Validating Assets

```bash
python3 validate-assets.py
```

This parses every SVG and XML/JSON file, decodes every PNG and checks its
dimensions, and confirms the `.ico` files contain genuine multi-size
bitmaps rather than a single renamed PNG. It exits non-zero if any check
fails.

## Required Software & Dependencies

- Python 3.9+
- `cairosvg`, `Pillow`, `fonttools` (Python packages)
- No Node.js, Inkscape, or ImageMagick-with-rsvg dependency is required —
  the whole pipeline runs on the above three packages.
- macOS `.icns` compilation requires `iconutil` (macOS only, ships with
  Xcode Command Line Tools).

## Known Platform-Specific Limitations

- macOS `.icns` is not pre-compiled in this kit (see above) — source
  `.iconset` is provided.
- The iOS asset catalog uses the modern single-size (1024px universal)
  configuration; projects targeting very old Xcode versions that require
  explicit per-size icon slots will need to re-export those sizes.
- Print CMYK values in `BRAND-GUIDELINES.md` are calculated conversions, not
  press-proofed.

## Licensing Notes

- **The QOVRI symbol, wordmark, and all composed lockups** are original
  artwork created for this project. See `LICENSES.md` for how you may use
  them.
- **Space Grotesk** and **Inter** are licensed under the SIL Open Font
  License 1.1 (full text in `assets/fonts/`), which permits embedding,
  modification, and commercial use.

## Trademark & Domain Verification Disclaimer

"QOVRI" is a proposed brand name. It has **not** been legally registered,
trademark-cleared, or confirmed available as a domain in any jurisdiction.
A preliminary web search turned up no identical existing company or product
(see `BRAND-GUIDELINES.md` §17 for details and sources). This is not a
substitute for a formal trademark clearance search — consult a qualified
attorney and register your domains before launch.
