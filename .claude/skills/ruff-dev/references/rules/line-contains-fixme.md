# [line-contains-fixme (FIX001)](#line-contains-fixme-fix001)

Added in [v0.0.272](https://github.com/astral-sh/ruff/releases/tag/v0.0.272) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27line-contains-fixme%27%20OR%20FIX001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_fixme%2Frules%2Ftodos.rs#L52)

Derived from the **[flake8-fixme](../#flake8-fixme-fix)** linter.

## [What it does](#what-it-does)

Checks for "FIXME" comments.

## [Why is this bad?](#why-is-this-bad)

"FIXME" comments are used to describe an issue that should be resolved
(usually, a bug or unexpected behavior).

Consider resolving the issue before deploying the code.

Note that if you use "FIXME" comments as a form of documentation, this
rule may not be appropriate for your project.

## [Example](#example)

```
def speed(distance, time):
    return distance / time  # FIXME: Raises ZeroDivisionError for time = 0.
```