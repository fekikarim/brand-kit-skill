#!/usr/bin/env python3
"""
QOVRI Brand Kit — Social Media & Business Asset Generator
Builds platform-sized assets from the vector masters: avatars, OG image,
LinkedIn cover, email signature, business card, document header, GitHub org
avatar, and presentation title-slide logo.
"""
import os
import re
import cairosvg

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG_DIR = os.path.join(ROOT, "assets", "logos", "svg")
SOCIAL_DIR = os.path.join(ROOT, "assets", "social")
os.makedirs(SOCIAL_DIR, exist_ok=True)

INK = "#10131B"
LIME = "#C9FF55"
PORCELAIN = "#F5F7FC"
SLATE = "#A8B0C0"
GRAPHITE = "#232835"


def inner_of(fname):
    with open(os.path.join(SVG_DIR, fname)) as f:
        content = f.read()
    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)">(.*)</svg>', content, re.S)
    return m.group(3), float(m.group(1)), float(m.group(2))


def save(name, svg, width, height=None):
    path = os.path.join(SOCIAL_DIR, name)
    cairosvg.svg2png(url=None, bytestring=svg.encode(), write_to=path,
                      output_width=width, output_height=height)
    print("wrote", os.path.relpath(path, ROOT))


def save_svg(name, svg):
    path = os.path.join(SOCIAL_DIR, name)
    with open(path, "w") as f:
        f.write(svg)
    print("wrote", os.path.relpath(path, ROOT))


sym_inner, sym_w, sym_h = inner_of("symbol-full-color.svg")
word_inner, word_w, word_h = inner_of("wordmark-white.svg")
word_ink_inner, _, _ = inner_of("wordmark-ink.svg")

# -----------------------------------------------------------------------
# 1. Square social avatar (symbol only, on brand ink, rounded) — 800x800
# -----------------------------------------------------------------------
scale = 0.56
size = 800
sym_size = size * scale
off = (size - sym_size) / 2
avatar_svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}">'
    f'<rect width="{size}" height="{size}" fill="{INK}"/>'
    f'<g transform="translate({off:.1f},{off:.1f}) scale({sym_size/200:.4f})">{sym_inner.replace(INK, PORCELAIN)}</g>'
    f'</svg>'
)
save("avatar-square-800.png", avatar_svg, 800)

# -----------------------------------------------------------------------
# 2. GitHub organization avatar — same composition, 460x460 (GitHub's
#    recommended minimum), also provided as SVG source
# -----------------------------------------------------------------------
save_svg("github-org-avatar.svg", avatar_svg)
save("github-org-avatar-460.png", avatar_svg, 460)

# -----------------------------------------------------------------------
# 3. LinkedIn company logo (square, 300x300 minimum) — symbol on white
#    per LinkedIn's guidance to avoid dark squares blending into the UI
# -----------------------------------------------------------------------
li_logo_svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300">'
    f'<rect width="300" height="300" fill="{PORCELAIN}"/>'
    f'<g transform="translate({300*(1-scale)/2:.1f},{300*(1-scale)/2:.1f}) scale({300*scale/200:.4f})">'
    f'{sym_inner.replace(INK, INK)}</g></svg>'
)
save("linkedin-company-logo-300.png", li_logo_svg, 300)

# -----------------------------------------------------------------------
# 4. LinkedIn company cover image — 1128x191
# -----------------------------------------------------------------------
cw, ch = 1128, 191
sym_h_cover = ch * 0.62
sym_scale = sym_h_cover / sym_w  # symbol is square so w==h basis
word_scale = (ch * 0.42) / word_h
word_w_r = word_w * word_scale
sym_w_r = sym_w * sym_scale
gap = 36
content_w = sym_w_r + gap + word_w_r
start_x = (cw - content_w) / 2
cover_svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {cw} {ch}">'
    f'<rect width="{cw}" height="{ch}" fill="{INK}"/>'
    f'<g transform="translate({start_x:.1f},{(ch-sym_h_cover)/2:.1f}) scale({sym_scale:.4f})">{sym_inner.replace(INK, PORCELAIN)}</g>'
    f'<g transform="translate({start_x+sym_w_r+gap:.1f},{(ch-word_scale*word_h)/2:.1f}) scale({word_scale:.4f})">{word_inner}</g>'
    f'<text x="{cw/2}" y="{ch-18}" text-anchor="middle" font-family="Inter SemiBold" font-size="16" letter-spacing="2" fill="{SLATE}">ENGINEERED FOR WHAT\'S NEXT</text>'
    f'</svg>'
)
save("linkedin-cover-1128x191.png", cover_svg, cw, ch)

# -----------------------------------------------------------------------
# 5. Open Graph / general social sharing image — 1200x630
# -----------------------------------------------------------------------
ogw, ogh = 1200, 630
sym_size_og = 260
word_scale_og = 380 / word_w
word_h_og = word_h * word_scale_og
total_h = sym_size_og + 40 + word_h_og
top = (ogh - total_h) / 2
og_svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ogw} {ogh}">'
    f'<rect width="{ogw}" height="{ogh}" fill="{INK}"/>'
    f'<g transform="translate({(ogw-sym_size_og)/2:.1f},{top:.1f}) scale({sym_size_og/200:.4f})">{sym_inner.replace(INK, PORCELAIN)}</g>'
    f'<g transform="translate({(ogw-380)/2:.1f},{top+sym_size_og+40:.1f}) scale({word_scale_og:.4f})">{word_inner}</g>'
    f'<text x="{ogw/2}" y="{ogh-50}" text-anchor="middle" font-family="Inter SemiBold" font-size="20" letter-spacing="3" fill="{SLATE}">ENGINEERED FOR WHAT\'S NEXT</text>'
    f'</svg>'
)
save("og-preview-1200x630.png", og_svg, ogw, ogh)

# -----------------------------------------------------------------------
# 6. Email signature logo — compact horizontal, transparent, small
# -----------------------------------------------------------------------
sig_h = 60
sym_scale_sig = sig_h / sym_w
word_scale_sig = (sig_h * 0.78) / word_h
sym_w_sig = sym_w * sym_scale_sig
word_w_sig = word_w * word_scale_sig
gap_sig = 14
total_w_sig = sym_w_sig + gap_sig + word_w_sig
sig_svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w_sig:.1f} {sig_h}">'
    f'<g transform="scale({sym_scale_sig:.4f})">{sym_inner}</g>'
    f'<g transform="translate({sym_w_sig+gap_sig:.1f},{(sig_h-word_h*word_scale_sig)/2:.1f}) scale({word_scale_sig:.4f})">{word_ink_inner}</g>'
    f'</svg>'
)
save_svg("email-signature-logo.svg", sig_svg)
save("email-signature-logo.png", sig_svg, int(total_w_sig * 3), sig_h * 3)

# -----------------------------------------------------------------------
# 7. Document / report header logo — horizontal, ink-on-transparent
# -----------------------------------------------------------------------
doc_h = 90
sym_scale_doc = doc_h / sym_w
word_scale_doc = (doc_h * 0.75) / word_h
sym_w_doc = sym_w * sym_scale_doc
word_w_doc = word_w * word_scale_doc
gap_doc = 22
total_w_doc = sym_w_doc + gap_doc + word_w_doc
doc_svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w_doc:.1f} {doc_h}">'
    f'<g transform="scale({sym_scale_doc:.4f})">{sym_inner}</g>'
    f'<g transform="translate({sym_w_doc+gap_doc:.1f},{(doc_h-word_h*word_scale_doc)/2:.1f}) scale({word_scale_doc:.4f})">{word_ink_inner}</g>'
    f'</svg>'
)
save_svg("document-header-logo.svg", doc_svg)
save("document-header-logo.png", doc_svg, int(total_w_doc * 3), doc_h * 3)

# -----------------------------------------------------------------------
# 8. Presentation title-slide logo — stacked, for dark slide background
# -----------------------------------------------------------------------
stacked_inner, stacked_w, stacked_h = inner_of("lockup-stacked-dark-bg.svg")
save("presentation-title-slide-logo.png", open(os.path.join(SVG_DIR, "lockup-stacked-dark-bg.svg")).read(), 900)

# -----------------------------------------------------------------------
# 9. Business card artwork — print-ready layout, 3.5in x 2in @ 300dpi
#    (1050x600px), front face, CMYK-documented in guidelines (sRGB source)
# -----------------------------------------------------------------------
card_w, card_h = 1050, 600
card_sym_scale = 110 / sym_w
card_word_target_w = 420
card_word_scale = card_word_target_w / word_w
card_svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {card_w} {card_h}">'
    f'<rect width="{card_w}" height="{card_h}" fill="{INK}"/>'
    f'<g transform="translate(70,70) scale({card_sym_scale:.4f})">{sym_inner.replace(INK, PORCELAIN)}</g>'
    f'<g transform="translate(70,230) scale({card_word_scale:.4f})">{word_inner}</g>'
    f'<text x="70" y="430" font-family="Inter Regular" font-size="22" fill="{SLATE}">Engineered for What\'s Next</text>'
    f'<line x1="70" y1="470" x2="{card_w-70}" y2="470" stroke="{GRAPHITE}" stroke-width="1.5"/>'
    f'<text x="70" y="510" font-family="Inter SemiBold" font-size="24" fill="{PORCELAIN}">Jordan Avery</text>'
    f'<text x="70" y="540" font-family="Inter Regular" font-size="18" fill="{SLATE}">Partnerships Lead</text>'
    f'<text x="{card_w-70}" y="510" text-anchor="end" font-family="Inter Regular" font-size="18" fill="{SLATE}">hello@qovri.com</text>'
    f'<text x="{card_w-70}" y="540" text-anchor="end" font-family="Inter Regular" font-size="18" fill="{SLATE}">qovri.com</text>'
    f'</svg>'
)
save("business-card-front-1050x600.png", card_svg, card_w, card_h)
save_svg("business-card-front.svg", card_svg)

print("Social and business assets generated.")
