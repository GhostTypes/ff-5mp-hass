# [non-lowercase-variable-in-function (N806)](#non-lowercase-variable-in-function-n806)

Added in [v0.0.89](https://github.com/astral-sh/ruff/releases/tag/v0.0.89) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27non-lowercase-variable-in-function%27%20OR%20N806)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpep8_naming%2Frules%2Fnon_lowercase_variable_in_function.rs#L41)

Derived from the **[pep8-naming](../#pep8-naming-n)** linter.

## [What it does](#what-it-does)

Checks for the use of non-lowercase variable names in functions.

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/#function-and-variable-names) recommends that all function variables use lowercase names:

> Function names should be lowercase, with words separated by underscores as necessary to
> improve readability. Variable names follow the same convention as function names. mixedCase
> is allowed only in contexts where that's already the prevailing style (e.g. threading.py),
> to retain backwards compatibility.

## [Example](#example)

```
def my_function(a):
    B = a + 3
    return B
```

Use instead:

```
def my_function(a):
    b = a + 3
    return b
```

## [Options](#options)

* [`lint.pep8-naming.ignore-names`](../../settings/#lint_pep8-naming_ignore-names)
* [`lint.pep8-naming.extend-ignore-names`](../../settings/#lint_pep8-naming_extend-ignore-names)