# [commented-out-code (ERA001)](#commented-out-code-era001)

Added in [v0.0.145](https://github.com/astral-sh/ruff/releases/tag/v0.0.145) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27commented-out-code%27%20OR%20ERA001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Feradicate%2Frules%2Fcommented_out_code.rs#L32)

Derived from the **[eradicate](../#eradicate-era)** linter.

## [What it does](#what-it-does)

Checks for commented-out Python code.

## [Why is this bad?](#why-is-this-bad)

Commented-out code is dead code, and is often included inadvertently.
It should be removed.

## [Known problems](#known-problems)

Prone to false positives when checking comments that resemble Python code,
but are not actually Python code ([#4845](https://github.com/astral-sh/ruff/issues/4845)).

## [Example](#example)

```
# print("Hello, world!")
```

## [Options](#options)

* [`lint.task-tags`](../../settings/#lint_task-tags)