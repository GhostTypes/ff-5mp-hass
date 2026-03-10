# [undocumented-warn (LOG009)](#undocumented-warn-log009)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27undocumented-warn%27%20OR%20LOG009)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_logging%2Frules%2Fundocumented_warn.rs#L35)

Derived from the **[flake8-logging](../#flake8-logging-log)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of `logging.WARN`.

## [Why is this bad?](#why-is-this-bad)

The `logging.WARN` constant is an undocumented alias for `logging.WARNING`.

Although it’s not explicitly deprecated, `logging.WARN` is not mentioned
in the `logging` documentation. Prefer `logging.WARNING` instead.

## [Example](#example)

```
import logging


logging.basicConfig(level=logging.WARN)
```

Use instead:

```
import logging


logging.basicConfig(level=logging.WARNING)
```