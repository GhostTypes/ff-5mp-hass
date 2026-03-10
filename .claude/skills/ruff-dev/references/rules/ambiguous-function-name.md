# [ambiguous-function-name (E743)](#ambiguous-function-name-e743)

Added in [v0.0.35](https://github.com/astral-sh/ruff/releases/tag/v0.0.35) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27ambiguous-function-name%27%20OR%20E743)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fambiguous_function_name.rs#L28)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

## [What it does](#what-it-does)

Checks for the use of the characters 'l', 'O', or 'I' as function names.

## [Why is this bad?](#why-is-this-bad)

In some fonts, these characters are indistinguishable from the
numerals one and zero. When tempted to use 'l', use 'L' instead.

## [Example](#example)

```
def l(x): ...
```

Use instead:

```
def long_name(x): ...
```