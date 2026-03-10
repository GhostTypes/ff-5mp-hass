# [undefined-local (F823)](#undefined-local-f823)

Added in [v0.0.24](https://github.com/astral-sh/ruff/releases/tag/v0.0.24) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27undefined-local%27%20OR%20F823)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fundefined_local.rs#L35)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for undefined local variables.

## [Why is this bad?](#why-is-this-bad)

Referencing a local variable before it has been assigned will raise
an `UnboundLocalError` at runtime.

## [Example](#example)

```
x = 1


def foo():
    x += 1
```

Use instead:

```
x = 1


def foo():
    global x
    x += 1
```