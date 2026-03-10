# [format-in-get-text-func-call (INT002)](#format-in-get-text-func-call-int002)

Added in [v0.0.260](https://github.com/astral-sh/ruff/releases/tag/v0.0.260) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27format-in-get-text-func-call%27%20OR%20INT002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_gettext%2Frules%2Fformat_in_gettext_func_call.rs#L43)

Derived from the **[flake8-gettext](../#flake8-gettext-int)** linter.

## [What it does](#what-it-does)

Checks for `str.format` calls in `gettext` function calls.

## [Why is this bad?](#why-is-this-bad)

In the `gettext` API, the `gettext` function (often aliased to `_`) returns
a translation of its input argument by looking it up in a translation
catalog.

Calling `gettext` with a formatted string as its argument can cause
unexpected behavior. Since the formatted string is resolved before the
function call, the translation catalog will look up the formatted string,
rather than the `str.format`-style template.

Instead, format the value returned by the function call, rather than
its argument.

## [Example](#example)

```
from gettext import gettext as _

name = "Maria"
_("Hello, {}!".format(name))  # Looks for "Hello, Maria!".
```

Use instead:

```
from gettext import gettext as _

name = "Maria"
_("Hello, %s!") % name  # Looks for "Hello, %s!".
```

## [References](#references)

* [Python documentation: `gettext` — Multilingual internationalization services](https://docs.python.org/3/library/gettext.html)