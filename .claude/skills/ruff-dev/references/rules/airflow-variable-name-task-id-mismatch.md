# [airflow-variable-name-task-id-mismatch (AIR001)](#airflow-variable-name-task-id-mismatch-air001)

Added in [v0.0.271](https://github.com/astral-sh/ruff/releases/tag/v0.0.271) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27airflow-variable-name-task-id-mismatch%27%20OR%20AIR001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fairflow%2Frules%2Ftask_variable_name.rs#L34)

Derived from the **[Airflow](../#airflow-air)** linter.

## [What it does](#what-it-does)

Checks that the task variable name matches the `task_id` value for
Airflow Operators.

## [Why is this bad?](#why-is-this-bad)

When initializing an Airflow Operator, for consistency, the variable
name should match the `task_id` value. This makes it easier to
follow the flow of the DAG.

## [Example](#example)

```
from airflow.operators import PythonOperator


incorrect_name = PythonOperator(task_id="my_task")
```

Use instead:

```
from airflow.operators import PythonOperator


my_task = PythonOperator(task_id="my_task")
```