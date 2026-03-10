# [line-contains-xxx (FIX003)](#line-contains-xxx-fix003)

Added in [v0.0.272](https://github.com/astral-sh/ruff/releases/tag/v0.0.272) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27line-contains-xxx%27%20OR%20FIX003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_fixme%2Frules%2Ftodos.rs#L76)

Derived from the **[flake8-fixme](../#flake8-fixme-fix)** linter.

## [What it does](#what-it-does)

Checks for "XXX" comments.

## [Why is this bad?](#why-is-this-bad)

"XXX" comments are used to describe an issue that should be resolved.

Consider resolving the issue before deploying the code, or, at minimum,
using a more descriptive comment tag (e.g, "TODO").

## [Example](#example)

```
def speed(distance, time):
    return distance / time  # XXX: Raises ZeroDivisionError for time = 0.
```