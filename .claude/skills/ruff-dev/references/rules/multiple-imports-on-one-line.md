# [multiple-imports-on-one-line (E401)](#multiple-imports-on-one-line-e401)

Added in [v0.0.191](https://github.com/astral-sh/ruff/releases/tag/v0.0.191) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27multiple-imports-on-one-line%27%20OR%20E401)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fmultiple_imports_on_one_line.rs#L33)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Check for multiple imports on one line.

## [Why is this bad?](#why-is-this-bad)

According to [PEP 8](https://peps.python.org/pep-0008/#imports), "imports should usually be on separate lines."

## [Example](#example)

```
import sys, os
```

Use instead:

```
import os
import sys
```