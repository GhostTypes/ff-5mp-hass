# [forward-annotation-syntax-error (F722)](#forward-annotation-syntax-error-f722)

Added in [v0.0.39](https://github.com/astral-sh/ruff/releases/tag/v0.0.39) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27forward-annotation-syntax-error%27%20OR%20F722)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fforward_annotation_syntax_error.rs#L26)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for forward annotations that include invalid syntax.

## [Why is this bad?](#why-is-this-bad)

In Python, type annotations can be quoted as strings literals to enable
references to types that have not yet been defined, known as "forward
references".

However, these quoted annotations must be valid Python expressions. The use
of invalid syntax in a quoted annotation won't raise a `SyntaxError`, but
will instead raise an error when type checking is performed.

## [Example](#example)

```
def foo() -> "/": ...
```

## [References](#references)

* [PEP 563 – Postponed Evaluation of Annotations](https://peps.python.org/pep-0563/)