# [docstring-missing-exception (DOC501)](#docstring-missing-exception-doc501)

Preview (since [0.5.5](https://github.com/astral-sh/ruff/releases/tag/0.5.5)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27docstring-missing-exception%27%20OR%20DOC501)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydoclint%2Frules%2Fcheck_docstring.rs#L345)

Derived from the **[pydoclint](../#pydoclint-doc)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for function docstrings that do not document all explicitly raised
exceptions.

## [Why is this bad?](#why-is-this-bad)

A function should document all exceptions that are directly raised in some
circumstances. Failing to document an exception that could be raised
can be misleading to users and/or a sign of incomplete documentation.

This rule is not enforced for abstract methods. It is also ignored for
"stub functions": functions where the body only consists of `pass`, `...`,
`raise NotImplementedError`, or similar.

## [Example](#example)

```
class FasterThanLightError(ArithmeticError): ...


def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    Args:
        distance: Distance traveled.
        time: Time spent traveling.

    Returns:
        Speed as distance divided by time.
    """
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
```

Use instead:

```
class FasterThanLightError(ArithmeticError): ...


def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    Args:
        distance: Distance traveled.
        time: Time spent traveling.

    Returns:
        Speed as distance divided by time.

    Raises:
        FasterThanLightError: If speed is greater than the speed of light.
    """
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
```