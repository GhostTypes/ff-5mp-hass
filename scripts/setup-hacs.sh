#!/bin/bash
# =============================================================================
# setup-hacs.sh — FlashForge HACS prod sandbox (homeassistant-prod/)
#
# Sets up the production-style environment that simulates a real HACS install.
# HACS and flashforge are already present in config/custom_components/ from
# the previous machine — this script only creates the .venv and installs HA.
#
# !! IMPORTANT — PyPI dependency check !!
# manifest.json requires: flashforge-python-api>=1.1.0
# As of writing, only 1.0.2 is on PyPI. Until 1.1.0 is published, HA will
# fail to install the dependency when loading the integration via HACS.
#
# Workaround (pre-release testing): pass --inject-api flag to this script.
# This installs the local ff-5mp-api-py editable into the prod venv so you
# can test the HACS integration flow before the library hits PyPI.
#
# Usage (from WSL):
#   cd /mnt/c/Users/coper/Documents/GitHub/ff-5mp-hass
#
#   # Normal (requires flashforge-python-api>=1.1.0 on PyPI):
#   bash scripts/setup-hacs.sh
#
#   # Pre-release workaround (injects local api-py into prod venv):
#   bash scripts/setup-hacs.sh --inject-api
# =============================================================================
set -e

INJECT_API=false
for arg in "$@"; do
    case $arg in
        --inject-api) INJECT_API=true ;;
        *) echo "Unknown argument: $arg"; exit 1 ;;
    esac
done

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HASS_DIR="$REPO_ROOT/homeassistant-prod"
API_DIR="/mnt/c/Users/coper/Documents/GitHub/ff-5mp-api-py"
HA_VERSION="2025.12.4"

echo "=============================================="
echo " FlashForge HACS Prod Sandbox Setup"
echo "=============================================="
echo " Repo  : $REPO_ROOT"
echo " HA dir: $HASS_DIR"
echo ""

# --- PyPI warning ------------------------------------------------------------

PYPI_VERSION=$(pip index versions flashforge-python-api 2>/dev/null | grep -oP '[\d.]+' | head -1 || echo "unknown")
echo "=============================================="
echo " PyPI status: flashforge-python-api latest = $PYPI_VERSION"
echo " manifest.json requires: >=1.1.0"
if python3 -c "from packaging.version import Version; exit(0 if Version('$PYPI_VERSION') >= Version('1.1.0') else 1)" 2>/dev/null; then
    echo " Status: OK — PyPI version satisfies the requirement"
else
    echo ""
    echo " WARNING: PyPI version does NOT satisfy >=1.1.0!"
    echo " The integration will fail to load via HACS until 1.1.0 is published."
    if [ "$INJECT_API" = false ]; then
        echo ""
        echo " To test now anyway, re-run with --inject-api:"
        echo "   bash scripts/setup-hacs.sh --inject-api"
        echo " (This installs the local ff-5mp-api-py into the prod venv)"
    else
        echo " --inject-api flag set: will install local ff-5mp-api-py"
    fi
fi
echo "=============================================="
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

if [ "$INJECT_API" = true ] && [ ! -d "$API_DIR" ]; then
    echo "ERROR: --inject-api requested but ff-5mp-api-py not found at $API_DIR"
    exit 1
fi

# --- Virtual environment -----------------------------------------------------

if [ -d "$HASS_DIR/.venv" ]; then
    echo "[skip] .venv already exists — delete it to force a fresh install"
else
    echo "[1/3] Creating Python 3.13 venv at .venv..."
    python3.13 -m venv "$HASS_DIR/.venv"
fi

source "$HASS_DIR/.venv/bin/activate"

# --- Install packages --------------------------------------------------------

echo "[2/3] Installing pip tools..."
pip install --upgrade pip wheel setuptools -q

echo "[2/3] Installing Home Assistant $HA_VERSION..."
pip install "homeassistant==$HA_VERSION" -q

if [ "$INJECT_API" = true ]; then
    echo "[2/3] Injecting local ff-5mp-api-py (editable)..."
    pip install -e "$API_DIR" -q
    echo "       NOTE: This overrides what HACS/HA would pull from PyPI."
fi

# --- Status check ------------------------------------------------------------

echo "[3/3] Checking installed components..."

HACS_DIR="$HASS_DIR/config/custom_components/hacs"
FF_DIR="$HASS_DIR/config/custom_components/flashforge"

if [ -d "$HACS_DIR" ]; then
    echo "       HACS component: present"
else
    echo "       HACS component: NOT FOUND — install it:"
    echo "         cd $HASS_DIR/config && wget -O - https://get.hacs.xyz | bash -"
fi

if [ -d "$FF_DIR" ]; then
    FF_VERSION=$(python3 -c "import json; d=json.load(open('$FF_DIR/manifest.json')); print(d.get('version','?'))" 2>/dev/null || echo "?")
    echo "       FlashForge component: present (v$FF_VERSION)"
else
    echo "       FlashForge component: not present (will be installed via HACS)"
fi

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
echo " HACS flow (if starting fresh):"
echo "   1. Complete HA onboarding"
echo "   2. Settings > Devices & Services > + Add Integration > HACS"
echo "   3. In HACS: 3-dot menu > Custom repositories"
echo "   4. Add: https://github.com/GhostTypes/ff-5mp-hass  Type: Integration"
echo "   5. Install 'FlashForge 3D Printer' and restart HA"
echo ""
echo " HACS flow (if HACS already configured — updating to latest release):"
echo "   1. Start HA and open HACS"
echo "   2. Go to Integrations > FlashForge 3D Printer"
echo "   3. If an update is available, click Update"
echo "   4. Restart HA after update"
echo ""
echo " To release ff-5mp-api-py 1.1.0 to PyPI (required for clean HACS path):"
echo "   See CLAUDE.md in ff-5mp-api-py — use the GitHub Actions 'Publish Release' workflow"
echo ""
