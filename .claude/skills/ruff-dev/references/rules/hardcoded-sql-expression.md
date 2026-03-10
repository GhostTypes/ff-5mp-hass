# [hardcoded-sql-expression (S608)](#hardcoded-sql-expression-s608)

Added in [v0.0.245](https://github.com/astral-sh/ruff/releases/tag/v0.0.245) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27hardcoded-sql-expression%27%20OR%20S608)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fhardcoded_sql_expression.rs#L47)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for strings that resemble SQL statements involved in some form
string building operation.

## [Why is this bad?](#why-is-this-bad)

SQL injection is a common attack vector for web applications. Directly
interpolating user input into SQL statements should always be avoided.
Instead, favor parameterized queries, in which the SQL statement is
provided separately from its parameters, as supported by `psycopg3`
and other database drivers and ORMs.

## [Example](#example)

```
query = "DELETE FROM foo WHERE id = '%s'" % identifier
```

## [References](#references)

* [B608: Test for SQL injection](https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html)
* [psycopg3: Server-side binding](https://www.psycopg.org/psycopg3/docs/basic/from_pg2.html#server-side-binding)