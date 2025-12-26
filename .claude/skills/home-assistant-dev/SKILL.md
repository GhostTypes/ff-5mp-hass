---
name: home-assistant-dev
description: Comprehensive Home Assistant custom integration development skill. Use when developing Home Assistant integrations, custom components, or plugins. Covers entity platforms, config flows, data management, quality requirements, testing, and HACS publishing. Includes complete reference documentation for all 47+ entity types, integration quality scale requirements, and step-by-step publishing guides.
---

# Home Assistant Development

Complete skill for building, testing, and publishing Home Assistant custom integrations.

## When to Use This Skill

Use this skill when:
- Creating a new Home Assistant custom integration or component  
- Developing entity platforms (sensors, switches, lights, etc.)
- Implementing config flows for UI-based setup
- Managing data coordinators and API polling
- Publishing to HACS (Home Assistant Community Store)
- Troubleshooting integration development issues
- Ensuring integration quality and best practices
- Understanding Home Assistant architecture and APIs

## Quick Start Workflow

### 1. Planning Your Integration

**Determine Integration Type:**
- **Device**: Physical hardware (smart bulbs, sensors, thermostats)
- **Service**: Cloud API or web service (weather, notifications, calendar)
- **Hub**: Local or cloud hub managing multiple devices (Zigbee, Z-Wave hubs)
- **Helper**: Utility integration (rare for custom integrations)

**Choose IoT Class:**
- `cloud_polling` - Poll cloud API regularly
- `cloud_push` - Cloud pushes updates to HA
- `local_polling` - Poll local device  
- `local_push` - Device pushes updates (webhooks, MQTT, etc.)
- `calculated` - Derives data from other sources

### 2. Set Up Development Environment

Options:
1. **VS Code DevContainer** (recommended for core contribution)
   - See: `assets/docs/setup_devcontainer_environment.md`
2. **Custom Integration Development**
   - Install Home Assistant (Core, Container, or Supervisor)
   - Create `custom_components/<your_domain>/` in config directory
   - Enable debug logging in configuration.yaml

### 3. Create Integration Structure

Run scaffold command (if contributing to core) or manually create:

```
custom_components/your_domain/
├── __init__.py              # Setup and coordinator
├── manifest.json            # Integration metadata
├── config_flow.py           # UI configuration flow
├── const.py                 # Constants (DOMAIN, etc.)
├── coordinator.py           # DataUpdateCoordinator (optional)
├── sensor.py                # Entity platforms
├── switch.py
├── strings.json             # Translations
└── translations/
    └── en.json
```

**Key Files:**
- `manifest.json` - Required metadata (domain, name, version, requirements, etc.)
  - Reference: [Integration Basics](#integration-basics)
- `__init__.py` - Entry point with `async_setup_entry()` and `async_unload_entry()`
- `config_flow.py` - UI-based configuration (Bronze quality requirement)
- Platform files - Entity implementations (sensor.py, switch.py, etc.)

### 4. Choose Entity Platforms

Identify what entities your integration provides. Reference the complete list:
- See: [Entity Platforms Reference](#entity-platforms)

Common combinations:
- **Smart Device**: sensor + switch + binary_sensor
- **Climate Control**: climate + sensor + switch
- **Media Device**: media_player + remote
- **Security**: binary_sensor + camera + alarm_control_panel
- **Voice Assistant**: stt + tts + conversation

### 5. Implement Config Flow

**Bronze Quality Requirement** - All integrations need UI configuration.

Steps:
1. Create `config_flow.py` extending `ConfigFlow`
2. Implement `async_step_user()` for manual setup
3. Set unique_id with `self.async_set_unique_id()`
4. Check for duplicates with `self._abort_if_unique_id_configured()`
5. Create entry with `self.async_create_entry()`
6. Add `config_flow: true` to manifest.json

**Reference:** [Config Flows](#config-flows-and-data-management)

### 6. Implement Setup Entry

In `__init__.py`:

```python
async def async_setup_entry(hass, entry):
    """Set up from config entry."""
    # 1. Create API client or coordinator
    coordinator = MyCoordinator(hass, entry)
    await coordinator.async_config_entry_first_refresh()
    
    # 2. Store in hass.data
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator
    
    # 3. Forward to platforms
    await hass.config_entries.async_forward_entry_setups(
        entry, ["sensor", "switch"]
    )
    
    # 4. Register update listener
    entry.async_on_unload(entry.add_update_listener(update_listener))
    
    return True

async def async_unload_entry(hass, entry):
    """Unload config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(
        entry, ["sensor", "switch"]
    )
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok
```

### 7. Implement Entities

Create platform files (e.g., `sensor.py`):

```python
async def async_setup_entry(hass, entry, async_add_entities):
    """Set up sensors."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    
    async_add_entities([
        MySensor(coordinator, "temperature"),
        MySensor(coordinator, "humidity"),
    ])

class MySensor(CoordinatorEntity, SensorEntity):
    """Sensor entity."""
    
    def __init__(self, coordinator, sensor_type):
        """Initialize sensor."""
        super().__init__(coordinator)
        self._attr_unique_id = f"{coordinator.device_id}_{sensor_type}"
        self._attr_has_entity_name = True
        self._attr_name = sensor_type.title()
        self._sensor_type = sensor_type
    
    @property
    def native_value(self):
        """Return sensor value."""
        return self.coordinator.data[self._sensor_type]
    
    @property
    def device_info(self):
        """Return device info."""
        return {
            "identifiers": {(DOMAIN, self.coordinator.device_id)},
            "name": "My Device",
            "manufacturer": "My Company",
            "model": "Model X",
        }
```

**Reference specific entity types:** [Entity Platforms](#entity-platforms)

### 8. Test Your Integration

**Required for Bronze Quality:**

1. **Write config flow tests** - Test all flow steps, error cases, duplicates
2. **Test setup/unload** - Verify entry lifecycle
3. **Test entities** - State, attributes, updates, availability
4. **Run validation** - `python3 -m script.hassfest`

**Reference:** [Testing and Validation](#testing-and-validation)

### 9. Ensure Quality

Follow the integration quality scale for reliability:

**Bronze** (Required for HACS):
- ✓ Config flow
- ✓ Config flow tests
- ✓ Unique config entry
- ✓ Brand assets

**Silver** (Recommended):
- ✓ Reauthentication flow
- ✓ Proper error handling
- ✓ Entity availability states

**Gold** (Professional):
- ✓ Reconfiguration flow
- ✓ Diagnostics
- ✓ Entity translations
- ✓ Good documentation

**Reference:** [Quality Scale](#integration-quality-scale)

### 10. Publish to HACS

**Prerequisites:**
1. Public GitHub repository
2. Valid manifest.json with `version` field
3. Repository description, topics, and README
4. `hacs.json` file (optional but recommended)
5. GitHub releases

**Publishing Steps:**
1. Add `hacs.json` to repository root
2. Validate with `hacs/action` GitHub Action
3. Create first GitHub release
4. Test as custom repository
5. Submit PR to `hacs/default` (optional, for default store)

**Reference:** [HACS Publishing](#hacs-publishing-guide)

## Reference Documentation

### Integration Basics

**File:** `references/integration-basics.md`

Core integration concepts:
- Integration types and IoT classes
- Manifest.json requirements
- File structure and organization
- Setup methods (async_setup_entry)
- Service definitions
- Device and entity registry
- State and event system
- AsyncIO best practices

**When to consult:**
- Starting a new integration
- Understanding integration architecture
- Setting up async coordinators
- Working with registries
- Implementing services

### Entity Platforms

**File:** `references/entity-platforms.md`

Complete reference for all 47+ entity platform types:
- Sensor, Binary Sensor, Switch, Light, Climate
- Media Player, Camera, Cover, Lock, Fan, Vacuum
- Weather, Humidifier, Water Heater
- Number, Select, Text, Button, Date/Time
- Calendar, Todo, Scene, Event
- Voice entities (STT, TTS, Conversation, Wake Word)
- And 20+ more specialized types

Each platform includes:
- Properties and device classes
- State classes and units of measurement
- Common patterns and examples
- Links to complete documentation

**When to consult:**
- Choosing entity types for your integration
- Understanding entity properties
- Implementing specific platforms
- Finding device classes and units
- Learning platform-specific features

### Config Flows and Data Management

**File:** `references/config-flows.md`

UI-based configuration and data handling:
- Config flow implementation
- Options flow for settings
- Data entry flow framework
- Setup and teardown
- DataUpdateCoordinator patterns
- Registry management (entity, device, area)
- Network discovery (mDNS, SSDP, DHCP, etc.)
- Authentication systems

**When to consult:**
- Implementing config flows (Bronze requirement)
- Adding options flows
- Managing data polling and updates
- Handling setup failures
- Working with discovery protocols
- Setting up authentication

### Integration Quality Scale

**File:** `references/quality-scale.md`

Quality tier requirements and best practices:
- Bronze: UI setup, basic tests, brand assets
- Silver: Reauth flow, error handling, availability
- Gold: Reconfigure flow, diagnostics, translations
- Platinum: Repairs, advanced features, comprehensive docs

Complete rule reference with paths to detailed documentation for each requirement.

**When to consult:**
- Planning integration features
- Preparing for HACS submission
- Improving integration reliability
- Understanding best practices
- Meeting quality requirements

### Testing and Validation

**File:** `references/testing-validation.md`

Comprehensive testing guide:
- Test structure and fixtures
- Config flow testing
- Entity testing patterns
- Mocking best practices
- Test coverage requirements
- Type checking with mypy
- Code style (ruff, pylint)
- hassfest validation
- CI/CD setup

**When to consult:**
- Writing tests for your integration
- Achieving required test coverage
- Mocking external dependencies
- Running validation tools
- Setting up CI/CD
- Preparing for code review

### HACS Publishing Guide

**File:** `references/hacs-publishing.md`

Complete HACS publishing process:
- General requirements
- hacs.json configuration
- Joining the default store
- GitHub Action validation
- Repository type requirements (integration, plugin, theme, etc.)
- Review pipeline
- Operations and lifecycle

**When to consult:**
- Publishing to HACS
- Understanding HACS requirements
- Configuring hacs.json
- Validating before submission
- Submitting to default store
- Maintaining published integrations

## Complete Documentation Archive

All Home Assistant developer documentation is available in:
`assets/docs/`

This includes:
- 290+ documentation files
- All 47 entity platform guides
- 53 quality scale rules
- API documentation (WebSocket, REST)
- Frontend development guides
- Add-on development
- Voice integration
- Testing frameworks
- And much more

**Organization:**
- `core/entity/` - All entity platforms
- `core/integration-quality-scale/rules/` - All quality rules
- `api/` - WebSocket and REST APIs
- `frontend/` - UI development
- Root level - Core development guides

Use the file paths provided in reference docs to access specific topics.

## Common Patterns and Solutions

### Data Coordinator Pattern

Use `DataUpdateCoordinator` for polling:

```python
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

class MyCoordinator(DataUpdateCoordinator):
    """Coordinator for managing data updates."""
    
    def __init__(self, hass, entry):
        """Initialize coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=30),
        )
        self.api = MyAPI(entry.data["host"])
    
    async def _async_update_data(self):
        """Fetch data from API."""
        try:
            return await self.api.async_get_data()
        except ConnectionError as err:
            raise UpdateFailed(f"Error communicating with API: {err}")
```

### Entity Naming Pattern (Gold Quality)

```python
class MySensor(SensorEntity):
    _attr_has_entity_name = True
    _attr_name = "Temperature"  # Just the sensor function, not device name
    
    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._device_id)},
            "name": "My Smart Device",  # Device name here
            "manufacturer": "ACME Corp",
        }
```

Result: Entity named "My Smart Device Temperature"

### Reauth Flow Pattern (Silver Quality)

```python
# In your update method, detect auth failure
if response.status == 401:
    entry.async_start_reauth(hass)
    return

# In config_flow.py
async def async_step_reauth(self, user_input=None):
    """Handle reauth flow."""
    entry = self.hass.config_entries.async_get_entry(self.context["entry_id"])
    
    if user_input is not None:
        # Validate new credentials
        try:
            await self._test_credentials(user_input["password"])
        except InvalidAuth:
            return self.async_show_form(
                step_id="reauth_confirm",
                errors={"base": "invalid_auth"},
            )
        
        # Update entry with new credentials
        self.hass.config_entries.async_update_entry(
            entry,
            data={**entry.data, **user_input},
        )
        await self.hass.config_entries.async_reload(entry.entry_id)
        return self.async_abort(reason="reauth_successful")
    
    return self.async_show_form(
        step_id="reauth_confirm",
        data_schema=vol.Schema({vol.Required("password"): str}),
    )
```

### Diagnostics Pattern (Gold Quality)

```python
# In your integration's __init__.py
async def async_get_config_entry_diagnostics(hass, entry):
    """Return diagnostics for a config entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    
    return {
        "entry_data": dict(entry.data),
        "device_info": {
            "model": coordinator.device.model,
            "firmware": coordinator.device.firmware_version,
        },
        "api_data": coordinator.data,
        "last_update": coordinator.last_update_success,
    }
```

## Tips and Best Practices

1. **Always use config flows** - YAML configuration is deprecated for new integrations
2. **Set unique_id early** - First thing in config flow to prevent duplicates
3. **Use DataUpdateCoordinator** - Don't poll in individual entities
4. **Implement proper error handling** - Raise ConfigEntryNotReady for temporary issues
5. **Make entities unavailable** - Set `available = False` when device offline (Silver quality)
6. **Add entity translations** - Use strings.json for professional quality (Gold)
7. **Write comprehensive tests** - Config flow tests are mandatory for Bronze
8. **Follow entity naming** - Use `has_entity_name = True` pattern (Gold quality)
9. **Provide device_info** - Link entities to devices in registry
10. **Document thoroughly** - Good docs are required for all quality tiers

## Development Checklist

Before publishing:

- [ ] Config flow implemented and tested
- [ ] All entity platforms working
- [ ] Proper error handling (ConfigEntryNotReady, ConfigEntryAuthFailed)
- [ ] Entities report unavailable state when offline
- [ ] Unique IDs set for all entities
- [ ] Device info provided
- [ ] manifest.json complete with version
- [ ] Tests written with good coverage
- [ ] Documentation complete
- [ ] hassfest validation passes
- [ ] hacs.json created
- [ ] GitHub repository with releases
- [ ] HACS validation passes

## Support and Resources

**Official Documentation:** https://developers.home-assistant.io/
**HACS Documentation:** https://hacs.xyz/
**Discord:** Join #developers channel
**Forum:** https://community.home-assistant.io/

## Skill Maintenance

This skill contains documentation current as of December 2024. Home Assistant releases monthly updates, so check for:
- New entity platforms or features
- Updated quality scale requirements
- Changes to config flow patterns
- New HACS requirements

The complete documentation archive in `assets/docs/` can be consulted for any topic.
