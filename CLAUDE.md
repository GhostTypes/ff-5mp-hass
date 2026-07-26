# CLAUDE.md

Guidance for AI coding assistants working in this repository.

## Current State (July 2026)
- Integration **version 1.3.2** (in-flight; 1.3.1 tagged 2026-07-23).
- Provides a complete Home Assistant experience for FlashForge printers using the **HTTP API only**.
- Entities shipped: **56 total** (38 sensors, 5 binary sensors, 2 switches, 4 buttons, 1 select, 1 MJPEG camera, 5 images — the g-code thumbnail plus 4 Material Station slot color swatches).
- Diagnostics download supported (`diagnostics.py`), with credentials and identifiers redacted.
- Reauthentication and reconfigure flows supported in addition to the original setup paths.
- UI config flow supports automatic discovery, manual entry, credential validation, and an adjustable polling interval (5–300 s, default 10 s).
- Depends on `flashforge-python-api>=1.3.0` from the companion repository `ff-5mp-api-py`.

## Development Requirements
- **Home Assistant Core**: 2026.4.2 (current stable)
- **Python**: 3.14.2+ (required by HA Core 2026.4.x)
- **Platform**: WSL2 on Windows (required for local testing with mirrored networking)
- **API Library**: `ff-5mp-api-py` installed in editable mode for live development

The local WSL dev sandbox under `homeassistant/` runs Python 3.14 + HA 2026.4.2. `scripts/setup-dev.sh` provisions this baseline and auto-recreates the venv if it is stale. Verified working: HA starts and the integration loads on this baseline.

## AI Development Guidelines
**When working on Home Assistant integration code** (anything in `custom_components/flashforge/`):
- **ALWAYS** invoke the `home-assistant-dev` skill for guidance on entity platforms, config flows, testing, quality requirements, and HACS publishing
- The skill contains complete HA documentation (290+ files), condensed reference guides, and HACS publishing requirements
- Do not rely on external docs or web searches - use the skill as the authoritative source

**When working on API code** (`ff-5mp-api-py` repo):
- Standard Python async/HTTP client patterns apply
- No special HA knowledge required

**Path conventions**:
- **CRITICAL**: This repository is developed on Windows. Always use Windows-style paths in Bash commands: `C:\Users\coper\Documents\GitHub\1flashforge_printers\ff-5mp-hass`
- **NEVER** use Unix-style paths like `/mnt/c/Users/Cope/...` - these will fail
- WSL2 commands in documentation are for reference only; actual development commands must use Windows paths

Treat this file as the living source of truth for workflows and expectations—update it whenever the process changes.

## Repository Layout Reference
- `custom_components/flashforge/` – Integration source (entities, coordinator, config flow, localization).
- `homeassistant/` – Local Home Assistant sandbox (WSL2 only: Python 3.14 venv, config, symlinked integration) for manual validation.
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
  - 38 sensors covering status, temperatures (per-toolhead on the Creator 5 series, plus a heated chamber), progress, layers, timing, filament metrics, fan speeds, air quality (5M Pro / Creator 5 Pro TVOC), active Material Station slot, print completion time, lifetime stats, plus diagnostic sensors (`firmware_version`, `free_disk_space`, `ip_address`, `error_code`).
  - 5 binary sensors tracking printing, online, error, paused, and door-open (Creator 5 Pro only) states.
  - 1 image entity for the active g-code thumbnail (fetched on demand, cached per filename).
  - 4 Material Station slot image entities (AD5X / Creator 5 series) — labeled color swatches (filament hex color + material name overlay) rendered with Pillow in an executor and cached per `(material, color)` tuple.
  - Entities grouped under a single device with manufacturer/model metadata.
- **Control**
  - LED switch with capability detection (graceful "unavailable" for unsupported models, with an option to override the check).
  - Filtration as a `select` entity with Off / Internal / External states (Adventurer 5M Pro / Creator 5 Pro only — gated on `is_pro OR is_creator5_pro`).
  - Pause / resume / cancel / clear-status buttons with post-action refresh.
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
- `config_flow.py` – Discovery + manual onboarding, reauth + reconfigure flows, credential validation via HTTP, options flow (scan interval + LED-availability override). Enforces `SUPPORTED_PIDS` early via `_is_supported_detail()`.
- `coordinator.py` – `DataUpdateCoordinator` wrapping `FlashForgeClient.info.get()` with graceful error handling and cleanup.
- `sensor.py` – 38 sensor entities (operational + diagnostic). `SENSORS` is composed of `_BASE_SENSORS + TOOLHEAD_SENSORS + CHAMBER_SENSORS` (per-toolhead and heated-chamber sensors are gated on the Creator 5 series). Modify the tuples, translations, and docs together when changing sensors.
- `binary_sensor.py` – 5 machine-state binary sensors (printing, online, error, paused, door-open). `door_open` is availability-gated on `has_door_sensor` (Creator 5 Pro only).
- `switch.py` – LED switch with client capability check (capability check can be overridden via options) and the camera switch. Descriptions carry both an `availability_fn` (greys the entity out; use when the printer may report the feature later) and a `supported_fn` (skips creating it entirely; use when the model's API cannot perform the action at all — the Creator 5 camera switch is inert, so it is never created there).
- `select.py` – Filtration mode select (Off / Internal / External; availability gated on `is_pro OR is_creator5_pro`, i.e. Adventurer 5M Pro / Creator 5 Pro).
- `button.py` – Pause / resume / cancel / clear-status commands; request a refresh after each action.
- `camera.py` – MJPEG camera entity (`http://<ip>:8080/?action=stream` by default).
- `image.py` – Hosts the active-print g-code thumbnail entity AND the 4 Material Station slot swatch entities (AD5X / Creator 5 series). Swatches are PNG-encoded by `render_swatch_bytes()` (Pillow) inside an executor; both entity types cache rendered bytes and only invalidate on input change.
- `diagnostics.py` – HA diagnostics download payload, with `check_code`, `serial_number`, MAC/IP, and cloud registration codes redacted.
- `util.py` – Shared helpers: `async_close_flashforge_client()` for HTTP session disposal, `build_device_info()` for the per-platform device-info dict.
- `strings.json` / `translations/en.json` – Keep UI copy synchronized between minimal strings and translation files. Every entity carries a `translation_key`; `name`s never set manually on entities.

## External Dependencies & Linked Projects
- **flashforge-python-api (ff-5mp-api-py)** – Located at `C:\Users\coper\Documents\GitHub\1flashforge_printers\ff-5mp-api-py`. Supplies the async HTTP client, discovery helpers, models (`FFMachineInfo`, `MachineState`, etc.). Do not duplicate API logic in this repository—import from the library.
- **Companion library** – `ff-5mp-api-py` (FlashForge HTTP API client).

## Development Workflow

### WSL2 Development Environment Setup
The local Home Assistant instance runs in **WSL2 only** with the following setup:

1. **Python Requirements**
   - Home Assistant Core 2026.4.2+ requires Python 3.14.2+
   - Install Python 3.14 in WSL2:
     ```bash
     sudo apt update
     sudo apt install software-properties-common -y
     sudo add-apt-repository ppa:deadsnakes/ppa -y
     sudo apt update
     sudo apt install python3.14 python3.14-venv python3.14-dev -y
     sudo apt install build-essential -y  # Required for compiling C extensions
     ```
   - Set Python 3.14 as default (optional, via alias):
     ```bash
     echo 'alias python=python3.14' >> ~/.bashrc
     echo 'alias python3=python3.14' >> ~/.bashrc
     source ~/.bashrc
     ```

2. **WSL2 Networking Configuration (Required for Discovery)**
   - **CRITICAL**: For printer discovery to work, WSL2 must use mirrored networking mode and have Hyper-V firewall configured.
   - Without this, discovery will fail even though manual entry works.

   **Configure Mirrored Networking:**
   ```powershell
   # In PowerShell or CMD, create/edit .wslconfig
   notepad C:\Users\coper\.wslconfig
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
   cd /mnt/c/Users/coper/Documents/GitHub/1flashforge_printers/ff-5mp-hass

   # Create fresh homeassistant directory if needed
   mkdir homeassistant
   cd homeassistant

   # Create Python 3.14 virtual environment
   python3.14 -m venv venv
   source venv/bin/activate

   # Upgrade pip
   pip install --upgrade pip

   # Install Home Assistant Core 2026.4.2
   pip install homeassistant==2026.4.2

   # Install ff-5mp-api-py in editable mode (for development)
   pip install -e /mnt/c/Users/coper/Documents/GitHub/1flashforge_printers/ff-5mp-api-py

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
   cd /mnt/c/Users/coper/Documents/GitHub/1flashforge_printers/ff-5mp-hass/homeassistant
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
   - Respect capability flags (`client.led_control` for the LED switch) before exposing features. Do NOT trust the `/product`-derived `client.filtration_control` — gate filtration/TVOC/chamber-fan on model identity (`is_pro OR is_creator5_pro`) instead.
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

### Two-Tier Testing Strategy

We use a **two-tier approach** to balance rapid iteration with comprehensive validation:

#### Tier 1: Cross-Platform Unit Tests (Primary - No HA Dependencies)

**What:** Tests business logic without requiring Home Assistant installation.

**Why this approach:**
- ✅ **Windows compatibility**: Home Assistant requires Unix-only modules (`fcntl`) and cannot install on Windows
- ✅ **Fast CI**: Avoids installing 500+ MB Home Assistant package, dramatically speeding up CI pipelines
- ✅ **Rapid iteration**: Tests run in ~1 second on local machines
- ✅ **Cross-platform development**: Test on Windows natively without WSL

**How it works:**
- `tests/ha_mocks.py` provides centralized Home Assistant module mocking
- Stub classes mimic HA's entity descriptions, base classes, enums, and constants
- Import mocks BEFORE importing integration code to intercept HA dependencies
- Tests focus on pure Python logic: value extraction, state transformations, utility functions

**Running tests:**
```bash
# From repository root (Windows or WSL)
pytest tests/unit/ -v

# With coverage report
pytest tests/unit/ --cov=custom_components.flashforge --cov-report=term-missing

# Specific test file
pytest tests/unit/test_sensor_value_functions.py -v
```

**Current coverage (125 tests total):**
- `tests/unit/test_discovery.py` – printer discovery protocol
- `tests/unit/test_sensor_value_functions.py` – sensor value extraction
- `tests/unit/test_binary_sensor_value_functions.py` – binary sensor logic
- `tests/unit/test_util.py` – utility functions (`async_close_flashforge_client`, `build_device_info`)
- `tests/unit/test_camera_entity.py` – camera entity behavior
- `tests/unit/test_config_flow_supported_printers.py` – PID-based supported-printer gate
- `tests/unit/test_coordinator.py` – coordinator update + error paths
- `tests/unit/test_setup_entry.py` – integration setup wiring
- `tests/unit/test_platform_registration.py` – platform list sanity
- `tests/unit/test_select_availability.py` – filtration select availability
- `tests/unit/test_switch_availability.py` – LED switch availability with override

**Test dependencies** (`requirements-test.txt`):
- Core: `pytest`, `pytest-asyncio`, `pytest-cov`
- Snapshot testing: `syrupy` (for future use)
- API library: `flashforge-python-api` (editable install for development)
- Network: `netifaces` (for discovery tests)
- **Explicitly excludes** `homeassistant` and `pytest-homeassistant-custom-component` (Unix-only)

#### Tier 2: Integration Tests (Future - WSL/Linux Only)

**What:** Tests requiring full Home Assistant runtime (config flows, coordinator, entity lifecycle).

**When to use:**
- Testing config flow UI interactions
- Validating coordinator update cycles
- Testing entity registration and state updates
- Verifying service calls and device registry integration

**Where to run:** WSL2 or Linux environments only (in `homeassistant/` dev environment).

**Deferred until:** Integration tests become necessary (e.g., preparing for HACS submission or major refactoring).

### Manual Validation Environments

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

### Manual Testing Checklist

1. Confirm printer is on, LAN mode enabled, and check code/serial are available.
2. Install the integration (copy folder or use dev symlink) and restart Home Assistant.
3. Add the integration via UI; test both discovery and manual paths.
4. Open the created device and verify entities:
   - Sensors: machine status, nozzle temps/targets, bed temps/targets, progress, file, current/total layers, elapsed/remaining time, filament length/weight, print speed, z offset, nozzle size, filament type, lifetime stats, plus diagnostic sensors (firmware version, free disk space, error code).
   - Binary sensors: printing, online, error, paused, door-open (Creator 5 Pro only).
   - Switch: LED (may show unavailable on unsupported models unless override is enabled).
   - Select: filtration mode — Off / Internal / External (Adventurer 5M Pro / Creator 5 Pro only).
   - Buttons: pause, resume, cancel, clear status.
   - Camera: MJPEG feed reachable.
   - Image: g-code thumbnail of the active print.
   - Image (AD5X / Creator 5 series): four Material Station slot swatches (`image.*_ifs_slot_1..4`) showing material color + label, "EMPTY" tile for unloaded slots.
5. Trigger control actions (pause/resume/cancel, switches) and ensure states refresh.
6. Observe coordinator error handling by temporarily disconnecting the printer and confirming entities surface availability correctly.

### Testing Utilities

- **Discovery diagnostics** – `scripts/test_discovery.py` and `scripts/discovery_probe.py` help debug LAN communication without HA.
- **Hardware caveat** – Full verification requires a FlashForge printer with LAN mode enabled; simulated runs only confirm flow logic.

## Implementation Guard Rails
- **HTTP-first policy** – Do not introduce direct TCP/G-code communication here. If unavoidable, extend the API library (`ff-5mp-api-py`) and consume it via HTTP-style helpers.
- **Coordinator as source of truth** – Entities derive state from the coordinator’s latest `FFMachineInfo`. Avoid storing custom copies of printer state in entities.
- **PID for model identity, never the printer name** – Modern HTTP printers report a stable firmware-set integer `pid` on `/detail` (35 = Adventurer 5M, 36 = 5M Pro, 38 = AD5X, 40 = Creator 5, 41 = Creator 5 Pro). The integration enforces this in TWO places that should both stay in sync:
  - `config_flow.py` `_is_supported_detail()` reads the raw `/detail` payload during pairing and rejects PIDs not in `SUPPORTED_PIDS = {35, 36, 38, 40, 41}`. This is the early gate — runs before any `FFMachineInfo` parsing happens.
  - The library (`flashforge-python-api>=1.3.0`) populates `FFMachineInfo.is_pro` / `is_ad5x` / `is_creator5` / `is_creator5_pro` / `pid` from the same value. This is the runtime gate — used by `switch.py` for LED availability and by `sensor.py` / `select.py` for model-identity capability gating.
  - Both gates are needed: the config-flow gate stops unsupported hardware from being added at all; the runtime gate keeps capability flags accurate after pairing. Do NOT substring-match `info.name` — it's user-mutable and broke detection in v1.1.8 (see issue #13 / v1.1.9 fix). When new modern PIDs ship, update `SUPPORTED_PIDS` here AND coordinate a library bump.
- **Error handling** – Wrap connection issues in `ConfigEntryNotReady`, `ConnectionError`, or `UpdateFailed` so Home Assistant retries gracefully.
- **Entity additions**
  - Add to the appropriate entity tuple.
  - Provide unique `key`, icon, units, and defensive `value_fn`.
  - Update documentation (README, CHANGELOG, CLAUDE/AGENTS) and translations.
- **Options flow** – Currently exposes the scan interval and the LED-availability override. Extend cautiously to avoid breaking existing entries.

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
- **Testing Without Home Assistant**: Use `tests/ha_mocks.py` for cross-platform unit tests. Home Assistant is Unix-only (requires `fcntl`) and cannot install on Windows. Mocking enables Windows development and fast CI without 500+ MB HA installation.
- **Two-Tier Testing**: Unit tests (Tier 1) validate business logic without HA runtime. Integration tests (Tier 2) require WSL/Linux and are deferred until needed. See TEST_PLAN.md for full strategy.
- **WSL2 Discovery**: Requires mirrored networking (`networkingMode=mirrored` in `.wslconfig`) AND Hyper-V firewall rule (`Set-NetFirewallHyperVVMSetting`) to receive UDP responses from printers
- **Editable Installs**: Both integration (symlinked) and API (`pip install -e`) are editable - changes apply immediately without reinstall
- **Config Entry Lifecycle**: Always use `ConfigEntryNotReady` for temporary connection failures (HA will retry automatically)
- **Entity Availability**: Set `available = False` when printer offline (Silver quality requirement)
- **HACS Testing**: Use `homeassistant-prod/` environment to test real user installation flow (not tracked in git)

## References
- **Home Assistant Development**: Use the `home-assistant-dev` skill for all HA integration work
- **Companion API**: https://github.com/GhostTypes/ff-5mp-api-py

Keep this document in sync with reality so every coding agent starts with the same, accurate context.
