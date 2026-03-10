# [invalid-get-logger-argument (LOG002)](#invalid-get-logger-argument-log002)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-get-logger-argument%27%20OR%20LOG002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_logging%2Frules%2Finvalid_get_logger_argument.rs#L47)

Derived from the **[flake8-logging](../#flake8-logging-log)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for any usage of `__cached__` and `__file__` as an argument to
`logging.getLogger()`.

## [Why is this bad?](#why-is-this-bad)

The [logging documentation](https://docs.python.org/3/library/logging.html#logger-objects) recommends this pattern:

```
logging.getLogger(__name__)
```

Here, `__name__` is the fully qualified module name, such as `foo.bar`,
which is the intended format for logger names.

This rule detects probably-mistaken usage of similar module-level dunder constants:

* `__cached__` - the pathname of the module's compiled version, such as `foo/__pycache__/bar.cpython-311.pyc`.
* `__file__` - the pathname of the module, such as `foo/bar.py`.

## [Example](#example)

```
import logging

logger = logging.getLogger(__file__)
```

Use instead:

```
import logging

logger = logging.getLogger(__name__)
```

## [Fix safety](#fix-safety)

This fix is always unsafe, as changing the arguments to `getLogger` can change the
received logger object, and thus program behavior.