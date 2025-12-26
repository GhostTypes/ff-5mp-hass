# Source: https://developers.home-assistant.io/docs/intent_builtin

The following intents are **supported**:

* HassTurnOn, HassTurnOff, HassGetState, HassNevermind, HassRespond, HassBroadcast, HassSetPosition, HassGetCurrentDate, HassGetCurrentTime, HassLightSet, HassClimateSetTemperature, HassClimateGetTemperature, HassShoppingListAddItem, HassShoppingListCompleteItem, HassGetWeather, HassListAddItem, HassListCompleteItem, HassVacuumStart, HassVacuumReturnToBase, HassMediaPause, HassMediaUnpause, HassMediaNext, HassMediaPrevious, HassSetVolume, HassMediaPlayerMute, HassMediaPlayerUnmute, HassSetVolumeRelative, HassMediaSearchAndPlay, HassStartTimer, HassCancelAllTimers, HassCancelTimer, HassIncreaseTimer, HassDecreaseTimer, HassPauseTimer, HassUnpauseTimer, HassTimerStatus, HassFanSetSpeed, HassLawnMowerStartMowing, HassLawnMowerDock

The following intents are **deprecated**:

* HassOpenCover, HassCloseCover, HassToggle, HassHumidifierSetpoint, HassHumidifierMode, HassShoppingListLastItems

**Slots**

For *HassTurnOn* and *HassTurnOff*, the *slots* are optional.

Possible slot combinations are:

| Slot combination | Example |
| --- | --- |
| name only | table light |
| area only | kitchen |
| area and name | living room reading light |
| area and domain | kitchen lights |
| area and device class | bathroom humidity |
| device class and domain | carbon dioxide sensors |

## Supported intents

### HassTurnOn

Turns on a device or entity

* **name** - Name of a device or entity
* **area** - Name of an area
* **floor** - Name of a floor
* **domain** - Domain of devices/entities in an area
* **device\_class** - Device class of devices/entities in an area

[Provided by the `homeassistant` integration.](https://www.home-assistant.io/integrations/homeassistant)

### HassTurnOff

Turns off a device or entity

* **name** - Name of a device or entity
* **area** - Name of an area
* **floor** - Name of a floor
* **domain** - Domain of devices/entities in an area
* **device\_class** - Device class of devices/entities in an area

[Provided by the `homeassistant` integration.](https://www.home-assistant.io/integrations/homeassistant)

### HassGetState

Gets or checks the state of an entity

* **name** - Name of a device or entity
* **area** - Name of an area
* **floor** - Name of a floor
* **domain** - Domain of devices/entities in an area
* **device\_class** - Device class of devices/entities in an area
* **state** - Name of state to match

[Provided by the `homeassistant` integration.](https://www.home-assistant.io/integrations/homeassistant)

### HassNevermind

Does nothing. Used to cancel a request

[Provided by the `homeassistant` integration.](https://www.home-assistant.io/integrations/homeassistant)

### HassRespond

Returns response but takes no action

* **response** - Text to respond with

[Provided by the `homeassistant` integration.](https://www.home-assistant.io/integrations/homeassistant)

### HassBroadcast

Announces a message on other satellites

* **message** - Message to broadcast (required)

[Provided by the `assist_satellite` integration.](https://www.home-assistant.io/integrations/assist_satellite)

### HassSetPosition

Sets the position of an entity

* **name** - Name of a device or entity
* **area** - Name of an area
* **floor** - Name of a floor
* **domain** - Domain of devices/entities in an area
* **device\_class** - Device class of devices/entities in an area
* **position** - Position from 0 to 100 (required)

[Provided by the `homeassistant` integration.](https://www.home-assistant.io/integrations/homeassistant)

### HassGetCurrentDate

Gets the current date

[Provided by the `homeassistant` integration.](https://www.home-assistant.io/integrations/homeassistant)

### HassGetCurrentTime

Gets the current time

[Provided by the `homeassistant` integration.](https://www.home-assistant.io/integrations/homeassistant)

### HassLightSet

Sets the brightness or color of a light

* **name** - Name of a device or entity
* **area** - Name of an area
* **floor** - Name of a floor
* **brightness** - Brightness percentage from 0 to 100
* **color** - Name of color

[Provided by the `light` integration.](https://www.home-assistant.io/integrations/light)

### HassClimateSetTemperature

Sets the desired indoor temperature

* **name** - Name of a device or entity
* **area** - Name of an area
* **floor** - Name of a floor
* **temperature** - Temperature in degrees (required)

[Provided by the `climate` integration.](https://www.home-assistant.io/integrations/climate)

### HassClimateGetTemperature

Gets the actual indoor temperature (not the desired indoor temperature as set by HassClimateSetTemperature)

* **name** - Name of a device or entity
* **area** - Name of an area
* **floor** - Name of a floor

[Provided by the `climate` integration.](https://www.home-assistant.io/integrations/climate)

### HassShoppingListAddItem

Adds an item to the shopping list

* **item** - Item to add (required)

[Provided by the `shopping_list` integration.](https://www.home-assistant.io/integrations/shopping_list)

### HassShoppingListCompleteItem

Checks off an item from the shopping list

* **item** - Item to check off (required)

[Provided by the `shopping_list` integration.](https://www.home-assistant.io/integrations/shopping_list)

### HassGetWeather

Gets the current weather

* **name** - Name of the weather entity to use

[Provided by the `weather` integration.](https://www.home-assistant.io/integrations/weather)

### HassListAddItem

Adds an item to a todo list

* **item** - Item to add (required)
* **name** - Name of the list (required)

[Provided by the `todo` integration.](https://www.home-assistant.io/integrations/todo)

### HassListCompleteItem

Checks off an item from a todo list

* **item** - Item to check off (required)
* **name** - Name of the list (required)

[Provided by the `todo` integration.](https://www.home-assistant.io/integrations/todo)

### HassVacuumStart

Starts a vacuum

* **name** - Name of a device or entity
* **area** - Name of an area
* **floor** - Name of a floor

[Provided by the `vacuum` integration.](https://www.home-assistant.io/integrations/vacuum)

### HassVacuumReturnToBase

Returns a vacuum to base

* **name** - Name of a device or entity
* **area** - Name of an area

[Provided by the `vacuum` integration.](https://www.home-assistant.io/integrations/vacuum)

### HassMediaPause

Pauses a media player

* **name** - Name of a device or entity
* **area** - Name of an area

[Provided by the `media_player` integration.](https://www.home-assistant.io/integrations/media_player)

### HassMediaUnpause

Unpauses a media player

* **name** - Name of a device or entity
* **area** - Name of an area

[Provided by the `media_player` integration.](https://www.home-assistant.io/integrations/media_player)

### HassMediaNext

Skips a media player to the next item

* **name** - Name of a device or entity
* **area** - Name of an area

[Provided by the `media_player` integration.](https://www.home-assistant.io/integrations/media_player)

### HassMediaPrevious

Skips a media player back to the previous item

* **name** - Name of a device or entity
* **area** - Name of an area

[Provided by the `media_player` integration.](https://www.home-assistant.io/integrations/media_player)

### HassSetVolume

Sets the volume of a media player

* **name** - Name of a device or entity
* **area** - Name of an area
* **volume\_level** - Volume level from 0 to 100 (required)

[Provided by the `media_player` integration.](https://www.home-assistant.io/integrations/media_player)

### HassMediaPlayerMute

Mutes a media player

* **name** - Name of a device or entity

[Provided by the `media_player` integration.](https://www.home-assistant.io/integrations/media_player)

### HassMediaPlayerUnmute

Unmutes a media player

* **name** - Name of a device or entity

[Provided by the `media_player` integration.](https://www.home-assistant.io/integrations/media_player)

### HassSetVolumeRelative

Increases or decreases the volume of a media player

* **volume\_step** - up, down, or the percentage to change from -100 to 100 (required)
* **name** - Name of a device or entity
* **area** - Name of an area
* **floor** - Name of a floor

[Provided by the `media_player` integration.](https://www.home-assistant.io/integrations/media_player)

### HassMediaSearchAndPlay

Searched for a media item and plays it

* **name** - Name of a device or entity
* **area** - Name of an area
* **search\_query** - Media to search for and play (required)
* **media\_class** - Type of media to search for (album, app, artist, channel, composer, contributing\_artist, directory, episode, game, genre, image, movie, music, playlist, podcast, season, track, tv\_show, url, video)

[Provided by the `media_player` integration.](https://www.home-assistant.io/integrations/media_player)

### HassStartTimer

Starts a timer

* **hours** - Number of hours
* **minutes** - Number of minutes
* **seconds** - Number of seconds
* **name** - Name attached to the timer
* **conversation\_command** - Command to execute when timer finishes

[Provided by the `homeassistant` integration.](https://www.home-assistant.io/integrations/homeassistant)

### HassCancelAllTimers

Cancels all timers

* **area** - Area of the device used to start the timer

[Provided by the `homeassistant` integration.](https://www.home-assistant.io/integrations/homeassistant)

### HassCancelTimer

Cancels a timer

* **start\_hours** - Hours the timer was started with
* **start\_minutes** - Minutes the timer was started with
* **start\_seconds** - Seconds the timer was started with
* **name** - Name attached to the timer
* **area** - Area of the device used to start the timer

[Provided by the `homeassistant` integration.](https://www.home-assistant.io/integrations/homeassistant)

### HassIncreaseTimer

Adds time to a timer

* **hours** - Number of hours
* **minutes** - Number of minutes
* **seconds** - Number of seconds
* **start\_hours** - Hours the timer was started with
* **start\_minutes** - Minutes the timer was started with
* **start\_seconds** - Seconds the timer was started with
* **name** - Name attached to the timer
* **area** - Area of the device used to start the timer

[Provided by the `homeassistant` integration.](https://www.home-assistant.io/integrations/homeassistant)

### HassDecreaseTimer

Removes time from a timer

* **hours** - Number of hours
* **minutes** - Number of minutes
* **seconds** - Number of seconds
* **start\_hours** - Hours the timer was started with
* **start\_minutes** - Minutes the timer was started with
* **start\_seconds** - Seconds the timer was started with
* **name** - Name attached to the timer
* **area** - Area of the device used to start the timer

[Provided by the `homeassistant` integration.](https://www.home-assistant.io/integrations/homeassistant)

### HassPauseTimer

Pauses a running timer

* **start\_hours** - Hours the timer was started with
* **start\_minutes** - Minutes the timer was started with
* **start\_seconds** - Seconds the timer was started with
* **name** - Name attached to the timer
* **area** - Area of the device used to start the timer

[Provided by the `homeassistant` integration.](https://www.home-assistant.io/integrations/homeassistant)

### HassUnpauseTimer

Resumes a paused timer

* **start\_hours** - Hours the timer was started with
* **start\_minutes** - Minutes the timer was started with
* **start\_seconds** - Seconds the timer was started with
* **name** - Name attached to the timer
* **area** - Area of the device used to start the timer

[Provided by the `homeassistant` integration.](https://www.home-assistant.io/integrations/homeassistant)

### HassTimerStatus

Reports status of one or more timers

* **start\_hours** - Hours the timer was started with
* **start\_minutes** - Minutes the timer was started with
* **start\_seconds** - Seconds the timer was started with
* **name** - Name attached to the timer
* **area** - Area of the device used to start the timer

[Provided by the `homeassistant` integration.](https://www.home-assistant.io/integrations/homeassistant)

### HassFanSetSpeed

Set the speed of a fan

* **name** - Name of a device or entity
* **area** - Name of an area
* **floor** - Name of a floor
* **percentage** - Speed percentage from 0 to 100 (required)

[Provided by the `fan` integration.](https://www.home-assistant.io/integrations/fan)

### HassLawnMowerStartMowing

Starts a lawn mower

* **name** - Name of a device or entity

[Provided by the `lawn_mower` integration.](https://www.home-assistant.io/integrations/lawn_mower)

### HassLawnMowerDock

Sends a lawn mower to dock

* **name** - Name of a device or entity

[Provided by the `lawn_mower` integration.](https://www.home-assistant.io/integrations/lawn_mower)

## Deprecated intents

These are old intents that are not supported by template matching sentences and are planned to be removed or replaced.

### HassOpenCover

*Deprecated; use `HassTurnOn` instead.*

Open a cover.

| Slot name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the cover entity to open. |

### HassCloseCover

*Deprecated; use `HassTurnOff` instead.*

Close a cover.

| Slot name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the cover entity to close. |

### HassToggle

Toggle the state of an entity.

| Slot name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the entity to toggle. |

### HassHumidifierSetpoint

Set target humidity.

| Slot name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the entity to control. |
| humidity | integer, 0-100 | Yes | Target humidity to set. |

### HassHumidifierMode

Set humidifier mode if supported by the humidifier.

| Slot name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the entity to control. |
| mode | string | Yes | The mode to switch to. |

### HassShoppingListLastItems

List the last 5 items on the shopping list.

*This intent has no slots.*

[This page is automatically generated based on the Intents repository.](https://github.com/home-assistant/intents/blob/main/intents.yaml)