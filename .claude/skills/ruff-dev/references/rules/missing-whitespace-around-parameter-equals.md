# [missing-whitespace-around-parameter-equals (E252)](#missing-whitespace-around-parameter-equals-e252)

Preview (since [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-whitespace-around-parameter-equals%27%20OR%20E252)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Flogical_lines%2Fwhitespace_around_named_parameter_equals.rs#L74)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for missing whitespace around the equals sign in an annotated
function keyword parameter.

## [Why is this bad?](#why-is-this-bad)

According to [PEP 8](https://peps.python.org/pep-0008/#whitespace-in-expressions-and-statements), the spaces around the equals sign in a keyword
parameter should only be omitted when the parameter is unannotated:

> Don’t use spaces around the = sign when used to indicate a keyword
> argument, or when used to indicate a default value for an unannotated
> function parameter.

## [Example](#example)

```
def add(a: int=0) -> int:
    return a + 1
```

Use instead:

```
def add(a: int = 0) -> int:
    return a + 1
```