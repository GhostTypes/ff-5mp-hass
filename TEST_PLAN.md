# FlashForge Integration - Test Coverage Plan

Comprehensive testing strategy with **two-tier approach**: cross-platform unit tests and WSL/Linux integration tests.

## Current State

✅ **Discovery Tests** (18 tests, ~0.6s runtime)
- `tests/unit/test_discovery.py` - 17 unit tests for printer discovery logic
- `tests/live/test_live_discovery.py` - 1 live test (opt-in, hardware required)

✅ **Sensor Value Function Tests** (56 tests, ~0.4s runtime)
- `tests/unit/test_sensor_value_functions.py` - Tests all 19 sensor value extraction lambdas
- Coverage: Sensor value_fn logic, edge cases, null handling, rounding behavior
- No Home Assistant dependencies - pure function testing

✅ **Binary Sensor Value Function Tests** (19 tests, ~0.2s runtime)
- `tests/unit/test_binary_sensor_value_functions.py` - Tests all 4 binary sensor state logic functions
- Coverage: MachineState-based boolean logic for printing/online/error/paused sensors
- No Home Assistant dependencies - pure function testing

✅ **Utility Function Tests** (8 tests, ~0.1s runtime)
- `tests/unit/test_util.py` - Tests async_close_flashforge_client utility
- Coverage: HTTP session cleanup logic, safe attribute access, edge cases

**Total Unit Tests: 101 tests** ✅ All passing on Windows/WSL/Linux/CI

## Two-Tier Testing Strategy

### Tier 1: Cross-Platform Unit Tests (CURRENT - No HA Dependencies)

**What we test:**
- Business logic (sensor value extraction, binary sensor state logic)
- Utility functions (HTTP cleanup, helpers)
- Data transformations and edge cases
- Configuration validation

**Why this approach:**
- ✅ Runs on Windows (no Unix-only fcntl requirement)
- ✅ Fast (no heavy Home Assistant installation)
- ✅ Enables rapid iteration during development
- ✅ Fast CI builds (no waiting for HA package installation)
- ✅ Tests core business logic in isolation

**How it works:**
- `tests/ha_mocks.py` provides centralized Home Assistant module mocks
- Stub classes for entity descriptions, base classes, enums
- Import mocks BEFORE importing integration code
- Only tests pure Python logic - no HA runtime required

### Tier 2: Integration Tests (FUTURE - Requires HA in WSL/Linux)

**What we'll test:**
- Config flow (user step, discovery, options, reauth)
- Coordinator lifecycle (setup, updates, error handling)
- Integration setup/teardown
- Entity creation and state updates
- Service calls and device registry
- Full Home Assistant runtime behavior

**Requirements:**
- WSL2 or Linux environment
- Home Assistant Core 2025.12.4+
- pytest-homeassistant-custom-component
- Runs in `homeassistant/` dev environment

**Deferred until integration tests are needed**

## Test Infrastructure

### Cross-Platform Unit Test Setup

**Dependencies** (`requirements-test.txt`):
```txt
# Core testing framework
pytest>=7.4.0
pytest-asyncio>=0.21.0
pytest-cov>=4.1.0

# Snapshot testing
syrupy>=4.0.0

# API library (editable install for development)
flashforge-python-api>=1.0.2

# Network interface detection (for discovery tests)
netifaces>=0.11.0
```

**Key Files:**
- `tests/ha_mocks.py` - Centralized Home Assistant module mocking
- `tests/conftest.py` - Shared test fixtures
- `pytest.ini` - Pytest configuration

**Running Tests:**
```bash
# Run all unit tests
pytest tests/unit/ -v

# Run with coverage
pytest tests/unit/ --cov=custom_components.flashforge --cov-report=term-missing

# Run specific test file
pytest tests/unit/test_sensor_value_functions.py -v
```

## Completed Tests (Tier 1 - Cross-Platform Unit Tests)

### ✅ Sensor Value Functions (56 tests)

**File:** `tests/unit/test_sensor_value_functions.py`

Tests all 19 sensor value extraction lambdas that transform `FFMachineInfo` data into sensor values.

**Coverage:**
- Machine status extraction with fallback handling
- Temperature rounding (nozzle/bed current/target)
- Progress percentage handling
- File name extraction with "None" fallback
- Layer counting (current/total)
- Time value handling (elapsed/remaining/lifetime)
- Filament metrics (length/weight/cumulative)
- Print settings (speed, z-offset, nozzle size, filament type)
- Edge cases: None, empty strings, zero values, negative values
- Configuration validation: sensor count, unique keys, required fields, icon format

**Example Tests:**
- `test_nozzle_temperature_rounded` - Verifies 2-decimal rounding
- `test_nozzle_temperature_no_extruder` - Verifies fallback to 0 when extruder data missing
- `test_print_progress_zero` - Verifies 0% is handled correctly (not treated as falsy)
- `test_z_offset_negative` - Verifies negative offsets are supported

### ✅ Binary Sensor Value Functions (19 tests)

**File:** `tests/unit/test_binary_sensor_value_functions.py`

Tests all 4 binary sensor state logic functions that determine ON/OFF states.

**Coverage:**
- `is_printing`: True when MachineState.PRINTING, False otherwise
- `is_online`: Always True (if we have data, printer is online)
- `has_error`: True when MachineState.ERROR, False otherwise
- `is_paused`: True when MachineState.PAUSED, False otherwise
- State transitions across all MachineState values
- Configuration validation: sensor count, unique keys, device classes, boolean returns

**Example Tests:**
- `test_is_printing_true_when_printing` - Verifies printing detection
- `test_is_online_true_regardless_of_state` - Verifies online logic for all states
- `test_has_error_false_when_paused` - Verifies error state exclusivity
- `test_value_functions_return_bool` - Verifies all functions return boolean

### ✅ Utility Functions (8 tests)

**File:** `tests/unit/test_util.py`

Tests the `async_close_flashforge_client` utility function.

**Coverage:**
- Closes HTTP session when present and not closed
- Skips already-closed sessions
- Handles missing `_http_session` attribute gracefully
- Handles None values safely
- Uses getattr for safe attribute access
- Preserves other client attributes
- Does not touch TCP resources (HTTP-only cleanup)

**Example Tests:**
- `test_closes_http_session_when_present` - Verifies session.close() is called
- `test_does_not_close_already_closed_session` - Verifies idempotency
- `test_handles_missing_http_session` - Verifies no errors on missing attribute
- `test_does_not_touch_tcp_resources` - Verifies TCP socket is untouched

### ✅ Discovery Tests (18 tests)

**File:** `tests/unit/test_discovery.py`

Tests printer discovery protocol and network communication (pre-existing).

**Coverage:** FlashForgePrinter class, FlashForgePrinterDiscovery class, UDP broadcast, response parsing

## Future Tests (Tier 2 - Integration Tests in WSL/Linux)

These tests require Home Assistant runtime and will be implemented in the WSL development environment.

### Priority 1: Config Flow (CRITICAL - Bronze Quality Requirement)

**File**: `tests/unit/test_config_flow.py`

Config flows are **mandatory** for Bronze quality and must have **100% test coverage**.

#### Test Cases Needed:

**User Step (Manual Entry)**:
- ✅ Test form display on init
- ✅ Test successful manual entry with valid credentials
- ✅ Test invalid IP address format → validation error
- ✅ Test connection failure → "cannot_connect" error
- ✅ Test authentication failure → "invalid_auth" error
- ✅ Test duplicate detection → "already_configured" abort
- ✅ Test unique_id setting and duplicate abort

**Discovery Step (Automatic)**:
- ✅ Test no printers found → fallback to manual
- ✅ Test single printer found → auto-select
- ✅ Test multiple printers found → selection form
- ✅ Test discovery selection → credential validation
- ✅ Test discovered printer already configured → skip

**Options Flow**:
- ✅ Test options flow init
- ✅ Test scan interval update (5-300s validation)
- ✅ Test invalid scan interval → validation error
- ✅ Test options saved to config entry

**Reauth Flow (Silver Quality)**:
- ✅ Test reauth triggered on auth failure
- ✅ Test reauth form display
- ✅ Test successful credential update
- ✅ Test invalid credentials → error
- ✅ Test config entry updated after reauth

**Example Test Structure**:
```python
async def test_user_form(hass: HomeAssistant, mock_flashforge_api) -> None:
    """Test user config flow - successful setup."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == FlowResultType.FORM
    assert result["step_id"] == "user"

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {
            "host": "192.168.1.100",
            "serial_number": "TEST123",
            "check_code": "12345678"
        },
    )

    assert result["type"] == FlowResultType.CREATE_ENTRY
    assert result["title"] == "Test Printer"
    assert result["data"]["host"] == "192.168.1.100"

    # Verify entry was created
    await hass.async_block_till_done()
    assert len(hass.config_entries.async_entries(DOMAIN)) == 1
```

**Coverage Target**: 100% (required for Bronze quality)

---

### Priority 2: Coordinator

**File**: `tests/unit/test_coordinator.py`

The coordinator is the core data management component.

#### Test Cases Needed:

**Initialization**:
- ✅ Test coordinator creation with config entry
- ✅ Test update interval from options
- ✅ Test client initialization

**Data Updates**:
- ✅ Test successful data fetch
- ✅ Test data parsing from API response
- ✅ Test coordinator listeners notified on update
- ✅ Test update interval timing

**Error Handling**:
- ✅ Test ConnectionError → UpdateFailed
- ✅ Test authentication error → triggers reauth
- ✅ Test transient errors → retry logic
- ✅ Test coordinator marks entities unavailable on persistent error

**Lifecycle**:
- ✅ Test first refresh (async_config_entry_first_refresh)
- ✅ Test ConfigEntryNotReady on initial failure
- ✅ Test proper cleanup on unload

**Example Test Structure**:
```python
async def test_coordinator_update_success(
    hass: HomeAssistant,
    mock_config_entry,
    mock_flashforge_api
) -> None:
    """Test successful coordinator data update."""
    coordinator = FlashForgeDataUpdateCoordinator(hass, mock_config_entry)

    await coordinator.async_config_entry_first_refresh()

    assert coordinator.last_update_success
    assert coordinator.data is not None
    assert coordinator.data.machine_name == "Test Printer"

async def test_coordinator_update_failure(
    hass: HomeAssistant,
    mock_config_entry,
    mock_flashforge_api
) -> None:
    """Test coordinator handles update failure."""
    mock_flashforge_api.info.get.side_effect = ConnectionError("Network error")

    coordinator = FlashForgeDataUpdateCoordinator(hass, mock_config_entry)

    with pytest.raises(UpdateFailed):
        await coordinator.async_config_entry_first_refresh()
```

**Coverage Target**: 95%+

---

### Priority 3: Integration Setup & Teardown

**File**: `tests/unit/test_init.py`

Tests for `__init__.py` setup/unload logic.

#### Test Cases Needed:

**Setup**:
- ✅ Test async_setup_entry success
- ✅ Test coordinator creation and first refresh
- ✅ Test platforms forwarded (sensor, binary_sensor, switch, button, camera)
- ✅ Test data stored in hass.data
- ✅ Test update listener registered

**Setup Failures**:
- ✅ Test ConfigEntryNotReady on connection failure
- ✅ Test ConfigEntryAuthFailed on auth failure
- ✅ Test setup retry behavior

**Unload**:
- ✅ Test async_unload_entry success
- ✅ Test platforms unloaded
- ✅ Test data removed from hass.data
- ✅ Test coordinator stopped

**Example Test Structure**:
```python
async def test_setup_entry(
    hass: HomeAssistant,
    mock_config_entry,
    mock_flashforge_api
) -> None:
    """Test successful config entry setup."""
    assert await async_setup_entry(hass, mock_config_entry)
    await hass.async_block_till_done()

    # Verify coordinator created
    assert DOMAIN in hass.data
    assert mock_config_entry.entry_id in hass.data[DOMAIN]

    # Verify platforms loaded
    assert hass.states.get("sensor.test_printer_nozzle_temperature") is not None
    assert hass.states.get("binary_sensor.test_printer_printing") is not None

async def test_setup_entry_not_ready(
    hass: HomeAssistant,
    mock_config_entry,
    mock_flashforge_api
) -> None:
    """Test setup raises ConfigEntryNotReady on connection failure."""
    mock_flashforge_api.info.get.side_effect = ConnectionError

    with pytest.raises(ConfigEntryNotReady):
        await async_setup_entry(hass, mock_config_entry)
```

**Coverage Target**: 95%+

---

### Priority 4: Sensors (18 entities)

**File**: `tests/unit/test_sensor.py`

Test all 18 sensor entities.

#### Test Cases Needed:

**Entity Creation**:
- ✅ Test all 18 sensors created from coordinator
- ✅ Test unique IDs generated correctly
- ✅ Test device_info linking
- ✅ Test entity naming (has_entity_name = True)

**State and Attributes**:
- ✅ Test machine_status sensor state
- ✅ Test nozzle_temperature sensor state and unit (°C)
- ✅ Test bed_temperature sensor state and unit (°C)
- ✅ Test progress sensor state and unit (%)
- ✅ Test elapsed_time sensor state and conversion (minutes → hours)
- ✅ Test remaining_time sensor state and conversion
- ✅ Test all other sensors (current_file, layers, filament, etc.)

**Icon Selection**:
- ✅ Test sensor icons match expected values
- ✅ Test device_class assignments where applicable

**Availability**:
- ✅ Test sensors available when printer online
- ✅ Test sensors unavailable when coordinator has error
- ✅ Test sensors handle missing data gracefully

**Updates**:
- ✅ Test sensors update when coordinator refreshes
- ✅ Test sensor state changes reflected immediately

**Example Test Structure**:
```python
async def test_sensor_states(
    hass: HomeAssistant,
    mock_config_entry,
    mock_flashforge_api
) -> None:
    """Test all sensor states are correct."""
    await async_setup_entry(hass, mock_config_entry)
    await hass.async_block_till_done()

    # Nozzle temperature
    state = hass.states.get("sensor.test_printer_nozzle_temperature")
    assert state.state == "25.0"
    assert state.attributes["unit_of_measurement"] == "°C"

    # Progress
    state = hass.states.get("sensor.test_printer_progress")
    assert state.state == "0"
    assert state.attributes["unit_of_measurement"] == "%"

    # Test all 18 sensors...

async def test_sensor_unavailable(
    hass: HomeAssistant,
    mock_config_entry,
    mock_flashforge_api
) -> None:
    """Test sensors become unavailable on error."""
    await async_setup_entry(hass, mock_config_entry)
    await hass.async_block_till_done()

    # Simulate coordinator error
    mock_flashforge_api.info.get.side_effect = ConnectionError

    # Trigger coordinator update
    coordinator = hass.data[DOMAIN][mock_config_entry.entry_id]
    await coordinator.async_refresh()
    await hass.async_block_till_done()

    state = hass.states.get("sensor.test_printer_nozzle_temperature")
    assert state.state == STATE_UNAVAILABLE
```

**Coverage Target**: 90%+

---

### Priority 5: Binary Sensors (4 entities)

**File**: `tests/unit/test_binary_sensor.py`

Test printing, online, error, paused binary sensors.

#### Test Cases Needed:

**State Logic**:
- ✅ Test printing binary sensor ON when MachineState.PRINTING
- ✅ Test printing binary sensor OFF when READY
- ✅ Test online binary sensor based on coordinator availability
- ✅ Test error binary sensor based on error state
- ✅ Test paused binary sensor logic

**Device Classes**:
- ✅ Test correct device_class assignments
- ✅ Test icon selection

**Availability**:
- ✅ Test binary sensors unavailable when offline

**Example Test Structure**:
```python
async def test_binary_sensor_printing(
    hass: HomeAssistant,
    mock_config_entry,
    mock_flashforge_api
) -> None:
    """Test printing binary sensor."""
    await async_setup_entry(hass, mock_config_entry)
    await hass.async_block_till_done()

    state = hass.states.get("binary_sensor.test_printer_printing")
    assert state.state == STATE_OFF  # READY state

    # Change to PRINTING
    mock_flashforge_api.info.get.return_value.machine_status = MachineState.PRINTING
    coordinator = hass.data[DOMAIN][mock_config_entry.entry_id]
    await coordinator.async_refresh()
    await hass.async_block_till_done()

    state = hass.states.get("binary_sensor.test_printer_printing")
    assert state.state == STATE_ON
```

**Coverage Target**: 90%+

---

### Priority 6: Switches (2 entities)

**File**: `tests/unit/test_switch.py`

Test LED and filtration control switches.

#### Test Cases Needed:

**Capability Detection**:
- ✅ Test switch created when capability supported
- ✅ Test switch not created when capability missing
- ✅ Test switch marked unavailable when not supported

**Turn On/Off**:
- ✅ Test LED switch turn_on calls client.control.led(True)
- ✅ Test LED switch turn_off calls client.control.led(False)
- ✅ Test filtration switch turn_on/off
- ✅ Test coordinator refreshes after command

**State Tracking**:
- ✅ Test switch state reflects current state
- ✅ Test switch updates when coordinator refreshes

**Error Handling**:
- ✅ Test switch handles command failure gracefully

**Example Test Structure**:
```python
async def test_switch_led_turn_on(
    hass: HomeAssistant,
    mock_config_entry,
    mock_flashforge_api
) -> None:
    """Test LED switch turn on."""
    await async_setup_entry(hass, mock_config_entry)
    await hass.async_block_till_done()

    await hass.services.async_call(
        "switch",
        "turn_on",
        {"entity_id": "switch.test_printer_led"},
        blocking=True,
    )

    mock_flashforge_api.control.led.assert_called_once_with(True)
    # Verify coordinator refreshed
    state = hass.states.get("switch.test_printer_led")
    assert state.state == STATE_ON
```

**Coverage Target**: 90%+

---

### Priority 7: Buttons (3 entities)

**File**: `tests/unit/test_button.py`

Test pause, resume, cancel buttons.

#### Test Cases Needed:

**Press Actions**:
- ✅ Test pause button calls client.job_control.pause()
- ✅ Test resume button calls client.job_control.resume()
- ✅ Test cancel button calls client.job_control.cancel()
- ✅ Test coordinator refreshes after each action

**Error Handling**:
- ✅ Test button handles command failure
- ✅ Test appropriate error logged

**Availability**:
- ✅ Test buttons available when printer online
- ✅ Test buttons unavailable when offline

**Example Test Structure**:
```python
async def test_button_pause(
    hass: HomeAssistant,
    mock_config_entry,
    mock_flashforge_api
) -> None:
    """Test pause button press."""
    await async_setup_entry(hass, mock_config_entry)
    await hass.async_block_till_done()

    await hass.services.async_call(
        "button",
        "press",
        {"entity_id": "button.test_printer_pause"},
        blocking=True,
    )

    mock_flashforge_api.job_control.pause.assert_called_once()
```

**Coverage Target**: 90%+

---

### Priority 8: Camera

**File**: `tests/unit/test_camera.py`

Test MJPEG camera entity.

#### Test Cases Needed:

**Stream URL**:
- ✅ Test camera stream URL constructed correctly (http://<ip>:8080/?action=stream)
- ✅ Test camera name and unique_id
- ✅ Test device_info linking

**Availability**:
- ✅ Test camera available when printer online
- ✅ Test camera unavailable when offline

**Example Test Structure**:
```python
async def test_camera_stream_url(
    hass: HomeAssistant,
    mock_config_entry,
    mock_flashforge_api
) -> None:
    """Test camera stream URL is correct."""
    await async_setup_entry(hass, mock_config_entry)
    await hass.async_block_till_done()

    state = hass.states.get("camera.test_printer")
    assert state is not None
    # Test stream URL construction
```

**Coverage Target**: 90%+

---

## Integration Tests (Lower Priority)

**File**: `tests/integration/test_full_lifecycle.py`

End-to-end integration tests.

#### Test Cases Needed:

**Full Setup Flow**:
- ✅ Test complete setup from config flow → entities created
- ✅ Test coordinator updates → entity states change
- ✅ Test entity service calls → API called → coordinator refreshed

**Error Recovery**:
- ✅ Test connection lost → entities unavailable → connection restored → entities available
- ✅ Test auth failure → reauth flow triggered → credentials updated → entities available

**Reload**:
- ✅ Test config entry reload
- ✅ Test options flow update → coordinator update interval changes

**Coverage Target**: Not critical, but aim for 80%+

---

## Test Infrastructure Updates Needed

### 1. Update `requirements-test.txt`

Add Home Assistant testing dependencies:
```txt
# Existing
pytest>=7.4.0
pytest-asyncio>=0.21.0
homeassistant>=2025.12.4
flashforge-python-api>=1.0.2
netifaces>=0.11.0

# ADD THESE:
pytest-homeassistant-custom-component>=0.13.0
syrupy>=4.0.0  # Snapshot testing
aioresponses>=0.7.6  # Mock aiohttp responses (if needed)
```

### 2. Update `tests/conftest.py`

Add Home Assistant plugin and common fixtures:
```python
"""Shared test fixtures for FlashForge integration tests."""
import sys
from pathlib import Path
from unittest.mock import AsyncMock, Mock, patch

import pytest
from homeassistant.core import HomeAssistant
from tests.common import MockConfigEntry

# Add the project root to sys.path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Enable Home Assistant pytest plugin
pytest_plugins = "pytest_homeassistant_custom_component"

@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Enable custom integrations for testing."""
    yield

# Keep existing fixtures (mock_flashforge_client, etc.)
# Add new fixtures for config entries, API mocking, etc.
```

### 3. Create Test Data Factories

**File**: `tests/fixtures.py`

```python
"""Test data factories for creating mock objects."""
from flashforge.models import FFMachineInfo, MachineState

def create_mock_machine_info(**overrides):
    """Create a mock FFMachineInfo with defaults."""
    defaults = {
        "machine_name": "Test Printer",
        "machine_type": "Adventurer 5M Pro",
        "machine_status": MachineState.READY,
        "nozzle_temp": 25.0,
        "nozzle_target_temp": 0.0,
        "bed_temp": 22.0,
        "bed_target_temp": 0.0,
        "progress": 0,
        "current_file": "",
        "current_layer": 0,
        "total_layers": 0,
        "print_time_elapsed_minutes": 0,
        "print_time_remaining_minutes": 0,
        "filament_length_mm": 0.0,
        "filament_weight_g": 0.0,
        "print_speed_pct": 100,
        "z_offset_mm": 0.0,
        "move_mode": "READY",
        "nozzle_size_mm": 0.4,
        "filament_type": "PLA"
    }
    return FFMachineInfo(**(defaults | overrides))
```

---

## Testing Best Practices (From HA Docs)

### 1. Don't Interact with Integration Internals

✅ **DO**: Test through public interfaces
```python
# Setup via core interface
await async_setup_entry(hass, mock_config_entry)

# Assert via state machine
state = hass.states.get("sensor.test")
assert state.state == "20"

# Call services via service registry
await hass.services.async_call("switch", "turn_on", {...})
```

❌ **DON'T**: Access integration internals directly
```python
# Don't do this
from custom_components.flashforge.sensor import MySensor
sensor = MySensor(...)
assert sensor.native_value == 20
```

### 2. Use Snapshot Testing for Large Outputs

For device registry, entity registry, diagnostics:
```python
async def test_device_info(
    hass: HomeAssistant,
    device_registry,
    snapshot: SnapshotAssertion
) -> None:
    """Test device registry entry."""
    await async_setup_entry(hass, mock_config_entry)

    device = device_registry.async_get_device(
        identifiers={(DOMAIN, "TEST123")}
    )
    assert device == snapshot
```

### 3. Mock External Dependencies Completely

Always mock the API client, never make real network calls:
```python
@pytest.fixture
async def mock_flashforge_api():
    """Mock FlashForge API client."""
    with patch("custom_components.flashforge.FlashForgeClient") as mock:
        # Setup all methods the integration will call
        client = mock.return_value
        client.info.get.return_value = create_mock_machine_info()
        client.control.led = AsyncMock()
        client.job_control.pause = AsyncMock()
        yield client
```

### 4. Test Error Paths Explicitly

Don't just test happy paths:
```python
async def test_coordinator_handles_connection_error(
    hass, mock_config_entry, mock_flashforge_api
):
    """Test coordinator handles connection errors gracefully."""
    mock_flashforge_api.info.get.side_effect = ConnectionError

    coordinator = FlashForgeDataUpdateCoordinator(hass, mock_config_entry)

    with pytest.raises(ConfigEntryNotReady):
        await coordinator.async_config_entry_first_refresh()
```

---

## Coverage Targets

| Component | Target | Priority | Notes |
|-----------|--------|----------|-------|
| Config Flow | 100% | **CRITICAL** | Bronze quality requirement |
| Coordinator | 95%+ | High | Core data management |
| Init (setup/unload) | 95%+ | High | Lifecycle management |
| Sensors | 90%+ | Medium | Many entities to test |
| Binary Sensors | 90%+ | Medium | State logic testing |
| Switches | 90%+ | Medium | Control functionality |
| Buttons | 90%+ | Medium | Control functionality |
| Camera | 90%+ | Low | Simple entity |
| Integration | 80%+ | Low | End-to-end validation |
| **Overall** | **90%+** | | Aim for high confidence |

---

## Implementation Phases

### Phase 1: Foundation (1-2 sessions)
1. Update `requirements-test.txt` with HA testing dependencies
2. Update `tests/conftest.py` with pytest plugin and HA fixtures
3. Create `tests/fixtures.py` with test data factories
4. Set up basic config flow tests (just user step)

### Phase 2: Config Flow Complete (1 session)
1. Complete all user step tests
2. Add discovery step tests
3. Add options flow tests
4. Add reauth flow tests (Silver quality)
5. Verify 100% config flow coverage

### Phase 3: Core Components (2 sessions)
1. Complete coordinator tests
2. Complete init (setup/unload) tests
3. Verify core infrastructure solid

### Phase 4: Entity Platforms (2-3 sessions)
1. Complete sensor tests (18 entities)
2. Complete binary sensor tests (4 entities)
3. Complete switch tests (2 entities)
4. Complete button tests (3 entities)
5. Complete camera tests (1 entity)

### Phase 5: Integration Tests (1 session)
1. Add end-to-end integration tests
2. Add error recovery tests
3. Add reload tests

### Phase 6: Polish (1 session)
1. Review coverage reports
2. Add missing edge cases
3. Add snapshot tests for diagnostics (Gold quality)
4. Update documentation

---

## Running Tests

### Run All Tests
```bash
pytest
```

### Run Specific Component
```bash
pytest tests/unit/test_config_flow.py -v
```

### Run With Coverage
```bash
pytest tests/unit/test_config_flow.py --cov=custom_components.flashforge.config_flow --cov-report=term-missing
```

### Run All Non-Live Tests With Coverage
```bash
pytest --cov=custom_components.flashforge --cov-report=html --cov-report=term-missing -v
```

### Update Snapshots
```bash
pytest tests/unit/test_init.py --snapshot-update
```

---

## Success Criteria

Before considering test coverage "complete":

- [ ] All config flow paths tested (100% coverage)
- [ ] All coordinator behavior tested (95%+ coverage)
- [ ] All entity platforms tested (90%+ coverage)
- [ ] All error paths tested
- [ ] All entity availability logic tested (Silver quality)
- [ ] Integration lifecycle tested (setup/unload/reload)
- [ ] Overall coverage >90%
- [ ] No flaky tests
- [ ] All tests run in <10 seconds (excluding live tests)
- [ ] CI/CD workflow created and passing

---

## Notes

- **Use Home Assistant fixtures** - Don't reinvent the wheel, use `hass`, `device_registry`, `entity_registry`, etc.
- **Mock completely** - Never make real network calls in unit tests
- **Test through public interfaces** - Use `hass.states.get()`, `hass.services.async_call()`, not internal methods
- **Snapshot test big objects** - Use Syrupy for device registry, entity registry, diagnostics
- **Keep tests fast** - Unit tests should be <10s total, integration tests <30s
- **Live tests opt-in** - Keep hardware tests separate with `-m live` marker

---

## References

- Home Assistant Testing Docs: `C:\Users\Cope\Documents\GitHub\ff-5mp-hass\.claude\skills\home-assistant-dev\references\testing-validation.md`
- Config Flow Docs: `C:\Users\Cope\Documents\GitHub\ff-5mp-hass\.claude\skills\home-assistant-dev\references\config-flows.md`
- Quality Scale: `C:\Users\Cope\Documents\GitHub\ff-5mp-hass\.claude\skills\home-assistant-dev\references\quality-scale.md`
- Integration Basics: `C:\Users\Cope\Documents\GitHub\ff-5mp-hass\.claude\skills\home-assistant-dev\references\integration-basics.md`
