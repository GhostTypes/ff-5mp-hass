# [builtin-import-shadowing (A004)](#builtin-import-shadowing-a004)

Added in [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27builtin-import-shadowing%27%20OR%20A004)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_builtins%2Frules%2Fbuiltin_import_shadowing.rs#L43)

Derived from the **[flake8-builtins](../#flake8-builtins-a)** linter.

## [What it does](#what-it-does)

Checks for imports that use the same names as builtins.

## [Why is this bad?](#why-is-this-bad)

Reusing a builtin for the name of an import increases the difficulty
of reading and maintaining the code, and can cause non-obvious errors,
as readers may mistake the variable for the builtin and vice versa.

Builtins can be marked as exceptions to this rule via the
[`lint.flake8-builtins.ignorelist`](../../settings/#lint_flake8-builtins_ignorelist) configuration option.

## [Example](#example)

```
from rich import print

print("Some message")
```

Use instead:

```
from rich import print as rich_print

rich_print("Some message")
```

or:

```
import rich

rich.print("Some message")
```

## [Options](#options)

* [`lint.flake8-builtins.ignorelist`](../../settings/#lint_flake8-builtins_ignorelist)
* [`target-version`](../../settings/#target-version)