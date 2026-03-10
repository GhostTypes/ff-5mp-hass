# [invalid-argument-name (N803)](#invalid-argument-name-n803)

Added in [v0.0.77](https://github.com/astral-sh/ruff/releases/tag/v0.0.77) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-argument-name%27%20OR%20N803)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpep8_naming%2Frules%2Finvalid_argument_name.rs#L48)

Derived from the **[pep8-naming](../#pep8-naming-n)** linter.

## [What it does](#what-it-does)

Checks for argument names that do not follow the `snake_case` convention.

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/#function-and-method-arguments) recommends that function names should be lower case and separated
by underscores (also known as `snake_case`).

> Function names should be lowercase, with words separated by underscores
> as necessary to improve readability.
>
> Variable names follow the same convention as function names.
>
> mixedCase is allowed only in contexts where that’s already the
> prevailing style (e.g. threading.py), to retain backwards compatibility.

Methods decorated with [`@typing.override`](https://docs.python.org/3/library/typing.html#typing.override) are ignored.

## [Example](#example)

```
def my_function(A, myArg):
    pass
```

Use instead:

```
def my_function(a, my_arg):
    pass
```

## [Options](#options)

* [`lint.pep8-naming.ignore-names`](../../settings/#lint_pep8-naming_ignore-names)
* [`lint.pep8-naming.extend-ignore-names`](../../settings/#lint_pep8-naming_extend-ignore-names)