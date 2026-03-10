# [continue-in-finally (PLE0116)](#continue-in-finally-ple0116)

Added in [v0.0.257](https://github.com/astral-sh/ruff/releases/tag/v0.0.257) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27continue-in-finally%27%20OR%20PLE0116)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fcontinue_in_finally.rs#L39)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for `continue` statements inside `finally`

## [Why is this bad?](#why-is-this-bad)

`continue` statements were not allowed within `finally` clauses prior to
Python 3.8. Using a `continue` statement within a `finally` clause can
cause a `SyntaxError`.

## [Example](#example)

```
while True:
    try:
        pass
    finally:
        continue
```

Use instead:

```
while True:
    try:
        pass
    except Exception:
        pass
    else:
        continue
```

## [Options](#options)

* [`target-version`](../../settings/#target-version)