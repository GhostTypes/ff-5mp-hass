# [airflow-dag-no-schedule-argument (AIR002)](#airflow-dag-no-schedule-argument-air002)

Added in [0.13.0](https://github.com/astral-sh/ruff/releases/tag/0.13.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27airflow-dag-no-schedule-argument%27%20OR%20AIR002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fairflow%2Frules%2Fdag_schedule_argument.rs#L43)

Derived from the **[Airflow](../#airflow-air)** linter.

## [What it does](#what-it-does)

Checks for a `DAG()` class or `@dag()` decorator without an explicit
`schedule` (or `schedule_interval` for Airflow 1) parameter.

## [Why is this bad?](#why-is-this-bad)

The default value of the `schedule` parameter on Airflow 2 and
`schedule_interval` on Airflow 1 is `timedelta(days=1)`, which is almost
never what a user is looking for. Airflow 3 changed the default value to `None`,
and would break existing dags using the implicit default.

If your dag does not have an explicit `schedule` / `schedule_interval` argument,
Airflow 2 schedules a run for it every day (at the time determined by `start_date`).
Such a dag will no longer be scheduled on Airflow 3 at all, without any
exceptions or other messages visible to the user.

## [Example](#example)

```
from airflow import DAG


# Using the implicit default schedule.
dag = DAG(dag_id="my_dag")
```

Use instead:

```
from datetime import timedelta

from airflow import DAG


dag = DAG(dag_id="my_dag", schedule=timedelta(days=1))
```