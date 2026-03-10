# [parenthesize-chained-operators (RUF021)](#parenthesize-chained-operators-ruf021)

Added in [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27parenthesize-chained-operators%27%20OR%20RUF021)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fparenthesize_chained_operators.rs#L36)

Fix is always available.

## [What it does](#what-it-does)

Checks for chained operators where adding parentheses could improve the
clarity of the code.

## [Why is this bad?](#why-is-this-bad)

`and` always binds more tightly than `or` when chaining the two together,
but this can be hard to remember (and sometimes surprising).
Adding parentheses in these situations can greatly improve code readability,
with no change to semantics or performance.

For example:

```
a, b, c = 1, 0, 2
x = a or b and c

d, e, f = 0, 1, 2
y = d and e or f
```

Use instead:

```
a, b, c = 1, 0, 2
x = a or (b and c)

d, e, f = 0, 1, 2
y = (d and e) or f
```