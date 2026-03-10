# [import-shadowed-by-loop-var (F402)](#import-shadowed-by-loop-var-f402)

Added in [v0.0.44](https://github.com/astral-sh/ruff/releases/tag/v0.0.44) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27import-shadowed-by-loop-var%27%20OR%20F402)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fimports.rs#L36)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for import bindings that are shadowed by loop variables.

## [Why is this bad?](#why-is-this-bad)

Shadowing an import with loop variables makes the code harder to read and
reason about, as the identify of the imported binding is no longer clear.
It's also often indicative of a mistake, as it's unlikely that the loop
variable is intended to be used as the imported binding.

Consider using a different name for the loop variable.

## [Example](#example)

```
from os import path

for path in files:
    print(path)
```

Use instead:

```
from os import path


for filename in files:
    print(filename)
```