# [pep484-style-positional-only-parameter (PYI063)](#pep484-style-positional-only-parameter-pyi063)

Added in [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pep484-style-positional-only-parameter%27%20OR%20PYI063)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fpre_pep570_positional_argument.rs#L42)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for the presence of [PEP 484](https://peps.python.org/pep-0484/#positional-only-arguments)-style positional-only parameters.

## [Why is this bad?](#why-is-this-bad)

Historically, [PEP 484](https://peps.python.org/pep-0484/#positional-only-arguments) recommended prefixing parameter names with double
underscores (`__`) to indicate to a type checker that they were
positional-only. However, [PEP 570](https://peps.python.org/pep-0570) (introduced in Python 3.8) introduced
dedicated syntax for positional-only arguments. If a forward slash (`/`) is
present in a function signature on Python 3.8+, all parameters prior to the
slash are interpreted as positional-only.

The new syntax should be preferred as it is more widely used, more concise
and more readable. It is also respected by Python at runtime, whereas the
old-style syntax was only understood by type checkers.

## [Example](#example)

```
def foo(__x: int) -> None: ...
```

Use instead:

```
def foo(x: int, /) -> None: ...
```

## [Options](#options)

* [`target-version`](../../settings/#target-version)