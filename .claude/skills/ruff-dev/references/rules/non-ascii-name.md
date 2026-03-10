# [non-ascii-name (PLC2401)](#non-ascii-name-plc2401)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27non-ascii-name%27%20OR%20PLC2401)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fnon_ascii_name.rs#L28)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for the use of non-ASCII characters in variable names.

## [Why is this bad?](#why-is-this-bad)

The use of non-ASCII characters in variable names can cause confusion
and compatibility issues (see: [PEP 672](https://peps.python.org/pep-0672/)).

## [Example](#example)

```
ápple_count: int
```

Use instead:

```
apple_count: int
```