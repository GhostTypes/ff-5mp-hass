# [datetime-timezone-utc (UP017)](#datetime-timezone-utc-up017)

Added in [v0.0.192](https://github.com/astral-sh/ruff/releases/tag/v0.0.192) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27datetime-timezone-utc%27%20OR%20UP017)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fdatetime_utc_alias.rs#L36)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of `datetime.timezone.utc`.

## [Why is this bad?](#why-is-this-bad)

As of Python 3.11, `datetime.UTC` is an alias for `datetime.timezone.utc`.
The alias is more readable and generally preferred over the full path.

## [Example](#example)

```
import datetime

datetime.timezone.utc
```

Use instead:

```
import datetime

datetime.UTC
```

## [Options](#options)

* [`target-version`](../../settings/#target-version)

## [References](#references)

* [Python documentation: `datetime.UTC`](https://docs.python.org/3/library/datetime.html#datetime.UTC)