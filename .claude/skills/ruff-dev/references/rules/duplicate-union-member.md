# [duplicate-union-member (PYI016)](#duplicate-union-member-pyi016)

Added in [v0.0.262](https://github.com/astral-sh/ruff/releases/tag/v0.0.262) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27duplicate-union-member%27%20OR%20PYI016)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fduplicate_union_member.rs#L39)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for duplicate union members.

## [Why is this bad?](#why-is-this-bad)

Duplicate union members are redundant and should be removed.

## [Example](#example)

```
foo: str | str
```

Use instead:

```
foo: str
```

## [Fix safety](#fix-safety)

This rule's fix is marked as safe unless the union contains comments.

For nested union, the fix will flatten type expressions into a single
top-level union.

## [References](#references)

* [Python documentation: `typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union)