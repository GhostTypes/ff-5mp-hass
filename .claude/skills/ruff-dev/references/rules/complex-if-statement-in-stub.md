# [complex-if-statement-in-stub (PYI002)](#complex-if-statement-in-stub-pyi002)

Added in [v0.0.276](https://github.com/astral-sh/ruff/releases/tag/v0.0.276) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27complex-if-statement-in-stub%27%20OR%20PYI002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fcomplex_if_statement_in_stub.rs#L34)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for `if` statements with complex conditionals in stubs.

## [Why is this bad?](#why-is-this-bad)

Type checkers understand simple conditionals to express variations between
different Python versions and platforms. However, complex tests may not be
understood by a type checker, leading to incorrect inferences when they
analyze your code.

## [Example](#example)

```
import sys

if (3, 10) <= sys.version_info < (3, 12): ...
```

Use instead:

```
import sys

if sys.version_info >= (3, 10) and sys.version_info < (3, 12): ...
```

## [References](#references)

* [Typing documentation: Version and platform checking](https://typing.python.org/en/latest/spec/directives.html#version-and-platform-checks)