# [redirected-noqa (RUF101)](#redirected-noqa-ruf101)

Added in [0.6.0](https://github.com/astral-sh/ruff/releases/tag/0.6.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27redirected-noqa%27%20OR%20RUF101)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fredirected_noqa.rs#L27)

Fix is always available.

## [What it does](#what-it-does)

Checks for `noqa` directives that use redirected rule codes.

## [Why is this bad?](#why-is-this-bad)

When one of Ruff's rule codes has been redirected, the implication is that the rule has
been deprecated in favor of another rule or code. To keep your codebase
consistent and up-to-date, prefer the canonical rule code over the deprecated
code.

## [Example](#example)

```
x = eval(command)  # noqa: PGH001
```

Use instead:

```
x = eval(command)  # noqa: S307
```