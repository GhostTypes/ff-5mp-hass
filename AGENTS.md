# AGENTS.md

Working agreement for AI assistants contributing to `ff-5mp-hass`.

## Project Snapshot
- **Integration:** FlashForge printers for Home Assistant (HTTP API only).
- **Current release:** `v1.0.1`.
- **Entities shipped:** 28 total (18 sensors, 4 binary sensors, 2 switches, 3 buttons, 1 camera).
- **Key dependency:** `flashforge-python-api>=1.0.0` (see sibling repo `ff-5mp-api-py`).
- **Primary references:** `CLAUDE.md` (agent workflow), `AGENTS.md` (this playbook), `README.md` (user docs), `CHANGELOG.md`, `homeassistant/README.md`, `HOME_ASSISTANT_DOCS_COMPANION.md`, and `HACS_PUBLISHER_COMPANION.md`.

## Agent Roles
- **Coding Agents**
  - Implement or refine integration logic in `custom_components/flashforge/`.
  - Uphold async patterns; rely on `FlashForgeClient` HTTP endpoints and coordinator-managed state.
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
- Respect the HTTP-only policy—introduce TCP/G-code handling only by extending `flashforge-python-api`.
- Treat the coordinator as the single source of truth; entities should not cache printer state.
- Update `strings.json` and `translations/en.json` alongside config-flow text changes.
- Keep imports ordered and comments purposeful.
- Record any manual testing nuances in pull requests, issues, or release notes for future reference.

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
   - Switches: LED and filtration (may show unavailable if unsupported).
   - Buttons: pause, resume, cancel.
   - Camera: MJPEG stream available.
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
