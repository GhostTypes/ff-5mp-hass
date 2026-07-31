<div align="center">
  <h1>FlashForge 3D Printer Integration for Home Assistant</h1>
  <p>A Home Assistant custom integration for modern FlashForge printers using the local HTTP API in LAN mode for reliable, real-time monitoring and control.</p>
</div>

<p align="center">
  <a href="https://github.com/hacs/integration">
    <img src="https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge">
  </a>
  <a href="https://github.com/GhostTypes/ff-5mp-hass/releases">
    <img src="https://img.shields.io/github/release/GhostTypes/ff-5mp-hass.svg?style=for-the-badge">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/github/license/GhostTypes/ff-5mp-hass.svg?style=for-the-badge">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/HA%20Min-2025.1.0-blue.svg?style=for-the-badge&logo=homeassistant&logoColor=white">
  <img src="https://img.shields.io/badge/HA%20Tested-2026.4.2-brightgreen.svg?style=for-the-badge&logo=homeassistant&logoColor=white">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg?style=for-the-badge&logo=python&logoColor=white">
</p>



<div align="center">
  <h2>Features</h2>
</div>

<div align="center">
<table>
  <tr>
    <th>Category</th>
    <th>Feature</th>
    <th>Details</th>
  </tr>
  <tr>
    <td rowspan="4"><b>Monitoring</b></td>
    <td>28 Sensors</td>
    <td>Real-time temperatures (per-toolhead on the Creator 5 series, plus a heated chamber), print progress, filament tracking, fan speeds, air quality (5M Pro / Creator 5 Pro TVOC), active Material Station slot, print completion time, lifetime statistics, and diagnostics</td>
  </tr>
  <tr>
    <td>4 Binary Sensors</td>
    <td>Printing status, connectivity, error detection, pause state</td>
  </tr>
  <tr>
    <td>Live Camera Feed</td>
    <td>MJPEG stream auto-detected from the printer-reported camera stream URL or the standard OEM fallback endpoint when firmware omits it</td>
  </tr>
  <tr>
    <td>5 Image Entities</td>
    <td>Active g-code thumbnail, plus 4 Material Station slot color swatches (AD5X / Creator 5 series — filament color + material label)</td>
  </tr>
  <tr>
    <td rowspan="3"><b>Control</b></td>
    <td>Switches</td>
    <td>LED control, plus Pro-only camera power toggle</td>
  </tr>
  <tr>
    <td>Select Entity</td>
    <td>Filtration mode control (Off/Internal/External)</td>
  </tr>
  <tr>
    <td>4 Buttons</td>
    <td>Pause, resume, cancel print jobs, and clear printer status directly from Home Assistant</td>
  </tr>
  <tr>
    <td>Print Job Card</td>
    <td>Browse the files on the printer, match each tool to a Material Station slot (AD5X / Creator 5 series), and start the print — a dashboard card installed with the integration</td>
  </tr>
  <tr>
    <td rowspan="4"><b>Architecture</b></td>
    <td>HTTP-First Design</td>
    <td>Superior reliability compared to TCP-only implementations</td>
  </tr>
  <tr>
    <td>Async/Await</td>
    <td>Fully asynchronous for optimal Home Assistant integration</td>
  </tr>
  <tr>
    <td>Auto-Discovery</td>
    <td>UDP-based network discovery with manual fallback</td>
  </tr>
  <tr>
    <td>Configurable Polling</td>
    <td>Adjust update frequency from 5-300 seconds</td>
  </tr>
</table>
</div>



<div align="center">
  <h2>Supported Hardware</h2>
</div>

<div align="center">
<table>
  <tr>
    <th>Printer Model</th>
    <th>Support Status</th>
  </tr>
  <tr>
    <td>FlashForge Adventurer 5M</td>
    <td>Supported</td>
  </tr>
  <tr>
    <td>FlashForge Adventurer 5M Pro</td>
    <td>Supported</td>
  </tr>
  <tr>
    <td>FlashForge AD5X</td>
    <td>Supported</td>
  </tr>
  <tr>
    <td>FlashForge Creator 5</td>
    <td>Supported</td>
  </tr>
  <tr>
    <td>FlashForge Creator 5 Pro</td>
    <td>Supported</td>
  </tr>
  <tr>
    <td>Legacy TCP-only models (including Adventurer 4)</td>
    <td>Not Supported</td>
  </tr>
</table>
</div>

<div align="center">
<p><i>Feature availability is detected at runtime. The camera entity is always created, and it becomes available when the printer reports an active OEM stream URL or the standard OEM fallback stream endpoint responds. The camera power switch remains Pro-only.</i></p>
<p><i>This integration does not support legacy TCP-only printers.</i></p>
</div>



<div align="center">
  <h2>Requirements</h2>
</div>

<div align="center">

| Requirement | Details |
|-------------|---------|
| **Home Assistant** | 2025.1.0 or newer |
| **Python Library** | [flashforge-python-api](https://pypi.org/project/flashforge-python-api/) 1.2.0+ |
| **Network** | Local LAN connectivity to printer |
| **Printer Setup** | LAN mode enabled with serial number and check code |

</div>


<div align="center">
  <h2>Installation</h2>
</div>

<div align="center">

| Method | Steps |
|--------|-------|
| **Via HACS (Recommended)** | 1. Open **HACS** in Home Assistant<br>2. Click on **Integrations**<br>3. Click the **⋮** menu (top right) → **Custom repositories**<br>4. Add repository:<br>&nbsp;&nbsp;&nbsp;• **URL**: `https://github.com/GhostTypes/ff-5mp-hass`<br>&nbsp;&nbsp;&nbsp;• **Category**: `Integration`<br>5. Click **Add**<br>6. Search for "FlashForge" in HACS<br>7. Click **Download**<br>8. **Restart Home Assistant** |
| **Manual Installation** | 1. Download the [latest release](https://github.com/GhostTypes/ff-5mp-hass/releases)<br>2. Extract the `custom_components/flashforge` folder<br>3. Copy to your Home Assistant `config/custom_components/` directory<br>4. Restart Home Assistant |

</div>


<div align="center">
  <h2>Configuration</h2>
</div>

<div align="center">

| Step | Instructions |
|------|--------------|
| **Prerequisites: Enable LAN Mode** | Before adding the integration, you must enable LAN mode on your FlashForge printer:<br><br>1. On the printer touchscreen, go to **Settings** → **Network** → **LAN Mode**<br>2. Enable LAN mode<br>3. Note the **Check Code** (8-digit code) - you'll need this for setup<br><br>[Video Tutorial](https://www.youtube.com/watch?v=krdEGccZuKo) |
| **Option 1: Automatic Discovery (Recommended)** | 1. Go to **Settings** → **Devices & Services** → **Integrations**<br>2. Click **+ Add Integration**<br>3. Search for **"FlashForge"**<br>4. Select your AD5X, Adventurer 5M, Adventurer 5M Pro, Creator 5, or Creator 5 Pro from the discovered list<br>5. Enter your printer's **Check Code**<br>6. Click **Submit** |
| **Option 2: Manual Configuration** | 1. Go to **Settings** → **Devices & Services** → **Integrations**<br>2. Click **+ Add Integration**<br>3. Search for **"FlashForge"**<br>4. Select **"Configure Manually"**<br>5. Enter:<br>&nbsp;&nbsp;&nbsp;• **IP Address**: Your printer's IP (e.g., `192.168.1.100`)<br>&nbsp;&nbsp;&nbsp;• **Printer Name**: Friendly name (optional)<br>&nbsp;&nbsp;&nbsp;• **Serial Number**: From the printer settings screen. **Must include the `SN` prefix** (e.g. `SN123456789`) — the `SN` printed on the back sticker is part of the value you enter, not just a label<br>&nbsp;&nbsp;&nbsp;• **Check Code**: From LAN mode settings<br>6. Click **Submit** |
| **Configuration Options** | After setup, you can adjust settings:<br><br>1. Go to **Settings** → **Devices & Services** → **FlashForge**<br>2. Click **⋮** on your printer → **Configure**<br>3. **Scan Interval**: Update frequency in seconds (5-300, default: 10) |
| **LED Switch Override** | If your printer's LED switch is not detected but you know it is supported, enable **Always show LED switch** in the options. This will force the LED switch to appear regardless of printer capability checks. |

</div>



<div align="center">
  <h2>Available Entities</h2>
</div>

<div align="center">

### Sensors

</div>

<div align="center">

| Entity | Description | Unit |
|--------|-------------|------|
| `sensor.flashforge_machine_status` | Current printer state (idle, printing, paused, error) | - |
| `sensor.flashforge_nozzle_temperature` | Current extruder temperature | °C |
| `sensor.flashforge_nozzle_target_temperature` | Target extruder temperature | °C |
| `sensor.flashforge_bed_temperature` | Current bed temperature | °C |
| `sensor.flashforge_bed_target_temperature` | Target bed temperature | °C |
| `sensor.flashforge_print_progress` | Print completion percentage | % |
| `sensor.flashforge_current_file` | Currently printing file name | - |
| `sensor.flashforge_current_layer` | Current layer number | - |
| `sensor.flashforge_total_layers` | Total layer count | - |
| `sensor.flashforge_elapsed_time` | Time spent printing | seconds |
| `sensor.flashforge_remaining_time` | Estimated time remaining | seconds |
| `sensor.flashforge_filament_length` | Estimated filament length needed | meters |
| `sensor.flashforge_filament_weight` | Estimated filament weight | grams |
| `sensor.flashforge_print_speed` | Speed adjustment percentage | % |
| `sensor.flashforge_z_offset` | Z-axis compensation | mm |
| `sensor.flashforge_nozzle_size` | Installed nozzle size | - |
| `sensor.flashforge_filament_type` | Current filament type | - |
| `sensor.flashforge_lifetime_filament` | Total filament used over printer lifetime | meters |
| `sensor.flashforge_lifetime_runtime` | Total runtime over printer lifetime | - |
| `sensor.flashforge_tool_[1-4]_temperature` | Per-toolhead current nozzle temperature (Creator 5 series) | °C |
| `sensor.flashforge_tool_[1-4]_target_temperature` | Per-toolhead target nozzle temperature (Creator 5 series) | °C |
| `sensor.flashforge_chamber_temperature` | Heated chamber current temperature (Creator 5 series) | °C |
| `sensor.flashforge_chamber_target_temperature` | Heated chamber target temperature (Creator 5 series) | °C |

</div>

<div align="center">

### Binary Sensors

</div>

<div align="center">

| Entity | Description | Device Class |
|--------|-------------|--------------|
| `binary_sensor.flashforge_printing` | On when actively printing | `running` |
| `binary_sensor.flashforge_online` | On when printer is connected | `connectivity` |
| `binary_sensor.flashforge_error` | On when error detected | `problem` |
| `binary_sensor.flashforge_paused` | On when print is paused | - |
| `binary_sensor.flashforge_door_open` | On when the lid or front door is ajar | `door` (Creator 5 Pro) |

</div>

<div align="center">

### Switches

</div>

<div align="center">

| Entity | Description | Availability |
|--------|-------------|--------------|
| `switch.flashforge_led` | Control printer LED lights | All Models |
| `switch.flashforge_camera` | Toggle the OEM camera power state | Pro models |

</div>

<div align="center">

### Select Entities

</div>

<div align="center">

| Entity | Description | Options | Availability |
|--------|-------------|---------|--------------|
| `select.flashforge_filtration_mode` | Control filtration system | Off, Internal, External | 5M Pro / Creator 5 Pro |

</div>

<div align="center">

### Buttons

</div>

<div align="center">

| Entity | Description |
|--------|-------------|
| `button.flashforge_pause_print` | Pause active print job |
| `button.flashforge_resume_print` | Resume paused print job |
| `button.flashforge_cancel_print` | Cancel and abort print job |
| `button.flashforge_clear_status` | Clear printer status/errors |

</div>

<div align="center">

### Camera

</div>

<div align="center">

| Entity | Description |
|--------|-------------|
| `camera.flashforge_camera` | Live MJPEG stream from the printer-reported OEM camera URL |

</div>



<div align="center">
  <h2>Starting Prints — the Job Card</h2>
</div>

The integration ships a dashboard card for starting prints of files already on the printer, including the **material matching** step the AD5X and Creator 5 series need for multi-material files.

**Adding it:** the card is installed and registered with the integration — there is no separate HACS entry and no Lovelace resource to add. Edit a dashboard → **Add card** → search for **FlashForge Print Job** → pick your printer.

> [!NOTE]
> **After installing or updating, reload the page once.** A browser tab loads the list of frontend modules when the page opens, so a tab that was already open before the install does not know the card exists yet — the picker will not offer it. The integration tells you when this applies: you will get a **notification in the sidebar** saying the card is ready. Press <kbd>Ctrl</kbd>+<kbd>R</kbd> (<kbd>Cmd</kbd>+<kbd>R</kbd> on a Mac) and it will be there. You will not be asked again until the next update.

**Using it:**

1. Pick a file. Each row shows its thumbnail, print time, filament weight and per-tool material swatches, where the printer reports them.
2. Optionally tick **Level the bed before printing**.
3. Press **Start print**.
   - **Single-material file, or a printer with no Material Station** — a confirmation dialog, then the print starts.
   - **Material Station file (AD5X / Creator 5 series)** — the matching dialog opens. Every tool in the file must be mapped to a loaded slot before the print can start. A sensible mapping is pre-filled for you; review it and press **Start print**, or click a tool and then the slot you want it to come from to change it.

**The matching rules**, identical to the FlashForge desktop app:

| Situation | Result |
|-----------|--------|
| Slot material differs from the tool's material | **Blocked** — PLA cannot be printed from a PETG slot |
| Slot color differs from the tool's color | **Allowed**, with a warning — the print will come out a different color |
| Slot is empty, or already assigned to another tool | Cannot be selected |
| A tool is left unmapped | **Start print** stays disabled |

> [!NOTE]
> **Only the ten most recent files are listed, on every model.** That is what the printer's HTTP API offers; the full local file listing exists only over the legacy TCP channel this integration deliberately does not speak. Send a file from your slicer and it will appear at the top of the list.

> [!NOTE]
> Per-file metadata (print time, filament weight, per-tool materials) is reported by the AD5X and Creator 5 series. The 5M / 5M Pro report file names only, so those rows show a name and start without a matching step.

<div align="center">
  <h2>Languages</h2>
</div>

The integration and the job card both follow the language set in your Home Assistant profile — there is nothing to configure.

| Language | Integration | Job card |
|----------|-------------|----------|
| English | ✅ | ✅ |
| German (Deutsch) | ✅ | ✅ |

German was contributed by [@RedAces](https://github.com/RedAces). Anything not yet translated falls back to English rather than showing a blank.

<details>
<summary><b>Adding a language</b></summary>

Two files, both plain JSON, both copied from the English version beside them:

1. **The integration** — copy `custom_components/flashforge/translations/en.json` to `<code>.json` (e.g. `fr.json`) and translate the values. Keys must match English exactly; Home Assistant has no per-key fallback here.
2. **The job card** — copy `custom_components/flashforge/frontend/translations/en.json` the same way. Leave `{placeholders}` such as `{slot}` and `{tool}` intact and in a natural position for your language. Keys you omit fall back to English, so a partial translation is fine.

Keep `_one` / `_other` pairs together (`tools_one`, `tools_other`) — they are chosen by count, and a missing half renders empty.

Then run `pytest tests/unit/test_translations.py`, which checks both files against English for missing or unknown keys, mismatched placeholders, and incomplete plurals. No build step and no JavaScript changes are involved. PRs welcome.
</details>

<div align="center">
  <h2>Usage Examples</h2>
</div>

<div align="center">

### Automation: Notify When Print Completes

</div>

```yaml
automation:
  - alias: "3D Print Complete Notification"
    trigger:
      - platform: state
        entity_id: binary_sensor.flashforge_printing
        from: "on"
        to: "off"
    action:
      - service: notify.mobile_app
        data:
          title: "Print Complete"
          message: "{{ states('sensor.flashforge_current_file') }} finished printing!"
```

<div align="center">

### Automation: Alert on Print Error

</div>

```yaml
automation:
  - alias: "3D Printer Error Alert"
    trigger:
      - platform: state
        entity_id: binary_sensor.flashforge_error
        to: "on"
    action:
      - service: notify.mobile_app
        data:
          title: "Printer Error"
          message: "FlashForge printer has encountered an error!"
          data:
            priority: high
```

<div align="center">

### Automation: Turn Off LED When Print Finishes

</div>

```yaml
automation:
  - alias: "Turn Off Printer LED After Print"
    trigger:
      - platform: state
        entity_id: binary_sensor.flashforge_printing
        from: "on"
        to: "off"
    action:
      - service: switch.turn_off
        target:
          entity_id: switch.flashforge_led
```

<div align="center">

### Lovelace Card Example

</div>

```yaml
type: entities
title: FlashForge Printer
entities:
  - entity: sensor.flashforge_machine_status
  - entity: binary_sensor.flashforge_printing
  - entity: sensor.flashforge_print_progress
  - entity: sensor.flashforge_nozzle_temperature
  - entity: sensor.flashforge_bed_temperature
  - entity: sensor.flashforge_remaining_time
  - type: divider
  - entity: button.flashforge_pause_print
  - entity: button.flashforge_resume_print
  - entity: button.flashforge_cancel_print
  - entity: button.flashforge_clear_status
  - type: divider
  - entity: switch.flashforge_led
  - entity: switch.flashforge_camera
  - entity: select.flashforge_filtration_mode
```

<div align="center">

### Camera Card

</div>

```yaml
type: picture-glance
camera_image: camera.flashforge_camera
entities:
  - binary_sensor.flashforge_printing
  - sensor.flashforge_print_progress
```



<div align="center">
  <h2>Troubleshooting</h2>
</div>

<div align="center">

| Issue | Problem | Solutions |
|-------|---------|-----------|
| **Discovery Not Finding Printer** | Automatic discovery doesn't detect your printer | • Ensure printer is on the same network/subnet as Home Assistant<br>• Check firewall settings (UDP port 18007 must be open)<br>• Verify LAN mode is enabled on the printer<br>• Try manual configuration with IP address |
| **Connection Failed During Setup** | Setup fails with connection error | • Verify printer has LAN mode enabled<br>• Check the check code is correct (codes can expire)<br>• Ensure printer is powered on and connected to network<br>• Test API access manually: `http://<PRINTER_IP>:8898/info`<br>• Verify the serial number includes the `SN` prefix and matches the value shown on the printer settings screen |
| **Entities Show "Unavailable"** | Integration installed but entities are unavailable | • Check printer is online and reachable<br>• Verify credentials are still valid<br>• Reload the integration: Settings → Integrations → FlashForge → ⋮ → Reload<br>• Check Home Assistant logs for connection errors |
| **Camera Entity Unavailable** | The camera entity shows unavailable | • The camera entity is always created, but it only becomes available when the printer reports an active OEM camera stream URL or the standard OEM fallback stream endpoint responds<br>• Verify the OEM camera is installed and enabled on the printer<br>• The `switch.flashforge_camera` power control remains Pro-only |
| **Remaining / Completion Time Missing or Wrong** | `sensor.flashforge_remaining_time` stays at `0` and `sensor.flashforge_print_completion_time` stays `unknown` during an active print | • FlashForge firmware only calculates an ETA when the sliced file carries its own print-time metadata, which is written by FlashForge's OrcaSlicer fork and FlashPrint but **not** by regular OrcaSlicer or similar slicers<br>• Without it the printer reports `estimatedTime: 0` over the API, so there is no accurate value for the integration to display<br>• The printer's own screen still shows a time because it reads the file directly — that isn't exposed over the HTTP API<br>• Fix: run [orca2flashforge](https://github.com/GhostTypes/orca2flashforge) as a post-processing script in your slicer to add the metadata FlashForge firmware expects |
| **Python API Not Installing** | Integration fails due to missing flashforge-python-api | • Verify Home Assistant has internet access<br>• Check PyPI is reachable: https://pypi.org/project/flashforge-python-api/<br>• Try manual install: `pip install flashforge-python-api` in HA environment<br>• Restart Home Assistant after installation |
| **Static IP Recommended** | - | For best reliability, assign a static IP address to your printer in your router's DHCP settings. This prevents connection issues if the printer's IP changes. |

</div>



<div align="center">
  <h2>Related Projects</h2>
</div>

<div align="center">
<table>
  <tr>
    <th>Project</th>
    <th>Description</th>
    <th>Link</th>
  </tr>
  <tr>
    <td>Python API Library</td>
    <td>Core HTTP API client for FlashForge printers</td>
    <td><a href="https://github.com/GhostTypes/ff-5mp-api-py">ff-5mp-api-py</a></td>
  </tr>
  <tr>
    <td>TypeScript API Library</td>
    <td>TypeScript/JavaScript API client</td>
    <td><a href="https://github.com/GhostTypes/ff-5mp-api-ts">ff-5mp-api-ts</a></td>
  </tr>
  <tr>
    <td>FlashForgeUI</td>
    <td>Cross-platform monitoring & control application</td>
    <td><a href="https://github.com/Parallel-7/FlashForgeUI-Electron">FlashForgeUI-Electron</a></td>
  </tr>
</table>
</div>



<div align="center">
  <h2>License</h2>
</div>

<div align="center">
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
</div>



<div align="center">
  <p><b>If you find this integration useful, please star the repository!</b></p>
</div>
