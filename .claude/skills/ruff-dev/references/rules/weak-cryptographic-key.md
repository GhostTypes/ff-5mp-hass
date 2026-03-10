# [weak-cryptographic-key (S505)](#weak-cryptographic-key-s505)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27weak-cryptographic-key%27%20OR%20S505)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fweak_cryptographic_key.rs#L35)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of cryptographic keys with vulnerable key sizes.

## [Why is this bad?](#why-is-this-bad)

Small keys are easily breakable. For DSA and RSA, keys should be at least
2048 bits long. For EC, keys should be at least 224 bits long.

## [Example](#example)

```
from cryptography.hazmat.primitives.asymmetric import dsa, ec

dsa.generate_private_key(key_size=512)
ec.generate_private_key(curve=ec.SECT163K1())
```

Use instead:

```
from cryptography.hazmat.primitives.asymmetric import dsa, ec

dsa.generate_private_key(key_size=4096)
ec.generate_private_key(curve=ec.SECP384R1())
```

## [References](#references)

* [CSRC: Transitioning the Use of Cryptographic Algorithms and Key Lengths](https://csrc.nist.gov/pubs/sp/800/131/a/r2/final)