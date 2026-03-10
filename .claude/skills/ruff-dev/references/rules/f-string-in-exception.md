# [f-string-in-exception (EM102)](#f-string-in-exception-em102)

Added in [v0.0.183](https://github.com/astral-sh/ruff/releases/tag/v0.0.183) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27f-string-in-exception%27%20OR%20EM102)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_errmsg%2Frules%2Fstring_in_exception.rs#L106)

Derived from the **[flake8-errmsg](../#flake8-errmsg-em)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for the use of f-strings in exception constructors.

## [Why is this bad?](#why-is-this-bad)

Python includes the `raise` in the default traceback (and formatters
like Rich and IPython do too).

By using an f-string, the error message will be duplicated in the
traceback, which can make the traceback less readable.

## [Example](#example)

Given:

```
sub = "Some value"
raise RuntimeError(f"{sub!r} is incorrect")
```

Python will produce a traceback like:

```
Traceback (most recent call last):
  File "tmp.py", line 2, in <module>
    raise RuntimeError(f"{sub!r} is incorrect")
RuntimeError: 'Some value' is incorrect
```

Instead, assign the string to a variable:

```
sub = "Some value"
msg = f"{sub!r} is incorrect"
raise RuntimeError(msg)
```

Which will produce a traceback like:

```
Traceback (most recent call last):
  File "tmp.py", line 3, in <module>
    raise RuntimeError(msg)
RuntimeError: 'Some value' is incorrect
```