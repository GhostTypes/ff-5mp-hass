# [airflow3-suggested-update (AIR311)](#airflow3-suggested-update-air311)

Added in [0.13.0](https://github.com/astral-sh/ruff/releases/tag/0.13.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27airflow3-suggested-update%27%20OR%20AIR311)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fairflow%2Frules%2Fsuggested_to_update_3_0.rs#L39)

Derived from the **[Airflow](../#airflow-air)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of deprecated Airflow functions and values that still have
a compatibility layer.

## [Why is this bad?](#why-is-this-bad)

Airflow 3.0 removed various deprecated functions, members, and other
values. Some have more modern replacements. Others are considered too niche
and not worth continued maintenance in Airflow.
Even though these symbols still work fine on Airflow 3.0, they are expected to be removed in a future version.
Where available, users should replace the removed functionality with the new alternatives.

## [Example](#example)

```
from airflow import Dataset


Dataset(uri="test://test/")
```

Use instead:

```
from airflow.sdk import Asset


Asset(uri="test://test/")
```