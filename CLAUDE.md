# CLAUDE.md

Guidance for AI coding assistants working in this repository.

## Current State (September 2026)
- Integration **version 1.6.0** (CHANGELOG dated 2026-09-27). Previous published release: 1.5.0 (2026-08-14). Releases fire on a `v*` tag push — `.github/workflows/release.yml` extracts the matching `## [X.Y.Z]` CHANGELOG section for the notes, so the section must exist before the tag is pushed.
- **1.6.0 adds the 3MF upload (`upload.py`), and it is NOT yet tested on real hardware.** A Creator 5 owner will test it. Treat the per-model upload dispatch as unconfirmed until that report arrives.
- Ships a **Lovelace card** (`frontend/ff-job-card.js`) for starting prints with material matching — from the printer's recent-file list, or from a sliced 3MF the user uploads. Served and registered by the integration itself — no separate HACS entry, no Lovelace resource step.
- **Languages: English + German**, for the integration (`translations/`) and independently for the card (`frontend/translations/`). Both follow the user's HA profile language. German contributed by @RedAces in PR #19.
- Provides a complete Home Assistant experience for FlashForge printers using the **HTTP API only**.
- Entities shipped: **56 total** (38 sensors, 5 binary sensors, 2 switches, 4 buttons, 1 select, 1 MJPEG camera, 5 images — the g-code thumbnail plus 4 Material Station slot color swatches).
- Diagnostics download supported (`diagnostics.py`), with credentials and identifiers redacted.
- Reauthentication and reconfigure flows supported in addition to the original setup paths.
- UI config flow supports automatic discovery, manual entry, credential validation, and an adjustable polling interval (5–300 s, default 10 s).
- Depends on `flashforge-python-api>=1.6.0` from the companion repository `ff-5mp-api-py`. The 1.6.0 floor is load-bearing for the upload: it adds `flashforge.threemf.parse_3mf` (the 3MF reader `upload.py` uses), and it fixes the upload methods so they open files off the event loop and no longer hit aiohttp's 5-minute total timeout on a large file over slow Wi-Fi. It also carries everything the older floors guaranteed (the 1.3.5 `"pause"` status mapping for the Creator 5 Pro clog fix, and the 1.3.4 range-validation removal). The completion-time state check stays in the integration anyway (see *Print Completion Time* below).

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
  - **Starting local prints** from the job card: the printer's ten most recent files (5M / 5M Pro / AD5X), with per-file metadata and per-tool material data where the model reports it (**AD5X only**), plus the tool-to-slot material matching dialog that model needs. The Creator 5 series gets **no file list**: the firmware can start a stored file, but it does not report which tools that file uses, so no third-party client can build correct material mappings for it. Starting it without mappings prints each tool from the slot with the slicer's filament number, whatever is loaded there. The server-side dispatch (`job.py` → `start_creator5_job`) is unchanged and still works if a client calls it directly — the card just does not offer it. Ported from FlashForgeUI-Electron's job picker + material-matching dialog.
  - **Uploading a sliced 3MF** from the job card (all models, since 1.6.0). The card's **Upload 3MF** button POSTs the file to `/api/flashforge/upload` (XHR for upload progress, bearer token, multipart `entry_id` first, then `file`). `upload.py` streams it to a scratch dir (`<system temp>/flashforge-hass-uploads/<upload_id>/<name>`), caps it at 500 MB, and parses it with `flashforge.threemf.parse_3mf`. The response has the `job/prepare` shape, so the card reuses the same matching / confirmation dialog, pre-filled by `auto_match`. Per-model dispatch mirrors FlashForgeUI / FlashForgeWebUI:
    - **Creator 5 / 5 Pro** — `upload_file_creator5` with `start_print=False`, `use_matl_station=True`, `gcode_tool_cnt` = tool count and **no** upload mappings (the firmware keeps upload-time mappings until the next print ends), then `start_creator5_job` with a mapping for every tool. A station report and per-tool data are required.
    - **AD5X with a station reported** — `upload_file_ad5x` with the mappings, starting at once.
    - **AD5X without a station, and 5M / 5M Pro** — plain `upload_file`, starting at once, no matching.
    - Options: bed leveling only (the card's existing checkbox).

    **On the Creator 5 series the upload is the card's only way to print**; the card shows "This printer can only print files you upload. Upload a sliced 3MF to match its materials and start it." in place of the file list. On other models the Upload button sits next to Start print.
    Refusals (`UploadError`, shown verbatim in the card): non-`.3mf` names or names with path separators, empty files, over 500 MB, not a ZIP, a project 3MF with no sliced G-code, a multi-plate 3MF, a file that uses filament 5 or higher on a station printer, a Creator 5 whose station is not reporting, a station-printer file with no filament data. Warnings (never block): the file was sliced for another model (`model_mismatch`, from the 3MF's printer model id), and the slicer's own warnings. Staged files are deleted after a successful start, on dialog close (`upload/discard`), after a 30-minute TTL, and on the first upload of a run (leftovers from a previous run). The TTL timer skips a file that is being sent (`in_progress`) and checks it again every minute, so a send that fails after the TTL still gets its file deleted. At most 8 uploads wait at once (HTTP 429 above that). A failed send keeps the staged file so the user can retry.
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
- `job.py` – Local print jobs: normalizing `/gcodeList` entries and Material Station slots for the card, the material-matching rules, and the per-model print-start dispatch (Creator 5 → `start_creator5_job`; AD5X → multi- or single-color; 5M → `print_local_file`). **This module is the authority on matching, not the card.**
- `websocket.py` – The card's backend. Registers `flashforge/entries`, `flashforge/files/list`, `flashforge/file/thumbnail`, `flashforge/job/prepare`, `flashforge/job/start`, plus `upload.py`'s `flashforge/upload/start` and `flashforge/upload/discard`, and the `FlashForgeUploadView` HTTP view. `job/start` re-fetches the file list and re-reads the live slots, re-deriving every material name and color rather than trusting the client's payload.
- `upload.py` – The 3MF upload path (1.6.0). `FlashForgeUploadView` (`POST /api/flashforge/upload`, `requires_auth = True`, any logged-in user) streams the file to disk — never into memory — and parses it with `flashforge.threemf.parse_3mf`. `threemf_to_file_entry()` converts the parsed file to the `job.file_to_dict` shape so the `job.py` rules apply unchanged. `upload_plan()` picks the per-model path (`creator5` / `ad5x_station` / `plain`) or raises `UploadError`. `UploadStore` holds staged files by opaque id with the TTL and the 8-upload cap. `flashforge/upload/start` refuses while the printer is in `BUSY_STATES`, re-runs `upload_plan()` against the live slots, and re-validates the mappings with `job.validate_mappings()`. `flashforge/upload/discard` deletes a staged file. `MAX_UPLOAD_BYTES` must match `MAX_UPLOAD_MB` in `ff-job-card.js` (the card checks only to fail fast).
- `card.py` – Serves the whole `frontend/` **directory** via `StaticPathConfig` (the card fetches its own translations from under it) and registers the JS with `frontend.add_extra_js_url`, once per HA run, cache-busted by the manifest version. Also owns `_async_notify_if_reload_needed()`, the one-time "reload this page" persistent notification — HA cannot add a module to an already-open tab, so the notification is the only channel that reaches one. Keyed on card version via a `Store`: fires on install/upgrade, silent on restart.
- `frontend/ff-job-card.js` – The job card. Vanilla custom element, **no build step** — the committed file is the shipped file. Bump `CARD_VERSION` alongside the manifest. Carries **no user-facing copy**; every string is looked up through `this._t(key, vars)` / `this._t.plural(key, count)`.
- `frontend/translations/<lang>.json` – The card's copy. Fetched at runtime from `hass.locale.language` (primary subtag only: `de-CH` loads `de.json`), cached per language across all cards on a dashboard. `en.json` is the per-key fallback, so a lagging translation degrades one string at a time. Adding a language is exactly one new file — no JS, no Python. Fetch outcomes are cached selectively: a 404 sticks (settled until the next release changes `?v=`), a *failed* request is dropped and retried with backoff, so one blip during an HA restart cannot pin the card to English for the life of the page. If the files cannot be served at all, `t()` returns the key rather than an empty string — a strange label is a legible failure, a blank card is not.
- `diagnostics.py` – HA diagnostics download payload, with `check_code`, `serial_number`, MAC/IP, and cloud registration codes redacted.
- `util.py` – Shared helpers: `async_close_flashforge_client()` for HTTP session disposal, `build_device_info()` for the per-platform device-info dict.
- `strings.json` / `translations/<lang>.json` – Home Assistant-side UI copy (entities, config flow, errors). Keep `strings.json` and `translations/en.json` synchronized; `tests/unit/test_translations.py` enforces it. Every entity carries a `translation_key`; `name`s never set manually on entities. Shipping: English, German (`de.json`, contributed by @RedAces).

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
   - **Never put user-facing copy in `ff-job-card.js`.** Card strings go in `frontend/translations/en.json` and are read via `this._t(...)`; a literal in the JS is invisible to translators and cannot be fixed without a code change. `tests/unit/test_translations.py` catches orphaned keys but cannot catch a hardcoded string — review for it.
   - Adding a card string means adding it to `en.json` only. Other languages fall back to English until someone translates them; do **not** machine-translate the other files to keep them "complete".
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

**Current coverage (282 tests total):**
- `tests/unit/test_upload.py` – the 3MF upload path (67 tests): file-name checks, staging and the 500 MB cap, refusals, per-model upload plans and dispatch, the busy-state and mapping re-validation in `upload/start`, discard, the TTL, and the 8-upload cap. Uses the `HomeAssistantView` stub in `tests/ha_mocks.py`.
- `tests/unit/test_translations.py` – every translation file against English: key sets, `{placeholder}` sets, plural pairs, and that no card string is orphaned
- `tests/unit/test_job.py` – material matching rules, auto-match suggestions, per-model print-start dispatch
- `tests/unit/test_websocket.py` – the job card's websocket commands, including the refusal to start a material-station print without mappings
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
5a. Add the **FlashForge Print Job** card to a dashboard (card picker → search "FlashForge"), confirm the file list, thumbnails and metadata load, then start a print:
   - single-material file → confirmation dialog only;
   - multi-material file on an **AD5X** → matching dialog with the mapping pre-filled; verify a PLA tool cannot be mapped to a PETG slot, that an empty slot is unselectable, and that a color mismatch warns but still starts.
   - **Creator 5 / Creator 5 Pro** → the card shows "This printer can only print files you upload. Upload a sliced 3MF to match its materials and start it." with no file list and no Start button, only **Upload 3MF**. The Material Station slot swatch entities must still be populated (they come from `/detail`).

   Then test **Upload 3MF** on each model (new in 1.6.0, not yet confirmed on hardware):
   - **Creator 5 / Creator 5 Pro** → upload a sliced multi-material 3MF. The progress bar moves, then the matching dialog opens with the tools read from the file and a pre-filled mapping. Start it and confirm on the printer that each tool prints from the slot you mapped (not from the slot with the slicer's filament number).
   - **AD5X with a Material Station** → upload a multi-material 3MF. The matching dialog opens; the same rules apply as for listed files. Start it and confirm the mapping on the printer.
   - **5M / 5M Pro** → upload a 3MF. A confirmation dialog opens (no matching). Start it; the print starts and the file appears at the top of the list.
   - **Refusals** → upload a project 3MF (no sliced G-code) and a multi-plate 3MF. Each is refused with a clear message, and nothing is left in `<system temp>/flashforge-hass-uploads/`.
   - **Cancel** → start a large upload and press **Cancel** during the upload. Confirm the staged file is deleted from `<system temp>/flashforge-hass-uploads/`. Also close a dialog after the upload ends, without starting; that file must be deleted too.
6. Observe coordinator error handling by temporarily disconnecting the printer and confirming entities surface availability correctly.

### Testing Utilities

- **Discovery diagnostics** – `scripts/test_discovery.py` and `scripts/discovery_probe.py` help debug LAN communication without HA.
- **Hardware caveat** – Full verification requires a FlashForge printer with LAN mode enabled; simulated runs only confirm flow logic.

## Implementation Guard Rails
- **HTTP-first policy** – Do not introduce direct TCP/G-code communication here. If unavoidable, extend the API library (`ff-5mp-api-py`) and consume it via HTTP-style helpers.
- **Coordinator as source of truth** – Entities derive state from the coordinator’s latest `FFMachineInfo`. Avoid storing custom copies of printer state in entities.
- **PID for model identity, never the printer name** – Modern HTTP printers report a stable firmware-set integer `pid` on `/detail` (35 = Adventurer 5M, 36 = 5M Pro, 38 = AD5X, 40 = Creator 5, 41 = Creator 5 Pro). The integration enforces this in TWO places that should both stay in sync:
  - `config_flow.py` `_is_supported_detail()` reads the raw `/detail` payload during pairing and rejects PIDs not in `SUPPORTED_PIDS = {35, 36, 38, 40, 41}`. This is the early gate, and "early" is load-bearing: it consumes `client.info.get_detail_raw()` (the undecoded JSON dict), so it runs before **any** validation, not just before `FFMachineInfo` parsing. Until v1.3.4 it read `pid` off a parsed `FFPrinterDetail`, which meant a supported Creator 5 could be turned away because an unrelated field (`chamberTemp: -108`) failed validation first — see issue #18. Never move this gate back onto a parsed model.
  - The library (`flashforge-python-api>=1.3.4`) populates `FFMachineInfo.is_pro` / `is_ad5x` / `is_creator5` / `is_creator5_pro` / `pid` from the same value. This is the runtime gate — used by `switch.py` for LED availability and by `sensor.py` / `select.py` for model-identity capability gating.
  - Both gates are needed: the config-flow gate stops unsupported hardware from being added at all; the runtime gate keeps capability flags accurate after pairing. Do NOT substring-match `info.name` — it's user-mutable and broke detection in v1.1.8 (see issue #13 / v1.1.9 fix). When new modern PIDs ship, update `SUPPORTED_PIDS` here AND coordinate a library bump.
- **The job card is an untrusted client** – Every matching rule enforced in `ff-job-card.js` is enforced again in `job.py`, which re-derives materials and colors from the file list and the live station report. The JS copy exists to explain the rule as the user clicks; the Python copy is what decides. A websocket client that skips the dialog entirely must not be able to start a material-station print without mappings — `ws_start_job` refuses it. **The upload path is an untrusted client too:** `ws_upload_start` re-runs `upload_plan()` against the live station report, re-validates the mappings with the same `job.validate_mappings()` rules, re-derives material names and colors server-side, and refuses a matching-required upload that arrives with no mappings. The HTTP view re-checks the file name and the 500 MB cap even though the card checks both first. When you change a rule, change both, and add the test to `tests/unit/test_job.py` (or `tests/unit/test_upload.py` for upload-only rules).
- **File listing is capped at ten files, deliberately** – `/gcodeList` returns the ten most recent files and nothing more; the full local listing exists only over TCP `M661`, which this integration does not speak. This will read as a bug report eventually; it is the documented cost of the HTTP-only policy, not an oversight.
- **`gcodeListDetail` is AD5X-only — the Creator 5 series does NOT report per-tool material data** – Only the AD5X answers `/gcodeList` with a `gcodeListDetail` array; the 5M / 5M Pro **and the Creator 5 / Creator 5 Pro** return bare file names. Confirmed against a real Creator 5 Pro (raw response, 2026-08-05) after the opposite was assumed for three releases. The consequence is structural: `requires_material_matching()` needs both slots *and* `tool_datas`, so a Creator 5 always takes the confirmation path, and no amount of work in this repo can change that — the input does not exist. It is a firmware regression, not a gap in the port: the AD5X is the newer *feature* here despite being the older printer. Do not "restore" C5 matching on listed files by inferring tools from the slot report or the file name; a mapping the printer did not describe is a guess sent to a machine. **C5 matching happens at upload time, in this integration too (since 1.6.0):** `upload.py` parses the 3MF locally, before it reaches the printer, and the tools come from the file itself — the same approach as FlashForgeUI-Electron and FlashForgeWebUI. That is why the card offers only the upload on the Creator 5 series and hides the recent-file list there. The Material Station slot entities are unaffected: they come from `/detail`, which the C5 populates fully.
- **Error handling** – Wrap connection issues in `ConfigEntryNotReady`, `ConnectionError`, or `UpdateFailed` so Home Assistant retries gracefully.
- **"Could not read the answer" is not "could not reach the printer"** – The library returns `None` when a request never got through and raises `FlashForgeResponseError` when the printer answered with a payload it could not parse. Keep the two apart all the way to the user: the config flow maps the exception to `invalid_response` (never `cannot_connect`), and `__init__.py` / `coordinator.py` log it with wording that sends the user to the issue tracker rather than to their router. Collapsing them is what made issue #18 take three releases — the printer was reachable and the credentials were correct the entire time, but every message on offer said otherwise.
- **Never constrain the *range* of data received from the printer** – This applies to the API library, but the integration is what breaks when it is violated. Pydantic validates a model all-or-nothing, so a `ge=`/`le=` on any one of ~50 `/detail` fields can fail the whole response and take every entity offline. Firmware also signals absent hardware with out-of-band sentinels (`chamberTemp: -108`) rather than by omitting the field, so "impossible" values are normal. Inbound models validate types only; range constraints belong on outbound command models, where a bad value is our own bug. If a new field needs bounds, normalize it in the parser, don't reject it.
- **Print Completion Time is gated on an actively advancing print, and the gate lives here** – `ADVANCING_STATES` in `sensor.py` contains `PRINTING` and nothing else, so `sensor.<printer>_print_completion_time` is `unknown` in every other state. The library derives that value as `now() + estimated_time`, a conversion that only holds still while the firmware counts `estimated_time` down; it freezes that field the moment the print stops advancing, so the sensor stepped forward a minute per minute and receded for as long as a pause lasted. **`HEATING` is excluded along with the paused states** — the pre-print warmup does not advance the job either and drifts identically, just for minutes rather than hours. `remaining_time` is unaffected and stays correct throughout a pause; it is the reading that remains meaningful there. Keep the check in the integration even though `flashforge-python-api` 1.4.0+ (and so the current 1.6.0 floor) returns `None` itself: the rule belongs to this sensor, and keeping it here means a library regression cannot bring the drift back. Do not "restore" a value during a pause by widening the set.
- **Gate capabilities on what the printer reported, not on its model family** – Options exist within a family: the heated chamber is a Creator 5 extra, so chamber entities gate on `has_chamber_sensor`, not `is_creator5`. Model identity is the right signal only for things the model genuinely cannot do at all (filtration, the Creator 5 camera switch).
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
