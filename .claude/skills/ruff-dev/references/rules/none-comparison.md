# [none-comparison (E711)](#none-comparison-e711)

Added in [v0.0.28](https://github.com/astral-sh/ruff/releases/tag/v0.0.28) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27none-comparison%27%20OR%20E711)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fliteral_comparisons.rs#L60)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for comparisons to `None` which are not using the `is` operator.

## [Why is this bad?](#why-is-this-bad)

According to [PEP 8](https://peps.python.org/pep-0008/#programming-recommendations), "Comparisons to singletons like None should always be done with
`is` or `is not`, never the equality operators."

## [Example](#example)

```
if arg != None:
    pass
if None == arg:
    pass
```

Use instead:

```
if arg is not None:
    pass
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as it may alter runtime behavior when
used with libraries that override the `==`/`__eq__` or `!=`/`__ne__` operators.
In these cases, `is`/`is not` may not be equivalent to `==`/`!=`. For more
information, see [this issue](https://github.com/astral-sh/ruff/issues/4560).