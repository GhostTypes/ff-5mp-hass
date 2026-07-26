# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.2] - 2026-07-26

### Changed

- **The camera switch is no longer created on the Creator 5 series.** v1.3.1 made `switch.<printer>_camera` *available* on those models, but hardware testing on a Creator 5 Pro (firmware 1.9.4) confirmed the API can no longer act on it: `streamCtrl_cmd` with `action: close` answers `{"code": 0, "Success"}` while port 8080 keeps serving live MJPEG frames 22 seconds later, and `cameraStreamUrl` never changes. The switch could not reflect an off state either — `is_on` reads that same always-present URL, so the next poll flipped it straight back to `on`. Rather than ship a control that silently does nothing, the switch is now omitted entirely on the Creator 5 / Creator 5 Pro; the `camera` entity itself is unaffected and continues to stream. Refs [#17](https://github.com/GhostTypes/ff-5mp-hass/issues/17).

### Fixed

- **Material Station entities now appear on the Creator 5 series.** The four slot swatches (`image.<printer>_ifs_slot_1..4`) and the Active Material Station Slot sensor were gated on `FFMachineInfo.has_matl_station`, which was a straight copy of the raw `hasMatlStation` field from `/detail`. A Creator 5 Pro does not report that field at all — verified on real hardware (pid 41, firmware 1.9.4), where it is absent from `/detail` entirely while `matlStationInfo` reports `slotCnt: 4` and four loaded slots. The flag parsed as `None`, the entities were never created, and the v1.3.0 change that moved the gate off `is_ad5x` had no effect on this model. Fixed in the library (`flashforge-python-api` 1.3.2), which now derives the capability from the slot data; the minimum requirement is raised accordingly.
- **Capability-gated entities are no longer decided once at setup.** The Material Station slot images and every `availability_fn`-gated sensor are now also added when their capability first shows up on a later refresh. Platform setup can run before the printer has reported a capability, and the first refresh may fail outright — either case previously left the printer permanently without those entities.

- **The LED switch is no longer greyed out on every printer.** The "Always show LED switch" option was passed to the library as `led_control_override` using its unset value `False`. That parameter is tri-state — `None` means "no override", `True` forces the capability on, and `False` forces it **off** — so with the option switched off, which is the default, the integration overrode the printer's own correct capability report and pinned `client.led_control` to `False` on every model. The switch stayed unavailable, and the library additionally refused `set_led_on()` / `set_led_off()` internally, which made enabling the override look like the only way to get a working switch: `True` was the only value that got past the veto. The option now sends `None` when off and `True` only when the user asks for it, which is what it was always meant to do. Reported and diagnosed on a Creator 5 Pro, where `/product` correctly reports `lightCtrlState: 1` all along. Refs [#17](https://github.com/GhostTypes/ff-5mp-hass/issues/17).

## [1.3.1] - 2026-07-23

### Fixed
- **Camera switch now available on the Creator 5 series.** The camera power toggle (`switch.<printer>_camera`) was permanently `unavailable` on Creator 5 / Creator 5 Pro because its availability was gated solely on `client.is_pro` (Adventurer 5M Pro only). The gate now ORs `is_pro` and `is_creator5_pro`, matching the model-identity capability gating already used in `select.py` / `sensor.py`. Refs [#17](https://github.com/GhostTypes/ff-5mp-hass/issues/17).

### Documentation
- Clarified that the serial number entered during manual setup (and referenced in troubleshooting) must include the `SN` prefix (e.g. `SN123456789`), matching the value shown on the printer's settings screen rather than treating `SN` as a sticker label. Refs [#14](https://github.com/GhostTypes/ff-5mp-hass/issues/14).

## [1.3.0] - 2026-06-28

### Added
- **Creator 5 / Creator 5 Pro support.** Both models are now recognized via their firmware PIDs (40 = Creator 5, 41 = Creator 5 Pro) in discovery, manual setup, and the device model display. The library (`>=1.3.0`) drives these via an HTTP-only transport (the Creator 5 series exposes no TCP/8899 service).
- **Per-toolhead temperature sensors (Creator 5 series).** 8 new sensors: `tool_1_temperature`…`tool_4_temperature` (current) and `tool_1_target_temperature`…`tool_4_target_temperature` (target), one per toolhead on the 4-tool tool-changer. Gated to the Creator 5 series.
- **Heated chamber sensors (Creator 5 series).** `chamber_temperature` and `chamber_target_temperature`, read from the library's `chamber` Temperature pair.
- **Door binary sensor (Creator 5 Pro only).** `binary_sensor.flashforge_door_open` (`device_class=DOOR`) — on when the lid or front door is ajar, off when both are closed. Gated on `has_door_sensor` (Creator 5 Pro only).
- **Diagnostics** now snapshots `is_creator5`, `is_creator5_pro`, and `http_only` alongside the existing capability flags.

### Changed
- **Material Station refactor.** The AD5X-only IFS slot images and the active-slot sensor are now gated on `has_matl_station` instead of `is_ad5x`, so they also render for the Creator 5 series (which reports the same `MatlStationInfo` shape). Display names relabeled from "IFS Slot" to "Material Station Slot"; entity `unique_id`s and translation keys are unchanged, so existing AD5X entities migrate with no registry churn. The image class was renamed `FlashForgeIFSSlotImage` → `FlashForgeMaterialStationSlotImage`.
- **Filtration / TVOC / chamber fan gating moved off the `/product` endpoint.** The printer's `/product` response is unreliable for capability detection — it misreports Creator 5 Pro filtration. These entities are now gated on model identity (`is_pro OR is_creator5_pro`) rather than the `/product`-derived `client.filtration_control` / `is_pro` flags. The `filtration_mode` select's availability now reads from coordinator data instead of the client.
- Bumped `flashforge-python-api` requirement to `>=1.3.0`.

### Fixed
- **`print_completion_time` is now timezone-aware (HA 2026 fix).** The library's `completion_time` can arrive as a naive datetime, which Home Assistant 2026 rejects on `device_class=TIMESTAMP` sensors. Naive values are now stamped with HA's configured default timezone (`dt_util.DEFAULT_TIME_ZONE`); aware values pass through unchanged.

## [1.2.0] - 2026-05-30

### Added
- **AD5X IFS material station entities** (AD5X only):
  - 4 `image` entities, one per slot, that render a labeled color swatch (filament hex color background + material name overlay, e.g. "PLA"). Empty slots render as a neutral "EMPTY" tile. Swatches are PNG-encoded with Pillow on a background executor and cached so re-renders only happen when the slot's material or color changes. Material name, color, and `has_filament` are also surfaced via `extra_state_attributes` for templating.
  - **Active IFS Slot** sensor — integer 1–4 of the slot currently being printed from, 0 when idle.
- **Print Completion Time** sensor (`device_class=TIMESTAMP`) — the absolute wall-clock time at which the active print is expected to finish, rounded to the nearest minute. Only populated while a print is active (printing / heating / pausing / paused); idle otherwise.
- **Cooling Fan Speed** sensor (universal, `%`) — the part-cooling fan duty cycle.
- **Chamber Fan Speed** sensor (Adventurer 5M Pro only, `%`).
- **TVOC** sensor (Adventurer 5M Pro only, `device_class=VOLATILE_ORGANIC_COMPOUNDS`, µg/m³) — air-quality reading from the Pro's onboard sensor.
- **Diagnostic sensors:** `firmware_version`, `free_disk_space`, `ip_address`, and `error_code` (the last disabled by default; pairs with the existing `Error` binary sensor for actionable detail).
- **Diagnostics download support** (`diagnostics.py`) — downloadable from the device page, with `check_code`, `serial_number`, MAC/IP, and cloud registration codes redacted.
- **Reauthentication flow** — when the printer rejects the check code, HA can prompt for a new one without removing and re-adding the integration.
- **Reconfigure flow** — IP and check code can be updated in place (e.g. after a DHCP shift).
- Hardware-only sensors and entities are gated at setup time: AD5X-only entities (the 4 IFS slot images and Active IFS Slot sensor) are only created on AD5X printers; Adventurer 5M Pro-only sensors (TVOC, Chamber Fan Speed) are only created on 5M Pro printers.

### Changed
- **Full entity translations across every platform (Gold quality scale).** Every entity now declares a `translation_key` and resolves its display name (and, where applicable, state values) through `strings.json` / `translations/en.json` instead of carrying a hardcoded `name`. Covers all sensors, binary sensors, the LED switch, all buttons, the filtration select (with translated state labels: Off / Internal / External), the camera, and the image entities. Machine-status sensor states are translated as well (Ready / Busy / Calibrating / Error / Heating / Printing / Pausing / Paused / Cancelled / Completed / Unknown).
- **Sensor type audit** — corrected device classes, units, and value formats so HA renders, graphs, and templates correctly:
  - `machine_status` is now `device_class=ENUM` with explicit `options` (the 11 `MachineState` values), enabling proper UI rendering and history graphs.
  - `elapsed_time` and `remaining_time` now expose **numeric durations in seconds** with `device_class=DURATION`, so templates / automations can do real arithmetic instead of parsing colon strings (e.g. `notify when remaining < 600`). **Breaking:** any user template that depended on the old `"HH:MM"` string format for these will need updating. `lifetime_runtime` remains a human-readable string ("818h:11m") since HA's default sensor card doesn't auto-format DURATION values into a friendly form and a many-digit number of minutes/seconds reads worse than the formatted string.
  - `filament_weight` gained `device_class=WEIGHT` + `UnitOfMass.GRAMS`.
  - `filament_length` and `lifetime_filament` gained `device_class=DISTANCE` + `UnitOfLength.METERS`.
  - `z_offset` now uses `UnitOfLength.MILLIMETERS` (was a literal `"mm"` string).
  - `free_disk_space` is now a numeric `device_class=DATA_SIZE` sensor in `UnitOfInformation.GIGABYTES` (was a pre-formatted string with no unit), matching the printer's reported unit.
  - Nozzle and bed temperature sensors now declare `device_class=temperature` for proper HA UI rendering.
  - `print_speed` now uses the `PERCENTAGE` constant rather than a literal `"%"`.
- Device `model` is now derived from the firmware-set `pid` (35 = Adventurer 5M, 36 = 5M Pro, 38 = AD5X) and resolved dynamically on every read, so it no longer permanently reads "Unknown" if the first refresh fails. Camera and image entities now report the model, which they were previously missing.
- Refactored `device_info` construction into a shared helper, eliminating duplication across all entity platforms.
- Bumped `flashforge-python-api` requirement to `>=1.2.3`. The library now derives `is_pro` / `is_ad5x` on `FFMachineInfo` from the firmware-set `pid` field instead of string-matching the user-mutable printer name, mirroring the v1.1.9 config-flow fix at the API layer ([ff-5mp-api-py CHANGELOG](https://github.com/GhostTypes/ff-5mp-api-py/blob/main/CHANGELOG.md#123---2026-05-08)). Refs [#13](https://github.com/GhostTypes/ff-5mp-hass/issues/13).

## [1.1.9] - 2026-05-08

### Fixed
- Renamed printers were rejected during initial pairing as unsupported because model detection matched against the user-mutable `name` field. Detection now uses the firmware-set `pid` value from `/detail` (35 = Adventurer 5M, 36 = 5M Pro, 38 = AD5X). Refs [#13](https://github.com/GhostTypes/ff-5mp-hass/issues/13).

## [1.1.8] - 2026-05-08

### Added
- New `image` entity exposing the g-code thumbnail of the currently printing file. Fetched on demand via the printer's `/gcodeThumb` HTTP endpoint and cached per-filename so the cache only invalidates when the active file changes.

## [1.1.7] - 2026-04-27

### Fixed
- Resolved "Config flow could not be loaded: Invalid handler specified" on Home Assistant 2026.4.x / Python 3.14 ([#10](https://github.com/GhostTypes/ff-5mp-hass/issues/10)). Root cause: the upstream `flashforge-python-api` depended on `netifaces`, which is source-only on PyPI and has no Python 3.14 wheel — install failed inside the HA environment, the integration's top-level `from flashforge import ...` raised `ImportError`, and HA reported the generic invalid-handler error for both auto-discovery and manual setup paths.
- Bumped `flashforge-python-api` requirement to `>=1.2.2`, which replaces `netifaces` with the pure-Python `ifaddr` library (already a transitive dependency of Home Assistant via `zeroconf`).

## [1.1.6] - 2026-03-23

### Fixed
- Fixed AD5X entities going unavailable while printing due to `currentPrintSpeed` / `printSpeedAdjust` Pydantic validation rejecting values above 200 (AD5X reports up to 500)
- Fixed HTTP connection churn caused by per-request `aiohttp.ClientSession()` creation across all API control modules — now uses a shared session with proper timeout handling
- Fixed intermittent timeouts during print operations by increasing the default HTTP timeout from 5s to 15s
- Updated dependency to `flashforge-python-api>=1.2.1` which includes all of the above upstream fixes (contributed by @spawnegit in [ff-5mp-api-py#12](https://github.com/GhostTypes/ff-5mp-api-py/pull/12))

## [1.1.5] - 2026-03-21

### Added
- Intelligent OEM camera fallback probing for printers that omit `camera_stream_url` from the HTTP `/detail` response
- Coordinator coverage to verify fallback probing only runs when firmware does not already report a stream URL

### Fixed
- Updated the Home Assistant dependency floor to `flashforge-python-api>=1.2.0`, which is now published and includes the camera fallback probe implementation
- Restored automatic camera availability for OEM cameras when firmware leaves the stream URL empty but the standard `http://<printer-ip>:8080/?action=stream` endpoint is reachable

## [1.1.4] - 2026-03-08

### Fixed
- Registered the filtration select platform so `select.flashforge_filtration_mode` now loads correctly
- Restricted discovery and setup to supported modern HTTP printers only: AD5X, Adventurer 5M, and Adventurer 5M Pro
- Corrected the README, support matrix, entity counts, and camera behavior notes for the `1.1.4` release
- Fixed AD5X compatibility when newer firmware returns additional `/detail` fields during setup and polling

### Changed
- Moved the LED availability workaround into `flashforge-python-api` client configuration instead of mutating integration state directly
- Updated dependency to `flashforge-python-api>=1.1.1` for modern-printer discovery improvements, AD5X detection, library-level LED override support, and newer AD5X `/detail` response compatibility
- Preserved the manual LED override for aftermarket LED installs while routing it through the library-level override model used by HACS installs
- Switched the camera entity to runtime OEM stream detection while keeping camera power control limited to Pro models

## [1.1.3] - 2025-12-31

### Added
- Configuration option to manually enable LED control for printers where automatic detection fails

### Changed
- Modernized options flow to align with Home Assistant 2025.12 standards
  - Updated to use revised options flow pattern per [HA developer blog](https://developers.home-assistant.io/blog/2024/11/12/options-flow/)

## [1.1.2] - 2025-12-26

### Fixed
- Fixed print progress sensor always showing 0%
- Fixed incorrect estimated time remaining (ETA) calculations
- Updated dependency to `flashforge-python-api>=1.0.2` with progress and ETA fixes

## [1.1.1] - 2025-12-24

### Fixed
- Updated dependency to `flashforge-python-api>=1.0.1` to fix Pydantic validation error when pairing printers with fractional estimated time values

## [1.1.0] - 2025-01-02

### Added
- **New Select Entity**: Filtration Mode control with three options (Off/Internal/External)
  - Replaces the binary filtration switch with more granular control
  - Supports both internal and external filtration fans independently
  - Only available on models with filtration support (AD5M Pro)
- **New Switch**: Camera power control for Pro models
  - Turn camera on/off via HTTP API
  - Only available on Pro models
- **New Sensors**: Lifetime statistics tracking
  - `sensor.flashforge_lifetime_filament` - Total filament used over printer lifetime (meters)
  - `sensor.flashforge_lifetime_runtime` - Total runtime over printer lifetime (formatted as "Xh:Ym")
- **New Button**: Clear Status button to clear printer errors/warnings
  - Uses `clear_platform()` API method

### Changed
- **Filtration Control**: Migrated from binary switch to select entity for better control
  - Previous: Single on/off switch (only controlled external fan)
  - Now: Select entity with Off/Internal/External options
- Entity count updated: 18 sensors (was 15), 1 switch (was 2), 1 select entity (new), 4 buttons (was 3)

### Documentation
- Updated README with new entity tables
- Added select entity documentation
- Updated Lovelace card examples
- Updated feature list to reflect new capabilities

## [1.0.1] - 2025-01-02

### Changed
- **Major README Overhaul**: Complete rewrite with professional documentation
  - Added comprehensive entity tables with all 15 sensors, 4 binary sensors, switches, buttons, and camera
  - Expanded usage examples with automation templates
  - Enhanced troubleshooting section
  - Added Lovelace card examples
  - Improved installation instructions with screenshots placeholders
- Updated minimum Home Assistant version requirement to 2024.1.0 (from 2023.1.0)

### Fixed
- HACS validation: Removed `content_in_root` field from hacs.json
  - Field was causing validation errors in HACS Action
  - Uses default behavior (false) when omitted

### Documentation
- Complete README.md rewrite with technical specifications
- Added development architecture section
- Enhanced configuration examples
- Expanded troubleshooting guide

## [1.0.0] - 2025-01-02

### Added
- Initial release of FlashForge Home Assistant integration
- HTTP API-based communication (superior to TCP-only implementations)
- UI-based configuration flow with automatic printer discovery
- Support for multiple entity platforms:
  - **Sensors**: Printer state, temperatures, print progress, filename
  - **Binary Sensors**: Printing status, online status
  - **Switches**: LED control, filtration control (model-dependent)
  - **Buttons**: Home axes, pause/resume/cancel print
  - **Camera**: Live printer feed (model-dependent)
- Automatic discovery via UDP broadcast
- Manual IP configuration option
- Model-specific feature detection (AD5M, AD5M Pro, AD4)
- Comprehensive error handling and recovery
- HACS-compatible structure
- Full async implementation using DataUpdateCoordinator

### Documentation
- Complete installation guide (HACS + manual)
- Configuration instructions with LAN mode setup
- Entity documentation and usage examples
- Automation examples
- Troubleshooting guide

### Supported Models
- FlashForge Adventurer 5M Series
- FlashForge Adventurer 4

[Unreleased]: https://github.com/GhostTypes/ff-5mp-hass/compare/v1.3.2...HEAD
[1.3.2]: https://github.com/GhostTypes/ff-5mp-hass/compare/v1.3.1...v1.3.2
[1.3.1]: https://github.com/GhostTypes/ff-5mp-hass/compare/v1.3.0...v1.3.1
[1.3.0]: https://github.com/GhostTypes/ff-5mp-hass/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/GhostTypes/ff-5mp-hass/compare/v1.1.9...v1.2.0
[1.1.9]: https://github.com/GhostTypes/ff-5mp-hass/compare/v1.1.8...v1.1.9
[1.1.8]: https://github.com/GhostTypes/ff-5mp-hass/compare/v1.1.7...v1.1.8
[1.1.7]: https://github.com/GhostTypes/ff-5mp-hass/compare/v1.1.6...v1.1.7
[1.1.6]: https://github.com/GhostTypes/ff-5mp-hass/compare/v1.1.5...v1.1.6
[1.1.5]: https://github.com/GhostTypes/ff-5mp-hass/compare/v1.1.4...v1.1.5
[1.1.4]: https://github.com/GhostTypes/ff-5mp-hass/compare/v1.1.3...v1.1.4
[1.1.3]: https://github.com/GhostTypes/ff-5mp-hass/compare/v1.1.2...v1.1.3
[1.1.2]: https://github.com/GhostTypes/ff-5mp-hass/compare/v1.1.1...v1.1.2
[1.1.1]: https://github.com/GhostTypes/ff-5mp-hass/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/GhostTypes/ff-5mp-hass/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/GhostTypes/ff-5mp-hass/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/GhostTypes/ff-5mp-hass/releases/tag/v1.0.0
