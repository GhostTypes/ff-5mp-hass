# [invalid-formatter-suppression-comment (RUF028)](#invalid-formatter-suppression-comment-ruf028)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-formatter-suppression-comment%27%20OR%20RUF028)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Finvalid_formatter_suppression_comment.rs#L57)

Fix is always available.

## [What it does](#what-it-does)

Checks for formatter suppression comments that are ineffective or incompatible
with Ruff's formatter.

## [Why is this bad?](#why-is-this-bad)

Suppression comments that do not actually prevent formatting could cause unintended changes
when the formatter is run.

## [Example](#example)

In the following example, all suppression comments would cause
a rule violation.

```
def decorator():
    pass


@decorator
# fmt: off
def example():
    if True:
        # fmt: skip
        expression = [
            # fmt: off
            1,
            2,
        ]
        # yapf: disable
    # fmt: on
    # yapf: enable
```

## [Fix safety](#fix-safety)

This fix is always marked as unsafe because it deletes the invalid suppression comment,
rather than trying to move it to a valid position, which the user more likely intended.