# [line-too-long (E501)](#line-too-long-e501)

Added in [v0.0.18](https://github.com/astral-sh/ruff/releases/tag/v0.0.18) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27line-too-long%27%20OR%20E501)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fline_too_long.rs#L72)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

## [What it does](#what-it-does)

Checks for lines that exceed the specified maximum character length.

## [Why is this bad?](#why-is-this-bad)

Overlong lines can hurt readability. [PEP 8](https://peps.python.org/pep-0008/#maximum-line-length), for example, recommends
limiting lines to 79 characters. By default, this rule enforces a limit
of 88 characters for compatibility with Black and the Ruff formatter,
though that limit is configurable via the [`line-length`](../../settings/#line-length) setting.

In the interest of pragmatism, this rule makes a few exceptions when
determining whether a line is overlong. Namely, it:

1. Ignores lines that consist of a single "word" (i.e., without any
   whitespace between its characters).
2. Ignores lines that end with a URL, as long as the URL starts before
   the line-length threshold.
3. Ignores line that end with a pragma comment (e.g., `# type: ignore`
   or `# noqa`), as long as the pragma comment starts before the
   line-length threshold. That is, a line will not be flagged as
   overlong if a pragma comment *causes* it to exceed the line length.
   (This behavior aligns with that of the Ruff formatter.)
4. Ignores SPDX license identifiers and copyright notices
   (e.g., `# SPDX-License-Identifier: MIT`), which are machine-readable
   and should *not* wrap over multiple lines.

If [`lint.pycodestyle.ignore-overlong-task-comments`](../../settings/#lint_pycodestyle_ignore-overlong-task-comments) is `true`, this rule will
also ignore comments that start with any of the specified [`lint.task-tags`](../../settings/#lint_task-tags)
(e.g., `# TODO:`).

## [Example](#example)

```
my_function(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10)
```

Use instead:

```
my_function(
    param1, param2, param3, param4, param5,
    param6, param7, param8, param9, param10
)
```

## [Error suppression](#error-suppression)

Hint: when suppressing `E501` errors within multi-line strings (like
docstrings), the `noqa` directive should come at the end of the string
(after the closing triple quote), and will apply to the entire string, like
so:

```
"""Lorem ipsum dolor sit amet.

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.
"""  # noqa: E501
```

## [Options](#options)

* [`line-length`](../../settings/#line-length)
* [`lint.task-tags`](../../settings/#lint_task-tags)
* [`lint.pycodestyle.ignore-overlong-task-comments`](../../settings/#lint_pycodestyle_ignore-overlong-task-comments)
* [`lint.pycodestyle.max-line-length`](../../settings/#lint_pycodestyle_max-line-length)