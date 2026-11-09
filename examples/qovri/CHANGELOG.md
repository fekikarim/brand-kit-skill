# Changelog

## 1.0.0 — Initial Release

Complete first release of the QOVRI brand identity system.

**Added**
- Symbol ("The Open Node"): standalone geometric Q mark in full-color,
  light/dark-background, black, white, monochrome-lime, and reversed
  treatments, plus a favicon-optimized bolder variant for small-size use.
- Wordmark: Space Grotesk Bold converted to vector paths with custom
  tracking and a bespoke modified Q terminal matching the symbol's
  language. Ink, black, white, and lime color variants.
- Combination lockups: horizontal and stacked, each in full-color,
  light-background, dark-background, black, white, and tagline variants.
- Full raster export set: PNG (256/512/1024/2048 for marks, proportional
  widths for wide lockups) and PDF for every logo variant.
- Favicon package: `favicon.ico` (7 embedded sizes), `favicon.svg`, PNG
  favicons (16/32/48), `apple-touch-icon.png`, `site.webmanifest`.
- PWA icons: standard and maskable, 192 and 512px, with verified safe-zone
  artwork for the maskable set.
- iOS asset catalog (`Assets.xcassets/AppIcon.appiconset`) using the
  modern universal 1024px configuration.
- Android adaptive icon resources: foreground, background, and monochrome
  (themed-icon) drawables across all five density buckets, adaptive-icon
  XML, and legacy pre-API-26 launcher PNGs.
- Desktop icons: Windows `.ico` (7 sizes), Linux hicolor PNGs (9 sizes),
  and a macOS `.iconset` source folder (requires `iconutil` on macOS to
  compile to `.icns` — not available in this build environment).
- Social and business assets: square avatar, GitHub org avatar, LinkedIn
  company logo and cover, Open Graph preview, email signature, document
  header, presentation title slide, and business card.
- Brand patterns and backgrounds derived from the symbol's own ring
  geometry: primary light/dark, a tileable ring-motif pattern, and
  presentation/social/website-hero background variants.
- Typography system: Space Grotesk (logo/headlines) + Inter (body/UI),
  sourced from Google Fonts under the SIL Open Font License, with static
  weight instances and WOFF2 conversions included.
- Full documentation: `README.md`, `BRAND-GUIDELINES.md`, `LICENSES.md`.
- Interactive local HTML brand showcase (`index.html`).
- Asset generation pipeline (`scripts/generate_*.py`) and a real validation
  script (`scripts/validate-assets.py`) that parses/decodes every shipped
  file rather than assuming correctness.

**Known limitations at this release**
- `.icns` not pre-compiled (no macOS tooling in build environment).
- Print CMYK values are calculated, not press-proofed.
- Trademark/domain availability is preliminary and non-legal — see
  `BRAND-GUIDELINES.md` §17.
