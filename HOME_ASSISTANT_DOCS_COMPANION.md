# Home Assistant Docs Companion

Curated highlights from <https://www.home-assistant.io/docs/> for fast reference while developing and testing the FlashForge integration (or any Home Assistant customization). Links point back to the canonical docs for deeper dives.

---

## 1. Configuration Essentials

- **configuration.yaml basics**  
  - Edit via add-ons (File Editor, Studio Code Server), SMB/SSH, or by mounting the container file system.  
  - `configuration.yaml` lives in the root of the Home Assistant config directory (see *Settings → System → Repairs → Three-dots → System information* for the path).  
  - Keep formatting strict YAML: spaces only, two-space indent, strings with special characters quoted.
- **Validation pipeline**  
  1. `Settings → Developer Tools → YAML → Check Configuration` (or run `ha core check` / `hass --script check_config`).  
  2. Resolve errors before restarting. The checker reports file/line.  
  3. Reload where possible instead of restarting: most platforms expose `homeassistant.reload_*` services (e.g. automation, script, template).
- **Applying changes**  
  - Use the “Reload” buttons under *Developer Tools → YAML* for Automations, Scenes, Scripts, Template Entities, etc.  
  - Only restart Home Assistant when a platform lacks a reload service or you added a brand-new integration.
- **Troubleshooting tips**  
  - Configuration errors appear in *Settings → System → Logs* with domain + line details.  
  - Temporarily comment out suspicious blocks (`#` + space).  
  - Use `!include` and `!include_dir_*` directives to keep large configs manageable; `secrets.yaml` isolates credentials.

---

## 2. Automations Refresher

- **Building blocks**  
  - *Trigger* (event/time/state) starts the automation.  
  - *Condition* (optional) checks current state/time/sun/etc.  
  - *Action sequence* runs services, scripts, scenes, waits, repeats, etc.
- **Common trigger types**  
  - `state`, `numeric_state`, `event`, `time`, `time_pattern`, `sun`, `template`, `zone`, `device`.  
  - Use *Automation Editor* for guided setup or YAML for version control.
- **Run modes** (Automation Editor → “Mode”):  
  - `single` (default): ignores new triggers while running.  
  - `restart`: cancels the current run and restarts.  
  - `queued`: queues up to `max` runs.  
  - `parallel`: spawns concurrent runs up to `max`.
- **Automation Trace**  
  - View via the automation detail page → “Trace” to see step-by-step execution, variable values, conditions that failed.  
  - Use “Debug” panel to retrigger with custom data.
- **Testing loop**  
  1. Build or edit automation.  
  2. Use “Run” button to manually exercise actions.  
  3. Watch trace + logs for unexpected branches.  
  4. Iterate until stable, then enable.

---

## 3. Scripts & Scenes

- **Scripts** (<https://www.home-assistant.io/docs/scripts/>)  
  - YAML structure is a list of action maps; single actions can omit the list wrapper.  
  - `alias` gives each step a friendly label in traces.  
  - `variables:` section defines inputs; use `sequence:` vs `parallel:` to control flow.  
  - Control flow helpers: `choose`, `if`, `repeat` (counted / while / for-each), `wait_for_trigger`, `wait_for_template`, `delay`.  
  - `continue_on_error: true` prevents aborting on failures; `timeout` on waits guards against hangs.
- **Scenes** (<https://www.home-assistant.io/docs/scene/>)  
  - Capture current entity states in UI or define YAML `entities:` blocks.  
  - Apply with `scene.turn_on`. Ideal for restoring LED/filtration combos while testing the integration.
- **Blueprints** (<https://www.home-assistant.io/docs/blueprint/>)  
  - Shareable automation/script templates.  
  - Define `input:` selectors; use to document standard printer automations for end users.

---

## 4. Template Cheat Sheet

Located at <https://www.home-assistant.io/docs/configuration/templating/>.

- **General rules**  
  - Home Assistant uses Jinja2 with custom filters/functions.  
  - Templates render in many places: automations (`value_template`, `data`), scripts, helpers, notifications, template entities.  
  - Use the Template Editor (*Developer Tools → Templates*) for live evaluation.
- **Core objects**  
  - `states.sensor.printer_temperature.state` → raw state string.  
  - `state_attr('sensor.printer_temperature', 'unit_of_measurement')` → attribute accessor.  
  - `this` → current entity when inside template entities, helpful for avoiding `entity_id` hard-coding.  
  - `sensor_entities('integration_domain')`, `device_entities(device_id)`, `area_entities(area_id)` simplify lookups.
- **Favorite helpers**  
  - `is_state(entity_id, value)`, `is_state_attr(entity_id, attr, value)`.  
  - Math filters: `|float(default)`, `|round(1)`, `|int(0)`; date/time: `now()`, `as_timestamp()`.  
  - List/set helpers: `|map`, `|selectattr`, `|reject`, `|union`, `|difference`.  
  - Control: `{% if ... %}`, `{% for ... %}`, `iif(condition, true, false)` for inline selection.
- **Limited vs unrestricted templates**  
  - Menu options like notification titles accept full templates.  
  - Some fields (e.g., helper names) only allow limited variables; doc sections label the limitations.
- **MQTT & incoming data**  
  - Use `value_template` to normalize payloads; convert strings to numbers with `|float`.  
  - `from_json` converts JSON payloads to dicts/lists for attribute extraction.

---

## 5. Entity & Organization Notes

- **Entities vs devices vs areas**  
  - Entities represent functionality (e.g., `sensor.flashforge_nozzle_temperature`).  
  - Devices group entities from a single physical unit (the integration registers a device per printer).  
  - Areas/floors/labels organize them for dashboards, Assist, and voice.
- **Entity registry**  
  - Maintain consistent entity IDs by editing *Settings → Devices & Services → Entities → (⋮) → Rename*.  
  - Disabled-by-default entities (e.g., some diagnostic sensors) can be enabled per device.
- **Device registry**  
  - Stores manufacturer/model info supplied in `device_info`. Ensure integration populates it so HA surfaces brand/model.

---

## 6. Debugging & Maintenance

- **Logs**  
  - Access via *Settings → System → Logs* or tail `homeassistant.log`.  
  - For deeper tracing, temporarily set `logger:` configuration (e.g., `custom_components.flashforge: debug`).  
  - Automation/script errors surface in trace plus logs; look for service call failures or template exceptions.
- **Event monitor**  
  - *Developer Tools → Events* allows listening to raw bus events (great for verifying discovery responses, button presses).  
  - Use `event.fire` to simulate events while testing.
- **Diagnostics & Repairs**  
  - *Settings → System → Repairs* lists integration issues (deprecated keys, config errors).  
  - `Settings → System → About` shows version/build date for support tickets.
- **Backups & versioning**  
  - Snapshot before major config edits (Supervisor → System → Backups).  
  - Check release notes (<https://www.home-assistant.io/blog/>) for breaking changes every monthly release.

---

## 7. Integration Developer Highlights (Developer Docs)

- **Scaffold quickly**  
  - Run `python3 -m script.scaffold integration` in the dev container to generate a UI-configurable skeleton (config flow, tests, translations).  
  - Minimum viable integration still requires a unique `DOMAIN`, `async_setup`/`async_setup_entry`, and a valid manifest.
- **File layout conventions**  
  - Core files: `__init__.py`, `manifest.json`, per-platform modules (e.g., `sensor.py`), optional `services.yaml`, and `coordinator.py` for shared polling.  
  - Custom integrations live in `<config>/custom_components/<domain>` and **must** define `version` in `manifest.json`; built-ins live in `homeassistant/components/<domain>`.
- **Manifest essentials** (<https://developers.home-assistant.io/docs/creating_integration_manifest/>)  
  - Required keys: `domain`, `name`, `documentation`, `codeowners`, `requirements`, `integration_type`, `iot_class`.  
  - Optional helpers: `dependencies`, `after_dependencies`, `ssdp`, `zeroconf`, `loggers`, `issue_tracker`, `quality_scale`.  
  - Add `config_flow: true` when exposing a UI flow; include `version` for custom/override integrations.
- **Config & options flows** (<https://developers.home-assistant.io/docs/config_entries_config_flow_handler/>)  
  - Implement `ConfigFlow` with `async_step_*` methods returning `FlowResult`.  
  - Always call `self.async_set_unique_id(...)` followed by `_abort_if_unique_id_configured()` to avoid duplicates.  
  - Use `ConfigEntryAuthFailed` for credential errors; let HA prompt re-auth.  
  - Pair with `OptionsFlow` to expose runtime settings (e.g., polling interval, advanced toggles).
- **Data fetch patterns** (<https://developers.home-assistant.io/docs/integration_fetching_data/>)  
  - Prefer one `DataUpdateCoordinator` per API; expose data via `.data` to all entities.  
  - Handle throttling with `update_interval`; raise `UpdateFailed` on transient errors so HA surfaces them cleanly.  
  - For push APIs set `should_poll = False`, subscribe in `async_added_to_hass`, unsubscribe in `async_will_remove_from_hass`.
- **Setup failure handling** (<https://developers.home-assistant.io/docs/integration_setup_failures/>)  
  - Raise `ConfigEntryNotReady` in `async_setup_entry` when the device/cloud is offline so HA retries automatically.  
  - Raise `ConfigEntryAuthFailed` to mark entries for re-auth flows.  
  - Register cleanup via `entry.async_on_unload` (close sessions, stop coordinators).
- **Quality scale checkpoints** (<https://developers.home-assistant.io/docs/core/integration-quality-scale/>)  
  - 🥉 Bronze: UI setup, config-flow tests, basic docs (baseline for new integrations).  
  - 🥈 Silver: Robust error handling, diagnostics, system health, troubleshooting docs.  
  - 🥇 Gold / 🏆 Platinum: Options flows, localized strings, analytics, repair issues, mature test coverage.  
  - Use the published checklist to plan incremental upgrades.

## 8. Handy Quick Links

| Topic | Doc URL | Usage Tips |
| --- | --- | --- |
| configuration.yaml | <https://www.home-assistant.io/docs/configuration/> | Editing, validation, reloading core config files. |
| Automations overview | <https://www.home-assistant.io/docs/automation/basics/> | Trigger/condition/action fundamentals with examples. |
| Automation triggers | <https://www.home-assistant.io/docs/automation/trigger/> | Supported trigger types, payload fields, templates. |
| Automation actions | <https://www.home-assistant.io/docs/automation/action/> | Service calls, delays, chooses, repeats, parallelization. |
| Automation conditions | <https://www.home-assistant.io/docs/automation/condition/> | Time, state, template, numeric, zone, etc. |
| Scripts syntax | <https://www.home-assistant.io/docs/scripts/> | Sequential/parallel actions, waits, variables. |
| Scenes | <https://www.home-assistant.io/docs/scene/> | Capturing state snapshots, editing scenes. |
| Templates | <https://www.home-assistant.io/docs/configuration/templating/> | Jinja extensions, helper functions, examples. |
| Events | <https://www.home-assistant.io/docs/configuration/events/> | Understanding and firing/listening to events. |
| Troubleshooting | <https://www.home-assistant.io/docs/configuration/troubleshooting/> | Common configuration pitfalls and resolutions. |
| Scaffold & manifest | <https://developers.home-assistant.io/docs/creating_component_index/> | Generate integration skeleton; review required files/manifests. |
| Config flow handler | <https://developers.home-assistant.io/docs/config_entries_config_flow_handler/> | Build UI-based setup/option flows correctly. |
| DataUpdateCoordinator | <https://developers.home-assistant.io/docs/integration_fetching_data/> | Central polling, caching, and error handling best practices. |
| Setup failures | <https://developers.home-assistant.io/docs/integration_setup_failures/> | Exceptions that trigger retries vs. aborts. |
| Quality scale | <https://developers.home-assistant.io/docs/core/integration-quality-scale/> | Requirements for bronze/silver/gold/platinum tiers. |

---

## 9. Workflow Recommendations for Agents

1. **Prototype safely**: Duplicate automations/scripts into YAML test files and load with `!include` to roll back quickly.  
2. **Lint YAML**: Use VS Code with the Home Assistant extension or run `yamllint` in CI.  
3. **Document assumptions**: Capture integration-specific setup steps in `README.md` (e.g., LAN mode, check code).  
4. **Leverage traces**: Share automation trace downloads when filing bugs—they include full context.  
5. **Avoid restarts**: Prefer reload services to keep iterative testing fast.  
6. **Track breaking changes**: Monitor the monthly release notes—update integration metadata (min HA version, new services) promptly.

---

### Using This Companion

- Start with the links in section 8 when you need canonical wording to copy into docs or to confirm edge-case behavior.  
- Section 4’s template cheat sheet is ideal while adjusting sensors or script payloads.  
- Share this file with new contributors so they can ramp up without trawling the full docs tree.
