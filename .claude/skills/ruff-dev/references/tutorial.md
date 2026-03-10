# [Tutorial](#tutorial)

This tutorial will walk you through the process of integrating Ruff's linter and formatter into
your project. For a more detailed overview, see [*Configuring Ruff*](../configuration/).

## [Getting Started](#getting-started)

To start, we'll initialize a project using [uv](https://docs.astral.sh/uv/):

```
$ uv init --lib numbers
```

This command creates a Python project with the following structure:

```
numbers
  ├── README.md
  ├── pyproject.toml
  └── src
      └── numbers
          ├── __init__.py
          └── py.typed
```

We'll then clear out the auto-generated content in `src/numbers/__init__.py`
and create `src/numbers/calculate.py` with the following code:

```
from typing import Iterable

import os


def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(
        num for num in numbers
        if num % 2 == 0
    )
```

Next, we'll add Ruff to our project:

```
$ uv add --dev ruff
```

We can then run the Ruff linter over our project via `uv run ruff check`:

```
$ uv run ruff check
src/numbers/calculate.py:3:8: F401 [*] `os` imported but unused
Found 1 error.
[*] 1 fixable with the `--fix` option.
```

Note

As an alternative to `uv run`, you can also run Ruff by activating the project's virtual
environment (`source .venv/bin/active` on Linux and macOS, or `.venv\Scripts\activate` on
Windows) and running `ruff check` directly.

Ruff identified an unused import, which is a common error in Python code. Ruff considers this a
"fixable" error, so we can resolve the issue automatically by running `ruff check --fix`:

```
$ uv run ruff check --fix
Found 1 error (1 fixed, 0 remaining).
```

Running `git diff` shows the following:

```
--- a/src/numbers/calculate.py
+++ b/src/numbers/calculate.py
@@ -1,7 +1,5 @@
 from typing import Iterable

-import os
-

def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(
        num for num in numbers
        if num % 2 == 0
    )
```

Note Ruff runs in the current directory by default, but you can pass specific paths to check:

```
$ uv run ruff check src/numbers/calculate.py
```

Now that our project is passing `ruff check`, we can run the Ruff formatter via `ruff format`:

```
$ uv run ruff format
1 file reformatted
```

Running `git diff` shows that the `sum` call was reformatted to fit within the default 88-character
line length limit:

```
--- a/src/numbers/calculate.py
+++ b/src/numbers/calculate.py
@@ -3,7 +3,4 @@ from typing import Iterable

 def sum_even_numbers(numbers: Iterable[int]) -> int:
     """Given an iterable of integers, return the sum of all even numbers in the iterable."""
-    return sum(
-        num for num in numbers
-        if num % 2 == 0
-    )
+    return sum(num for num in numbers if num % 2 == 0)
```

Thus far, we've been using Ruff's default configuration. Let's take a look at how we can customize
Ruff's behavior.

## [Configuration](#configuration)

To determine the appropriate settings for each Python file, Ruff looks for the first
`pyproject.toml`, `ruff.toml`, or `.ruff.toml` file in the file's directory or any parent directory.

To configure Ruff, we'll add the following to the configuration file in our project's root directory:

pyproject.tomlruff.toml

```
[tool.ruff]
# Set the maximum line length to 79.
line-length = 79

[tool.ruff.lint]
# Add the `line-too-long` rule to the enforced rule set. By default, Ruff omits rules that
# overlap with the use of a formatter, like Black, but we can override this behavior by
# explicitly adding the rule.
extend-select = ["E501"]
```

```
# Set the maximum line length to 79.
line-length = 79

[lint]
# Add the `line-too-long` rule to the enforced rule set. By default, Ruff omits rules that
# overlap with the use of a formatter, like Black, but we can override this behavior by
# explicitly adding the rule.
extend-select = ["E501"]
```

Running Ruff again, we see that it now enforces a maximum line width, with a limit of 79:

```
$ uv run ruff check
src/numbers/calculate.py:5:80: E501 Line too long (90 > 79)
Found 1 error.
```

For a full enumeration of the supported settings, see [*Settings*](../settings/). For our project
specifically, we'll want to make note of the minimum supported Python version:

pyproject.tomlruff.toml

```
[project]
# Support Python 3.10+.
requires-python = ">=3.10"

[tool.ruff]
# Set the maximum line length to 79.
line-length = 79

[tool.ruff.lint]
# Add the `line-too-long` rule to the enforced rule set.
extend-select = ["E501"]
```

```
# Support Python 3.10+.
target-version = "py310"
# Set the maximum line length to 79.
line-length = 79

[lint]
# Add the `line-too-long` rule to the enforced rule set.
extend-select = ["E501"]
```

### [Rule Selection](#rule-selection)

Ruff supports [over 800 lint rules](../rules/) split across over 50 built-in plugins, but
determining the right set of rules will depend on your project's needs: some rules may be too
strict, some are framework-specific, and so on.

By default, Ruff enables Flake8's `F` rules, along with a subset of the `E` rules, omitting any
stylistic rules that overlap with the use of a formatter, like `ruff format` or
[Black](https://github.com/psf/black).

If you're introducing a linter for the first time, **the default rule set is a great place to
start**: it's narrow and focused while catching a wide variety of common errors (like unused
imports) with zero configuration.

If you're migrating to Ruff from another linter, you can enable rules that are equivalent to
those enforced in your previous configuration. For example, if we want to enforce the pyupgrade
rules, we can set our configuration file to the following:

pyproject.tomlruff.toml

```
[project]
requires-python = ">=3.10"

[tool.ruff.lint]
extend-select = [
  "UP",  # pyupgrade
]
```

```
target-version = "py310"

[lint]
extend-select = [
  "UP",  # pyupgrade
]
```

If we run Ruff again, we'll see that it now enforces the pyupgrade rules. In particular, Ruff flags
the use of the deprecated `typing.Iterable` instead of `collections.abc.Iterable`:

```
$ uv run ruff check
src/numbers/calculate.py:1:1: UP035 [*] Import from `collections.abc` instead: `Iterable`
Found 1 error.
[*] 1 fixable with the `--fix` option.
```

Over time, we may choose to enforce additional rules. For example, we may want to enforce that
all functions have docstrings:

pyproject.tomlruff.toml

```
[project]
requires-python = ">=3.10"

[tool.ruff.lint]
extend-select = [
  "UP",  # pyupgrade
  "D",   # pydocstyle
]

[tool.ruff.lint.pydocstyle]
convention = "google"
```

```
target-version = "py310"

[lint]
extend-select = [
  "UP",  # pyupgrade
  "D",   # pydocstyle
]

[lint.pydocstyle]
convention = "google"
```

If we run Ruff again, we'll see that it now enforces the pydocstyle rules:

```
$ uv run ruff check
src/numbers/__init__.py:1:1: D104 Missing docstring in public package
src/numbers/calculate.py:1:1: UP035 [*] Import from `collections.abc` instead: `Iterable`
  |
1 | from typing import Iterable
  | ^^^^^^^^^^^^^^^^^^^^^^^^^^^ UP035
  |
  = help: Import from `collections.abc`

src/numbers/calculate.py:1:1: D100 Missing docstring in public module
Found 3 errors.
[*] 1 fixable with the `--fix` option.
```

### [Ignoring Errors](#ignoring-errors)

Any lint rule can be ignored by adding a `# noqa` comment to the line in question. For example,
let's ignore the `UP035` rule for the `Iterable` import:

```
from typing import Iterable  # noqa: UP035


def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(num for num in numbers if num % 2 == 0)
```

Running `ruff check` again, we'll see that it no longer flags the `Iterable` import:

```
$ uv run ruff check
src/numbers/__init__.py:1:1: D104 Missing docstring in public package
src/numbers/calculate.py:1:1: D100 Missing docstring in public module
Found 2 errors.
```

If we want to ignore a rule for an entire file, we can add the line `# ruff: noqa: {code}` anywhere
in the file, preferably towards the top, like so:

```
# ruff: noqa: UP035
from typing import Iterable


def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(num for num in numbers if num % 2 == 0)
```

For more in-depth instructions on ignoring errors, please see [*Error suppression*](../linter/#error-suppression).

### [Adding Rules](#adding-rules)

When enabling a new rule on an existing codebase, you may want to ignore all *existing*
violations of that rule and instead focus on enforcing it going forward.

Ruff enables this workflow via the `--add-noqa` flag, which will add a `# noqa` directive to each
line based on its existing violations. We can combine `--add-noqa` with the `--select` command-line
flag to add `# noqa` directives to all existing `UP035` violations:

```
$ uv run ruff check --select UP035 --add-noqa .
Added 1 noqa directive.
```

Running `git diff` shows the following:

```
diff --git a/numbers/src/numbers/calculate.py b/numbers/src/numbers/calculate.py
index 71fca60c8d..e92d839f1b 100644
--- a/numbers/src/numbers/calculate.py
+++ b/numbers/src/numbers/calculate.py
@@ -1,4 +1,4 @@
-from typing import Iterable
+from typing import Iterable  # noqa: UP035
```

## [Integrations](#integrations)

This tutorial has focused on Ruff's command-line interface, but Ruff can also be used as a
[pre-commit](https://pre-commit.com) hook via [`ruff-pre-commit`](https://github.com/astral-sh/ruff-pre-commit):

```
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.14.10
  hooks:
    # Run the linter.
    - id: ruff-check
    # Run the formatter.
    - id: ruff-format
```

Ruff can also be integrated into your editor of choice. Refer to the [Editors](../editors/)
section for more information.

For other integrations, see the [Integrations](../integrations/) section.