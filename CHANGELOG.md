# Changelog

All notable changes to the Brand Identity Kit skill are documented here.

## [1.0.0] — 2026-11-09

### Added
- Initial release of the Brand Identity Kit AI Skill
- Complete 7-phase brand identity generation workflow
- Phase 0: Brand Discovery & Briefing system
- Phase 1: Bespoke geometric logo symbol design with 7 archetype templates
- Phase 2: WCAG AA-verified color palette + typography system
- Phase 3: Font-outline wordmark generation (fonttools-based, no live text)
- Phase 4: Full asset pipeline — 8 Python generation scripts
  - `generate_masters.py` — 11 symbol SVG variants
  - `generate_wordmark.py` — 4 wordmark color variants
  - `generate_lockups.py` — 12 combination mark variants
  - `export_raster.py` — PNG + PDF rasterization
  - `generate_favicons.py` — Complete favicon suite
  - `generate_pwa_icons.py` — Standard + maskable PWA icons
  - `generate_social_assets.py` — 13 social + marketing assets
  - `generate_patterns.py` — 8 backgrounds + brand patterns
- Phase 5: Interactive brand showcase (index.html)
- Phase 6: Documentation suite (BRAND-GUIDELINES.md, README.md, LICENSES.md, CHANGELOG.md)
- Phase 7: Asset validation script + ZIP packaging
- IDE integration support: Antigravity, Claude Code, Cursor, Windsurf, GitHub Copilot, Gemini CLI, any AI
- Universal runner script (`scripts/run_brand_kit.sh`)
- Reference architecture document with code templates
- Example brand kit (NovaSpark)

[1.0.0]: https://github.com/fekikarim/brand-kit-skill/releases/tag/v1.0.0
