#!/bin/bash
# =============================================================================
# setup-dev.sh — FlashForge dev sandbox (homeassistant/)
#
# Sets up the editable-install + symlinked integration environment.
# Run this ONCE on a new machine, then use ./start.sh to launch HA.
#
# Usage (from WSL):
#   cd /mnt/c/Users/coper/Documents/GitHub/ff-5mp-hass
#   bash scripts/setup-dev.sh
# =============================================================================
set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HASS_DIR="$REPO_ROOT/homeassistant"
API_DIR="/mnt/c/Users/coper/Documents/GitHub/ff-5mp-api-py"
HA_VERSION="2025.12.4"

echo "=============================================="
echo " FlashForge Dev Sandbox Setup"
echo "=============================================="
echo " Repo  : $REPO_ROOT"
echo " HA dir: $HASS_DIR"
echo " API   : $API_DIR"
echo ""

# --- Prereq checks -----------------------------------------------------------

if ! command -v python3.13 &>/dev/null; then
    echo "ERROR: python3.13 not found. Install it first:"
    echo ""
    echo "  sudo apt update"
    echo "  sudo apt install -y software-properties-common build-essential"
    echo "  sudo add-apt-repository ppa:deadsnakes/ppa -y"
    echo "  sudo apt update"
    echo "  sudo apt install -y python3.13 python3.13-venv python3.13-dev"
    exit 1
fi

if [ ! -d "$API_DIR" ]; then
    echo "ERROR: ff-5mp-api-py not found at $API_DIR"
    echo "Clone it there or edit API_DIR in this script."
    exit 1
fi

# --- Virtual environment -----------------------------------------------------

if [ -d "$HASS_DIR/venv" ]; then
    echo "[skip] venv already exists — delete it to force a fresh install"
else
    echo "[1/4] Creating Python 3.13 venv..."
    python3.13 -m venv "$HASS_DIR/venv"
fi

source "$HASS_DIR/venv/bin/activate"

# --- Install packages --------------------------------------------------------

echo "[2/4] Installing pip tools..."
pip install --upgrade pip wheel setuptools -q

echo "[3/4] Installing Home Assistant $HA_VERSION..."
pip install "homeassistant==$HA_VERSION" -q

echo "[3/4] Installing ff-5mp-api-py in editable mode..."
pip install -e "$API_DIR" -q

# --- Symlink -----------------------------------------------------------------

echo "[4/4] Setting up integration symlink..."

LINK="$HASS_DIR/config/custom_components/flashforge"
mkdir -p "$HASS_DIR/config/custom_components"

if [ -L "$LINK" ]; then
    echo "       Symlink already exists — skipping"
elif [ -d "$LINK" ]; then
    echo "WARNING: $LINK is a real directory (not a symlink)."
    echo "         Remove it manually if you want a symlink:"
    echo "         rm -rf $LINK && bash scripts/setup-dev.sh"
else
    ln -sfn "$REPO_ROOT/custom_components/flashforge" "$LINK"
    echo "       Created: $LINK -> $REPO_ROOT/custom_components/flashforge"
fi

# --- Verify ------------------------------------------------------------------

echo ""
echo "Verifying symlink contents:"
ls "$LINK/" | head -5

echo ""
echo "=============================================="
echo " Setup complete!"
echo "=============================================="
echo ""
echo " To start Home Assistant:"
echo "   cd $HASS_DIR && ./start.sh"
echo ""
echo " Access UI: http://localhost:8123"
echo ""
echo " Notes:"
echo "   - Integration changes in custom_components/flashforge/ apply immediately"
echo "   - API changes in ff-5mp-api-py/ apply immediately (editable install)"
echo "   - Reload via: Settings > Devices & Services > FlashForge > ⋮ > Reload"
echo "   - Logs: tail -f $HASS_DIR/config/home-assistant.log"
echo ""
