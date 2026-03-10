# [line-contains-todo (FIX002)](#line-contains-todo-fix002)

Added in [v0.0.272](https://github.com/astral-sh/ruff/releases/tag/v0.0.272) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27line-contains-todo%27%20OR%20FIX002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_fixme%2Frules%2Ftodos.rs#L25)

Derived from the **[flake8-fixme](../#flake8-fixme-fix)** linter.

## [What it does](#what-it-does)

Checks for "TODO" comments.

## [Why is this bad?](#why-is-this-bad)

"TODO" comments are used to describe an issue that should be resolved
(usually, a missing feature, optimization, or refactoring opportunity).

Consider resolving the issue before deploying the code.

Note that if you use "TODO" comments as a form of documentation (e.g.,
to [provide context for future work](https://gist.github.com/dmnd/ed5d8ef8de2e4cfea174bd5dafcda382)),
this rule may not be appropriate for your project.

## [Example](#example)

```
def greet(name):
    return f"Hello, {name}!"  # TODO: Add support for custom greetings.
```