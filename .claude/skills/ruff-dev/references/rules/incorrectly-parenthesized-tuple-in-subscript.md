# [incorrectly-parenthesized-tuple-in-subscript (RUF031)](#incorrectly-parenthesized-tuple-in-subscript-ruf031)

Preview (since [0.5.7](https://github.com/astral-sh/ruff/releases/tag/0.5.7)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27incorrectly-parenthesized-tuple-in-subscript%27%20OR%20RUF031)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fincorrectly_parenthesized_tuple_in_subscript.rs#L40)

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for consistent style regarding whether nonempty tuples in subscripts
are parenthesized.

The exact nature of this violation depends on the setting
[`lint.ruff.parenthesize-tuple-in-subscript`](../../settings/#lint_ruff_parenthesize-tuple-in-subscript). By default, the use of
parentheses is considered a violation.

This rule is not applied inside "typing contexts" (type annotations,
type aliases and subscripted class bases), as these have their own specific
conventions around them.

## [Why is this bad?](#why-is-this-bad)

It is good to be consistent and, depending on the codebase, one or the other
convention may be preferred.

## [Example](#example)

```
directions = {(0, 1): "North", (1, 0): "East", (0, -1): "South", (-1, 0): "West"}
directions[(0, 1)]
```

Use instead (with default setting):

```
directions = {(0, 1): "North", (1, 0): "East", (0, -1): "South", (-1, 0): "West"}
directions[0, 1]
```

## [Options](#options)

* [`lint.ruff.parenthesize-tuple-in-subscript`](../../settings/#lint_ruff_parenthesize-tuple-in-subscript)