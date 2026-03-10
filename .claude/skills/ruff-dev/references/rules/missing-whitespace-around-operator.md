# [missing-whitespace-around-operator (E225)](#missing-whitespace-around-operator-e225)

Preview (since [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-whitespace-around-operator%27%20OR%20E225)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Flogical_lines%2Fmissing_whitespace_around_operator.rs#L32)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for missing whitespace around all operators.

## [Why is this bad?](#why-is-this-bad)

According to [PEP 8](https://peps.python.org/pep-0008/#pet-peeves), there should be one space before and after all
assignment (`=`), augmented assignment (`+=`, `-=`, etc.), comparison,
and Booleans operators.

## [Example](#example)

```
if number==42:
    print('you have found the meaning of life')
```

Use instead:

```
if number == 42:
    print('you have found the meaning of life')
```