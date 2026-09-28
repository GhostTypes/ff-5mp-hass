"""Exercise camera sharing against an HTTP camera that accepts one client."""

import asyncio
from contextlib import suppress

import pytest
from aiohttp import ClientSession, web
from aiohttp.test_utils import TestServer

from tests.ha_mocks import mock_homeassistant

mock_homeassistant()

from custom_components.flashforge import camera_stream

pytestmark = [pytest.mark.unit, pytest.mark.asyncio]


def jpeg(label: str) -> bytes:
    """Opaque JPEG payloads distinguish frames without testing an image decoder."""
    return b"\xff\xd8" + label.encode() + b"\xff\xd9"


async def eventually(predicate) -> None:
    """Wait for socket cleanup without depending on a fixed scheduling delay."""
    async with asyncio.timeout(2):
        while not predicate():
            await asyncio.sleep(0.005)


class CameraConnection:
    """One controllable response from the fake camera."""

    def __init__(self, request: web.Request) -> None:
        self.request = request
        self.commands: asyncio.Queue[tuple[bytes, ...] | None] = asyncio.Queue()
        self.ended = False

    @property
    def active(self) -> bool:
        transport = self.request.transport
        return not self.ended and transport is not None and not transport.is_closing()

    def send(self, *chunks: bytes) -> None:
        self.commands.put_nowait(chunks)

    def disconnect(self) -> None:
        self.commands.put_nowait(None)


class SingleClientCamera:
    """Reject an overlapping request, reproducing the printer's failure mode."""

    def __init__(self) -> None:
        self.connections: list[CameraConnection] = []
        self.opened: asyncio.Queue[CameraConnection] = asyncio.Queue()
        self.rejected = 0
        self.maximum_active = 0
        self.url = ""

    @property
    def active(self) -> int:
        return sum(connection.active for connection in self.connections)

    async def next_connection(self) -> CameraConnection:
        return await asyncio.wait_for(self.opened.get(), 2)

    async def handle(self, request: web.Request) -> web.StreamResponse:
        if self.active:
            self.rejected += 1
            return web.Response(status=503)
        connection = CameraConnection(request)
        self.connections.append(connection)
        self.maximum_active = max(self.maximum_active, self.active)
        response = web.StreamResponse(
            headers={"Content-Type": "multipart/x-mixed-replace; boundary=frame"}
        )
        await response.prepare(request)
        self.opened.put_nowait(connection)
        try:
            while connection.active:
                try:
                    chunks = await asyncio.wait_for(connection.commands.get(), 0.01)
                except TimeoutError:
                    continue
                if chunks is None:
                    break
                for chunk in chunks:
                    await response.write(chunk)
        except (ConnectionError, RuntimeError):
            pass
        finally:
            connection.ended = True
        return response


@pytest.fixture
async def printer():
    camera = SingleClientCamera()
    app = web.Application()
    app.router.add_get("/{path:.*}", camera.handle)
    async with TestServer(app) as server:
        camera.url = str(server.make_url("/stream"))
        yield camera


@pytest.fixture
async def shared(printer, monkeypatch):
    monkeypatch.setattr(camera_stream, "RETRY_DELAY", 0.01)
    tasks = []

    def create_task(coroutine):
        task = asyncio.create_task(coroutine)
        tasks.append(task)
        return task

    async with ClientSession() as session:
        stream = camera_stream.SharedCameraStream(session, create_task)
        stream.set_url(printer.url)
        try:
            yield stream
        finally:
            await stream.close()
            assert all(task.done() for task in tasks)


async def test_two_viewers_and_snapshot_share_one_connection(printer, shared):
    """Simultaneous subscription and a still request never open another socket."""
    viewers = [shared.subscribe(), shared.subscribe()]
    await asyncio.gather(*(viewer.__aenter__() for viewer in viewers))
    try:
        connection = await printer.next_connection()
        first = jpeg("first")
        connection.send(first)
        results = await asyncio.gather(shared.frame(), shared.frame())
        assert results[0] == results[1]
        assert results[0][1] == first

        async with shared.subscribe():
            assert await shared.frame() == results[0]

        await viewers.pop().__aexit__(None, None, None)
        second = jpeg("second")
        connection.send(second)
        assert (await shared.frame(after=results[0][0]))[1] == second
        assert len(printer.connections) == 1
        assert printer.rejected == 0
        assert printer.maximum_active == 1
    finally:
        await asyncio.gather(
            *(viewer.__aexit__(None, None, None) for viewer in viewers)
        )
    await eventually(lambda: printer.active == 0)


async def test_slow_viewer_receives_latest_frame_without_holding_up_others(
    printer, shared
):
    """Each viewer has its own cursor; old frames do not form a backlog."""
    async with shared.subscribe(), shared.subscribe():
        connection = await printer.next_connection()
        connection.send(jpeg("first"))
        slow_cursor, _ = await shared.frame()
        connection.send(jpeg("second"))
        fast_cursor, _ = await shared.frame(after=slow_cursor)
        connection.send(jpeg("third"))
        latest = await shared.frame(after=fast_cursor)
        assert latest[1] == jpeg("third")
        assert await shared.frame(after=slow_cursor) == latest
        assert printer.rejected == 0


async def test_disconnect_reconnects_for_existing_viewers(printer, shared):
    """A source disconnect can recover without a browser refresh."""
    async with shared.subscribe():
        original = await printer.next_connection()
        original.send(jpeg("before"))
        cursor, _ = await shared.frame()
        original.disconnect()
        replacement = await printer.next_connection()
        replacement.send(jpeg("after"))
        assert (await shared.frame(after=cursor))[1] == jpeg("after")
        assert printer.maximum_active == 1


async def test_url_change_releases_old_connection_and_discards_old_frame(
    printer, shared
):
    """Switching sources cannot return the previous source's cached snapshot."""
    async with shared.subscribe():
        original = await printer.next_connection()
        original.send(jpeg("old source"))
        await shared.frame()
        shared.set_url(printer.url + "?source=new")
        replacement = await printer.next_connection()
        assert replacement.request.query["source"] == "new"
        replacement.send(jpeg("new source"))
        assert (await shared.frame())[1] == jpeg("new source")
        assert printer.maximum_active == 1
        assert not original.active


async def test_camera_disabled_and_close_wake_waiters(printer, shared):
    """Off and unload stop waiting consumers promptly instead of leaking tasks."""
    async with shared.subscribe():
        await printer.next_connection()
        waiting = asyncio.create_task(shared.frame())
        shared.set_url(None)
        assert await asyncio.wait_for(waiting, 0.5) is None
        await eventually(lambda: printer.active == 0)

        shared.set_url(printer.url)
        await printer.next_connection()
        waiting = asyncio.create_task(shared.frame())
        await shared.close()
        assert await asyncio.wait_for(waiting, 0.5) is None
        await eventually(lambda: printer.active == 0)
    async with shared.subscribe():
        assert await shared.frame() is None
    assert len(printer.connections) == 2


async def test_cancelling_one_viewer_preserves_the_other(printer, shared):
    """Browser disconnection releases its subscription without cancelling peers."""
    ready = asyncio.Event()

    async def viewer():
        async with shared.subscribe():
            ready.set()
            await shared.frame()

    async with shared.subscribe():
        connection = await printer.next_connection()
        cancelled = asyncio.create_task(viewer())
        await ready.wait()
        cancelled.cancel()
        with suppress(asyncio.CancelledError):
            await cancelled
        connection.send(jpeg("remaining viewer"))
        assert (await shared.frame())[1] == jpeg("remaining viewer")
        assert len(printer.connections) == 1
    await eventually(lambda: printer.active == 0)


async def test_immediate_resubscribe_waits_for_previous_reader_to_close(
    printer, shared
):
    """Closing and reopening a preview cannot race two upstream readers."""
    async with shared.subscribe():
        original = await printer.next_connection()
        original.send(jpeg("before reopening"))
        await shared.frame()
    async with shared.subscribe():
        replacement = await printer.next_connection()
        replacement.send(jpeg("reopened"))
        assert (await shared.frame())[1] == jpeg("reopened")
        assert not original.active
        assert printer.maximum_active == 1
        assert printer.rejected == 0


async def test_stale_snapshot_is_not_returned_as_live(printer, shared, monkeypatch):
    """A previously valid JPEG cannot mask a camera that has stopped sending."""
    monkeypatch.setattr(camera_stream, "FRAME_TIMEOUT", 0.05)
    monkeypatch.setattr(camera_stream, "READ_TIMEOUT", 0.05)
    async with shared.subscribe():
        connection = await printer.next_connection()
        connection.send(jpeg("last frame"))
        assert (await shared.frame())[1] == jpeg("last frame")
        await asyncio.sleep(0.06)
        assert await shared.frame() is None


async def test_fragmented_jpeg_and_multipart_headers(printer, shared):
    """Header bytes and JPEG markers split across HTTP chunks are supported."""
    async with shared.subscribe():
        connection = await printer.next_connection()
        payload = jpeg("fragmented")
        connection.send(
            b"--frame\r\nContent-Type: image/jpeg\r\nContent-Length: 14\r\n\r\n",
            payload[:1],
        )
        waiting = asyncio.create_task(shared.frame())
        await asyncio.sleep(0.02)
        assert not waiting.done()
        connection.send(payload[1:-1])
        await asyncio.sleep(0.02)
        assert not waiting.done()
        connection.send(payload[-1:], b"\r\n--frame\r\n")
        assert (await waiting)[1] == payload


async def test_oversized_incomplete_frame_recovers_without_publishing_it(
    printer, shared, monkeypatch
):
    """Bounded parsing skips a broken oversized frame and accepts the next JPEG."""
    monkeypatch.setattr(camera_stream, "MAX_FRAME_SIZE", 64)
    async with shared.subscribe():
        connection = await printer.next_connection()
        connection.send(b"\xff\xd8" + b"x" * 80)
        replacement = await printer.next_connection()
        replacement.send(jpeg("valid"))
        assert (await shared.frame())[1] == jpeg("valid")
