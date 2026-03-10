# [invalid-envvar-default (PLW1508)](#invalid-envvar-default-plw1508)

Added in [v0.0.255](https://github.com/astral-sh/ruff/releases/tag/v0.0.255) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-envvar-default%27%20OR%20PLW1508)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Finvalid_envvar_default.rs#L35)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for `os.getenv` calls with invalid default values.

## [Why is this bad?](#why-is-this-bad)

If an environment variable is set, `os.getenv` will return its value as
a string. If the environment variable is *not* set, `os.getenv` will
return `None`, or the default value if one is provided.

If the default value is not a string or `None`, then it will be
inconsistent with the return type of `os.getenv`, which can lead to
confusing behavior.

## [Example](#example)

```
import os

int(os.getenv("FOO", 1))
```

Use instead:

```
import os

int(os.getenv("FOO", "1"))
```