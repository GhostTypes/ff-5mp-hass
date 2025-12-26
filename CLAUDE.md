# CLAUDE.md

Guidance for AI coding assistants working in this repository.

## Current State (January 2025)
- Integration **version 1.1.2** is published and HACS-ready.
- Provides a complete Home Assistant experience for FlashForge printers using the **HTTP API only**.
- Entities shipped: **28 total** (18 sensors, 4 binary sensors, 2 switches, 3 buttons, 1 MJPEG camera).
- UI config flow supports automatic discovery, manual entry, credential validation, and an adjustable polling interval (5–300 s, default 10 s).
- Depends on `flashforge-python-api>=1.0.2` from the companion repository `ff-5mp-api-py`.

## Development Requirements
- **Home Assistant Core**: 2025.12.4 (latest stable as of December 2025)
- **Python**: 3.13.2+ (required by HA Core 2025.12.4)
- **Platform**: WSL2 on Windows (required for local testing with mirrored networking)
- **API Library**: `ff-5mp-api-py` installed in editable mode for live development

## AI Development Guidelines
**When working on Home Assistant integration code** (anything in `custom_components/flashforge/`):
- **ALWAYS** invoke the `home-assistant-dev` skill for guidance on entity platforms, config flows, testing, quality requirements, and HACS publishing
- The skill contains complete HA documentation (290+ files), condensed reference guides, and HACS publishing requirements
- Do not rely on external docs or web searches - use the skill as the authoritative source

**When working on API code** (`ff-5mp-api-py` repo):
- Standard Python async/HTTP client patterns apply
- No special HA knowledge required

Treat this file as the living source of truth for workflows and expectations—update it whenever the process changes.

## Repository Layout Reference
- `custom_components/flashforge/` – Integration source (entities, coordinator, config flow, localization).
- `homeassistant/` – Local Home Assistant sandbox (WSL2 only: Python 3.13 venv, config, symlinked integration) for manual validation.
- `scripts/` – Utility scripts for network discovery and diagnostics.
- `README.md` – Public documentation aligned with the published build.
- `CHANGELOG.md` – Release history (must match `manifest.json` versioning).
- `CLAUDE.md`, `AGENTS.md` – AI-facing playbooks; keep them synchronized.

## Key Capabilities
- **Configuration**
  - Automatic printer discovery via UDP broadcast with multi-printer selection.
  - Manual fallback for IP/serial/check-code entry.
  - Credential validation before config entry creation.
  - Options flow exposes adjustable polling (5–300 s).
- **Monitoring**
  - 18 sensors covering status, temperatures, progress, layers, timing, filament metrics.
  - 4 binary sensors tracking printing, online, error, and paused states.
  - Entities grouped under a single device with manufacturer/model metadata.
- **Control**
  - LED and filtration switches with capability detection (graceful “unavailable” for unsupported models).
  - Pause/resume/cancel buttons with post-action refresh.
  - MJPEG camera entity targeting `http://<ip>:8080/?action=stream`.
- **Architecture**
  - HTTP API only (`FlashForgeClient.info/control/job_control`).
  - `DataUpdateCoordinator` refresh loop with error recovery and client cleanup.
  - Unique IDs built from config entry, serial number, and entity keys.

## Installation Quick Start
1. Copy or symlink `custom_components/flashforge` into your Home Assistant `config/custom_components/` directory.
2. Restart Home Assistant.
3. Navigate to **Settings → Devices & Services → + Add Integration → FlashForge**.
4. Choose **Automatic Discovery** or **Manual Entry** and provide the printer’s check code and serial number.
5. After setup, adjust the polling interval from the integration’s **Configure** dialog if needed.

## Core Modules and Responsibilities
- `__init__.py` – Config entry setup, HTTP client initialization, coordinator registration, teardown.
- `config_flow.py` – Discovery + manual onboarding, credential validation via HTTP, options flow for scan interval.
- `coordinator.py` – `DataUpdateCoordinator` wrapping `FlashForgeClient.info.get()` with graceful error handling and cleanup.
- `sensor.py` – 18 sensor entities. Modify the `SENSORS` tuple, translations, and docs together when changing sensors.
- `binary_sensor.py` – 4 machine-state binary sensors (printing, online, error, paused).
- `switch.py` – LED and filtration switches with client capability checks.
- `button.py` – Pause/resume/cancel commands; request a refresh after each action.
- `camera.py` – MJPEG camera entity (`http://<ip>:8080/?action=stream` by default).
- `util.py` – Shared helpers (currently HTTP session disposal).
- `strings.json` / `translations/en.json` – Keep UI copy synchronized between minimal strings and translation files.

## External Dependencies & Linked Projects
- **flashforge-python-api (ff-5mp-api-py)** – Located at `C:\Users\Cope\Documents\GitHub\ff-5mp-api-py`. Supplies the async HTTP client, discovery helpers, models (`FFMachineInfo`, `MachineState`, etc.). Do not duplicate API logic in this repository—import from the library.
- **Companion library** – `ff-5mp-api-py` (FlashForge HTTP API client).

## Development Workflow

### WSL2 Development Environment Setup
The local Home Assistant instance runs in **WSL2 only** with the following setup:

1. **Python Requirements**
   - Home Assistant Core 2025.12.4+ requires Python 3.13.2+
   - Install Python 3.13 in WSL2:
     ```bash
     sudo apt update
     sudo apt install software-properties-common -y
     sudo add-apt-repository ppa:deadsnakes/ppa -y
     sudo apt update
     sudo apt install python3.13 python3.13-venv python3.13-dev -y
     sudo apt install build-essential -y  # Required for compiling C extensions
     ```
   - Set Python 3.13 as default (optional, via alias):
     ```bash
     echo 'alias python=python3.13' >> ~/.bashrc
     echo 'alias python3=python3.13' >> ~/.bashrc
     source ~/.bashrc
     ```

2. **WSL2 Networking Configuration (Required for Discovery)**
   - **CRITICAL**: For printer discovery to work, WSL2 must use mirrored networking mode and have Hyper-V firewall configured.
   - Without this, discovery will fail even though manual entry works.

   **Configure Mirrored Networking:**
   ```powershell
   # In PowerShell or CMD, create/edit .wslconfig
   notepad C:\Users\Cope\.wslconfig
   ```

   Add this configuration:
   ```ini
   [wsl2]
   networkingMode=mirrored
   ```

   **Configure Hyper-V Firewall:**
   ```powershell
   # In PowerShell as Administrator
   # This allows WSL to receive UDP discovery responses from printers
   Set-NetFirewallHyperVVMSetting -Name '{40E0AC32-46A5-438A-A0B2-2B479E8F2E90}' -DefaultInboundAction Allow
   ```

   **Restart WSL:**
   ```powershell
   wsl --shutdown
   ```

   **Verify Network Configuration (in WSL):**
   ```bash
   ip addr show
   # Should show eth0 with 192.168.x.x address matching your local network
   # Should show broadcast address matching your subnet (e.g., 192.168.1.255)
   ```

   **Reference**: [WSL Networking Documentation](https://learn.microsoft.com/en-us/windows/wsl/networking)

3. **Initial Setup (from scratch)**
   ```bash
   # Navigate to repo root
   cd /mnt/c/Users/Cope/Documents/GitHub/ff-5mp-hass

   # Create fresh homeassistant directory if needed
   mkdir homeassistant
   cd homeassistant

   # Create Python 3.13 virtual environment
   python3.13 -m venv venv
   source venv/bin/activate

   # Upgrade pip
   pip install --upgrade pip

   # Install Home Assistant Core 2025.12.4
   pip install homeassistant==2025.12.4

   # Install ff-5mp-api-py in editable mode (for development)
   pip install -e /mnt/c/Users/Cope/Documents/GitHub/ff-5mp-api-py

   # Create config directory structure
   mkdir -p config/custom_components

   # Create symlink to integration (IMPORTANT: use exactly this path)
   ln -s ../../../custom_components/flashforge config/custom_components/flashforge

   # Verify symlink works
   ls config/custom_components/flashforge/

   # Create basic configuration files (see below)
   ```

4. **Configuration Files**
   Create `config/configuration.yaml`:
   ```yaml
   # Configure a default setup of Home Assistant (frontend, api, etc)
   default_config:

   # Enable debug logging for FlashForge
   logger:
     default: info
     logs:
       custom_components.flashforge: debug
       flashforge: debug

   # Text to speech
   tts:
     - platform: google_translate

   automation: !include automations.yaml
   script: !include scripts.yaml
   scene: !include scenes.yaml
   ```

   Create empty files: `touch config/automations.yaml config/scripts.yaml config/scenes.yaml`

5. **Starting Home Assistant**
   ```bash
   cd /mnt/c/Users/Cope/Documents/GitHub/ff-5mp-hass/homeassistant
   source venv/bin/activate
   hass -c config
   ```
   - Access at `http://localhost:8123`
   - Complete onboarding on first run
   - Add FlashForge integration via UI: Settings → Devices & Services → + Add Integration

6. **Development Workflow**
   - **Integration changes**: Edit files in `custom_components/flashforge/` (they're symlinked, so changes are instant)
   - **API changes**: Edit files in `ff-5mp-api-py` repo (editable install means changes are instant)
   - **Apply changes**: Restart Home Assistant or reload the integration via UI (Settings → Devices & Services → FlashForge → ⋮ → Reload)
   - **Logs**: Monitor `homeassistant/config/home-assistant.log` or use HA UI (Settings → System → Logs)

7. **Key Points**
   - Both the integration (`custom_components/flashforge`) and API (`ff-5mp-api-py`) are in editable/development mode
   - Changes to either repo apply immediately without reinstallation
   - No need for `update_dev.py` or manual copying - symlink handles it
   - Use `pip install -e` for Python packages you're actively developing
   - Home Assistant will NOT download from PyPI since the package is already installed in editable mode

### Code Implementation Guidelines
1. **Implementation**
   - Keep everything async; no blocking calls inside Home Assistant callbacks.
   - Use HTTP-facing client methods (`client.info`, `client.control`, `client.job_control`, etc.).
   - Respect capability flags (`client.led_control`, `client.filtration_control`) before exposing features.
2. **Localization & Docs**
   - Update `strings.json` and `translations/en.json` whenever UI text changes.
   - Reflect behavior changes in `README.md`, `CHANGELOG.md`, `CLAUDE.md`, and `AGENTS.md` as appropriate.
3. **Versioning**
   - Bump `manifest.json` `version` with every release-worthy change; keep `CHANGELOG.md` and release notes in sync.
4. **Style**
   - Favor concise helper functions over duplicated logic.
   - Maintain alphabetical imports within groups.
   - Reserve comments for clarifying non-obvious behavior.

## Testing & Validation
- **Development Environment** (`homeassistant/`)
  - **WSL2 only**: `cd homeassistant && source venv/bin/activate && hass -c config`
  - Logs: `homeassistant/config/home-assistant.log` (tail for live debugging: `tail -f homeassistant/config/home-assistant.log`)
  - Access UI: `http://localhost:8123`
  - Uses editable install of `ff-5mp-api-py` and symlinked integration
- **Production Test Environment** (`homeassistant-prod/`)
  - **WSL2 only**: `cd homeassistant-prod && ./start.sh`
  - Clean install environment for testing HACS installation flow
  - Uses `.venv` (created with `uv`) instead of `venv`
  - **NOT tracked in git** (in `.gitignore`) - but accessible when needed
  - Simulates real user experience (no symlinks, downloads from PyPI)
- **Quick checklist**
  1. Confirm printer is on, LAN mode enabled, and check code/serial are available.
  2. Install the integration (copy folder or use dev symlink) and restart Home Assistant.
  3. Add the integration via UI; test both discovery and manual paths.
  4. Open the created device and verify entities:
     - Sensors: machine status, nozzle temps/targets, bed temps/targets, progress, file, current/total layers, elapsed/remaining time, filament length/weight, print speed, z offset, move mode, nozzle size, filament type.
     - Binary sensors: printing, online, error, paused.
     - Switches: LED and filtration (may show unavailable if unsupported).
     - Buttons: pause, resume, cancel.
     - Camera: MJPEG feed reachable.
  5. Trigger control actions (pause/resume/cancel, switches) and ensure states refresh.
  6. Observe coordinator error handling by temporarily disconnecting the printer and confirming entities surface availability correctly.
- **Discovery diagnostics** – `scripts/test_discovery.py` and `scripts/discovery_probe.py` help debug LAN communication without HA.
- **Automated tests** – None yet. If you add pytest suites, document how to run them and keep them optional for contributors.
- **Hardware caveat** – Full verification requires a FlashForge printer with LAN mode enabled; simulated runs only confirm flow logic.

## Implementation Guard Rails
- **HTTP-first policy** – Do not introduce direct TCP/G-code communication here. If unavoidable, extend the API library (`ff-5mp-api-py`) and consume it via HTTP-style helpers.
- **Coordinator as source of truth** – Entities derive state from the coordinator’s latest `FFMachineInfo`. Avoid storing custom copies of printer state in entities.
- **Error handling** – Wrap connection issues in `ConfigEntryNotReady`, `ConnectionError`, or `UpdateFailed` so Home Assistant retries gracefully.
- **Entity additions**
  - Add to the appropriate entity tuple.
  - Provide unique `key`, icon, units, and defensive `value_fn`.
  - Update documentation (README, CHANGELOG, CLAUDE/AGENTS) and translations.
- **Options flow** – Currently only the scan interval. Extend cautiously to avoid breaking existing entries.

## Release & Publishing Checklist
1. Implement and document changes.
2. Bump `manifest.json` `version` and update `CHANGELOG.md`.
3. Validate in the local HA sandbox and, if possible, on real hardware.
4. Tag and publish a GitHub release (`vX.Y.Z`) for HACS distribution.
5. Ensure README badges (release, HACS status, minimum HA version) stay accurate.

## HACS Installation (for Testing)
To test the integration as users will experience it:
1. **Install HACS** in production environment:
   ```bash
   cd homeassistant-prod/config
   sudo apt install unzip  # Required dependency
   wget -O - https://get.hacs.xyz | bash -
   ```
2. **Restart Home Assistant** and complete HACS setup via UI (Settings → Devices & Services → Add Integration → HACS)
3. **Add custom repository**: In HACS, add `https://github.com/GhostTypes/ff-5mp-hass` as Integration
4. **Install integration** through HACS UI and test

## Critical Lessons Learned
- **WSL2 Discovery**: Requires mirrored networking (`networkingMode=mirrored` in `.wslconfig`) AND Hyper-V firewall rule (`Set-NetFirewallHyperVVMSetting`) to receive UDP responses from printers
- **Editable Installs**: Both integration (symlinked) and API (`pip install -e`) are editable - changes apply immediately without reinstall
- **Config Entry Lifecycle**: Always use `ConfigEntryNotReady` for temporary connection failures (HA will retry automatically)
- **Entity Availability**: Set `available = False` when printer offline (Silver quality requirement)
- **HACS Testing**: Use `homeassistant-prod/` environment to test real user installation flow (not tracked in git)

## References
- **Home Assistant Development**: Use the `home-assistant-dev` skill for all HA integration work
- **Companion API**: https://github.com/GhostTypes/ff-5mp-api-py

Keep this document in sync with reality so every coding agent starts with the same, accurate context.
