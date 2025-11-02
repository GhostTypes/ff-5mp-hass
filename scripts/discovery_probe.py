#!/usr/bin/env python3
"""Standalone discovery probe for FlashForge printers.

Run this inside the Home Assistant virtual environment to verify network
visibility from WSL before exercising the Home Assistant config flow.
"""

from __future__ import annotations

import argparse
import asyncio
import logging
from typing import Sequence

from flashforge.discovery import FlashForgePrinter, FlashForgePrinterDiscovery


def configure_logging(verbose: bool) -> None:
    """Configure root logger for the discovery run."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )


def format_printer(printer: FlashForgePrinter) -> str:
    """Format a printer object for terminal output."""
    name = printer.name or "<unnamed>"
    serial = printer.serial_number or "<no-serial>"
    return f"{name} (serial: {serial}) @ {printer.ip_address}"


async def run_discovery(
    timeout_ms: int,
    idle_timeout_ms: int,
    retries: int,
) -> Sequence[FlashForgePrinter]:
    """Execute a discovery scan and print results."""
    discovery = FlashForgePrinterDiscovery()

    broadcast_addresses = discovery._get_broadcast_addresses()  # pylint: disable=protected-access
    if broadcast_addresses:
        print(f"Broadcast addresses: {', '.join(broadcast_addresses)}")
    else:
        print("No broadcast addresses detected before discovery run.")

    printers = await discovery.discover_printers_async(
        timeout_ms=timeout_ms,
        idle_timeout_ms=idle_timeout_ms,
        max_retries=retries,
    )

    if printers:
        print(f"Discovered {len(printers)} printer(s):")
        for printer in printers:
            print(f" - {format_printer(printer)}")
    else:
        print("No printers responded to discovery probe.")

    return printers


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for the probe."""
    parser = argparse.ArgumentParser(
        description="Run a standalone FlashForge printer discovery scan.",
    )
    parser.add_argument(
        "--timeout-ms",
        type=int,
        default=5000,
        help="Total timeout in milliseconds for each discovery attempt (default: 5000).",
    )
    parser.add_argument(
        "--idle-timeout-ms",
        type=int,
        default=1500,
        help="Idle timeout in milliseconds before ending the wait phase (default: 1500).",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=3,
        help="Number of discovery attempts before giving up (default: 3).",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable DEBUG logging output from flashforge discovery internals.",
    )
    return parser.parse_args()


def main() -> None:
    """Entry point."""
    args = parse_args()
    configure_logging(args.verbose)

    try:
        asyncio.run(
            run_discovery(
                timeout_ms=args.timeout_ms,
                idle_timeout_ms=args.idle_timeout_ms,
                retries=args.retries,
            )
        )
    except KeyboardInterrupt:  # pragma: no cover - manual interruption
        print("Discovery probe interrupted.")


if __name__ == "__main__":
    main()
