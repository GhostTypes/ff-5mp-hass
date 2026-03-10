# [docstring-extraneous-exception (DOC502)](#docstring-extraneous-exception-doc502)

Preview (since [0.5.5](https://github.com/astral-sh/ruff/releases/tag/0.5.5)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27docstring-extraneous-exception%27%20OR%20DOC502)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydoclint%2Frules%2Fcheck_docstring.rs#L413)

Derived from the **[pydoclint](../#pydoclint-doc)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for function docstrings that state that exceptions could be raised
even though they are not directly raised in the function body.

## [Why is this bad?](#why-is-this-bad)

Some conventions prefer non-explicit exceptions be omitted from the
docstring.

This rule is not enforced for abstract methods. It is also ignored for
"stub functions": functions where the body only consists of `pass`, `...`,
`raise NotImplementedError`, or similar.

## [Example](#example)

```
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    Args:
        distance: Distance traveled.
        time: Time spent traveling.

    Returns:
        Speed as distance divided by time.

    Raises:
        ZeroDivisionError: Divided by zero.
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

## [Known issues](#known-issues)

It may often be desirable to document *all* exceptions that a function
could possibly raise, even those which are not explicitly raised using
`raise` statements in the function body.