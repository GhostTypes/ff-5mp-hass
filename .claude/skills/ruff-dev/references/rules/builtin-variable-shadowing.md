# [builtin-variable-shadowing (A001)](#builtin-variable-shadowing-a001)

Added in [v0.0.48](https://github.com/astral-sh/ruff/releases/tag/v0.0.48) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27builtin-variable-shadowing%27%20OR%20A001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_builtins%2Frules%2Fbuiltin_variable_shadowing.rs#L46)

Derived from the **[flake8-builtins](../#flake8-builtins-a)** linter.

## [What it does](#what-it-does)

Checks for variable (and function) assignments that use the same names
as builtins.

## [Why is this bad?](#why-is-this-bad)

Reusing a builtin name for the name of a variable increases the
difficulty of reading and maintaining the code, and can cause
non-obvious errors, as readers may mistake the variable for the
builtin and vice versa.

Builtins can be marked as exceptions to this rule via the
[`lint.flake8-builtins.ignorelist`](../../settings/#lint_flake8-builtins_ignorelist) configuration option.

## [Example](#example)

```
def find_max(list_of_lists):
    max = 0
    for flat_list in list_of_lists:
        for value in flat_list:
            max = max(max, value)  # TypeError: 'int' object is not callable
    return max
```

Use instead:

```
def find_max(list_of_lists):
    result = 0
    for flat_list in list_of_lists:
        for value in flat_list:
            result = max(result, value)
    return result
```

## [Options](#options)

* [`lint.flake8-builtins.ignorelist`](../../settings/#lint_flake8-builtins_ignorelist)

## [References](#references)

* [*Why is it a bad idea to name a variable `id` in Python?*](https://stackoverflow.com/questions/77552/id-is-a-bad-variable-name-in-python)