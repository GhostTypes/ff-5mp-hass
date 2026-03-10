# [missing-f-string-syntax (RUF027)](#missing-f-string-syntax-ruf027)

Preview (since [v0.2.1](https://github.com/astral-sh/ruff/releases/tag/v0.2.1)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-f-string-syntax%27%20OR%20RUF027)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fmissing_fstring_syntax.rs#L64)

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Searches for strings that look like they were meant to be f-strings, but are missing an `f` prefix.

## [Why is this bad?](#why-is-this-bad)

Expressions inside curly braces are only evaluated if the string has an `f` prefix.

## [Details](#details)

There are many possible string literals which are not meant to be f-strings
despite containing f-string-like syntax. As such, this lint ignores all strings
where one of the following conditions applies:

1. The string is a standalone expression. For example, the rule ignores all docstrings.
2. The string is part of a function call with argument names that match at least one variable
   (for example: `format("Message: {value}", value="Hello World")`)
3. The string (or a parent expression of the string) has a direct method call on it
   (for example: `"{value}".format(...)`)
4. The string has no `{...}` expression sections, or uses invalid f-string syntax.
5. The string references variables that are not in scope, or it doesn't capture variables at all.
6. Any format specifiers in the potential f-string are invalid.
7. The string is part of a function call that is known to expect a template string rather than an
   evaluated f-string: for example, a [`logging`](https://docs.python.org/3/howto/logging-cookbook.html#using-particular-formatting-styles-throughout-your-application) call, a [`gettext`](https://docs.python.org/3/library/gettext.html) call,
   or a [FastAPI path](https://fastapi.tiangolo.com/tutorial/path-params/).

## [Example](#example)

```
name = "Sarah"
day_of_week = "Tuesday"
print("Hello {name}! It is {day_of_week} today!")
```

Use instead:

```
name = "Sarah"
day_of_week = "Tuesday"
print(f"Hello {name}! It is {day_of_week} today!")
```

## [Fix safety](#fix-safety)

This fix will always change the behavior of the program and, despite the precautions detailed
above, this may be undesired. As such the fix is always marked as unsafe.