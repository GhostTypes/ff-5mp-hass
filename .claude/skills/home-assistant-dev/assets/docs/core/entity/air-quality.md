# Source: https://developers.home-assistant.io/docs/core/entity/air-quality

## Properties

Deprecated

The Air Quality entity is deprecated and should not be used. Instead, use
separate sensors for these measurements.

Integrations that still rely on the Air Quality Entity should be migrated.

> **caution**
>
> The Air Quality entity does not support attribute shorthand for [property implementation](/docs/core/entity#entity-class-or-instance-attributes)

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| particulate\_matter\_2\_5 | `str | int | float | None` | **Required** | The particulate matter 2.5 (<= 2.5 μm) level. |
| particulate\_matter\_10 | `str | int | float | None` | `None` | The particulate matter 10 (<= 10 μm) level. |
| particulate\_matter\_0\_1 | `str | int | float | None` | `None` | The particulate matter 0.1 (<= 0.1 μm) level. |
| air\_quality\_index | `str | int | float | None` | `None` | The Air Quality Index (AQI). |
| ozone | `str | int | float | None` | `None` | The O3 (ozone) level. |
| carbon\_monoxide | `str | int | float | None` | `None` | The CO (carbon monoxide) level. |
| carbon\_dioxide | `str | int | float | None` | `None` | The CO2 (carbon dioxide) level. |
| sulphur\_dioxide | `str | int | float | None` | `None` | The SO2 (sulphur dioxide) level. |
| nitrogen\_oxide | `str | int | float | None` | `None` | The N2O (nitrogen oxide) level. |
| nitrogen\_monoxide | `str | int | float | None` | `None` | The NO (nitrogen monoxide) level. |
| nitrogen\_dioxide | `str | int | float | None` | `None` | The NO2 (nitrogen dioxide) level. |

Properties have to follow the units defined in the `unit_system`.