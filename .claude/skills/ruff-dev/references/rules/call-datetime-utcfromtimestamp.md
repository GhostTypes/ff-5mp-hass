# [call-datetime-utcfromtimestamp (DTZ004)](#call-datetime-utcfromtimestamp-dtz004)

Added in [v0.0.188](https://github.com/astral-sh/ruff/releases/tag/v0.0.188) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27call-datetime-utcfromtimestamp%27%20OR%20DTZ004)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_datetimez%2Frules%2Fcall_datetime_utcfromtimestamp.rs#L49)

Derived from the **[flake8-datetimez](../#flake8-datetimez-dtz)** linter.

## [What it does](#what-it-does)

Checks for usage of `datetime.datetime.utcfromtimestamp()`.

## [Why is this bad?](#why-is-this-bad)

Python datetime objects can be naive or timezone-aware. While an aware
object represents a specific moment in time, a naive object does not
contain enough information to unambiguously locate itself relative to other
datetime objects. Since this can lead to errors, it is recommended to
always use timezone-aware objects.

`datetime.datetime.utcfromtimestamp()` returns a naive datetime
object; instead, use `datetime.datetime.fromtimestamp(ts, tz=...)`
to create a timezone-aware object.

## [Example](#example)

```
import datetime

datetime.datetime.utcfromtimestamp(946684800)
```

Use instead:

```
import datetime

datetime.datetime.fromtimestamp(946684800, tz=datetime.timezone.utc)
```

Or, on Python 3.11 and later:

```
import datetime

datetime.datetime.fromtimestamp(946684800, tz=datetime.UTC)
```

## [References](#references)

* [Python documentation: Aware and Naive Objects](https://docs.python.org/3/library/datetime.html#aware-and-naive-objects)