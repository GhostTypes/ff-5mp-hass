# [too-many-statements (PLR0915)](#too-many-statements-plr0915)

Added in [v0.0.240](https://github.com/astral-sh/ruff/releases/tag/v0.0.240) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27too-many-statements%27%20OR%20PLR0915)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Ftoo_many_statements.rs#L50)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for functions or methods with too many statements.

By default, this rule allows up to 50 statements, as configured by the
[`lint.pylint.max-statements`](../../settings/#lint_pylint_max-statements) option.

## [Why is this bad?](#why-is-this-bad)

Functions or methods with many statements are harder to understand
and maintain.

Instead, consider refactoring the function or method into smaller
functions or methods, or identifying generalizable patterns and
replacing them with generic logic or abstractions.

## [Example](#example)

```
def is_even(number: int) -> bool:
    if number == 0:
        return True
    elif number == 1:
        return False
    elif number == 2:
        return True
    elif number == 3:
        return False
    elif number == 4:
        return True
    elif number == 5:
        return False
    else:
        ...
```

Use instead:

```
def is_even(number: int) -> bool:
    return number % 2 == 0
```

## [Options](#options)

* [`lint.pylint.max-statements`](../../settings/#lint_pylint_max-statements)