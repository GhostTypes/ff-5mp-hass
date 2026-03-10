# [camelcase-imported-as-lowercase (N813)](#camelcase-imported-as-lowercase-n813)

Added in [v0.0.82](https://github.com/astral-sh/ruff/releases/tag/v0.0.82) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27camelcase-imported-as-lowercase%27%20OR%20N813)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpep8_naming%2Frules%2Fcamelcase_imported_as_lowercase.rs#L38)

Derived from the **[pep8-naming](../#pep8-naming-n)** linter.

## [What it does](#what-it-does)

Checks for `CamelCase` imports that are aliased to lowercase names.

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/) recommends naming conventions for classes, functions,
constants, and more. The use of inconsistent naming styles between
import and alias names may lead readers to expect an import to be of
another type (e.g., confuse a Python class with a constant).

Import aliases should thus follow the same naming style as the member
being imported.

## [Example](#example)

```
from example import MyClassName as myclassname
```

Use instead:

```
from example import MyClassName
```

## [Options](#options)

* [`lint.pep8-naming.ignore-names`](../../settings/#lint_pep8-naming_ignore-names)
* [`lint.pep8-naming.extend-ignore-names`](../../settings/#lint_pep8-naming_extend-ignore-names)