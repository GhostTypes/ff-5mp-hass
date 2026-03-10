# [type-alias-without-annotation (PYI026)](#type-alias-without-annotation-pyi026)

Added in [v0.0.279](https://github.com/astral-sh/ruff/releases/tag/v0.0.279) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27type-alias-without-annotation%27%20OR%20PYI026)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fsimple_defaults.rs#L237)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for type alias definitions that are not annotated with
`typing.TypeAlias`.

## [Why is this bad?](#why-is-this-bad)

In Python, a type alias is defined by assigning a type to a variable (e.g.,
`Vector = list[float]`).

It's best to annotate type aliases with the `typing.TypeAlias` type to
make it clear that the statement is a type alias declaration, as opposed
to a normal variable assignment.

## [Example](#example)

```
Vector = list[float]
```

Use instead:

```
from typing import TypeAlias

Vector: TypeAlias = list[float]
```

## [Availability](#availability)

Because this rule relies on the third-party `typing_extensions` module for Python versions
before 3.10, its diagnostic will not be emitted, and no fix will be offered, if
`typing_extensions` imports have been disabled by the [`lint.typing-extensions`](../../settings/#lint_typing-extensions) linter option.

## [Options](#options)

* [`lint.typing-extensions`](../../settings/#lint_typing-extensions)