# [unused-noqa (RUF100)](#unused-noqa-ruf100)

Added in [v0.0.155](https://github.com/astral-sh/ruff/releases/tag/v0.0.155) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unused-noqa%27%20OR%20RUF100)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Funused_noqa.rs#L60)

Fix is always available.

## [What it does](#what-it-does)

Checks for `noqa` directives that are no longer applicable.

## [Why is this bad?](#why-is-this-bad)

A `noqa` directive that no longer matches any diagnostic violations is
likely included by mistake, and should be removed to avoid confusion.

## [Example](#example)

```
import foo  # noqa: F401


def bar():
    foo.bar()
```

Use instead:

```
import foo


def bar():
    foo.bar()
```

## [Options](#options)

* [`lint.external`](../../settings/#lint_external)

## [References](#references)

* [Ruff error suppression](https://docs.astral.sh/ruff/linter/#error-suppression)