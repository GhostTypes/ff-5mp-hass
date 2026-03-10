# [unnecessary-round (RUF057)](#unnecessary-round-ruf057)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-round%27%20OR%20RUF057)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Funnecessary_round.rs#L36)

Fix is always available.

## [What it does](#what-it-does)

Checks for `round()` calls that have no effect on the input.

## [Why is this bad?](#why-is-this-bad)

Rounding a value that's already an integer is unnecessary.
It's clearer to use the value directly.

## [Example](#example)

```
a = round(1, 0)
```

Use instead:

```
a = 1
```

## [Fix safety](#fix-safety)

The fix is marked unsafe if it is not possible to guarantee that the first argument of
`round()` is of type `int`, or if the fix deletes comments.