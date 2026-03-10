# [unexpected-indentation-comment (E116)](#unexpected-indentation-comment-e116)

Preview (since [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unexpected-indentation-comment%27%20OR%20E116)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Flogical_lines%2Findentation.rs#L213)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for unexpected indentation of comment.

## [Why is this bad?](#why-is-this-bad)

Comments should match the indentation of the containing code block.

## [Example](#example)

```
a = 1
    # b = 2
```

Use instead:

```
a = 1
# b = 2
```