# [trailing-whitespace (W291)](#trailing-whitespace-w291)

Added in [v0.0.253](https://github.com/astral-sh/ruff/releases/tag/v0.0.253) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27trailing-whitespace%27%20OR%20W291)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Ftrailing_whitespace.rs#L34)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for superfluous trailing whitespace.

## [Why is this bad?](#why-is-this-bad)

According to [PEP 8](https://peps.python.org/pep-0008/#other-recommendations), "avoid trailing whitespace anywhere. Because it’s usually
invisible, it can be confusing"

## [Example](#example)

```
spam(1) \n#
```

Use instead:

```
spam(1)\n#
```

## [Fix safety](#fix-safety)

This fix is marked unsafe if the whitespace is inside a multiline string,
as removing it changes the string's content.