# [undefined-export (F822)](#undefined-export-f822)

Added in [v0.0.25](https://github.com/astral-sh/ruff/releases/tag/v0.0.25) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27undefined-export%27%20OR%20F822)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fundefined_export.rs#L42)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for undefined names in `__all__`.

## [Why is this bad?](#why-is-this-bad)

In Python, the `__all__` variable is used to define the names that are
exported when a module is imported as a wildcard (e.g.,
`from foo import *`). The names in `__all__` must be defined in the module,
but are included as strings.

Including an undefined name in `__all__` is likely to raise `NameError` at
runtime, when the module is imported.

In [preview](https://docs.astral.sh/ruff/preview/), this rule will flag undefined names in `__init__.py` file,
even if those names implicitly refer to other modules in the package. Users
that rely on implicit exports should disable this rule in `__init__.py`
files via [`lint.per-file-ignores`](../../settings/#lint_per-file-ignores).

## [Example](#example)

```
from foo import bar


__all__ = ["bar", "baz"]  # undefined name `baz` in `__all__`
```

Use instead:

```
from foo import bar, baz


__all__ = ["bar", "baz"]
```

## [References](#references)

* [Python documentation: `__all__`](https://docs.python.org/3/tutorial/modules.html#importing-from-a-package)