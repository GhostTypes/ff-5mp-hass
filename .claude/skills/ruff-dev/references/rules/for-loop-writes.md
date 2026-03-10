# [for-loop-writes (FURB122)](#for-loop-writes-furb122)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27for-loop-writes%27%20OR%20FURB122)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Ffor_loop_writes.rs#L49)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for the use of `IOBase.write` in a for loop.

## [Why is this bad?](#why-is-this-bad)

When writing a batch of elements, it's more idiomatic to use a single method call to
`IOBase.writelines`, rather than write elements one by one.

## [Example](#example)

```
from pathlib import Path

with Path("file").open("w") as f:
    for line in lines:
        f.write(line)

with Path("file").open("wb") as f_b:
    for line_b in lines_b:
        f_b.write(line_b.encode())
```

Use instead:

```
from pathlib import Path

with Path("file").open("w") as f:
    f.writelines(lines)

with Path("file").open("wb") as f_b:
    f_b.writelines(line_b.encode() for line_b in lines_b)
```

## [Fix safety](#fix-safety)

This fix is marked as unsafe if it would cause comments to be deleted.

## [References](#references)

* [Python documentation: `io.IOBase.writelines`](https://docs.python.org/3/library/io.html#io.IOBase.writelines)