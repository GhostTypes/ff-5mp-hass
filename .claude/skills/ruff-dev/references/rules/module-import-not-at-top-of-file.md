# [module-import-not-at-top-of-file (E402)](#module-import-not-at-top-of-file-e402)

Added in [v0.0.28](https://github.com/astral-sh/ruff/releases/tag/v0.0.28) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27module-import-not-at-top-of-file%27%20OR%20E402)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fmodule_import_not_at_top_of_file.rs#L42)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

## [What it does](#what-it-does)

Checks for imports that are not at the top of the file.

## [Why is this bad?](#why-is-this-bad)

According to [PEP 8](https://peps.python.org/pep-0008/#imports), "imports are always put at the top of the file, just after any
module comments and docstrings, and before module globals and constants."

This rule makes an exception for both `sys.path` modifications (allowing for
`sys.path.insert`, `sys.path.append`, etc.) and `os.environ` modifications
between imports.

## [Example](#example)

```
"One string"
"Two string"
a = 1
import os
from sys import x
```

Use instead:

```
import os
from sys import x

"One string"
"Two string"
a = 1
```

## [Notebook behavior](#notebook-behavior)

For Jupyter notebooks, this rule checks for imports that are not at the top of a *cell*.