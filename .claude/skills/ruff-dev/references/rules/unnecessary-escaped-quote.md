# [unnecessary-escaped-quote (Q004)](#unnecessary-escaped-quote-q004)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-escaped-quote%27%20OR%20Q004)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_quotes%2Frules%2Funnecessary_escaped_quote.rs#L35)

Derived from the **[flake8-quotes](../#flake8-quotes-q)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for strings that include unnecessarily escaped quotes.

## [Why is this bad?](#why-is-this-bad)

If a string contains an escaped quote that doesn't match the quote
character used for the string, it's unnecessary and can be removed.

## [Example](#example)

```
foo = "bar\'s"
```

Use instead:

```
foo = "bar's"
```

## [Formatter compatibility](#formatter-compatibility)

We recommend against using this rule alongside the [formatter](https://docs.astral.sh/ruff/formatter). The
formatter automatically removes unnecessary escapes, making the rule
redundant.