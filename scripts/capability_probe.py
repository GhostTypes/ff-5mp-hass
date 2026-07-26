#!/usr/bin/env python3
"""Probe how a real printer reports its capabilities, and what the integration makes of them.

Several capability flags are verbatim copies of the printer's JSON and are wrong
or absent on models that clearly have the feature (see the "never trust /product"
and "never gate on a single raw /detail field" rules in AGENTS.md). This dumps the
untouched ``/detail`` and ``/product`` payloads next to the flags the integration
gates its entities on, so a greyed-out entity can be traced to its source.

Read-only unless ``--led`` is passed.

Usage (from the repository root):

    python scripts/capability_probe.py --ip 192.168.1.50 --serial SN123 --check-code ABCD
    python scripts/capability_probe.py --ip ... --led on

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

from flashforge import FiveMClientConnectionOptions, FlashForgeClient  # noqa: E402
from flashforge.api.constants.endpoints import Endpoints  # noqa: E402
from flashforge.models.responses import FFPrinterDetail  # noqa: E402

from custom_components.flashforge.util import has_material_station  # noqa: E402


async def connect(ip: str, serial: str, check_code: str) -> FlashForgeClient:
    """Set the client up the same way the integration's async_setup_entry does.

    Note the options are left empty: passing ``led_control_override=False`` here
    would pin ``led_control`` to False, which is exactly the bug this script is
    meant to expose.
    """
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


def report_flags(client: FlashForgeClient, info) -> None:
    """Print the model identity and the flags entities are gated on."""
    print("Printer")
    print(f"  model                     {getattr(info, 'model', None)}  (pid={getattr(info, 'pid', None)})")
    print(f"  is_pro                    {client.is_pro}")
    print(f"  is_ad5x                   {client.is_ad5x}")
    print(f"  is_creator5               {client.is_creator5}")
    print(f"  is_creator5_pro           {client.is_creator5_pro}")
    print(f"  http_only                 {client.http_only}")

    print("\nCapability flags")
    print(f"  client.led_control        {client.led_control}   (LED switch)")
    print(f"  client.filtration_control {client.filtration_control}   (unused: the select gates on model identity)")
    print(f"  has_matl_station (raw)    {getattr(info, 'has_matl_station', None)}")
    print(f"  has_material_station()    {has_material_station(info)}   (Material Station entities)")
    print(f"  has_door_sensor           {getattr(info, 'has_door_sensor', None)}")
    print(f"  has_camera                {getattr(info, 'has_camera', None)}")

    station = getattr(info, "matl_station_info", None)
    for slot in getattr(station, "slot_infos", None) or []:
        print(
            f"    slot {getattr(slot, 'slot_id', '?')}: "
            f"material={getattr(slot, 'material_name', '') or '-'} "
            f"color={getattr(slot, 'material_color', '') or '-'} "
            f"loaded={getattr(slot, 'has_filament', None)}"
        )


async def _post(client: FlashForgeClient, endpoint: str) -> dict | None:
    payload = {
        "serialNumber": client.serial_number,
        "checkCode": client.check_code,
    }
    session = await client.get_http_session()
    async with session.post(
        client.get_endpoint(endpoint),
        json=payload,
        headers={"Content-Type": "application/json"},
    ) as response:
        print(f"\nRaw POST {endpoint} -> HTTP {response.status}")
        return await response.json(content_type=None)


async def report_raw_detail(client: FlashForgeClient) -> None:
    """Dump the untouched /detail payload and inspect the Material Station keys.

    ``FFMachineInfo.has_matl_station`` is a straight copy of the raw
    ``hasMatlStation`` field. The Creator 5 series leaves it None while
    ``matlStationInfo`` is fully populated, so this shows whether the printer
    omits the flag entirely or reports it under a different name.
    """
    data = await _post(client, Endpoints.DETAIL)
    print(json.dumps(data, indent=2, ensure_ascii=False)[:6000])

    detail = data.get("detail") if isinstance(data, dict) else None
    if not isinstance(detail, dict):
        print("\n  No 'detail' object in the response.")
        return

    print("\nMaterial Station keys in the raw /detail payload:")
    print(f"  'hasMatlStation' present  {'hasMatlStation' in detail}")
    if "hasMatlStation" in detail:
        print(f"  hasMatlStation            {detail['hasMatlStation']!r}")
    print(f"  'matlStationInfo' present {'matlStationInfo' in detail}")
    station = detail.get("matlStationInfo")
    if isinstance(station, dict):
        print(f"  slotCnt                   {station.get('slotCnt')!r}")
        print(f"  slotInfos entries         {len(station.get('slotInfos') or [])}")

    # Any key containing "matl"/"station" the model doesn't declare - would
    # reveal the flag hiding behind a different name on this firmware.
    known = set(FFPrinterDetail.model_fields) | {
        field.alias for field in FFPrinterDetail.model_fields.values() if field.alias
    }
    extras = sorted(
        key
        for key in detail
        if key not in known and ("matl" in key.lower() or "station" in key.lower())
    )
    print(f"  undeclared matl/station keys {extras or 'none'}")


async def report_product(client: FlashForgeClient) -> None:
    """Dump /product, the source of the LED and filtration capability flags."""
    data = await _post(client, Endpoints.PRODUCT)
    print(json.dumps(data, indent=2, ensure_ascii=False)[:4000])

    product = (data or {}).get("product") if isinstance(data, dict) else None
    if isinstance(product, dict):
        print("\nCapability-relevant fields:")
        for key in (
            "lightCtrlState",
            "internalFanCtrlState",
            "externalFanCtrlState",
            "chamberTempCtrlState",
            "cameraCtrlState",
        ):
            print(f"  {key:24} {product.get(key, '<absent>')!r}")


async def report_led(client: FlashForgeClient, state: str) -> None:
    """Send the LED command, bypassing the client's own capability guard.

    ``control.set_led_on/off`` refuse when ``client.led_control`` is False, so
    this forces the override first: it answers whether the printer accepts
    lightControl_cmd at all, independently of what /product claims.
    """
    print(f"\nForcing led_control on and sending lightControl_cmd '{state}'")
    client.set_feature_overrides(led_control=True)

    if state == "on":
        ok = await client.control.set_led_on()
    else:
        ok = await client.control.set_led_off()
    print(f"  printer accepted the command: {ok}")

    info = await client.info.get()
    print(f"  /detail now reports lights_on: {getattr(info, 'lights_on', None)}")


async def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ip", default=os.environ.get("FF_IP"))
    parser.add_argument("--serial", default=os.environ.get("FF_SERIAL"))
    parser.add_argument("--check-code", default=os.environ.get("FF_CHECK_CODE"))
    parser.add_argument(
        "--led",
        choices=("on", "off"),
        help="switch the printer's LED, bypassing the capability guard",
    )
    args = parser.parse_args()

    if not (args.ip and args.serial and args.check_code):
        parser.error("--ip, --serial and --check-code are required (or FF_* env vars)")

    client = await connect(args.ip, args.serial, args.check_code)
    try:
        info = await client.info.get()
        client.cache_details(info)
        report_flags(client, info)
        await report_raw_detail(client)
        await report_product(client)

        if args.led:
            await report_led(client, args.led)
    finally:
        await client.dispose()


if __name__ == "__main__":
    asyncio.run(main())
