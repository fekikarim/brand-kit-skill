#!/usr/bin/env python3
"""
QOVRI Brand Kit — Combination Mark (Lockup) Generator
Composites the standalone symbol with the wordmark into horizontal and
stacked lockups, in full-color, light, dark, and tagline variants.
Reads the already-generated symbol/wordmark SVG masters and recombines
their inner markup, so geometry always stays in sync with the sources.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG_DIR = os.path.join(ROOT, "assets", "logos", "svg")

INK = "#10131B"
LIME = "#C9FF55"
PORCELAIN = "#F5F7FC"
WHITE = "#FFFFFF"
BLACK = "#000000"
SLATE = "#A8B0C0"


def read_inner(fname):
    with open(os.path.join(SVG_DIR, fname)) as f:
        content = f.read()
    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)">(.*)</svg>', content, re.S)
    vb_w, vb_h, inner = float(m.group(1)), float(m.group(2)), m.group(3)
    return inner, vb_w, vb_h


def write(name, content):
    path = os.path.join(SVG_DIR, name)
    with open(path, "w") as f:
        f.write(content)
    print("wrote", os.path.relpath(path, ROOT))


def horizontal_lockup(symbol_file, wordmark_file, bg=None, bg_pad=0, rounded=False, tagline=False, tagline_color=None):
    sym_inner, sym_w, sym_h = read_inner(symbol_file)
    word_inner, word_w, word_h = read_inner(wordmark_file)

    target_sym_h = 220
    scale_sym = target_sym_h / sym_h
    scale_word = target_sym_h * 0.82 / word_h  # wordmark cap-height slightly under symbol height optically

    gap = 48
    sym_render_w = sym_w * scale_sym
    word_render_w = word_w * scale_word

    content_w = sym_render_w + gap + word_render_w
    content_h = target_sym_h

    pad = 36
    total_w = content_w + pad * 2
    total_h = content_h + pad * 2

    tagline_block = ""
    if tagline:
        total_h += 60
        tagline_block = (
            f'<text x="{pad + sym_render_w + gap}" y="{pad + content_h + 46}" '
            f'font-family="Inter SemiBold" font-size="30" letter-spacing="3" '
            f'fill="{tagline_color or SLATE}">ENGINEERED FOR WHAT\'S NEXT</text>'
        )

    bg_rect = ""
    if bg:
        rx = 28 if rounded else 0
        bg_rect = f'<rect x="0" y="0" width="{total_w:.1f}" height="{total_h:.1f}" rx="{rx}" fill="{bg}"/>'

    sym_y = pad + (content_h - sym_render_w / sym_w * sym_h) / 2 if False else pad
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w:.1f} {total_h:.1f}">'
        f'{bg_rect}'
        f'<g transform="translate({pad},{pad}) scale({scale_sym})">{sym_inner}</g>'
        f'<g transform="translate({pad + sym_render_w + gap},{pad + (content_h - word_h*scale_word)/2}) scale({scale_word})">{word_inner}</g>'
        f'{tagline_block}'
        f'</svg>'
    )
    return svg


def stacked_lockup(symbol_file, wordmark_file, bg=None, rounded=False, tagline=False, tagline_color=None):
    sym_inner, sym_w, sym_h = read_inner(symbol_file)
    word_inner, word_w, word_h = read_inner(wordmark_file)

    target_sym_h = 260
    scale_sym = target_sym_h / sym_h
    sym_render_w = sym_w * scale_sym

    target_word_w = target_sym_h * 2.6
    scale_word = target_word_w / word_w
    word_render_h = word_h * scale_word
    word_render_w = word_w * scale_word

    gap = 44
    content_w = max(sym_render_w, word_render_w)
    content_h = target_sym_h + gap + word_render_h

    pad = 40
    total_w = content_w + pad * 2
    total_h = content_h + pad * 2

    tagline_block = ""
    if tagline:
        total_h += 56
        tagline_block = (
            f'<text x="{total_w/2:.1f}" y="{pad + content_h + 42}" text-anchor="middle" '
            f'font-family="Inter SemiBold" font-size="26" letter-spacing="3" '
            f'fill="{tagline_color or SLATE}">ENGINEERED FOR WHAT\'S NEXT</text>'
        )

    bg_rect = ""
    if bg:
        rx = 28 if rounded else 0
        bg_rect = f'<rect x="0" y="0" width="{total_w:.1f}" height="{total_h:.1f}" rx="{rx}" fill="{bg}"/>'

    sym_x = pad + (content_w - sym_render_w) / 2
    word_x = pad + (content_w - word_render_w) / 2
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w:.1f} {total_h:.1f}">'
        f'{bg_rect}'
        f'<g transform="translate({sym_x},{pad}) scale({scale_sym})">{sym_inner}</g>'
        f'<g transform="translate({word_x},{pad + target_sym_h + gap}) scale({scale_word})">{word_inner}</g>'
        f'{tagline_block}'
        f'</svg>'
    )
    return svg


# --- Horizontal lockups ------------------------------------------------
write("lockup-horizontal-color.svg", horizontal_lockup("symbol-full-color.svg", "wordmark-ink.svg"))
write("lockup-horizontal-dark-bg.svg", horizontal_lockup("symbol-dark-bg.svg", "wordmark-white.svg", bg=INK, rounded=False))
write("lockup-horizontal-light-bg.svg", horizontal_lockup("symbol-light-bg.svg", "wordmark-ink.svg", bg=PORCELAIN, rounded=False))
write("lockup-horizontal-black.svg", horizontal_lockup("symbol-black.svg", "wordmark-black.svg"))
write("lockup-horizontal-white.svg", horizontal_lockup("symbol-white.svg", "wordmark-white.svg", bg=INK))
write("lockup-horizontal-tagline.svg", horizontal_lockup("symbol-full-color.svg", "wordmark-ink.svg", tagline=True, tagline_color=GRAPHITE if (GRAPHITE := "#232835") else None))

# --- Stacked lockups -----------------------------------------------------
write("lockup-stacked-color.svg", stacked_lockup("symbol-full-color.svg", "wordmark-ink.svg"))
write("lockup-stacked-dark-bg.svg", stacked_lockup("symbol-dark-bg.svg", "wordmark-white.svg", bg=INK))
write("lockup-stacked-light-bg.svg", stacked_lockup("symbol-light-bg.svg", "wordmark-ink.svg", bg=PORCELAIN))
write("lockup-stacked-tagline.svg", stacked_lockup("symbol-full-color.svg", "wordmark-ink.svg", tagline=True))
write("lockup-stacked-white.svg", stacked_lockup("symbol-white.svg", "wordmark-white.svg", bg=INK))
write("lockup-stacked-black.svg", stacked_lockup("symbol-black.svg", "wordmark-black.svg"))

print("Lockup masters generated.")
