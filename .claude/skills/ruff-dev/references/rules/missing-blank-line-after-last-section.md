# [missing-blank-line-after-last-section (D413)](#missing-blank-line-after-last-section-d413)

Added in [v0.0.71](https://github.com/astral-sh/ruff/releases/tag/v0.0.71) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-blank-line-after-last-section%27%20OR%20D413)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fsections.rs#L984)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for missing blank lines after the last section of a multiline
docstring.

## [Why is this bad?](#why-is-this-bad)

This rule enforces a consistent style for multiline docstrings.

Multiline docstrings are typically composed of a summary line, followed by
a blank line, followed by a series of sections, each with a section header
and a section body.

This rule may not apply to all projects; its applicability is a matter of
convention. By default, the rule is disabled when using the `google`,
`numpy`, and `pep257` conventions.

## [Example](#example)

```
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    Parameters
    ----------
    distance : float
        Distance traveled.
    time : float
        Time spent traveling.
    Returns
    -------
    float
        Speed as distance divided by time.
    Raises
    ------
    FasterThanLightError
        If speed is greater than the speed of light.
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

    Parameters
    ----------
    distance : float
        Distance traveled.
    time : float
        Time spent traveling.

    Returns
    -------
    float
        Speed as distance divided by time.

    Raises
    ------
    FasterThanLightError
        If speed is greater than the speed of light.

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