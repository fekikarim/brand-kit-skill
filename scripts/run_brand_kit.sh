#!/usr/bin/env bash
# ============================================================================
#  Brand Identity Kit — Universal Runner Script
#  Works with any Python 3.9+ environment
#  Usage: ./scripts/run_brand_kit.sh [output_directory]
# ============================================================================

set -e

BRAND_KIT_DIR="${1:-./brand-kit-output}"
SCRIPTS_DIR="$BRAND_KIT_DIR/scripts"

echo ""
echo "🎨  Brand Identity Kit — Asset Generator"
echo "========================================"
echo ""

# Check Python
if ! command -v python3 &>/dev/null; then
  echo "❌  Python 3 not found. Install from https://python.org"
  exit 1
fi

PYTHON_VERSION=$(python3 --version | awk '{print $2}')
echo "✅  Python $PYTHON_VERSION detected"

# Check dependencies
echo "📦  Checking dependencies..."
python3 -c "import cairosvg, PIL, fontTools" 2>/dev/null || {
  echo ""
  echo "⚠️   Missing dependencies. Installing..."
  pip install cairosvg pillow fonttools
}
echo "✅  Dependencies OK"
echo ""

# Navigate to scripts dir
if [ ! -d "$SCRIPTS_DIR" ]; then
  echo "❌  Scripts directory not found: $SCRIPTS_DIR"
  echo "    Make sure the AI agent has completed Phase 4a first."
  exit 1
fi

cd "$SCRIPTS_DIR"

echo "🚀  Running asset generation pipeline..."
echo ""

run_script() {
  local name="$1"
  echo "▶  $name"
  python3 "$name" && echo "   ✅  Done" || { echo "   ❌  FAILED — stopping"; exit 1; }
  echo ""
}

run_script "generate_masters.py"
run_script "generate_wordmark.py"
run_script "generate_lockups.py"
run_script "export_raster.py"
run_script "generate_favicons.py"
run_script "generate_pwa_icons.py"
run_script "generate_social_assets.py"
run_script "generate_patterns.py"

echo ""
echo "🔍  Validating assets..."
python3 validate_assets.py

echo ""
echo "📦  Creating ZIP package..."
cd "$(dirname "$SCRIPTS_DIR")"
BRAND_NAME=$(basename "$(pwd)" | sed 's/-Brand-Kit//')
ZIP_NAME="${BRAND_NAME}-brand-kit.zip"
zip -r "../$ZIP_NAME" . --exclude "*/scripts/__pycache__/*"
echo "✅  Created: $ZIP_NAME"

echo ""
echo "🎉  Brand kit complete!"
echo "    Open index.html in a browser to preview your brand showcase."
echo ""
