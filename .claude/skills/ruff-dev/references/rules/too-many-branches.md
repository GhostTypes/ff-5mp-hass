# [too-many-branches (PLR0912)](#too-many-branches-plr0912)

Added in [v0.0.242](https://github.com/astral-sh/ruff/releases/tag/v0.0.242) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27too-many-branches%27%20OR%20PLR0912)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Ftoo_many_branches.rs#L147)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for functions or methods with too many branches, including (nested)
`if`, `elif`, and `else` branches, `for` loops, `try`-`except` clauses, and
`match` and `case` statements.

By default, this rule allows up to 12 branches. This can be configured
using the [`lint.pylint.max-branches`](../../settings/#lint_pylint_max-branches) option.

## [Why is this bad?](#why-is-this-bad)

Functions or methods with many branches are harder to understand
and maintain than functions or methods with fewer branches.

## [Example](#example)

Given:

```
def capital(country):
    if country == "Australia":
        return "Canberra"
    elif country == "Brazil":
        return "Brasilia"
    elif country == "Canada":
        return "Ottawa"
    elif country == "England":
        return "London"
    elif country == "France":
        return "Paris"
    elif country == "Germany":
        return "Berlin"
    elif country == "Poland":
        return "Warsaw"
    elif country == "Romania":
        return "Bucharest"
    elif country == "Spain":
        return "Madrid"
    elif country == "Thailand":
        return "Bangkok"
    elif country == "Turkey":
        return "Ankara"
    elif country == "United States":
        return "Washington"
    else:
        return "Unknown"  # 13th branch
```

Use instead:

```
def capital(country):
    capitals = {
        "Australia": "Canberra",
        "Brazil": "Brasilia",
        "Canada": "Ottawa",
        "England": "London",
        "France": "Paris",
        "Germany": "Berlin",
        "Poland": "Warsaw",
        "Romania": "Bucharest",
        "Spain": "Madrid",
        "Thailand": "Bangkok",
        "Turkey": "Ankara",
        "United States": "Washington",
    }
    city = capitals.get(country, "Unknown")
    return city
```

Given:

```
def grades_to_average_number(grades):
    numbers = []
    for grade in grades:  # 1st branch
        if len(grade) not in {1, 2}:
            raise ValueError(f"Invalid grade: {grade}")

        if len(grade) == 2 and grade[1] not in {"+", "-"}:
            raise ValueError(f"Invalid grade: {grade}")

        letter = grade[0]

        if letter in {"F", "E"}:
            number = 0.0
        elif letter == "D":
            number = 1.0
        elif letter == "C":
            number = 2.0
        elif letter == "B":
            number = 3.0
        elif letter == "A":
            number = 4.0
        else:
            raise ValueError(f"Invalid grade: {grade}")

        modifier = 0.0
        if letter != "F" and grade[-1] == "+":
            modifier = 0.3
        elif letter != "F" and grade[-1] == "-":
            modifier = -0.3

        numbers.append(max(0.0, min(number + modifier, 4.0)))

    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:  # 13th branch
        return 0
```

Use instead:

```
def grades_to_average_number(grades):
    grade_values = {"F": 0.0, "E": 0.0, "D": 1.0, "C": 2.0, "B": 3.0, "A": 4.0}
    modifier_values = {"+": 0.3, "-": -0.3}

    numbers = []
    for grade in grades:
        if len(grade) not in {1, 2}:
            raise ValueError(f"Invalid grade: {grade}")

        letter = grade[0]
        if letter not in grade_values:
            raise ValueError(f"Invalid grade: {grade}")
        number = grade_values[letter]

        if len(grade) == 2 and grade[1] not in modifier_values:
            raise ValueError(f"Invalid grade: {grade}")
        modifier = modifier_values.get(grade[-1], 0.0)

        if letter == "F":
            numbers.append(0.0)
        else:
            numbers.append(max(0.0, min(number + modifier, 4.0)))

    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0
```

## [Options](#options)

* [`lint.pylint.max-branches`](../../settings/#lint_pylint_max-branches)