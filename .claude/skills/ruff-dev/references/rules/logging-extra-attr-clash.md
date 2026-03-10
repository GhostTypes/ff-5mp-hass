# [logging-extra-attr-clash (G101)](#logging-extra-attr-clash-g101)

Added in [v0.0.236](https://github.com/astral-sh/ruff/releases/tag/v0.0.236) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27logging-extra-attr-clash%27%20OR%20G101)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_logging_format%2Fviolations.rs#L455)

Derived from the **[flake8-logging-format](../#flake8-logging-format-g)** linter.

## [What it does](#what-it-does)

Checks for `extra` keywords in logging statements that clash with
`LogRecord` attributes.

## [Why is this bad?](#why-is-this-bad)

The `logging` module provides a mechanism for passing additional values to
be logged using the `extra` keyword argument. These values are then passed
to the `LogRecord` constructor.

Providing a value via `extra` that clashes with one of the attributes of
the `LogRecord` constructor will raise a `KeyError` when the `LogRecord` is
constructed.

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

logging.basicConfig(format="%(name) - %(message)s", level=logging.INFO)

username = "Maria"

logging.info("Something happened", extra=dict(name=username))
```

Use instead:

```
import logging

logging.basicConfig(format="%(user_id)s - %(message)s", level=logging.INFO)

username = "Maria"

logging.info("Something happened", extra=dict(user_id=username))
```

## [Options](#options)

* [`lint.logger-objects`](../../settings/#lint_logger-objects)

## [References](#references)

* [Python documentation: LogRecord attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes)