# [load-before-global-declaration (PLE0118)](#load-before-global-declaration-ple0118)

Added in [v0.0.174](https://github.com/astral-sh/ruff/releases/tag/v0.0.174) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27load-before-global-declaration%27%20OR%20PLE0118)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fload_before_global_declaration.rs#L39)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for uses of names that are declared as `global` prior to the
relevant `global` declaration.

## [Why is this bad?](#why-is-this-bad)

The `global` declaration applies to the entire scope. Using a name that's
declared as `global` in a given scope prior to the relevant `global`
declaration is a `SyntaxError`.

## [Example](#example)

```
counter = 1


def increment():
    print(f"Adding 1 to {counter}")
    global counter
    counter += 1
```

Use instead:

```
counter = 1


def increment():
    global counter
    print(f"Adding 1 to {counter}")
    counter += 1
```

## [References](#references)

* [Python documentation: The `global` statement](https://docs.python.org/3/reference/simple_stmts.html#the-global-statement)