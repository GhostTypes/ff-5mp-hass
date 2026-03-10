# [long-sleep-not-forever (ASYNC116)](#long-sleep-not-forever-async116)

Added in [0.13.0](https://github.com/astral-sh/ruff/releases/tag/0.13.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27long-sleep-not-forever%27%20OR%20ASYNC116)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_async%2Frules%2Flong_sleep_not_forever.rs#L41)

Derived from the **[flake8-async](../#flake8-async-async)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of `trio.sleep()` or `anyio.sleep()` with a delay greater than 24 hours.

## [Why is this bad?](#why-is-this-bad)

Calling `sleep()` with a delay greater than 24 hours is usually intended
to sleep indefinitely. Instead of using a large delay,
`trio.sleep_forever()` or `anyio.sleep_forever()` better conveys the intent.

## [Example](#example)

```
import trio


async def func():
    await trio.sleep(86401)
```

Use instead:

```
import trio


async def func():
    await trio.sleep_forever()
```

## [Fix safety](#fix-safety)

This fix is marked as unsafe as it changes program behavior.