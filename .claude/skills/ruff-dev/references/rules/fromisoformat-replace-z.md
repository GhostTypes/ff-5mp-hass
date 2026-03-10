# [fromisoformat-replace-z (FURB162)](#fromisoformat-replace-z-furb162)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27fromisoformat-replace-z%27%20OR%20FURB162)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Ffromisoformat_replace_z.rs#L69)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `datetime.fromisoformat()` calls
where the only argument is an inline replacement
of `Z` with a zero offset timezone.

## [Why is this bad?](#why-is-this-bad)

On Python 3.11 and later, `datetime.fromisoformat()` can handle most [ISO 8601](https://www.iso.org/obp/ui/#iso:std:iso:8601)
formats including ones affixed with `Z`, so such an operation is unnecessary.

More information on unsupported formats
can be found in [the official documentation](https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat).

## [Example](#example)

```
from datetime import datetime


date = "2025-01-01T00:00:00Z"

datetime.fromisoformat(date.replace("Z", "+00:00"))
datetime.fromisoformat(date[:-1] + "-00")
datetime.fromisoformat(date.strip("Z", "-0000"))
datetime.fromisoformat(date.rstrip("Z", "-00:00"))
```

Use instead:

```
from datetime import datetime


date = "2025-01-01T00:00:00Z"

datetime.fromisoformat(date)
```

## [Fix safety](#fix-safety)

The fix is always marked as unsafe,
as it might change the program's behaviour.

For example, working code might become non-working:

```
d = "Z2025-01-01T00:00:00Z"  # Note the leading `Z`

datetime.fromisoformat(d.strip("Z") + "+00:00")  # Fine
datetime.fromisoformat(d)  # Runtime error
```

## [References](#references)

* [What’s New In Python 3.11 § `datetime`](https://docs.python.org/3/whatsnew/3.11.html#datetime)
* [`fromisoformat`](https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat)