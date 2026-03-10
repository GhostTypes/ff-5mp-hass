# [bad-quotes-multiline-string (Q001)](#bad-quotes-multiline-string-q001)

Added in [v0.0.88](https://github.com/astral-sh/ruff/releases/tag/v0.0.88) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27bad-quotes-multiline-string%27%20OR%20Q001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_quotes%2Frules%2Fcheck_string_quotes.rs#L97)

Derived from the **[flake8-quotes](../#flake8-quotes-q)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for multiline strings that use single quotes or double quotes,
depending on the value of the [`lint.flake8-quotes.multiline-quotes`](../../settings/#lint_flake8-quotes_multiline-quotes)
setting.

## [Why is this bad?](#why-is-this-bad)

Consistency is good. Use either single or double quotes for multiline
strings, but be consistent.

## [Example](#example)

```
foo = '''
bar
'''
```

Assuming `multiline-quotes` is set to `double`, use instead:

```
foo = """
bar
"""
```

## [Options](#options)

* [`lint.flake8-quotes.multiline-quotes`](../../settings/#lint_flake8-quotes_multiline-quotes)

## [Formatter compatibility](#formatter-compatibility)

We recommend against using this rule alongside the [formatter](https://docs.astral.sh/ruff/formatter). The
formatter enforces double quotes for multiline strings, making the rule
redundant.