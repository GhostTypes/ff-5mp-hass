# [undefined-name (F821)](#undefined-name-f821)

Added in [v0.0.20](https://github.com/astral-sh/ruff/releases/tag/v0.0.20) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27undefined-name%27%20OR%20F821)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fundefined_name.rs#L29)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for uses of undefined names.

## [Why is this bad?](#why-is-this-bad)

An undefined name is likely to raise `NameError` at runtime.

## [Example](#example)

```
def double():
    return n * 2  # raises `NameError` if `n` is undefined when `double` is called
```

Use instead:

```
def double(n):
    return n * 2
```

## [Options](#options)

* [`target-version`](../../settings/#target-version): Can be used to configure which symbols Ruff will understand
  as being available in the `builtins` namespace.

## [References](#references)

* [Python documentation: Naming and binding](https://docs.python.org/3/reference/executionmodel.html#naming-and-binding)