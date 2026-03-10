# [t-suffixed-type-alias (PYI043)](#t-suffixed-type-alias-pyi043)

Added in [v0.0.265](https://github.com/astral-sh/ruff/releases/tag/v0.0.265) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27t-suffixed-type-alias%27%20OR%20PYI043)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Ftype_alias_naming.rs#L68)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for private type alias definitions suffixed with 'T'.

## [Why is this bad?](#why-is-this-bad)

It's conventional to use the 'T' suffix for type variables; the use of
such a suffix implies that the object is a `TypeVar`.

Adding the 'T' suffix to a non-`TypeVar`, it can be misleading and should
be avoided.

## [Example](#example)

```
from typing import TypeAlias

_MyTypeT: TypeAlias = int
```

Use instead:

```
from typing import TypeAlias

_MyType: TypeAlias = int
```

## [References](#references)

* [PEP 484: Type Aliases](https://peps.python.org/pep-0484/#type-aliases)