# [blocking-http-call-httpx-in-async-function (ASYNC212)](#blocking-http-call-httpx-in-async-function-async212)

Preview (since [0.12.11](https://github.com/astral-sh/ruff/releases/tag/0.12.11)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27blocking-http-call-httpx-in-async-function%27%20OR%20ASYNC212)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_async%2Frules%2Fblocking_http_call_httpx.rs#L39)

Derived from the **[flake8-async](../#flake8-async-async)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks that async functions do not use blocking httpx clients.

## [Why is this bad?](#why-is-this-bad)

Blocking an async function via a blocking HTTP call will block the entire
event loop, preventing it from executing other tasks while waiting for the
HTTP response, negating the benefits of asynchronous programming.

Instead of using the blocking `httpx` client, use the asynchronous client.

## [Example](#example)

```
import httpx


async def fetch():
    client = httpx.Client()
    response = client.get(...)
```

Use instead:

```
import httpx


async def fetch():
    async with httpx.AsyncClient() as client:
        response = await client.get(...)
```