# [assert-raises-exception (B017)](#assert-raises-exception-b017)

Added in [v0.0.83](https://github.com/astral-sh/ruff/releases/tag/v0.0.83) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27assert-raises-exception%27%20OR%20B017)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fassert_raises_exception.rs#L31)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for `assertRaises` and `pytest.raises` context managers that catch
`Exception` or `BaseException`.

## [Why is this bad?](#why-is-this-bad)

These forms catch every `Exception`, which can lead to tests passing even
if, e.g., the code under consideration raises a `SyntaxError` or
`IndentationError`.

Either assert for a more specific exception (builtin or custom), or use
`assertRaisesRegex` or `pytest.raises(..., match=<REGEX>)` respectively.

## [Example](#example)

```
self.assertRaises(Exception, foo)
```

Use instead:

```
self.assertRaises(SomeSpecificException, foo)
```