# [utf8-encoding-declaration (UP009)](#utf8-encoding-declaration-up009)

Added in [v0.0.155](https://github.com/astral-sh/ruff/releases/tag/v0.0.155) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27utf8-encoding-declaration%27%20OR%20UP009)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Funnecessary_coding_comment.rs#L34)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary UTF-8 encoding declarations.

## [Why is this bad?](#why-is-this-bad)

[PEP 3120](https://peps.python.org/pep-3120/) makes UTF-8 the default encoding, so a UTF-8 encoding
declaration is unnecessary.

## [Example](#example)

```
# -*- coding: utf-8 -*-
print("Hello, world!")
```

Use instead:

```
print("Hello, world!")
```