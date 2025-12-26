# Config Flows and Data Management

Configuration flows allow users to set up integrations through the UI rather than YAML. This is the recommended approach for all new integrations.

## Core Documentation

**Config Flow Handler** - Main setup flow
- Path: `assets/docs/config_entries_config_flow_handler.md`
- Creating UI-based setup flows
- Step definitions and validation
- Unique ID handling to prevent duplicates

**Options Flow Handler** - Runtime configuration
- Path: `assets/docs/config_entries_options_flow_handler.md`
- Allow users to modify settings after setup
- Exposing configuration options in UI

**Data Entry Flow** - Framework basics
- Path: `assets/docs/data_entry_flow_index.md`
- Flow step return types
- Form schemas with voluptuous
- Error handling and validation

## Key Concepts

### Config Entry Lifecycle

1. **Discovery/User Initiation** → Config Flow
2. **Setup** → `async_setup_entry()`
3. **Runtime** → Integration runs, coordinates data
4. **Reload** → Unload and reload entry
5. **Options** → Options Flow for configuration changes
6. **Remove** → `async_unload_entry()`

### Setup and Teardown

**Setup Failures**
- Path: `assets/docs/integration_setup_failures.md`
- Raise `ConfigEntryNotReady` for temporary failures
- Raise `ConfigEntryAuthFailed` for auth issues
- Use `entry.async_on_unload()` for cleanup

**Unloading**
- Always implement `async_unload_entry()`
- Stop coordinators
- Close connections
- Clean up listeners

## Data Fetching Patterns

**DataUpdateCoordinator**
- Path: `assets/docs/integration_fetching_data.md`
- Central polling for multiple entities
- Automatic retry with exponential backoff
- Handles `UpdateFailed` exceptions
- Shares data across all entities

**Push vs Pull**
- Pull: Use DataUpdateCoordinator with update_interval
- Push: Set `should_poll = False`, subscribe in `async_added_to_hass()`

## Registry Management

**Entity Registry**
- Path: `assets/docs/entity_registry_index.md`
- Tracks unique_id to entity_id mapping
- Persistence across restarts
- Disabled by default entities

**Device Registry**  
- Path: `assets/docs/device_registry_index.md`
- Groups entities by physical device
- Stores manufacturer, model, sw_version
- Device identification and organization

**Area Registry**
- Path: `assets/docs/area_registry_index.md`
- Location-based organization
- Used for voice commands and automation

## Network Discovery

**Discovery Support**
- Path: `assets/docs/network_discovery.md`
- mDNS (Zeroconf)
- SSDP (UPnP)
- DHCP
- USB
- Bluetooth

## Authentication

**Auth Module**
- Path: `assets/docs/auth_auth_module.md`
- Custom authentication providers

**Auth Provider**
- Path: `assets/docs/auth_auth_provider.md`
- Login provider implementation

**Permissions**
- Path: `assets/docs/auth_permissions.md`
- Policy-based access control

## Best Practices

### Unique IDs
- Always call `self.async_set_unique_id()` early in config flow
- Follow with `self._abort_if_unique_id_configured()` to prevent duplicates
- Use stable identifiers (MAC address, serial number, etc.)

### Error Handling
- Validate user input before attempting connections
- Provide clear error messages
- Use schema validation for type safety

### Step Flow Pattern
```python
async def async_step_user(self, user_input=None):
    errors = {}
    
    if user_input is not None:
        # Validate and create entry
        try:
            await self._test_connection(user_input)
        except ConnectionError:
            errors["base"] = "cannot_connect"
        except Exception:
            errors["base"] = "unknown"
        else:
            return self.async_create_entry(
                title=user_input["host"],
                data=user_input
            )
    
    return self.async_show_form(
        step_id="user",
        data_schema=vol.Schema({
            vol.Required("host"): str,
            vol.Required("password"): str,
        }),
        errors=errors
    )
```

### Options Flow Pattern
```python
@staticmethod
@callback
def async_get_options_flow(config_entry):
    return OptionsFlowHandler(config_entry)

class OptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)
        
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional(
                    "scan_interval",
                    default=self.config_entry.options.get("scan_interval", 60)
                ): int,
            })
        )
```

## Related Documentation

- Config entries index: `assets/docs/config_entries_index.md`
- YAML configuration (legacy): `assets/docs/configuration_yaml_index.md`
