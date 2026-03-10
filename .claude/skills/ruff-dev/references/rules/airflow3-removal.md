# [airflow3-removal (AIR301)](#airflow3-removal-air301)

Added in [0.13.0](https://github.com/astral-sh/ruff/releases/tag/0.13.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27airflow3-removal%27%20OR%20AIR301)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fairflow%2Frules%2Fremoval_in_3.rs#L43)

Derived from the **[Airflow](../#airflow-air)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of deprecated Airflow functions and values.

## [Why is this bad?](#why-is-this-bad)

Airflow 3.0 removed various deprecated functions, members, and other
values. Some have more modern replacements. Others are considered too niche
and not worth continued maintenance in Airflow.

## [Example](#example)

```
from airflow.utils.dates import days_ago


yesterday = days_ago(today, 1)
```

Use instead:

```
from datetime import timedelta


yesterday = today - timedelta(days=1)
```