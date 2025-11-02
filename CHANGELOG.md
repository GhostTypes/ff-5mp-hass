# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
