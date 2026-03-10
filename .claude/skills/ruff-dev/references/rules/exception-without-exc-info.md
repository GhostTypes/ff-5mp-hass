# [exception-without-exc-info (LOG007)](#exception-without-exc-info-log007)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27exception-without-exc-info%27%20OR%20LOG007)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_logging%2Frules%2Fexception_without_exc_info.rs#L33)

Derived from the **[flake8-logging](../#flake8-logging-log)** linter.

## [What it does](#what-it-does)

Checks for uses of `logging.exception()` with `exc_info` set to `False`.

## [Why is this bad?](#why-is-this-bad)

The `logging.exception()` method captures the exception automatically, but
accepts an optional `exc_info` argument to override this behavior. Setting
`exc_info` to `False` disables the automatic capture of the exception and
stack trace.

Instead of setting `exc_info` to `False`, prefer `logging.error()`, which
has equivalent behavior to `logging.exception()` with `exc_info` set to
`False`, but is clearer in intent.

## [Example](#example)

```
logging.exception("...", exc_info=False)
```

Use instead:

```
logging.error("...")
```