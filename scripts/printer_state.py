#!/usr/bin/env python3
"""Watch what the printer reports, and what the integration makes of it.

Written for a specific failure and kept for the next one: a Creator 5 Pro
detects a clog, pauses, and the Machine Status sensor goes to "unknown". The
sensor is an enum fed by the library's `MachineState`, which maps a fixed set of
raw status strings and falls back to UNKNOWN for the rest - so an unmapped value
is indistinguishable from a printer that reported nothing at all.

This prints the raw status beside the mapped one and flags anything unmapped, so
the cause is visible while it happens instead of being reconstructed afterwards.
The library also logs `Unknown machine status received` for each occurrence; if
you have the Home Assistant log, grep it for that first.

Standard library only: no dependency on the integration, its virtualenv, or the
API library, so this can be dropped onto any machine that can reach the printer.

Usage (from the repository root):

    python scripts/printer_state.py --ip 192.168.1.50 --serial SN123 --check-code ABCD
    python scripts/printer_state.py --ha-config /config          # read credentials from HA
    python scripts/printer_state.py --watch                      # poll until Ctrl+C
    python scripts/printer_state.py --watch --log clog.jsonl     # and keep every sample
    python scripts/printer_state.py --raw                        # full /detail payload

Credentials may also come from the environment: FF_IP, FF_SERIAL, FF_CHECK_CODE.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path

HTTP_PORT = 8898

# Mirrored from flashforge/api/controls/info.py `_get_machine_state`. Anything
# the printer reports that is not in here becomes MachineState.UNKNOWN, which
# Home Assistant renders as "unknown". Keep this list in step with the library;
# a value that appears here but not there is exactly the bug this script hunts.
KNOWN_STATUS = {
    "ready": "READY",
    "busy": "BUSY",
    "calibrate_doing": "CALIBRATING",
    "error": "ERROR",
    "heating": "HEATING",
    "printing": "PRINTING",
    "pausing": "PAUSING",
    "pause": "PAUSED",
    "paused": "PAUSED",
    "cancel": "CANCELLED",
    "completed": "COMPLETED",
    "downloading": "BUSY",
}


def credentials_from_ha(config_dir: str) -> dict[str, str]:
    """Read ip / serial / check code out of Home Assistant's config entry.

    Saves keeping a second copy of the check code, and cannot drift out of step
    with the integration, because it is the same value the integration uses.
    """
    store = Path(config_dir) / ".storage" / "core.config_entries"
    try:
        data = json.loads(store.read_text(encoding="utf-8"))
    except OSError as err:
        sys.exit(f"Could not read {store}: {err}")

    for entry in data.get("data", {}).get("entries", []):
        if entry.get("domain") == "flashforge":
            payload = entry["data"]
            return {
                "ip": payload["ip_address"],
                "serial": payload["serial_number"],
                "check_code": payload["check_code"],
                "name": entry.get("title") or "FlashForge",
            }
    sys.exit(f"No FlashForge config entry found in {store}")


def fetch_detail(creds: dict[str, str], timeout: float = 10.0) -> dict:
    """POST /detail and return the parsed payload."""
    payload = json.dumps(
        {"serialNumber": creds["serial"], "checkCode": creds["check_code"]}
    ).encode()
    request = urllib.request.Request(
        f"http://{creds['ip']}:{HTTP_PORT}/detail",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read())


def summarize(detail: dict) -> dict:
    """Pull out the fields that matter when the printer stops doing what it should."""
    d = detail.get("detail", {}) if isinstance(detail, dict) else {}
    status = d.get("status", "")
    return {
        "status": status,
        "mapped": KNOWN_STATUS.get(str(status).lower(), "UNKNOWN"),
        "known": str(status).lower() in KNOWN_STATUS,
        "error_code": d.get("errorCode", ""),
        "file": d.get("printFileName", ""),
        "progress": d.get("printProgress"),
        "layer": d.get("printLayer"),
        "layers": d.get("targetPrintLayer"),
        "nozzle_temps": d.get("nozzleTemps"),
        "bed": d.get("platTemp"),
        "bed_target": d.get("platTargetTemp"),
        "chamber": d.get("chamberTemp"),
        "door": d.get("doorStatus"),
        "firmware": d.get("firmwareVersion"),
        "active_slot": (d.get("matlStationInfo") or {}).get("currentSlot"),
    }


def format_line(now: str, s: dict) -> str:
    progress = (
        f"{float(s['progress']) * 100:5.1f}%" if s["progress"] is not None else "    - "
    )
    layers = f"{s['layer']}/{s['layers']}" if s["layers"] else "-"
    error = (
        f"  err={s['error_code']}" if s["error_code"] not in ("", "0", None) else ""
    )
    unmapped = "" if s["known"] else "  <== UNMAPPED, Home Assistant shows 'unknown'"
    return (
        f"{now}  {str(s['status']):<12} -> {s['mapped']:<11}"
        f" {progress} {layers:>9}  bed {s['bed']}/{s['bed_target']}"
        f"{error}{unmapped}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ip", default=os.environ.get("FF_IP"))
    parser.add_argument("--serial", default=os.environ.get("FF_SERIAL"))
    parser.add_argument("--check-code", default=os.environ.get("FF_CHECK_CODE"))
    parser.add_argument(
        "--ha-config",
        metavar="DIR",
        help="read the credentials from this Home Assistant config directory",
    )
    parser.add_argument("--watch", action="store_true", help="poll until interrupted")
    parser.add_argument(
        "--interval", type=float, default=10.0, help="seconds between polls"
    )
    parser.add_argument("--raw", action="store_true", help="dump the whole /detail payload")
    parser.add_argument("--log", metavar="FILE", help="append one JSON object per poll")
    args = parser.parse_args()

    if args.ha_config:
        creds = credentials_from_ha(args.ha_config)
    elif args.ip and args.serial and args.check_code:
        creds = {
            "ip": args.ip,
            "serial": args.serial,
            "check_code": args.check_code,
            "name": "FlashForge",
        }
    else:
        parser.error(
            "need --ip, --serial and --check-code (or FF_* env vars), or --ha-config"
        )

    print(f"{creds['name']} @ {creds['ip']}\n")

    log = Path(args.log).open("a", encoding="utf-8") if args.log else None
    previous = None

    try:
        while True:
            now = datetime.now().strftime("%H:%M:%S")
            try:
                detail = fetch_detail(creds)
            except Exception as err:  # noqa: BLE001 - a probe reports, it does not raise
                print(f"{now}  printer unreachable: {err}")
                if not args.watch:
                    return
                time.sleep(args.interval)
                continue

            summary = summarize(detail)

            if args.raw:
                print(json.dumps(detail, indent=2, ensure_ascii=False))

            # In watch mode only changes are printed: a status that repeats for
            # an hour must not bury the moment it changed. The log keeps
            # everything regardless.
            state = (summary["status"], summary["error_code"])
            if not args.watch or state != previous:
                print(format_line(now, summary))
                previous = state

            if log:
                log.write(
                    json.dumps({"time": datetime.now().isoformat(), **summary}) + "\n"
                )
                log.flush()

            if not args.watch:
                return
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        if log:
            log.close()


if __name__ == "__main__":
    main()
