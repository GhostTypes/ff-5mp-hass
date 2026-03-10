# [line-contains-hack (FIX004)](#line-contains-hack-fix004)

Added in [v0.0.272](https://github.com/astral-sh/ruff/releases/tag/v0.0.272) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27line-contains-hack%27%20OR%20FIX004)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_fixme%2Frules%2Ftodos.rs#L112)

Derived from the **[flake8-fixme](../#flake8-fixme-fix)** linter.

## [What it does](#what-it-does)

Checks for "HACK" comments.

## [Why is this bad?](#why-is-this-bad)

"HACK" comments are used to describe an issue that should be resolved
(usually, a suboptimal solution or temporary workaround).

Consider resolving the issue before deploying the code.

Note that if you use "HACK" comments as a form of documentation, this
rule may not be appropriate for your project.

## [Example](#example)

```
import os


def running_windows():  # HACK: Use platform module instead.
    try:
        os.mkdir("C:\\Windows\\System32\\")
    except FileExistsError:
        return True
    else:
        os.rmdir("C:\\Windows\\System32\\")
        return False
```