# Source: https://developers.home-assistant.io/docs/dev_101_config

On [the hass object](/docs/dev_101_hass) there is an instance of the Config class. The Config class contains the users preferred units, the path to the config directory and which components are loaded.

| Name | Type | Description |
| --- | --- | --- |
| latitude | float | Latitude of the instance location |
| longitude | float | Longitude of the instance location |
| elevation | int | Elevation of the instance |
| location\_name | str | Name of the instance |
| time\_zone | str | Timezone |
| units | UnitSystem | Unit system |
| internal\_url | str | URL the instance can be reached on internally |
| external\_url | str | URL the instance can be reached on externally |
| currency | str | Preferred currency |
| country | str | Country the instance is in |
| language | str | Preferred language |
| config\_source | ConfigSource | If the configuration was set via the UI or stored in YAML |
| skip\_pip | bool | If True, pip install is skipped for requirements on startup |
| skip\_pip\_packages | list[str] | List of packages to skip when installing requirements on startup |
| components | set[str] | List of loaded components |
| api | ApiConfig | API (HTTP) server configuration |
| config\_dir | str | Directory that holds the configuration |
| allowlist\_external\_dirs | set[str] | List of allowed external dirs to access |
| allowlist\_external\_urls | set[str] | List of allowed external URLs that integrations may use |
| media\_dirs | dict[str, str] | Dictionary of Media folders that integrations may use |
| safe\_mode | bool | If Home Assistant is running in safe mode |
| legacy\_templates | bool | Use legacy template behavior |

It also provides some helper methods.