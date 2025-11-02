# Quick Start - Testing the FlashForge Integration

## You're All Set! 🎉

Home Assistant has been installed and configured in the `homeassistant/` directory with our FlashForge integration ready to test.

## Start Home Assistant

**Option 1: Use the start script (easiest)**
```bash
cd homeassistant
./start-homeassistant.sh
```

**Option 2: Start manually**
```bash
cd homeassistant
source venv/Scripts/activate
hass -c config
```

## What Happens Next

1. **First Run** (1-2 minutes)
   - Home Assistant downloads required components
   - Sets up database
   - Starts web server on port 8123

2. **Open Browser**
   - Go to http://localhost:8123
   - Create your account (first time only)
   - Complete onboarding wizard

3. **Add FlashForge Integration**
   - **Settings** → **Devices & Services**
   - Click **+ ADD INTEGRATION**
   - Search: "**FlashForge**"
   - Choose setup method:
     - **Automatic Discovery** (recommended)
     - **Manual Entry** (if discovery doesn't work)

4. **Enter Credentials**
   - Check code (from printer display)
   - Serial number (if manual entry)

5. **Verify Entities**
   - You should see **28 entities**:
     - 18 Sensors (temps, progress, filament, etc.)
     - 4 Binary Sensors (printing, online, error, paused)
     - 2 Switches (LED, filtration)
     - 3 Buttons (pause, resume, cancel)
     - 1 Camera (MJPEG stream)

## Before You Start

**Make sure your printer has:**
- ✅ LAN mode enabled
- ✅ Check code visible on display
- ✅ Connected to same network as your computer
- ✅ (Optional) Static IP assigned

## Viewing Logs

**In another terminal:**
```bash
tail -f homeassistant/config/home-assistant.log
```

**Or in Home Assistant UI:**
- **Settings** → **System** → **Logs**
- Filter for "flashforge"

Debug logging is already enabled in the config!

## Common Issues

### Integration Doesn't Show Up
**Solution:** Restart Home Assistant (Ctrl+C, then restart)

### Discovery Doesn't Find Printer
**Solution:** Use **Manual Entry** instead - this is normal!

### Connection Fails
**Check:**
- Printer IP is correct
- Check code is current
- Can ping printer: `ping <printer-ip>`

### Entities Unavailable
**Try:**
- Reload integration: Settings → Devices & Services → FlashForge → ⋮ → Reload

## Full Documentation

- **`homeassistant/README.md`** - Detailed setup and troubleshooting
- **`TESTING.md`** - Comprehensive test checklist
- **`README.md`** - Full integration documentation

## Ready to Test!

Everything is configured and ready. Just run:
```bash
cd homeassistant
./start-homeassistant.sh
```

Then open http://localhost:8123 and add the FlashForge integration!

---

**Need help?** Check the logs or see `homeassistant/README.md` for detailed troubleshooting.
