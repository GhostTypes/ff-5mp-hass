# [manual-from-import (PLR0402)](#manual-from-import-plr0402)

Added in [v0.0.155](https://github.com/astral-sh/ruff/releases/tag/v0.0.155) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27manual-from-import%27%20OR%20PLR0402)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fmanual_import_from.rs#L29)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for submodule imports that are aliased to the submodule name.

## [Why is this bad?](#why-is-this-bad)

Using the `from` keyword to import the submodule is more concise and
readable.

## [Example](#example)

```
import concurrent.futures as futures
```

Use instead:

```
from concurrent import futures
```

## [References](#references)

* [Python documentation: Submodules](https://docs.python.org/3/reference/import.html#submodules)