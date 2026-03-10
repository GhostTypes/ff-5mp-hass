# [docstring-extraneous-parameter (DOC102)](#docstring-extraneous-parameter-doc102)

Preview (since [0.14.1](https://github.com/astral-sh/ruff/releases/tag/0.14.1)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27docstring-extraneous-parameter%27%20OR%20DOC102)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydoclint%2Frules%2Fcheck_docstring.rs#L61)

Derived from the **[pydoclint](../#pydoclint-doc)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for function docstrings that include parameters which are not
in the function signature.

## [Why is this bad?](#why-is-this-bad)

If a docstring documents a parameter which is not in the function signature,
it can be misleading to users and/or a sign of incomplete documentation or
refactors.

## [Example](#example)

```
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    Args:
        distance: Distance traveled.
        time: Time spent traveling.
        acceleration: Rate of change of speed.

    Returns:
        Speed as distance divided by time.
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