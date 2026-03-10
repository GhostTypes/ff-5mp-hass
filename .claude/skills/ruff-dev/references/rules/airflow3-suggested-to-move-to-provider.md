# [airflow3-suggested-to-move-to-provider (AIR312)](#airflow3-suggested-to-move-to-provider-air312)

Added in [0.13.0](https://github.com/astral-sh/ruff/releases/tag/0.13.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27airflow3-suggested-to-move-to-provider%27%20OR%20AIR312)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fairflow%2Frules%2Fsuggested_to_move_to_provider_in_3.rs#L53)

Derived from the **[Airflow](../#airflow-air)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of Airflow functions and values that have been moved to its providers
but still have a compatibility layer (e.g., `apache-airflow-providers-standard`).

## [Why is this bad?](#why-is-this-bad)

Airflow 3.0 moved various deprecated functions, members, and other
values to its providers. Even though these symbols still work fine on Airflow 3.0,
they are expected to be removed in a future version. The user is suggested to install
the corresponding provider and replace the original usage with the one in the provider.

## [Example](#example)

```
from airflow.operators.python import PythonOperator


def print_context(ds=None, **kwargs):
    print(kwargs)
    print(ds)


print_the_context = PythonOperator(
    task_id="print_the_context", python_callable=print_context
)
```

Use instead:

```
from airflow.providers.standard.operators.python import PythonOperator


def print_context(ds=None, **kwargs):
    print(kwargs)
    print(ds)


print_the_context = PythonOperator(
    task_id="print_the_context", python_callable=print_context
)
```