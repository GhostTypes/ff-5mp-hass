# [numeric-literal-too-long (PYI054)](#numeric-literal-too-long-pyi054)

Added in [v0.0.271](https://github.com/astral-sh/ruff/releases/tag/v0.0.271) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27numeric-literal-too-long%27%20OR%20PYI054)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fnumeric_literal_too_long.rs#L32)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for numeric literals with a string representation longer than ten
characters.

## [Why is this bad?](#why-is-this-bad)

If a function has a default value where the literal representation is
greater than 10 characters, the value is likely to be an implementation
detail or a constant that varies depending on the system you're running on.

Default values like these should generally be omitted from stubs. Use
ellipses (`...`) instead.

## [Example](#example)

```
def foo(arg: int = 693568516352839939918568862861217771399698285293568) -> None: ...
```

Use instead:

```
def foo(arg: int = ...) -> None: ...
```