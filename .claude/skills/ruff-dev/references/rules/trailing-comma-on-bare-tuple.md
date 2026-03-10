# [trailing-comma-on-bare-tuple (COM818)](#trailing-comma-on-bare-tuple-com818)

Added in [v0.0.223](https://github.com/astral-sh/ruff/releases/tag/v0.0.223) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27trailing-comma-on-bare-tuple%27%20OR%20COM818)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_commas%2Frules%2Ftrailing_commas.rs#L201)

Derived from the **[flake8-commas](../#flake8-commas-com)** linter.

## [What it does](#what-it-does)

Checks for the presence of trailing commas on bare (i.e., unparenthesized)
tuples.

## [Why is this bad?](#why-is-this-bad)

The presence of a misplaced comma will cause Python to interpret the value
as a tuple, which can lead to unexpected behaviour.

## [Example](#example)

```
import json


foo = json.dumps({"bar": 1}),
```

Use instead:

```
import json


foo = json.dumps({"bar": 1})
```

In the event that a tuple is intended, then use instead:

```
import json


foo = (json.dumps({"bar": 1}),)
```