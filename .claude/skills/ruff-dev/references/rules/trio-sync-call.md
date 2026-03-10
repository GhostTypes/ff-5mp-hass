# [trio-sync-call (ASYNC105)](#trio-sync-call-async105)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27trio-sync-call%27%20OR%20ASYNC105)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_async%2Frules%2Fsync_call.rs#L40)

Derived from the **[flake8-async](../#flake8-async-async)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for calls to trio functions that are not immediately awaited.

## [Why is this bad?](#why-is-this-bad)

Many of the functions exposed by trio are asynchronous, and must be awaited
to take effect. Calling a trio function without an `await` can lead to
`RuntimeWarning` diagnostics and unexpected behaviour.

## [Example](#example)

```
import trio


async def double_sleep(x):
    trio.sleep(2 * x)
```

Use instead:

```
import trio


async def double_sleep(x):
    await trio.sleep(2 * x)
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as adding an `await` to a function
call changes its semantics and runtime behavior.