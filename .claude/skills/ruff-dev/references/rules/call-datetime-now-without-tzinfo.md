# [call-datetime-now-without-tzinfo (DTZ005)](#call-datetime-now-without-tzinfo-dtz005)

Added in [v0.0.188](https://github.com/astral-sh/ruff/releases/tag/v0.0.188) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27call-datetime-now-without-tzinfo%27%20OR%20DTZ005)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_datetimez%2Frules%2Fcall_datetime_now_without_tzinfo.rs#L48)

Derived from the **[flake8-datetimez](../#flake8-datetimez-dtz)** linter.

## [What it does](#what-it-does)

Checks for usages of `datetime.datetime.now()` that do not specify a timezone.

## [Why is this bad?](#why-is-this-bad)

Python datetime objects can be naive or timezone-aware. While an aware
object represents a specific moment in time, a naive object does not
contain enough information to unambiguously locate itself relative to other
datetime objects. Since this can lead to errors, it is recommended to
always use timezone-aware objects.

`datetime.datetime.now()` or `datetime.datetime.now(tz=None)` returns a naive
datetime object. Instead, use `datetime.datetime.now(tz=<timezone>)` to create
a timezone-aware object.

## [Example](#example)

```
import datetime

datetime.datetime.now()
```

Use instead:

```
import datetime

datetime.datetime.now(tz=datetime.timezone.utc)
```

Or, for Python 3.11 and later:

```
import datetime

datetime.datetime.now(tz=datetime.UTC)
```

## [References](#references)

* [Python documentation: Aware and Naive Objects](https://docs.python.org/3/library/datetime.html#aware-and-naive-objects)