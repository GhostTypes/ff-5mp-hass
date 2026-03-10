# [missing-trailing-comma (COM812)](#missing-trailing-comma-com812)

Added in [v0.0.223](https://github.com/astral-sh/ruff/releases/tag/v0.0.223) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-trailing-comma%27%20OR%20COM812)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_commas%2Frules%2Ftrailing_commas.rs#L155)

Derived from the **[flake8-commas](../#flake8-commas-com)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for the absence of trailing commas.

## [Why is this bad?](#why-is-this-bad)

The presence of a trailing comma can reduce diff size when parameters or
elements are added or removed from function calls, function definitions,
literals, etc.

## [Example](#example)

```
foo = {
    "bar": 1,
    "baz": 2
}
```

Use instead:

```
foo = {
    "bar": 1,
    "baz": 2,
}
```

## [Formatter compatibility](#formatter-compatibility)

We recommend against using this rule alongside the [formatter](https://docs.astral.sh/ruff/formatter/). The
formatter enforces consistent use of trailing commas, making the rule redundant.