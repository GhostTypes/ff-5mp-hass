# [non-capitalized-section-name (D405)](#non-capitalized-section-name-d405)

Added in [v0.0.71](https://github.com/astral-sh/ruff/releases/tag/v0.0.71) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27non-capitalized-section-name%27%20OR%20D405)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fsections.rs#L281)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for section headers in docstrings that do not begin with capital
letters.

## [Why is this bad?](#why-is-this-bad)

For stylistic consistency, all section headers in a docstring should be
capitalized.

Multiline docstrings are typically composed of a summary line, followed by
a blank line, followed by a series of sections. Each section typically has
a header and a body.

This rule is enabled when using the `numpy` and `google` conventions, and
disabled when using the `pep257` convention.

## [Example](#example)

```
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    args:
        distance: Distance traveled.
        time: Time spent traveling.

    returns:
        Speed as distance divided by time.

    raises:
        FasterThanLightError: If speed is greater than the speed of light.
    """
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
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

    Raises:
        FasterThanLightError: If speed is greater than the speed of light.
    """
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
```

## [Options](#options)

* [`lint.pydocstyle.convention`](../../settings/#lint_pydocstyle_convention)

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [PEP 287 – reStructuredText Docstring Format](https://peps.python.org/pep-0287/)
* [NumPy Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
* [Google Python Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)