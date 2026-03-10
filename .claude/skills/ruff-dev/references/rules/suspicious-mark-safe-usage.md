# [suspicious-mark-safe-usage (S308)](#suspicious-mark-safe-usage-s308)

Added in [v0.0.258](https://github.com/astral-sh/ruff/releases/tag/v0.0.258) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-mark-safe-usage%27%20OR%20S308)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_function_call.rs#L392)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of calls to `django.utils.safestring.mark_safe`.

## [Why is this bad?](#why-is-this-bad)

Cross-site scripting (XSS) vulnerabilities allow attackers to execute
arbitrary JavaScript. To guard against XSS attacks, Django templates
assumes that data is unsafe and automatically escapes malicious strings
before rending them.

`django.utils.safestring.mark_safe` marks a string as safe for use in HTML
templates, bypassing XSS protection. Its usage can be dangerous if the
contents of the string are dynamically generated, because it may allow
cross-site scripting attacks if the string is not properly escaped.

For dynamically generated strings, consider utilizing
`django.utils.html.format_html`.

In [preview](https://docs.astral.sh/ruff/preview/), this rule will also flag references to `django.utils.safestring.mark_safe`.

## [Example](#example)

```
from django.utils.safestring import mark_safe


def render_username(username):
    return mark_safe(f"<i>{username}</i>")  # Dangerous if username is user-provided.
```

Use instead:

```
from django.utils.html import format_html


def render_username(username):
    return format_html("<i>{}</i>", username)  # username is escaped.
```

## [References](#references)

* [Django documentation: `mark_safe`](https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.safestring.mark_safe)
* [Django documentation: Cross Site Scripting (XSS) protection](https://docs.djangoproject.com/en/dev/topics/security/#cross-site-scripting-xss-protection)
* [Common Weakness Enumeration: CWE-80](https://cwe.mitre.org/data/definitions/80.html)