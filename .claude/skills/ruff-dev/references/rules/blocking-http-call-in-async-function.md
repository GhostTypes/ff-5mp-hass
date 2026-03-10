# [blocking-http-call-in-async-function (ASYNC210)](#blocking-http-call-in-async-function-async210)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27blocking-http-call-in-async-function%27%20OR%20ASYNC210)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_async%2Frules%2Fblocking_http_call.rs#L40)

Derived from the **[flake8-async](../#flake8-async-async)** linter.

## [What it does](#what-it-does)

Checks that async functions do not contain blocking HTTP calls.

## [Why is this bad?](#why-is-this-bad)

Blocking an async function via a blocking HTTP call will block the entire
event loop, preventing it from executing other tasks while waiting for the
HTTP response, negating the benefits of asynchronous programming.

Instead of making a blocking HTTP call, use an asynchronous HTTP client
library such as `aiohttp` or `httpx`.

## [Example](#example)

```
import urllib


async def fetch():
    urllib.request.urlopen("https://example.com/foo/bar").read()
```

Use instead:

```
import aiohttp


async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://example.com/foo/bar") as resp:
            ...
```