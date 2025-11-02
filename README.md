# FlashForge 3D Printer - Home Assistant Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

A Home Assistant custom integration for FlashForge 3D Printers using the HTTP API. This integration provides comprehensive monitoring and control of your FlashForge printer directly from Home Assistant.

## Features

- **Automatic Discovery**: Automatically discover FlashForge printers on your network via UDP broadcast
- **Manual Configuration**: Supports manual IP entry for custom network setups
- **HTTP API Only**: Uses the modern HTTP API (port 8898) for reliable communication
- **Comprehensive Monitoring**:
  - Real-time temperature monitoring (nozzle and bed)
  - Print progress tracking
  - Layer information
  - Time estimates (elapsed and remaining)
  - Machine status and move mode
  - Current file information

- **Control Capabilities**:
  - LED control (if supported by printer model)
  - Filtration control (if supported by printer model)
  - Pause/Resume/Cancel print jobs
  - Live camera feed

- **Configurable Update Interval**: Set custom polling intervals (5-300 seconds, default 10s)

## Supported Models

- FlashForge Adventurer 5M Series
- FlashForge Adventurer 4
- Other FlashForge models with HTTP API support

## Prerequisites

### Printer Setup

1. **Enable LAN Mode** on your FlashForge printer
2. **Obtain Check Code** from the printer's display (Settings → Network → LAN Mode)
3. **Note the Serial Number** (visible on printer display or discovery)
4. **Assign Static IP** (recommended) to your printer via your router settings

For detailed instructions on enabling LAN mode, see: [FlashForge LAN Mode Setup](https://www.youtube.com/watch?v=krdEGccZuKo)

### Home Assistant Requirements

- Home Assistant 2023.1.0 or newer
- Network access to printer on the same local network

## Installation

### HACS (Recommended)

1. Open HACS in Home Assistant
2. Click on "Integrations"
3. Click the three dots in the top right corner
4. Select "Custom repositories"
5. Add this repository URL: `https://github.com/cope/ff-5mp-hass`
6. Select category: "Integration"
7. Click "Add"
8. Search for "FlashForge 3D Printer" in HACS
9. Click "Download"
10. Restart Home Assistant

### Manual Installation

1. Download the latest release from this repository
2. Copy the `custom_components/flashforge` folder to your Home Assistant's `custom_components` directory
3. If the `custom_components` directory doesn't exist, create it in the same directory as your `configuration.yaml`
4. Restart Home Assistant

## Configuration

### Via UI (Recommended)

1. Go to **Settings** → **Devices & Services**
2. Click **"+ Add Integration"**
3. Search for **"FlashForge 3D Printer"**
4. Choose configuration mode:
   - **Automatic Discovery**: Scans network for printers
   - **Manual Entry**: Enter IP address and credentials manually

#### Automatic Discovery

1. Select "Automatic Discovery"
2. Wait for printer discovery (up to 5 seconds)
3. If multiple printers found, select your printer
4. Enter the **Check Code** from your printer's display
5. Click Submit

#### Manual Configuration

1. Select "Manual Entry"
2. Enter:
   - **Printer Name**: Friendly name (e.g., "My AD5M")
   - **IP Address**: Printer's IP address (e.g., 192.168.1.100)
   - **Serial Number**: Printer's serial number
   - **Check Code**: Check code from printer display
3. Click Submit

### Options

After setup, you can configure additional options:

1. Go to **Settings** → **Devices & Services**
2. Find your FlashForge printer
3. Click "Configure"
4. Adjust **Update Interval** (5-300 seconds, default: 10 seconds)

## Entities

Once configured, the integration creates the following entities:

### Sensors (18 total)

**Core Print Status:**
| Entity | Description | Unit |
|--------|-------------|------|
| Machine Status | Current printer state (READY, PRINTING, PAUSED, ERROR) | - |
| Nozzle Temperature | Current nozzle temperature | °C |
| Nozzle Target Temperature | Target nozzle temperature | °C |
| Bed Temperature | Current bed temperature | °C |
| Bed Target Temperature | Target bed temperature | °C |
| Print Progress | Current print job progress | % |
| Current File | Name of current/last file | - |
| Current Layer | Current layer number | - |
| Total Layers | Total layers in print | - |
| Elapsed Time | Time elapsed since print started | seconds |
| Remaining Time | Estimated time remaining (calculated) | seconds |

**Print Details:**
| Entity | Description | Unit |
|--------|-------------|------|
| Filament Length | Estimated filament usage | meters |
| Filament Weight | Estimated filament weight | grams |
| Print Speed | Current print speed adjustment | % |
| Z-Axis Offset | Z-axis compensation value | mm |
| Nozzle Size | Installed nozzle size | - |
| Filament Type | Current filament type | - |

### Binary Sensors

| Entity | Description |
|--------|-------------|
| Printing | Whether printer is actively printing |
| Online | Connection status |
| Error | Whether printer has an error |
| Paused | Whether print is paused |

### Switches

| Entity | Description | Availability |
|--------|-------------|--------------|
| LED | Control printer LED lighting | AD5X models |
| Filtration | Control air filtration system | AD5X models |

### Buttons

| Entity | Description |
|--------|-------------|
| Pause Print | Pause current print job |
| Resume Print | Resume paused print job |
| Cancel Print | Cancel current print job |

### Camera

| Entity | Description |
|--------|-------------|
| Camera | Live MJPEG camera stream (port 8080) |

## Usage Examples

### Automation: Notify When Print Complete

```yaml
automation:
  - alias: "Notify when 3D print completes"
    trigger:
      - platform: state
        entity_id: binary_sensor.flashforge_printer_printing
        from: "on"
        to: "off"
    action:
      - service: notify.mobile_app
        data:
          title: "3D Print Complete"
          message: "Your print job {{ state_attr('sensor.flashforge_printer_current_file', 'state') }} is finished!"
```

### Automation: Turn Off LED When Not Printing

```yaml
automation:
  - alias: "Turn off printer LED when idle"
    trigger:
      - platform: state
        entity_id: sensor.flashforge_printer_machine_status
        to: "READY"
        for:
          minutes: 5
    action:
      - service: switch.turn_off
        target:
          entity_id: switch.flashforge_printer_led
```

### Dashboard Card Example

```yaml
type: entities
title: FlashForge Printer
entities:
  - entity: sensor.flashforge_printer_machine_status
  - entity: binary_sensor.flashforge_printer_printing
  - entity: sensor.flashforge_printer_print_progress
  - entity: sensor.flashforge_printer_nozzle_temperature
  - entity: sensor.flashforge_printer_bed_temperature
  - entity: sensor.flashforge_printer_current_file
  - entity: sensor.flashforge_printer_remaining_time
  - type: divider
  - entity: switch.flashforge_printer_led
  - entity: button.flashforge_printer_pause_print
  - entity: button.flashforge_printer_resume_print
  - entity: button.flashforge_printer_cancel_print
```

## Troubleshooting

### Printer Not Discovered

- Ensure printer is on the same network as Home Assistant
- Check that LAN mode is enabled on the printer
- Try manual configuration with printer's IP address
- Check firewall settings allow UDP broadcast on port 18007

### Cannot Connect Error

- Verify IP address is correct
- Ensure serial number and check code are entered correctly
- Confirm LAN mode is enabled with correct check code
- Check network connectivity between Home Assistant and printer
- Assign static IP to printer in router settings

### Entities Not Updating

- Check configured scan interval in integration options
- Verify printer is powered on and connected to network
- Check Home Assistant logs for errors: **Settings** → **System** → **Logs**

### Switch Entities Not Available

- LED and Filtration switches only available on supported models (primarily AD5X series)
- Check that printer model supports these features
- Entities will show as unavailable if feature not supported

## Development

This integration uses the [flashforge-python-api](https://github.com/cope/ff-5mp-api-py) library for all printer communication.

### Project Structure

```
custom_components/flashforge/
├── __init__.py          # Component initialization
├── manifest.json        # Integration metadata
├── config_flow.py       # Configuration UI
├── const.py            # Constants
├── coordinator.py       # Data update coordinator
├── sensor.py           # Sensor entities
├── binary_sensor.py    # Binary sensor entities
├── switch.py           # Switch entities
├── button.py           # Button entities
├── camera.py           # Camera entity
├── strings.json        # UI strings
└── translations/
    └── en.json         # English translations
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Credits

- Based on reference implementation: [hass-flashforge-adventurer-5](https://github.com/kruzhkov/hass-flashforge-adventurer-5)
- Uses the [flashforge-python-api](https://github.com/cope/ff-5mp-api-py) library
- Developed for the Home Assistant community

## Support

- **Issues**: [GitHub Issues](https://github.com/cope/ff-5mp-hass/issues)
- **Discussions**: [GitHub Discussions](https://github.com/cope/ff-5mp-hass/discussions)
- **Home Assistant Community**: [Community Forum](https://community.home-assistant.io/)

## Changelog

### Version 1.0.0
- Initial release
- HTTP API support
- Automatic discovery and manual configuration
- Full sensor coverage
- Control buttons and switches
- Camera support
- Configurable polling interval
