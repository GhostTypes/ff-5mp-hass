# [implicit-namespace-package (INP001)](#implicit-namespace-package-inp001)

Added in [v0.0.225](https://github.com/astral-sh/ruff/releases/tag/v0.0.225) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27implicit-namespace-package%27%20OR%20INP001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_no_pep420%2Frules%2Fimplicit_namespace_package.rs#L34)

Derived from the **[flake8-no-pep420](../#flake8-no-pep420-inp)** linter.

## [What it does](#what-it-does)

Checks for packages that are missing an `__init__.py` file.

## [Why is this bad?](#why-is-this-bad)

Python packages are directories that contain a file named `__init__.py`.
The existence of this file indicates that the directory is a Python
package, and so it can be imported the same way a module can be
imported.

Directories that lack an `__init__.py` file can still be imported, but
they're indicative of a special kind of package, known as a "namespace
package" (see: [PEP 420](https://peps.python.org/pep-0420/)).
Namespace packages are less widely used, so a package that lacks an
`__init__.py` file is typically meant to be a regular package, and
the absence of the `__init__.py` file is probably an oversight.

## [Options](#options)

* [`namespace-packages`](../../settings/#namespace-packages)