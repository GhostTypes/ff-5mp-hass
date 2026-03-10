# [docstring-missing-yields (DOC402)](#docstring-missing-yields-doc402)

Preview (since [0.5.7](https://github.com/astral-sh/ruff/releases/tag/0.5.7)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27docstring-missing-yields%27%20OR%20DOC402)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydoclint%2Frules%2Fcheck_docstring.rs#L221)

Derived from the **[pydoclint](../#pydoclint-doc)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for functions with `yield` statements that do not have "Yields" sections in
their docstrings.

## [Why is this bad?](#why-is-this-bad)

A missing "Yields" section is a sign of incomplete documentation.

This rule is not enforced for abstract methods or functions that only yield `None`.
It is also ignored for "stub functions": functions where the body only consists
of `pass`, `...`, `raise NotImplementedError`, or similar.

## [Example](#example)

```
def count_to_n(n: int) -> int:
    """Generate integers up to *n*.

    Args:
        n: The number at which to stop counting.
    """
    for i in range(1, n + 1):
        yield i
```

Use instead:

```
def count_to_n(n: int) -> int:
    """Generate integers up to *n*.

    Args:
        n: The number at which to stop counting.

    Yields:
        int: The number we're at in the count.
    """
    for i in range(1, n + 1):
        yield i
```