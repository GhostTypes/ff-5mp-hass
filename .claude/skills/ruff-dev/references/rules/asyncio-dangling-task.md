# [asyncio-dangling-task (RUF006)](#asyncio-dangling-task-ruf006)

Added in [v0.0.247](https://github.com/astral-sh/ruff/releases/tag/v0.0.247) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27asyncio-dangling-task%27%20OR%20RUF006)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fasyncio_dangling_task.rs#L55)

## [What it does](#what-it-does)

Checks for `asyncio.create_task` and `asyncio.ensure_future` calls
that do not store a reference to the returned result.

## [Why is this bad?](#why-is-this-bad)

Per the `asyncio` documentation, the event loop only retains a weak
reference to tasks. If the task returned by `asyncio.create_task` and
`asyncio.ensure_future` is not stored in a variable, or a collection,
or otherwise referenced, it may be garbage collected at any time. This
can lead to unexpected and inconsistent behavior, as your tasks may or
may not run to completion.

## [Example](#example)

```
import asyncio

for i in range(10):
    # This creates a weak reference to the task, which may be garbage
    # collected at any time.
    asyncio.create_task(some_coro(param=i))
```

Use instead:

```
import asyncio

background_tasks = set()

for i in range(10):
    task = asyncio.create_task(some_coro(param=i))

    # Add task to the set. This creates a strong reference.
    background_tasks.add(task)

    # To prevent keeping references to finished tasks forever,
    # make each task remove its own reference from the set after
    # completion:
    task.add_done_callback(background_tasks.discard)
```

## [References](#references)

* [*The Heisenbug lurking in your async code*](https://textual.textualize.io/blog/2023/02/11/the-heisenbug-lurking-in-your-async-code/)
* [The Python Standard Library](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task)