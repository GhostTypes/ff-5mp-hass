# [missing-whitespace-around-bitwise-or-shift-operator (E227)](#missing-whitespace-around-bitwise-or-shift-operator-e227)

Preview (since [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-whitespace-around-bitwise-or-shift-operator%27%20OR%20E227)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Flogical_lines%2Fmissing_whitespace_around_operator.rs#L112)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for missing whitespace around bitwise and shift operators.

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/#other-recommendations) recommends never using more than one space, and always having the
same amount of whitespace on both sides of a binary operator.

For consistency, this rule enforces one space before and after bitwise and
shift operators (`<<`, `>>`, `&`, `|`, `^`).

(Note that [PEP 8](https://peps.python.org/pep-0008/#other-recommendations) suggests only adding whitespace around the operator with
the lowest precedence, but that authors should "use [their] own judgment".)

## [Example](#example)

```
x = 128<<1
```

Use instead:

```
x = 128 << 1
```