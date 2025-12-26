# Integration Quality Scale

The Home Assistant integration quality scale defines requirements for different quality tiers. Meeting higher tiers makes integrations more reliable and user-friendly.

## Overview

**Main Documentation**
- Path: `assets/docs/core/integration-quality-scale.md`
- Checklist: `assets/docs/core/integration-quality-scale/checklist.md`
- All rules: `assets/docs/core/integration-quality-scale/rules.md`

## Quality Tiers

### No Score (Baseline)
Minimum requirements for any integration:
- Valid manifest.json
- Passes hassfest validation
- Basic functionality works

### Bronze 🥉
Foundation tier - UI-based setup and testing:
- Config flow (not YAML configuration)
- Test coverage for config flow
- Unique config entry (no duplicates)
- Proper documentation structure
- Brand assets in home-assistant/brands

**Key Rules:**
- `config-flow`: `assets/docs/core/integration-quality-scale/rules/config-flow.md`
- `config-flow-test-coverage`: `assets/docs/core/integration-quality-scale/rules/config-flow-test-coverage.md`
- `unique-config-entry`: `assets/docs/core/integration-quality-scale/rules/unique-config-entry.md`
- `brands`: `assets/docs/core/integration-quality-scale/rules/brands.md`

### Silver 🥈
Reliability tier - proper error handling and user experience:
- Reauthentication flow for expired credentials
- Handles setup failures gracefully (ConfigEntryNotReady)
- Runtime data storage in entry.runtime_data
- Test coverage before configuration
- Entities have proper device classes
- Entities are unavailable when appropriate
- Proper logging when unavailable

**Key Rules:**
- `reauthentication-flow`: `assets/docs/core/integration-quality-scale/rules/reauthentication-flow.md`
- `test-before-configure`: `assets/docs/core/integration-quality-scale/rules/test-before-configure.md`
- `runtime-data`: `assets/docs/core/integration-quality-scale/rules/runtime-data.md`
- `entity-device-class`: `assets/docs/core/integration-quality-scale/rules/entity-device-class.md`
- `entity-unavailable`: `assets/docs/core/integration-quality-scale/rules/entity-unavailable.md`
- `log-when-unavailable`: `assets/docs/core/integration-quality-scale/rules/log-when-unavailable.md`

### Gold 🥇
Excellence tier - polished user experience:
- Reconfiguration flow (change settings without re-adding)
- Diagnostics for debugging
- Test coverage before setup
- Appropriate polling intervals
- Parallel updates when safe
- Entities use translations (not hardcoded names)
- Entity naming follows best practices (has_entity_name)
- Custom icons with translations

**Key Rules:**
- `reconfiguration-flow`: `assets/docs/core/integration-quality-scale/rules/reconfiguration-flow.md`
- `diagnostics`: `assets/docs/core/integration-quality-scale/rules/diagnostics.md`
- `test-before-setup`: `assets/docs/core/integration-quality-scale/rules/test-before-setup.md`
- `appropriate-polling`: `assets/docs/core/integration-quality-scale/rules/appropriate-polling.md`
- `parallel-updates`: `assets/docs/core/integration-quality-scale/rules/parallel-updates.md`
- `entity-translations`: `assets/docs/core/integration-quality-scale/rules/entity-translations.md`
- `has-entity-name`: `assets/docs/core/integration-quality-scale/rules/has-entity-name.md`
- `icon-translations`: `assets/docs/core/integration-quality-scale/rules/icon-translations.md`

### Platinum 🏆
Exceptional tier - advanced features and documentation:
- Repair issues for user-actionable problems
- Service actions with proper validation
- Entity event platform for webhooks/push events
- Comprehensive documentation with examples
- Dependency transparency
- Proper entity categories (config/diagnostic)
- Action exception handling and translations
- Dynamic device management

**Key Rules:**
- `repair-issues`: `assets/docs/core/integration-quality-scale/rules/repair-issues.md`
- `action-setup`: `assets/docs/core/integration-quality-scale/rules/action-setup.md`
- `action-exceptions`: `assets/docs/core/integration-quality-scale/rules/action-exceptions.md`
- `entity-event-setup`: `assets/docs/core/integration-quality-scale/rules/entity-event-setup.md`
- `entity-category`: `assets/docs/core/integration-quality-scale/rules/entity-category.md`
- `dependency-transparency`: `assets/docs/core/integration-quality-scale/rules/dependency-transparency.md`

## All Quality Scale Rules

Complete rule documentation is available in:
`assets/docs/core/integration-quality-scale/rules/`

### Common Rules Across Tiers

**Testing:**
- test-coverage.md - Minimum test coverage requirements
- test-before-setup.md - Test connection before creating entry
- test-before-configure.md - Validate before showing config form

**Entity Handling:**
- entity-unique-id.md - All entities must have unique IDs
- entity-disabled-by-default.md - Diagnostic entities disabled by default
- entity-device-class.md - Use appropriate device classes
- entity-category.md - Categorize config/diagnostic entities
- has-entity-name.md - Use has_entity_name pattern
- entity-translations.md - Translate entity names and states
- icon-translations.md - Translate custom icons

**Setup & Configuration:**
- config-flow.md - UI-based configuration required
- config-entry-unloading.md - Proper teardown on unload
- unique-config-entry.md - Prevent duplicate entries
- reauthentication-flow.md - Handle auth failures
- reconfiguration-flow.md - Allow reconfiguration

**Discovery:**
- discovery.md - Implement appropriate discovery methods
- discovery-update-info.md - Update discovered entry info

**Device Management:**
- devices.md - Provide device information
- dynamic-devices.md - Handle device changes
- stale-devices.md - Clean up removed devices

**Documentation:**
- docs-high-level-description.md - Clear overview
- docs-installation-instructions.md - Setup guide
- docs-installation-parameters.md - Explain config parameters
- docs-configuration-parameters.md - Document options
- docs-examples.md - Provide examples
- docs-use-cases.md - Describe use cases
- docs-known-limitations.md - Document limitations
- docs-troubleshooting.md - Troubleshooting guide
- docs-removal-instructions.md - Removal guide
- docs-supported-devices.md - List supported hardware
- docs-supported-functions.md - Document features
- docs-actions.md - Document service actions
- docs-data-update.md - Explain data update mechanism

**Code Quality:**
- strict-typing.md - Use type hints
- async-dependency.md - Use async libraries
- common-modules.md - Share code via common modules
- inject-websession.md - Use aiohttp_client.async_get_clientsession()

**Other:**
- integration-owner.md - At least one codeowner
- brands.md - Brand assets registered
- diagnostics.md - Provide diagnostic data
- appropriate-polling.md - Reasonable poll intervals
- parallel-updates.md - Allow parallel updates when safe
- dependency-transparency.md - Declare all dependencies
- repair-issues.md - Create repairs for issues
- exception-translations.md - Translate exception messages

## Progressive Enhancement Strategy

Start with Bronze and progressively add features:

1. **Start:** Basic integration with config flow
2. **Bronze:** Add tests, brand assets, basic docs
3. **Silver:** Add reauth flow, error handling, proper entity states
4. **Gold:** Add reconfigure flow, diagnostics, translations, proper naming
5. **Platinum:** Add repairs, service actions, advanced docs, event entities

## Quality Scale in Custom Integrations

While the quality scale is designed for built-in integrations, following these guidelines makes custom integrations:
- More reliable and user-friendly
- Easier to debug
- Ready for potential inclusion in core
- Professional and polished

Focus especially on:
- Config flow (Bronze requirement)
- Reauth flow (Silver - handles expired credentials gracefully)
- Proper entity unavailability (Silver - users see offline status)
- Diagnostics (Gold - easier troubleshooting)
- Good documentation (all tiers)
