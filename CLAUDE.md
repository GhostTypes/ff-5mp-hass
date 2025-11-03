# CLAUDE.md

Guidance for AI coding assistants working in this repository.

## Current State (January 2025)
- Integration **version 1.0.1** is published and HACS-ready.
- Provides a complete Home Assistant experience for FlashForge printers using the **HTTP API only**.
- Entities shipped: **28 total** (18 sensors, 4 binary sensors, 2 switches, 3 buttons, 1 MJPEG camera).
- UI config flow supports automatic discovery, manual entry, credential validation, and an adjustable polling interval (5–300 s, default 10 s).
- Depends on `flashforge-python-api>=1.0.0` from the companion repository `ff-5mp-api-py`.

Treat this file as the living source of truth for workflows and expectations—update it whenever the process changes.

## Repository Layout Reference
- `custom_components/flashforge/` – Integration source (entities, coordinator, config flow, localization).
- `homeassistant/` – Local Home Assistant sandbox (virtualenv, config, launch scripts) for manual validation.
- `scripts/` – Utility scripts for network discovery and diagnostics.
- `README.md` – Public documentation aligned with the published build.
- `CHANGELOG.md` – Release history (must match `manifest.json` versioning).
- `CLAUDE.md`, `AGENTS.md` – AI-facing playbooks; keep them synchronized.
- `HOME_ASSISTANT_DOCS_COMPANION.md` – Quick links and reminders from the official HA docs.
- `HACS_PUBLISHER_COMPANION.md` – Condensed guide to HACS publisher requirements.

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
- **Local Home Assistant instance**
  - Windows: `homeassistant\start-homeassistant.bat`
  - WSL/Linux/macOS: `./homeassistant/start-homeassistant.sh`
  - Logs: `homeassistant/config/home-assistant.log` (tail for live debugging).
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

## Helpful References
- HACS publishing guide – https://hacs.xyz/docs/publish/integration/
- Home Assistant developer docs – https://developers.home-assistant.io/docs/
- Companion API repo – https://github.com/GhostTypes/ff-5mp-api-py
- In-repo docs – `README.md`, `CHANGELOG.md`, `CLAUDE.md`, `AGENTS.md`, `homeassistant/README.md`, `HOME_ASSISTANT_DOCS_COMPANION.md`, `HACS_PUBLISHER_COMPANION.md`.

Keep this document in sync with reality so every coding agent starts with the same, accurate context.
