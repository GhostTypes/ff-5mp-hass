# [call-datetime-strptime-without-zone (DTZ007)](#call-datetime-strptime-without-zone-dtz007)

Added in [v0.0.188](https://github.com/astral-sh/ruff/releases/tag/v0.0.188) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27call-datetime-strptime-without-zone%27%20OR%20DTZ007)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_datetimez%2Frules%2Fcall_datetime_strptime_without_zone.rs#L53)

Derived from the **[flake8-datetimez](../#flake8-datetimez-dtz)** linter.

## [What it does](#what-it-does)

Checks for uses of `datetime.datetime.strptime()` that lead to naive
datetime objects.

## [Why is this bad?](#why-is-this-bad)

Python datetime objects can be naive or timezone-aware. While an aware
object represents a specific moment in time, a naive object does not
contain enough information to unambiguously locate itself relative to other
datetime objects. Since this can lead to errors, it is recommended to
always use timezone-aware objects.

`datetime.datetime.strptime()` without `%z` returns a naive datetime
object. Follow it with `.replace(tzinfo=<timezone>)` or `.astimezone()`.

## [Example](#example)

```
import datetime

datetime.datetime.strptime("2022/01/31", "%Y/%m/%d")
```

Instead, use `.replace(tzinfo=<timezone>)`:

```
import datetime

datetime.datetime.strptime("2022/01/31", "%Y/%m/%d").replace(
    tzinfo=datetime.timezone.utc
)
```

Or, use `.astimezone()`:

```
import datetime

datetime.datetime.strptime("2022/01/31", "%Y/%m/%d").astimezone(datetime.timezone.utc)
```

On Python 3.11 and later, `datetime.timezone.utc` can be replaced with
`datetime.UTC`.

## [References](#references)

* [Python documentation: Aware and Naive Objects](https://docs.python.org/3/library/datetime.html#aware-and-naive-objects)
* [Python documentation: `strftime()` and `strptime()` Behavior](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)