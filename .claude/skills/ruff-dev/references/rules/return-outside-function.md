# [return-outside-function (F706)](#return-outside-function-f706)

Added in [v0.0.18](https://github.com/astral-sh/ruff/releases/tag/v0.0.18) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27return-outside-function%27%20OR%20F706)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Freturn_outside_function.rs#L20)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for `return` statements outside of functions.

## [Why is this bad?](#why-is-this-bad)

The use of a `return` statement outside of a function will raise a
`SyntaxError`.

## [Example](#example)

```
class Foo:
    return 1
```

## [References](#references)

* [Python documentation: `return`](https://docs.python.org/3/reference/simple_stmts.html#the-return-statement)