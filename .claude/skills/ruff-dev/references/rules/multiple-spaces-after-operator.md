# [multiple-spaces-after-operator (E222)](#multiple-spaces-after-operator-e222)

Preview (since [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27multiple-spaces-after-operator%27%20OR%20E222)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Flogical_lines%2Fspace_around_operator.rs#L127)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for extraneous whitespace after an operator.

## [Why is this bad?](#why-is-this-bad)

According to [PEP 8](https://peps.python.org/pep-0008/#whitespace-in-expressions-and-statements), operators should be surrounded by at most a single space on either
side.

## [Example](#example)

```
a = 4 +  5
```

Use instead:

```
a = 4 + 5
```