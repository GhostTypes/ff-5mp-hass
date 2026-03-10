# [bad-quotes-docstring (Q002)](#bad-quotes-docstring-q002)

Added in [v0.0.88](https://github.com/astral-sh/ruff/releases/tag/v0.0.88) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27bad-quotes-docstring%27%20OR%20Q002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_quotes%2Frules%2Fcheck_string_quotes.rs#L153)

Derived from the **[flake8-quotes](../#flake8-quotes-q)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for docstrings that use single quotes or double quotes, depending
on the value of the [`lint.flake8-quotes.docstring-quotes`](../../settings/#lint_flake8-quotes_docstring-quotes) setting.

## [Why is this bad?](#why-is-this-bad)

Consistency is good. Use either single or double quotes for docstring
strings, but be consistent.

## [Example](#example)

```
'''
bar
'''
```

Assuming `docstring-quotes` is set to `double`, use instead:

```
"""
bar
"""
```

## [Options](#options)

* [`lint.flake8-quotes.docstring-quotes`](../../settings/#lint_flake8-quotes_docstring-quotes)

## [Formatter compatibility](#formatter-compatibility)

We recommend against using this rule alongside the [formatter](https://docs.astral.sh/ruff/formatter). The
formatter enforces double quotes for docstrings, making the rule
redundant.