# [raise-vanilla-class (TRY002)](#raise-vanilla-class-try002)

Added in [v0.0.236](https://github.com/astral-sh/ruff/releases/tag/v0.0.236) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27raise-vanilla-class%27%20OR%20TRY002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Ftryceratops%2Frules%2Fraise_vanilla_class.rs#L55)

Derived from the **[tryceratops](../#tryceratops-try)** linter.

## [What it does](#what-it-does)

Checks for code that raises `Exception` or `BaseException` directly.

## [Why is this bad?](#why-is-this-bad)

Handling such exceptions requires the use of `except Exception` or
`except BaseException`. These will capture almost *any* raised exception,
including failed assertions, division by zero, and more.

Prefer to raise your own exception, or a more specific built-in
exception, so that you can avoid over-capturing exceptions that you
don't intend to handle.

## [Example](#example)

```
def main_function():
    if not cond:
        raise Exception()


def consumer_func():
    try:
        do_step()
        prepare()
        main_function()
    except Exception:
        logger.error("Oops")
```

Use instead:

```
def main_function():
    if not cond:
        raise CustomException()


def consumer_func():
    try:
        do_step()
        prepare()
        main_function()
    except CustomException:
        logger.error("Main function failed")
    except Exception:
        logger.error("Oops")
```