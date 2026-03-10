# [uncapitalized-environment-variables (SIM112)](#uncapitalized-environment-variables-sim112)

Added in [v0.0.218](https://github.com/astral-sh/ruff/releases/tag/v0.0.218) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27uncapitalized-environment-variables%27%20OR%20SIM112)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fast_expr.rs#L43)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Check for environment variables that are not capitalized.

## [Why is this bad?](#why-is-this-bad)

By convention, environment variables should be capitalized.

On Windows, environment variables are case-insensitive and are converted to
uppercase, so using lowercase environment variables can lead to subtle bugs.

## [Example](#example)

```
import os

os.environ["foo"]
```

Use instead:

```
import os

os.environ["FOO"]
```

## [Fix safety](#fix-safety)

This fix is always marked as unsafe because automatically capitalizing environment variable names
can change program behavior in environments where the variable names are case-sensitive, such as most
Unix-like systems.

## [References](#references)

* [Python documentation: `os.environ`](https://docs.python.org/3/library/os.html#os.environ)