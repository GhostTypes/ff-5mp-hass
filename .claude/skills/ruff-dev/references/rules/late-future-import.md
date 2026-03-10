# [late-future-import (F404)](#late-future-import-f404)

Added in [v0.0.34](https://github.com/astral-sh/ruff/releases/tag/v0.0.34) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27late-future-import%27%20OR%20F404)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fimports.rs#L159)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for `__future__` imports that are not located at the beginning of a
file.

## [Why is this bad?](#why-is-this-bad)

Imports from `__future__` must be placed the beginning of the file, before any
other statements (apart from docstrings). The use of `__future__` imports
elsewhere is invalid and will result in a `SyntaxError`.

## [Example](#example)

```
from pathlib import Path

from __future__ import annotations
```

Use instead:

```
from __future__ import annotations

from pathlib import Path
```

## [References](#references)

* [Python documentation: Future statements](https://docs.python.org/3/reference/simple_stmts.html#future)