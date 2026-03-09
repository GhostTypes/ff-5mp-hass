"""Wrapper-level discovery tests for the Home Assistant integration."""

import sys
from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from flashforge.discovery import DiscoveredPrinter, DiscoveryProtocol, PrinterModel
from flashforge.discovery import FlashForgePrinter, FlashForgePrinterDiscovery


@pytest.mark.unit
class TestFlashForgePrinter:
    """Test cases for FlashForgePrinter class."""

    def test_create_printer(self):
        printer = FlashForgePrinter()
        assert printer.name == ""
        assert printer.serial_number == ""
        assert printer.ip_address == ""

    def test_printer_string_representation(self):
        printer = FlashForgePrinter(
            name="Test Printer",
            serial_number="TEST123",
            ip_address="192.168.1.50",
        )
        assert str(printer) == "Name: Test Printer, Serial: TEST123, IP: 192.168.1.50"


@pytest.mark.unit
class TestFlashForgePrinterDiscovery:
    """Wrapper tests for FlashForgePrinterDiscovery."""

    def test_create_discovery(self):
        discovery = FlashForgePrinterDiscovery()
        assert discovery.discovery_port == 48899
        assert discovery.listen_port == 18007
        assert len(discovery.discovery_message) == 20
        assert discovery.discovery_message[:7] == b"www.usr"

    def test_calculate_broadcast_address(self):
        discovery = FlashForgePrinterDiscovery()
        assert discovery._calculate_broadcast_address("192.168.1.10", "255.255.255.0") == "192.168.1.255"
        assert discovery._calculate_broadcast_address("invalid", "255.255.255.0") is None

    def test_parse_printer_response_historical_payload(self):
        discovery = FlashForgePrinterDiscovery()
        response = bytearray(200)
        response[0:18] = b"Adventurer 5M Pro"
        response[0x92 : 0x92 + 11] = b"FF123456789"

        printer = discovery._parse_printer_response(bytes(response), "192.168.1.100")

        assert printer is not None
        assert printer.name == "Adventurer 5M Pro"
        assert printer.serial_number == "FF123456789"
        assert printer.ip_address == "192.168.1.100"

    @pytest.mark.asyncio
    async def test_discover_printers_async_returns_wrapper_objects(self):
        discovery = FlashForgePrinterDiscovery()
        discovered_printer = DiscoveredPrinter(
            model=PrinterModel.ADVENTURER_5M_PRO,
            protocol_format=DiscoveryProtocol.MODERN,
            name="Adventurer 5M Pro",
            ip_address="192.168.1.100",
            command_port=8899,
            serial_number="FF123456789",
        )

        with patch.object(
            discovery._discovery,
            "discover",
            AsyncMock(return_value=[discovered_printer]),
        ):
            printers = await discovery.discover_printers_async(timeout_ms=50, idle_timeout_ms=10, max_retries=1)

        assert printers == [
            FlashForgePrinter(
                name="Adventurer 5M Pro",
                serial_number="FF123456789",
                ip_address="192.168.1.100",
            )
        ]
