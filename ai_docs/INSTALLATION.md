# Installation Guide

This guide will walk you through installing and configuring the FlashForge Home Assistant integration.

## Prerequisites

### 1. Printer Setup

Before installing the integration, you need to enable LAN mode on your FlashForge printer:

1. **Turn on your FlashForge printer**
2. **Navigate to Settings** on the printer's touchscreen
3. **Select Network → LAN Mode**
4. **Enable LAN Mode**
5. **Note the Check Code** displayed on screen (you'll need this during setup)
6. **Note the Serial Number** (visible on the printer display)

**Video Tutorial:** [How to Enable LAN Mode](https://www.youtube.com/watch?v=krdEGccZuKo)

### 2. Network Setup (Recommended)

For best reliability, assign a **static IP address** to your printer:

1. Log into your router's admin panel
2. Find your FlashForge printer in the DHCP client list
3. Create a DHCP reservation or assign a static IP
4. Note the IP address for manual configuration (optional)

### 3. Home Assistant Requirements

- Home Assistant 2023.1.0 or newer
- Printer and Home Assistant on the same local network
- HACS installed (for easiest installation)

## Installation Methods

### Method 1: HACS (Recommended)

1. Open **HACS** in your Home Assistant instance
2. Click on **Integrations**
3. Click the **⋮** (three dots) menu in the top right
4. Select **Custom repositories**
5. Enter repository URL: `https://github.com/cope/ff-5mp-hass`
6. Select category: **Integration**
7. Click **Add**
8. Search for **"FlashForge 3D Printer"**
9. Click **Download**
10. **Restart Home Assistant**

### Method 2: Manual Installation

1. Download the [latest release](https://github.com/cope/ff-5mp-hass/releases/latest)
2. Unzip the downloaded file
3. Copy the `custom_components/flashforge` folder to your Home Assistant installation:
   ```
   <config_directory>/custom_components/flashforge/
   ```
4. **Restart Home Assistant**

**Note:** Your config directory is where your `configuration.yaml` file is located.

## Configuration

### Step 1: Add Integration

1. Go to **Settings** → **Devices & Services**
2. Click **+ ADD INTEGRATION**
3. Search for **"FlashForge"** or **"FlashForge 3D Printer"**
4. Click on the integration

### Step 2: Choose Configuration Mode

You'll see two options:

- **Automatic Discovery** - Recommended for most users
- **Manual Entry** - For advanced network setups

#### Option A: Automatic Discovery

1. Select **"Automatic Discovery"**
2. Click **Submit**
3. Wait 5-10 seconds while the integration scans your network
4. **If one printer is found:**
   - You'll be taken directly to the credentials step
5. **If multiple printers are found:**
   - Select your printer from the dropdown list
   - Click **Submit**
6. **Enter Check Code:**
   - Enter the check code from your printer's LAN mode screen
   - Click **Submit**
7. **Done!** Your printer is now configured

**Troubleshooting Discovery:**
- If no printers are found, try manual entry
- Ensure printer is powered on and LAN mode is enabled
- Check that printer and Home Assistant are on the same network
- Verify firewall isn't blocking UDP port 18007

#### Option B: Manual Entry

1. Select **"Manual Entry"**
2. Click **Submit**
3. Fill in the form:
   - **Printer Name:** A friendly name (e.g., "3D Printer", "AD5M")
   - **IP Address:** Your printer's IP address (e.g., 192.168.1.100)
   - **Serial Number:** From printer display
   - **Check Code:** From printer's LAN mode screen
4. Click **Submit**
5. **Done!** Your printer is now configured

### Step 3: Configure Options (Optional)

After setup, you can adjust the polling interval:

1. Go to **Settings** → **Devices & Services**
2. Find **"FlashForge 3D Printer"** in the list
3. Click **Configure**
4. Adjust **Update Interval** (5-300 seconds, default: 10)
5. Click **Submit**

**Lower intervals = more responsive but more network traffic**

## Verifying Installation

### Check Entities

After configuration, you should see:

1. Go to **Settings** → **Devices & Services**
2. Click on **FlashForge 3D Printer**
3. Click on your printer device
4. You should see entities like:
   - Machine Status
   - Nozzle Temperature
   - Bed Temperature
   - Print Progress
   - Binary sensors (Printing, Online, Error, Paused)
   - Switches (LED, Filtration - if supported)
   - Buttons (Home, Pause, Resume, Cancel)
   - Camera

### Test the Integration

1. **Check sensor values:**
   - Temperatures should show current values
   - Machine status should show current state

2. **Test a switch (if available):**
   - Toggle the LED switch
   - Verify LED turns on/off on printer

3. **View camera feed:**
   - Add camera entity to a dashboard
   - Verify live feed appears

## Common Installation Issues

### "Cannot Connect" Error

**Possible causes:**
- Incorrect IP address → Verify IP in router settings
- Wrong serial number or check code → Double-check values on printer
- LAN mode not enabled → Enable in printer settings
- Network connectivity issue → Ping printer IP from Home Assistant host
- Firewall blocking port 8898 → Check firewall rules

**Solution:**
1. Delete the failed integration
2. Verify LAN mode is enabled
3. Confirm check code on printer display
4. Try manual configuration with verified IP address

### "No Printers Found" During Discovery

**Possible causes:**
- Printer not on same network → Check network configuration
- Firewall blocking UDP broadcasts → Check firewall on port 18007
- LAN mode disabled → Enable in printer settings

**Solution:**
1. Use manual entry instead
2. Verify printer IP with router admin panel
3. Check firewall settings

### Integration Loads but Entities Show "Unavailable"

**Possible causes:**
- Printer powered off → Turn on printer
- Network connectivity lost → Check network
- Invalid credentials → Verify check code hasn't changed

**Solution:**
1. Check printer is powered on and connected
2. Go to **Settings** → **System** → **Logs** to see errors
3. Reload integration or restart Home Assistant

### Entities Not Updating

**Possible causes:**
- Scan interval too high → Reduce in options
- Printer in sleep mode → Wake printer
- Network latency issues → Check network

**Solution:**
1. Check scan interval in integration options
2. Restart integration: **Settings** → **Devices & Services** → Click **⋮** → **Reload**

### Switch Entities Not Available

**Expected behavior:**
- LED and Filtration switches only work on supported models (AD5X series)
- These will show as "unavailable" on unsupported models

## Next Steps

Once installed:

1. **Add to Dashboard** - Create cards to monitor your printer
2. **Create Automations** - Get notified when prints complete
3. **Set up Alerts** - Monitor for errors or temperature issues

See the [README.md](README.md) for example automations and dashboard configurations.

## Getting Help

If you encounter issues:

1. Check the logs: **Settings** → **System** → **Logs**
2. Search [existing issues](https://github.com/cope/ff-5mp-hass/issues)
3. Create a [new issue](https://github.com/cope/ff-5mp-hass/issues/new) with:
   - Home Assistant version
   - Printer model
   - Error messages from logs
   - Steps to reproduce

## Uninstalling

To remove the integration:

1. Go to **Settings** → **Devices & Services**
2. Find **FlashForge 3D Printer**
3. Click **⋮** (three dots)
4. Select **Delete**
5. Confirm deletion

To completely remove files (manual installation only):
1. Delete `<config>/custom_components/flashforge/` folder
2. Restart Home Assistant
