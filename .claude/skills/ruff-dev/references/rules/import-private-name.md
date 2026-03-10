# [import-private-name (PLC2701)](#import-private-name-plc2701)

Preview (since [v0.1.14](https://github.com/astral-sh/ruff/releases/tag/v0.1.14)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27import-private-name%27%20OR%20PLC2701)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fimport_private_name.rs#L52)

Derived from the **[Pylint](../#pylint-pl)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for import statements that import a private name (a name starting
with an underscore `_`) from another module.

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/) states that names starting with an underscore are private. Thus,
they are not intended to be used outside of the module in which they are
defined.

Further, as private imports are not considered part of the public API, they
are prone to unexpected changes, especially outside of semantic versioning.

Instead, consider using the public API of the module.

This rule ignores private name imports that are exclusively used in type
annotations. Ideally, types would be public; however, this is not always
possible when using third-party libraries.

## [Known problems](#known-problems)

Does not ignore private name imports from within the module that defines
the private name if the module is defined with [PEP 420](https://peps.python.org/pep-0420/) namespace packages
(i.e., directories that omit the `__init__.py` file). Namespace packages
must be configured via the [`namespace-packages`](../../settings/#namespace-packages) setting.

## [Example](#example)

```
from foo import _bar
```

## [Options](#options)

* [`namespace-packages`](../../settings/#namespace-packages)

## [References](#references)

* [PEP 8: Naming Conventions](https://peps.python.org/pep-0008/#naming-conventions)
* [Semantic Versioning](https://semver.org/)