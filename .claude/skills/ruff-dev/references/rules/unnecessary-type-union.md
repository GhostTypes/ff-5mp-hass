# [unnecessary-type-union (PYI055)](#unnecessary-type-union-pyi055)

Added in [v0.0.283](https://github.com/astral-sh/ruff/releases/tag/v0.0.283) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-type-union%27%20OR%20PYI055)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Funnecessary_type_union.rs#L34)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for the presence of multiple `type`s in a union.

## [Why is this bad?](#why-is-this-bad)

`type[T | S]` has identical semantics to `type[T] | type[S]` in a type
annotation, but is cleaner and more concise.

## [Example](#example)

```
field: type[int] | type[float] | str
```

Use instead:

```
field: type[int | float] | str
```

## [Fix safety](#fix-safety)

This rule's fix is marked as safe, unless the type annotation contains comments.

Note that while the fix may flatten nested unions into a single top-level union,
the semantics of the annotation will remain unchanged.