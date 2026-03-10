# [continue-outside-loop (F702)](#continue-outside-loop-f702)

Added in [v0.0.36](https://github.com/astral-sh/ruff/releases/tag/v0.0.36) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27continue-outside-loop%27%20OR%20F702)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fcontinue_outside_loop.rs#L20)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for `continue` statements outside of loops.

## [Why is this bad?](#why-is-this-bad)

The use of a `continue` statement outside of a `for` or `while` loop will
raise a `SyntaxError`.

## [Example](#example)

```
def foo():
    continue  # SyntaxError
```

## [References](#references)

* [Python documentation: `continue`](https://docs.python.org/3/reference/simple_stmts.html#the-continue-statement)