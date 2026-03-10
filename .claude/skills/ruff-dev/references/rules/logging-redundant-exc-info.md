# [logging-redundant-exc-info (G202)](#logging-redundant-exc-info-g202)

Added in [v0.0.236](https://github.com/astral-sh/ruff/releases/tag/v0.0.236) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27logging-redundant-exc-info%27%20OR%20G202)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_logging_format%2Fviolations.rs#L581)

Derived from the **[flake8-logging-format](../#flake8-logging-format-g)** linter.

## [What it does](#what-it-does)

Checks for redundant `exc_info` keyword arguments in logging statements.

## [Why is this bad?](#why-is-this-bad)

`exc_info` is `True` by default for `logging.exception`, and `False` by
default for `logging.error`.

Passing `exc_info=True` to `logging.exception` calls is redundant, as is
passing `exc_info=False` to `logging.error` calls.

## [Known problems](#known-problems)

This rule detects uses of the `logging` module via a heuristic.
Specifically, it matches against:

* Uses of the `logging` module itself (e.g., `import logging; logging.info(...)`).
* Uses of `flask.current_app.logger` (e.g., `from flask import current_app; current_app.logger.info(...)`).
* Objects whose name starts with `log` or ends with `logger` or `logging`,
  when used in the same file in which they are defined (e.g., `logger = logging.getLogger(); logger.info(...)`).
* Imported objects marked as loggers via the [`lint.logger-objects`](../../settings/#lint_logger-objects) setting, which can be
  used to enforce these rules against shared logger objects (e.g., `from module import logger; logger.info(...)`,
  when [`lint.logger-objects`](../../settings/#lint_logger-objects) is set to `["module.logger"]`).

## [Example](#example)

```
import logging

try:
    ...
except ValueError:
    logging.exception("Exception occurred", exc_info=True)
```

Use instead:

```
import logging

try:
    ...
except ValueError:
    logging.exception("Exception occurred")
```

## [Options](#options)

* [`lint.logger-objects`](../../settings/#lint_logger-objects)

## [References](#references)

* [Python documentation: `logging.exception`](https://docs.python.org/3/library/logging.html#logging.exception)
* [Python documentation: `exception`](https://docs.python.org/3/library/logging.html#logging.Logger.exception)
* [Python documentation: `logging.error`](https://docs.python.org/3/library/logging.html#logging.error)
* [Python documentation: `error`](https://docs.python.org/3/library/logging.html#logging.Logger.error)