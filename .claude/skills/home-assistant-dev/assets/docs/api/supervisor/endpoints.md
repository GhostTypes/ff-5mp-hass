# Source: https://developers.home-assistant.io/docs/api/supervisor/endpoints

For API endpoints marked with 🔒 you need use an authorization header with a `Bearer` token.

The token is available for add-ons and Home Assistant using the
`SUPERVISOR_TOKEN` environment variable.

To see more details about each endpoint, click on it to expand it.

### Add-ons

get

`/addons`

🔒

Return overview information about installed add-ons.

**Payload:**

| key | type | description |
| --- | --- | --- |
| addons | list | A list of [Addon models](/docs/api/supervisor/models#addon) |

**Example response:**

```
{
  "addons": [
    {
      "name": "Awesome add-on",
      "slug": "awesome_addon",
      "description": "My awesome add-on",
      "advanced": false,
      "stage": "stable",
      "repository": "core",
      "version": null,
      "version_latest": "1.0.1",
      "update_available": false,
      "installed": false,
      "detached": true,
      "available": true,
      "build": false,
      "url": null,
      "icon": false,
      "logo": false,
      "system_managed": false
    }
  ]
}
```

post

`/addons/reload`

🔒

Reloads the information stored about add-ons.

get

`/addons/<addon>/changelog`

🔒

Get the changelog for an add-on.

get

`/addons/<addon>/documentation`

🔒

Get the documentation for an add-on.

get

`/addons/<addon>/logs`

🔒

Get logs for an add-on via the Systemd journal backend.

The endpoint accepts the same headers and provides the same functionality as
`/host/logs`.

get

`/addons/<addon>/logs/follow`

🔒

Identical to `/addons/<addon>/logs` except it continuously returns new log entries.

get

`/addons/<addon>/logs/latest`

🔒

Return all logs of the latest startup of the add-on container.

The `Range` header is ignored but the `lines` query parameter can be used.

get

`/addons/<addon>/logs/boots/<bootid>`

🔒

Get logs for an add-on related to a specific boot.

The `bootid` parameter is interpreted in the same way as in
`/host/logs/boots/<bootid>` and the endpoint otherwise provides the same
functionality as `/host/logs`.

get

`/addons/<addon>/logs/boots/<bootid>/follow`

🔒

Identical to `/addons/<addon>/logs/boots/<bootid>` except it continuously returns
new log entries.

get

`/addons/<addon>/icon`

🔒

Get the add-on icon

get

`/addons/<addon>/info`

🔒

Get details about an add-on

**Returned data:**

| key | type | description |
| --- | --- | --- |
| advanced | boolean | `true` if advanced mode is enabled |
| apparmor | string | disabled, default or the name of the profile |
| arch | list | A list of supported architectures for the add-on |
| audio | boolean | `true` if audio is enabled |
| audio\_input | float or null | The device index |
| audio\_output | float or null | The device index |
| auth\_api | boolean | `true` if auth api access is granted is enabled |
| auto\_uart | boolean | `true` if auto\_uart access is granted is enabled |
| auto\_update | boolean | `true` if auto update is enabled |
| available | boolean | `true` if the add-on is available |
| boot | string | "auto" or "manual" |
| boot\_config | string | Default boot mode of addon or "manual\_only" if boot mode cannot be auto |
| build | boolean | `true` if local add-on |
| changelog | boolean | `true` if changelog is available |
| description | string | The add-on description |
| detached | boolean | `true` if the add-on is running detached |
| devices | list | A list of attached devices |
| devicetree | boolean | `true` if devicetree access is granted is enabled |
| discovery | list | A list of discovery services |
| dns | list | A list of DNS servers used by the add-on |
| docker\_api | boolean | `true` if docker\_api access is granted is enabled |
| documentation | boolean | `true` if documentation is available |
| full\_access | boolean | `true` if full access access is granted is enabled |
| gpio | boolean | `true` if gpio access is granted is enabled |
| hassio\_api | boolean | `true` if hassio api access is granted is enabled |
| hassio\_role | string | The hassio role (default, homeassistant, manager, admin) |
| homeassistant | string or null | The minimum Home Assistant Core version |
| homeassistant\_api | boolean | `true` if homeassistant api access is granted is enabled |
| host\_dbus | boolean | `true` if host dbus access is granted is enabled |
| host\_ipc | boolean | `true` if host ipc access is granted is enabled |
| host\_network | boolean | `true` if host network access is granted is enabled |
| host\_pid | boolean | `true` if host pid access is granted is enabled |
| host\_uts | boolean | `true` if host UTS namespace access is enabled. |
| hostname | string | The host name of the add-on |
| icon | boolean | `true` if icon is available |
| ingress | boolean | `true` if ingress is enabled |
| ingress\_entry | string or null | The ingress entrypoint |
| ingress\_panel | boolean or null | `true` if ingress\_panel is enabled |
| ingress\_port | int or null | The ingress port |
| ingress\_url | string or null | The ingress URL |
| ip\_address | string | The IP address of the add-on |
| kernel\_modules | boolean | `true` if kernel module access is granted is enabled |
| logo | boolean | `true` if logo is available |
| long\_description | string | The long add-on description |
| machine | list | A list of supported machine types for the add-on |
| name | string | The name of the add-on |
| network | dictionary or null | The network configuration for the add-on |
| network\_description | dictionary or null | The description for the network configuration |
| options | dictionary | The add-on configuration |
| privileged | list | A list of hardwars/system attributes the add-onn has access to |
| protected | boolean | `true` if protection mode is enabled |
| rating | int | The addon rating |
| repository | string | The URL to the add-on repository |
| schema | dictionary or null | The schema for the add-on configuration |
| services\_role | list | A list of services and the add-ons role for that service |
| slug | string | The add-on slug |
| stage | string | The add-on stage (stable, experimental, deprecated) |
| startup | string | The stage when the add-on is started (initialize, system, services, application, once) |
| state | string or null | The state of the add-on (started, stopped) |
| stdin | boolean | `true` if the add-on accepts stdin commands |
| system\_managed | boolean | Indicates whether the add-on is managed by Home Assistant |
| system\_managed\_config\_entry | string | Provides the configuration entry ID if the add-on is managed by Home Assistant |
| translations | dictionary | A dictionary containing content of translation files for the add-on |
| udev | boolean | `true` if udev access is granted is enabled |
| update\_available | boolean | `true` if an update is available |
| url | string or null | URL to more information about the add-on |
| usb | list | A list of attached USB devices |
| version | string | The installed version of the add-on |
| version\_latest | string | The latest version of the add-on |
| video | boolean | `true` if video is enabled |
| watchdog | boolean | `true` if watchdog is enabled |
| webui | string or null | The URL to the web UI for the add-on |
| signed | boolean | True if the image is signed and trust |

**Example response:**

```
{
  "advanced": false,
  "apparmor": "default",
  "arch": ["armhf", "aarch64", "i386", "amd64"],
  "audio_input": null,
  "audio_output": null,
  "audio": false,
  "auth_api": false,
  "auto_uart": false,
  "auto_update": false,
  "available": false,
  "boot": "auto",
  "boot_config": "auto",
  "build": false,
  "changelog": false,
  "description": "description",
  "detached": false,
  "devices": ["/dev/xy"],
  "devicetree": false,
  "discovery": ["service"],
  "dns": [],
  "docker_api": false,
  "documentation": false,
  "full_access": false,
  "gpio": false,
  "hassio_api": false,
  "hassio_role": "default",
  "homeassistant_api": false,
  "homeassistant": null,
  "host_dbus": false,
  "host_ipc": false,
  "host_network": false,
  "host_pid": false,
  "host_uts": false,
  "hostname": "awesome-addon",
  "icon": false,
  "ingress_entry": null,
  "ingress_panel": true,
  "ingress_port": 1337,
  "ingress_url": null,
  "ingress": false,
  "ip_address": "172.0.0.21",
  "kernel_modules": false,
  "logo": false,
  "long_description": "Long description",
  "machine": ["raspberrypi2", "tinker"],
  "name": "Awesome add-on",
  "network_description": "{}|null",
  "network": {},
  "options": {},
  "privileged": ["NET_ADMIN", "SYS_ADMIN"],
  "protected": false,
  "rating": "1-6",
  "repository": "12345678",
  "schema": {},
  "services_role": ["service:access"],
  "slug": "awesome_addon",
  "stage": "stable",
  "startup": "application",
  "state": "started",
  "stdin": false,
  "system_managed": true,
  "system_managed_config_entry": "abc123",
  "translations": {
    "en": {
      "configuration": {
        "lorem": "ipsum"
      }
    }
  },
  "udev": false,
  "update_available": false,
  "url": null,
  "usb": ["/dev/usb1"],
  "version_latest": "1.0.2",
  "version": "1.0.0",
  "video": false,
  "watchdog": true,
  "webui": "http://[HOST]:1337/xy/zx",
  "signed": false
}
```

post

`/addons/<addon>/install`

🔒

Install an add-on

**Deprecated!** Use [`/store/addons/<addon>/install`](#store) instead.

get

`/addons/<addon>/logo`

🔒

Get the add-on logo

post

`/addons/<addon>/options`

🔒

Set the options for an add-on.

> **tip**
>
> To reset customized network/audio/options, set it `null`.

**Payload:**

| key | type | description |
| --- | --- | --- |
| boot | string | (auto, manual) |
| auto\_update | boolean | `true` if the add-on should auto update |
| network | dictionary | A map of network configuration. |
| options | dictionary | The add-on configuration |
| audio\_output | float or null | The index of the audio output device |
| audio\_input | float or null | The index of the audio input device |
| ingress\_panel | boolean | `true` if ingress\_panel is enabled |
| watchdog | boolean | `true` if watchdog is enabled |

**You need to supply at least one key in the payload.**

**Example payload:**

```
{
  "boot": "manual",
  "auto_update": false,
  "network": {
    "CONTAINER": "1337"
  },
  "options": {
    "awesome": true
  },
  "watchdog": true
}
```

post

`/addons/<addon>/sys_options`

🔒

Change options specific to system managed addons.

This endpoint is only callable by Home Assistant and not by any other client.

**Payload**

| key | type | description |
| --- | --- | --- |
| system\_managed | boolean | `true` if managed by Home Assistant |
| system\_managed\_config\_entry | boolean | ID of config entry managing addon |

**You need to supply at least one key in the payload.**

**Example payload:**

```
{
  "system_managed": true,
  "system_managed_config_entry": "abc123"
}
```

post

`/addons/<addon>/options/validate`

🔒

Run a configuration validation against the current stored add-on configuration or payload.

**Payload:**

Optional the raw add-on options.

**Returned data:**

| key | type | description |
| --- | --- | --- |
| message | string | Include the error message |
| valid | boolean | If config is valid or not |
| pwned | boolean | None |

get

`/addons/<addon>/options/config`

🔒

The Data endpoint to get his own rendered configuration.

post

`/addons/<addon>/rebuild`

🔒

Rebuild the add-on, only supported for local build add-ons.

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| force | boolean | True | Force rebuild of the add-on even if pre-built images are provided |

post

`/addons/<addon>/restart`

🔒

Restart an add-on

post

`/addons/<addon>/security`

🔒

Set the protection mode on an add-on.

This function is not callable by itself and you can not use `self` as the slug here.

**Payload:**

| key | type | description |
| --- | --- | --- |
| protected | boolean | `true` if protection mode is on |

post

`/addons/<addon>/start`

🔒

Start an add-on

get

`/addons/<addon>/stats`

🔒

Returns a [Stats model](/docs/api/supervisor/models#stats) for the add-on.

**Example response:**

```
{
  "cpu_percent": 14.0,
  "memory_usage": 288888,
  "memory_limit": 322222,
  "memory_percent": 32.4,
  "network_tx": 110,
  "network_rx": 902,
  "blk_read": 12,
  "blk_write": 27
}
```

post

`/addons/<addon>/stdin`

🔒

Write data to add-on stdin.

The payload you want to pass into the addon you give the endpoint as the body of the request.

post

`/addons/<addon>/stop`

🔒

Stop an add-on

post

`/addons/<addon>/uninstall`

🔒

Uninstall an add-on

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| remove\_config | boolean | True | Delete addon's config folder (if used) |

post

`/addons/<addon>/update`

🔒

Update an add-on

**Deprecated!** Use [`/store/addons/<addon>/update`](#store) instead.

### Audio

post

`/audio/default/input`

🔒

Set a profile as the default input profile

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| name | string | False | The name of the profile |

post

`/audio/default/output`

🔒

Set a profile as the default output profile

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| name | string | False | The name of the profile |

get

`/audio/info`

🔒

Return information about the audio plugin.

**Returned data:**

| key | type | description |
| --- | --- | --- |
| host | string | The IP address of the plugin |
| version | string | The installed observer version |
| version\_latest | string | The latest published version |
| update\_available | boolean | `true` if an update is available |
| audio | dictionary | An [Audio model](/docs/api/supervisor/models#audio) |

**Example response:**

```
{
  "host": "172.0.0.19",
  "version": "1",
  "latest_version": "2",
  "update_available": true,
  "audio": {
    "card": [
      {
        "name": "Awesome card",
        "index": 1,
        "driver": "Awesome driver",
        "profiles": [
          {
            "name": "Awesome profile",
            "description": "My awesome profile",
            "active": false
          }
        ]
      }
    ],
    "input": [
      {
        "name": "Awesome device",
        "index": 0,
        "description": "My awesome device",
        "volume": 0.3,
        "mute": false,
        "default": false,
        "card": null,
        "applications": [
          {
            "name": "Awesome application",
            "index": 0,
            "stream_index": 0,
            "stream_type": "INPUT",
            "volume": 0.3,
            "mute": false,
            "addon": "awesome_addon"
          }
        ]
      }
    ],
    "output": [
      {
        "name": "Awesome device",
        "index": 0,
        "description": "My awesome device",
        "volume": 0.3,
        "mute": false,
        "default": false,
        "card": 1,
        "applications": [
          {
            "name": "Awesome application",
            "index": 0,
            "stream_index": 0,
            "stream_type": "INPUT",
            "volume": 0.3,
            "mute": false,
            "addon": "awesome_addon"
          }
        ]
      }
    ],
    "application": [
      {
        "name": "Awesome application",
        "index": 0,
        "stream_index": 0,
        "stream_type": "OUTPUT",
        "volume": 0.3,
        "mute": false,
        "addon": "awesome_addon"
      }
    ]
  }
}
```

get

`/audio/logs`

🔒

Get logs for the audio plugin container via the Systemd journal backend.

The endpoint accepts the same headers and provides the same functionality as
`/host/logs`.

get

`/audio/logs/follow`

🔒

Identical to `/audio/logs` except it continuously returns new log entries.

get

`/audio/logs/latest`

🔒

Return all logs of the latest startup of the audio plugin container.

The `Range` header is ignored but the `lines` query parameter can be used.

get

`/audio/logs/boots/<bootid>`

🔒

Get logs for the audio plugin container related to a specific boot.

The `bootid` parameter is interpreted in the same way as in
`/host/logs/boots/<bootid>` and the endpoint otherwise provides the same
functionality as `/host/logs`.

get

`/audio/logs/boots/<bootid>/follow`

🔒

Identical to `/audio/logs/boots/<bootid>` except it continuously returns
new log entries.

post

`/audio/mute/input`

🔒

Mute input devices

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| index | string | False | The index of the device |
| active | boolean | False | `true` if muted |

post

`/audio/mute/input/<application>`

🔒

Mute input for a specific application

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| index | string | False | The index of the device |
| active | boolean | False | `true` if muted |

post

`/audio/mute/output`

🔒

Mute output devices

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| index | string | False | The index of the device |
| active | boolean | False | `true` if muted |

post

`/audio/mute/output/<application>`

🔒

Mute output for a specific application

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| index | string | False | The index of the device |
| active | boolean | False | `true` if muted |

post

`/audio/profile`

🔒

Create an audio profile

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| card | string | False | The name of the audio device |
| name | string | False | The name of the profile |

post

`/audio/reload`

🔒

Reload audio information

post

`/audio/restart`

🔒

Restart the audio plugin

get

`/audio/stats`

🔒

Returns a [Stats model](/docs/api/supervisor/models#stats) for the audio plugin.

**Example response:**

```
{
  "cpu_percent": 14.0,
  "memory_usage": 288888,
  "memory_limit": 322222,
  "memory_percent": 32.4,
  "network_tx": 110,
  "network_rx": 902,
  "blk_read": 12,
  "blk_write": 27
}
```

post

`/audio/update`

🔒

Update the audio plugin

**Payload:**

| key | type | description |
| --- | --- | --- |
| version | string | The version you want to install, default is the latest version |

post

`/audio/volume/input`

🔒

Set the input volume

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| index | string | False | The index of the device |
| volume | float | False | The volume (between `0.0`and `1.0`) |

post

`/audio/volume/input/<application>`

🔒

Set the input volume for a specific application

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| index | string | False | The index of the device |
| volume | float | False | The volume (between `0.0`and `1.0`) |

post

`/audio/volume/output`

🔒

Set the output volume

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| index | string | False | The index of the device |
| volume | float | False | The volume (between `0.0`and `1.0`) |

post

`/audio/volume/output/<application>`

🔒

Set the output volume for a specific application

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| index | string | False | The index of the device |
| volume | float | False | The volume (between `0.0`and `1.0`) |

### Auth

get

`/auth`

🔒

You can do authentication against Home Assistant Core using Basic Authentication.
Use the `X-Supervisor-Token` header to provide the Supervisor authentication token.
See the corresponding POST method to provide JSON or urlencoded credentials.

post

`/auth`

🔒

You can do authentication against Home Assistant Core.
You can POST the data as JSON, as urlencoded (with `application/x-www-form-urlencoded` header) or by using use basic authentication.
For using Basic authentication, you can use the `X-Supervisor-Token` for Supervisor authentication token.

**Payload:**

| key | type | description |
| --- | --- | --- |
| username | string | The username for the user |
| password | string | The password for the user |

post

`/auth/reset`

🔒

Set a new password for a Home Assistant Core user.

**Payload:**

| key | type | description |
| --- | --- | --- |
| username | string | The username for the user |
| password | string | The new password for the user |

delete

`/auth/cache`

🔒

Reset internal authentication cache, this is useful if you have changed the password for a user and need to clear the internal cache.

get

`/auth/list`

🔒

List all users in Home Assistant to help with credentials recovery. Requires an admin level authentication token.

**Payload:**

| key | type | description |
| --- | --- | --- |
| users | list | List of the Home Assistant [users](/docs/api/supervisor/models#user). |

### Backup

get

`/backups`

🔒

Return a list of [Backups](/docs/api/supervisor/models#backup)

**Example response:**

```
{
  "backups": [
    {
      "slug": "skuwe823",
      "date": "2020-09-30T20:25:34.273Z",
      "name": "Awesome backup",
      "type": "partial",
      "size": 44,
      "protected": true,
      "location": "MountedBackups",
      "compressed": true,
      "content": {
        "homeassistant": true,
        "addons": ["awesome_addon"],
        "folders": ["ssl", "media"]
      }
    }
  ]
}
```

get

`/backups/info`

🔒

Return information about backup manager.

**Returned data:**

| key | type | description |
| --- | --- | --- |
| backups | list | A list of [Backups](/docs/api/supervisor/models#backup) |
| days\_until\_stale | int | Number of days until a backup is considered stale |

**Example response:**

```
{
  "backups": [
    {
      "slug": "skuwe823",
      "date": "2020-09-30T20:25:34.273Z",
      "name": "Awesome backup",
      "type": "partial",
      "size": 44,
      "protected": true,
      "compressed": true,
      "location": null,
      "content": {
        "homeassistant": true,
        "addons": ["awesome_addon"],
        "folders": ["ssl", "media"]
      }
    }
  ],
  "days_until_stale": 30
}
```

post

`/backups/new/full`

🔒

Create a full backup.

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| name | string | True | The name you want to give the backup |
| password | string | True | The password you want to give the backup |
| compressed | boolean | True | `false` to create uncompressed backups |
| location | string or null | True | Name of a backup mount or `null` for /backup |
| homeassistant\_exclude\_database | boolean | True | Exclude the Home Assistant database file from backup |
| background | boolean | True | Return `job_id` immediately, do not wait for backup to complete. Clients must check job for status and slug. |

**Example response:**

```
{
  "slug": "skuwe823"
}
```

post

`/backups/new/upload`

🔒

Upload a backup.

**Example response:**

```
{
  "slug": "skuwe823",
  "job_id": "abc123"
}
```

> **note**
>
> Error responses from this API may also include a `job_id` if the message alone cannot accurately describe what happened.
Callers should direct users to review the job or supervisor logs to get an understanding of what occurred.

post

`/backups/new/partial`

🔒

Create a partial backup.

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| name | string | True | The name you want to give the backup |
| password | string | True | The password you want to give the backup |
| homeassistant | boolean | True | Add home assistant core settings to the backup |
| addons | list | True | A list of strings representing add-on slugs |
| folders | list | True | A list of strings representing directories |
| compressed | boolean | True | `false` to create uncompressed backups |
| location | string or null | True | Name of a backup mount or `null` for /backup |
| homeassistant\_exclude\_database | boolean | True | Exclude the Home Assistant database file from backup |
| background | boolean | True | Return `job_id` immediately, do not wait for backup to complete. Clients must check job for status and slug. |

**You need to supply at least one key in the payload.**

**Example response:**

```
{
  "slug": "skuwe823",
  "job_id": "abc123"
}
```

> **note**
>
> Error responses from this API may also include a `job_id` if the message alone cannot accurately describe what happened.
Callers should direct users to review the job or supervisor logs to get an understanding of what occurred.

post

`/backups/options`

🔒

Update options for backup manager, you need to supply at least one of the payload keys to the API call.

**Payload:**

| key | type | description |
| --- | --- | --- |
| days\_until\_stale | int | Set number of days until a backup is considered stale |

**You need to supply at least one key in the payload.**

post

`/backups/reload`

🔒

Reload backup from storage.

post

`/backups/freeze`

🔒

Put Supervisor in a freeze state and prepare Home Assistant and addons for an external backup.

> **note**
>
> This does not take a backup. It prepares Home Assistant and addons for one but the expectation
is that the user is using an external tool to make the backup. Such as the snapshot feature in
KVM or Proxmox. The caller should call `/backups/thaw` when done.

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| timeout | int | True | Seconds before freeze times out and thaw begins automatically (default: 600). |

post

`/backups/thaw`

🔒

End a freeze initiated by `/backups/freeze` and resume normal behavior in Home Assistant and addons.

get

`/backups/<backup>/download`

🔒

Download the backup file with the given slug.

get

`/backups/<backup>/info`

🔒

Returns a [Backup details model](/docs/api/supervisor/models#backup-details) for the add-on.

delete

`/backups/<backup>`

🔒

Removes the backup file with the given slug.

post

`/backups/<backup>/restore/full`

🔒

Does a full restore of the backup with the given slug.

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| password | string | True | The password for the backup if any |
| background | boolean | True | Return `job_id` immediately, do not wait for restore to complete. Clients must check job for status. |

**Example response:**

```
{
  "job_id": "abc123"
}
```

> **note**
>
> Error responses from this API may also include a `job_id` if the message alone cannot accurately describe what happened.
Callers should direct users to review the job or supervisor logs to get an understanding of what occurred.

post

`/backups/<backup>/restore/partial`

🔒

Does a partial restore of the backup with the given slug.

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| homeassistant | boolean | True | `true` if Home Assistant should be restored |
| addons | list | True | A list of add-on slugs that should be restored |
| folders | list | True | A list of directories that should be restored |
| password | string | True | The password for the backup if any |
| background | boolean | True | Return `job_id` immediately, do not wait for restore to complete. Clients must check job for status. |

**You need to supply at least one key in the payload.**

**Example response:**

```
{
  "job_id": "abc123"
}
```

> **note**
>
> Error responses from this API may also include a `job_id` if the message alone cannot accurately describe what happened.
Callers should direct users to review the job or supervisor logs to get an understanding of what occurred.

### CLI

get

`/cli/info`

🔒

Returns information about the CLI plugin

**Returned data:**

| key | type | description |
| --- | --- | --- |
| version | string | The installed cli version |
| version\_latest | string | The latest published version |
| update\_available | boolean | `true` if an update is available |

**Example response:**

```
{
  "version": "1",
  "version_latest": "2",
  "update_available": true
}
```

get

`/cli/stats`

🔒

Returns a [Stats model](/docs/api/supervisor/models#stats) for the CLI plugin.

**Example response:**

```
{
  "cpu_percent": 14.0,
  "memory_usage": 288888,
  "memory_limit": 322222,
  "memory_percent": 32.4,
  "network_tx": 110,
  "network_rx": 902,
  "blk_read": 12,
  "blk_write": 27
}
```

post

`/cli/update`

🔒

Update the CLI plugin

**Payload:**

| key | type | description |
| --- | --- | --- |
| version | string | The version you want to install, default is the latest version |

### Core

get

`/core/api`

🔒

Proxy GET API calls to the Home Assistant API

post

`/core/api`

🔒

Proxy POST API calls to the Home Assistant API

post

`/core/check`

🔒

Run a configuration check

get

`/core/info`

🔒

Returns information about the Home Assistant core

**Returned data:**

| key | type | description |
| --- | --- | --- |
| version | string | The installed core version |
| version\_latest | string | The latest published version in the active channel |
| update\_available | boolean | `true` if an update is available |
| arch | string | The architecture of the host (armhf, aarch64, i386, amd64) |
| machine | string | The machine type that is running the host |
| ip\_address | string | The internal docker IP address to the supervisor |
| image | string | The container image that is running the core |
| boot | boolean | `true` if it should start on boot |
| port | int | The port Home Assistant is running on |
| ssl | boolean | `true` if Home Assistant is using SSL |
| watchdog | boolean | `true` if watchdog is enabled |
| wait\_boot | int | Max time to wait during boot |
| audio\_input | string or null | The description of the audio input device |
| audio\_output | string or null | The description of the audio output device |
| backups\_exclude\_database | boolean | Backups exclude Home Assistant database file by default |
| duplicate\_log\_file | boolean | Home Assistant duplicates logs to a file |

**Example response:**

```
{
  "version": "0.117.0",
  "version_latest": "0.117.0",
  "update_available": true,
  "arch": "arch",
  "machine": "amd64",
  "ip_address": "172.0.0.15",
  "image": "homeassistant/home-assistant",
  "boot": true,
  "port": 8123,
  "ssl": false,
  "watchdog": true,
  "wait_boot": 800,
  "audio_input": "AMCP32",
  "audio_output": "AMCP32"
}
```

get

`/core/logs`

🔒

Get logs for the Home Assistant Core container via the Systemd journal backend.

The endpoint accepts the same headers and provides the same functionality as
`/host/logs`.

get

`/core/logs/follow`

🔒

Identical to `/core/logs` except it continuously returns new log entries.

get

`/core/logs/latest`

🔒

Return all logs of the latest startup of the Home Assistant Core container.

The `Range` header is ignored but the `lines` query parameter can be used.

get

`/core/logs/boots/<bootid>`

🔒

Get logs for the Home Assistant Core container related to a specific boot.

The `bootid` parameter is interpreted in the same way as in
`/host/logs/boots/<bootid>` and the endpoint otherwise provides the same
functionality as `/host/logs`.

get

`/core/logs/boots/<bootid>/follow`

🔒

Identical to `/core/logs/boots/<bootid>` except it continuously returns
new log entries.

post

`/core/options`

🔒

Update options for Home Assistant, you need to supply at least one of the payload keys to the API call.
You need to call `/core/restart` after updating the options.

> **tip**
>
> Passing `image`, `refresh_token`, `audio_input` or `audio_output` with `null` resets the option.

**Payload:**

| key | type | description |
| --- | --- | --- |
| boot | boolean | Start Core on boot |
| image | string or null | Name of custom image |
| port | int | The port that Home Assistant run on |
| ssl | boolean | `true` to enable SSL |
| watchdog | boolean | `true` to enable the watchdog |
| wait\_boot | int | Time to wait for Core to startup |
| refresh\_token | string or null | Token to authenticate with Core |
| audio\_input | string or null | Profile name for audio input |
| audio\_output | string or null | Profile name for audio output |
| backups\_exclude\_database | boolean | `true` to exclude Home Assistant database file from backups |
| duplicate\_log\_file | boolean | `true` to duplicate Home Assistant logs to a file |

**You need to supply at least one key in the payload.**

post

`/core/rebuild`

🔒

Rebuild the Home Assistant core container

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| safe\_mode | boolean | True | Rebuild Core into safe mode |
| force | boolean | True | Force rebuild during a Home Assistant offline db migration |

post

`/core/restart`

🔒

Restart the Home Assistant core container

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| safe\_mode | boolean | True | Restart Core into safe mode |
| force | boolean | True | Force restart during a Home Assistant offline db migration |

post

`/core/start`

🔒

Start the Home Assistant core container

get

`/core/stats`

🔒

Returns a [Stats model](/docs/api/supervisor/models#stats) for the Home Assistant core.

**Example response:**

```
{
  "cpu_percent": 14.0,
  "memory_usage": 288888,
  "memory_limit": 322222,
  "memory_percent": 32.4,
  "network_tx": 110,
  "network_rx": 902,
  "blk_read": 12,
  "blk_write": 27
}
```

post

`/core/stop`

🔒

Stop the Home Assistant core container

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| force | boolean | True | Force stop during a Home Assistant offline db migration |

post

`/core/update`

🔒

Update Home Assistant core

**Payload:**

| key | type | description |
| --- | --- | --- |
| version | string | The version you want to install, default is the latest version |
| backup | boolean | Create a partial backup of core and core configuration before updating, default is false |

get

`/core/websocket`

🔒

Proxy to Home Assistant Core websocket.

### Discovery

get

`/discovery`

🔒

Return information about enabled discoveries.

**Returned data:**

| key | type | description |
| --- | --- | --- |
| discovery | list | A list of [Discovery models](/docs/api/supervisor/models#discovery) |
| services | dictionary | A dictionary of services that contains a list of add-ons that have that service. |

**Example response:**

```
{
  "discovery": [
    {
      "addon": "awesome_addon",
      "service": "awesome.service",
      "uuid": "fh874r-fj9o37yr3-fehsf7o3-fd798",
      "config": {}
    }
  ],
  "services": {
    "awesome": ["awesome_addon"]
  }
}
```

post

`/discovery`

🔒

Create a discovery service

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| service | string | False | The name of the service |
| config | dictionary | False | The configuration of the service |

**Example response:**

```
{
  "uuid": "uuid"
}
```

get

`/discovery/<uuid>`

🔒

Get a [discovery model](/docs/api/supervisor/models#discovery) for a UUID.

delete

`/discovery/<uuid>`

🔒

Delete a specific service.

### DNS

get

`/dns/info`

🔒

Return information about the DNS plugin.

**Returned data:**

| key | type | description |
| --- | --- | --- |
| fallback | bool | Try fallback DNS on failure |
| host | string | The IP address of the plugin |
| llmnr | bool | Can resolve LLMNR hostnames |
| locals | list | A list of DNS servers |
| mdns | bool | Can resolve MulticastDNS hostnames |
| servers | list | A list of DNS servers |
| update\_available | boolean | `true` if an update is available |
| version | string | The installed observer version |
| version\_latest | string | The latest published version |

**Example response:**

```
{
  "host": "127.0.0.18",
  "version": "1",
  "version_latest": "2",
  "update_available": true,
  "servers": ["dns://8.8.8.8"],
  "locals": ["dns://127.0.0.18"],
  "mdns": true,
  "llmnr": false,
  "fallback": true
}
```

get

`/dns/logs`

🔒

Get logs for the DNS plugin container via the Systemd journal backend.

The endpoint accepts the same headers and provides the same functionality as
`/host/logs`.

get

`/dns/logs/follow`

🔒

Identical to `/dns/logs` except it continuously returns new log entries.

get

`/dns/logs/latest`

🔒

Return all logs of the latest startup of the DNS plugin container.

The `Range` header is ignored but the `lines` query parameter can be used.

get

`/dns/logs/boots/<bootid>`

🔒

Get logs for the DNS plugin container related to a specific boot.

The `bootid` parameter is interpreted in the same way as in
`/host/logs/boots/<bootid>` and the endpoint otherwise provides the same
functionality as `/host/logs`.

get

`/dns/logs/boots/<bootid>/follow`

🔒

Identical to `/dns/logs/boots/<bootid>` except it continuously returns
new log entries.

post

`/dns/options`

🔒

Set DNS options

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| fallback | bool | True | Enable/Disable fallback DNS |
| servers | list | True | A list of DNS servers |

**You need to supply at least one key in the payload.**

post

`/dns/reset`

🔒

Reset the DNS configuration.

post

`/dns/restart`

🔒

Restart the DNS plugin

get

`/dns/stats`

🔒

Returns a [Stats model](/docs/api/supervisor/models#stats) for the dns plugin.

**Example response:**

```
{
  "cpu_percent": 14.0,
  "memory_usage": 288888,
  "memory_limit": 322222,
  "memory_percent": 32.4,
  "network_tx": 110,
  "network_rx": 902,
  "blk_read": 12,
  "blk_write": 27
}
```

post

`/dns/update`

🔒

Update the DNS plugin

**Payload:**

| key | type | description |
| --- | --- | --- |
| version | string | The version you want to install, default is the latest version |

### Docker

get

`/docker/info`

🔒

Returns information about the docker instance.

**Returned data:**

| key | type | description |
| --- | --- | --- |
| version | string | The version of the docker engine |
| enable\_ipv6 | bool | Enable/Disable IPv6 for containers |
| storage | string | The storage type |
| logging | string | The logging type |
| registries | dictionary | A dictionary of dictionaries containing `username` and `password` keys for registries. |

**Example response:**

```
{
  "version": "1.0.1",
  "enable_ipv6": true,
  "storage": "overlay2",
  "logging": "journald",
  "registries": {}
}
```

post

`/docker/options`

🔒

Set docker options

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| enable\_ipv6 | bool | True | Enable/Disable IPv6 for containers |

**You need to supply at least one key in the payload.**

get

`/docker/registries`

🔒

Get all configured container registries, this returns a dict with the registry hostname as the key, and a dictionary containing the username configured for that registry.

**Example response:**

```
{
  "registry.example.com": {
    "username": "AwesomeUser"
  }
}
```

post

`/docker/registries`

🔒

Add a new container registry.

**Payload:**

| key | type | description |
| --- | --- | --- |
| hostname | dictionary | A dictionary containing `username` and `password` keys for the registry. |

**Example payload:**

```
{
  "registry.example.com": {
    "username": "AwesomeUser",
    "password": "MySuperStrongPassword!"
  }
}
```

> **note**
>
> To login to the default container registry (Docker Hub), use `hub.docker.com` as the registry.

delete

`/docker/registries/<registry>`

🔒

Delete a registry from the configured container registries.

post

`/docker/migrate-storage-driver`

🔒

Schedule a Docker storage driver migration. The migration will be applied on the next system reboot.

This endpoint allows migrating to either:

* `overlayfs`: The Containerd overlayfs driver
* `overlay2`: The Docker graph overlay2 driver

> **note**
>
> This endpoint requires Home Assistant OS 17.0 or newer. A `404` error will be returned on older versions or non-HAOS installations.

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| storage\_driver | string | False | The target storage driver (`overlayfs` or `overlay2`) |

**Example payload:**

```
{
  "storage_driver": "overlayfs"
}
```

After calling this endpoint, a reboot is required to apply the migration. The response will create a `reboot_required` issue in the resolution center.

### Hardware

get

`/hardware/info`

🔒

Get hardware information.

**Example response:**

```
{
    "devices": [
      {
        "name": "ttyACM0",
        "sysfs": "/sys/devices/usb/00:01",
        "dev_path": "/dev/ttyACM0",
        "by_id": "/dev/serial/by-id/usb-Silicon_Labs-RFUSB_9017F723B061A7C01410CFCF-if00-port1",
        "subsystem": "tty",
        "parent": null,
        "attributes": {
          "MINOR": "5"
        },
        "children": [
          "/sys/devices/soc/platform/00ef"
        ]
      }
    ],
    "drives": [
      {
        "vendor": "Generic",
        "model": "Flash Disk",
        "revision": "8.07",
        "serial": "AABBCCDD",
        "id": "Generic-Flash-Disk-AABBCCDD",
        "size": 8054112256,
        "time_detected": "2023-02-15T21:44:22.504878+00:00",
        "connection_bus": "usb",
        "seat": "seat0",
        "removable": true,
        "ejectable": true,
        "filesystems": [
          {
            "device": "/dev/sda1",
            "id": "by-uuid-1122-1ABA",
            "size": 67108864,
            "name": "",
            "system": false,
            "mount_points": []
          }
        ]
      }
    ]
}
```

**Returned data:**

| key | description |
| --- | --- |
| devices | A list of [Device models](/docs/api/supervisor/models#device) |
| drives | A list of [Drive models](/docs/api/supervisor/models#drive) |

get

`/hardware/audio`

🔒

Get audio devices

**Example response:**

```
{
  "audio": {
    "input": {
      "0,0": "Mic"
    },
    "output": {
      "1,0": "Jack",
      "1,1": "HDMI"
    }
  }
}
```

### Host

get

`/host/info`

🔒

Return information about the host.

**Returned data**

| key | type | description |
| --- | --- | --- |
| agent\_version | string or null | Agent version running on the Host |
| apparmor\_version | string or null | The AppArmor version from host |
| boot\_timestamp | int | The timestamp for the last boot in microseconds |
| broadcast\_llmnr | bool or null | Host is broadcasting its LLMNR hostname |
| broadcast\_mdns | bool or null | Host is broadcasting its MulticastDNS hostname |
| chassis | string or null | The chassis type |
| virtualization | string or null | Virtualization hypervisor in use (if any) |
| cpe | string or null | The local CPE |
| deployment | string or null | The deployment stage of the OS if any |
| disk\_total | float | Total space of the disk in MB |
| disk\_used | float | Used space of the disk in MB |
| disk\_free | float | Free space of the disk in MB |
| features | list | A list of features available for the host |
| hostname | string or null | The hostname of the host |
| kernel | string or null | The kernel version on the host |
| llmnr\_hostname | string or null | The hostname currently exposed on the network via LLMNR for host |
| operating\_system | string | The operating system on the host |
| startup\_time | float | The time in seconds it took for last boot |
| disk\_life\_time | float or null | Percentage of estimated disk lifetime used (0–100). Not all disks provide this information, returns `null` if unavailable. |
| timezone | string | The current timezone of the host. |
| dt\_utc | string | Current UTC date/time of the host in ISO 8601 format. |
| dt\_synchronized | bool | `true` if the host is synchronized with an NTP service. |
| use\_ntp | bool | `true` if the host is using an NTP service for time synchronization. |

**Example response:**

```
{
  "agent_version": "1.2.0",
  "apparmor_version": "2.13.2",
  "chassis": "specific",
  "cpe": "xy",
  "deployment": "stable",
  "disk_total": 32.0,
  "disk_used": 30.0,
  "disk_free": 2.0,
  "features": ["shutdown", "reboot", "hostname", "services", "haos"],
  "hostname": "Awesome host",
  "llmnr_hostname": "Awesome host",
  "kernel": "4.15.7",
  "operating_system": "Home Assistant OS",
  "boot_timestamp": 1234567788,
  "startup_time": 12.345,
  "broadcast_llmnr": true,
  "broadcast_mdns": false,
  "virtualization": "",
  "disk_life_time": 10.0,
  "timezone": "Europe/Brussels",
  "dt_utc": "2025-09-08T12:00:00.000000+00:00",
  "dt_synchronized": true,
  "use_ntp": true
}
```

get

`/host/logs`

🔒

Get systemd Journal logs from the host. Returns log entries in plain text, one
log record per line.

**HTTP Request Headers**

| Header | optional | description |
| --- | --- | --- |
| Accept | true | Type of data (text/plain or text/x-log) |
| Range | true | Range of log entries. The format is `entries=cursor[[:num_skip]:num_entries]` |

**HTTP Query Parameters**

These are a convenience alternative to the headers shown above as query
parameters are easier to use in development and with the Home Assistant proxy.
You should only provide one or the other.

| Query | type | description |
| --- | --- | --- |
| verbose | N/A | If included, uses `text/x-log` as log output type (alternative to `Accept` header) |
| lines | int | Number of lines of output to return (alternative to `Range` header) |
| no\_colors | N/A | If included, ANSI escape codes for terminal coloring will be stripped from the output |

Example query string:

```
?verbose&lines=100&no_colors
```

> **tip**
>
> To get the last log entries the Range request header supports negative values
as `num_skip`. E.g. `Range: entries=:-9:` returns the last 10 entries. Or
`Range: entries=:-200:100` to see 100 entries starting from the one 200 ago.

API returns the last 100 lines by default. Provide a value for `Range` to see
logs further in the past.

The `Accept` header can be set to `text/x-log` to get logs annotated with
extra information, such as the timestamp and Systemd unit name. If no
identifier is specified (i.e. for the host logs containing logs for multiple
identifiers/units), this option is ignored - these logs are always annotated.

get

`/host/logs/follow`

🔒

Identical to `/host/logs` except it continuously returns new log entries.

`/host/logs/identifiers`

🔒

Returns a list of syslog identifiers from the systemd journal that you can use
with `/host/logs/identifiers/<identifier>` and `/host/logs/boots/<bootid>/identifiers/<identifier>`.

get

`/host/logs/identifiers/<identifier>`

🔒

Get systemd Journal logs from the host for entries related to a specific log
identifier. Some examples of useful identifiers here include

* `audit` - If developing an apparmor profile shows you permission issues
* `NetworkManager` - Shows NetworkManager logs when having network issues
* `bluetoothd` - Shows bluetoothd logs when having bluetooth issues

A call to `GET /host/logs/identifiers` will show the complete list of possible
values for `identifier`.

Otherwise it provides the same functionality as `/host/logs`.

get

`/host/logs/identifiers/<identifier>/follow`

🔒

Identical to `/host/logs/identifiers/<identifier>` except it continuously returns
new log entries.

`/host/logs/boots`

🔒

Returns a dictionary of boot IDs for this system that you can use with
`/host/logs/boots/<bootid>` and `/host/logs/boots/<bootid>/identifiers/<identifier>`.

The key for each item in the dictionary is the boot offset. 0 is the current boot,
a negative number denotes how many boots ago that boot was.

get

`/host/logs/boots/<bootid>`

🔒

Get systemd Journal logs from the host for entries related to a specific boot.
Call `GET /host/info/boots` to see the boot IDs. Alternatively you can provide a
boot offset:

* 0 - The current boot
* Negative number - Count backwards from current boot (-1 is previous boot)
* Positive number - Count forward from last known boot (1 is last known boot)

Otherwise it provides the same functionality as `/host/logs`.

get

`/host/logs/boots/<bootid>/follow`

🔒

Identical to `/host/logs/boots/<bootid>` except it continuously returns
new log entries.

get

`/host/logs/boots/<bootid>/identifiers/<identifier>`

🔒

Get systemd Journal logs entries for a specific log identifier and boot.
A combination of `/host/logs/boots/<bootid>` and `/host/logs/identifiers/<identifier>`.

get

`/host/logs/boot/<bootid>/<identifier>/entries/follow`

🔒

Identical to `/host/logs/boots/<bootid>/identifiers/<identifier>` except it continuously
returns new log entries.

post

`/host/options`

🔒

Set host options

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| hostname | string | True | A string that will be used as the new hostname |

**You need to supply at least one key in the payload.**

post

`/host/reboot`

🔒

Reboot the host

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| force | boolean | True | Force reboot during a Home Assistant offline db migration |

post

`/host/reload`

🔒

Reload host information

post

`/host/service/<service>/start`

🔒

Start a service on the host.

post

`/host/service/<service>/stop`

🔒

Stop a service on the host.

post

`/host/service/<service>/reload`

🔒

Reload a service on the host.

get

`/host/services`

🔒

Get information about host services.

**Returned data:**

| key | description |
| --- | --- |
| services | A dictionary of [Host service models](/docs/api/supervisor/models#host-service) |

**Example response:**

```
{
  "services": [
    {
      "name": "awesome.service",
      "description": "Just an awesome service",
      "state": "active"
    }
  ]
}
```

post

`/host/shutdown`

🔒

Shutdown the host

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| force | boolean | True | Force shutdown during a Home Assistant offline db migration |

get

`/host/disks/<disk>/usage`

🔒

Get detailed disk usage information in bytes.

The only supported `disk` for now is "default". It will return usage info for the data disk.

Supports an optional `max_depth` query param. Defaults to 1

**Example response:**

```
{
  "id": "root",
  "label": "Default",
  "total_space": 503312781312,
  "used_space": 430245011456,
  "children": [
    {
      "id": "system",
      "label": "System",
      "used_space": 75660903137
    },
    {
      "id": "addons_data",
      "label": "Addons data",
      "used_space": 42349200762
    },
    {
      "id": "addons_config",
      "label": "Addons configuration",
      "used_space": 5283318814
    },
    {
      "id": "media",
      "label": "Media",
      "used_space": 476680019
    },
    {
      "id": "share",
      "label": "Share",
      "used_space": 37477206419
    },
    {
      "id": "backup",
      "label": "Backup",
      "used_space": 268350699520
    },
    {
      "id": "ssl",
      "label": "SSL",
      "used_space": 202912633
    },
    {
      "id": "homeassistant",
      "label": "Home assistant",
      "used_space": 444090152
    }
  ]
}
```

### Ingress

get

`/ingress/panels`

🔒

**Returned data:**

| key | type | description |
| --- | --- | --- |
| panels | dictionary | dictionary of [Panel models](/docs/api/supervisor/models#panel) |

**Example response:**

```
{
  "panels": {
    "addon_slug": {
      "enable": true,
      "icon": "mdi:awesome-icon",
      "title": "Awesome add-on",
      "admin": true
    }
  }
}
```

post

`/ingress/session`

🔒

Create a new session for access to the ingress service.

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| user\_id | string | True | The ID of the user authenticated for the new session |

**Returned data:**

| key | type | optional | description |
| --- | --- | --- | --- |
| session | string | False | The token for the ingress session |

post

`/ingress/validate_session`

🔒

Validate an ingress session, extending it's validity period.

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| session | string | False | The token for the ingress session |

### Jobs

get

`/jobs/info`

🔒

Returns info on ignored job conditions and currently running or completed jobs

**Returned data:**

| key | type | description |
| --- | --- | --- |
| ignore\_conditions | list | List of job conditions being ignored |
| jobs | list | List of running or completed [Jobs](/docs/api/supervisor/models#job) |

**Example response:**

```
{
  "ignore_conditions": [],
  "jobs": [{
    "name": "backup_manager_full_backup",
    "reference": "a01bc3",
    "uuid": "123456789",
    "progress": 0,
    "stage": "addons",
    "done": false,
    "child_jobs": [],
    "extra": null
  }]
}
```

post

`/jobs/options`

🔒

Set options for job manager

**Payload:**

| key | type | description |
| --- | --- | --- |
| ignore\_conditions | list | List of job conditions to ignore (replaces existing list) |

get

`/jobs/<job_id>`

🔒

Returns info on a currently running or completed job

**Returned data:**

See [Job](/docs/api/supervisor/models#job) model

**Example response:**

```
{
  "name": "backup_manager_full_backup",
  "reference": "a01bc3",
  "uuid": "123456789",
  "progress": 0,
  "stage": "addons",
  "done": false,
  "child_jobs": [],
  "extra": null
}
```

delete

`/jobs/<job_id>`

🔒

Removes a completed job from Supervisor cache if client is no longer interested in it

post

`/jobs/reset`

🔒

Reset job manager to defaults (stops ignoring any ignored job conditions)

### Root

get

`/available_updates`

🔒

Returns information about available updates

**Example response:**

```
{
  "available_updates": [
  {
      "panel_path": "/update-available/core",
      "update_type": "core",
      "version_latest": "321",
    },
    {
      "panel_path": "/update-available/os",
      "update_type": "os",
      "version_latest": "321",
    },
    {
      "panel_path": "/update-available/supervisor",
      "update_type": "supervisor",
      "version_latest": "321",
    },
    {
      "name": "Awesome addon",
      "icon": "/addons/awesome_addon/icon",
      "panel_path": "/update-available/awesome_addon",
      "update_type": "addon",
      "version_latest": "321",
    }
  ]
}
```

**Returned data:**

| key | type | description |
| --- | --- | --- |
| update\_type | string | `addon`, `os`, `core` or `supervisor` |
| name | string | Returns the name (only if the `update_type` is `addon`) |
| icon | string | Returns the path for the icon if any (only if the `update_type` is `addon`) |
| version\_latest | string | Returns the available version |
| panel\_path | string | Returns path where the UI can be loaded |

post

`/reload_updates`

🔒

This reloads information about main components (OS, Supervisor, Core, and
Plug-ins).

post

`/refresh_updates`

🔒

This reloads information about add-on repositories and fetches new version files.
This endpoint is currently discouraged. Use `/reload_updates` or `/store/reload`
instead.

get

`/info`

🔒

Returns a dict with selected keys from other `/*/info` endpoints.

**Returned data:**

| key | type | description |
| --- | --- | --- |
| supervisor | string | The installed version of the supervisor |
| homeassistant | string | The installed version of Home Assistant |
| hassos | string or null | The version of Home Assistant OS or null |
| docker | string | The docker version on the host |
| hostname | string | The hostname on the host |
| operating\_system | string | The operating system on the host |
| features | list | A list ov available features on the host |
| machine | string | The machine type |
| machine\_id | string or null | The machine ID of the underlying operating system |
| arch | string | The architecture on the host |
| supported\_arch | list | A list of supported host architectures |
| supported | boolean | `true` if the environment is supported |
| channel | string | The active channel (stable, beta, dev) |
| logging | string | The active log level (debug, info, warning, error, critical) |
| state | string | The core state of the Supervisor. |
| timezone | string | The current timezone |

**Example response:**

```
{
  "supervisor": "300",
  "homeassistant": "0.117.0",
  "hassos": "5.0",
  "docker": "24.17.2",
  "hostname": "Awesome Hostname",
  "operating_system": "Home Assistant OS",
  "features": ["shutdown", "reboot", "hostname", "services", "hassos"],
  "machine": "ova",
  "arch": "amd64",
  "supported_arch": ["amd64"],
  "supported": true,
  "channel": "stable",
  "logging": "info",
  "state": "running",
  "timezone": "Europe/Brussels"
}
```

### Mounts

get

`/mounts`

🔒

Returns information about mounts configured in Supervisor

**Returned data:**

| key | type | description |
| --- | --- | --- |
| mounts | list | A list of [Mounts](/docs/api/supervisor/models#mount) |
| default\_backup\_mount | string or null | Name of a backup mount or `null` for /backup |

**Example response:**

```
{
  "default_backup_mount": "my_share",
  "mounts": [
    {
      "name": "my_share",
      "usage": "media",
      "type": "cifs",
      "server": "server.local",
      "share": "media",
      "state": "active",
      "read_only": false
    }
  ]
}
```

post

`/mounts/options`

🔒

Set mount manager options

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| default\_backup\_mount | string or null | True | Name of a backup mount or `null` for /backup |

**You need to supply at least one key in the payload.**

post

`/mounts`

🔒

Add a new mount in Supervisor and mount it

**Payload:**

Accepts a [Mount](/docs/api/supervisor/models#mount)

Value in `name` must be unique and can only consist of letters, numbers and underscores.

**Example payload:**

```
{
  "name": "my_share",
  "usage": "media",
  "type": "cifs",
  "server": "server.local",
  "share": "media",
  "username": "admin",
  "password": "password",
  "read_only": false
}
```

put

`/mounts/<name>`

🔒

Update an existing mount in Supervisor and remount it

**Payload:**

Accepts a [Mount](/docs/api/supervisor/models#mount).

The `name` field should be omitted. If included the value must match the existing
name, it cannot be changed. Delete and re-add the mount to change the name.

**Example payload:**

```
{
  "usage": "media",
  "type": "nfs",
  "server": "server.local",
  "path": "/media/camera",
  "read_only": true
}
```

delete

`/mounts/<name>`

🔒

Unmount and delete an existing mount from Supervisor.

post

`/mounts/<name>/reload`

🔒

Unmount and remount an existing mount in Supervisor using the same configuration.

### Multicast

get

`/multicast/info`

🔒

Returns information about the multicast plugin

**Returned data:**

| key | type | description |
| --- | --- | --- |
| version | string | The installed multicast version |
| version\_latest | string | The latest published version |
| update\_available | boolean | `true` if an update is available |

**Example response:**

```
{
  "version": "1",
  "version_latest": "2",
  "update_available": true
}
```

get

`/multicast/logs`

🔒

Get logs for the multicast plugin via the Systemd journal backend.

The endpoint accepts the same headers and provides the same functionality as
`/host/logs`.

get

`/multicast/logs/follow`

🔒

Identical to `/multicast/logs` except it continuously returns new log entries.

get

`/multicast/logs/latest`

🔒

Return all logs of the latest startup of the multicast plugin container.

The `Range` header is ignored but the `lines` query parameter can be used.

get

`/multicast/logs/boots/<bootid>`

🔒

Get logs for the multicast plugin related to a specific boot.

The `bootid` parameter is interpreted in the same way as in
`/host/logs/boots/<bootid>` and the endpoint otherwise provides the same
functionality as `/host/logs`.

get

`/multicast/logs/boots/<bootid>/follow`

🔒

Identical to `/multicast/logs/boots/<bootid>` except it continuously returns
new log entries.

post

`/multicast/restart`

🔒

Restart the multicast plugin.

get

`/multicast/stats`

🔒

Returns a [Stats model](/docs/api/supervisor/models#stats) for the multicast plugin.

**Example response:**

```
{
  "cpu_percent": 14.0,
  "memory_usage": 288888,
  "memory_limit": 322222,
  "memory_percent": 32.4,
  "network_tx": 110,
  "network_rx": 902,
  "blk_read": 12,
  "blk_write": 27
}
```

post

`/multicast/update`

🔒

Update the multicast plugin

**Payload:**

| key | type | description |
| --- | --- | --- |
| version | string | The version you want to install, default is the latest version |

### Network

get

`/network/info`

🔒

Get network information.

**Returned data:**

| key | description |
| --- | --- |
| interfaces | A list of [Network interface models](/docs/api/supervisor/models#network-interface) |
| docker | Information about the internal docker network |
| host\_internet | Boolean to indicate if the host can reach the internet. |
| supervisor\_internet | Boolean to indicate if the Supervisor can reach the internet. |

**Example response:**

```
{
  "interfaces": [
    {
      "interface": "eth0",
      "type": "ethernet",
      "primary": true,
      "enabled": true,
      "connected": true,
      "ipv4": {
        "method": "static",
        "ip_address": "192.168.1.100/24",
        "gateway": "192.168.1.1",
        "nameservers": ["192.168.1.1"],
      },
      "ipv6": null,
      "wifi": null,
      "vlan": null,
    }
  ],
  "docker": {
    "interface": "hassio",
    "address": "172.30.32.0/23",
    "gateway": "172.30.32.1",
    "dns": "172.30.32.3"
  },
  "host_internet": true,
  "supervisor_internet": true
}
```

get

`/network/interface/<interface>/info`

🔒

Returns a [Network interface model](/docs/api/supervisor/models#network-interface) for a specific network interface.

post

`/network/reload`

🔒

Update all Network interface data.

post

`/network/interface/<interface>/update`

🔒

Update the settings for a network interface.

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| enabled | bool | True | Enable/Disable an ethernet interface / VLAN got removed with disabled |
| ipv6 | dict | True | A struct with ipv6 interface settings |
| ipv4 | dict | True | A struct with ipv4 interface settings |
| wifi | dict | True | A struct with Wireless connection settings |

**ipv6:**

| key | type | optional | description |
| --- | --- | --- | --- |
| method | string | True | Set IP configuration method can be `auto` for DHCP or Router Advertisements, `static` or `disabled` |
| addr\_gen\_mode | string | True | Address generation mode can be `eui64`, `stable-privacy`, `default-or-eui64` or `default` |
| ip6\_privacy | string | True | Privacy extensions options are `disabled`, `enabled-prefer-public`, `enabled` or `default` |
| address | list | True | The new IP address for the interface in the ::/XX format as list |
| nameservers | list | True | List of DNS servers to use |
| gateway | string | True | The gateway the interface should use |

**ipv4:**

| key | type | optional | description |
| --- | --- | --- | --- |
| method | string | True | Set IP configuration method can be `auto` for DHCP, `static` or `disabled` |
| address | list | True | The new IP address for the interface in the X.X.X.X/XX format as list |
| nameservers | list | True | List of DNS servers to use |
| gateway | string | True | The gateway the interface should use |

**wifi:**

| key | type | optional | description |
| --- | --- | --- | --- |
| mode | string | True | Set the mode `infrastructure` (default), `mesh`, `adhoc` or `ap` |
| auth | string | True | Set the auth mode: `open` (default), `web`, `wpa-psk` |
| ssid | string | True | Set the SSID for connect into |
| psk | string | True | The shared key which is used with `web` or `wpa-psk` |

get

`/network/interface/<interface>/accesspoints`

🔒

Return a list of available [Access Points](/docs/api/supervisor/models#access-points) on this Wireless interface.

**This function only works with Wireless interfaces!**

**Returned data:**

| key | description |
| --- | --- |
| accesspoints | A list of [Access Points](/docs/api/supervisor/models#access-points) |

**Example response:**

```
{
  "accesspoints": [
    {
      "mode": "infrastructure",
      "ssid": "MY_TestWifi",
      "mac": "00:00:00:00",
      "frequency": 24675,
      "signal": 90
    }
  ]
}
```

post

`/network/interface/<interface>/vlan/<id>`

🔒

Create a new VLAN *id* on this network interface.

**This function only works with ethernet interfaces!**

**Payload:**

| key | type | optional | description |
| --- | --- | --- | --- |
| ipv6 | dict | True | A struct with ipv6 interface settings |
| ipv4 | dict | True | A struct with ipv4 interface settings |

### Observer

get

`/observer/info`

🔒

Returns information about the observer plugin

**Returned data:**

| key | type | description |
| --- | --- | --- |
| host | string | The IP address of the plugin |
| version | string | The installed observer version |
| version\_latest | string | The latest published version |
| update\_available | boolean | `true` if an update is available |

**Example response:**

```
{
  "host": "172.0.0.17",
  "version": "1",
  "version_latest": "2",
  "update_available": true
}
```

get

`/observer/stats`

🔒

Returns a [Stats model](/docs/api/supervisor/models#stats) for the observer plugin.

**Example response:**

```
{
  "cpu_percent": 14.0,
  "memory_usage": 288888,
  "memory_limit": 322222,
  "memory_percent": 32.4,
  "network_tx": 110,
  "network_rx": 902,
  "blk_read": 12,
  "blk_write": 27
}
```

post

`/observer/update`

🔒

Update the observer plugin

**Payload:**

| key | type | description |
| --- | --- | --- |
| version | string | The version you want to install, default is the latest version |

### OS

post

`/os/config/sync`

🔒

Load host configurations from a USB stick.

get

`/os/info`

🔒

Returns information about the OS.

**Returned data:**

| key | type | description |
| --- | --- | --- |
| version | string | The current version of the OS |
| version\_latest | string | The latest published version of the OS in the active channel |
| update\_available | boolean | `true` if an update is available |
| board | string | The name of the board |
| boot | string | Which slot that are in use |
| data\_disk | string | Device which is used for holding OS data persistent |
| boot\_slots | dict | Dictionary of [boot slots](/docs/api/supervisor/models#boot-slot) keyed by name |

**Example response:**

```
{
  "version": "4.3",
  "version_latest": "5.0",
  "update_available": true,
  "board": "ova",
  "boot": "slot1",
  "data_disk": "BJTD4R-0x123456789",
  "boot_slots": {
    "A": {
      "state": "inactive",
      "status": "good",
      "version": "10.1"
    },
    "B": {
      "state": "active",
      "status": "good",
      "version": "10.2"
    }
  }
}
```

post

`/os/update`

🔒

Update Home Assistant OS

**Payload:**

| key | type | description |
| --- | --- | --- |
| version | string | The version you want to install, default is the latest version |

post

`/os/boot-slot`

🔒

Change the active boot slot, **This will also reboot the device!**

**Payload:**

| key | type | description |
| --- | --- | --- |
| boot\_slot | string | Boot slot to change to. See options in `boot_slots` from `/os/info` API. |

get

`/os/config/swap`

🔒

Get current HAOS swap configuration. Unavailable on Supervised.

**Returned data:**

| key | type | description |
| --- | --- | --- |
| swap\_size | string | Current swap size. |
| swappiness | int | Current kernel swappiness value. |

**Example response:**

```
{
  "swap_size": "2G",
  "swappiness": 1
}
```

post

`/os/config/swap`

🔒

Set HAOS swap configuration. Unavailable on Supervised.

**Payload:**

| key | type | description |
| --- | --- | --- |
| swap\_size | string | New swap siz as number with optional units (K/M/G). Anything lower than 40K disables swap. |
| swappiness | int | New swappiness value (0-100). |

get

`/os/datadisk/list`

🔒

Returns possible targets for the new data partition.

**Returned data:**

| key | type | description |
| --- | --- | --- |
| devices | list | List of IDs of possible data disk targets |
| disks | list | List of [disks](/docs/api/supervisor/models#disk) which are possible data disk targets |

**Example response:**

```
{
  "devices": [
    "Generic-Flash-Disk-123ABC456",
    "SSK-SSK-Storage-ABC123DEF"
  ],
  "disks": [
    {
      "name": "Generic Flash Disk (123ABC456)",
      "vendor": "Generic",
      "model": "Flash Disk",
      "serial": "123ABC456",
      "size": 8054112256,
      "id": "Generic-Flash-Disk-123ABC456",
      "dev_path": "/dev/sda"
    },
    {
      "name": "SSK SSK Storage (ABC123DEF)",
      "vendor": "SSK",
      "model": "SSK Storage",
      "serial": "ABC123DEF",
      "size": 250059350016,
      "id": "SSK-SSK-Storage-ABC123DEF",
      "dev_path": "/dev/sdb"
    }
  ]
}
```

post

`/os/datadisk/move`

🔒

Move datadisk to a new location, **This will also reboot the device!**

**Payload:**

| key | type | description |
| --- | --- | --- |
| device | string | ID of the disk device which should be used as the target for the data migration |

post

`/os/datadisk/wipe`

🔒

Wipe the datadisk including all user data and settings, **This will also reboot the device!** This API requires an admin token

This API will wipe all config/settings for addons, Home Assistant and the Operating
System and any locally stored data in config, backups, media, etc. The machine will
reboot during this.

After the reboot completes the latest stable version of Home Assistant and Supervisor
will be downloaded. Once the process is complete the user will see onboarding, like
during initial setup.

This wipe also includes network settings. So after the reboot the user may need to
reconfigure those in order to access Home Assistant again.

The operating system version as well as its boot configuration will be preserved.

get

`/os/boards/{board}`

🔒

Returns information about your board if it has features or settings
that can be modified from Home Assistant. The value for `board`
is the value in the `board` field returned by `/os/info`.

Boards with such options are documented below.

get

`/os/boards/yellow`

🔒

If running on a yellow board, returns current values for its settings.

**Returned data:**

| key | type | description |
| --- | --- | --- |
| disk\_led | boolean | Is the disk LED enabled |
| heartbeat\_led | boolean | Is the heartbeat LED enabled |
| power\_led | boolean | Is the power LED enabled |

**Example response:**

```
{
  "disk_led": true,
  "heartbeat_led": true,
  "power_led": false
}
```

post

`/os/boards/yellow`

🔒

If running on a yellow board, changes one or more of its settings.

**Payload:**

| key | type | description |
| --- | --- | --- |
| disk\_led | boolean | Enable/disable the disk LED |
| heartbeat\_led | boolean | Enable/disable the heartbeat LED |
| power\_led | boolean | Enable/disable the power LED |

get

`/os/boards/green`

🔒

If running on a green board, returns current values for its settings.

**Returned data:**

| key | type | description |
| --- | --- | --- |
| activity\_led | boolean | Is the green activity LED enabled |
| power\_led | boolean | Is the white power LED enabled |
| system\_health\_led | boolean | Is the yellow system health LED enabled |

**Example response:**

```
{
  "activity_led": true,
  "power_led": true,
  "system_health_led": false
}
```

post

`/os/boards/green`

🔒

If running on a green board, changes one or more of its settings.

**Payload:**

| key | type | description |
| --- | --- | --- |
| activity\_led | boolean | Enable/disable the green activity LED |
| power\_led | boolean | Enable/disable the white power LED |
| system\_health\_led | boolean | Enable/disable the yellow system health LED |

### Resolution

get

`/resolution/info`

🔒

**Returned data:**

| key | type | description |
| --- | --- | --- |
| unsupported | list | A list of reasons why an installation is marked as unsupported (container, dbus, docker\_configuration, docker\_version, lxc, network\_manager, os, privileged, systemd) |
| unhealthy | list | A list of reasons why an installation is marked as unhealthy (docker, supervisor, privileged, setup) |
| issues | list | A list of [Issue models](/docs/api/supervisor/models#issues) |
| suggestions | list | A list of [Suggestion models](/docs/api/supervisor/models#suggestion) actions |
| checks | list | A list of [Check models](/docs/api/supervisor/models#check) |

**Example response:**

```
{
  "unsupported": ["os"],
  "unhealthy": ["docker"],
  "issues": [
    {
      "uuid": "A89924620F9A11EBBDC3C403FC2CA371",
      "type": "free_space",
      "context": "system",
      "reference": null
     }
  ],
  "suggestions": [
    {
      "uuid": "B9923620C9A11EBBDC3C403FC2CA371",
      "type": "clear_backups",
      "context": "system",
      "reference": null,
      "auto": false
    }
  ],
  "checks": [
    {
      "slug": "free_space",
      "enabled": true
    }
  ]
}
```

post

`/resolution/suggestion/<suggestion>`

🔒

Apply a suggested action

delete

`/resolution/suggestion/<suggestion>`

🔒

Dismiss a suggested action

get

`/resolution/issue/<issue>/suggestions`

🔒

Get suggestions that would fix an issue if applied.

**Returned data:**

| key | type | description |
| --- | --- | --- |
| suggestions | list | A list of [Suggestion models](/docs/api/supervisor/models#suggestion) actions |

**Example response:**

```
{
  "suggestions": [
    {
      "uuid": "B9923620C9A11EBBDC3C403FC2CA371",
      "type": "clear_backups",
      "context": "system",
      "reference": null,
      "auto": false
    }
  ]
}
```

delete

`/resolution/issue/<issue>`

🔒

Dismiss an issue

post

`/resolution/healthcheck`

🔒

Execute a healthcheck and autofix & notification.

post

`/resolution/check/<check>/options`

🔒

Set options for this check.

**Payload:**

| key | type | description |
| --- | --- | --- |
| enabled | bool | If the check should be enabled or disabled |

post

`/resolution/check/<check>/run`

🔒

Execute a specific check right now.

### Service

get

`/services`

🔒

**Returned data:**

| key | type | description |
| --- | --- | --- |
| services | dictionary | dictionary of [Service models](/docs/api/supervisor/models#service) |

**Example response:**

```
{
  "services": [
    {
      "slug": "name",
      "available": true,
      "providers": ["awesome_addon"]
    }
  ]
}
```

get

`/services/mqtt`

🔒

**Returned data:**

| key | type | description |
| --- | --- | --- |
| addon | string | The add-on slug |
| host | string | The IP of the addon running the service |
| port | string | The port the service is running on |
| ssl | boolean | `true` if SSL is in use |
| username | string | The username for the service |
| password | string | The password for the service |
| protocol | string | The MQTT protocol |

**Example response:**

```
{
  "addon": "awesome_mqtt",
  "host": "172.0.0.17",
  "port": "8883",
  "ssl": true,
  "username": "awesome_user",
  "password": "strong_password",
  "protocol": "3.1.1"
}
```

post

`/services/mqtt`

🔒

Create a service definition

**Payload:**

| key | type | description |
| --- | --- | --- |
| host | string | The IP of the addon running the service |
| port | string | The port the service is running on |
| ssl | boolean | `true` if SSL is in use |
| username | string | The username for the service |
| password | string | The password for the service |
| protocol | string | The MQTT protocol |

delete

`/services/mqtt`

🔒

Deletes the service definitions

get

`/services/mysql`

🔒

**Returned data:**

| key | type | description |
| --- | --- | --- |
| addon | string | The add-on slug |
| host | string | The IP of the addon running the service |
| port | string | The port the service is running on |
| ssl | boolean | `true` if SSL is in use |
| username | string | The username for the service |
| password | string | The password for the service |
| protocol | string | The MQTT protocol |

**Example response:**

```
{
  "addon": "awesome_mysql",
  "host": "172.0.0.17",
  "port": "8883",
  "username": "awesome_user",
  "password": "strong_password"
}
```

post

`/services/mysql`

🔒

Create a service definition

**Payload:**

| key | type | description |
| --- | --- | --- |
| host | string | The IP of the addon running the service |
| port | string | The port the service is running on |
| username | string | The username for the service |
| password | string | The password for the service |

delete

`/services/mysql`

🔒

Deletes the service definitions

### Store

get

`/store`

🔒

Returns add-on store information.

**Example response:**

```
{ "addons":
  [
    {
      "name": "Awesome add-on",
      "slug": "7kshd7_awesome",
      "description": "Awesome description",
      "repository": "https://example.com/addons",
      "version": "1.0.0",
      "installed": "1.0.0",
      "icon": false,
      "logo": true,
      "state": "started"
    }
  ],
  "repositories": [
    {
      "slug": "awesom_repository",
      "name": "Awesome Repository",
      "source": "https://example.com/addons",
      "url": "https://example.com/addons",
      "maintainer": "Awesome Maintainer"
    }
  ]
}
```

get

`/store/addons`

🔒

Returns a list of store add-ons

**Example response:**

```
[
  {
    "name": "Awesome add-on",
    "slug": "7kshd7_awesome",
    "description": "Awesome description",
    "repository": "https://example.com/addons",
    "version": "1.0.0",
    "installed": "1.0.0",
    "icon": false,
    "logo": true,
    "state": "started"
  }
]
```

get

`/store/addons/<addon>`

🔒

Returns information about a store add-on

**Example response:**

```
{
  "advanced": false,
  "apparmor": "default",
  "arch": ["armhf", "aarch64", "i386", "amd64"],
  "auth_api": true,
  "available": true,
  "build": false,
  "description": "Awesome description",
  "detached": false,
  "docker_api": false,
  "documentation": true,
  "full_access": true,
  "hassio_api": false,
  "hassio_role": "manager",
  "homeassistant_api": true,
  "homeassistant": "2021.2.0b0",
  "host_network": false,
  "host_pid": false,
  "icon": false,
  "ingress": true,
  "installed": false,
  "logo": true,
  "long_description": "lorem ipsum",
  "name": "Awesome add-on",
  "rating": 5,
  "repository": "core",
  "signed": false,
  "slug": "7kshd7_awesome",
  "stage": "stable",
  "update_available": false,
  "url": "https://example.com/addons/tree/main/awesome_addon",
  "version_latest": "1.0.0",
  "version": "1.0.0"
}
```

post

`/store/addons/<addon>/install`

🔒

Install an add-on from the store.

**Payload:**

| key | type | description |
| --- | --- | --- |
| background | boolean | Return `job_id` immediately, do not wait for install to complete. Clients must check job for status |

post

`/store/addons/<addon>/update`

🔒

Update an add-on from the store.

**Payload:**

| key | type | description |
| --- | --- | --- |
| backup | boolean | Create a partial backup of the add-on, default is false |
| background | boolean | Return `job_id` immediately, do not wait for update to complete. Clients must check job for status |

get

`/store/addons/<addon>/changelog`

🔒

Get the changelog for an add-on.

get

`/store/addons/<addon>/documentation`

🔒

Get the documentation for an add-on.

get

`/store/addons/<addon>/icon`

🔒

Get the add-on icon

get

`/store/addons/<addon>/logo`

🔒

Get the add-on logo

get

`/store/addons/<addon>/availability`

🔒

Returns 200 success status if the latest version of the add-on is able to be
installed on the current system. Returns a 400 error status if it is not with a
message explaining why.

post

`/store/reload`

🔒

Reloads the information stored about add-ons.

get

`/store/repositories`

🔒

Returns a list of store repositories

**Example response:**

```
[
  {
    "slug": "awesom_repository",
    "name": "Awesome Repository",
    "source": "https://example.com/addons",
    "url": "https://example.com/addons",
    "maintainer": "Awesome Maintainer"
  }
]
```

post

`/store/repositories`

🔒

Add an addon repository to the store

**Payload:**

| key | type | description |
| --- | --- | --- |
| repository | string | URL of the addon repository to add to the store. |

**Example payload:**

```
{
  "repository": "https://example.com/addons"
}
```

get

`/store/repositories/<repository>`

🔒

Returns information about a store repository

**Example response:**

```
{
  "slug": "awesom_repository",
  "name": "Awesome Repository",
  "source": "https://example.com/addons",
  "url": "https://example.com/addons",
  "maintainer": "Awesome Maintainer"
}
```

delete

`/store/repositories/<repository>`

🔒

Remove an unused addon repository from the store.

### Security

get

`/security/info`

🔒

Returns information about the security features

**Returned data:**

| key | type | description |
| --- | --- | --- |
| content\_trust | bool | If content-trust is enabled or disabled on the backend |
| pwned | bool | If pwned check is enabled or disabled on the backend |
| force\_security | bool | If force-security is enabled or disabled on the backend |

**Example response:**

```
{
  "content_trust": true,
  "pwned": true,
  "force_security": false,
}
```

post

`/security/options`

🔒

**Payload:**

| key | type | description |
| --- | --- | --- |
| content\_trust | bool | Disable/Enable content-trust |
| pwned | bool | Disable/Enable pwned |
| force\_security | bool | Disable/Enable force-security |

post

`/security/integrity`

🔒

Run a full platform integrity check.

**Returned data:**

| key | type | description |
| --- | --- | --- |
| supervisor | str | `pass`, `error`, `failed`, `untested` |
| core | str | `pass`, `error`, `failed`, `untested` |
| plugins | dict | A dictionary with key per plugin as `pass`, `error`, `failed`, `untested` |
| addons | dict | A dictionary with key per addon as `pass`, `error`, `failed`, `untested` |

**Example response:**

```
{
  "supervisor": "pass",
  "core": "pass",
  "plugins": {
    "audio": "pass",
    "cli": "pass"
  },
  "addons": {
    "core_ssh": "untested",
    "xj3493_test": "pass"
  }
}
```

### Supervisor

get

`/supervisor/info`

🔒

Returns information about the supervisor

**Returned data:**

| key | type | description |
| --- | --- | --- |
| version | string | The installed supervisor version |
| version\_latest | string | The latest published version in the active channel |
| update\_available | boolean | `true` if an update is available |
| arch | string | The architecture of the host (armhf, aarch64, i386, amd64) |
| channel | string | The active channel (stable, beta, dev) |
| timezone | string | The current timezone |
| healthy | bool | The supervisor is in a healthy state |
| supported | bool | The environment is supported |
| logging | string | The current log level (debug, info, warning, error, critical) |
| ip\_address | string | The internal docker IP address to the supervisor |
| wait\_boot | int | Max time to wait during boot |
| debug | bool | Debug is active |
| debug\_block | bool | `true` if debug block is enabled |
| diagnostics | bool or null | Sending diagnostics is enabled |
| addons\_repositories | list | A list of add-on repository URL's as strings |
| auto\_update | bool | Is auto update enabled for supervisor |
| detect\_blocking\_io | bool | Supervisor raises exceptions for blocking I/O in event loop |

**Example response:**

```
{
  "version": "246",
  "version_latest": "version_latest",
  "update_available": true,
  "arch": "amd64",
  "channel": "dev",
  "timezone": "TIMEZONE",
  "healthy": true,
  "supported": false,
  "logging": "debug",
  "ip_address": "172.0.0.2",
  "wait_boot": 800,
  "debug": false,
  "debug_block": false,
  "diagnostics": null,
  "addons_repositories": ["https://example.com/addons"],
  "auto_update": true,
  "detect_blocking_io": false
}
```

get

`/supervisor/logs`

🔒

Get logs for the Supervisor container via the Systemd journal backend. If the
Systemd journal gateway fails to provide the logs, raw Docker container logs are
returned as the fallback.

The endpoint accepts the same headers and provides the same functionality as
`/host/logs`.

get

`/supervisor/logs/follow`

🔒

Identical to `/supervisor/logs` except it continuously returns new log entries.

get

`/supervisor/logs/latest`

🔒

Return all logs of the latest startup of the Supervisor container.

The `Range` header is ignored but the `lines` query parameter can be used.

get

`/supervisor/logs/boots/<bootid>`

🔒

Get logs for the Supervisor container related to a specific boot.

The `bootid` parameter is interpreted in the same way as in
`/host/logs/boots/<bootid>` and the endpoint otherwise provides the same
functionality as `/host/logs`.

get

`/supervisor/logs/boots/<bootid>/follow`

🔒

Identical to `/supervisor/logs/boots/<bootid>` except it continuously returns
new log entries.

post

`/supervisor/options`

🔒

Update options for the supervisor, you need to supply at least one of the payload keys to the API call.
You need to call `/supervisor/reload` after updating the options.

**Payload:**

| key | type | description |
| --- | --- | --- |
| channel | string | Set the active channel (stable, beta, dev) |
| timezone | string | Set the timezone |
| wait\_boot | int | Set the time to wait for boot |
| debug | bool | Enable debug |
| debug\_block | bool | Enable debug block |
| logging | string | Set logging level |
| addons\_repositories | list | Set a list of URL's as strings for add-on repositories |
| auto\_update | bool | Enable/disable auto update for supervisor |
| detect\_blocking\_io | string | Enable blocking I/O in event loop detection. Valid values are `on`, `off` and `on_at_startup`. |

get

`/supervisor/ping`

🔓

Ping the supervisor to check if it can return a response.

post

`/supervisor/reload`

🔒

Reload parts of the supervisor, this enable new options, and check for updates.

post

`/supervisor/restart`

🔒

Restart the supervisor, can help to get the supervisor healthy again.

post

`/supervisor/repair`

🔒

Repair docker overlay issues, and lost images.

get

`/supervisor/stats`

🔒

Returns a [Stats model](/docs/api/supervisor/models#stats) for the supervisor.

**Example response:**

```
{
  "cpu_percent": 14.0,
  "memory_usage": 288888,
  "memory_limit": 322222,
  "memory_percent": 32.4,
  "network_tx": 110,
  "network_rx": 902,
  "blk_read": 12,
  "blk_write": 27
}
```

post

`/supervisor/update`

🔒

Update the supervisor

**Payload:**

| key | type | description |
| --- | --- | --- |
| version | string | The version to install. Defaults to the latest version. Development only: Only works in the Supervisor development environment. |

### Placeholders

Some of the endpoints uses placeholders indicated with `<...>` in the endpoint URL.

| placeholder | description |
| --- | --- |
| addon | The slug for the addon, to get the slug you can call `/addons`, to call endpoints for the add-on calling the endpoints you can use `self`as the slug. |
| application | The name of an application, call `/audio/info` to get the correct name |
| backup | A valid backup slug, example `skuwe823`, to get the slug you can call `/backups` |
| bootid | An id or offset of a particular boot, used to filter logs. Call `/host/logs/boots` to get a list of boot ids or see `/host/logs/boots/<bootid>` to understand boot offsets |
| check | The slug of a system check in Supervisor's resolution manager. Call `/resolution/info` for a list of options from the `checks` field |
| disk | Identifier of a disk attached to host or `default`. See `/host/disks/<disk>/usage` for more details |
| id | Numeric id of a vlan on a particular interface. See `/network/interface/<interface>/vlan/<id>` for details |
| identifier | A syslog identifier used to filter logs. Call `/host/logs/identifiers` to get a list of options. See `/host/logs/identifiers/<identifier>` for some common examples |
| interface | A valid interface name, example `eth0`, to get the interface name you can call `/network/info`. You can use `default` to get the primary interface |
| issue | The UUID of an issue with the system identified by Supervisor. Call `/resolution/info` for a list of options from the `issues` field |
| job\_id | The UUID of a currently running or completed Supervisor job |
| name | Name of a mount added to Supervisor. Call `/mounts` to get a list of options from `mounts` field |
| registry | A registry hostname defined in the container registry configuration, to get the hostname you can call `/docker/registries` |
| repository | The slug of an addon repository added to Supervisor. Call `/store` for a list of options from the `repositories` field |
| service | The service name for a service on the host. |
| suggestion | The UUID of a suggestion for a system issue identified by Supervisor. Call `/resolution/info` for a list of options from the `suggestions` field |
| uuid | The UUID of a discovery service, to get the UUID you can call `/discovery` |