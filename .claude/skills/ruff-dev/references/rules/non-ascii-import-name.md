# [non-ascii-import-name (PLC2403)](#non-ascii-import-name-plc2403)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27non-ascii-import-name%27%20OR%20PLC2403)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fnon_ascii_module_import.rs#L32)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for the use of non-ASCII characters in import statements.

## [Why is this bad?](#why-is-this-bad)

The use of non-ASCII characters in import statements can cause confusion
and compatibility issues (see: [PEP 672](https://peps.python.org/pep-0672/)).

## [Example](#example)

```
import bár
```

Use instead:

```
import bar
```

If the module is third-party, use an ASCII-only alias:

```
import bár as bar
```