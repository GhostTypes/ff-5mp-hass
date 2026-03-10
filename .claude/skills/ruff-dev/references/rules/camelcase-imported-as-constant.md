# [camelcase-imported-as-constant (N814)](#camelcase-imported-as-constant-n814)

Added in [v0.0.82](https://github.com/astral-sh/ruff/releases/tag/v0.0.82) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27camelcase-imported-as-constant%27%20OR%20N814)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpep8_naming%2Frules%2Fcamelcase_imported_as_constant.rs#L53)

Derived from the **[pep8-naming](../#pep8-naming-n)** linter.

## [What it does](#what-it-does)

Checks for `CamelCase` imports that are aliased to constant-style names.

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/) recommends naming conventions for classes, functions,
constants, and more. The use of inconsistent naming styles between
import and alias names may lead readers to expect an import to be of
another type (e.g., confuse a Python class with a constant).

Import aliases should thus follow the same naming style as the member
being imported.

## [Example](#example)

```
from example import MyClassName as MY_CLASS_NAME
```

Use instead:

```
from example import MyClassName
```

## [Note](#note)

Identifiers consisting of a single uppercase character are ambiguous under
the rules of [PEP 8](https://peps.python.org/pep-0008/), which specifies `CamelCase` for classes and
`ALL_CAPS_SNAKE_CASE` for constants. Without a second character, it is not
possible to reliably guess whether the identifier is intended to be part
of a `CamelCase` string for a class or an `ALL_CAPS_SNAKE_CASE` string for
a constant, since both conventions will produce the same output when given
a single input character. Therefore, this lint rule does not apply to cases
where the alias for the imported identifier consists of a single uppercase
character.

A common example of a single uppercase character being used for a class
name can be found in Django's `django.db.models.Q` class.

## [Options](#options)

* [`lint.pep8-naming.ignore-names`](../../settings/#lint_pep8-naming_ignore-names)
* [`lint.pep8-naming.extend-ignore-names`](../../settings/#lint_pep8-naming_extend-ignore-names)