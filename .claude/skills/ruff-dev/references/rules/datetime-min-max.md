# [datetime-min-max (DTZ901)](#datetime-min-max-dtz901)

Added in [0.10.0](https://github.com/astral-sh/ruff/releases/tag/0.10.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27datetime-min-max%27%20OR%20DTZ901)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_datetimez%2Frules%2Fdatetime_min_max.rs#L44)

Derived from the **[flake8-datetimez](../#flake8-datetimez-dtz)** linter.

## [What it does](#what-it-does)

Checks for uses of `datetime.datetime.min` and `datetime.datetime.max`.

## [Why is this bad?](#why-is-this-bad)

`datetime.min` and `datetime.max` are non-timezone-aware datetime objects.

As such, operations on `datetime.min` and `datetime.max` may behave
unexpectedly, as in:

```
import datetime

# Timezone: UTC-14
datetime.datetime.min.timestamp()  # ValueError: year 0 is out of range
datetime.datetime.max.timestamp()  # ValueError: year 10000 is out of range
```

## [Example](#example)

```
import datetime

datetime.datetime.max
```

Use instead:

```
import datetime

datetime.datetime.max.replace(tzinfo=datetime.UTC)
```

## [References](#references)

* [Python documentation: Aware and Naive Objects](https://docs.python.org/3/library/datetime.html#aware-and-naive-objects)