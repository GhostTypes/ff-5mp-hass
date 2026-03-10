# [true-false-comparison (E712)](#true-false-comparison-e712)

Added in [v0.0.28](https://github.com/astral-sh/ruff/releases/tag/v0.0.28) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27true-false-comparison%27%20OR%20E712)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fliteral_comparisons.rs#L123)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for equality comparisons to boolean literals.

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/#programming-recommendations) recommends against using the equality operators `==` and `!=` to
compare values to `True` or `False`.

Instead, use `if cond:` or `if not cond:` to check for truth values.

If you intend to check if a value is the boolean literal `True` or `False`,
consider using `is` or `is not` to check for identity instead.

## [Example](#example)

```
if foo == True:
    ...

if bar == False:
    ...
```

Use instead:

```
if foo:
    ...

if not bar:
    ...
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as it may alter runtime behavior when
used with libraries that override the `==`/`__eq__` or `!=`/`__ne__` operators.
In these cases, `is`/`is not` may not be equivalent to `==`/`!=`. For more
information, see [this issue](https://github.com/astral-sh/ruff/issues/4560).