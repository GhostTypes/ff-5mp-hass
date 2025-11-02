# Quick Testing Guide

This guide will help you test the integration for the first time.

## Pre-Testing Setup

### 1. Ensure Printer is Ready

- [ ] Printer powered on
- [ ] LAN mode enabled
- [ ] Check code visible on printer display
- [ ] Serial number noted
- [ ] Printer connected to same network as Home Assistant

### 2. Copy Integration to Home Assistant

**Option A: Direct Copy**
```bash
# From this repository directory
cp -r custom_components/flashforge /path/to/homeassistant/config/custom_components/
```

**Option B: Symlink (for development)**
```bash
# From Home Assistant config directory
ln -s /path/to/ff-5mp-hass/custom_components/flashforge custom_components/flashforge
```

### 3. Restart Home Assistant

Restart to load the new integration.

## Testing Checklist

### Phase 1: Basic Setup

#### Test 1: Automatic Discovery

1. Go to **Settings** → **Devices & Services**
2. Click **+ ADD INTEGRATION**
3. Search for "FlashForge"
4. Select **"Automatic Discovery"**
5. Click **Submit**

**Expected:**
- Should find your printer within 5 seconds
- Shows printer name from UDP response

**If it fails:**
- Check printer LAN mode is enabled
- Verify printer and HA on same network
- Try manual entry instead

#### Test 2: Enter Check Code

1. Enter the check code from printer display
2. Click **Submit**

**Expected:**
- Connection validates successfully
- Config entry created
- Redirected to devices page

**If it fails:**
- Verify check code is correct
- Check printer IP is accessible
- Look at Home Assistant logs: **Settings** → **System** → **Logs**

### Phase 2: Entity Verification

#### Test 3: Check All Entities Appear

1. Go to **Settings** → **Devices & Services**
2. Click **FlashForge 3D Printer**
3. Click on your printer device

**Expected entities:**

**Sensors (12):**
- [ ] Machine Status
- [ ] Nozzle Temperature
- [ ] Nozzle Target Temperature
- [ ] Bed Temperature
- [ ] Bed Target Temperature
- [ ] Print Progress
- [ ] Current File
- [ ] Current Layer
- [ ] Total Layers
- [ ] Elapsed Time
- [ ] Remaining Time
- [ ] Move Mode

**Binary Sensors (4):**
- [ ] Printing
- [ ] Online
- [ ] Error
- [ ] Paused

**Switches (2):**
- [ ] LED (may be unavailable on unsupported models)
- [ ] Filtration (may be unavailable on unsupported models)

**Buttons (3):**
- [ ] Pause Print
- [ ] Resume Print
- [ ] Cancel Print

**Camera (1):**
- [ ] Camera

#### Test 4: Verify Sensor Values

Check that sensor values make sense:

- [ ] Temperatures show reasonable values (°C)
- [ ] Machine status shows current state
- [ ] Binary sensors reflect actual printer state
- [ ] If printing: progress, layers, times update

### Phase 3: Functional Testing

#### Test 5: LED Switch (if available)

1. Toggle **LED** switch ON
2. Check printer LED turns on
3. Toggle **LED** switch OFF
4. Check printer LED turns off

**Expected:** LED responds to switch changes

#### Test 6: Filtration Switch (if available)

1. Toggle **Filtration** switch ON
2. Check filtration system activates
3. Toggle **Filtration** switch OFF
4. Check filtration system deactivates

**Expected:** Filtration responds to switch changes

#### Test 7: Camera Feed

1. Go to **Overview** (or any dashboard)
2. Add **Camera** entity to a card
3. View the feed

**Expected:**
- MJPEG stream displays
- Live video from printer camera

**If camera doesn't work:**
- Verify printer model supports camera
- Check port 8080 is accessible
- Camera may not be supported on all models

### Phase 4: Update Testing

#### Test 9: Monitor Updates

1. Watch sensor values for 30 seconds
2. Note if values update

**Expected:**
- Values update every 10 seconds (default)
- No errors in logs

#### Test 10: Change Scan Interval

1. Go to **Settings** → **Devices & Services**
2. Find **FlashForge 3D Printer**
3. Click **Configure**
4. Change **Update Interval** to 30 seconds
5. Click **Submit**
6. Watch sensor values

**Expected:**
- Values now update every 30 seconds
- Change takes effect immediately

### Phase 5: Error Handling

#### Test 11: Connection Loss

1. Turn off printer (or disconnect network)
2. Wait 30 seconds
3. Check entity states

**Expected:**
- Entities show as "Unavailable"
- Logs show connection errors (normal)

4. Turn printer back on
5. Wait 30 seconds

**Expected:**
- Entities recover automatically
- Values update normally

#### Test 12: Reload Integration

1. Go to **Settings** → **Devices & Services**
2. Find **FlashForge 3D Printer**
3. Click **⋮** (three dots)
4. Select **Reload**

**Expected:**
- Integration reloads successfully
- All entities remain
- Values resume updating

### Phase 6: Print Job Testing (Optional)

#### Test 13: During Active Print

If you have a print running:

1. Monitor **Print Progress** sensor
2. Check **Current Layer** and **Total Layers**
3. Watch **Elapsed Time** and **Remaining Time**
4. Verify **Printing** binary sensor is ON

**Expected:**
- Progress increases over time
- Layer counts accurate
- Times update correctly

#### Test 14: Pause/Resume (⚠️ Use with caution!)

**Only if you're comfortable pausing your print:**

1. Press **Pause Print** button
2. Check printer pauses
3. Wait 10 seconds
4. Press **Resume Print** button
5. Check printer resumes

**Expected:**
- Printer responds to commands
- Binary sensors reflect state changes

#### Test 15: Cancel Print (⚠️ Destructive!)

**Only test this on a test print you don't care about:**

1. Press **Cancel Print** button
2. Check printer cancels job

**Expected:**
- Print job cancelled
- Machine status returns to READY

### Phase 7: Configuration Flow Testing

#### Test 16: Manual Entry

1. Remove the integration:
   - **Settings** → **Devices & Services**
   - Find **FlashForge 3D Printer**
   - Click **⋮** → **Delete**

2. Re-add using manual entry:
   - **Settings** → **Devices & Services**
   - Click **+ ADD INTEGRATION**
   - Search "FlashForge"
   - Select **"Manual Entry"**
   - Enter: Name, IP, Serial Number, Check Code
   - Click **Submit**

**Expected:**
- Integration sets up successfully
- All entities appear as before

#### Test 17: Duplicate Detection

1. Try to add the same printer again
2. Go through config flow

**Expected:**
- Shows "Already configured" error
- Prevents duplicate entry

## Common Issues & Solutions

### "Cannot Connect" Error

**Check:**
- [ ] Printer IP is correct
- [ ] Serial number matches printer
- [ ] Check code is current (hasn't changed)
- [ ] Printer LAN mode is enabled
- [ ] Network connectivity (can you ping the printer?)

**Look at logs:**
```bash
# In Home Assistant
Settings → System → Logs
# Filter for "flashforge"
```

### Entities Show "Unavailable"

**Check:**
- [ ] Printer is powered on
- [ ] Network connection is stable
- [ ] Check code hasn't changed
- [ ] Reload integration

**Try:**
```
Settings → Devices & Services → FlashForge → ⋮ → Reload
```

### Discovery Finds No Printers

**Not necessarily a bug!** Use manual entry instead.

**Check:**
- [ ] Printer is on
- [ ] LAN mode enabled
- [ ] Same network as HA
- [ ] Firewall not blocking UDP

### Switches Don't Work

**Check:**
- [ ] Printer model supports LED/filtration (AD5X series)
- [ ] Entities showing "unavailable" is normal on unsupported models

## Logging Debug Information

If you encounter issues, enable debug logging:

1. Edit `configuration.yaml`:
```yaml
logger:
  default: info
  logs:
    custom_components.flashforge: debug
    flashforge: debug  # The library
```

2. Restart Home Assistant
3. Reproduce the issue
4. Check logs: **Settings** → **System** → **Logs**

## Reporting Issues

If you find bugs, please report with:

1. **Home Assistant version:** (e.g., 2024.1.0)
2. **Printer model:** (e.g., FlashForge Adventurer 5M)
3. **Error message:** (from logs)
4. **Steps to reproduce:** What you did before the error
5. **Expected vs actual behavior:** What should happen vs what did happen

**GitHub Issues:** https://github.com/cope/ff-5mp-hass/issues

## Success Criteria

✅ **Integration is working correctly if:**

- Discovery finds your printer (or manual entry succeeds)
- All expected entities appear
- Sensor values are accurate
- Entities update every scan interval
- Switches and buttons work (if supported)
- Camera displays feed (if supported)
- Integration survives printer power cycle
- No continuous errors in logs

## Next Steps After Testing

Once testing is complete:

1. **Document any issues** found
2. **Note printer model** tested on
3. **Create example automations** for your use case
4. **Share feedback** if integration works well
5. **Consider contributing** improvements

## Advanced Testing

### Performance Testing

Monitor Home Assistant performance:
```bash
# Check memory usage
Settings → System → Hardware

# Monitor database size
Settings → System → Storage
```

### Network Traffic Analysis

Use Wireshark or tcpdump to verify:
- HTTP requests go to port 8898
- Polling happens at configured interval
- No excessive retries

### Stress Testing

- Run with multiple printers
- Test with very short scan interval (5s)
- Monitor during long prints

---

**Happy Testing!** 🎉

If the integration works well for you, consider:
- ⭐ Starring the repository
- 📝 Writing a review
- 🤝 Contributing improvements
- 💬 Sharing in Home Assistant community
