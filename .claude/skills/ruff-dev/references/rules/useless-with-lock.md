# [useless-with-lock (PLW2101)](#useless-with-lock-plw2101)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27useless-with-lock%27%20OR%20PLW2101)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fuseless_with_lock.rs#L50)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for lock objects that are created and immediately discarded in
`with` statements.

## [Why is this bad?](#why-is-this-bad)

Creating a lock (via `threading.Lock` or similar) in a `with` statement
has no effect, as locks are only relevant when shared between threads.

Instead, assign the lock to a variable outside the `with` statement,
and share that variable between threads.

## [Example](#example)

```
import threading

counter = 0


def increment():
    global counter

    with threading.Lock():
        counter += 1
```

Use instead:

```
import threading

counter = 0
lock = threading.Lock()


def increment():
    global counter

    with lock:
        counter += 1
```

## [References](#references)

* [Python documentation: `Lock Objects`](https://docs.python.org/3/library/threading.html#lock-objects)