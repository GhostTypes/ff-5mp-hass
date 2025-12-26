# Testing and Validation

Comprehensive guide to testing Home Assistant custom integrations and validating code quality.

## Testing Overview

**Main Documentation**
- Path: `assets/docs/development_testing.md`
- Test file structure: `assets/docs/creating_integration_tests_file_structure.md`

## Test Structure

Tests should be in `tests/` directory mirroring the integration structure:

```
tests/
├── __init__.py
├── conftest.py           # Shared fixtures
├── test_config_flow.py   # Config flow tests
├── test_init.py          # Setup/unload tests
└── test_sensor.py        # Platform tests
```

## Validation Tools

### hassfest
Validates integration structure, manifest, and requirements:

```bash
python3 -m script.hassfest --integration my_integration
```

**Checks:**
- manifest.json schema
- requirements format
- codeowners format
- documentation links
- File structure

**Validation Documentation**
- Path: `assets/docs/development_validation.md`

### Code Review
Before submission, ensure your integration passes:
- Path: `assets/docs/creating_component_code_review.md`
- Path: `assets/docs/creating_platform_code_review.md`

## pytest Configuration

### Basic conftest.py

```python
"""Fixtures for integration tests."""
import pytest
from homeassistant.core import HomeAssistant

pytest_plugins = "pytest_homeassistant_custom_component"

@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Enable custom integrations."""
    yield
```

### Common Fixtures

```python
@pytest.fixture
async def mock_api():
    """Mock the API client."""
    with patch("custom_components.my_integration.api.MyAPI") as mock:
        mock.return_value.async_get_data.return_value = {"temp": 20}
        yield mock

@pytest.fixture
async def mock_config_entry(hass: HomeAssistant) -> MockConfigEntry:
    """Create a mock config entry."""
    entry = MockConfigEntry(
        domain=DOMAIN,
        data={"host": "192.168.1.1", "password": "test"},
        unique_id="test_unique_id",
    )
    entry.add_to_hass(hass)
    return entry
```

## Config Flow Testing

### Test User Step

```python
async def test_user_form(hass: HomeAssistant, mock_api) -> None:
    """Test user config flow."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == FlowResultType.FORM
    assert result["step_id"] == "user"

    # Test successful submission
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {"host": "192.168.1.1", "password": "password"},
    )
    assert result["type"] == FlowResultType.CREATE_ENTRY
    assert result["title"] == "192.168.1.1"
    assert result["data"] == {
        "host": "192.168.1.1",
        "password": "password",
    }
```

### Test Validation Errors

```python
async def test_user_form_cannot_connect(hass: HomeAssistant, mock_api) -> None:
    """Test connection error in user flow."""
    mock_api.return_value.async_get_data.side_effect = ConnectionError
    
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {"host": "192.168.1.1", "password": "password"},
    )
    
    assert result["type"] == FlowResultType.FORM
    assert result["errors"] == {"base": "cannot_connect"}
```

### Test Duplicate Prevention

```python
async def test_user_form_already_configured(
    hass: HomeAssistant, mock_config_entry
) -> None:
    """Test duplicate detection."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {"host": "192.168.1.1", "password": "password"},
    )
    
    assert result["type"] == FlowResultType.ABORT
    assert result["reason"] == "already_configured"
```

## Integration Setup Testing

### Test Setup Entry

```python
async def test_setup_entry(hass: HomeAssistant, mock_config_entry, mock_api) -> None:
    """Test setup of config entry."""
    assert await async_setup_entry(hass, mock_config_entry)
    await hass.async_block_till_done()
    
    # Verify platforms were loaded
    assert hass.states.get("sensor.test_temperature") is not None

async def test_setup_entry_not_ready(
    hass: HomeAssistant, mock_config_entry, mock_api
) -> None:
    """Test setup when device not ready."""
    mock_api.return_value.async_get_data.side_effect = ConnectionError
    
    with pytest.raises(ConfigEntryNotReady):
        await async_setup_entry(hass, mock_config_entry)
```

### Test Unload Entry

```python
async def test_unload_entry(
    hass: HomeAssistant, mock_config_entry, mock_api
) -> None:
    """Test unload of config entry."""
    assert await async_setup_entry(hass, mock_config_entry)
    await hass.async_block_till_done()
    
    assert await async_unload_entry(hass, mock_config_entry)
    await hass.async_block_till_done()
    
    assert DOMAIN not in hass.data
```

## Entity Testing

### Test Entity State

```python
async def test_sensor_state(
    hass: HomeAssistant, mock_config_entry, mock_api
) -> None:
    """Test sensor reports correct state."""
    await async_setup_entry(hass, mock_config_entry)
    await hass.async_block_till_done()
    
    state = hass.states.get("sensor.test_temperature")
    assert state.state == "20"
    assert state.attributes["unit_of_measurement"] == "°C"
```

### Test Entity Updates

```python
async def test_sensor_update(
    hass: HomeAssistant, mock_config_entry, mock_api
) -> None:
    """Test sensor updates."""
    await async_setup_entry(hass, mock_config_entry)
    await hass.async_block_till_done()
    
    # Change mock data
    mock_api.return_value.async_get_data.return_value = {"temp": 25}
    
    # Trigger update
    await async_fire_time_changed(hass, dt_util.utcnow() + timedelta(minutes=5))
    await hass.async_block_till_done()
    
    state = hass.states.get("sensor.test_temperature")
    assert state.state == "25"
```

### Test Entity Availability

```python
async def test_sensor_unavailable(
    hass: HomeAssistant, mock_config_entry, mock_api
) -> None:
    """Test sensor becomes unavailable on error."""
    await async_setup_entry(hass, mock_config_entry)
    await hass.async_block_till_done()
    
    # Simulate connection error
    mock_api.return_value.async_get_data.side_effect = ConnectionError
    
    await async_fire_time_changed(hass, dt_util.utcnow() + timedelta(minutes=5))
    await hass.async_block_till_done()
    
    state = hass.states.get("sensor.test_temperature")
    assert state.state == STATE_UNAVAILABLE
```

## Mocking Best Practices

### Mock External Libraries

```python
from unittest.mock import patch, MagicMock

@pytest.fixture
async def mock_device():
    """Mock the device library."""
    with patch("custom_components.my_integration.MyDevice") as mock:
        device = mock.return_value
        device.connect.return_value = True
        device.get_temperature.return_value = 20.0
        device.is_connected = True
        yield device
```

### Mock Time

```python
from homeassistant.util import dt as dt_util
from datetime import timedelta

async def test_with_time():
    """Test with mocked time."""
    now = dt_util.utcnow()
    
    # Fast-forward time
    async_fire_time_changed(hass, now + timedelta(hours=1))
    await hass.async_block_till_done()
```

### Mock aiohttp Responses

```python
from aiohttp import ClientSession
from aioresponses import aioresponses

@pytest.fixture
def mock_aiohttp():
    """Mock aiohttp responses."""
    with aioresponses() as m:
        m.get(
            "https://api.example.com/data",
            payload={"temp": 20},
            status=200,
        )
        yield m
```

## Test Coverage

### Run with Coverage

```bash
pytest --cov=custom_components.my_integration --cov-report=term-missing
```

### Minimum Coverage Requirements

- Config flow: 100% (all paths tested)
- Setup/unload: 95%+
- Entities: 90%+
- Overall: 90%+

## Type Checking

**Type Hints Required**
- Path: `assets/docs/development_typing.md`
- Use mypy for type checking
- All functions should have type hints

```bash
mypy custom_components/my_integration
```

## Code Style

### ruff (linter and formatter)

```bash
ruff check custom_components/my_integration
ruff format custom_components/my_integration
```

### pylint

```bash
pylint custom_components/my_integration
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      
      - name: Install dependencies
        run: |
          pip install -r requirements_test.txt
      
      - name: Run hassfest
        run: python3 -m script.hassfest --integration my_integration
      
      - name: Run tests
        run: pytest --cov --cov-report=xml
      
      - name: Type check
        run: mypy custom_components/my_integration
      
      - name: Lint
        run: ruff check custom_components/my_integration
```

## HACS Validation

For HACS publishing, also run:

```bash
# HACS validation action
# See: /home/claude/home-assistant-dev/references/hacs-publishing.md
```

## Common Testing Patterns

### Test Discovery

```python
async def test_zeroconf_discovery(hass: HomeAssistant) -> None:
    """Test zeroconf discovery."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN,
        context={"source": config_entries.SOURCE_ZEROCONF},
        data=zeroconf.ZeroconfServiceInfo(
            ip_address=ip_address("192.168.1.5"),
            ip_addresses=[ip_address("192.168.1.5")],
            hostname="mydevice.local.",
            name="My Device._http._tcp.local.",
            port=80,
            type="_http._tcp.local.",
            properties={"model": "ABC123"},
        ),
    )
    
    assert result["type"] == FlowResultType.FORM
```

### Test Reauth Flow

```python
async def test_reauth_flow(
    hass: HomeAssistant, mock_config_entry
) -> None:
    """Test reauth flow."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN,
        context={
            "source": config_entries.SOURCE_REAUTH,
            "entry_id": mock_config_entry.entry_id,
            "unique_id": mock_config_entry.unique_id,
        },
        data=mock_config_entry.data,
    )
    
    assert result["type"] == FlowResultType.FORM
    assert result["step_id"] == "reauth_confirm"
```

### Test Options Flow

```python
async def test_options_flow(
    hass: HomeAssistant, mock_config_entry
) -> None:
    """Test options flow."""
    result = await hass.config_entries.options.async_init(
        mock_config_entry.entry_id
    )
    
    assert result["type"] == FlowResultType.FORM
    assert result["step_id"] == "init"
    
    result = await hass.config_entries.options.async_configure(
        result["flow_id"],
        user_input={"scan_interval": 30},
    )
    
    assert result["type"] == FlowResultType.CREATE_ENTRY
    assert mock_config_entry.options == {"scan_interval": 30}
```

## Additional Resources

**Development Guidelines**
- Path: `assets/docs/development_guidelines.md`

**Development Tips**
- Path: `assets/docs/development_tips.md`

**Review Process**
- Path: `assets/docs/review-process.md`
