# [whitespace-before-parameters (E211)](#whitespace-before-parameters-e211)

Preview (since [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27whitespace-before-parameters%27%20OR%20E211)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Flogical_lines%2Fwhitespace_before_parameters.rs#L28)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for extraneous whitespace immediately preceding an open parenthesis
or bracket.

## [Why is this bad?](#why-is-this-bad)

According to [PEP 8](https://peps.python.org/pep-0008/#pet-peeves), open parentheses and brackets should not be preceded
by any trailing whitespace.

## [Example](#example)

```
spam (1)
```

Use instead:

```
spam(1)
```