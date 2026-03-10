# [root-logger-call (LOG015)](#root-logger-call-log015)

Added in [0.10.0](https://github.com/astral-sh/ruff/releases/tag/0.10.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27root-logger-call%27%20OR%20LOG015)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_logging%2Frules%2Froot_logger_call.rs#L30)

Derived from the **[flake8-logging](../#flake8-logging-log)** linter.

## [What it does](#what-it-does)

Checks for usages of the following `logging` top-level functions:
`debug`, `info`, `warn`, `warning`, `error`, `critical`, `log`, `exception`.

## [Why is this bad?](#why-is-this-bad)

Using the root logger causes the messages to have no source information,
making them less useful for debugging.

## [Example](#example)

```
import logging

logging.info("Foobar")
```

Use instead:

```
import logging

logger = logging.getLogger(__name__)
logger.info("Foobar")
```