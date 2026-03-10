# [missing-newline-at-end-of-file (W292)](#missing-newline-at-end-of-file-w292)

Added in [v0.0.61](https://github.com/astral-sh/ruff/releases/tag/v0.0.61) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-newline-at-end-of-file%27%20OR%20W292)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fmissing_newline_at_end_of_file.rs#L26)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for files missing a new line at the end of the file.

## [Why is this bad?](#why-is-this-bad)

Trailing blank lines in a file are superfluous.

However, the last line of the file should end with a newline.

## [Example](#example)

```
spam(1)
```

Use instead:

```
spam(1)\n
```