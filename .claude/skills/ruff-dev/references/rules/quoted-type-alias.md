# [quoted-type-alias (TC008)](#quoted-type-alias-tc008)

Preview (since [0.8.1](https://github.com/astral-sh/ruff/releases/tag/0.8.1)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27quoted-type-alias%27%20OR%20TC008)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_type_checking%2Frules%2Ftype_alias_quotes.rs#L136)

Derived from the **[flake8-type-checking](../#flake8-type-checking-tc)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for unnecessary quotes in [PEP 613](https://peps.python.org/pep-0613/) explicit type aliases
and [PEP 695](https://peps.python.org/pep-0695/#generic-type-alias) type statements.

## [Why is this bad?](#why-is-this-bad)

Unnecessary string forward references can lead to additional overhead
in runtime libraries making use of type hints. They can also have bad
interactions with other runtime uses like [PEP 604](https://peps.python.org/pep-0604/) type unions.

PEP-613 type aliases are only flagged by the rule if Ruff can have high
confidence that the quotes are unnecessary. Specifically, any PEP-613
type alias where the type expression on the right-hand side contains
subscripts or attribute accesses will not be flagged. This is because
type aliases can reference types that are, for example, generic in stub
files but not at runtime. That can mean that a type checker expects the
referenced type to be subscripted with type arguments despite the fact
that doing so would fail at runtime if the type alias value was not
quoted. Similarly, a type alias might need to reference a module-level
attribute that exists in a stub file but not at runtime, meaning that
the type alias value would need to be quoted to avoid a runtime error.

## [Example](#example)

Given:

```
from typing import TypeAlias

OptInt: TypeAlias = "int | None"
```

Use instead:

```
from typing import TypeAlias

OptInt: TypeAlias = int | None
```

Given:

```
type OptInt = "int | None"
```

Use instead:

```
type OptInt = int | None
```

## [Fix safety](#fix-safety)

This rule's fix is marked as safe, unless the type annotation contains comments.

## [See also](#see-also)

This rule only applies to type aliases in non-stub files. For removing quotes in other
contexts or in stub files, see:

* [`quoted-annotation-in-stub`](https://docs.astral.sh/ruff/rules/quoted-annotation-in-stub/): A rule that
  removes all quoted annotations from stub files
* [`quoted-annotation`](https://docs.astral.sh/ruff/rules/quoted-annotation/): A rule that removes unnecessary quotes
  from *annotations* in runtime files.

## [References](#references)

* [PEP 613 – Explicit Type Aliases](https://peps.python.org/pep-0613/)
* [PEP 695: Generic Type Alias](https://peps.python.org/pep-0695/#generic-type-alias)
* [PEP 604 – Allow writing union types as `X | Y`](https://peps.python.org/pep-0604/)