# [indented-form-feed (RUF054)](#indented-form-feed-ruf054)

Preview (since [0.9.6](https://github.com/astral-sh/ruff/releases/tag/0.9.6)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27indented-form-feed%27%20OR%20RUF054)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Findented_form_feed.rs#L33)

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for form feed characters preceded by either a space or a tab.

## [Why is this bad?](#why-is-this-bad)

[The language reference](https://docs.python.org/3/reference/lexical_analysis.html#indentation) states:

> A formfeed character may be present at the start of the line;
> it will be ignored for the indentation calculations above.
> Formfeed characters occurring elsewhere in the leading whitespace
> have an undefined effect (for instance, they may reset the space count to zero).

## [Example](#example)

```
if foo():\n    \fbar()
```

Use instead:

```
if foo():\n    bar()
```