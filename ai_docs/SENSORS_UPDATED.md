# Sensor Updates - HTTP API Accurate Implementation

## Changes Made

### ✅ Fixed Field Names (Breaking Change!)

All sensors now use the correct `FFMachineInfo` field names from the Python API:

**Old (WRONG) → New (CORRECT):**
- `data.MachineStatus` → `data.machine_state`
- `data.CurrentNozzleTemp` → `data.extruder.current`
- `data.TargetNozzleTemp` → `data.extruder.set`
- `data.CurrentBedTemp` → `data.print_bed.current`
- `data.TargetBedTemp` → `data.print_bed.set`
- `data.PrintProgress` → `data.print_progress`
- `data.CurrentFile` → `data.print_file_name`
- `data.CurrentLayer` → `data.current_print_layer`
- `data.TotalLayers` → `data.total_print_layers`
- `data.ElapsedTime` → `data.print_duration`
- `data.RemainingTime` → Calculated: `(estimated_time - print_duration)`
- `data.MoveMode` → **REMOVED** (not in HTTP API!)

### ✅ Added New Sensors (6 total)

Based on FlashForgeUI-Electron and `FFMachineInfo` model:

1. **Filament Length** (meters)
   - Field: `data.est_length`
   - Unit: m
   - Icon: mdi:ruler

2. **Filament Weight** (grams)
   - Field: `data.est_weight`
   - Unit: g
   - Icon: mdi:weight-gram

3. **Print Speed** (percentage)
   - Field: `data.print_speed_adjust`
   - Unit: %
   - Icon: mdi:speedometer

4. **Z-Axis Offset** (mm)
   - Field: `data.z_axis_compensation`
   - Unit: mm
   - Icon: mdi:format-vertical-align-center

5. **Nozzle Size**
   - Field: `data.nozzle_size`
   - Icon: mdi:printer-3d-nozzle

6. **Filament Type**
   - Field: `data.filament_type`
   - Icon: mdi:printer-3d-nozzle-heat

### ✅ Fixed Remaining Time Calculation

**Old (Incorrect):**
```python
value_fn=lambda data: data.RemainingTime  # Field doesn't exist!
```

**New (Correct):**
```python
value_fn=lambda data: max(0, (data.estimated_time or 0) - (data.print_duration or 0)) if data.estimated_time else 0
```

Now accurately calculates: **estimated total time - elapsed time = remaining time**

## New Complete Sensor List (18 total)

### Core Print Status (12 sensors)
1. Machine Status (READY, PRINTING, PAUSED, etc.)
2. Nozzle Temperature (°C)
3. Nozzle Target Temperature (°C)
4. Bed Temperature (°C)
5. Bed Target Temperature (°C)
6. Print Progress (%)
7. Current File
8. Current Layer
9. Total Layers
10. Elapsed Time (seconds)
11. Remaining Time (seconds) - **NOW ACCURATE!**
12. ~~Move Mode~~ - **REMOVED** (not in HTTP API)

### New Print Info Sensors (6 sensors)
13. Filament Length (m) - **NEW!**
14. Filament Weight (g) - **NEW!**
15. Print Speed (%) - **NEW!**
16. Z-Axis Offset (mm) - **NEW!**
17. Nozzle Size - **NEW!**
18. Filament Type - **NEW!**

## Total Entity Count Update

**Old:** 23 entities (12 sensors + 4 binary + 2 switches + 4 buttons + 1 camera)
**New:** 28 entities (18 sensors + 4 binary + 2 switches + 3 buttons + 1 camera)

**Breakdown:**
- **Sensors:** 12 → 18 (+6 new, -1 removed = +5 net)
- **Binary Sensors:** 4 (unchanged)
- **Switches:** 2 (unchanged)
- **Buttons:** 4 → 3 (-1 home axes)
- **Camera:** 1 (unchanged)

## Matching FlashForgeUI-Electron

The new sensors now match what the Electron app displays:

**Printer Status Panel:**
- ✅ Machine state
- ✅ Runtime (elapsed_time)
- ✅ Filament used (filament_length in meters)

**Additional Info Panel:**
- ✅ Nozzle size
- ✅ Filament type
- ✅ Speed offset
- ✅ Z-axis offset

**Job Info Panel:**
- ✅ Current job name
- ✅ Progress percentage
- ✅ Estimated/remaining time

## HTTP API Only

All sensors use **only HTTP API fields** from the `/status` endpoint:

- ✅ `data.machine_state` (from `status` field)
- ✅ `data.extruder` (Temperature model)
- ✅ `data.print_bed` (Temperature model)
- ✅ `data.print_progress`
- ✅ `data.print_file_name`
- ✅ `data.current_print_layer`
- ✅ `data.total_print_layers`
- ✅ `data.print_duration`
- ✅ `data.estimated_time`
- ✅ `data.est_length`
- ✅ `data.est_weight`
- ✅ `data.print_speed_adjust`
- ✅ `data.z_axis_compensation`
- ✅ `data.nozzle_size`
- ✅ `data.filament_type`

**Zero TCP fields used!**

## Testing Priority

When testing, verify these new sensors:

1. **Filament metrics update during print**
   - Length in meters
   - Weight in grams

2. **Print speed shows current adjustment**
   - Default 100%
   - Updates if user changes speed on printer

3. **Z-offset shows compensation value**
   - Typically -0.XXX to +0.XXX mm

4. **Nozzle size and filament type populated**
   - From printer configuration

5. **Remaining time decreases as print progresses**
   - Should be: estimated_time - print_duration
   - Should hit 0 when print completes

## Breaking Changes

⚠️ **All sensor field names changed!**

If anyone was already using this integration (unlikely since it's brand new), they would need to:
- Delete the integration
- Restart Home Assistant
- Re-add the integration

The entity unique IDs are the same, but internal field mappings changed.

## Implementation Notes

- **Rounded values:** Filament sensors round to 2 decimals, z-offset to 3
- **Default fallbacks:** All sensors return 0 or "Unknown" if data unavailable
- **Type safety:** Using proper Pydantic models from ff-5mp-api-py
- **State classes:** Numeric sensors have `SensorStateClass.MEASUREMENT` for statistics

---

**Status:** ✅ Complete
**Tested:** Needs real printer validation
**API:** 100% HTTP only
**Entity Count:** 28 total
