"""Unit tests for how setup failures are reported to the user.

Issue #18: every failure in `validate_connection` raised a bare ConnectionError
and surfaced as "Failed to connect to the printer. Please check the IP address
and credentials." A response the library could not parse, an unreachable
printer, and a genuinely wrong check code were indistinguishable - and the one
message on offer blamed the credentials in all three cases. Two reporters read
that same message two different ways ("check code not working" and
"cannot_connect / TCP problem"); neither had a credential problem.

These tests pin the distinction: only a printer that answered and refused
produces `invalid_auth`.
"""

import json
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from tests.ha_mocks import mock_homeassistant

mock_homeassistant()
sys.modules["voluptuous"] = MagicMock()

from custom_components.flashforge.config_flow import (
    FlashForgeResponseError,
    InvalidAuthError,
    UnsupportedPrinterError,
    validate_connection,
)
from homeassistant.const import CONF_IP_ADDRESS, CONF_NAME

ENTRY = {
    CONF_NAME: "Creator 5 Pro",
    CONF_IP_ADDRESS: "192.168.1.120",
    "serial_number": "SN123456",
    "check_code": "12345678",
}


def _client(*, detail=None, machine_info=True, product_ok=True, get_raises=None) -> Mock:
    """Build a mock client.

    `detail` is a raw dict now, not a parsed model: the flow reads identity off
    the undecoded /detail payload so the supported-model gate cannot be blocked
    by an unrelated field failing validation.
    """
    client = Mock()
    client.info.get_detail_raw = AsyncMock(
        return_value={"code": 0, "detail": detail} if detail is not None else None
    )
    client.info.get = AsyncMock(
        return_value=SimpleNamespace(name="Creator 5 Pro") if machine_info else None,
        side_effect=get_raises,
    )
    client.cache_details = Mock()
    client.send_product_command = AsyncMock(return_value=product_ok)
    client._http_session = None
    return client


@pytest.mark.unit
@pytest.mark.asyncio
async def test_rejected_credentials_raise_invalid_auth():
    """The one case that really is a credential problem."""
    client = _client(detail={"pid": 41, "name": "Creator 5 Pro"}, product_ok=False)

    with patch("custom_components.flashforge.config_flow.FlashForgeClient", return_value=client):
        with pytest.raises(InvalidAuthError):
            await validate_connection(Mock(), ENTRY)


@pytest.mark.unit
@pytest.mark.asyncio
async def test_unreadable_detail_is_not_reported_as_bad_credentials():
    """A /detail the library could not parse comes back as None.

    That is the issue #18 path. It must stay a plain ConnectionError, so the
    user is not told their check code is wrong when it is not.
    """
    client = _client(detail=None)

    with patch("custom_components.flashforge.config_flow.FlashForgeClient", return_value=client):
        with pytest.raises(ConnectionError) as excinfo:
            await validate_connection(Mock(), ENTRY)

    assert not isinstance(excinfo.value, InvalidAuthError)
    client.send_product_command.assert_not_awaited()


@pytest.mark.unit
@pytest.mark.asyncio
async def test_unparseable_machine_info_is_not_reported_as_bad_credentials():
    """Same rule for the second /detail read, which parses into FFMachineInfo."""
    client = _client(detail={"pid": 41, "name": "Creator 5 Pro"}, machine_info=False)

    with patch("custom_components.flashforge.config_flow.FlashForgeClient", return_value=client):
        with pytest.raises(ConnectionError) as excinfo:
            await validate_connection(Mock(), ENTRY)

    assert not isinstance(excinfo.value, InvalidAuthError)


@pytest.mark.unit
def test_invalid_auth_is_caught_before_connection_error():
    """InvalidAuthError subclasses ConnectionError, so handler order matters.

    If `except ConnectionError` were listed first it would swallow every auth
    failure and the new message would never be shown.
    """
    source = (
        project_root / "custom_components" / "flashforge" / "config_flow.py"
    ).read_text(encoding="utf-8")

    # Four flows handle these: user, manual, reauth, reconfigure.
    assert source.count('errors["base"] = "invalid_auth"') == 4
    for block in source.split("except UnsupportedPrinterError:")[1:]:
        auth_at = block.find("except InvalidAuthError:")
        conn_at = block.find("except ConnectionError:")
        assert auth_at != -1, "every handler chain must catch InvalidAuthError"
        assert auth_at < conn_at, "InvalidAuthError must be caught before ConnectionError"


@pytest.mark.unit
def test_error_strings_exist_and_stop_blaming_the_credentials():
    """Each failure mode owns a message that describes only that failure mode.

    The messages used to hedge - `cannot_connect` and `invalid_auth` both had to
    end with "...but check the log, it might be an unreadable response instead",
    because there was no third error to route that case to. Now there is
    (`invalid_response`), so each message can state its own cause plainly.
    """
    for name in ("strings.json", "translations/en.json"):
        path = project_root / "custom_components" / "flashforge" / name
        errors = json.loads(path.read_text(encoding="utf-8"))["config"]["error"]

        for key in ("invalid_auth", "cannot_connect", "invalid_response"):
            assert key in errors, f"{name} is missing {key}"

        # The original wording, which sent both #18 reporters chasing their check code.
        assert "check the IP address and credentials" not in errors["cannot_connect"]
        # The unreadable-response message must send the user to the issue
        # tracker, and must not leave them suspecting their network.
        assert "issues" in errors["invalid_response"]
        assert "not a network" in errors["invalid_response"].lower()


@pytest.mark.unit
@pytest.mark.asyncio
async def test_unreadable_response_propagates_as_its_own_error_type():
    """A payload the library cannot read must not arrive as a ConnectionError.

    This is the heart of issue #18: the printer is reachable and the credentials
    are fine, but `chamberTemp: -108` failed validation and the user was told to
    check their network for three releases. The error has to stay distinguishable
    all the way up to the message the user reads.
    """
    client = _client(
        detail={"pid": 40, "name": "Creator 5"},
        get_raises=FlashForgeResponseError("chamberTemp out of range"),
    )

    with patch("custom_components.flashforge.config_flow.FlashForgeClient", return_value=client):
        with pytest.raises(FlashForgeResponseError):
            await validate_connection(Mock(), ENTRY)


@pytest.mark.unit
def test_every_flow_maps_unreadable_responses_to_invalid_response():
    """All four flows (user, manual, reauth, reconfigure) must route it."""
    source = (
        project_root / "custom_components" / "flashforge" / "config_flow.py"
    ).read_text(encoding="utf-8")

    assert source.count('errors["base"] = "invalid_response"') == 4
    for block in source.split("except UnsupportedPrinterError:")[1:]:
        response_at = block.find("except FlashForgeResponseError")
        unknown_at = block.find("except Exception")
        assert response_at != -1, "every handler chain must catch FlashForgeResponseError"
        # It is a plain Exception, not a ConnectionError, so the only ordering
        # that matters is that the catch-all does not swallow it first.
        assert response_at < unknown_at, "must be caught before the generic handler"


@pytest.mark.unit
@pytest.mark.asyncio
async def test_supported_gate_reads_pid_before_validation():
    """A supported printer is never rejected over an unrelated bad field.

    The gate used to read `pid` off a parsed model, so it could only run once
    the whole ~50-field payload had validated - meaning a Creator 5 was refused
    because of a chamber reading that has no bearing on whether it is supported.
    Reading the raw payload means the model check happens first and the
    unreadable-response path is reported for what it is.
    """
    client = _client(
        detail={"pid": 40, "name": "Creator 5", "chamberTemp": -108},
        get_raises=FlashForgeResponseError("chamberTemp out of range"),
    )

    with patch("custom_components.flashforge.config_flow.FlashForgeClient", return_value=client):
        with pytest.raises(FlashForgeResponseError):
            await validate_connection(Mock(), ENTRY)

    # Crucially NOT UnsupportedPrinterError - the model gate passed on pid 40.
    client.info.get.assert_awaited()


@pytest.mark.unit
@pytest.mark.asyncio
async def test_unsupported_printer_still_wins_over_auth():
    """An unsupported model is reported as such, not as an auth failure."""
    client = _client(detail={"pid": 30, "name": "Adventurer 4"}, product_ok=False)

    with patch("custom_components.flashforge.config_flow.FlashForgeClient", return_value=client):
        with pytest.raises(UnsupportedPrinterError):
            await validate_connection(Mock(), ENTRY)
