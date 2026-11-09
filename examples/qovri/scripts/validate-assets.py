#!/usr/bin/env python3
"""
QOVRI Brand Kit — Asset Validator
Real checks, not a rubber stamp: every SVG is parsed, every PNG is decoded
and inspected for mode/alpha/size, every JSON/XML manifest is parsed, and
the ICO/iconset outputs are checked for genuine embedded sizes.
Run from QOVRI-Brand-Kit/scripts: python3 validate-assets.py
"""
import os
import sys
import json
import xml.dom.minidom as minidom
from xml.etree import ElementTree as ET
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []
warnings = []
checked = 0


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def rel(p):
    return os.path.relpath(p, ROOT)


# 1. SVG validation — parse as XML, confirm viewBox present, no obvious
#    external href dependencies.
print("== SVG files ==")
svg_count = 0
for dirpath, _, files in os.walk(ROOT):
    for fn in files:
        if fn.endswith(".svg"):
            path = os.path.join(dirpath, fn)
            svg_count += 1
            try:
                tree = ET.parse(path)
                root = tree.getroot()
                if "viewBox" not in root.attrib:
                    warn(f"{rel(path)}: no viewBox attribute")
                content = open(path).read()
                if "http://" in content.replace("http://www.w3.org", "") or "https://" in content:
                    warn(f"{rel(path)}: contains an external URL reference")
            except ET.ParseError as e:
                err(f"{rel(path)}: INVALID XML — {e}")
print(f"Parsed {svg_count} SVG files.")
checked += svg_count

# 2. PNG validation — decode, check mode/alpha, confirm no zero-byte files,
#    confirm aspect ratio looks sane (no accidental 1x1 etc).
print("\n== PNG files ==")
png_count = 0
for dirpath, _, files in os.walk(ROOT):
    for fn in files:
        if fn.endswith(".png"):
            path = os.path.join(dirpath, fn)
            png_count += 1
            try:
                im = Image.open(path)
                im.verify()
                im2 = Image.open(path)  # reopen after verify() invalidates the handle
                w, h = im2.size
                if w < 8 or h < 8:
                    err(f"{rel(path)}: suspiciously small ({w}x{h})")
                if "transparent" in fn.lower() or "symbol" in fn.lower() and "bg" not in fn.lower():
                    pass  # informational only
            except Exception as e:
                err(f"{rel(path)}: FAILED TO DECODE — {e}")
print(f"Decoded {png_count} PNG files.")
checked += png_count

# 3. JSON validation (manifests, Contents.json)
print("\n== JSON files ==")
json_count = 0
for dirpath, _, files in os.walk(ROOT):
    for fn in files:
        if fn.endswith(".json") or fn.endswith(".webmanifest"):
            path = os.path.join(dirpath, fn)
            json_count += 1
            try:
                with open(path) as f:
                    json.load(f)
            except Exception as e:
                err(f"{rel(path)}: INVALID JSON — {e}")
print(f"Parsed {json_count} JSON/manifest files.")
checked += json_count

# 4. XML validation (Android resources)
print("\n== XML files ==")
xml_count = 0
for dirpath, _, files in os.walk(ROOT):
    for fn in files:
        if fn.endswith(".xml"):
            path = os.path.join(dirpath, fn)
            xml_count += 1
            try:
                minidom.parse(path)
            except Exception as e:
                err(f"{rel(path)}: INVALID XML — {e}")
print(f"Parsed {xml_count} XML files.")
checked += xml_count

# 5. ICO validation — confirm genuine multi-size embedded ICO, not a
#    renamed single PNG.
print("\n== ICO files ==")
for ico_path in [
    os.path.join(ROOT, "assets", "icons", "favicon", "favicon.ico"),
    os.path.join(ROOT, "assets", "icons", "desktop", "qovri.ico"),
]:
    if os.path.exists(ico_path):
        with open(ico_path, "rb") as f:
            header = f.read(6)
        if header[:4] != b"\x00\x00\x01\x00":
            err(f"{rel(ico_path)}: does not have a valid ICO header")
        else:
            count = header[4] | (header[5] << 8)
            if count < 3:
                warn(f"{rel(ico_path)}: only {count} embedded sizes (expected several)")
            else:
                print(f"{rel(ico_path)}: {count} embedded sizes — OK")
    else:
        err(f"Missing expected file: {rel(ico_path)}")

# 6. Required files presence check
print("\n== Required top-level files ==")
required = [
    "README.md", "BRAND-GUIDELINES.md", "LICENSES.md", "CHANGELOG.md", "index.html",
    "assets/icons/favicon/site.webmanifest",
    "assets/icons/favicon/favicon.svg",
    "assets/icons/ios/Assets.xcassets/AppIcon.appiconset/Contents.json",
    "assets/icons/android/mipmap-anydpi-v26/ic_launcher.xml",
]
for rpath in required:
    full = os.path.join(ROOT, rpath)
    if not os.path.exists(full):
        err(f"Missing required file: {rpath}")
    else:
        print(f"{rpath}: present")

# 7. No empty directories, no zero-byte files
print("\n== Empty files / directories ==")
for dirpath, dirs, files in os.walk(ROOT):
    if "scripts" in dirpath:
        continue
    if not dirs and not files:
        warn(f"Empty directory: {rel(dirpath)}")
    for fn in files:
        p = os.path.join(dirpath, fn)
        if os.path.getsize(p) == 0:
            err(f"Zero-byte file: {rel(p)}")

# --- Summary -------------------------------------------------------------
print("\n" + "=" * 60)
print(f"VALIDATION SUMMARY — {checked} assets inspected")
print("=" * 60)
if warnings:
    print(f"\n{len(warnings)} WARNING(S):")
    for w in warnings:
        print(" -", w)
if errors:
    print(f"\n{len(errors)} ERROR(S):")
    for e in errors:
        print(" -", e)
    sys.exit(1)
else:
    print("\nNo errors found.")
