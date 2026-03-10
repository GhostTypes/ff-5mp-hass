# [too-many-newlines-at-end-of-file (W391)](#too-many-newlines-at-end-of-file-w391)

Preview (since [v0.3.3](https://github.com/astral-sh/ruff/releases/tag/v0.3.3)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27too-many-newlines-at-end-of-file%27%20OR%20W391)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Ftoo_many_newlines_at_end_of_file.rs#L31)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for files with multiple trailing blank lines.

In the case of notebooks, this check is applied to
each cell separately.

## [Why is this bad?](#why-is-this-bad)

Trailing blank lines in a file are superfluous.

However, the last line of the file should end with a newline.

## [Example](#example)

```
spam(1)\n\n\n
```

Use instead:

```
spam(1)\n
```