# [dunder-function-name (N807)](#dunder-function-name-n807)

Added in [v0.0.82](https://github.com/astral-sh/ruff/releases/tag/v0.0.82) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27dunder-function-name%27%20OR%20N807)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpep8_naming%2Frules%2Fdunder_function_name.rs#L40)

Derived from the **[pep8-naming](../#pep8-naming-n)** linter.

## [What it does](#what-it-does)

Checks for functions with "dunder" names (that is, names with two
leading and trailing underscores) that are not documented.

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/) recommends that only documented "dunder" methods are used:

> ..."magic" objects or attributes that live in user-controlled
> namespaces. E.g. `__init__`, `__import__` or `__file__`. Never invent
> such names; only use them as documented.

## [Example](#example)

```
def __my_function__():
    pass
```

Use instead:

```
def my_function():
    pass
```

## [Options](#options)

* [`lint.pep8-naming.ignore-names`](../../settings/#lint_pep8-naming_ignore-names)
* [`lint.pep8-naming.extend-ignore-names`](../../settings/#lint_pep8-naming_extend-ignore-names)