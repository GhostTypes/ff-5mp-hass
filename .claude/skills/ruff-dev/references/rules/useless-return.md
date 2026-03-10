# [useless-return (PLR1711)](#useless-return-plr1711)

Added in [v0.0.257](https://github.com/astral-sh/ruff/releases/tag/v0.0.257) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27useless-return%27%20OR%20PLR1711)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fuseless_return.rs#L31)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for functions that end with an unnecessary `return` or
`return None`, and contain no other `return` statements.

## [Why is this bad?](#why-is-this-bad)

Python implicitly assumes a `None` return at the end of a function, making
it unnecessary to explicitly write `return None`.

## [Example](#example)

```
def f():
    print(5)
    return None
```

Use instead:

```
def f():
    print(5)
```