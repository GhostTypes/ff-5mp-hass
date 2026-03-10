# [deprecated-log-warn (PGH002)](#deprecated-log-warn-pgh002)

Removed (since [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27deprecated-log-warn%27%20OR%20PGH002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpygrep_hooks%2Frules%2Fdeprecated_log_warn.rs#L36)

Derived from the **[pygrep-hooks](../#pygrep-hooks-pgh)** linter.

**Warning: This rule has been removed and its documentation is only available for historical reasons.**

Fix is sometimes available.

## [Removed](#removed)

This rule is identical to [G010](https://docs.astral.sh/ruff/rules/logging-warn/) which should be used instead.

## [What it does](#what-it-does)

Check for usages of the deprecated `warn` method from the `logging` module.

## [Why is this bad?](#why-is-this-bad)

The `warn` method is deprecated. Use `warning` instead.

## [Example](#example)

```
import logging


def foo():
    logging.warn("Something happened")
```

Use instead:

```
import logging


def foo():
    logging.warning("Something happened")
```

## [References](#references)

* [Python documentation: `logger.Logger.warning`](https://docs.python.org/3/library/logging.html#logging.Logger.warning)