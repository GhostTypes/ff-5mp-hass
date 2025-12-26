# Entity Platform Development Reference

This reference covers the development of entity platforms in Home Assistant. For detailed information on specific entity types, consult the corresponding files.

## Overview

Home Assistant supports 47+ different entity platform types. Each entity type has specific properties, device classes, and behaviors.

## Core Entity Types

### Most Common Platforms

**Sensor** - Read-only entities providing measurements
- Source: `assets/docs/core/entity/sensor.md`
- Device classes: temperature, humidity, power, energy, etc.
- State classes: measurement, total, total_increasing

**Binary Sensor** - Read-only entities with on/off states
- Source: `assets/docs/core/entity/binary-sensor.md`
- Device classes: motion, door, window, moisture, etc.

**Switch** - Controllable on/off entities
- Source: `assets/docs/core/entity/switch.md`
- Simple binary control with turn_on/turn_off services

**Light** - Controllable lighting entities
- Source: `assets/docs/core/entity/light.md`
- Supports brightness, color, effects
- Color modes: RGB, HS, XY, color temp, white

**Climate** - HVAC control entities
- Source: `assets/docs/core/entity/climate.md`
- HVAC modes, temperature control, presets
- Supports heating, cooling, heat/cool, auto, etc.

### Media & Entertainment

**Media Player** - Audio/video playback control
- Source: `assets/docs/core/entity/media-player.md`
- Supports play, pause, volume, source selection
- Media browsing capabilities

**Camera** - Image/video streaming
- Source: `assets/docs/core/entity/camera.md`
- Still image snapshots and streaming

### Covers & Physical Controls

**Cover** - Window coverings, garage doors, etc.
- Source: `assets/docs/core/entity/cover.md`
- Open, close, stop, position control
- Device classes: blind, curtain, garage, gate, shade, shutter, etc.

**Lock** - Physical lock control
- Source: `assets/docs/core/entity/lock.md`
- Lock and unlock operations
- Optional code entry support

**Fan** - Fan control
- Source: `assets/docs/core/entity/fan.md`
- Speed control, direction, oscillation
- Preset modes

**Vacuum** - Vacuum cleaner control
- Source: `assets/docs/core/entity/vacuum.md`
- Start, stop, pause, return to base
- Cleaning modes and battery level

### Environmental & Sensors

**Weather** - Weather information
- Source: `assets/docs/core/entity/weather.md`
- Current conditions and forecast
- Temperature, humidity, pressure, wind, etc.

**Humidifier** - Humidity control
- Source: `assets/docs/core/entity/humidifier.md`
- Target humidity, modes

**Water Heater** - Water heating control
- Source: `assets/docs/core/entity/water-heater.md`
- Temperature control, operation modes

### Input & Configuration

**Number** - Numeric input
- Source: `assets/docs/core/entity/number.md`
- Min, max, step values
- Supports same device classes as sensor

**Select** - Dropdown selection
- Source: `assets/docs/core/entity/select.md`
- List of options for user selection

**Text** - Text input
- Source: `assets/docs/core/entity/text.md`
- Single or multi-line text entry

**Button** - Trigger button
- Source: `assets/docs/core/entity/button.md`
- Press action, no state

**Date/Time/Datetime** - Temporal inputs
- Sources: 
  - `assets/docs/core/entity/date.md`
  - `assets/docs/core/entity/time.md`
  - `assets/docs/core/entity/datetime.md`

### Automation & Organization

**Calendar** - Calendar events
- Source: `assets/docs/core/entity/calendar.md`
- Events with start/end times

**Todo** - Task lists
- Source: `assets/docs/core/entity/todo.md`
- Create, complete, update tasks

**Scene** - State snapshots
- Source: `assets/docs/core/entity/scene.md`
- Activate predefined states

**Event** - Discrete event entities
- Source: `assets/docs/core/entity/event.md`
- For events that occur at specific times

### Voice & AI

**STT (Speech-to-Text)**
- Source: `assets/docs/core/entity/stt.md`

**TTS (Text-to-Speech)**
- Source: `assets/docs/core/entity/tts.md`

**Conversation** - AI conversation agents
- Source: `assets/docs/core/entity/conversation.md`

**Wake Word** - Wake word detection
- Source: `assets/docs/core/entity/wake_word.md`

**Assist Satellite** - Voice assistant devices
- Source: `assets/docs/core/entity/assist-satellite.md`

### Specialized Types

**Alarm Control Panel**
- Source: `assets/docs/core/entity/alarm-control-panel.md`

**Update** - Software/firmware updates
- Source: `assets/docs/core/entity/update.md`

**Image** - Static or updating images
- Source: `assets/docs/core/entity/image.md`

**Notify** - Notification service
- Source: `assets/docs/core/entity/notify.md`

**Remote** - IR/RF remote control
- Source: `assets/docs/core/entity/remote.md`

**Siren** - Audible alerts
- Source: `assets/docs/core/entity/siren.md`

**Valve** - Valve control
- Source: `assets/docs/core/entity/valve.md`

**Device Tracker** - Location tracking
- Source: `assets/docs/core/entity/device-tracker.md`

**Lawn Mower** - Robotic lawn mower
- Source: `assets/docs/core/entity/lawn-mower.md`

**Air Quality**
- Source: `assets/docs/core/entity/air-quality.md`

**AI Task** - AI task execution
- Source: `assets/docs/core/entity/ai-task.md`

## Common Entity Properties

All entities should implement:
- `name` - Display name
- `unique_id` - Unique identifier for entity registry
- `device_info` - Link to device registry
- `entity_category` - config, diagnostic, or None

Many entities support:
- `available` - Entity availability
- `icon` - Icon override
- `entity_picture` - Image for entity
- `extra_state_attributes` - Additional data

## Entity Base Class

All entity platforms inherit from `homeassistant.helpers.entity.Entity` and platform-specific bases like:
- `SensorEntity`
- `BinarySensorEntity`
- `SwitchEntity`
- etc.

## Key Concepts

**State vs Attributes**
- State: Primary value (temperature, on/off, etc.)
- Attributes: Additional context (unit, mode, battery, etc.)

**Properties vs Methods**
- Use properties for data from memory
- Use `update()` or `async_update()` for I/O operations

**Entity Naming**
- Use `has_entity_name = True`
- Set `name` to describe function, not device
- Device name comes from device_info

## Documentation Locations

All entity platform documentation is in:
`assets/docs/core/entity/`

Use the file paths above to reference complete documentation for each platform type.
