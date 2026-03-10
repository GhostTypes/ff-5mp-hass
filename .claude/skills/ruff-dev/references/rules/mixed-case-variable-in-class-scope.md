# [mixed-case-variable-in-class-scope (N815)](#mixed-case-variable-in-class-scope-n815)

Added in [v0.0.89](https://github.com/astral-sh/ruff/releases/tag/v0.0.89) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27mixed-case-variable-in-class-scope%27%20OR%20N815)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpep8_naming%2Frules%2Fmixed_case_variable_in_class_scope.rs#L43)

Derived from the **[pep8-naming](../#pep8-naming-n)** linter.

## [What it does](#what-it-does)

Checks for class variable names that follow the `mixedCase` convention.

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/#function-and-method-arguments) recommends that variable names should be lower case and separated
by underscores (also known as `snake_case`).

> Function names should be lowercase, with words separated by underscores
> as necessary to improve readability.
>
> Variable names follow the same convention as function names.
>
> mixedCase is allowed only in contexts where that’s already the
> prevailing style (e.g. threading.py), to retain backwards compatibility.

## [Example](#example)

```
class MyClass:
    myVariable = "hello"
    another_variable = "world"
```

Use instead:

```
class MyClass:
    my_variable = "hello"
    another_variable = "world"
```

## [Options](#options)

* [`lint.pep8-naming.ignore-names`](../../settings/#lint_pep8-naming_ignore-names)
* [`lint.pep8-naming.extend-ignore-names`](../../settings/#lint_pep8-naming_extend-ignore-names)