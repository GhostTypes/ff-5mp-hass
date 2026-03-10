# [unquoted-type-alias (TC007)](#unquoted-type-alias-tc007)

Added in [0.10.0](https://github.com/astral-sh/ruff/releases/tag/0.10.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unquoted-type-alias%27%20OR%20TC007)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_type_checking%2Frules%2Ftype_alias_quotes.rs#L51)

Derived from the **[flake8-type-checking](../#flake8-type-checking-tc)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks if [PEP 613](https://peps.python.org/pep-0613/) explicit type aliases contain references to
symbols that are not available at runtime.

## [Why is this bad?](#why-is-this-bad)

Referencing type-checking only symbols results in a `NameError` at runtime.

## [Example](#example)

```
from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    from foo import Foo
OptFoo: TypeAlias = Foo | None
```

Use instead:

```
from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    from foo import Foo
OptFoo: TypeAlias = "Foo | None"
```

## [Fix safety](#fix-safety)

This rule's fix is currently always marked as unsafe, since runtime
typing libraries may try to access/resolve the type alias in a way
that we can't statically determine during analysis and relies on the
type alias not containing any forward references.

## [References](#references)

* [PEP 613 – Explicit Type Aliases](https://peps.python.org/pep-0613/)