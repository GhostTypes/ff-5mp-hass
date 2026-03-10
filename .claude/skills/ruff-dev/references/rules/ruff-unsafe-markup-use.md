# [ruff-unsafe-markup-use (RUF035)](#ruff-unsafe-markup-use-ruf035)

Removed (since [0.10.0](https://github.com/astral-sh/ruff/releases/tag/0.10.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27ruff-unsafe-markup-use%27%20OR%20RUF035)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Funsafe_markup_use.rs#L75)

**Warning: This rule has been removed and its documentation is only available for historical reasons.**

## [Removed](#removed)

This rule was implemented in `bandit` and has been remapped to
[S704](../unsafe-markup-use/)

## [What it does](#what-it-does)

Checks for non-literal strings being passed to [`markupsafe.Markup`](https://markupsafe.palletsprojects.com/en/stable/escaping/#markupsafe.Markup).

## [Why is this bad?](#why-is-this-bad)

[`markupsafe.Markup`](https://markupsafe.palletsprojects.com/en/stable/escaping/#markupsafe.Markup) does not perform any escaping,
so passing dynamic content, like f-strings, variables or interpolated strings
will potentially lead to XSS vulnerabilities.

Instead you should interpolate the `Markup` object.

Using [`lint.flake8-bandit.extend-markup-names`](../../settings/#lint_flake8-bandit_extend-markup-names) additional objects can be
treated like `Markup`.

This rule was originally inspired by [flake8-markupsafe](https://github.com/vmagamedov/flake8-markupsafe) but doesn't carve
out any exceptions for i18n related calls by default.

You can use [`lint.flake8-bandit.allowed-markup-calls`](../../settings/#lint_flake8-bandit_allowed-markup-calls) to specify exceptions.

## [Example](#example)

Given:

```
from markupsafe import Markup

content = "<script>alert('Hello, world!')</script>"
html = Markup(f"<b>{content}</b>")  # XSS
```

Use instead:

```
from markupsafe import Markup

content = "<script>alert('Hello, world!')</script>"
html = Markup("<b>{}</b>").format(content)  # Safe
```

Given:

```
from markupsafe import Markup

lines = [
    Markup("<b>heading</b>"),
    "<script>alert('XSS attempt')</script>",
]
html = Markup("<br>".join(lines))  # XSS
```

Use instead:

```
from markupsafe import Markup

lines = [
    Markup("<b>heading</b>"),
    "<script>alert('XSS attempt')</script>",
]
html = Markup("<br>").join(lines)  # Safe
```

## [Options](#options)

* [`lint.flake8-bandit.extend-markup-names`](../../settings/#lint_flake8-bandit_extend-markup-names)
* [`lint.flake8-bandit.allowed-markup-calls`](../../settings/#lint_flake8-bandit_allowed-markup-calls)

## [References](#references)

* [MarkupSafe on PyPI](https://pypi.org/project/MarkupSafe/)
* [`markupsafe.Markup` API documentation](https://markupsafe.palletsprojects.com/en/stable/escaping/#markupsafe.Markup)