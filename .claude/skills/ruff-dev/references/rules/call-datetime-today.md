# [call-datetime-today (DTZ002)](#call-datetime-today-dtz002)

Added in [v0.0.188](https://github.com/astral-sh/ruff/releases/tag/v0.0.188) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27call-datetime-today%27%20OR%20DTZ002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_datetimez%2Frules%2Fcall_datetime_today.rs#L48)

Derived from the **[flake8-datetimez](../#flake8-datetimez-dtz)** linter.

## [What it does](#what-it-does)

Checks for usage of `datetime.datetime.today()`.

## [Why is this bad?](#why-is-this-bad)

`datetime` objects are "naive" by default, in that they do not include
timezone information. "Naive" objects are easy to understand, but ignore
some aspects of reality, which can lead to subtle bugs. Timezone-aware
`datetime` objects are preferred, as they represent a specific moment in
time, unlike "naive" objects.

`datetime.datetime.today()` creates a "naive" object; instead, use
`datetime.datetime.now(tz=...)` to create a timezone-aware object.

## [Example](#example)

```
import datetime

datetime.datetime.today()
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