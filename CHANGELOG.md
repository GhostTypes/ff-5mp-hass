# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

[1.0.0]: https://github.com/GhostTypes/ff-5mp-hass/releases/tag/v1.0.0
[1.0.1]: https://github.com/GhostTypes/ff-5mp-hass/releases/tag/v1.0.1
[1.1.0]: https://github.com/GhostTypes/ff-5mp-hass/releases/tag/v1.1.0
[1.1.1]: https://github.com/GhostTypes/ff-5mp-hass/releases/tag/v1.1.1
[1.1.2]: https://github.com/GhostTypes/ff-5mp-hass/releases/tag/v1.1.2
[1.1.3]: https://github.com/GhostTypes/ff-5mp-hass/releases/tag/v1.1.3
