# [pass-statement-stub-body (PYI009)](#pass-statement-stub-body-pyi009)

Added in [v0.0.253](https://github.com/astral-sh/ruff/releases/tag/v0.0.253) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pass-statement-stub-body%27%20OR%20PYI009)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fpass_statement_stub_body.rs#L27)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `pass` statements in empty stub bodies.

## [Why is this bad?](#why-is-this-bad)

For stylistic consistency, `...` should always be used rather than `pass`
in stub files.

## [Example](#example)

```
def foo(bar: int) -> list[int]: pass
```

Use instead:

```
def foo(bar: int) -> list[int]: ...
```

## [References](#references)

* [Typing documentation - Writing and Maintaining Stub Files](https://typing.python.org/en/latest/guides/writing_stubs.html)