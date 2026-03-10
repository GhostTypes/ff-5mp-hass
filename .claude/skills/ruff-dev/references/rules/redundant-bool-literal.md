# [redundant-bool-literal (RUF038)](#redundant-bool-literal-ruf038)

Preview (since [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27redundant-bool-literal%27%20OR%20RUF038)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fredundant_bool_literal.rs#L57)

Fix is sometimes available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for `Literal[True, False]` type annotations.

## [Why is this bad?](#why-is-this-bad)

`Literal[True, False]` can be replaced with `bool` in type annotations,
which has the same semantic meaning but is more concise and readable.

`bool` type has exactly two constant instances: `True` and `False`. Static
type checkers such as [mypy](https://github.com/python/mypy/blob/master/mypy/typeops.py#L985) treat `Literal[True, False]` as equivalent to
`bool` in a type annotation.

## [Example](#example)

```
from typing import Literal

x: Literal[True, False]
y: Literal[True, False, "hello", "world"]
```

Use instead:

```
from typing import Literal

x: bool
y: Literal["hello", "world"] | bool
```

## [Fix safety](#fix-safety)

The fix for this rule is marked as unsafe, as it may change the semantics of the code.
Specifically:

* Type checkers may not treat `bool` as equivalent when overloading boolean arguments
  with `Literal[True]` and `Literal[False]` (see, e.g., [#14764](https://github.com/python/mypy/issues/14764) and [#5421](https://github.com/microsoft/pyright/issues/5421)).
* `bool` is not strictly equivalent to `Literal[True, False]`, as `bool` is
  a subclass of `int`, and this rule may not apply if the type annotations are used
  in a numeric context.

Further, the `Literal` slice may contain trailing-line comments which the fix would remove.

## [References](#references)

* [Typing documentation: Legal parameters for `Literal` at type check time](https://typing.python.org/en/latest/spec/literal.html#legal-parameters-for-literal-at-type-check-time)
* [Python documentation: Boolean type - `bool`](https://docs.python.org/3/library/stdtypes.html#boolean-type-bool)