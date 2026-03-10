# [return-in-generator (B901)](#return-in-generator-b901)

Preview (since [v0.4.8](https://github.com/astral-sh/ruff/releases/tag/v0.4.8)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27return-in-generator%27%20OR%20B901)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Freturn_in_generator.rs#L80)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for `return {value}` statements in functions that also contain `yield`
or `yield from` statements.

## [Why is this bad?](#why-is-this-bad)

Using `return {value}` in a generator function was syntactically invalid in
Python 2. In Python 3 `return {value}` *can* be used in a generator; however,
the combination of `yield` and `return` can lead to confusing behavior, as
the `return` statement will cause the generator to raise `StopIteration`
with the value provided, rather than returning the value to the caller.

For example, given:

```
from collections.abc import Iterable
from pathlib import Path


def get_file_paths(file_types: Iterable[str] | None = None) -> Iterable[Path]:
    dir_path = Path(".")
    if file_types is None:
        return dir_path.glob("*")

    for file_type in file_types:
        yield from dir_path.glob(f"*.{file_type}")
```

Readers might assume that `get_file_paths()` would return an iterable of
`Path` objects in the directory; in reality, though, `list(get_file_paths())`
evaluates to `[]`, since the `return` statement causes the generator to raise
`StopIteration` with the value `dir_path.glob("*")`:

```
>>> list(get_file_paths(file_types=["cfg", "toml"]))
[PosixPath('setup.cfg'), PosixPath('pyproject.toml')]
>>> list(get_file_paths())
[]
```

For intentional uses of `return` in a generator, consider suppressing this
diagnostic.

## [Example](#example)

```
from collections.abc import Iterable
from pathlib import Path


def get_file_paths(file_types: Iterable[str] | None = None) -> Iterable[Path]:
    dir_path = Path(".")
    if file_types is None:
        return dir_path.glob("*")

    for file_type in file_types:
        yield from dir_path.glob(f"*.{file_type}")
```

Use instead:

```
from collections.abc import Iterable
from pathlib import Path


def get_file_paths(file_types: Iterable[str] | None = None) -> Iterable[Path]:
    dir_path = Path(".")
    if file_types is None:
        yield from dir_path.glob("*")
    else:
        for file_type in file_types:
            yield from dir_path.glob(f"*.{file_type}")
```