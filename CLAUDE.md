# CLAUDE.md

Guidance for AI coding assistants working in this repository.

## Current State (May 2026)
- Integration **version 1.3.0** (in-flight; not yet tagged).
- Provides a complete Home Assistant experience for FlashForge printers using the **HTTP API only**.
- Entities shipped: **58 total** (38 sensors, 5 binary sensors, 2 switches, 5 buttons, 2 selects, 1 MJPEG camera, 5 images — the g-code thumbnail plus 4 Material Station slot color swatches).
- One service: `flashforge.print_file` (entity service on the Local File Selection entity).
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
  - Options flow exposes the LED-availability override, the pre-print bed-leveling default, and adjustable polling (5–300 s).
- **Monitoring**
  - 38 sensors covering status, temperatures (per-toolhead on the Creator 5 series, plus a heated chamber), progress, layers, timing, filament metrics, fan speeds, air quality (5M Pro / Creator 5 Pro TVOC), active Material Station slot, print completion time, lifetime stats, plus diagnostic sensors (`firmware_version`, `free_disk_space`, `ip_address`, `error_code`).
  - 5 binary sensors tracking printing, online, error, paused, and door-open (Creator 5 Pro only) states.
  - 1 image entity for the active g-code thumbnail (fetched on demand, cached per filename).
  - 4 Material Station slot image entities (AD5X / Creator 5 series) — labeled color swatches (filament hex color + material name overlay) rendered with Pillow in an executor and cached per `(material, color)` tuple.
  - Entities grouped under a single device with manufacturer/model metadata.
- **Control**
  - LED switch with capability detection (graceful "unavailable" for unsupported models, with an option to override the check).
  - Filtration as a `select` entity with Off / Internal / External states (AD5X only).
  - Pause / resume / cancel / clear-status buttons with post-action refresh.
  - Local file printing: a `select` listing the printer's files, a "print selected file" button, and the `flashforge.print_file` service.
  - MJPEG camera entity targeting `http://<ip>:8080/?action=stream`.
- **Architecture**
  - HTTP API only (`FlashForgeClient.info/control/job_control/files`).
  - `DataUpdateCoordinator` refresh loop with error recovery and client cleanup; a second, slower coordinator for the file list.
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
- `coordinator.py` – `FlashForgeDataUpdateCoordinator` wrapping `FlashForgeClient.info.get()` with graceful error handling and cleanup, plus `FlashForgeFileListCoordinator` polling `files.get_recent_file_list()` on the slower `FILE_LIST_SCAN_INTERVAL` (it also holds the file selected for printing and never closes the shared client).
- `sensor.py` – 28 sensor entities (operational + diagnostic). Modify the `SENSORS` tuple, translations, and docs together when changing sensors.
- `binary_sensor.py` – 4 machine-state binary sensors (printing, online, error, paused).
- `switch.py` – LED switch with client capability check (capability check can be overridden via options).
- `select.py` – Filtration mode select (Off / Internal / External, AD5X only) and the Local File Selection entity (`FlashForgeFileSelect`, options = the printer's file list, metadata in `extra_state_attributes`). Also registers the `flashforge.print_file` entity service.
- `button.py` – Pause / resume / cancel / clear-status commands plus `FlashForgePrintSelectedFileButton`; request a refresh after each action.
- `print_job.py` – Per-model dispatch for starting a file already on the printer (`start_creator5_job` / AD5X single+multi color / `print_local_file`) and `build_material_mappings()`, which derives Material Station mappings from the file's tool data plus the printer's slot colors. Raises `ServiceValidationError` instead of guessing an incomplete mapping. **Per-file metadata is model-dependent**: the AD5X returns `gcodeListDetail` (print time, weight, per-tool material data), a Creator 5 Pro returns plain file names — verified on hardware with `scripts/file_print_probe.py`. Unknown values must stay unknown (`select.file_attributes()` omits them); treating them as `0`/`False` would make a multi-material file look single-material. A Creator 5 Pro was confirmed to accept and start a three-material file sent **without** `materialMappings` — the firmware falls back to the assignment stored in the 3MF, so no mapping input is needed on that model. The resulting color assignment itself is unverified (the test job was cancelled right after the start).
- `services.yaml` – Service definition for `flashforge.print_file` (keep in sync with the `services` block in `strings.json`).
- `camera.py` – MJPEG camera entity (`http://<ip>:8080/?action=stream` by default).
- `image.py` – Hosts the active-print g-code thumbnail entity AND the 4 Material Station slot swatch entities (AD5X / Creator 5 series). Swatches are PNG-encoded by `render_swatch_bytes()` (Pillow) inside an executor; both entity types cache rendered bytes and only invalidate on input change.
- `diagnostics.py` – HA diagnostics download payload, with `check_code`, `serial_number`, MAC/IP, and cloud registration codes redacted.
- `util.py` – Shared helpers: `async_close_flashforge_client()` for HTTP session disposal, `build_device_info()` for the per-platform device-info dict, `has_material_station()` for Material Station capability detection (see the guard rails — the raw `has_matl_station` flag is unreliable).
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

**Current coverage (161 tests total):**
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
- `tests/unit/test_file_list_coordinator.py` – local file list fetch, filtering, and error paths
- `tests/unit/test_print_job.py` – per-model print-start dispatch and Material Station mapping
- `tests/unit/test_print_file_entities.py` – print file select + print button behavior
- `tests/unit/test_material_station_gating.py` – Material Station capability detection (Creator 5 Pro reports no `hasMatlStation` flag) and deferred entity creation for image + sensor platforms

**Test dependencies** (`requirements-test.txt`):
- Core: `pytest`, `pytest-asyncio`, `pytest-cov`
- Snapshot testing: `syrupy` (for future use)
- Schema validation: `voluptuous` (config flow + service schemas)
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
   - Binary sensors: printing, online, error, paused.
   - Switch: LED (may show unavailable on unsupported models unless override is enabled).
   - Select: filtration mode — Off / Internal / External (AD5X only); Local File Selection — lists the printer's files.
   - Buttons: pause, resume, cancel, clear status, print selected file (errors when pressed with nothing selected).
   - Service: `flashforge.print_file` on the Local File Selection entity, with and without `file_name` / `leveling_before_print`.
   - Camera: MJPEG feed reachable.
   - Image: g-code thumbnail of the active print.
   - Image (AD5X only): four IFS slot swatches (`image.*_ifs_slot_1..4`) showing material color + label, "EMPTY" tile for unloaded slots.
5. Trigger control actions (pause/resume/cancel, switches) and ensure states refresh.
6. Observe coordinator error handling by temporarily disconnecting the printer and confirming entities surface availability correctly.

### Testing Utilities

- **Discovery diagnostics** – `scripts/test_discovery.py` and `scripts/discovery_probe.py` help debug LAN communication without HA.
- **File list / print start** – `scripts/file_print_probe.py` runs the integration's own `print_job` code against a real printer without a HA runtime (it borrows `tests/ha_mocks.py`). Read-only by default; `--raw` dumps the untouched `/gcodeList` payload and how the library's pydantic models parse it; `--print <file> --yes` actually starts a print.
- **Hardware caveat** – Full verification requires a FlashForge printer with LAN mode enabled; simulated runs only confirm flow logic.

## Implementation Guard Rails
- **HTTP-first policy** – Do not introduce direct TCP/G-code communication here. If unavoidable, extend the API library (`ff-5mp-api-py`) and consume it via HTTP-style helpers. This is why the file list uses `files.get_recent_file_list()` (HTTP `/gcodeList`, most recent files only) instead of `files.get_file_list()`, which falls back to a TCP/8899 directory listing on the 5M family. The `flashforge.print_file` service accepts a free-form `file_name` so files outside that list stay printable.
- **Coordinator as source of truth** – Entities derive state from the coordinator’s latest `FFMachineInfo`. Avoid storing custom copies of printer state in entities.
- **PID for model identity, never the printer name** – Modern HTTP printers report a stable firmware-set integer `pid` on `/detail` (35 = Adventurer 5M, 36 = 5M Pro, 38 = AD5X). The integration enforces this in TWO places that should both stay in sync:
  - `config_flow.py` `_is_supported_detail()` reads the raw `/detail` payload during pairing and rejects PIDs not in `SUPPORTED_PIDS = {35, 36, 38}`. This is the early gate — runs before any `FFMachineInfo` parsing happens.
  - The library (`flashforge-python-api>=1.2.3`) populates `FFMachineInfo.is_pro` / `is_ad5x` / `pid` from the same value. This is the runtime gate — used by `switch.py` for LED / filtration availability.
  - Both gates are needed: the config-flow gate stops unsupported hardware from being added at all; the runtime gate keeps capability flags accurate after pairing. Do NOT substring-match `info.name` — it's user-mutable and broke detection in v1.1.8 (see issue #13 / v1.1.9 fix). When new modern PIDs ship, update `SUPPORTED_PIDS` here AND coordinate a library bump.
- **Capability flags: never trust a raw `/detail` field on its own** – Several `FFMachineInfo` fields are straight copies of the printer's JSON and are simply absent on some models. `has_matl_station` is the known case: a Creator 5 Pro (pid 41) leaves `hasMatlStation` out of `/detail` entirely (it parses as `None`) while `matlStationInfo` reports four loaded slots, so gating on the flag hid the Material Station entities on exactly the models v1.3.0 added them for. Gate on `util.has_material_station()`, which also accepts populated slot data as proof. When adding a capability gate, derive it from the data the capability actually produces, and verify with `scripts/file_print_probe.py --raw` (dumps the untouched `/detail` and `/gcodeList` payloads) before trusting a single field.
- **Capability-gated entities must survive a late capability** – Platforms are only set up once, so deciding availability from `coordinator.data` at setup time permanently drops entities when the first refresh failed or the capability reported in late. `sensor.py` and `image.py` re-check on coordinator updates via `coordinator.async_add_listener` and add the entities when the gate first passes; follow that pattern for new conditional entities instead of filtering once in `async_setup_entry`.
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
