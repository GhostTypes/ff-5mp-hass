# Integration Development Basics

Core concepts and requirements for building Home Assistant custom integrations.

## Getting Started

**Development Environment**
- Path: `assets/docs/development_environment.md`
- DevContainer setup for VS Code
- Path: `assets/docs/setup_devcontainer_environment.md`

**Creating an Integration**
- Path: `assets/docs/creating_component_index.md`
- Manifest requirements
- File structure
- Initial setup methods

## Integration Structure

### Required Files

**manifest.json** - Integration metadata
- Path: `assets/docs/creating_integration_manifest.md`
- Required fields: domain, name, documentation, codeowners, requirements, integration_type, iot_class
- Optional: config_flow, dependencies, after_dependencies, version (for custom integrations)

**__init__.py** - Entry point
- `async_setup()` or `async_setup_entry()` required
- Coordinate platform loading
- Initialize data coordinators

**Platform files** - Entity implementations
- sensor.py, switch.py, etc.
- `async_setup_platform()` or `async_setup_entry()` for each platform

### File Organization
- Path: `assets/docs/creating_integration_file_structure.md`
- Path: `assets/docs/creating_integration_tests_file_structure.md`

```
custom_components/my_integration/
├── __init__.py           # Setup and coordinator
├── manifest.json         # Integration metadata
├── config_flow.py        # UI configuration (optional)
├── const.py              # Constants
├── coordinator.py        # Data update coordinator (optional)
├── sensor.py             # Sensor platform
├── switch.py             # Switch platform
├── services.yaml         # Service definitions (optional)
├── strings.json          # Translations
└── translations/         # Additional language files
    └── en.json
```

## Core Concepts

### Integration Types
- `device` - Physical devices
- `hub` - Cloud service or local hub coordinating multiple devices
- `service` - Web service integration
- `helper` - Utility integration (rare for custom)

### IoT Classes
- `cloud_polling` - Polls cloud API
- `cloud_push` - Cloud pushes updates
- `local_polling` - Polls local device
- `local_push` - Device pushes updates
- `calculated` - Derived/calculated values
- `assumed_state` - State assumed from commands

## Setup Methods

### YAML-based Setup (Legacy)
```python
async def async_setup(hass, config):
    """Set up integration from YAML."""
    # Process YAML config
    # Load platforms
    return True
```

### Config Entry Setup (Recommended)
```python
async def async_setup_entry(hass, entry):
    """Set up from config entry."""
    # Initialize coordinator
    coordinator = MyCoordinator(hass, entry)
    await coordinator.async_config_entry_first_refresh()
    
    # Store coordinator
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator
    
    # Forward to platforms
    await hass.config_entries.async_forward_entry_setups(
        entry, ["sensor", "switch"]
    )
    
    # Register services
    async def handle_custom_service(call):
        """Handle custom service call."""
        # Implementation
    
    hass.services.async_register(DOMAIN, "my_service", handle_custom_service)
    
    # Setup update listener for options
    entry.async_on_unload(entry.add_update_listener(update_listener))
    
    return True

async def async_unload_entry(hass, entry):
    """Unload config entry."""
    # Unload platforms
    unload_ok = await hass.config_entries.async_unload_platforms(
        entry, ["sensor", "switch"]
    )
    
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    
    return unload_ok

async def update_listener(hass, entry):
    """Handle options update."""
    await hass.config_entries.async_reload(entry.entry_id)
```

## Service Definitions

### Creating Services
- Path: `assets/docs/dev_101_services.md`
- Define in services.yaml
- Register in `async_setup()` or `async_setup_entry()`
- Provide translations in strings.json

### Service Response Support
Services can return data to the caller for use in automations and scripts.

## Device and Entity Management

### Device Info
```python
@property
def device_info(self):
    """Return device info."""
    return {
        "identifiers": {(DOMAIN, self._device_id)},
        "name": "My Device",
        "manufacturer": "My Company",
        "model": "Model X",
        "sw_version": "1.0.0",
        "via_device": (DOMAIN, self._hub_id),  # If behind a hub
    }
```

### Entity Registry
- Path: `assets/docs/entity_registry_index.md`
- `unique_id` required for entity registry
- Disabled by default: `entity_registry_enabled_default = False`
- Entity categories: config, diagnostic

## State and Events

**State Management**
- Path: `assets/docs/dev_101_states.md`
- State is a string (or datetime/date for specific entity types)
- Attributes provide additional context
- State changes fire events

**Event System**
- Path: `assets/docs/dev_101_events.md`
- `state_changed` fired on state updates
- Custom events for integration-specific needs
- Path: `assets/docs/integration_events.md`

## Testing

**Test Structure**
- Path: `assets/docs/development_testing.md`
- Use pytest
- Mock external dependencies
- Test config flows, setup, and entity behavior

## Development Guidelines

**Code Quality**
- Path: `assets/docs/development_guidelines.md`
- Follow PEP 8
- Use type hints
- Async-first approach
- Path: `assets/docs/development_typing.md`

**Validation**
- Path: `assets/docs/development_validation.md`
- Run `python3 -m script.hassfest`
- Validates manifest and structure
- Checks requirements and dependencies

**Submission**
- Path: `assets/docs/development_submitting.md`
- Path: `assets/docs/development_checklist.md`
- Path: `assets/docs/review-process.md`

## Additional Topics

**Automations Support**
- Path: `assets/docs/automations.md`
- Triggers, conditions, actions

**Device Automation**
- Path: `assets/docs/device_automation_index.md`
- Device triggers: `assets/docs/device_automation_trigger.md`
- Device conditions: `assets/docs/device_automation_condition.md`
- Device actions: `assets/docs/device_automation_action.md`

**Bluetooth Integration**
- Path: `assets/docs/bluetooth.md`
- BLE device discovery and connection
- Path: `assets/docs/core/bluetooth/api.md`

**Voice and Intent**
- Path: `assets/docs/intent_index.md`
- Intent handling: `assets/docs/intent_handling.md`
- Built-in intents: `assets/docs/intent_builtin.md`

**Diagnostics**
- Path: `assets/docs/core/integration_diagnostics.md`
- Provide debugging information to users

**System Health**
- Path: `assets/docs/core/integration_system_health.md`
- Report integration health status

**Repairs**
- Path: `assets/docs/core/platform/repairs.md`
- Create repair issues for user attention

## AsyncIO Best Practices

- Path: `assets/docs/asyncio_index.md`
- AsyncIO 101: `assets/docs/asyncio_101.md`
- Working with async: `assets/docs/asyncio_working_with_async.md`
- Thread safety: `assets/docs/asyncio_thread_safety.md`
- Blocking operations: `assets/docs/asyncio_blocking_operations.md`
- Categorizing functions: `assets/docs/asyncio_categorizing_functions.md`
