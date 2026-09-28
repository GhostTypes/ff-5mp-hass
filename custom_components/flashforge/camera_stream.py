"""One on-demand MJPEG reader shared by a camera's live and still consumers."""

from __future__ import annotations

import asyncio
import logging
import time
from collections.abc import AsyncIterator, Callable, Coroutine
from contextlib import asynccontextmanager
from typing import Any

import aiohttp

_LOGGER = logging.getLogger(__name__)
FRAME_TIMEOUT = 30
READ_TIMEOUT = 10
RETRY_DELAY = 1
MAX_FRAME_SIZE = 4 * 1024 * 1024


class SharedCameraStream:
    """Keep only the newest JPEG, independently of how fast each viewer reads."""

    def __init__(
        self,
        session: aiohttp.ClientSession,
        create_task: Callable[[Coroutine[Any, Any, None]], asyncio.Task[None]],
    ) -> None:
        self._session = session
        self._create_task = create_task
        self._url: str | None = None
        self._task: asyncio.Task[None] | None = None
        self._users = 0
        self._closed = False
        self._image: bytes | None = None
        self._image_time = 0.0
        self._sequence = 0
        self._changed = asyncio.Event()

    def set_url(self, url: str | None) -> None:
        """Invalidate frames and stop the old connection before changing source."""
        if self._url == url:
            return
        self._url = url
        self._stop()
        self._start()

    @asynccontextmanager
    async def subscribe(self) -> AsyncIterator[SharedCameraStream]:
        """Hold the shared reader open until this consumer leaves."""
        self._users += 1
        self._start()
        try:
            yield self
        finally:
            self._users -= 1
            if not self._users:
                self._stop()

    async def frame(self, after: int = -1) -> tuple[int, bytes] | None:
        """Wait for a fresh frame newer than this consumer's last sequence."""
        try:
            async with asyncio.timeout(FRAME_TIMEOUT):
                while not self._closed and self._url:
                    if (
                        self._image is not None
                        and self._sequence > after
                        and time.monotonic() - self._image_time < READ_TIMEOUT
                    ):
                        return self._sequence, self._image
                    await self._changed.wait()
        except TimeoutError:
            pass
        return None

    async def close(self) -> None:
        """Release the connection and wake all consumers on entity removal."""
        self._closed = True
        self._stop()
        if self._task is not None:
            await asyncio.gather(self._task, return_exceptions=True)

    def _notify(self) -> None:
        self._changed.set()
        self._changed = asyncio.Event()

    def _start(self) -> None:
        if self._task is None and self._users and self._url and not self._closed:
            self._task = self._create_task(self._read())
            self._task.add_done_callback(self._reader_done)

    def _stop(self) -> None:
        self._image = None
        self._notify()
        if self._task is not None:
            self._task.cancel()

    def _reader_done(self, task: asyncio.Task[None]) -> None:
        # A replacement reader must wait for cancellation to close the old socket.
        self._task = None
        if not task.cancelled() and (error := task.exception()) is not None:
            _LOGGER.error("Camera reader stopped unexpectedly", exc_info=error)
            return
        self._start()

    async def _read(self) -> None:
        """Read JPEG markers as HA's MJPEG snapshot reader does, with a size cap."""
        timeout = aiohttp.ClientTimeout(
            total=None, sock_connect=READ_TIMEOUT, sock_read=READ_TIMEOUT
        )
        while True:
            try:
                async with self._session.get(self._url, timeout=timeout) as response:
                    response.raise_for_status()
                    buffer = bytearray()
                    async for chunk in response.content.iter_chunked(16384):
                        buffer.extend(chunk)
                        while buffer:
                            start = buffer.find(b"\xff\xd8")
                            if start < 0:
                                # Retain a split JPEG start marker, not MIME headers.
                                buffer[:] = buffer[-1:] if buffer[-1] == 0xFF else b""
                                break
                            if start:
                                del buffer[:start]
                            end = buffer.find(b"\xff\xd9", 2)
                            if end < 0:
                                if len(buffer) > MAX_FRAME_SIZE:
                                    raise ValueError("Camera frame exceeds size limit")
                                break
                            if end + 2 > MAX_FRAME_SIZE:
                                raise ValueError("Camera frame exceeds size limit")
                            self._image = bytes(buffer[: end + 2])
                            del buffer[: end + 2]
                            self._image_time = time.monotonic()
                            self._sequence += 1
                            self._notify()
            except (aiohttp.ClientError, TimeoutError, ValueError) as err:
                _LOGGER.debug(
                    "Camera stream interrupted (%s); retrying", type(err).__name__
                )
            # Do not serve old images as live while the upstream reconnects.
            self._image = None
            await asyncio.sleep(RETRY_DELAY)
