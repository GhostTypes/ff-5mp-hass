# [future-annotations-in-stub (PYI044)](#future-annotations-in-stub-pyi044)

Added in [v0.0.273](https://github.com/astral-sh/ruff/releases/tag/v0.0.273) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27future-annotations-in-stub%27%20OR%20PYI044)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Ffuture_annotations_in_stub.rs#L20)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for the presence of the `from __future__ import annotations` import
statement in stub files.

## [Why is this bad?](#why-is-this-bad)

Stub files natively support forward references in all contexts, as stubs are
never executed at runtime. (They should be thought of as "data files" for
type checkers.) As such, the `from __future__ import annotations` import
statement has no effect and should be omitted.

## [References](#references)

* [Typing Style Guide](https://typing.python.org/en/latest/guides/writing_stubs.html#language-features)