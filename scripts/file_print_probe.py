#!/usr/bin/env python3
"""Probe the local-file-list / print-start feature against a real printer.

Runs the integration's own code paths (``print_job.build_material_mappings``,
``print_job.async_start_local_print``) without a Home Assistant runtime, so the
HTTP requests, the parsed file list, and the derived Material Station mappings
can be verified on real hardware from Windows.

Read-only unless ``--print`` is passed. ``--print`` reports the job start only -
the printer summary, file list, and the other dumps are skipped.

Usage (from the repository root):

    python scripts/file_print_probe.py --discover
    python scripts/file_print_probe.py --ip 192.168.1.50 --serial SN123 --check-code ABCD
    python scripts/file_print_probe.py --ip ... --raw
    python scripts/file_print_probe.py --ip ... --thumb benchy.3mf --thumb-out t.png
    python scripts/file_print_probe.py --ip ... --print benchy.3mf --yes

Credentials may also come from the environment: FF_IP, FF_SERIAL, FF_CHECK_CODE.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

# The integration modules import Home Assistant; borrow the test mocks so they
# can be imported outside a HA runtime.
from tests.ha_mocks import mock_homeassistant  # noqa: E402

mock_homeassistant()

from flashforge import (  # noqa: E402
    FiveMClientConnectionOptions,
    FlashForgeClient,
    PrinterDiscovery,
)
from flashforge.api.constants.endpoints import Endpoints  # noqa: E402
from flashforge.models.responses import GCodeListResponse  # noqa: E402
from pydantic import ValidationError  # noqa: E402

from custom_components.flashforge.print_job import (  # noqa: E402
    async_start_local_print,
    build_material_mappings,
    needs_material_station,
)
from homeassistant.exceptions import HomeAssistantError  # noqa: E402


def _fmt_duration(seconds: int | None) -> str:
    if not seconds:
        return "-"
    hours, rest = divmod(int(seconds), 3600)
    return f"{hours}h{rest // 60:02d}m"


async def discover() -> None:
    """List the printers answering the UDP discovery broadcast."""
    printers = await PrinterDiscovery().discover()
    if not printers:
        print("No printers answered the discovery broadcast.")
        return
    for printer in printers:
        print(
            f"  {printer.name or '<unnamed>'}  serial={printer.serial_number}  "
            f"ip={printer.ip_address}  model={getattr(printer, 'model', '?')}"
        )
    print("\nThe check code is only on the printer's LAN mode screen.")


async def connect(ip: str, serial: str, check_code: str) -> FlashForgeClient:
    """Set the client up the same way the integration's async_setup_entry does."""
    client = FlashForgeClient(
        ip_address=ip,
        serial_number=serial,
        check_code=check_code,
        options=FiveMClientConnectionOptions(),
    )
    try:
        info = await client.info.get()
        if info is None:
            raise SystemExit(f"No answer from {ip} - check IP, serial, and check code.")
        client.cache_details(info)
        if not await client.send_product_command():
            raise SystemExit("Printer rejected the credentials (check code).")
    except BaseException:
        await client.dispose()
        raise
    return client


def report_printer(client: FlashForgeClient, info) -> None:
    print("Printer")
    print(f"  model               {getattr(info, 'model', None)}  (pid={getattr(info, 'pid', None)})")
    print(f"  is_creator5         {client.is_creator5}")
    print(f"  is_creator5_pro     {client.is_creator5_pro}")
    print(f"  is_ad5x             {client.is_ad5x}")
    print(f"  http_only           {client.http_only}")
    print(f"  state               {getattr(info, 'machine_state', None)}")

    # Slot colors feed the material mappings below; capability flags belong in
    # scripts/capability_probe.py.
    station = getattr(info, "matl_station_info", None)
    for slot in getattr(station, "slot_infos", None) or []:
        print(
            f"    slot {getattr(slot, 'slot_id', '?')}: "
            f"material={getattr(slot, 'material_name', '') or '-'} "
            f"color={getattr(slot, 'material_color', '') or '-'} "
            f"loaded={getattr(slot, 'has_filament', None)}"
        )

    # Which print-start command async_start_local_print would pick.
    if client.is_creator5:
        route = "job_control.start_creator5_job"
    elif client.is_ad5x:
        route = "job_control.start_ad5x_{single,multi}_color_job"
    else:
        route = "job_control.print_local_file"
    print(f"  print command       {route}")


def _has_metadata(entry) -> bool:
    """Return True when the printer reported anything beyond the file name."""
    return bool(
        entry.printing_time
        or entry.total_filament_weight is not None
        or entry.gcode_tool_cnt is not None
        or entry.use_matl_station is not None
        or entry.gcode_tool_datas
    )


def report_files(entries, info) -> None:
    print(f"\nFiles reported by /gcodeList ({len(entries)})")
    if not entries:
        print("  <none> - upload a file to the printer first.")
        return

    for entry in entries:
        print(f"\n  {entry.gcode_file_name}")

        # Distinguish "the printer says no" from "the printer says nothing":
        # a names-only /gcodeList leaves every detail field unset, and calling
        # that a single-material file would be a claim we cannot make.
        if not _has_metadata(entry):
            print("    no metadata reported for this file (names-only /gcodeList)")
            print(
                "    mapping: unknown - the file is started without mappings and "
                "the printer uses the tool/slot assignment stored in it"
            )
            continue

        print(
            f"    print time {_fmt_duration(entry.printing_time)}   "
            f"filament {entry.total_filament_weight if entry.total_filament_weight is not None else '?'} g   "
            f"tools {entry.gcode_tool_cnt if entry.gcode_tool_cnt is not None else '?'}   "
            f"material station "
            f"{entry.use_matl_station if entry.use_matl_station is not None else '?'}"
        )
        for tool in entry.gcode_tool_datas or []:
            print(
                f"      tool {tool.tool_id} -> slot {tool.slot_id}  "
                f"{tool.material_name or '-'}  {tool.material_color or '-'}  "
                f"{tool.filament_weight} g"
            )

        if not needs_material_station(entry):
            print("    mapping: not needed (file does not use the material station)")
            continue
        try:
            mappings = build_material_mappings(entry, info)
        except HomeAssistantError as err:
            print(f"    mapping REFUSED: {err}")
            continue
        for mapping in mappings:
            print(
                f"    mapping: tool {mapping.tool_id} -> slot {mapping.slot_id}  "
                f"{mapping.material_name}  tool={mapping.tool_material_color}  "
                f"slot={mapping.slot_material_color}"
            )


async def report_thumbnail(client: FlashForgeClient, file_name: str, out: str | None) -> None:
    """Check whether /gcodeThumb serves a thumbnail for an arbitrary stored file.

    The integration only ever asks for the *currently printing* file. The
    Creator 5 lists /gcodeThumb among its endpoints, so a per-file preview may
    be possible even on printers whose /gcodeList carries no metadata.
    """
    print(f"\nRequesting {Endpoints.GCODE_THUMB} for '{file_name}'")
    data = await client.files.get_gcode_thumbnail(file_name)
    if not data:
        print("  no thumbnail returned (endpoint unsupported, or none stored).")
        return

    kind = "PNG" if data[:8] == b"\x89PNG\r\n\x1a\n" else f"unknown ({data[:8]!r})"
    print(f"  received {len(data)} bytes, format: {kind}")
    if out:
        Path(out).write_bytes(data)
        print(f"  written to {out}")


async def report_raw(client: FlashForgeClient) -> None:
    """Dump the untouched /gcodeList payload and how the library models parse it.

    Both GCodeListResponse and FFGcodeFileEntry are ``extra="forbid"``: a single
    unexpected field makes the library fall back to a names-only list and drop
    all per-file metadata. This shows whether that is happening.
    """
    payload = {
        "serialNumber": client.serial_number,
        "checkCode": client.check_code,
    }
    session = await client.get_http_session()
    async with session.post(
        client.get_endpoint(Endpoints.GCODE_LIST),
        json=payload,
        headers={"Content-Type": "application/json"},
    ) as response:
        print(f"\nRaw POST {Endpoints.GCODE_LIST} -> HTTP {response.status}")
        data = await response.json(content_type=None)

    print(json.dumps(data, indent=2, ensure_ascii=False)[:4000])

    print("\nParsing with the library's GCodeListResponse model:")
    try:
        result = GCodeListResponse(**data)
    except ValidationError as err:
        print("  REJECTED - the library falls back to names only. Reasons:")
        for error in err.errors():
            print(f"    {'.'.join(str(p) for p in error['loc'])}: {error['msg']}")
        return
    detail = result.gcode_list_detail
    print(f"  accepted. gcodeListDetail entries: {len(detail) if detail else 0}")
    if not detail:
        print("  -> the printer itself reports no per-file metadata.")


async def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true", help="only run discovery")
    parser.add_argument("--ip", default=os.environ.get("FF_IP"))
    parser.add_argument("--serial", default=os.environ.get("FF_SERIAL"))
    parser.add_argument("--check-code", default=os.environ.get("FF_CHECK_CODE"))
    parser.add_argument(
        "--raw",
        action="store_true",
        help="dump the untouched /gcodeList payload and the model parse result",
    )
    parser.add_argument(
        "--thumb",
        metavar="FILE",
        help="ask /gcodeThumb for this stored file's preview image",
    )
    parser.add_argument("--thumb-out", metavar="PATH", help="save the --thumb image here")
    parser.add_argument(
        "--print",
        dest="print_file",
        help="START a print of this file; suppresses the reports above",
    )
    parser.add_argument("--leveling", action="store_true", help="level the bed first")
    parser.add_argument("--yes", action="store_true", help="confirm the print start")
    args = parser.parse_args()

    if args.discover:
        await discover()
        return

    if not (args.ip and args.serial and args.check_code):
        parser.error("--ip, --serial and --check-code are required (or FF_* env vars)")

    client = await connect(args.ip, args.serial, args.check_code)
    try:
        info = await client.info.get()
        client.cache_details(info)

        # Always needed: the entry carries the tool data the mappings derive
        # from, and the machine info carries the slot colors.
        entries = await client.files.get_recent_file_list()
        entries = [e for e in entries or [] if e.gcode_file_name]

        # --print keeps the output to the job itself; the reports would bury it.
        if not args.print_file:
            report_printer(client, info)
            report_files(entries, info)

            if args.raw:
                await report_raw(client)

            if args.thumb:
                await report_thumbnail(client, args.thumb, args.thumb_out)

            print("\nRead-only run. Pass --print <file> --yes to start a print.")
            return

        if not args.yes:
            print(
                f"Would start '{args.print_file}' "
                f"(leveling={args.leveling}). Re-run with --yes to actually print."
            )
            return

        entry = next(
            (e for e in entries if e.gcode_file_name == args.print_file), None
        )
        print(f"Starting '{args.print_file}' (leveling={args.leveling}) ...")
        await async_start_local_print(
            client,
            args.print_file,
            leveling_before_print=args.leveling,
            file_entry=entry,
            machine_info=info,
        )
        print("Printer accepted the job.")
    finally:
        await client.dispose()


if __name__ == "__main__":
    asyncio.run(main())
