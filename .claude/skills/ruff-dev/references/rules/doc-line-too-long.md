# [doc-line-too-long (W505)](#doc-line-too-long-w505)

Added in [v0.0.219](https://github.com/astral-sh/ruff/releases/tag/v0.0.219) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27doc-line-too-long%27%20OR%20W505)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fdoc_line_too_long.rs#L74)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

## [What it does](#what-it-does)

Checks for doc lines that exceed the specified maximum character length.

## [Why is this bad?](#why-is-this-bad)

For flowing long blocks of text (docstrings or comments), overlong lines
can hurt readability. [PEP 8](https://peps.python.org/pep-0008/#maximum-line-length), for example, recommends that such lines be
limited to 72 characters, while this rule enforces the limit specified by
the [`lint.pycodestyle.max-doc-length`](../../settings/#lint_pycodestyle_max-doc-length) setting. (If no value is provided, this
rule will be ignored, even if it's added to your `--select` list.)

In the context of this rule, a "doc line" is defined as a line consisting
of either a standalone comment or a standalone string, like a docstring.

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

If [`lint.pycodestyle.ignore-overlong-task-comments`](../../settings/#lint_pycodestyle_ignore-overlong-task-comments) is `true`, this rule will
also ignore comments that start with any of the specified [`lint.task-tags`](../../settings/#lint_task-tags)
(e.g., `# TODO:`).

## [Example](#example)

```
def function(x):
    """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis auctor purus ut ex fermentum, at maximus est hendrerit."""
```

Use instead:

```
def function(x):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Duis auctor purus ut ex fermentum, at maximus est hendrerit.
    """
```

## [Error suppression](#error-suppression)

Hint: when suppressing `W505` errors within multi-line strings (like
docstrings), the `noqa` directive should come at the end of the string
(after the closing triple quote), and will apply to the entire string, like
so:

```
"""Lorem ipsum dolor sit amet.

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.
"""  # noqa: W505
```

## [Options](#options)

* [`lint.task-tags`](../../settings/#lint_task-tags)
* [`lint.pycodestyle.max-doc-length`](../../settings/#lint_pycodestyle_max-doc-length)
* [`lint.pycodestyle.ignore-overlong-task-comments`](../../settings/#lint_pycodestyle_ignore-overlong-task-comments)