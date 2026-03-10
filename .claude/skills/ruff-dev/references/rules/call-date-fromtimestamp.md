# [call-date-fromtimestamp (DTZ012)](#call-date-fromtimestamp-dtz012)

Added in [v0.0.188](https://github.com/astral-sh/ruff/releases/tag/v0.0.188) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27call-date-fromtimestamp%27%20OR%20DTZ012)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_datetimez%2Frules%2Fcall_date_fromtimestamp.rs#L47)

Derived from the **[flake8-datetimez](../#flake8-datetimez-dtz)** linter.

## [What it does](#what-it-does)

Checks for usage of `datetime.date.fromtimestamp()`.

## [Why is this bad?](#why-is-this-bad)

Python date objects are naive, that is, not timezone-aware. While an aware
object represents a specific moment in time, a naive object does not
contain enough information to unambiguously locate itself relative to other
datetime objects. Since this can lead to errors, it is recommended to
always use timezone-aware objects.

`datetime.date.fromtimestamp(ts)` returns a naive date object.
Instead, use `datetime.datetime.fromtimestamp(ts, tz=...).date()` to
create a timezone-aware datetime object and retrieve its date component.

## [Example](#example)

```
import datetime

datetime.date.fromtimestamp(946684800)
```

Use instead:

```
import datetime

datetime.datetime.fromtimestamp(946684800, tz=datetime.timezone.utc).date()
```

Or, for Python 3.11 and later:

```
import datetime

datetime.datetime.fromtimestamp(946684800, tz=datetime.UTC).date()
```

## [References](#references)

* [Python documentation: Aware and Naive Objects](https://docs.python.org/3/library/datetime.html#aware-and-naive-objects)