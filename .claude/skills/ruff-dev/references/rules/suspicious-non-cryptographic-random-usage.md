# [suspicious-non-cryptographic-random-usage (S311)](#suspicious-non-cryptographic-random-usage-s311)

Added in [v0.0.258](https://github.com/astral-sh/ruff/releases/tag/v0.0.258) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-non-cryptographic-random-usage%27%20OR%20S311)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_function_call.rs#L488)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of cryptographically weak pseudo-random number generators.

## [Why is this bad?](#why-is-this-bad)

Cryptographically weak pseudo-random number generators are insecure, as they
are easily predictable. This can allow an attacker to guess the generated
numbers and compromise the security of the system.

Instead, use a cryptographically secure pseudo-random number generator
(such as using the [`secrets` module](https://docs.python.org/3/library/secrets.html))
when generating random numbers for security purposes.

In [preview](https://docs.astral.sh/ruff/preview/), this rule will also flag references to these generators.

## [Example](#example)

```
import random

random.randrange(10)
```

Use instead:

```
import secrets

secrets.randbelow(10)
```

## [References](#references)

* [Python documentation: `random` — Generate pseudo-random numbers](https://docs.python.org/3/library/random.html)