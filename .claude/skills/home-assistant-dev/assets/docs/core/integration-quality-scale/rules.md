# Source: https://developers.home-assistant.io/docs/core/integration-quality-scale/rules

The rules for each tier are defined down below and come with its own page with examples and more information.

### 🥉 Bronze

* [action-setup](/docs/core/integration-quality-scale/rules/action-setup) - Service actions are registered in async\_setup
* [appropriate-polling](/docs/core/integration-quality-scale/rules/appropriate-polling) - If it's a polling integration, set an appropriate polling interval
* [brands](/docs/core/integration-quality-scale/rules/brands) - Has branding assets available for the integration
* [common-modules](/docs/core/integration-quality-scale/rules/common-modules) - Place common patterns in common modules
* [config-flow-test-coverage](/docs/core/integration-quality-scale/rules/config-flow-test-coverage) - Full test coverage for the config flow
* [config-flow](/docs/core/integration-quality-scale/rules/config-flow) - Integration needs to be able to be set up via the UI
* [dependency-transparency](/docs/core/integration-quality-scale/rules/dependency-transparency) - Dependency transparency
* [docs-actions](/docs/core/integration-quality-scale/rules/docs-actions) - The documentation describes the provided service actions that can be used
* [docs-high-level-description](/docs/core/integration-quality-scale/rules/docs-high-level-description) - The documentation includes a high-level description of the integration brand, product, or service
* [docs-installation-instructions](/docs/core/integration-quality-scale/rules/docs-installation-instructions) - The documentation provides step-by-step installation instructions for the integration, including, if needed, prerequisites
* [docs-removal-instructions](/docs/core/integration-quality-scale/rules/docs-removal-instructions) - The documentation provides removal instructions
* [entity-event-setup](/docs/core/integration-quality-scale/rules/entity-event-setup) - Entity events are subscribed in the correct lifecycle methods
* [entity-unique-id](/docs/core/integration-quality-scale/rules/entity-unique-id) - Entities have a unique ID
* [has-entity-name](/docs/core/integration-quality-scale/rules/has-entity-name) - Entities use has\_entity\_name = True
* [runtime-data](/docs/core/integration-quality-scale/rules/runtime-data) - Use ConfigEntry.runtime\_data to store runtime data
* [test-before-configure](/docs/core/integration-quality-scale/rules/test-before-configure) - Test a connection in the config flow
* [test-before-setup](/docs/core/integration-quality-scale/rules/test-before-setup) - Check during integration initialization if we are able to set it up correctly
* [unique-config-entry](/docs/core/integration-quality-scale/rules/unique-config-entry) - Don't allow the same device or service to be able to be set up twice

### 🥈 Silver

* [action-exceptions](/docs/core/integration-quality-scale/rules/action-exceptions) - Service actions raise exceptions when encountering failures
* [config-entry-unloading](/docs/core/integration-quality-scale/rules/config-entry-unloading) - Support config entry unloading
* [docs-configuration-parameters](/docs/core/integration-quality-scale/rules/docs-configuration-parameters) - The documentation describes all integration configuration options
* [docs-installation-parameters](/docs/core/integration-quality-scale/rules/docs-installation-parameters) - The documentation describes all integration installation parameters
* [entity-unavailable](/docs/core/integration-quality-scale/rules/entity-unavailable) - Mark entity unavailable if appropriate
* [integration-owner](/docs/core/integration-quality-scale/rules/integration-owner) - Has an integration owner
* [log-when-unavailable](/docs/core/integration-quality-scale/rules/log-when-unavailable) - If internet/device/service is unavailable, log once when unavailable and once when back connected
* [parallel-updates](/docs/core/integration-quality-scale/rules/parallel-updates) - Number of parallel updates is specified
* [reauthentication-flow](/docs/core/integration-quality-scale/rules/reauthentication-flow) - Reauthentication needs to be available via the UI
* [test-coverage](/docs/core/integration-quality-scale/rules/test-coverage) - Above 95% test coverage for all integration modules

### 🥇 Gold

* [devices](/docs/core/integration-quality-scale/rules/devices) - The integration creates devices
* [diagnostics](/docs/core/integration-quality-scale/rules/diagnostics) - Implements diagnostics
* [discovery-update-info](/docs/core/integration-quality-scale/rules/discovery-update-info) - Integration uses discovery info to update network information
* [discovery](/docs/core/integration-quality-scale/rules/discovery) - Devices can be discovered
* [docs-data-update](/docs/core/integration-quality-scale/rules/docs-data-update) - The documentation describes how data is updated
* [docs-examples](/docs/core/integration-quality-scale/rules/docs-examples) - The documentation provides automation examples the user can use.
* [docs-known-limitations](/docs/core/integration-quality-scale/rules/docs-known-limitations) - The documentation describes known limitations of the integration (not to be confused with bugs)
* [docs-supported-devices](/docs/core/integration-quality-scale/rules/docs-supported-devices) - The documentation describes known supported / unsupported devices
* [docs-supported-functions](/docs/core/integration-quality-scale/rules/docs-supported-functions) - The documentation describes the supported functionality, including entities, and platforms
* [docs-troubleshooting](/docs/core/integration-quality-scale/rules/docs-troubleshooting) - The documentation provides troubleshooting information
* [docs-use-cases](/docs/core/integration-quality-scale/rules/docs-use-cases) - The documentation describes use cases to illustrate how this integration can be used
* [dynamic-devices](/docs/core/integration-quality-scale/rules/dynamic-devices) - Devices added after integration setup
* [entity-category](/docs/core/integration-quality-scale/rules/entity-category) - Entities are assigned an appropriate EntityCategory
* [entity-device-class](/docs/core/integration-quality-scale/rules/entity-device-class) - Entities use device classes where possible
* [entity-disabled-by-default](/docs/core/integration-quality-scale/rules/entity-disabled-by-default) - Integration disables less popular (or noisy) entities
* [entity-translations](/docs/core/integration-quality-scale/rules/entity-translations) - Entities have translated names
* [exception-translations](/docs/core/integration-quality-scale/rules/exception-translations) - Exception messages are translatable
* [icon-translations](/docs/core/integration-quality-scale/rules/icon-translations) - Entities implement icon translations
* [reconfiguration-flow](/docs/core/integration-quality-scale/rules/reconfiguration-flow) - Integrations should have a reconfigure flow
* [repair-issues](/docs/core/integration-quality-scale/rules/repair-issues) - Repair issues and repair flows are used when user intervention is needed
* [stale-devices](/docs/core/integration-quality-scale/rules/stale-devices) - Stale devices are removed

### 🏆 Platinum

* [async-dependency](/docs/core/integration-quality-scale/rules/async-dependency) - Dependency is async
* [inject-websession](/docs/core/integration-quality-scale/rules/inject-websession) - The integration dependency supports passing in a websession
* [strict-typing](/docs/core/integration-quality-scale/rules/strict-typing) - Strict typing