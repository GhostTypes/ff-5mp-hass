# [undocumented-param (D417)](#undocumented-param-d417)

Added in [v0.0.73](https://github.com/astral-sh/ruff/releases/tag/v0.0.73) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27undocumented-param%27%20OR%20D417)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fsections.rs#L1242)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

## [What it does](#what-it-does)

Checks for function docstrings that do not include documentation for all
parameters in the function.

## [Why is this bad?](#why-is-this-bad)

This rule helps prevent you from leaving Google-style docstrings unfinished
or incomplete. Multiline Google-style docstrings should describe all
parameters for the function they are documenting.

Multiline docstrings are typically composed of a summary line, followed by
a blank line, followed by a series of sections, each with a section header
and a section body. Function docstrings often include a section for
function arguments; this rule is concerned with that section only.
Note that this rule only checks docstrings with an arguments (e.g. `Args`) section.

This rule is enabled when using the `google` convention, and disabled when
using the `pep257` and `numpy` conventions.

Parameters annotated with `typing.Unpack` are exempt from this rule.
This follows the Python typing specification for unpacking keyword arguments.

## [Example](#example)

```
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    Args:
        distance: Distance traveled.

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
* [`lint.pydocstyle.ignore-var-parameters`](../../settings/#lint_pydocstyle_ignore-var-parameters)

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [PEP 287 – reStructuredText Docstring Format](https://peps.python.org/pep-0287/)
* [Google Python Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
* [Python - Unpack for keyword arguments](https://typing.python.org/en/latest/spec/callables.html#unpack-kwargs)