# [mixed-case-variable-in-global-scope (N816)](#mixed-case-variable-in-global-scope-n816)

Added in [v0.0.89](https://github.com/astral-sh/ruff/releases/tag/v0.0.89) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27mixed-case-variable-in-global-scope%27%20OR%20N816)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpep8_naming%2Frules%2Fmixed_case_variable_in_global_scope.rs#L54)

Derived from the **[pep8-naming](../#pep8-naming-n)** linter.

## [What it does](#what-it-does)

Checks for global variable names that follow the `mixedCase` convention.

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/#global-variable-names) recommends that global variable names should be lower case and
separated by underscores (also known as `snake_case`).

> ### [Global Variable Names](#global-variable-names)
>
> (Let’s hope that these variables are meant for use inside one module
> only.) The conventions are about the same as those for functions.
>
> Modules that are designed for use via `from M import *` should use the
> `__all__` mechanism to prevent exporting globals, or use the older
> convention of prefixing such globals with an underscore (which you might
> want to do to indicate these globals are “module non-public”).
>
> ### [Function and Variable Names](#function-and-variable-names)
>
> Function names should be lowercase, with words separated by underscores
> as necessary to improve readability.
>
> Variable names follow the same convention as function names.
>
> mixedCase is allowed only in contexts where that’s already the prevailing
> style (e.g. threading.py), to retain backwards compatibility.

## [Example](#example)

```
myVariable = "hello"
another_variable = "world"
yet_anotherVariable = "foo"
```

Use instead:

```
my_variable = "hello"
another_variable = "world"
yet_another_variable = "foo"
```

## [Options](#options)

* [`lint.pep8-naming.ignore-names`](../../settings/#lint_pep8-naming_ignore-names)
* [`lint.pep8-naming.extend-ignore-names`](../../settings/#lint_pep8-naming_extend-ignore-names)