"""Constants for the FlashForge integration."""

DOMAIN = "flashforge"

# Configuration keys
CONF_SERIAL_NUMBER = "serial_number"
CONF_CHECK_CODE = "check_code"
CONF_SCAN_INTERVAL = "scan_interval"
CONF_OVERRIDE_LED_AVAILABILITY = "override_led_availability"
CONF_LEVELING_BEFORE_PRINT = "leveling_before_print"

# Default values
DEFAULT_NAME = "FlashForge Printer"
DEFAULT_SCAN_INTERVAL = 10  # seconds
DEFAULT_HTTP_PORT = 8898
DEFAULT_CAMERA_PORT = 8080
DEFAULT_LEVELING_BEFORE_PRINT = False

# The printer's local file list changes only when a file is uploaded or deleted,
# so it is polled on its own, slower schedule than the machine state.
FILE_LIST_SCAN_INTERVAL = 60  # seconds

# Services
SERVICE_PRINT_FILE = "print_file"
ATTR_FILE_NAME = "file_name"
ATTR_LEVELING_BEFORE_PRINT = "leveling_before_print"

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

MANUFACTURER = "FlashForge"

PRINTER_MODEL_NAMES: dict[int, str] = {
    35: "Adventurer 5M",
    36: "Adventurer 5M Pro",
    38: "AD5X",
    40: "Creator 5",
    41: "Creator 5 Pro",
}
SUPPORTED_PIDS = frozenset(PRINTER_MODEL_NAMES)
