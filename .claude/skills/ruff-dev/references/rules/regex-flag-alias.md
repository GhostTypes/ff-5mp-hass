# [regex-flag-alias (FURB167)](#regex-flag-alias-furb167)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27regex-flag-alias%27%20OR%20FURB167)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fregex_flag_alias.rs#L34)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for the use of shorthand aliases for regular expression flags
(e.g., `re.I` instead of `re.IGNORECASE`).

## [Why is this bad?](#why-is-this-bad)

The regular expression module provides descriptive names for each flag,
along with single-letter aliases. Prefer the descriptive names, as they
are more readable and self-documenting.

## [Example](#example)

```
import re

if re.match("^hello", "hello world", re.I):
    ...
```

Use instead:

```
import re

if re.match("^hello", "hello world", re.IGNORECASE):
    ...
```