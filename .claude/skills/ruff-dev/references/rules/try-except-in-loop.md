# [try-except-in-loop (PERF203)](#try-except-in-loop-perf203)

Added in [v0.0.276](https://github.com/astral-sh/ruff/releases/tag/v0.0.276) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27try-except-in-loop%27%20OR%20PERF203)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fperflint%2Frules%2Ftry_except_in_loop.rs#L79)

Derived from the **[Perflint](../#perflint-perf)** linter.

## [What it does](#what-it-does)

Checks for uses of except handling via `try`-`except` within `for` and
`while` loops.

## [Why is this bad?](#why-is-this-bad)

Exception handling via `try`-`except` blocks incurs some performance
overhead, regardless of whether an exception is raised.

To optimize your code, two techniques are possible:

1. Refactor your code to put the entire loop into the `try`-`except` block,
   rather than wrapping each iteration in a separate `try`-`except` block.
2. Use "Look Before You Leap" idioms that attempt to avoid exceptions
   being raised in the first place, avoiding the need to use `try`-`except`
   blocks in the first place.

This rule is only enforced for Python versions prior to 3.11, which
introduced "zero-cost" exception handling. However, note that even on
Python 3.11 and newer, refactoring your code to avoid exception handling in
tight loops can provide a significant speedup in some cases, as zero-cost
exception handling is only zero-cost in the "happy path" where no exception
is raised in the `try`-`except` block.

As with all `perflint` rules, this is only intended as a
micro-optimization. In many cases, it will have a negligible impact on
performance.

## [Example](#example)

```
string_numbers: list[str] = ["1", "2", "three", "4", "5"]

# `try`/`except` that could be moved out of the loop:
int_numbers: list[int] = []
for num in string_numbers:
    try:
        int_numbers.append(int(num))
    except ValueError as e:
        print(f"Couldn't convert to integer: {e}")
        break

# `try`/`except` used when "look before you leap" idioms could be used:
number_names: dict[int, str] = {1: "one", 3: "three", 4: "four"}
for number in range(5):
    try:
        name = number_names[number]
    except KeyError:
        continue
    else:
        print(f"The name of {number} is {name}")
```

Use instead:

```
string_numbers: list[str] = ["1", "2", "three", "4", "5"]

int_numbers: list[int] = []
try:
    for num in string_numbers:
        int_numbers.append(int(num))
except ValueError as e:
    print(f"Couldn't convert to integer: {e}")

number_names: dict[int, str] = {1: "one", 3: "three", 4: "four"}
for number in range(5):
    name = number_names.get(number)
    if name is not None:
        print(f"The name of {number} is {name}")
```

## [Options](#options)

* [`target-version`](../../settings/#target-version)