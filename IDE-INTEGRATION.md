# Universal Brand Kit Skill — IDE Integration Guide

This file documents how to use the brand-identity-kit skill with any AI IDE.

## Quick Reference

| IDE | Method | Config file |
|-----|--------|------------|
| **Antigravity (AGY)** | Native skill loading | `.agents/skills/*/SKILL.md` |
| **Claude Code** | Paste into CLAUDE.md | `CLAUDE.md` |
| **Cursor** | Add to .cursor/rules | `.cursor/rules/brand-kit.mdc` |
| **Windsurf** | Add to .windsurfrules | `.windsurfrules` |
| **GitHub Copilot** | Workspace instructions | `.github/copilot-instructions.md` |
| **Gemini CLI** | System prompt file | `~/.gemini/SYSTEM.md` |
| **Any Chat AI** | Paste as system prompt | (chat interface) |

## Skill Activation Phrases

After installing, trigger the skill with any of these:

```
Create a brand kit for [brand name]
I need a full brand identity for [brand name]
Generate a brand kit — [brand description]
Brand identity system for [brand name]: [description]
```

## What the AI Will Do

1. Ask clarifying questions about your brand (or extract from your description)
2. Show you a logo symbol design → **wait for your approval**
3. Propose colors + typography → **wait for your approval**
4. Generate all 200+ files via Python scripts
5. Validate all assets
6. Package everything into a zip

## Requirements

- Python 3.9+
- `pip install cairosvg pillow fonttools`
- macOS: `brew install cairo` (if cairosvg fails)
- Linux: `sudo apt install libcairo2-dev` (if cairosvg fails)
