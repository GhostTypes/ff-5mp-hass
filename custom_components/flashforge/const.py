"""Constants for the FlashForge integration."""

DOMAIN = "flashforge"

# Configuration keys
CONF_SERIAL_NUMBER = "serial_number"
CONF_CHECK_CODE = "check_code"
CONF_SCAN_INTERVAL = "scan_interval"
CONF_OVERRIDE_LED_AVAILABILITY = "override_led_availability"

# Default values
DEFAULT_NAME = "FlashForge Printer"
DEFAULT_SCAN_INTERVAL = 10  # seconds
DEFAULT_HTTP_PORT = 8898
DEFAULT_CAMERA_PORT = 8080

# Entity keys
ATTR_MACHINE_STATUS = "machine_status"
ATTR_MOVE_MODE = "move_mode"
ATTR_CURRENT_FILE = "current_file"
ATTR_LAYER = "layer"
ATTR_TOTAL_LAYERS = "total_layers"
ATTR_PRINT_PROGRESS = "print_progress"
ATTR_ELAPSED_TIME = "elapsed_time"
ATTR_REMAINING_TIME = "remaining_time"

# Printer states
STATE_IDLE = "READY"
STATE_PRINTING = "BUILDING_FROM_SD"
STATE_PAUSED = "PAUSED"
STATE_ERROR = "ERROR"
