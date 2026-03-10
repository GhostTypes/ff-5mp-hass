# [unaliased-collections-abc-set-import (PYI025)](#unaliased-collections-abc-set-import-pyi025)

Added in [v0.0.271](https://github.com/astral-sh/ruff/releases/tag/v0.0.271) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unaliased-collections-abc-set-import%27%20OR%20PYI025)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Funaliased_collections_abc_set_import.rs#L42)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `from collections.abc import Set` imports that do not alias
`Set` to `AbstractSet`.

## [Why is this bad?](#why-is-this-bad)

The `Set` type in `collections.abc` is an abstract base class for set-like types.
It is easily confused with, and not equivalent to, the `set` builtin.

To avoid confusion, `Set` should be aliased to `AbstractSet` when imported. This
makes it clear that the imported type is an abstract base class, and not the
`set` builtin.

## [Example](#example)

```
from collections.abc import Set
```

Use instead:

```
from collections.abc import Set as AbstractSet
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe for `Set` imports defined at the
top-level of a `.py` module. Top-level symbols are implicitly exported by the
module, and so renaming a top-level symbol may break downstream modules
that import it.

The same is not true for `.pyi` files, where imported symbols are only
re-exported if they are included in `__all__`, use a "redundant"
`import foo as foo` alias, or are imported via a `*` import. As such, the
fix is marked as safe in more cases for `.pyi` files.