# [quoted-annotation-in-stub (PYI020)](#quoted-annotation-in-stub-pyi020)

Added in [v0.0.265](https://github.com/astral-sh/ruff/releases/tag/v0.0.265) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27quoted-annotation-in-stub%27%20OR%20PYI020)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fquoted_annotation_in_stub.rs#L31)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for quoted type annotations in stub (`.pyi`) files, which should be avoided.

## [Why is this bad?](#why-is-this-bad)

Stub files natively support forward references in all contexts, as stubs
are never executed at runtime. (They should be thought of as "data files"
for type checkers and IDEs.) As such, quotes are never required for type
annotations in stub files, and should be omitted.

## [Example](#example)

```
def function() -> "int": ...
```

Use instead:

```
def function() -> int: ...
```

## [References](#references)

* [Typing documentation - Writing and Maintaining Stub Files](https://typing.python.org/en/latest/guides/writing_stubs.html)