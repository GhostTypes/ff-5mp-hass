# [Preview](#preview)

Ruff includes an opt-in preview mode to provide an opportunity for community feedback and increase confidence that
changes are a net-benefit before enabling them for everyone.

Preview mode enables a collection of unstable features such as new lint rules and fixes, formatter style changes, interface updates, and more. Warnings about deprecated features may turn into errors when using preview mode.

Enabling preview mode does not on its own enable all preview rules. See the [rules section](#using-rules-that-are-in-preview) for details on selecting preview rules.

## [Enabling preview mode](#enabling-preview-mode)

Preview mode can be enabled with the `--preview` flag on the CLI or by setting `preview = true` in your Ruff
configuration file.

Preview mode can be configured separately for linting and formatting. To enable preview lint rules without preview style formatting:

pyproject.tomlruff.tomlCLI

```
[tool.ruff.lint]
preview = true
```

```
[lint]
preview = true
```

```
ruff check --preview
```

To enable preview style formatting without enabling any preview lint rules:

pyproject.tomlruff.tomlCLI

```
[tool.ruff.format]
preview = true
```

```
[format]
preview = true
```

```
ruff format --preview
```

## [Using rules that are in preview](#using-rules-that-are-in-preview)

If a rule is marked as preview, it can only be selected if preview mode is enabled. For example, consider a
hypothetical rule, `HYP001`. If `HYP001` were in preview, it would *not* be enabled by adding it to the selected rule set.

pyproject.tomlruff.tomlCLI

```
[tool.ruff.lint]
extend-select = ["HYP001"]
```

```
[lint]
extend-select = ["HYP001"]
```

```
ruff check --extend-select HYP001
```

It also would *not* be enabled by selecting the `HYP` category, like so:

pyproject.tomlruff.tomlCLI

```
[tool.ruff.lint]
extend-select = ["HYP"]
```

```
[lint]
extend-select = ["HYP"]
```

```
ruff check --extend-select HYP
```

Similarly, it would *not* be enabled via the `ALL` selector:

pyproject.tomlruff.tomlCLI

```
[tool.ruff.lint]
select = ["ALL"]
```

```
[lint]
select = ["ALL"]
```

```
ruff check --select ALL
```

However, it *would* be enabled in any of the above cases if you enabled preview mode:

pyproject.tomlruff.tomlCLI

```
[tool.ruff.lint]
extend-select = ["HYP"]
preview = true
```

```
[lint]
extend-select = ["HYP"]
preview = true
```

```
ruff check --extend-select HYP --preview
```

To see which rules are currently in preview, visit the [rules reference](../rules/).

## [Selecting single preview rules](#selecting-single-preview-rules)

When preview mode is enabled, selecting rule categories or prefixes will include all preview rules that match.
If you'd prefer to opt in to each preview rule individually, you can toggle the `explicit-preview-rules`
setting in your configuration file:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
preview = true
explicit-preview-rules = true
```

```
[lint]
preview = true
explicit-preview-rules = true
```

In our previous example, `--select` with `ALL` `HYP`, `HYP0`, or `HYP00` would not enable `HYP001`. Each preview
rule will need to be selected with its exact code: for example, `--select ALL,HYP001`.

If preview mode is not enabled, this setting has no effect.

## [Deprecated rules](#deprecated-rules)

When preview mode is enabled, deprecated rules will be disabled. If a deprecated rule is selected explicitly, an
error will be raised. Deprecated rules will not be included if selected via a rule category or prefix.