# [runtime-string-union (TC010)](#runtime-string-union-tc010)

Added in [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27runtime-string-union%27%20OR%20TC010)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_type_checking%2Frules%2Fruntime_string_union.rs#L55)

Derived from the **[flake8-type-checking](../#flake8-type-checking-tc)** linter.

## [What it does](#what-it-does)

Checks for the presence of string literals in `X | Y`-style union types.

## [Why is this bad?](#why-is-this-bad)

[PEP 604](https://peps.python.org/pep-0604/) introduced a new syntax for union type annotations based on the
`|` operator.

While Python's type annotations can typically be wrapped in strings to
avoid runtime evaluation, the use of a string member within an `X | Y`-style
union type will cause a runtime error.

Instead, remove the quotes, wrap the *entire* union in quotes, or use
`from __future__ import annotations` to disable runtime evaluation of
annotations entirely.

## [Example](#example)

```
var: "Foo" | None


class Foo: ...
```

Use instead:

```
from __future__ import annotations

var: Foo | None


class Foo: ...
```

Or, extend the quotes to include the entire union:

```
var: "Foo | None"


class Foo: ...
```

## [References](#references)

* [PEP 563 - Postponed Evaluation of Annotations](https://peps.python.org/pep-0563/)
* [PEP 604 – Allow writing union types as `X | Y`](https://peps.python.org/pep-0604/)