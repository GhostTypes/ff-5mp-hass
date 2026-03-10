# [docstring-missing-returns (DOC201)](#docstring-missing-returns-doc201)

Preview (since [0.5.6](https://github.com/astral-sh/ruff/releases/tag/0.5.6)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27docstring-missing-returns%27%20OR%20DOC201)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydoclint%2Frules%2Fcheck_docstring.rs#L116)

Derived from the **[pydoclint](../#pydoclint-doc)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for functions with `return` statements that do not have "Returns"
sections in their docstrings.

## [Why is this bad?](#why-is-this-bad)

A missing "Returns" section is a sign of incomplete documentation.

This rule is not enforced for abstract methods or functions that only return
`None`. It is also ignored for "stub functions": functions where the body only
consists of `pass`, `...`, `raise NotImplementedError`, or similar.

## [Example](#example)

```
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    Args:
        distance: Distance traveled.
        time: Time spent traveling.
    """
    return distance / time
```

Use instead:

```
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    Args:
        distance: Distance traveled.
        time: Time spent traveling.

    Returns:
        Speed as distance divided by time.
    """
    return distance / time
```