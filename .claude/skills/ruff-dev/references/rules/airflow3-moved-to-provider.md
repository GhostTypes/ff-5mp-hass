# [airflow3-moved-to-provider (AIR302)](#airflow3-moved-to-provider-air302)

Added in [0.13.0](https://github.com/astral-sh/ruff/releases/tag/0.13.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27airflow3-moved-to-provider%27%20OR%20AIR302)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fairflow%2Frules%2Fmoved_to_provider_in_3.rs#L37)

Derived from the **[Airflow](../#airflow-air)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of Airflow functions and values that have been moved to its providers
(e.g., `apache-airflow-providers-fab`).

## [Why is this bad?](#why-is-this-bad)

Airflow 3.0 moved various deprecated functions, members, and other
values to its providers. The user needs to install the corresponding provider and replace
the original usage with the one in the provider.

## [Example](#example)

```
from airflow.auth.managers.fab.fab_auth_manager import FabAuthManager

fab_auth_manager_app = FabAuthManager().get_fastapi_app()
```

Use instead:

```
from airflow.providers.fab.auth_manager.fab_auth_manager import FabAuthManager

fab_auth_manager_app = FabAuthManager().get_fastapi_app()
```