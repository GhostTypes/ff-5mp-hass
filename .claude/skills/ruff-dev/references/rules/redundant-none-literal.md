# [redundant-none-literal (PYI061)](#redundant-none-literal-pyi061)

Added in [0.13.0](https://github.com/astral-sh/ruff/releases/tag/0.13.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27redundant-none-literal%27%20OR%20PYI061)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fredundant_none_literal.rs#L51)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for redundant `Literal[None]` annotations.

## [Why is this bad?](#why-is-this-bad)

While `Literal[None]` is a valid type annotation, it is semantically equivalent to `None`.
Prefer `None` over `Literal[None]` for both consistency and readability.

## [Example](#example)

```
from typing import Literal

Literal[None]
Literal[1, 2, 3, "foo", 5, None]
```

Use instead:

```
from typing import Literal

None
Literal[1, 2, 3, "foo", 5] | None
```

## [Fix safety and availability](#fix-safety-and-availability)

This rule's fix is marked as safe unless the literal contains comments.

There is currently no fix available when applying the fix would lead to
a `TypeError` from an expression of the form `None | None` or when we
are unable to import the symbol `typing.Optional` and the Python version
is 3.9 or below.

## [References](#references)

* [Typing documentation: Legal parameters for `Literal` at type check time](https://typing.python.org/en/latest/spec/literal.html#legal-parameters-for-literal-at-type-check-time)