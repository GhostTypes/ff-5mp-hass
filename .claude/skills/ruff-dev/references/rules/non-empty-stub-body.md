# [non-empty-stub-body (PYI010)](#non-empty-stub-body-pyi010)

Added in [v0.0.253](https://github.com/astral-sh/ruff/releases/tag/v0.0.253) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27non-empty-stub-body%27%20OR%20PYI010)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fnon_empty_stub_body.rs#L30)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for non-empty function stub bodies.

## [Why is this bad?](#why-is-this-bad)

Stub files are never executed at runtime; they should be thought of as
"data files" for type checkers or IDEs. Function bodies are redundant
for this purpose.

## [Example](#example)

```
def double(x: int) -> int:
    return x * 2
```

Use instead:

```
def double(x: int) -> int: ...
```

## [References](#references)

* [Typing documentation - Writing and Maintaining Stub Files](https://typing.python.org/en/latest/guides/writing_stubs.html)