# [missing-whitespace-after-keyword (E275)](#missing-whitespace-after-keyword-e275)

Preview (since [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-whitespace-after-keyword%27%20OR%20E275)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Flogical_lines%2Fmissing_whitespace_after_keyword.rs#L29)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for missing whitespace after keywords.

## [Why is this bad?](#why-is-this-bad)

Missing whitespace after keywords makes the code harder to read.

## [Example](#example)

```
if(True):
    pass
```

Use instead:

```
if (True):
    pass
```

## [References](#references)

* [Python documentation: Keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)