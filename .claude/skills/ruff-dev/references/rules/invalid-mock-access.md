# [invalid-mock-access (PGH005)](#invalid-mock-access-pgh005)

Added in [v0.0.266](https://github.com/astral-sh/ruff/releases/tag/v0.0.266) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-mock-access%27%20OR%20PGH005)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpygrep_hooks%2Frules%2Finvalid_mock_access.rs#L35)

Derived from the **[pygrep-hooks](../#pygrep-hooks-pgh)** linter.

## [What it does](#what-it-does)

Checks for common mistakes when using mock objects.

## [Why is this bad?](#why-is-this-bad)

The `mock` module exposes an assertion API that can be used to verify that
mock objects undergo expected interactions. This rule checks for common
mistakes when using this API.

For example, it checks for mock attribute accesses that should be replaced
with mock method calls.

## [Example](#example)

```
my_mock.assert_called
```

Use instead:

```
my_mock.assert_called()
```