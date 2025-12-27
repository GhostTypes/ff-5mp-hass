"""Unit tests for utility functions.

Tests utility helpers without Home Assistant dependencies.
"""
import sys
from pathlib import Path
from unittest.mock import AsyncMock, Mock

import pytest

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Mock Home Assistant modules before importing integration code
from tests.ha_mocks import mock_homeassistant
mock_homeassistant()

from custom_components.flashforge.util import async_close_flashforge_client


@pytest.mark.unit
class TestAsyncCloseFlashForgeClient:
    """Test async_close_flashforge_client utility function."""

    @pytest.mark.asyncio
    async def test_closes_http_session_when_present(self):
        """Test that HTTP session is closed when present and not closed."""
        # Create mock client with HTTP session
        mock_client = Mock()
        mock_session = AsyncMock()
        mock_session.closed = False
        mock_client._http_session = mock_session

        # Close the client
        await async_close_flashforge_client(mock_client)

        # Verify session was closed
        mock_session.close.assert_called_once()

    @pytest.mark.asyncio
    async def test_does_not_close_already_closed_session(self):
        """Test that already-closed sessions are not closed again."""
        # Create mock client with closed HTTP session
        mock_client = Mock()
        mock_session = AsyncMock()
        mock_session.closed = True  # Already closed
        mock_client._http_session = mock_session

        # Close the client
        await async_close_flashforge_client(mock_client)

        # Verify session.close() was NOT called
        mock_session.close.assert_not_called()

    @pytest.mark.asyncio
    async def test_handles_missing_http_session(self):
        """Test that missing HTTP session is handled gracefully."""
        # Create mock client without HTTP session
        mock_client = Mock(spec=[])  # Empty spec - no _http_session attribute

        # Should not raise an error
        await async_close_flashforge_client(mock_client)

    @pytest.mark.asyncio
    async def test_handles_none_http_session(self):
        """Test that None HTTP session is handled gracefully."""
        # Create mock client with None HTTP session
        mock_client = Mock()
        mock_client._http_session = None

        # Should not raise an error
        await async_close_flashforge_client(mock_client)

    @pytest.mark.asyncio
    async def test_uses_getattr_safely(self):
        """Test that getattr is used to safely access _http_session."""
        # Create mock client that raises AttributeError
        mock_client = Mock(spec=[])

        # Should not raise an error (getattr returns None)
        await async_close_flashforge_client(mock_client)

    @pytest.mark.asyncio
    async def test_closes_session_with_custom_attributes(self):
        """Test that session is closed even if client has other attributes."""
        # Create mock client with HTTP session and other attributes
        mock_client = Mock()
        mock_client.some_other_attribute = "value"
        mock_session = AsyncMock()
        mock_session.closed = False
        mock_client._http_session = mock_session

        # Close the client
        await async_close_flashforge_client(mock_client)

        # Verify session was closed
        mock_session.close.assert_called_once()

    @pytest.mark.asyncio
    async def test_does_not_touch_tcp_resources(self):
        """Test that only HTTP session is closed, not TCP resources."""
        # Create mock client with both HTTP and TCP resources
        mock_client = Mock()

        mock_http_session = AsyncMock()
        mock_http_session.closed = False
        mock_client._http_session = mock_http_session

        mock_tcp_socket = Mock()
        mock_client._tcp_socket = mock_tcp_socket

        # Close the client
        await async_close_flashforge_client(mock_client)

        # Verify only HTTP session was closed
        mock_http_session.close.assert_called_once()

        # Verify TCP socket was NOT touched (no close call)
        assert not hasattr(
            mock_tcp_socket, "close"
        ) or not mock_tcp_socket.close.called
