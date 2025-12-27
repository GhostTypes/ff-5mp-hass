"""Unit tests for FlashForge printer discovery functionality."""
import asyncio
import socket
import sys
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

# Add the project root to sys.path for testing
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from flashforge.discovery import FlashForgePrinter, FlashForgePrinterDiscovery


@pytest.mark.unit
class TestFlashForgePrinter:
    """Test cases for FlashForgePrinter class."""

    def test_create_printer(self):
        """Test creating a FlashForgePrinter instance."""
        printer = FlashForgePrinter()
        assert printer.name == ""
        assert printer.serial_number == ""
        assert printer.ip_address == ""

    def test_create_printer_with_data(self):
        """Test creating a printer with initial data."""
        printer = FlashForgePrinter(
            name="Adventurer 5M Pro",
            serial_number="ABC123456",
            ip_address="192.168.1.100"
        )
        assert printer.name == "Adventurer 5M Pro"
        assert printer.serial_number == "ABC123456"
        assert printer.ip_address == "192.168.1.100"

    def test_printer_string_representation(self):
        """Test string representation of printer."""
        printer = FlashForgePrinter(
            name="Test Printer",
            serial_number="TEST123",
            ip_address="192.168.1.50"
        )
        expected = "Name: Test Printer, Serial: TEST123, IP: 192.168.1.50"
        assert str(printer) == expected

    def test_printer_repr(self):
        """Test repr representation of printer."""
        printer = FlashForgePrinter(
            name="Test",
            serial_number="123",
            ip_address="192.168.1.1"
        )
        repr_str = repr(printer)
        assert "FlashForgePrinter" in repr_str
        assert "name='Test'" in repr_str
        assert "serial_number='123'" in repr_str
        assert "ip_address='192.168.1.1'" in repr_str


@pytest.mark.unit
class TestFlashForgePrinterDiscovery:
    """Test cases for FlashForgePrinterDiscovery class."""

    def test_create_discovery(self):
        """Test creating a discovery instance."""
        discovery = FlashForgePrinterDiscovery()
        assert discovery.discovery_port == 48899
        assert discovery.listen_port == 18007
        assert len(discovery.discovery_message) == 20
        assert discovery.discovery_message[:7] == b'www.usr'

    def test_discovery_message_format(self):
        """Test that the discovery message has the correct format."""
        discovery = FlashForgePrinterDiscovery()
        expected = bytes([
            0x77, 0x77, 0x77, 0x2e, 0x75, 0x73, 0x72, 0x22,  # "www.usr"
            0x65, 0x36, 0xc0, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00
        ])
        assert discovery.discovery_message == expected

    def test_calculate_broadcast_address(self):
        """Test broadcast address calculation."""
        discovery = FlashForgePrinterDiscovery()

        # Test common network configurations
        result = discovery._calculate_broadcast_address("192.168.1.10", "255.255.255.0")
        assert result == "192.168.1.255"

        result = discovery._calculate_broadcast_address("10.0.0.50", "255.255.0.0")
        assert result == "10.0.255.255"

        result = discovery._calculate_broadcast_address("172.16.5.100", "255.255.255.192")
        assert result == "172.16.5.127"

    def test_calculate_broadcast_address_invalid(self):
        """Test broadcast address calculation with invalid inputs."""
        discovery = FlashForgePrinterDiscovery()

        # Test invalid IP formats
        assert discovery._calculate_broadcast_address("invalid", "255.255.255.0") is None
        assert discovery._calculate_broadcast_address("192.168.1.10", "invalid") is None
        assert discovery._calculate_broadcast_address("192.168.1", "255.255.255.0") is None

    def test_parse_printer_response_valid(self):
        """Test parsing a valid printer response."""
        discovery = FlashForgePrinterDiscovery()

        # Create a mock response (196 bytes minimum)
        response = bytearray(200)

        # Set printer name at offset 0 (32 bytes)
        name = b"Adventurer 5M Pro\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        response[0:32] = name

        # Set serial number at offset 0x92 (146 decimal, 32 bytes)
        serial = b"FF123456789\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        response[0x92:0x92+32] = serial

        printer = discovery._parse_printer_response(bytes(response), "192.168.1.100")
        assert printer is not None
        assert printer.name == "Adventurer 5M Pro"
        assert printer.serial_number == "FF123456789"
        assert printer.ip_address == "192.168.1.100"

    def test_parse_printer_response_invalid(self):
        """Test parsing invalid printer responses."""
        discovery = FlashForgePrinterDiscovery()

        # Test None response
        assert discovery._parse_printer_response(None, "192.168.1.100") is None

        # Test too short response
        short_response = b"short"
        assert discovery._parse_printer_response(short_response, "192.168.1.100") is None

        # Test response with correct length but no data
        empty_response = bytes(200)
        printer = discovery._parse_printer_response(empty_response, "192.168.1.100")
        # Should return None since both name and serial are empty
        assert printer is None

    @patch('netifaces.interfaces')
    @patch('netifaces.ifaddresses')
    def test_get_broadcast_addresses(self, mock_ifaddresses, mock_interfaces):
        """Test getting broadcast addresses from network interfaces."""
        discovery = FlashForgePrinterDiscovery()

        # Mock network interfaces
        mock_interfaces.return_value = ['eth0', 'lo']

        # Mock interface addresses
        import netifaces
        mock_ifaddresses.side_effect = lambda iface: {
            netifaces.AF_INET: [
                {
                    'addr': '192.168.1.100' if iface == 'eth0' else '127.0.0.1',
                    'netmask': '255.255.255.0' if iface == 'eth0' else '255.0.0.0'
                }
            ]
        } if iface in ['eth0', 'lo'] else {}

        addresses = discovery._get_broadcast_addresses()

        # Should include calculated broadcast address and fallback
        assert '192.168.1.255' in addresses
        assert '255.255.255.255' in addresses
        # Should not include loopback broadcast
        assert '127.255.255.255' not in addresses

    @patch('netifaces.interfaces')
    def test_get_broadcast_addresses_fallback(self, mock_interfaces):
        """Test broadcast address fallback when netifaces fails."""
        discovery = FlashForgePrinterDiscovery()

        # Mock interfaces to raise an exception
        mock_interfaces.side_effect = Exception("Network error")

        addresses = discovery._get_broadcast_addresses()

        # Should include fallback addresses
        expected_fallbacks = ['255.255.255.255', '192.168.1.255', '192.168.0.255']
        for addr in expected_fallbacks:
            assert addr in addresses

    def test_print_debug_info(self, capsys):
        """Test debug info printing."""
        discovery = FlashForgePrinterDiscovery()

        test_data = b"Test data with some bytes: \x01\x02\x03\xFF"
        discovery.print_debug_info(test_data, "192.168.1.100")

        captured = capsys.readouterr()
        assert "Received response from 192.168.1.100" in captured.out
        assert f"Response length: {len(test_data)} bytes" in captured.out
        assert "Hex dump:" in captured.out
        assert "ASCII dump:" in captured.out


@pytest.mark.unit
@pytest.mark.asyncio
class TestDiscoveryIntegration:
    """Integration tests for discovery functionality."""

    async def test_discover_printers_no_printers(self):
        """Test discovery when no printers are found."""
        discovery = FlashForgePrinterDiscovery()

        # Mock the DiscoveryProtocol to return no printers
        async def mock_wait_for_responses(self, timeout, idle_timeout):
            return []

        with patch('flashforge.discovery.discovery.DiscoveryProtocol.wait_for_responses', new=mock_wait_for_responses):
            printers = await discovery.discover_printers_async(
                timeout_ms=100,  # Short timeout for testing
                idle_timeout_ms=50,
                max_retries=1
            )

        assert printers == []

    async def test_discover_printers_with_mock_response(self):
        """Test discovery with a mocked printer response."""
        discovery = FlashForgePrinterDiscovery()

        # Create a mock printer response
        mock_printer = FlashForgePrinter(
            name="Test Printer",
            serial_number="TEST123",
            ip_address="192.168.1.100"
        )

        # Mock the transport and protocol
        mock_transport = Mock()
        mock_transport.close = Mock()
        mock_transport.sendto = Mock()

        # Create a mock protocol that returns our test printer
        class MockProtocol:
            async def wait_for_responses(self, timeout, idle_timeout):
                return [mock_printer]

        mock_protocol = MockProtocol()

        async def mock_create_datagram_endpoint(protocol_factory, **kwargs):
            return (mock_transport, mock_protocol)

        # Patch the event loop's create_datagram_endpoint method
        with patch('asyncio.get_event_loop') as mock_loop:
            loop = asyncio.get_event_loop()
            mock_loop.return_value = loop

            with patch.object(loop, 'create_datagram_endpoint', new=mock_create_datagram_endpoint):
                printers = await discovery.discover_printers_async(
                    timeout_ms=100,
                    idle_timeout_ms=50,
                    max_retries=1
                )

        assert len(printers) == 1
        assert printers[0].name == "Test Printer"
        assert printers[0].serial_number == "TEST123"
        assert printers[0].ip_address == "192.168.1.100"

    async def test_discover_printers_removes_duplicates(self):
        """Test that discovery removes duplicate printers by IP."""
        discovery = FlashForgePrinterDiscovery()

        # Create duplicate printers with same IP
        printer1 = FlashForgePrinter(
            name="Printer1",
            serial_number="123",
            ip_address="192.168.1.100"
        )
        printer2 = FlashForgePrinter(
            name="Printer2",  # Different name
            serial_number="456",  # Different serial
            ip_address="192.168.1.100"  # Same IP
        )

        duplicates = [printer1, printer2]

        # Mock the transport and protocol to avoid real socket operations
        mock_transport = Mock()
        mock_transport.close = Mock()
        mock_transport.sendto = Mock()

        # Create a mock protocol that returns duplicate printers
        class MockProtocol:
            async def wait_for_responses(self, timeout, idle_timeout):
                return duplicates

        mock_protocol = MockProtocol()

        async def mock_create_datagram_endpoint(protocol_factory, **kwargs):
            return (mock_transport, mock_protocol)

        # Patch the event loop's create_datagram_endpoint method
        with patch('asyncio.get_event_loop') as mock_loop:
            loop = asyncio.get_event_loop()
            mock_loop.return_value = loop

            with patch.object(loop, 'create_datagram_endpoint', new=mock_create_datagram_endpoint):
                printers = await discovery.discover_printers_async(
                    timeout_ms=100,
                    idle_timeout_ms=50,
                    max_retries=1
                )

        # Should only have one printer (duplicates removed by IP)
        assert len(printers) == 1
        assert printers[0].ip_address == "192.168.1.100"


@pytest.mark.unit
@pytest.mark.skipif(not hasattr(socket, 'AF_INET'), reason="Socket operations not available")
class TestDiscoveryNetwork:
    """Network-level tests for discovery (may require network access)."""

    @pytest.mark.asyncio
    async def test_socket_creation(self):
        """Test that sockets can be created and configured properly."""
        discovery = FlashForgePrinterDiscovery()

        # Test discovery socket creation
        discovery_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        discovery_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        discovery_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        discovery_socket.close()

        # Test listening socket creation
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.close()

        # If we get here without exceptions, socket creation works
        assert True


if __name__ == "__main__":
    # Run tests directly
    pytest.main([__file__, "-v"])
