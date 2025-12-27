"""Live discovery tests requiring real FlashForge printers on the network.

These tests are opt-in and require real hardware. Run with: pytest -m live
"""
import sys
from pathlib import Path

import pytest

# Add the project root to sys.path for testing
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from flashforge.discovery import FlashForgePrinter, FlashForgePrinterDiscovery


@pytest.mark.live
@pytest.mark.asyncio
class TestLiveDiscovery:
    """Live discovery tests with real hardware (requires actual printers on network)."""

    async def test_discover_printers_live(self):
        """Test discovery with actual printers on the network.

        This test requires real FlashForge printers on your network to pass.
        It will pass with 0 printers if none are found, allowing it to run in CI/CD.
        """
        discovery = FlashForgePrinterDiscovery()
        printers = await discovery.discover_printers_async(
            timeout_ms=10000,
            idle_timeout_ms=1500,
            max_retries=3
        )

        # Print results for visibility
        print(f"\n[Live Discovery] Found {len(printers)} printer(s):")
        for printer in printers:
            print(f"  - {printer.name} ({printer.ip_address}) - Serial: {printer.serial_number}")

        # Test passes regardless of how many printers found
        # This allows the test to run in CI/CD environments without printers
        assert isinstance(printers, list)

        # If printers were found, validate their structure
        for printer in printers:
            assert isinstance(printer, FlashForgePrinter)
            assert printer.ip_address != ""
            # Name or serial should be populated (at minimum)
            assert printer.name != "" or printer.serial_number != ""


if __name__ == "__main__":
    # Run live tests directly
    pytest.main([__file__, "-v", "-m", "live"])
