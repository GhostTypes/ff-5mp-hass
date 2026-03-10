# [bare-except (E722)](#bare-except-e722)

Added in [v0.0.36](https://github.com/astral-sh/ruff/releases/tag/v0.0.36) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27bare-except%27%20OR%20E722)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fbare_except.rs#L47)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

## [What it does](#what-it-does)

Checks for bare `except` catches in `try`-`except` statements.

## [Why is this bad?](#why-is-this-bad)

A bare `except` catches `BaseException` which includes
`KeyboardInterrupt`, `SystemExit`, `Exception`, and others. Catching
`BaseException` can make it hard to interrupt the program (e.g., with
Ctrl-C) and can disguise other problems.

## [Example](#example)

```
try:
    raise KeyboardInterrupt("You probably don't mean to break CTRL-C.")
except:
    print("But a bare `except` will ignore keyboard interrupts.")
```

Use instead:

```
try:
    do_something_that_might_break()
except MoreSpecificException as e:
    handle_error(e)
```

If you actually need to catch an unknown error, use `Exception` which will
catch regular program errors but not important system exceptions.

```
def run_a_function(some_other_fn):
    try:
        some_other_fn()
    except Exception as e:
        print(f"How exceptional! {e}")
```

## [References](#references)

* [Python documentation: Exception hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
* [Google Python Style Guide: "Exceptions"](https://google.github.io/styleguide/pyguide.html#24-exceptions)