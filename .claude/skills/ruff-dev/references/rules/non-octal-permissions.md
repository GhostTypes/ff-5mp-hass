# [non-octal-permissions (RUF064)](#non-octal-permissions-ruf064)

Preview (since [0.12.1](https://github.com/astral-sh/ruff/releases/tag/0.12.1)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27non-octal-permissions%27%20OR%20RUF064)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fnon_octal_permissions.rs#L74)

Fix is sometimes available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for standard library functions which take a numeric `mode` argument
where a non-octal integer literal is passed.

## [Why is this bad?](#why-is-this-bad)

Numeric modes are made up of one to four octal digits. Converting a non-octal
integer to octal may not be the mode the author intended.

## [Example](#example)

```
os.chmod("foo", 644)
```

Use instead:

```
os.chmod("foo", 0o644)
```

## [Fix safety](#fix-safety)

There are two categories of fix, the first of which is where it looks like
the author intended to use an octal literal but the `0o` prefix is missing:

```
os.chmod("foo", 400)
os.chmod("foo", 644)
```

This class of fix changes runtime behaviour. In the first case, `400`
corresponds to `0o620` (`u=rw,g=w,o=`). As this mode is not deemed likely,
it is changed to `0o400` (`u=r,go=`). Similarly, `644` corresponds to
`0o1204` (`u=ws,g=,o=r`) and is changed to `0o644` (`u=rw,go=r`).

The second category is decimal literals which are recognised as likely valid
but in decimal form:

```
os.chmod("foo", 256)
os.chmod("foo", 493)
```

`256` corresponds to `0o400` (`u=r,go=`) and `493` corresponds to `0o755`
(`u=rwx,go=rx`). Both of these fixes keep runtime behavior unchanged. If the
original code really intended to use `0o256` (`u=w,g=rx,o=rw`) instead of
`256`, this fix should not be accepted.

As a special case, zero is allowed to omit the `0o` prefix unless it has
multiple digits:

```
os.chmod("foo", 0)  # Ok
os.chmod("foo", 0o000)  # Ok
os.chmod("foo", 000)  # Lint emitted and fix suggested
```

Ruff will suggest a safe fix for multi-digit zeros to add the `0o` prefix.

## [Fix availability](#fix-availability)

A fix is only available if the integer literal matches a set of common modes.