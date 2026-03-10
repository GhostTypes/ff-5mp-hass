# [no-space-after-inline-comment (E262)](#no-space-after-inline-comment-e262)

Preview (since [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27no-space-after-inline-comment%27%20OR%20E262)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Flogical_lines%2Fwhitespace_before_comment.rs#L70)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks if one space is used after inline comments.

## [Why is this bad?](#why-is-this-bad)

An inline comment is a comment on the same line as a statement.

Per [PEP 8](https://peps.python.org/pep-0008/#comments), inline comments should start with a # and a single space.

## [Example](#example)

```
x = x + 1  #Increment x
x = x + 1  #  Increment x
x = x + 1  # \xa0Increment x
```

Use instead:

```
x = x + 1  # Increment x
x = x + 1    # Increment x
```