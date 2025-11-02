# FlashForge Home Assistant Integration - Feature List

## ✅ Implemented Features

### Configuration & Setup

**Auto-Discovery:**
- UDP broadcast discovery (finds printers automatically)
- Multi-printer selection (if multiple found)
- Single printer auto-select

**Manual Configuration:**
- Manual IP entry option
- Serial number input
- Check code authentication
- Connection validation

**Options:**
- Configurable scan interval (5-300s, default 10s)
- Reload integration support

**Security:**
- Check code authentication (stored in config entries)
- Serial number as unique ID
- Duplicate printer detection

---

### Monitoring Entities (16 total)

**Sensors (12):**
1. Machine Status (READY, BUILDING_FROM_SD, PAUSED, ERROR)
2. Nozzle Temperature (°C)
3. Nozzle Target Temperature (°C)
4. Bed Temperature (°C)
5. Bed Target Temperature (°C)
6. Print Progress (%)
7. Current File (filename)
8. Current Layer (number)
9. Total Layers (number)
10. Elapsed Time (seconds)
11. Remaining Time (seconds)
12. Move Mode (string)

**Binary Sensors (4):**
1. Is Printing (on/off)
2. Is Online (connectivity status)
3. Has Error (problem detection)
4. Is Paused (paused state)

---

### Control Entities (6 total)

**Switches (2):**
1. LED Control (on/off) - AD5X models only
2. Filtration Control (on/off) - AD5X models only
   - Auto-detects if supported
   - Shows "unavailable" on unsupported models

**Buttons (3):**
1. Pause Print
2. Resume Print
3. Cancel Print

**Camera (1):**
1. Live MJPEG Camera Stream (port 8080)

---

### Technical Features

**HTTP API Only:**
- Port 8898 for all communication
- Zero TCP usage (no port 8899)
- JSON requests/responses
- Proper error handling

**Data Management:**
- DataUpdateCoordinator pattern
- Configurable polling (10s default)
- Graceful error recovery
- Automatic reconnection

**Entity Management:**
- Device grouping (all entities under one device)
- Unique IDs for entity registry
- Proper device info (manufacturer, model, name)
- Entity availability tracking

**Code Quality:**
- Full async/await
- Type hints throughout
- Pydantic models from ff-5mp-api-py
- Comprehensive error handling
- Logging at appropriate levels

---

### Integration Features

**HACS Compatible:**
- Proper manifest.json
- hacs.json configuration
- GitHub release ready
- Custom repository support

**User Interface:**
- Config flow (no YAML needed)
- User-friendly error messages
- Multi-step configuration
- Options flow for settings

**Documentation:**
- README.md (user guide)
- INSTALLATION.md (setup guide)
- TESTING.md (test checklist)
- IMPLEMENTATION_SUMMARY.md (technical details)
- HTTP_API_ONLY.md (architecture explanation)
- MORNING_BRIEF.md (quick overview)

---

## 📊 Summary

**Total Files Created:** 21
**Total Entities:** 22 (across 5 platforms)
**Platforms:** sensor, binary_sensor, switch, button, camera
**API Protocol:** HTTP only (port 8898)
**Supported Models:** AD5M, AD4, other FlashForge with HTTP API
**Configuration:** UI-based with auto-discovery
**Polling:** Configurable (5-300s, default 10s)

---

## ❌ Intentionally Excluded

**TCP-Only Features:**
- Home axes (requires G-code)
- Manual movement (requires G-code)
- Filament runout sensor control
- Direct temperature setting (safety)

**Complex Features (v1.0 scope):**
- File upload/management
- Print start from HA
- Thumbnail display
- Print history

**Reason:** These require either TCP (excluded by design) or complex UX out of scope for v1.0

---

## 🎯 What Works

✅ Full printer monitoring (temps, progress, status)
✅ Print job control (pause, resume, cancel)
✅ LED control (if supported)
✅ Filtration control (if supported)
✅ Live camera feed
✅ Auto-discovery
✅ Manual configuration
✅ Configurable polling
✅ Graceful error handling
✅ HACS installation
✅ Device grouping
✅ Entity availability tracking

**Everything you need to monitor and control prints from Home Assistant!**
