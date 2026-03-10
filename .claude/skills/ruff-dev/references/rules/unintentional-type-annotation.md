# [unintentional-type-annotation (B032)](#unintentional-type-annotation-b032)

Added in [v0.0.250](https://github.com/astral-sh/ruff/releases/tag/v0.0.250) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unintentional-type-annotation%27%20OR%20B032)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Funintentional_type_annotation.rs#L25)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for the unintentional use of type annotations.

## [Why is this bad?](#why-is-this-bad)

The use of a colon (`:`) in lieu of an assignment (`=`) can be syntactically valid, but
is almost certainly a mistake when used in a subscript or attribute assignment.

## [Example](#example)

```
a["b"]: 1
```

Use instead:

```
a["b"] = 1
```