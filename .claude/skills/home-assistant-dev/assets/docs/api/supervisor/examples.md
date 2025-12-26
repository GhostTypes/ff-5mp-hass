# Source: https://developers.home-assistant.io/docs/api/supervisor/examples

Examples on how to interface against the supervisor API.

## Get network information with cURL

```
curl -sSL -H "Authorization: Bearer $SUPERVISOR_TOKEN" http://supervisor/network/info
```

**response:**

```
{
  "result": "ok",
  "data": {
    "interfaces": {
      "eth0": {
        "ip_address": "192.168.1.100/24",
        "gateway": "192.168.1.1",
        "id": "Wired connection 1",
        "type": "802-3-ethernet",
        "nameservers": ["192.168.1.1"],
        "method": "static",
        "primary": true
      }
    }
  }
}
```

## Ping the supervisor

```
curl -sSL http://supervisor/supervisor/ping
```

**response:**

```
{
  "result": "ok",
  "data": {}
}
```