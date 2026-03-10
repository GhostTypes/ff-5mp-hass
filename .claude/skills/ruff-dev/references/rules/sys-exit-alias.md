# [sys-exit-alias (PLR1722)](#sys-exit-alias-plr1722)

Added in [v0.0.156](https://github.com/astral-sh/ruff/releases/tag/v0.0.156) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27sys-exit-alias%27%20OR%20PLR1722)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fsys_exit_alias.rs#L52)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of the `exit()` and `quit()`.

## [Why is this bad?](#why-is-this-bad)

`exit` and `quit` come from the `site` module, which is typically imported
automatically during startup. However, it is not *guaranteed* to be
imported, and so using these functions may result in a `NameError` at
runtime. Generally, these constants are intended to be used in an interactive
interpreter, and not in programs.

Prefer `sys.exit()`, as the `sys` module is guaranteed to exist in all
contexts.

## [Fix safety](#fix-safety)

This fix is always unsafe. When replacing `exit` or `quit` with `sys.exit`,
the behavior can change in the following ways:

1. If the code runs in an environment where the `site` module is not imported
   (e.g., with `python -S`), the original code would raise a `NameError`, while
   the fixed code would execute normally.
2. `site.exit` and `sys.exit` handle tuple arguments differently. `site.exit`
   treats tuples as regular objects and always returns exit code 1, while `sys.exit`
   interprets tuple contents to determine the exit code: an empty tuple () results in
   exit code 0, and a single-element tuple like (2,) uses that element's value (2) as
   the exit code.

## [Example](#example)

```
if __name__ == "__main__":
    exit()
```

Use instead:

```
import sys

if __name__ == "__main__":
    sys.exit()
```

## [References](#references)

* [Python documentation: Constants added by the `site` module](https://docs.python.org/3/library/constants.html#constants-added-by-the-site-module)