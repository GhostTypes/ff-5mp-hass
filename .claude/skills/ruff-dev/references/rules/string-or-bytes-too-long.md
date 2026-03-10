# [string-or-bytes-too-long (PYI053)](#string-or-bytes-too-long-pyi053)

Added in [v0.0.271](https://github.com/astral-sh/ruff/releases/tag/v0.0.271) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27string-or-bytes-too-long%27%20OR%20PYI053)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fstring_or_bytes_too_long.rs#L35)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for the use of string and bytes literals longer than 50 characters
in stub (`.pyi`) files.

## [Why is this bad?](#why-is-this-bad)

If a function or variable has a default value where the string or bytes
representation is greater than 50 characters long, it is likely to be an
implementation detail or a constant that varies depending on the system
you're running on.

Although IDEs may find them useful, default values are ignored by type
checkers, the primary consumers of stub files. Replace very long constants
with ellipses (`...`) to simplify the stub.

## [Example](#example)

```
def foo(arg: str = "51 character stringgggggggggggggggggggggggggggggggg") -> None: ...
```

Use instead:

```
def foo(arg: str = ...) -> None: ...
```