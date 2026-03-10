# [direct-logger-instantiation (LOG001)](#direct-logger-instantiation-log001)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27direct-logger-instantiation%27%20OR%20LOG001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_logging%2Frules%2Fdirect_logger_instantiation.rs#L44)

Derived from the **[flake8-logging](../#flake8-logging-log)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for direct instantiation of `logging.Logger`, as opposed to using
`logging.getLogger()`.

## [Why is this bad?](#why-is-this-bad)

The [Logger Objects](https://docs.python.org/3/library/logging.html#logger-objects) documentation states that:

> Note that Loggers should NEVER be instantiated directly, but always
> through the module-level function `logging.getLogger(name)`.

If a logger is directly instantiated, it won't be added to the logger
tree, and will bypass all configuration. Messages logged to it will
only be sent to the "handler of last resort", skipping any filtering
or formatting.

## [Example](#example)

```
import logging

logger = logging.Logger(__name__)
```

Use instead:

```
import logging

logger = logging.getLogger(__name__)
```

## [Fix safety](#fix-safety)

This fix is always unsafe, as changing from `Logger` to `getLogger`
changes program behavior by will adding the logger to the logging tree.