# [missing-section-name-colon (D416)](#missing-section-name-colon-d416)

Added in [v0.0.74](https://github.com/astral-sh/ruff/releases/tag/v0.0.74) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-section-name-colon%27%20OR%20D416)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fsections.rs#L1152)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for docstring section headers that do not end with a colon.

## [Why is this bad?](#why-is-this-bad)

This rule enforces a consistent style for multiline Google-style
docstrings. If a multiline Google-style docstring consists of multiple
sections, each section header should end with a colon.

Multiline docstrings are typically composed of a summary line, followed by
a blank line, followed by a series of sections, each with a section header
and a section body.

This rule is enabled when using the `google` convention, and disabled when
using the `pep257` and `numpy` conventions.

## [Example](#example)

```
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    Args
        distance: Distance traveled.
        time: Time spent traveling.

    Returns
        Speed as distance divided by time.

    Raises
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
* [Google Style Guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)