# [redundant-final-literal (PYI064)](#redundant-final-literal-pyi064)

Added in [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27redundant-final-literal%27%20OR%20PYI064)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fredundant_final_literal.rs#L36)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for redundant `Final[Literal[...]]` annotations.

## [Why is this bad?](#why-is-this-bad)

All constant variables annotated as `Final` are understood as implicitly
having `Literal` types by a type checker. As such, a `Final[Literal[...]]`
annotation can often be replaced with a bare `Final`, annotation, which
will have the same meaning to the type checker while being more concise and
more readable.

## [Example](#example)

```
from typing import Final, Literal

x: Final[Literal[42]]
y: Final[Literal[42]] = 42
```

Use instead:

```
from typing import Final, Literal

x: Final = 42
y: Final = 42
```