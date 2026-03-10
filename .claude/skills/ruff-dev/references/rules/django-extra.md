# [django-extra (S610)](#django-extra-s610)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27django-extra%27%20OR%20S610)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fdjango_extra.rs#L36)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of Django's `extra` function where one or more arguments
passed are not literal expressions.

## [Why is this bad?](#why-is-this-bad)

Django's `extra` function can be used to execute arbitrary SQL queries,
which can in turn lead to SQL injection vulnerabilities.

## [Example](#example)

```
from django.contrib.auth.models import User

# String interpolation creates a security loophole that could be used
# for SQL injection:
User.objects.all().extra(select={"test": "%secure" % "nos"})
```

Use instead:

```
from django.contrib.auth.models import User

# SQL injection is impossible if all arguments are literal expressions:
User.objects.all().extra(select={"test": "secure"})
```

## [References](#references)

* [Django documentation: SQL injection protection](https://docs.djangoproject.com/en/dev/topics/security/#sql-injection-protection)
* [Common Weakness Enumeration: CWE-89](https://cwe.mitre.org/data/definitions/89.html)