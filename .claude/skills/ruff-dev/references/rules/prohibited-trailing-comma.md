# [prohibited-trailing-comma (COM819)](#prohibited-trailing-comma-com819)

Added in [v0.0.223](https://github.com/astral-sh/ruff/releases/tag/v0.0.223) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27prohibited-trailing-comma%27%20OR%20COM819)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_commas%2Frules%2Ftrailing_commas.rs#L234)

Derived from the **[flake8-commas](../#flake8-commas-com)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for the presence of prohibited trailing commas.

## [Why is this bad?](#why-is-this-bad)

Trailing commas are not essential in some cases and can therefore be viewed
as unnecessary.

## [Example](#example)

```
foo = (1, 2, 3,)
```

Use instead:

```
foo = (1, 2, 3)
```

## [Formatter compatibility](#formatter-compatibility)

We recommend against using this rule alongside the [formatter](https://docs.astral.sh/ruff/formatter/). The
formatter enforces consistent use of trailing commas, making the rule redundant.