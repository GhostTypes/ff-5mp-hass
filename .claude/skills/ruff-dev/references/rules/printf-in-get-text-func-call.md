# [printf-in-get-text-func-call (INT003)](#printf-in-get-text-func-call-int003)

Added in [v0.0.260](https://github.com/astral-sh/ruff/releases/tag/v0.0.260) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27printf-in-get-text-func-call%27%20OR%20INT003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_gettext%2Frules%2Fprintf_in_gettext_func_call.rs#L42)

Derived from the **[flake8-gettext](../#flake8-gettext-int)** linter.

## [What it does](#what-it-does)

Checks for printf-style formatted strings in `gettext` function calls.

## [Why is this bad?](#why-is-this-bad)

In the `gettext` API, the `gettext` function (often aliased to `_`) returns
a translation of its input argument by looking it up in a translation
catalog.

Calling `gettext` with a formatted string as its argument can cause
unexpected behavior. Since the formatted string is resolved before the
function call, the translation catalog will look up the formatted string,
rather than the printf-style template.

Instead, format the value returned by the function call, rather than
its argument.

## [Example](#example)

```
from gettext import gettext as _

name = "Maria"
_("Hello, %s!" % name)  # Looks for "Hello, Maria!".
```

Use instead:

```
from gettext import gettext as _

name = "Maria"
_("Hello, %s!") % name  # Looks for "Hello, %s!".
```

## [References](#references)

* [Python documentation: `gettext` — Multilingual internationalization services](https://docs.python.org/3/library/gettext.html)