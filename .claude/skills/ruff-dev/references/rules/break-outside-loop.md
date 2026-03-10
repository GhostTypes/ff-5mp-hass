# [break-outside-loop (F701)](#break-outside-loop-f701)

Added in [v0.0.36](https://github.com/astral-sh/ruff/releases/tag/v0.0.36) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27break-outside-loop%27%20OR%20F701)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fbreak_outside_loop.rs#L20)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for `break` statements outside of loops.

## [Why is this bad?](#why-is-this-bad)

The use of a `break` statement outside of a `for` or `while` loop will
raise a `SyntaxError`.

## [Example](#example)

```
def foo():
    break
```

## [References](#references)

* [Python documentation: `break`](https://docs.python.org/3/reference/simple_stmts.html#the-break-statement)