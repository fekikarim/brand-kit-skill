<div align="center">

<img src="https://img.shields.io/badge/AI%20Skill-Brand%20Identity%20Kit-6C47FF?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMiAxNWwtNS01IDEuNDEtMS40MUwxMCAxNC4xN2w3LjU5LTcuNTlMMTkgOGwtOSA5eiIvPjwvc3ZnPg==&logoColor=white" alt="Brand Identity Kit Skill"/>

# 🎨 Brand Identity Kit — AI Skill

### *Full end-to-end brand identity system generator for AI coding agents*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Works with Antigravity](https://img.shields.io/badge/Works%20with-Antigravity-6C47FF?style=flat-square)](https://antigravity.dev)
[![Works with Claude](https://img.shields.io/badge/Works%20with-Claude-orange?style=flat-square)](https://claude.ai)
[![Works with Cursor](https://img.shields.io/badge/Works%20with-Cursor-blue?style=flat-square)](https://cursor.sh)
[![Works with any AI IDE](https://img.shields.io/badge/Works%20with-Any%20AI%20IDE-green?style=flat-square)](#-ide-integration-guide)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python&logoColor=white)](https://python.org)

<br/>

> **Give an AI agent a brand description → get a complete, production-ready brand kit zip.**
> Every logo, icon, social asset, font, and guideline — generated and packaged automatically.

<br/>

[**Quick Start**](#-quick-start) · [**What You Get**](#-what-you-get) · [**IDE Guide**](#-ide-integration-guide) · [**Examples**](#-examples) · [**Architecture**](#-architecture)

---

</div>

## ✨ What Is This?

**Brand Identity Kit** is an AI agent skill — a set of structured instructions that teaches any capable AI coding assistant to act as a world-class brand designer. 

You describe your brand in plain language. The AI:

1. 🔍 **Discovers** your brand's personality, audience, and goals through smart questions
2. 🎨 **Designs** a bespoke geometric logo symbol (with your approval)
3. 🎨 **Selects** a color palette + typography system (with your approval)
4. ⚡ **Generates** every deliverable automatically via Python scripts
5. 📦 **Packages** everything into a `{brand-name}-brand-kit.zip` ready to ship

No design software. No subscriptions. No manual work. Pure AI-powered branding.

---

## 🎁 What You Get

A single zip containing **200+ production-ready files**:

<table>
<tr>
<td width="50%">

### 🔷 Logos & Marks
- `symbol-full-color.svg` + 10 variants
- `wordmark-ink.svg` + 4 color variants
- `lockup-horizontal-*.svg` — 6 compositions
- `lockup-stacked-*.svg` — 6 compositions
- PNG exports at 256, 512, 1024, 2048px
- PDF versions for print

### 🔵 Icons
- `favicon.ico` (multi-size: 16–256px)
- `favicon.svg` + PNG set
- `apple-touch-icon.png` (180×180)
- PWA icons — standard + maskable (192 & 512px)
- iOS Xcode asset catalog
- Android adaptive icon drawables (all densities)
- Desktop: `.ico`, Linux PNGs, macOS `.iconset`

</td>
<td width="50%">

### 🟣 Social & Marketing
- `avatar-square-800.png` — universal avatar
- `github-org-avatar-460.png`
- `linkedin-company-logo-300.png`
- `linkedin-cover-1128x191.png`
- `og-preview-1200x630.png` — Open Graph
- `email-signature-logo.svg` + PNG @3×
- `business-card-front.svg` + PNG (300dpi)

### 📐 Backgrounds & Patterns
- Brand pattern tile + tiled sheet
- Presentation background (1920×1080)
- Social square background (1080×1080)
- Website hero background (1920×1080)
- Light & dark flat backgrounds

### 📖 Documentation
- `BRAND-GUIDELINES.md` — full brand manual
- `index.html` — interactive brand showcase
- `CHANGELOG.md`, `LICENSES.md`
- Asset validation script

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Step 1 — Install the skill in your AI IDE

> See the [IDE Integration Guide](#-ide-integration-guide) for your specific tool.

### Step 2 — Install Python dependencies

```bash
pip install cairosvg pillow fonttools
```

> **macOS only:** If `cairosvg` fails, run `brew install cairo` first.  
> **Linux:** `sudo apt install libcairo2-dev` then retry pip.

### Step 3 — Describe your brand to the AI

Simply tell your AI assistant something like:

```
I want to create a brand kit for "NovaSpark" — a fintech startup 
that helps Gen Z manage their investments. Modern, bold, trustworthy 
but not corporate. Output to ~/Desktop/brands/
```

The AI will guide you through the rest. **You'll be asked to approve the logo and colors before 200+ files are generated.**

### Step 4 — Get your zip

After generation, ask the AI:

```
Now zip everything into novaspark-brand-kit.zip
```

---

## 🖥️ IDE Integration Guide

This skill works with **any AI IDE or agent** that can read a markdown instruction file.

<details>
<summary><strong>🟣 Antigravity (AGY) — Native Support</strong></summary>

This skill is natively packaged for Antigravity. Install via:

1. Open the Antigravity Marketplace
2. Search for "brand-identity-kit"
3. Click Install

Or install manually:
```bash
# Clone to your Antigravity skills directory
git clone https://github.com/fekikarim/brand-kit-skill ~/.gemini/config/plugins/brand-kit-skill
```

The skill auto-loads when the `.agents/skills/brand-identity-kit/SKILL.md` path is detected.

</details>

<details>
<summary><strong>🔵 Claude Code</strong></summary>

```bash
# 1. Clone the repo
git clone https://github.com/fekikarim/brand-kit-skill

# 2. Add to your project's CLAUDE.md or reference it in chat:
cat brand-kit-skill/.agents/skills/brand-identity-kit/SKILL.md >> CLAUDE.md

# 3. Or attach the SKILL.md directly in Claude's context:
# "Here are my instructions: [paste SKILL.md content]"
```

**Recommended:** Add to your Claude project's custom instructions:
> "When asked about brand identity or brand kits, follow the instructions in the attached SKILL.md file."

</details>

<details>
<summary><strong>🟡 Cursor</strong></summary>

```bash
# 1. Clone into your project
git clone https://github.com/fekikarim/brand-kit-skill .cursor/brand-kit-skill

# 2. Create or edit .cursor/rules/brand-kit.md
cp brand-kit-skill/.agents/skills/brand-identity-kit/SKILL.md .cursor/rules/brand-kit.mdc
```

Or add to your **Cursor Settings → Rules for AI**:
- Paste the contents of `SKILL.md` into the custom rules box.

</details>

<details>
<summary><strong>🔴 Windsurf (Codeium)</strong></summary>

```bash
# 1. Clone the skill
git clone https://github.com/fekikarim/brand-kit-skill

# 2. Add as a Windsurf instruction
cp brand-kit-skill/.agents/skills/brand-identity-kit/SKILL.md .windsurfrules
```

</details>

<details>
<summary><strong>🟢 GitHub Copilot (VS Code)</strong></summary>

```bash
# 1. Clone the skill
git clone https://github.com/fekikarim/brand-kit-skill

# 2. Add to VS Code workspace instructions
mkdir -p .github
cp brand-kit-skill/.agents/skills/brand-identity-kit/SKILL.md .github/copilot-instructions.md
```

Then reference it in Copilot chat: `#file:.github/copilot-instructions.md`

</details>

<details>
<summary><strong>🤖 Gemini CLI / AI Studio</strong></summary>

```bash
# 1. Clone the skill
git clone https://github.com/fekikarim/brand-kit-skill

# 2. For Gemini CLI, add to your system prompt file:
cat brand-kit-skill/.agents/skills/brand-identity-kit/SKILL.md >> ~/.gemini/SYSTEM.md
```

</details>

<details>
<summary><strong>🌐 Any Other AI (ChatGPT, Mistral, etc.)</strong></summary>

The `SKILL.md` is a plain markdown file — it works as a **system prompt** for any AI:

1. Open `SKILL.md` and copy the full contents
2. Paste it as the **system prompt** or **custom instructions** in your AI tool
3. Start a conversation and describe your brand

</details>

---

## 🔄 The Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│                     BRAND IDENTITY KIT WORKFLOW                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Phase 0 ──▶ Brand Discovery (name, industry, audience, feel)       │
│      ↓                                                              │
│  Phase 1 ──▶ Logo Symbol Design ──▶ 🔒 Gate 1: User Approves Logo   │
│      ↓                                                              │
│  Phase 2 ──▶ Color Palette + Typography ──▶ 🔒 Gate 2: User Approves│
│      ↓                                                              │
│  Phase 3 ──▶ Wordmark Generation (font outlines → vector paths)     │
│      ↓                                                              │
│  Phase 4 ──▶ Full Asset Pipeline (8 Python scripts, 200+ files)     │
│      ↓                                                              │
│  Phase 5 ──▶ Interactive Brand Showcase (index.html)                │
│      ↓                                                              │
│  Phase 6 ──▶ Documentation (Guidelines, Licenses, Changelog)        │
│      ↓                                                              │
│  Phase 7 ──▶ Validation + ZIP Package ✅                            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Human approval is required at Gates 1 and 2** — the AI never proceeds past the logo or color selection without your explicit "looks good." Everything else is automated.

---

## 🏗️ Architecture

### Skill Structure

```
brand-kit-skill/
├── .agents/
│   └── skills/
│       └── brand-identity-kit/
│           ├── SKILL.md                  ← Main AI instruction file (645 lines)
│           └── references/
│               └── architecture.md       ← Code patterns & templates
├── examples/
│   └── novaspark/                        ← Example brand kit output
├── scripts/
│   └── run_brand_kit.sh                  ← Convenience runner script
├── README.md                             ← This file
├── CONTRIBUTING.md
└── LICENSE
```

### Generated Brand Kit Structure

```
{BRAND_NAME}-Brand-Kit/
├── README.md
├── BRAND-GUIDELINES.md
├── LICENSES.md
├── CHANGELOG.md
├── index.html                        ← Interactive brand showcase (open in browser)
├── assets/
│   ├── logos/
│   │   ├── svg/                      ← 20+ vector masters (source of truth)
│   │   ├── png/                      ← Raster exports (256, 512, 1024, 2048px)
│   │   └── pdf/                      ← Print-ready PDFs
│   ├── icons/
│   │   ├── favicon/                  ← favicon.ico, .svg, PNG set, webmanifest
│   │   ├── pwa/                      ← Standard + maskable PWA icons
│   │   ├── ios/                      ← Xcode asset catalog
│   │   ├── android/                  ← Adaptive icon drawables (all densities)
│   │   └── desktop/                  ← .ico, Linux PNGs, macOS .iconset
│   ├── social/                       ← Avatar, OG, LinkedIn, email sig, biz card
│   ├── backgrounds/                  ← Hero, presentation, social backgrounds
│   ├── brand-patterns/               ← Pattern tile + tiled sheets
│   └── fonts/                        ← TTF + WOFF2 + OFL licenses
├── previews/                         ← Contact sheet overview images
└── scripts/
    ├── generate_masters.py           ← Symbol SVG masters (run first)
    ├── generate_wordmark.py          ← Font-outline wordmark
    ├── generate_lockups.py           ← Combination marks
    ├── export_raster.py              ← PNG + PDF from SVGs
    ├── generate_favicons.py          ← Favicon suite
    ├── generate_pwa_icons.py         ← PWA icons
    ├── generate_social_assets.py     ← Social + marketing assets
    ├── generate_patterns.py          ← Backgrounds + brand patterns
    └── validate_assets.py            ← Asset integrity checker
```

---

## 📸 Examples

> *Example brand kits generated with this skill:*

| Brand | Industry | Style | Preview |
|-------|----------|-------|---------|
| **NovaSpark** | Fintech / Gen Z investing | Bold, electric, modern | [View →](examples/novaspark/) |
| *(your brand here)* | *…* | *…* | *Share your result!* |

---

## ⚙️ Python Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `cairosvg` | ≥ 2.7 | SVG → PNG/PDF rasterization |
| `Pillow` | ≥ 10.0 | Image processing, ICO generation |
| `fonttools` | ≥ 4.40 | Font outline extraction for wordmark |

```bash
# Install all at once
pip install cairosvg pillow fonttools

# macOS (if cairosvg fails)
brew install cairo && pip install cairosvg pillow fonttools

# Ubuntu/Debian
sudo apt install libcairo2-dev && pip install cairosvg pillow fonttools

# Windows (use WSL or conda)
conda install -c conda-forge cairo && pip install cairosvg pillow fonttools
```

---

## 🎯 Design Quality Standards

This skill enforces **professional brand design standards**, not just file generation:

- ✅ **WCAG AA contrast** — every color combination is verified (≥ 4.5:1 ratio)
- ✅ **Favicon legibility** — symbol readable at 16×16px (heavier weight variant)
- ✅ **Vector-first** — all logos are path-based SVGs, no font dependencies
- ✅ **Optically balanced** — lockups use optical centering, not mathematical
- ✅ **Platform-correct** — iOS, Android, PWA icons follow each platform's spec
- ✅ **Completely original** — no emoji reskins, no clip-art, bespoke geometry only

---

## 🧑‍💻 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ideas for contributions:
- 🎨 New logo archetype templates
- 📱 Additional social platform formats (TikTok, Bluesky, etc.)
- 🌍 More font pairing suggestions
- 📝 More example brand kits in `examples/`
- 🔧 Platform-specific improvements (macOS `.icns`, Windows installer icons)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

Brand artwork generated by this skill is **your property** — the skill produces original output, not copied or derived works.

Font files downloaded during generation are licensed under the [Open Font License (OFL 1.1)](https://openfontlicense.org/), which allows free commercial use.

---

## 🙏 Credits

Built and maintained by [@fekikarim](https://github.com/fekikarim).  
Architecture inspired by real-world brand identity systems and professional design workflows.

---

<div align="center">

**Made with ❤️ for builders who want beautiful brands**

[⭐ Star this repo](https://github.com/fekikarim/brand-kit-skill) · [🐛 Report a bug](https://github.com/fekikarim/brand-kit-skill/issues) · [💡 Request a feature](https://github.com/fekikarim/brand-kit-skill/issues/new)

</div>
