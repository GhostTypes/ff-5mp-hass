# [avoidable-escaped-quote (Q003)](#avoidable-escaped-quote-q003)

Added in [v0.0.88](https://github.com/astral-sh/ruff/releases/tag/v0.0.88) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27avoidable-escaped-quote%27%20OR%20Q003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_quotes%2Frules%2Favoidable_escaped_quote.rs#L36)

Derived from the **[flake8-quotes](../#flake8-quotes-q)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for strings that include escaped quotes, and suggests changing
the quote style to avoid the need to escape them.

## [Why is this bad?](#why-is-this-bad)

It's preferable to avoid escaped quotes in strings. By changing the
outer quote style, you can avoid escaping inner quotes.

## [Example](#example)

```
foo = "bar\"s"
```

Use instead:

```
foo = 'bar"s'
```

## [Formatter compatibility](#formatter-compatibility)

We recommend against using this rule alongside the [formatter](https://docs.astral.sh/ruff/formatter). The
formatter automatically removes unnecessary escapes, making the rule
redundant.