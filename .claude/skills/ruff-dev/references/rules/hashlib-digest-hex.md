# [hashlib-digest-hex (FURB181)](#hashlib-digest-hex-furb181)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27hashlib-digest-hex%27%20OR%20FURB181)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fhashlib_digest_hex.rs#L33)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for the use of `.digest().hex()` on a hashlib hash, like `sha512`.

## [Why is this bad?](#why-is-this-bad)

When generating a hex digest from a hash, it's preferable to use the
`.hexdigest()` method, rather than calling `.digest()` and then `.hex()`,
as the former is more concise and readable.

## [Example](#example)

```
from hashlib import sha512

hashed = sha512(b"some data").digest().hex()
```

Use instead:

```
from hashlib import sha512

hashed = sha512(b"some data").hexdigest()
```

## [References](#references)

* [Python documentation: `hashlib`](https://docs.python.org/3/library/hashlib.html)