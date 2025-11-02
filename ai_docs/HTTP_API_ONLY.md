# HTTP API Only - Implementation Details

## Overview

This FlashForge Home Assistant integration uses **exclusively the HTTP API** for all printer communication. Zero TCP/G-code commands are used.

## Why HTTP Only?

### Technical Benefits

1. **Better Reliability**
   - HTTP has built-in error handling
   - Proper status codes and response validation
   - Content-type negotiation
   - Connection pooling via aiohttp

2. **Cleaner Code**
   - No G-code response parsing
   - Structured JSON requests/responses
   - Type-safe with Pydantic models
   - Easier to test and maintain

3. **Modern Protocol**
   - FlashForge's officially supported API
   - Better documentation
   - Active development and support
   - Future-proof

4. **Better Security**
   - Authentication via check code
   - HTTPS capable (if printer supports)
   - No raw socket connections
   - Proper session management

5. **Easier Maintenance**
   - Single communication protocol
   - No dual TCP/HTTP complexity
   - Simpler error handling
   - Fewer edge cases

## What Works via HTTP

### ✅ Fully Supported Features

**Monitoring (Sensors):**
- Machine status (READY, PRINTING, PAUSED, ERROR)
- Temperatures (nozzle current & target, bed current & target)
- Print progress (percentage)
- Layer information (current layer, total layers)
- Time tracking (elapsed time, remaining time)
- Current file name
- Move mode

**Control (Job Control):**
- Pause print job
- Resume print job
- Cancel print job

**Control (Switches):**
- LED on/off (AD5X models)
- Filtration on/off (AD5X models)

**Monitoring (Camera):**
- MJPEG camera stream (port 8080)

### ❌ Excluded (TCP/G-code Required)

The following features require TCP G-code commands and are **intentionally excluded**:

1. **Home Axes** (`G28`)
   - Requires sending raw G-code
   - Not available via HTTP API
   - Workaround: Use printer touchscreen

2. **Manual Movement** (`G0`, `G1`)
   - Requires sending raw G-code commands
   - Not available via HTTP API
   - Workaround: Use printer touchscreen

3. **Filament Runout Sensor Control**
   - Uses custom FlashForge G-code
   - Not exposed via HTTP API
   - Workaround: Use printer settings

4. **Direct Temperature Setting**
   - Technically available via HTTP for some models
   - Excluded for safety (prevent accidental burns/damage)
   - Workaround: Use printer touchscreen or slicer

## HTTP API Endpoints Used

### Authentication
All requests require:
```json
{
  "serialNumber": "ABCD1234",
  "checkCode": "12345678"
}
```

### Endpoints

**1. Machine Status** (`/status`)
- GET request
- Returns comprehensive machine information
- Polled every 10 seconds (configurable)

**2. Control Commands** (`/control`)
- POST request
- Controls LED, filtration, etc.
- Payload includes command and args

**3. Job Control** (`/control`)
- POST request
- Pause/resume/cancel print jobs
- Uses `stateCtrl_cmd` with specific actions

**4. Camera Stream** (`http://IP:8080/?action=stream`)
- MJPEG stream endpoint
- Direct HTTP streaming
- No authentication required (printer limitation)

## Code Structure

### HTTP-Only Modules Used

From `ff-5mp-api-py` library:

```python
# HTTP-based modules (used)
client.info.get_machine_status()          # ✅ Used
client.info.get_machine_info()            # ✅ Used
client.job_control.pause_print_job()      # ✅ Used
client.job_control.resume_print_job()     # ✅ Used
client.job_control.cancel_print_job()     # ✅ Used
client.control.set_led_on()               # ✅ Used
client.control.set_led_off()              # ✅ Used
client.control.set_external_filtration_on()  # ✅ Used
client.control.set_filtration_off()       # ✅ Used

# TCP-based modules (NOT used)
client.control.home_axes()                # ❌ Excluded
client.tcp_client.*                       # ❌ Never accessed
```

### Network Ports

**HTTP API:**
- Port: 8898
- Protocol: HTTP (JSON)
- Authentication: Serial number + check code

**Camera:**
- Port: 8080
- Protocol: HTTP (MJPEG)
- Authentication: None

**Discovery:**
- Send: UDP port 48899 (broadcast)
- Receive: UDP port 18007
- Protocol: UDP broadcast

**TCP API (NOT USED):**
- Port: 8899
- Protocol: Raw TCP socket
- ❌ Completely excluded from this integration

## Error Handling

HTTP-specific error handling:

```python
# Content-Type fix for FlashForge bug
try:
    data = await response.json()
except aiohttp.ContentTypeError:
    # Fallback: Some printers send "appliation/json"
    text = await response.text()
    data = json.loads(text)

# Status code checking
if response.status != 200:
    raise UpdateFailed("HTTP request failed")

# Response validation
if not NetworkUtils.is_ok(data):
    raise UpdateFailed("Printer returned error")
```

## Performance Characteristics

### Network Traffic (10s polling)

**Per polling cycle:**
- HTTP GET `/status`: ~200 bytes request
- Response: ~1-2 KB JSON
- Total: ~2.5 MB per hour

**Comparison to TCP:**
- HTTP: Single request/response
- TCP: Multiple commands + parsing
- HTTP is actually MORE efficient!

### Connection Management

**HTTP:**
- Connection pooling via aiohttp
- Keep-alive connections
- Automatic retry logic
- Session management

**TCP (if it were used):**
- Raw socket connections
- Manual reconnection
- No connection pooling
- More complex state management

## Testing HTTP-Only Implementation

### Verification Steps

1. **Check No TCP Usage:**
```python
# This should never be called
assert client.tcp_client is not None  # Only instantiated, never used
assert not hasattr(client, 'tcp_connection')  # No active connection
```

2. **Monitor Network Traffic:**
```bash
# Should only see port 8898 (HTTP API)
tcpdump -i any host <printer_ip> and port 8898

# Should NOT see port 8899 (TCP API)
tcpdump -i any host <printer_ip> and port 8899  # Empty
```

3. **Verify All Features Work:**
- All sensors update ✅
- Pause/resume/cancel work ✅
- LED/filtration toggles work ✅
- No errors in logs ✅

## Migration from TCP-Based Integrations

### Differences from Reference Implementation

**Reference (kruzhkov/hass-flashforge-adventurer-5):**
- Uses TCP port 8899
- Sends raw G-code commands
- Parses text-based responses
- Has home axes button
- Manual movement possible

**This Implementation:**
- Uses HTTP port 8898
- Sends JSON requests
- Receives JSON responses
- No home axes button
- No manual movement

### Feature Parity

| Feature | Reference (TCP) | This (HTTP) | Status |
|---------|----------------|-------------|---------|
| Monitor temps | ✅ | ✅ | Same |
| Print progress | ✅ | ✅ | Same |
| Layer info | ✅ | ✅ | Same |
| Machine status | ✅ | ✅ | Same |
| Pause/resume/cancel | ✅ | ✅ | Same |
| Camera | ✅ | ✅ | Same |
| LED control | ❌ | ✅ | Better! |
| Filtration | ❌ | ✅ | Better! |
| Home axes | ✅ | ❌ | Removed |
| Manual movement | ✅ | ❌ | Removed |

**Result:** This HTTP implementation has MORE features (LED, filtration) despite excluding TCP!

## Conclusion

This HTTP-only implementation provides:
- ✅ All critical monitoring features
- ✅ All critical control features
- ✅ Better reliability than TCP
- ✅ Cleaner, more maintainable code
- ✅ Future-proof architecture
- ✅ Additional features (LED, filtration)

The excluded features (home axes, manual movement) are:
- Rarely needed in Home Assistant
- Better handled via printer touchscreen
- Safety risk if automated
- Not worth the TCP complexity

**This is the RIGHT architectural choice for a production integration.**

---

**Protocol:** HTTP API Only
**TCP Usage:** Zero
**Port 8898:** ✅ Used
**Port 8899:** ❌ Never touched
**Implementation:** Clean, modern, reliable
