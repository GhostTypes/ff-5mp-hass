# AGENTS.md

Working agreement for AI assistants contributing to `ff-5mp-hass`.

## Project Snapshot
- **Integration:** FlashForge printers for Home Assistant (HTTP API only).
- **Current release:** `v1.3.0` (in-flight; not yet tagged). Last published: `v1.2.0`.
- **Supported printers:** `AD5X`, `Adventurer 5M`, `Adventurer 5M Pro`, `Creator 5`, and `Creator 5 Pro` only.
- **Entities shipped:** 58 total (38 sensors, 5 binary sensors, 2 switches (the camera switch is not created on the Creator 5 series), 2 selects, 5 buttons, 1 camera, 5 images — the g-code thumbnail plus 4 Material Station slot color swatches).
- **Services:** `flashforge.print_file` — starts a file already stored on the printer (entity service on the Local File Selection entity).
- **Key dependency:** `flashforge-python-api>=1.3.4` (see sibling repo `ff-5mp-api-py`).
- **Primary references:** `CLAUDE.md` (agent workflow), `AGENTS.md` (this playbook), `README.md` (user docs), `CHANGELOG.md`, `homeassistant/README.md`, `HOME_ASSISTANT_DOCS_COMPANION.md`, and `HACS_PUBLISHER_COMPANION.md`.

## Agent Roles
- **Coding Agents**
  - Implement or refine integration logic in `custom_components/flashforge/`.
  - Uphold async patterns; rely on `FlashForgeClient` HTTP endpoints and coordinator-managed state.
  - Keep the integration scoped to supported modern LAN mode HTTP printers only.
  - Mirror logic changes in translations and documentation.
  - Coordinate with Documentation/Test agents when feature surface changes.
- **Documentation Agents**
  - Maintain `README.md`, `CHANGELOG.md`, `CLAUDE.md`, and `AGENTS.md`.
  - Ensure end-user instructions, entity tables, and troubleshooting tips stay accurate.
  - Flag new features that require updated screenshots or GIFs (keep assets tracked externally).
- **Testing/Validation Agents**
  - Exercise the local HA sandbox under `homeassistant/`.
  - Follow the testing checklist below and log findings in issue/PR notes or release summaries.
  - Verify discovery scripts (`scripts/test_discovery.py`) when networking is touched.
  - Capture regressions or gaps and report back to Coding/Documentation agents.
- **Release Agents**
  - Confirm version bumps (`manifest.json`, `CHANGELOG.md`, tags).
  - Run final validation in HA sandbox and, if possible, on real hardware.
  - Prepare GitHub releases and ensure README badges reflect the latest status.

## Shared Guidelines
- Respect the HTTP-only policy—introduce TCP/G-code handling only by extending `flashforge-python-api`. The file list therefore comes from `files.get_recent_file_list()` (HTTP `/gcodeList`, most recent files only), never from the TCP directory listing.
- Treat the coordinator as the single source of truth; entities should not cache printer state.
- Update `strings.json` and `translations/en.json` alongside config-flow text changes.
- Keep imports ordered and comments purposeful.
- Record any manual testing nuances in pull requests, issues, or release notes for future reference.
- **Identify printers by PID, not name.** `config_flow.py` `_is_supported_detail()` checks the firmware-set `pid` on `/detail` against `SUPPORTED_PIDS = {35, 36, 38, 40, 41}` (5M, 5M Pro, AD5X, Creator 5, Creator 5 Pro); the upstream library (≥1.3.4) does the same internally to derive `is_pro` / `is_ad5x` / `is_creator5` / `is_creator5_pro`. The config-flow gate reads the **raw** `/detail` dict (`info.get_detail_raw()`), so model identity is established before any validation runs — reading `pid` off a parsed model let one unrelated bad field reject a supported printer (issue #18). The `name` field is user-mutable via the LCD or cloud and must never be substring-matched for model detection (broke in v1.1.8, fixed in v1.1.9 — see issue #13). Adding a new modern PID means updating `SUPPORTED_PIDS` here AND bumping the library dep floor.
- **Never trust the `/product` endpoint for capability gating.** It reliably reports filtration control for the Adventurer 5M Pro but misreports it for the Creator 5 Pro (wrong values). TVOC, chamber fan speed, and the filtration select are therefore gated on model identity (`is_pro OR is_creator5_pro`), not on the `/product`-derived `client.filtration_control` flag. Once the API gates capabilities internally we can re-derive from `/product`.
- **A capability that can be "unknown" will be read as "no".** Firmware omits fields that don't apply to a model, so an absent value means "not reported", and any `None`-able flag invites a consumer to collapse the two. `hasMatlStation` is the case that bit us: AD5X-only, absent on a Creator 5 Pro that has four loaded slots, so the Material Station entities never appeared on the models that have a station. Gate on a derived, always-concrete capability — `FFMachineInfo.has_matl_station` (library ≥1.3.2) — never on a raw `/detail` passthrough. The same trap caught `led_control_override`, where the option's unset `False` was read by the library as "force the capability off" and greyed out the LED switch on every printer; tri-state parameters need `None` for "no opinion".
- **Capability-gated entities must be added when the capability appears, not only at setup.** Platform setup can run before the printer has reported a capability, and the first refresh may fail outright. Add what is available, then watch `coordinator.async_add_listener` for the rest (see `image.py` / `sensor.py`), latching so a capability is only added once and registering the teardown with `entry.async_on_unload`.
- **A button's availability must not depend on anything but reachability.** A button entity is stateless — its state *is* the last-press timestamp — so any write of that state is reported to the logbook as a press. Gating availability on a selection or a mode means changing that input logs a phantom press. Validate in `async_press` and raise `ServiceValidationError` instead.
- **Never validate the *range* of data received from the printer.** Pydantic validates a model all-or-nothing, so a single `ge=`/`le=` on any one of ~50 `/detail` fields fails the whole response — the library returns "no data" and every entity goes unavailable. Firmware also reports absent hardware with out-of-band sentinels (`chamberTemp: -108` on a Creator 5 with no chamber heater) instead of omitting the field, so "impossible" values are routine. That exact constraint made the integration unusable for a whole printer configuration across three releases (issue #18) while every message blamed the network. Inbound models validate types only; ranges belong on outbound command models, where a bad value is our own bug. Needed bounds get normalized in the parser, never rejected. Same rule for required fields: only require what the payload is meaningless without.
- **A response we cannot read must never be reported as a printer we cannot reach.** `FlashForgeResponseError` (library ≥1.3.4) means the printer answered and we failed to parse it; a `None` return means the request never got through. The first is a bug report, the second is a network check, and the user can only act on the right one. The config flow maps them to `invalid_response` and `cannot_connect` respectively; `__init__.py` and `coordinator.py` log them with matching, distinct wording. Never flatten the exception into `ConnectionError`.
- **Gate on the capability the printer reported, not on the model that usually has it.** Options exist within a model family — the heated chamber is a Creator 5 extra, not a family trait, so chamber sensors gate on `has_chamber_sensor` rather than `is_creator5`. Gating on the family gave chamber-less units two entities pinned at 0 °C. Model identity is only the right signal when the model's API genuinely cannot do the thing at all (filtration, the Creator 5 camera switch).
- **"Unavailable" and "not created" are different answers; pick the one that is true.** Grey an entity out (`availability_fn`) when the printer *could* report the feature later — that is a temporary state. Omit it entirely (`supported_fn` in `switch.py`, applied once at setup where model identity is already known) when the model's API cannot perform the action at all. The Creator 5 camera switch is the case: its `streamCtrl_cmd` returns success and does nothing, and `cameraStreamUrl` stays populated so the switch snaps back to `on` — a control that accepts a press, reports success and changes nothing is worse than a missing one. Confirm on hardware before deciding a command is inert; "available but unconfirmed" is a fine interim state, "available and known-inert" is not.

## Standard Workflows
### Feature or Bug Fix
1. Review `CLAUDE.md` for current practices.
2. Modify integration code; adjust entities and capability checks as needed.
3. Update docs/translations; bump version if user-facing behavior changes.
4. Validate in the HA sandbox; document results alongside the work item (PR/issue/release).

### Documentation-Only Update
1. Sync wording with the actual implementation.
2. Ensure tables and entity counts match `sensor.py`, `binary_sensor.py`, etc.
3. Update related references in `README.md`, `CHANGELOG.md`, `CLAUDE.md`, and `AGENTS.md`.

### Release Prep
1. Confirm feature completeness and manual test coverage.
2. Align `manifest.json`, `CHANGELOG.md`, README badges, and tags.
3. Draft release notes highlighting new capabilities and testing status.

## Testing Checklist
1. **Pre-flight** – Printer powered, LAN mode enabled, check code/serial handy; integration copied or symlinked into Home Assistant; restart Home Assistant.
2. **Config Flow** – Run both discovery and manual setup paths; ensure credentials are validated and duplicate detection works.
3. **Entities** – On the device page verify:
   - Sensors: machine status, nozzle temps/targets, bed temps/targets, progress, file, current/total layers, elapsed/remaining time, filament length/weight, print speed, z offset, move mode, nozzle size, filament type.
   - Binary sensors: printing, online, error, paused.
   - Switches: LED and camera power (may show unavailable if unsupported).
   - Select: filtration mode (may show unavailable if unsupported); Local File Selection (lists the printer's files, selecting starts nothing).
   - Buttons: pause, resume, cancel, clear status, print selected file.
   - Service: `flashforge.print_file` (defaults to the selected file, accepts any file name on the printer).
   - Camera: entity exists and becomes available when the printer reports an OEM stream URL.
4. **Controls** – Exercise switches and buttons; confirm state refreshes and coordinator remains healthy.
5. **Resilience** – Temporarily disrupt connectivity (e.g., disable LAN mode) and confirm graceful error handling and recovery in Home Assistant logs.
6. **Discovery Scripts** – When networking changes, run `scripts/test_discovery.py` or `scripts/discovery_probe.py` to confirm UDP discovery continues to succeed.

## Quick Reference
- **Integration source:** `custom_components/flashforge/`
- **Local HA sandbox:** `homeassistant/`
- **Discovery tools:** `scripts/` (no legacy reference repo needed)
- **Agent playbooks:** `CLAUDE.md`, `AGENTS.md`
- **Doc companions:** `HOME_ASSISTANT_DOCS_COMPANION.md`, `HACS_PUBLISHER_COMPANION.md`

Always log meaningful changes and decisions so the next agent can pick up without guesswork.
