# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository is for developing a Home Assistant custom integration for FlashForge 3D Printers. The integration will be HACS-compatible and use the HTTP API exclusively (avoiding TCP API where possible).

**Key Resources:**
- FlashForge Python API Library: `C:\Users\Cope\Documents\GitHub\ff-5mp-api-py` (referenced as additional working directory)
- Reference Implementation: https://github.com/kruzhkov/hass-flashforge-adventurer-5 (existing TCP-based integration)
- HACS Documentation: https://hacs.xyz/docs/publish/integration/
- Home Assistant Integration Docs: https://developers.home-assistant.io/docs/creating_integration_manifest

## Architecture

### Two-Repository Structure
1. **ff-5mp-api-py** - Standalone Python library for FlashForge printer communication
   - HTTP API client (modern, preferred)
   - TCP/G-code client (legacy, fallback)
   - Discovery service (UDP broadcast)
   - Fully typed with Pydantic models
   - Async-first design

2. **ff-5mp-hass** (this repo) - Home Assistant integration
   - Consumes the ff-5mp-api-py library
   - HTTP-first approach (superior to reference implementation)
   - HACS-compatible structure

### FlashForge API Library Structure

The library in `ff-5mp-api-py` is organized as follows:

**Core Client (`flashforge/client.py`):**
- `FlashForgeClient` - Main unified client class
- Orchestrates HTTP and TCP communication layers
- Control modules accessed via properties:
  - `client.control` - Movement, LED, filtration, camera
  - `client.job_control` - Start/pause/resume/cancel prints
  - `client.info` - Status and machine information
  - `client.files` - File upload/download/management
  - `client.temp_control` - Temperature settings
  - `client.tcp_client` - Low-level TCP access

**Discovery (`flashforge/discovery/`):**
- `FlashForgePrinterDiscovery` - UDP-based network discovery
- Broadcasts on port 48899, listens on port 18007
- Returns `FlashForgePrinter` objects with name, serial, and IP

**Models (`flashforge/models/`):**
- Pydantic models for type safety
- `FFMachineInfo` - Comprehensive machine state and info
- `MachineState` - Current operational state enum
- Response models for all API endpoints

**TCP Client (`flashforge/tcp/`):**
- Legacy G-code communication
- Parsers for various response formats
- Used for features not available in HTTP API

## Home Assistant Integration Requirements

### Required Directory Structure
```
custom_components/flashforge/
├── __init__.py          # Component setup, config flow registration
├── manifest.json        # Integration metadata (REQUIRED)
├── config_flow.py       # UI configuration flow
├── const.py            # Constants (domain, defaults)
├── coordinator.py       # Data update coordinator
├── sensor.py           # Sensor entities (status, temperatures, progress)
├── camera.py           # Camera entity for printer feed
├── binary_sensor.py    # Binary sensors (is_printing, etc.)
├── switch.py           # Switch entities (LED, filtration)
├── button.py           # Button entities (home, pause, resume, cancel)
└── strings.json        # Localization strings
```

### manifest.json Requirements
Must include these keys:
- `domain` - Integration domain (e.g., "flashforge")
- `name` - Display name
- `documentation` - Link to documentation
- `issue_tracker` - Link to GitHub issues
- `codeowners` - GitHub usernames with @ prefix
- `version` - Semantic version
- `requirements` - Python dependencies (include `flashforge-python-api>=1.0.0`)
- `iot_class` - Set to `local_polling` or `local_push`
- `config_flow` - Set to `true` for UI configuration

### HACS Compatibility
1. Repository must have `hacs.json` in root (optional but recommended)
2. Integration must be in `custom_components/<integration_name>/` directory
3. Must register with Home Assistant Brands: https://github.com/home-assistant/brands
4. Recommended to use GitHub releases for versioning

### Configuration Flow Pattern
Users should configure via UI (Settings → Integrations → Add Integration):
1. Discover printers automatically using `FlashForgePrinterDiscovery`
2. Or allow manual IP entry
3. Collect serial number and check code (required for HTTP API)
4. Validate connection during setup
5. Create device with entities

## Development Commands

### FlashForge API Library (ff-5mp-api-py)

**Setup:**
```bash
cd C:\Users\Cope\Documents\GitHub\ff-5mp-api-py
uv sync                    # Install core dependencies
uv sync --all-extras      # Install with dev tools and imaging support
```

**Testing:**
```bash
# Run all tests
uv run python tests/run_tests.py

# Run tests with coverage
uv run python tests/run_tests.py --coverage

# Run specific test suites
uv run python tests/run_tests.py --discovery
uv run python tests/run_tests.py --parsers

# Run pytest directly for more control
uv run pytest -v tests/
uv run pytest -v tests/test_discovery.py -k "test_name"
```

**Code Quality:**
```bash
# Check code quality (formatting, linting, types)
uv run python tests/run_tests.py --lint

# Auto-format code
uv run python tests/run_tests.py --format

# Individual tools
uv run black flashforge/ tests/ examples/
uv run ruff check flashforge/ tests/ examples/
uv run ruff check --fix flashforge/ tests/ examples/
uv run mypy flashforge/
```

**Environment Info:**
```bash
uv run python tests/run_tests.py --env-info
```

### Home Assistant Integration (ff-5mp-hass)

**Local Development:**
```bash
# Install HA development dependencies
pip install homeassistant

# Validate manifest
hass --script check_config -c config/

# Run Home Assistant with custom component
hass -c config/
```

**HACS Validation:**
```bash
# Use HACS Action locally (requires Docker)
docker run --rm -v $(pwd):/workspace ghcr.io/hacs/action:latest
```

## Key Implementation Patterns

### Using FlashForge Client in Home Assistant

```python
from flashforge import FlashForgeClient, FlashForgePrinterDiscovery

# Discovery
discovery = FlashForgePrinterDiscovery()
printers = await discovery.discover_printers_async(timeout=5.0)

# Client initialization
async with FlashForgeClient(
    ip_address="192.168.1.100",
    serial_number="ABCD1234",
    check_code="12345678"
) as client:
    # Verify connection
    if await client.initialize():
        # Get status
        status = await client.info.get_machine_status()

        # Control printer
        await client.control.home_xyz()
        await client.temp_control.set_bed_temp(60)

        # Job control
        await client.job_control.pause_print_job()
        await client.job_control.resume_print_job()
```

### Data Update Coordinator Pattern

Use Home Assistant's `DataUpdateCoordinator` for polling:
- Poll `client.info.get_machine_status()` every 10-30 seconds
- Handle connection errors gracefully
- Update all entities from coordinator data

### Printer Models Support

Tested models:
- FlashForge Adventurer 5M Series
- FlashForge Adventurer 4

Detection:
- `client.is_ad5x` - True for AD5X models
- `client.is_pro` - True for Pro models
- `client.led_control` - True if LED control available
- `client.filtration_control` - True if filtration available

### Authentication Requirements

The HTTP API requires LAN mode setup:
1. Enable LAN mode on printer
2. Obtain check code from printer display
3. Both serial number and check code required for API access
4. See: https://www.youtube.com/watch?v=krdEGccZuKo

## Testing Strategy

### For API Library
- Unit tests in `tests/` directory
- Mock printer responses for deterministic testing
- Integration tests marked with `@pytest.mark.integration`
- Network tests marked with `@pytest.mark.network`

### For Home Assistant Integration
- Use Home Assistant's test fixtures
- Mock `FlashForgeClient` in tests
- Test config flow with discovery and manual entry
- Test entity state updates and error handling

## Important Technical Details

### HTTP vs TCP API
- **Prefer HTTP API** - Modern, more reliable, better error handling
- HTTP uses port 8898
- TCP used only for features unavailable in HTTP (thumbnails, some status data)
- TCP uses port 8899

### Discovery Protocol
- UDP broadcast on port 48899
- Listen for responses on port 18007
- Broadcast to all network interfaces
- 5-second timeout recommended

### Entity Suggestions
**Sensors:**
- Printer state (idle, printing, paused, error)
- Current temperature (extruder, bed)
- Target temperature (extruder, bed)
- Print progress (percentage)
- Current filename
- Estimated time remaining

**Binary Sensors:**
- Is printing
- Is online
- Has error

**Switches:**
- LED control (if supported)
- Filtration (if supported)

**Buttons:**
- Home all axes
- Pause print
- Resume print
- Cancel print

**Camera:**
- Live camera feed (if supported by model)

## Common Pitfalls

1. **Content-Type Header Issue**: FlashForge printers sometimes return `appliation/json` instead of `application/json`. The library handles this, but be aware.

2. **Printer Availability**: Not all features available on all models. Check `client.led_control` and `client.filtration_control` before exposing entities.

3. **Model-Specific Features**: Use `client.is_ad5x` and `client.is_pro` to enable model-specific functionality.

4. **Static IP Recommended**: Advise users to assign static IP to printer in router settings for reliability.

5. **Session Management**: Always use async context manager (`async with`) or call `client.dispose()` to clean up resources.

## Related Documentation Links

**HACS Publisher Documentation:**
- Integration requirements: https://hacs.xyz/docs/publish/integration/
- General publishing guide: https://hacs.xyz/docs/publish/start/
- Include in default repo: https://hacs.xyz/docs/publish/include/
- GitHub Action validation: https://hacs.xyz/docs/publish/action/

**Home Assistant Developer Docs:**
- Creating integrations: https://developers.home-assistant.io/docs/creating_integration_manifest
- Config flow: https://developers.home-assistant.io/docs/config_entries_config_flow_handler
- Data coordinator: https://developers.home-assistant.io/docs/integration_fetching_data
- Entity platform docs: https://developers.home-assistant.io/docs/core/entity/

**Reference Implementations:**
- HACS Blueprint: https://github.com/custom-components/blueprint
- Cookiecutter template: https://github.com/oncleben31/cookiecutter-homeassistant-custom-component
- Existing FlashForge integration: https://github.com/kruzhkov/hass-flashforge-adventurer-5
