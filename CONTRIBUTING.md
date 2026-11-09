# Contributing to Brand Identity Kit Skill

Thank you for your interest in contributing! This skill is designed to help AI agents generate professional brand identities, and your contributions help make it better for everyone.

## 🤝 Ways to Contribute

### 1. Share Example Brand Kits
Run the skill and share your result by opening a PR with:
```
examples/{your-brand-name}/
├── README.md           ← brief description of the brand
├── preview.png         ← screenshot of your brand showcase
└── ...                 ← (optional) select assets to showcase
```

### 2. Improve the SKILL.md Instructions
The core skill lives in `.agents/skills/brand-identity-kit/SKILL.md`. Improvements welcome for:
- New logo archetype templates
- Better typography pairings
- Additional social platform formats
- Clearer phase instructions

### 3. Add References
The `references/architecture.md` file contains code patterns. Add:
- New script templates
- Better rasterization approaches
- Platform-specific icon generation patterns

### 4. Report Issues
Open a GitHub Issue describing:
- What IDE/AI you used
- What phase failed or produced unexpected output
- Sample output or error messages

## 📋 Pull Request Guidelines

1. **Keep changes focused** — one improvement per PR
2. **Test the skill end-to-end** — run a complete brand kit generation before submitting
3. **Update the README** if adding new features or integrations
4. **Follow the existing tone** — instructions should be clear, unambiguous, and professional

## 🛠️ Local Development

```bash
# Clone the repo
git clone https://github.com/fekikarim/brand-kit-skill
cd brand-kit-skill

# Install Python dependencies for testing
pip install cairosvg pillow fonttools

# macOS: install cairo if needed
brew install cairo
```

## 📌 Code of Conduct

Be respectful and constructive. This is a tool for creators — keep the focus on helping people build great brands.

## 📬 Contact

Open an issue or reach out via GitHub Discussions.
