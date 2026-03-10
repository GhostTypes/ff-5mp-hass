# [suspicious-insecure-cipher-mode-usage (S305)](#suspicious-insecure-cipher-mode-usage-s305)

Added in [v0.0.258](https://github.com/astral-sh/ruff/releases/tag/v0.0.258) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-insecure-cipher-mode-usage%27%20OR%20S305)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_function_call.rs#L247)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of weak or broken cryptographic cipher modes.

## [Why is this bad?](#why-is-this-bad)

Weak or broken cryptographic ciphers may be susceptible to attacks that
allow an attacker to decrypt ciphertext without knowing the key or
otherwise compromise the security of the cipher, such as forgeries.

Use strong, modern cryptographic ciphers instead of weak or broken ones.

In [preview](https://docs.astral.sh/ruff/preview/), this rule will also flag references to insecure cipher modes.

## [Example](#example)

```
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

algorithm = algorithms.ARC4(key)
cipher = Cipher(algorithm, mode=modes.ECB(iv))
encryptor = cipher.encryptor()
```

Use instead:

```
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

algorithm = algorithms.ARC4(key)
cipher = Cipher(algorithm, mode=modes.CTR(iv))
encryptor = cipher.encryptor()
```

## [References](#references)

* [Common Weakness Enumeration: CWE-327](https://cwe.mitre.org/data/definitions/327.html)