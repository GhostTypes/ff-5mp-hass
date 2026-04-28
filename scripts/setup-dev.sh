#!/bin/bash
# =============================================================================
# setup-dev.sh — FlashForge dev sandbox (homeassistant/)
#
# Sets up the editable-install + symlinked integration environment.
# Run this ONCE on a new machine, then use ./start.sh to launch HA.
#
# Re-run safely: if an existing venv targets a different Python version than
# the one pinned below, it will be deleted and recreated.
#
# Usage (from WSL):
#   cd /mnt/c/Users/coper/Documents/GitHub/ff-5mp-hass
#   bash scripts/setup-dev.sh
# =============================================================================
set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HASS_DIR="$REPO_ROOT/homeassistant"
API_DIR="/mnt/c/Users/coper/Documents/GitHub/ff-5mp-api-py"

# HA Core 2026.4+ requires Python 3.14.2+. Bump these together when upgrading.
PYTHON_BIN="python3.14"
HA_VERSION="2026.4.2"

echo "=============================================="
echo " FlashForge Dev Sandbox Setup"
echo "=============================================="
echo " Repo   : $REPO_ROOT"
echo " HA dir : $HASS_DIR"
echo " API    : $API_DIR"
echo " Python : $PYTHON_BIN"
echo " HA ver : $HA_VERSION"
echo ""

# --- Prereq checks -----------------------------------------------------------

if ! command -v "$PYTHON_BIN" &>/dev/null; then
    echo "ERROR: $PYTHON_BIN not found. Install it first:"
    echo ""
    echo "  sudo apt update"
    echo "  sudo apt install -y software-properties-common build-essential"
    echo "  sudo add-apt-repository ppa:deadsnakes/ppa -y"
    echo "  sudo apt update"
    echo "  sudo apt install -y ${PYTHON_BIN} ${PYTHON_BIN}-venv ${PYTHON_BIN}-dev"
    exit 1
fi

if [ ! -d "$API_DIR" ]; then
    echo "ERROR: ff-5mp-api-py not found at $API_DIR"
    echo "Clone it there or edit API_DIR in this script."
    exit 1
fi

# --- Virtual environment -----------------------------------------------------

# Detect a stale venv (different Python version) and recreate it.
NEEDS_FRESH_VENV=0
if [ -d "$HASS_DIR/venv" ]; then
    EXPECTED_VERSION="$("$PYTHON_BIN" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
    if [ -x "$HASS_DIR/venv/bin/python" ]; then
        ACTUAL_VERSION="$("$HASS_DIR/venv/bin/python" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null || echo "unknown")"
        if [ "$ACTUAL_VERSION" != "$EXPECTED_VERSION" ]; then
            echo "[venv] Existing venv uses Python $ACTUAL_VERSION but $EXPECTED_VERSION is required."
            echo "       Removing and recreating..."
            rm -rf "$HASS_DIR/venv"
            NEEDS_FRESH_VENV=1
        fi
    else
        echo "[venv] Existing venv looks broken (no python binary). Recreating..."
        rm -rf "$HASS_DIR/venv"
        NEEDS_FRESH_VENV=1
    fi
else
    NEEDS_FRESH_VENV=1
fi

if [ "$NEEDS_FRESH_VENV" -eq 1 ]; then
    echo "[1/4] Creating $PYTHON_BIN venv..."
    "$PYTHON_BIN" -m venv "$HASS_DIR/venv"
else
    echo "[1/4] Reusing existing venv (matching Python version)."
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
