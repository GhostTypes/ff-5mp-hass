# [snake-case-type-alias (PYI042)](#snake-case-type-alias-pyi042)

Added in [v0.0.265](https://github.com/astral-sh/ruff/releases/tag/v0.0.265) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27snake-case-type-alias%27%20OR%20PYI042)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Ftype_alias_naming.rs#L28)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for type aliases that do not use the CamelCase naming convention.

## [Why is this bad?](#why-is-this-bad)

It's conventional to use the CamelCase naming convention for type aliases,
to distinguish them from other variables.

## [Example](#example)

```
from typing import TypeAlias

type_alias_name: TypeAlias = int
```

Use instead:

```
from typing import TypeAlias

TypeAliasName: TypeAlias = int
```