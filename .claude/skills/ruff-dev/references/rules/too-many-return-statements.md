# [too-many-return-statements (PLR0911)](#too-many-return-statements-plr0911)

Added in [v0.0.242](https://github.com/astral-sh/ruff/releases/tag/v0.0.242) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27too-many-return-statements%27%20OR%20PLR0911)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Ftoo_many_return_statements.rs#L54)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for functions or methods with too many return statements.

By default, this rule allows up to six return statements, as configured by
the [`lint.pylint.max-returns`](../../settings/#lint_pylint_max-returns) option.

## [Why is this bad?](#why-is-this-bad)

Functions or methods with many return statements are harder to understand
and maintain, and often indicative of complex logic.

## [Example](#example)

```
def capital(country: str) -> str | None:
    if country == "England":
        return "London"
    elif country == "France":
        return "Paris"
    elif country == "Poland":
        return "Warsaw"
    elif country == "Romania":
        return "Bucharest"
    elif country == "Spain":
        return "Madrid"
    elif country == "Thailand":
        return "Bangkok"
    else:
        return None
```

Use instead:

```
def capital(country: str) -> str | None:
    capitals = {
        "England": "London",
        "France": "Paris",
        "Poland": "Warsaw",
        "Romania": "Bucharest",
        "Spain": "Madrid",
        "Thailand": "Bangkok",
    }
    return capitals.get(country)
```

## [Options](#options)

* [`lint.pylint.max-returns`](../../settings/#lint_pylint_max-returns)