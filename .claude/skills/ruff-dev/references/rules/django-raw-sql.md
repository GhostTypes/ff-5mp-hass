# [django-raw-sql (S611)](#django-raw-sql-s611)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27django-raw-sql%27%20OR%20S611)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fdjango_raw_sql.rs#L27)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of Django's `RawSQL` function.

## [Why is this bad?](#why-is-this-bad)

Django's `RawSQL` function can be used to execute arbitrary SQL queries,
which can in turn lead to SQL injection vulnerabilities.

## [Example](#example)

```
from django.db.models.expressions import RawSQL
from django.contrib.auth.models import User

User.objects.annotate(val=RawSQL("%s" % input_param, []))
```

## [References](#references)

* [Django documentation: SQL injection protection](https://docs.djangoproject.com/en/dev/topics/security/#sql-injection-protection)
* [Common Weakness Enumeration: CWE-89](https://cwe.mitre.org/data/definitions/89.html)