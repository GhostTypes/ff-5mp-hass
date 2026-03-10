# [repeated-global (FURB154)](#repeated-global-furb154)

Preview (since [v0.4.9](https://github.com/astral-sh/ruff/releases/tag/v0.4.9)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27repeated-global%27%20OR%20FURB154)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Frepeated_global.rs#L39)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for consecutive `global` (or `nonlocal`) statements.

## [Why is this bad?](#why-is-this-bad)

The `global` and `nonlocal` keywords accepts multiple comma-separated names.
Instead of using multiple `global` (or `nonlocal`) statements for separate
variables, you can use a single statement to declare multiple variables at
once.

## [Example](#example)

```
def func():
    global x
    global y

    print(x, y)
```

Use instead:

```
def func():
    global x, y

    print(x, y)
```

## [References](#references)

* [Python documentation: the `global` statement](https://docs.python.org/3/reference/simple_stmts.html#the-global-statement)
* [Python documentation: the `nonlocal` statement](https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement)