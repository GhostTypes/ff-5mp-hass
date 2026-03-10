# [invalid-envvar-value (PLE1507)](#invalid-envvar-value-ple1507)

Added in [v0.0.255](https://github.com/astral-sh/ruff/releases/tag/v0.0.255) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-envvar-value%27%20OR%20PLE1507)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Finvalid_envvar_value.rs#L32)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for `os.getenv` calls with an invalid `key` argument.

## [Why is this bad?](#why-is-this-bad)

`os.getenv` only supports strings as the first argument (`key`).

If the provided argument is not a string, `os.getenv` will throw a
`TypeError` at runtime.

## [Example](#example)

```
import os

os.getenv(1)
```

Use instead:

```
import os

os.getenv("1")
```