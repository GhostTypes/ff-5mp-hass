# [bad-quotes-inline-string (Q000)](#bad-quotes-inline-string-q000)

Added in [v0.0.88](https://github.com/astral-sh/ruff/releases/tag/v0.0.88) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27bad-quotes-inline-string%27%20OR%20Q000)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_quotes%2Frules%2Fcheck_string_quotes.rs#L39)

Derived from the **[flake8-quotes](../#flake8-quotes-q)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for inline strings that use single quotes or double quotes,
depending on the value of the [`lint.flake8-quotes.inline-quotes`](../../settings/#lint_flake8-quotes_inline-quotes) option.

## [Why is this bad?](#why-is-this-bad)

Consistency is good. Use either single or double quotes for inline
strings, but be consistent.

## [Example](#example)

```
foo = 'bar'
```

Assuming `inline-quotes` is set to `double`, use instead:

```
foo = "bar"
```

## [Options](#options)

* [`lint.flake8-quotes.inline-quotes`](../../settings/#lint_flake8-quotes_inline-quotes)

## [Formatter compatibility](#formatter-compatibility)

We recommend against using this rule alongside the [formatter](https://docs.astral.sh/ruff/formatter). The
formatter enforces consistent quotes for inline strings, making the rule
redundant.