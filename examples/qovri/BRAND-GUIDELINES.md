# QOVRI Brand Guidelines

Version 1.0 — see `CHANGELOG.md` for revision history.

---

## 1. Brand Overview & Positioning

QOVRI is a premium international digital engineering company: websites,
mobile and desktop applications, custom software, SaaS products, AI
integration, UI/UX, and digital transformation for entrepreneurs, startups,
and enterprises worldwide.

**Positioning:** A premium, forward-thinking digital engineering partner
that transforms ambitious ideas into elegant, reliable, scalable digital
products.

**Tagline:** Engineered for What's Next.

## 2. Mission, Audience, Personality

**Mission:** Transform ideas into powerful, elegant, and scalable digital
solutions through creative design, engineering excellence, and intelligent
technology.

**Audience:** International entrepreneurs, startups, SMBs, and enterprises.

**Personality:** Premium and sophisticated · technically precise · modern
and forward-thinking · minimalist and confident · innovative without being
gimmicky · trustworthy and internationally recognizable.

## 3. The Symbol — "The Open Node"

The standalone mark is a geometric Q built from a 290° precision ring
(evoking a compass arc, a loop, a system boundary) left deliberately open at
the lower right. A diagonal connector bar completes the Q through that
opening and terminates in a small square node — read together as
connection, forward motion, and engineering precision, without resorting to
circuit-board clichés or literal arrows.

- The symbol must always remain recognizable at favicon scale. A dedicated,
  bolder-weight variant (`symbol-favicon-color.svg` / `symbol-favicon-mono.svg`)
  is provided for anything rendered at 32px or below — use it instead of
  scaling down the standard-weight master, which thins out too much at that
  size.
- The ring and the tail may be rendered in two tones (as in the full-color
  version) or as a single flat color (monochrome, black, white) — both are
  equally valid primary treatments.
- Never redraw the ring as a full circle, never close the gap, and never
  detach the node from the tail.

## 4. The Wordmark

Set in **Space Grotesk Bold**, with opened tracking (+28 units) for a more
confident, premium letter-spacing than the typeface's default setting. The
"Q" terminal has been bespoke-modified: the typeface's stock descender was
removed and replaced with a diagonal connector + node in the same geometric
language as the standalone symbol, visually unifying wordmark and symbol as
one system.

**Honesty note:** this is a customization of an existing typeface (tracking,
spacing, and a modified Q terminal), not a fully custom-drawn display face.
Do not describe the wordmark as "custom type" in marketing copy — "a
bespoke QOVRI wordmark" or "modified Space Grotesk" are accurate.

All distributed wordmark files ship as pure vector path outlines (text
converted to paths) — they do not depend on the font being installed on the
viewer's system.

## 5. Logo Variants & When to Use Them

| Variant | File | Use when |
|---|---|---|
| Horizontal lockup, full color | `lockup-horizontal-color.svg` | Default — website headers, docs, most contexts on light backgrounds |
| Horizontal lockup, dark background | `lockup-horizontal-dark-bg.svg` | Placed on Midnight Ink or any dark surface |
| Horizontal lockup, light background | `lockup-horizontal-light-bg.svg` | Placed on Porcelain or white, ink-only treatment |
| Horizontal lockup, tagline | `lockup-horizontal-tagline.svg` | Title slides, splash screens, formal intros |
| Stacked lockup (+ variants) | `lockup-stacked-*.svg` | Square or narrow-width placements: app splash screens, social avatars, narrow sidebars |
| Standalone symbol | `symbol-full-color.svg` | App icons, favicons, compact UI, social avatars, anywhere the wordmark won't fit |
| Wordmark only | `wordmark-*.svg` | Alongside a separately-placed symbol (e.g. symbol as app icon + wordmark in a nav bar), or contexts where a name-only mark is more appropriate than a full lockup |
| Favicon-optimized symbol | `symbol-favicon-color.svg` / `-mono.svg` | 16–48px contexts only |

## 6. Clear Space & Minimum Size

- **Clear space:** maintain a minimum margin around any logo variant equal
  to the height of the node square in that composition (roughly 10% of the
  symbol's height). Do not let text, images, or UI chrome enter this zone.
- **Minimum size, standalone symbol:** 24px digital / 8mm print, using the
  standard-weight master. Below that, switch to the favicon-optimized
  variant, which remains legible down to 16px.
- **Minimum size, horizontal lockup:** 120px wide digital / 25mm print.
- **Minimum size, stacked lockup:** 96px wide digital / 20mm print.

## 7. Correct & Incorrect Usage

**Do:**
- Use the provided color/light/dark variant that matches the background.
- Scale the logo proportionally (lock aspect ratio).
- Give it the clear space defined above.

**Don't:**
- Don't recolor the symbol outside the approved palette.
- Don't close the ring's gap or detach the tail/node.
- Don't stretch, skew, or rotate the lockup.
- Don't place the full-color mark on a busy photographic background without
  a solid-color safe area behind it.
- Don't add drop shadows, bevels, outlines, or 3D effects.
- Don't recreate the wordmark by typing "QOVRI" in plain Space Grotesk — it
  will be missing the modified Q terminal and will look like a typo of the
  real mark.

## 8. Color Palette

### Primary
| Name | Hex | RGB |
|---|---|---|
| Midnight Ink | `#10131B` | 16, 19, 27 |
| Electric Lime | `#C9FF55` | 201, 255, 85 |
| Porcelain | `#F5F7FC` | 245, 247, 252 |

### Supporting / neutral
| Name | Hex | RGB |
|---|---|---|
| Graphite | `#232835` | 35, 40, 53 |
| Muted Slate | `#A8B0C0` | 168, 176, 192 |
| Pure White | `#FFFFFF` | 255, 255, 255 |
| Pure Black | `#000000` | 0, 0, 0 |

### Suggested print conversions (sRGB → CMYK, uncalibrated)
These are starting points derived mathematically from the RGB values above,
**not guaranteed print matches**. Verify against a physical proof with your
chosen printer and substrate before production.

| Name | Suggested CMYK |
|---|---|
| Midnight Ink | 60, 48, 17, 85 |
| Electric Lime | 25, 0, 85, 0 |
| Porcelain | 3, 2, 0, 1 |

The palette was kept to the three primaries from the original creative
brief plus a minimal neutral set — no additional accent colors were
introduced, to keep the system disciplined and legible in black-and-white
reproduction (every lockup has been verified in pure black and pure white;
see `assets/logos/svg/symbol-black.svg` / `symbol-white.svg`).

## 9. Typography

| Role | Typeface | Weight | License |
|---|---|---|---|
| Logo / wordmark | Space Grotesk | Bold (custom Q terminal) | SIL Open Font License 1.1 |
| Headlines | Space Grotesk | Medium / Bold | SIL Open Font License 1.1 |
| Body / UI | Inter | Regular / SemiBold | SIL Open Font License 1.1 |
| Technical docs | Inter | Regular | SIL Open Font License 1.1 |

Both typefaces are sourced from Google Fonts' official open-source
repository and are free for commercial use, embedding, and modification
under the OFL. Full license text is included at `assets/fonts/OFL-*.txt`
and in `LICENSES.md`. `.ttf` and `.woff2` files are both provided.

## 10. Backgrounds & Contrast Rules

- Full-color mark → use on Porcelain, white, or light neutral photography
  with sufficient contrast.
- Light/reversed mark (Porcelain + Lime) → use on Midnight Ink, Graphite, or
  dark photography.
- Never place the full-color mark directly on Electric Lime — use the
  all-Ink monochrome symbol on lime instead (see `symbol-on-lime.svg`) so
  the lime tail doesn't disappear into the lime background.
- Minimum contrast: the ring color must maintain at least a 4.5:1 contrast
  ratio against its background (WCAG AA for graphical objects); all shipped
  variants meet this against their intended background.

## 11. Icon & Favicon Usage

- Browser tab favicon: `assets/icons/favicon/favicon.ico` (multi-size) or
  `favicon.svg` (modern browsers).
- PWA: use `site.webmanifest` as provided; it references both standard and
  maskable icons.
- Do not substitute the standard-weight symbol into favicon slots — always
  use the favicon-optimized master.

## 12. Social Media & Document Applications

See `assets/social/` for ready-made avatar, cover, Open Graph, business
card, email signature, and document-header assets. Use the symbol alone for
anything square/compact (avatars), and the horizontal lockup for anything
wide (covers, headers, signatures).

## 13. Recommended Export Formats

| Use case | Format |
|---|---|
| Web (crisp at any size) | SVG |
| Web (raster, transparent) | PNG |
| Print / professional sharing | PDF |
| App icons (platform-specific) | PNG, ICO, Xcode asset catalog, Android resources |

## 14. File-Naming Conventions

`<mark-type>-<variant>[-<size-or-context>].<ext>`, e.g.
`symbol-full-color.svg`, `lockup-horizontal-dark-bg-1024.png`,
`wordmark-ink.svg`. Platform-specific bundles (iOS, Android) follow each
platform's own required naming conventions instead (documented in
`README.md`).

## 15. Asset Regeneration Instructions

All raster, favicon, PWA, platform-icon, social, and pattern assets are
**derived** from the SVG masters in `assets/logos/svg/` by the scripts in
`scripts/`. Never hand-edit a derived PNG/ICO/PDF — edit the SVG master (or
the generator script that builds it) and re-run the pipeline. See
`README.md` → "Regenerating assets" for exact commands.

## 16. Accessibility Considerations

- All lockups have been checked for 4.5:1 minimum contrast against their
  intended background (see §10).
- The identity does not rely on color alone to convey meaning — the
  monochrome, black, and white variants are equally legible and the "Q"
  reads correctly in silhouette.
- Body copy uses Inter, chosen in part for its high legibility at small
  sizes and extensive language/diacritic coverage.
- No animation or motion is required to recognize the mark.

## 17. Known Limitations & Outstanding Verification Tasks

- **Trademark/brand clearance:** a preliminary web search for "QOVRI" during
  this project turned up no identical company or product name. The closest
  phonetic neighbors found were unrelated companies with different
  spellings (e.g. Qorvo, a semiconductor company; Qoview, registered for
  household goods; Qovia, a VoIP company; Quovantis, a software company).
  **This is not a legal clearance.** Before launch, commission a proper
  trademark search and registrability opinion from a qualified attorney in
  every jurisdiction you intend to operate in.
- **Domain availability** was not purchased or verified beyond informal
  search; check and register your preferred TLDs before launch.
- **macOS `.icns` file** could not be compiled in this Linux build
  environment (no `iconutil`/`png2icns` available). A complete, correctly
  named `.iconset` source folder is provided at
  `assets/icons/desktop/qovri.iconset/` — run
  `iconutil -c icns qovri.iconset` on macOS to produce `qovri.icns`.
- **Print CMYK values** are mathematical conversions, not press-verified —
  proof physically before high-volume print runs.
- **Font embedding in PDF exports**: the logo PDFs contain vector paths
  only (text already converted to outlines), so no font embedding or
  licensing concern applies to those files specifically; the separate
  `.ttf`/`.woff2` files in `assets/fonts/` carry their own OFL terms (see
  `LICENSES.md`).
