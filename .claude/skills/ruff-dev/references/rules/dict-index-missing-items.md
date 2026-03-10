# [dict-index-missing-items (PLC0206)](#dict-index-missing-items-plc0206)

Added in [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27dict-index-missing-items%27%20OR%20PLC0206)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fdict_index_missing_items.rs#L48)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for dictionary iterations that extract the dictionary value
via explicit indexing, instead of using `.items()`.

## [Why is this bad?](#why-is-this-bad)

Iterating over a dictionary with `.items()` is semantically clearer
and more efficient than extracting the value with the key.

## [Example](#example)

```
ORCHESTRA = {
    "violin": "strings",
    "oboe": "woodwind",
    "tuba": "brass",
    "gong": "percussion",
}

for instrument in ORCHESTRA:
    print(f"{instrument}: {ORCHESTRA[instrument]}")
```

Use instead:

```
ORCHESTRA = {
    "violin": "strings",
    "oboe": "woodwind",
    "tuba": "brass",
    "gong": "percussion",
}

for instrument, section in ORCHESTRA.items():
    print(f"{instrument}: {section}")
```