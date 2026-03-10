# [exc-info-outside-except-handler (LOG014)](#exc-info-outside-except-handler-log014)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27exc-info-outside-except-handler%27%20OR%20LOG014)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_logging%2Frules%2Fexc_info_outside_except_handler.rs#L46)

Derived from the **[flake8-logging](../#flake8-logging-log)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for logging calls with `exc_info=` outside exception handlers.

## [Why is this bad?](#why-is-this-bad)

Using `exc_info=True` outside of an exception handler
attaches `None` as the exception information, leading to confusing messages:

```
>>> logging.warning("Uh oh", exc_info=True)
WARNING:root:Uh oh
NoneType: None
```

## [Example](#example)

```
import logging


logging.warning("Foobar", exc_info=True)
```

Use instead:

```
import logging


logging.warning("Foobar")
```

## [Fix safety](#fix-safety)

The fix is always marked as unsafe, as it changes runtime behavior.