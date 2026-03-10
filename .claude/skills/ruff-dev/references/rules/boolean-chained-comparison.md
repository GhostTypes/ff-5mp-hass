# [boolean-chained-comparison (PLR1716)](#boolean-chained-comparison-plr1716)

Added in [0.9.0](https://github.com/astral-sh/ruff/releases/tag/0.9.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27boolean-chained-comparison%27%20OR%20PLR1716)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fboolean_chained_comparison.rs#L37)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is always available.

## [What it does](#what-it-does)

Check for chained boolean operations that can be simplified.

## [Why is this bad?](#why-is-this-bad)

Refactoring the code will improve readability for these cases.

## [Example](#example)

```
a = int(input())
b = int(input())
c = int(input())
if a < b and b < c:
    pass
```

Use instead:

```
a = int(input())
b = int(input())
c = int(input())
if a < b < c:
    pass
```