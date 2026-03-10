# [Settings](#settings)

## [Top-level](#top-level)

#### [`builtins`](#builtins)

A list of builtins to treat as defined references, in addition to the
system builtins.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
builtins = ["_"]
```

```
builtins = ["_"]
```

---

#### [`cache-dir`](#cache-dir)

A path to the cache directory.

By default, Ruff stores cache results in a `.ruff_cache` directory in
the current project root.

However, Ruff will also respect the `RUFF_CACHE_DIR` environment
variable, which takes precedence over that default.

This setting will override even the `RUFF_CACHE_DIR` environment
variable, if set.

**Default value**: `".ruff_cache"`

**Type**: `str`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
cache-dir = "~/.cache/ruff"
```

```
cache-dir = "~/.cache/ruff"
```

---

#### [`exclude`](#exclude)

A list of file patterns to exclude from formatting and linting.

Exclusions are based on globs, and can be either:

* Single-path patterns, like `.mypy_cache` (to exclude any directory
  named `.mypy_cache` in the tree), `foo.py` (to exclude any file named
  `foo.py`), or `foo_*.py` (to exclude any file matching `foo_*.py` ).
* Relative patterns, like `directory/foo.py` (to exclude that specific
  file) or `directory/*.py` (to exclude any Python files in
  `directory`). Note that these paths are relative to the project root
  (e.g., the directory containing your `pyproject.toml`).

For more information on the glob syntax, refer to the [`globset` documentation](https://docs.rs/globset/latest/globset/#syntax).

Note that you'll typically want to use
[`extend-exclude`](#extend-exclude) to modify the excluded paths.

**Default value**: `[".bzr", ".direnv", ".eggs", ".git", ".git-rewrite", ".hg", ".mypy_cache", ".nox", ".pants.d", ".pytype", ".ruff_cache", ".svn", ".tox", ".venv", "__pypackages__", "_build", "buck-out", "dist", "node_modules", "venv"]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
exclude = [".venv"]
```

```
exclude = [".venv"]
```

---

#### [`extend`](#extend)

A path to a local `pyproject.toml` or `ruff.toml` file to merge into this
configuration. User home directory and environment variables will be
expanded.

To resolve the current configuration file, Ruff will first load
this base configuration file, then merge in properties defined
in the current configuration file. Most settings follow simple override
behavior where the child value replaces the parent value. However,
rule selection (`lint.select` and `lint.ignore`) has special merging
behavior: if the child configuration specifies `lint.select`, it
establishes a new baseline rule set and the parent's `lint.ignore`
rules are discarded; if the child configuration omits `lint.select`,
the parent's rule selection is inherited and both parent and child
`lint.ignore` rules are accumulated together.

**Default value**: `null`

**Type**: `str`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
# Extend the `pyproject.toml` file in the parent directory.
extend = "../pyproject.toml"
# But use a different line length.
line-length = 100
```

```
# Extend the `pyproject.toml` file in the parent directory.
extend = "../pyproject.toml"
# But use a different line length.
line-length = 100
```

---

#### [`extend-exclude`](#extend-exclude)

A list of file patterns to omit from formatting and linting, in addition to those
specified by [`exclude`](#exclude).

Exclusions are based on globs, and can be either:

* Single-path patterns, like `.mypy_cache` (to exclude any directory
  named `.mypy_cache` in the tree), `foo.py` (to exclude any file named
  `foo.py`), or `foo_*.py` (to exclude any file matching `foo_*.py` ).
* Relative patterns, like `directory/foo.py` (to exclude that specific
  file) or `directory/*.py` (to exclude any Python files in
  `directory`). Note that these paths are relative to the project root
  (e.g., the directory containing your `pyproject.toml`).

For more information on the glob syntax, refer to the [`globset` documentation](https://docs.rs/globset/latest/globset/#syntax).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
# In addition to the standard set of exclusions, omit all tests, plus a specific file.
extend-exclude = ["tests", "src/bad.py"]
```

```
# In addition to the standard set of exclusions, omit all tests, plus a specific file.
extend-exclude = ["tests", "src/bad.py"]
```

---

#### [`extend-include`](#extend-include)

A list of file patterns to include when linting, in addition to those
specified by [`include`](#include).

Inclusion are based on globs, and should be single-path patterns, like
`*.pyw`, to include any file with the `.pyw` extension.

For more information on the glob syntax, refer to the [`globset` documentation](https://docs.rs/globset/latest/globset/#syntax).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
# In addition to the standard set of inclusions, include `.pyw` files.
extend-include = ["*.pyw"]
```

```
# In addition to the standard set of inclusions, include `.pyw` files.
extend-include = ["*.pyw"]
```

---

#### [`fix`](#fix)

Enable fix behavior by-default when running `ruff` (overridden
by the `--fix` and `--no-fix` command-line flags).
Only includes automatic fixes unless `--unsafe-fixes` is provided.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
fix = true
```

```
fix = true
```

---

#### [`fix-only`](#fix-only)

Like [`fix`](#fix), but disables reporting on leftover violation. Implies [`fix`](#fix).

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
fix-only = true
```

```
fix-only = true
```

---

#### [`force-exclude`](#force-exclude)

Whether to enforce [`exclude`](#exclude) and [`extend-exclude`](#extend-exclude) patterns,
even for paths that are passed to Ruff explicitly. Typically, Ruff will lint
any paths passed in directly, even if they would typically be
excluded. Setting `force-exclude = true` will cause Ruff to
respect these exclusions unequivocally.

This is useful for [`pre-commit`](https://pre-commit.com/), which explicitly passes all
changed files to the [`ruff-pre-commit`](https://github.com/astral-sh/ruff-pre-commit)
plugin, regardless of whether they're marked as excluded by Ruff's own
settings.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
force-exclude = true
```

```
force-exclude = true
```

---

#### [`include`](#include)

A list of file patterns to include when linting.

Inclusion are based on globs, and should be single-path patterns, like
`*.pyw`, to include any file with the `.pyw` extension. `pyproject.toml` is
included here not for configuration but because we lint whether e.g. the
`[project]` matches the schema.

Notebook files (`.ipynb` extension) are included by default on Ruff 0.6.0+.

For more information on the glob syntax, refer to the [`globset` documentation](https://docs.rs/globset/latest/globset/#syntax).

**Default value**: `["*.py", "*.pyi", "*.pyw", "*.ipynb", "**/pyproject.toml"]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
include = ["*.py"]
```

```
include = ["*.py"]
```

---

#### [`indent-width`](#indent-width)

The number of spaces per indentation level (tab).

Used by the formatter and when enforcing long-line violations (like `E501`) to determine the visual
width of a tab.

This option changes the number of spaces the formatter inserts when
using soft-tabs (`indent-style = space`).

PEP 8 recommends using 4 spaces per [indentation level](https://peps.python.org/pep-0008/#indentation).

**Default value**: `4`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
indent-width = 2
```

```
indent-width = 2
```

---

#### [`line-length`](#line-length)

The line length to use when enforcing long-lines violations (like `E501`)
and at which `isort` and the formatter prefers to wrap lines.

The length is determined by the number of characters per line, except for lines containing East Asian characters or emojis.
For these lines, the [unicode width](https://unicode.org/reports/tr11/) of each character is added up to determine the length.

The value must be greater than `0` and less than or equal to `320`.

Note: While the formatter will attempt to format lines such that they remain
within the `line-length`, it isn't a hard upper bound, and formatted lines may
exceed the `line-length`.

See [`pycodestyle.max-line-length`](#lint_pycodestyle_max-line-length) to configure different lengths for `E501` and the formatter.

**Default value**: `88`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
# Allow lines to be as long as 120.
line-length = 120
```

```
# Allow lines to be as long as 120.
line-length = 120
```

---

#### [`namespace-packages`](#namespace-packages)

Mark the specified directories as namespace packages. For the purpose of
module resolution, Ruff will treat those directories and all their subdirectories
as if they contained an `__init__.py` file.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
namespace-packages = ["airflow/providers"]
```

```
namespace-packages = ["airflow/providers"]
```

---

#### [`output-format`](#output-format)

The style in which violation messages should be formatted: `"full"` (default)
(shows source), `"concise"`, `"grouped"` (group messages by file), `"json"`
(machine-readable), `"junit"` (machine-readable XML), `"github"` (GitHub
Actions annotations), `"gitlab"` (GitLab CI code quality report),
`"pylint"` (Pylint text format) or `"azure"` (Azure Pipeline logging commands).

**Default value**: `"full"`

**Type**: `"full" | "concise" | "grouped" | "json" | "junit" | "github" | "gitlab" | "pylint" | "azure"`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
# Group violations by containing file.
output-format = "grouped"
```

```
# Group violations by containing file.
output-format = "grouped"
```

---

#### [`per-file-target-version`](#per-file-target-version)

A list of mappings from glob-style file pattern to Python version to use when checking the
corresponding file(s).

This may be useful for overriding the global Python version settings in `target-version` or
`requires-python` for a subset of files. For example, if you have a project with a minimum
supported Python version of 3.9 but a subdirectory of developer scripts that want to use a
newer feature like the `match` statement from Python 3.10, you can use
`per-file-target-version` to specify `"developer_scripts/*.py" = "py310"`.

This setting is used by the linter to enforce any enabled version-specific lint rules, as
well as by the formatter for any version-specific formatting options, such as parenthesizing
context managers on Python 3.10+.

**Default value**: `{}`

**Type**: `dict[str, PythonVersion]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.per-file-target-version]
# Override the project-wide Python version for a developer scripts directory:
"scripts/*.py" = "py312"
```

```
[per-file-target-version]
# Override the project-wide Python version for a developer scripts directory:
"scripts/*.py" = "py312"
```

---

#### [`preview`](#preview)

Whether to enable preview mode. When preview mode is enabled, Ruff will
use unstable rules, fixes, and formatting.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
# Enable preview features.
preview = true
```

```
# Enable preview features.
preview = true
```

---

#### [`required-version`](#required-version)

Enforce a requirement on the version of Ruff, to enforce at runtime.
If the version of Ruff does not meet the requirement, Ruff will exit
with an error.

Useful for unifying results across many environments, e.g., with a
`pyproject.toml` file.

Accepts a [PEP 440](https://peps.python.org/pep-0440/) specifier, like `==0.3.1` or `>=0.3.1`.

**Default value**: `null`

**Type**: `str`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
required-version = ">=0.0.193"
```

```
required-version = ">=0.0.193"
```

---

#### [`respect-gitignore`](#respect-gitignore)

Whether to automatically exclude files that are ignored by `.ignore`,
`.gitignore`, `.git/info/exclude`, and global `gitignore` files.
Enabled by default.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
respect-gitignore = false
```

```
respect-gitignore = false
```

---

#### [`show-fixes`](#show-fixes)

Whether to show an enumeration of all fixed lint violations
(overridden by the `--show-fixes` command-line flag).

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
# Enumerate all fixed violations.
show-fixes = true
```

```
# Enumerate all fixed violations.
show-fixes = true
```

---

#### [`src`](#src)

The directories to consider when resolving first- vs. third-party
imports.

When omitted, the `src` directory will typically default to including both:

1. The directory containing the nearest `pyproject.toml`, `ruff.toml`, or `.ruff.toml` file (the "project root").
2. The `"src"` subdirectory of the project root.

These defaults ensure that Ruff supports both flat layouts and `src` layouts out-of-the-box.
(If a configuration file is explicitly provided (e.g., via the `--config` command-line
flag), the current working directory will be considered the project root.)

As an example, consider an alternative project structure, like:

```
my_project
├── pyproject.toml
└── lib
    └── my_package
        ├── __init__.py
        ├── foo.py
        └── bar.py
```

In this case, the `./lib` directory should be included in the `src` option
(e.g., `src = ["lib"]`), such that when resolving imports, `my_package.foo`
is considered first-party.

This field supports globs. For example, if you have a series of Python
packages in a `python_modules` directory, `src = ["python_modules/*"]`
would expand to incorporate all packages in that directory. User home
directory and environment variables will also be expanded.

**Default value**: `[".", "src"]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
# Allow imports relative to the "src" and "test" directories.
src = ["src", "test"]
```

```
# Allow imports relative to the "src" and "test" directories.
src = ["src", "test"]
```

---

#### [`target-version`](#target-version)

The minimum Python version to target, e.g., when considering automatic
code upgrades, like rewriting type annotations. Ruff will not propose
changes using features that are not available in the given version.

For example, to represent supporting Python >=3.11 or ==3.11
specify `target-version = "py311"`.

If you're already using a `pyproject.toml` file, we recommend
`project.requires-python` instead, as it's based on Python packaging
standards, and will be respected by other tools. For example, Ruff
treats the following as identical to `target-version = "py38"`:

```
[project]
requires-python = ">=3.8"
```

If both are specified, `target-version` takes precedence over
`requires-python`. See [*Inferring the Python version*](https://docs.astral.sh/ruff/configuration/#inferring-the-python-version)
for a complete description of how the `target-version` is determined
when left unspecified.

Note that a stub file can [sometimes make use of a typing feature](https://typing.python.org/en/latest/spec/distributing.html#syntax)
before it is available at runtime, as long as the stub does not make
use of new *syntax*. For example, a type checker will understand
`int | str` in a stub as being a `Union` type annotation, even if the
type checker is run using Python 3.9, despite the fact that the `|`
operator can only be used to create union types at runtime on Python
3.10+. As such, Ruff will often recommend newer features in a stub
file than it would for an equivalent runtime file with the same target
version.

**Default value**: `"py310"`

**Type**: `"py37" | "py38" | "py39" | "py310" | "py311" | "py312" | "py313" | "py314"`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
# Always generate Python 3.7-compatible code.
target-version = "py37"
```

```
# Always generate Python 3.7-compatible code.
target-version = "py37"
```

---

#### [`unsafe-fixes`](#unsafe-fixes)

Enable application of unsafe fixes.
If excluded, a hint will be displayed when unsafe fixes are available.
If set to false, the hint will be hidden.

**Default value**: `null`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff]
unsafe-fixes = true
```

```
unsafe-fixes = true
```

---

### [`analyze`](#analyze)

Configures Ruff's `analyze` command.

#### [`detect-string-imports`](#analyze_detect-string-imports)

Whether to detect imports from string literals. When enabled, Ruff will search for string
literals that "look like" import paths, and include them in the import map, if they resolve
to valid Python modules.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.analyze]
detect-string-imports = true
```

```
[analyze]
detect-string-imports = true
```

---

#### [`direction`](#analyze_direction)

Whether to generate a map from file to files that it depends on (dependencies) or files that
depend on it (dependents).

**Default value**: `"dependencies"`

**Type**: `"dependents" | "dependencies"`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.analyze]
direction = "dependencies"
```

```
[analyze]
direction = "dependencies"
```

---

#### [`exclude`](#analyze_exclude)

A list of file patterns to exclude from analysis in addition to the files excluded globally (see [`exclude`](#exclude), and [`extend-exclude`](#extend-exclude)).

Exclusions are based on globs, and can be either:

* Single-path patterns, like `.mypy_cache` (to exclude any directory
  named `.mypy_cache` in the tree), `foo.py` (to exclude any file named
  `foo.py`), or `foo_*.py` (to exclude any file matching `foo_*.py` ).
* Relative patterns, like `directory/foo.py` (to exclude that specific
  file) or `directory/*.py` (to exclude any Python files in
  `directory`). Note that these paths are relative to the project root
  (e.g., the directory containing your `pyproject.toml`).

For more information on the glob syntax, refer to the [`globset` documentation](https://docs.rs/globset/latest/globset/#syntax).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.analyze]
exclude = ["generated"]
```

```
[analyze]
exclude = ["generated"]
```

---

#### [`include-dependencies`](#analyze_include-dependencies)

A map from file path to the list of Python or non-Python file paths or globs that should be
considered dependencies of that file, regardless of whether relevant imports are detected.

**Default value**: `{}`

**Type**: `dict[str, list[str]]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.analyze.include-dependencies]
"foo/bar.py" = ["foo/baz/*.py"]
"foo/baz/reader.py" = ["configs/bar.json"]
```

```
[analyze.include-dependencies]
"foo/bar.py" = ["foo/baz/*.py"]
"foo/baz/reader.py" = ["configs/bar.json"]
```

---

#### [`preview`](#analyze_preview)

Whether to enable preview mode. When preview mode is enabled, Ruff will expose unstable
commands.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.analyze]
# Enable preview features.
preview = true
```

```
[analyze]
# Enable preview features.
preview = true
```

---

#### [`string-imports-min-dots`](#analyze_string-imports-min-dots)

The minimum number of dots in a string to consider it a valid import.

This setting is only relevant when [`detect-string-imports`](#detect-string-imports) is enabled.
For example, if this is set to `2`, then only strings with at least two dots (e.g., `"path.to.module"`)
would be considered valid imports.

**Default value**: `2`

**Type**: `usize`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.analyze]
string-imports-min-dots = 2
```

```
[analyze]
string-imports-min-dots = 2
```

---

#### [`type-checking-imports`](#analyze_type-checking-imports)

Whether to include imports that are only used for type checking (i.e., imports within `if TYPE_CHECKING:` blocks).
When enabled (default), type-checking-only imports are included in the import graph.
When disabled, they are excluded.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.analyze]
# Exclude type-checking-only imports from the graph
type-checking-imports = false
```

```
[analyze]
# Exclude type-checking-only imports from the graph
type-checking-imports = false
```

---

### [`format`](#format)

Configures the way Ruff formats your code.

#### [`docstring-code-format`](#format_docstring-code-format)

Whether to format code snippets in docstrings.

When this is enabled, Python code examples within docstrings are
automatically reformatted.

For example, when this is enabled, the following code:

```
def f(x):
    """
    Something about `f`. And an example in doctest format:

    >>> f(  x  )

    Markdown is also supported:

    ```py
    f(  x  )
    ```

    As are reStructuredText literal blocks::

        f(  x  )


    And reStructuredText code blocks:

    .. code-block:: python

        f(  x  )
    """
    pass
```

... will be reformatted (assuming the rest of the options are set to
their defaults) as:

```
def f(x):
    """
    Something about `f`. And an example in doctest format:

    >>> f(x)

    Markdown is also supported:

    ```py
    f(x)
    ```

    As are reStructuredText literal blocks::

        f(x)


    And reStructuredText code blocks:

    .. code-block:: python

        f(x)
    """
    pass
```

If a code snippet in a docstring contains invalid Python code or if the
formatter would otherwise write invalid Python code, then the code
example is ignored by the formatter and kept as-is.

Currently, doctest, Markdown, reStructuredText literal blocks, and
reStructuredText code blocks are all supported and automatically
recognized. In the case of unlabeled fenced code blocks in Markdown and
reStructuredText literal blocks, the contents are assumed to be Python
and reformatted. As with any other format, if the contents aren't valid
Python, then the block is left untouched automatically.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.format]
# Enable reformatting of code snippets in docstrings.
docstring-code-format = true
```

```
[format]
# Enable reformatting of code snippets in docstrings.
docstring-code-format = true
```

---

#### [`docstring-code-line-length`](#format_docstring-code-line-length)

Set the line length used when formatting code snippets in docstrings.

This only has an effect when the `docstring-code-format` setting is
enabled.

The default value for this setting is `"dynamic"`, which has the effect
of ensuring that any reformatted code examples in docstrings adhere to
the global line length configuration that is used for the surrounding
Python code. The point of this setting is that it takes the indentation
of the docstring into account when reformatting code examples.

Alternatively, this can be set to a fixed integer, which will result
in the same line length limit being applied to all reformatted code
examples in docstrings. When set to a fixed integer, the indent of the
docstring is not taken into account. That is, this may result in lines
in the reformatted code example that exceed the globally configured
line length limit.

For example, when this is set to `20` and [`docstring-code-format`](#docstring-code-format)
is enabled, then this code:

```
def f(x):
    '''
    Something about `f`. And an example:

    .. code-block:: python

        foo, bar, quux = this_is_a_long_line(lion, hippo, lemur, bear)
    '''
    pass
```

... will be reformatted (assuming the rest of the options are set
to their defaults) as:

```
def f(x):
    """
    Something about `f`. And an example:

    .. code-block:: python

        (
            foo,
            bar,
            quux,
        ) = this_is_a_long_line(
            lion,
            hippo,
            lemur,
            bear,
        )
    """
    pass
```

**Default value**: `"dynamic"`

**Type**: `int | "dynamic"`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.format]
# Format all docstring code snippets with a line length of 60.
docstring-code-line-length = 60
```

```
[format]
# Format all docstring code snippets with a line length of 60.
docstring-code-line-length = 60
```

---

#### [`exclude`](#format_exclude)

A list of file patterns to exclude from formatting in addition to the files excluded globally (see [`exclude`](#exclude), and [`extend-exclude`](#extend-exclude)).

Exclusions are based on globs, and can be either:

* Single-path patterns, like `.mypy_cache` (to exclude any directory
  named `.mypy_cache` in the tree), `foo.py` (to exclude any file named
  `foo.py`), or `foo_*.py` (to exclude any file matching `foo_*.py` ).
* Relative patterns, like `directory/foo.py` (to exclude that specific
  file) or `directory/*.py` (to exclude any Python files in
  `directory`). Note that these paths are relative to the project root
  (e.g., the directory containing your `pyproject.toml`).

For more information on the glob syntax, refer to the [`globset` documentation](https://docs.rs/globset/latest/globset/#syntax).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.format]
exclude = ["generated"]
```

```
[format]
exclude = ["generated"]
```

---

#### [`indent-style`](#format_indent-style)

Whether to use spaces or tabs for indentation.

`indent-style = "space"` (default):

```
def f():
    print("Hello") #  Spaces indent the `print` statement.
```

`indent-style = "tab"`:

```
def f():
    print("Hello") #  A tab `\t` indents the `print` statement.
```

PEP 8 recommends using spaces for [indentation](https://peps.python.org/pep-0008/#indentation).
We care about accessibility; if you do not need tabs for accessibility, we do not recommend you use them.

See [`indent-width`](#indent-width) to configure the number of spaces per indentation and the tab width.

**Default value**: `"space"`

**Type**: `"space" | "tab"`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.format]
# Use tabs instead of 4 space indentation.
indent-style = "tab"
```

```
[format]
# Use tabs instead of 4 space indentation.
indent-style = "tab"
```

---

#### [`line-ending`](#format_line-ending)

The character Ruff uses at the end of a line.

* `auto`: The newline style is detected automatically on a file per file basis. Files with mixed line endings will be converted to the first detected line ending. Defaults to `\n` for files that contain no line endings.
* `lf`: Line endings will be converted to `\n`. The default line ending on Unix.
* `cr-lf`: Line endings will be converted to `\r\n`. The default line ending on Windows.
* `native`: Line endings will be converted to `\n` on Unix and `\r\n` on Windows.

**Default value**: `"auto"`

**Type**: `"auto" | "lf" | "cr-lf" | "native"`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.format]
# Use `\n` line endings for all files
line-ending = "lf"
```

```
[format]
# Use `\n` line endings for all files
line-ending = "lf"
```

---

#### [`preview`](#format_preview)

Whether to enable the unstable preview style formatting.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.format]
# Enable preview style formatting.
preview = true
```

```
[format]
# Enable preview style formatting.
preview = true
```

---

#### [`quote-style`](#format_quote-style)

Configures the preferred quote character for strings. The recommended options are

* `double` (default): Use double quotes `"`
* `single`: Use single quotes `'`

In compliance with [PEP 8](https://peps.python.org/pep-0008/) and [PEP 257](https://peps.python.org/pep-0257/),
Ruff prefers double quotes for triple quoted strings and docstrings even when using `quote-style = "single"`.

Ruff deviates from using the configured quotes if doing so prevents the need for
escaping quote characters inside the string:

```
a = "a string without any quotes"
b = "It's monday morning"
```

Ruff will change the quotes of the string assigned to `a` to single quotes when using `quote-style = "single"`.
However, Ruff uses double quotes for the string assigned to `b` because using single quotes would require escaping the `'`,
which leads to the less readable code: `'It\'s monday morning'`.

In addition, Ruff supports the quote style `preserve` for projects that already use
a mixture of single and double quotes and can't migrate to the `double` or `single` style.
The quote style `preserve` leaves the quotes of all strings unchanged.

**Default value**: `"double"`

**Type**: `"double" | "single" | "preserve"`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.format]
# Prefer single quotes over double quotes.
quote-style = "single"
```

```
[format]
# Prefer single quotes over double quotes.
quote-style = "single"
```

---

#### [`skip-magic-trailing-comma`](#format_skip-magic-trailing-comma)

Ruff uses existing trailing commas as an indication that short lines should be left separate.
If this option is set to `true`, the magic trailing comma is ignored.

For example, Ruff leaves the arguments separate even though
collapsing the arguments to a single line doesn't exceed the line length if `skip-magic-trailing-comma = false`:

```
# The arguments remain on separate lines because of the trailing comma after `b`
def test(
    a,
    b,
): pass
```

Setting `skip-magic-trailing-comma = true` changes the formatting to:

```
# The arguments are collapsed to a single line because the trailing comma is ignored
def test(a, b):
    pass
```

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.format]
skip-magic-trailing-comma = true
```

```
[format]
skip-magic-trailing-comma = true
```

---

### [`lint`](#lint)

Configures how Ruff checks your code.

Options specified in the `lint` section take precedence over the deprecated top-level settings.

#### [`allowed-confusables`](#lint_allowed-confusables)

A list of allowed "confusable" Unicode characters to ignore when
enforcing `RUF001`, `RUF002`, and `RUF003`.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
# Allow minus-sign (U+2212), greek-small-letter-rho (U+03C1), and the asterisk-operator (U+2217),
# which could be confused for "-", "p", and "*", respectively.
allowed-confusables = ["−", "ρ", "∗"]
```

```
[lint]
# Allow minus-sign (U+2212), greek-small-letter-rho (U+03C1), and the asterisk-operator (U+2217),
# which could be confused for "-", "p", and "*", respectively.
allowed-confusables = ["−", "ρ", "∗"]
```

---

#### [`dummy-variable-rgx`](#lint_dummy-variable-rgx)

A regular expression used to identify "dummy" variables, or those which
should be ignored when enforcing (e.g.) unused-variable rules. The
default expression matches `_`, `__`, and `_var`, but not `_var_`.

**Default value**: `"^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"`

**Type**: `str`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
# Only ignore variables named "_".
dummy-variable-rgx = "^_$"
```

```
[lint]
# Only ignore variables named "_".
dummy-variable-rgx = "^_$"
```

---

#### [`exclude`](#lint_exclude)

A list of file patterns to exclude from linting in addition to the files excluded globally (see [`exclude`](#exclude), and [`extend-exclude`](#extend-exclude)).

Exclusions are based on globs, and can be either:

* Single-path patterns, like `.mypy_cache` (to exclude any directory
  named `.mypy_cache` in the tree), `foo.py` (to exclude any file named
  `foo.py`), or `foo_*.py` (to exclude any file matching `foo_*.py` ).
* Relative patterns, like `directory/foo.py` (to exclude that specific
  file) or `directory/*.py` (to exclude any Python files in
  `directory`). Note that these paths are relative to the project root
  (e.g., the directory containing your `pyproject.toml`).

For more information on the glob syntax, refer to the [`globset` documentation](https://docs.rs/globset/latest/globset/#syntax).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
exclude = ["generated"]
```

```
[lint]
exclude = ["generated"]
```

---

#### [`explicit-preview-rules`](#lint_explicit-preview-rules)

Whether to require exact codes to select preview rules. When enabled,
preview rules will not be selected by prefixes — the full code of each
preview rule will be required to enable the rule.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
# Require explicit selection of preview rules.
explicit-preview-rules = true
```

```
[lint]
# Require explicit selection of preview rules.
explicit-preview-rules = true
```

---

#### [`extend-fixable`](#lint_extend-fixable)

A list of rule codes or prefixes to consider fixable, in addition to those
specified by [`fixable`](#lint_fixable).

**Default value**: `[]`

**Type**: `list[RuleSelector]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
# Enable fix for flake8-bugbear (`B`), on top of any rules specified by `fixable`.
extend-fixable = ["B"]
```

```
[lint]
# Enable fix for flake8-bugbear (`B`), on top of any rules specified by `fixable`.
extend-fixable = ["B"]
```

---

#### [`extend-ignore`](#lint_extend-ignore)

Deprecated

This option has been deprecated. The `extend-ignore` option is now interchangeable with [`ignore`](#lint_ignore). Please update your configuration to use the [`ignore`](#lint_ignore) option instead.

A list of rule codes or prefixes to ignore, in addition to those
specified by `ignore`.

**Default value**: `[]`

**Type**: `list[RuleSelector]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
# Skip unused variable rules (`F841`).
extend-ignore = ["F841"]
```

```
[lint]
# Skip unused variable rules (`F841`).
extend-ignore = ["F841"]
```

---

#### [`extend-per-file-ignores`](#lint_extend-per-file-ignores)

A list of mappings from file pattern to rule codes or prefixes to
exclude, in addition to any rules excluded by [`per-file-ignores`](#lint_per-file-ignores).

**Default value**: `{}`

**Type**: `dict[str, list[RuleSelector]]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.extend-per-file-ignores]
# Also ignore `E402` in all `__init__.py` files.
"__init__.py" = ["E402"]
```

```
[lint.extend-per-file-ignores]
# Also ignore `E402` in all `__init__.py` files.
"__init__.py" = ["E402"]
```

---

#### [`extend-safe-fixes`](#lint_extend-safe-fixes)

A list of rule codes or prefixes for which unsafe fixes should be considered
safe.

**Default value**: `[]`

**Type**: `list[RuleSelector]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
# Allow applying all unsafe fixes in the `E` rules and `F401` without the `--unsafe-fixes` flag
extend-safe-fixes = ["E", "F401"]
```

```
[lint]
# Allow applying all unsafe fixes in the `E` rules and `F401` without the `--unsafe-fixes` flag
extend-safe-fixes = ["E", "F401"]
```

---

#### [`extend-select`](#lint_extend-select)

A list of rule codes or prefixes to enable, in addition to those
specified by [`select`](#lint_select).

**Default value**: `[]`

**Type**: `list[RuleSelector]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
# On top of the default `select` (`E4`, E7`, `E9`, and `F`), enable flake8-bugbear (`B`) and flake8-quotes (`Q`).
extend-select = ["B", "Q"]
```

```
[lint]
# On top of the default `select` (`E4`, E7`, `E9`, and `F`), enable flake8-bugbear (`B`) and flake8-quotes (`Q`).
extend-select = ["B", "Q"]
```

---

#### [`extend-unsafe-fixes`](#lint_extend-unsafe-fixes)

A list of rule codes or prefixes for which safe fixes should be considered
unsafe.

**Default value**: `[]`

**Type**: `list[RuleSelector]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
# Require the `--unsafe-fixes` flag when fixing the `E` rules and `F401`
extend-unsafe-fixes = ["E", "F401"]
```

```
[lint]
# Require the `--unsafe-fixes` flag when fixing the `E` rules and `F401`
extend-unsafe-fixes = ["E", "F401"]
```

---

#### [`external`](#lint_external)

A list of rule codes or prefixes that are unsupported by Ruff, but should be
preserved when (e.g.) validating `# noqa` directives. Useful for
retaining `# noqa` directives that cover plugins not yet implemented
by Ruff.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
# Avoiding flagging (and removing) any codes starting with `V` from any
# `# noqa` directives, despite Ruff's lack of support for `vulture`.
external = ["V"]
```

```
[lint]
# Avoiding flagging (and removing) any codes starting with `V` from any
# `# noqa` directives, despite Ruff's lack of support for `vulture`.
external = ["V"]
```

---

#### [`fixable`](#lint_fixable)

A list of rule codes or prefixes to consider fixable. By default,
all rules are considered fixable.

**Default value**: `["ALL"]`

**Type**: `list[RuleSelector]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
# Only allow fix behavior for `E` and `F` rules.
fixable = ["E", "F"]
```

```
[lint]
# Only allow fix behavior for `E` and `F` rules.
fixable = ["E", "F"]
```

---

#### [`future-annotations`](#lint_future-annotations)

Whether to allow rules to add `from __future__ import annotations` in cases where this would
simplify a fix or enable a new diagnostic.

For example, `TC001`, `TC002`, and `TC003` can move more imports into `TYPE_CHECKING` blocks
if `__future__` annotations are enabled.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
# Enable `from __future__ import annotations` imports
future-annotations = true
```

```
[lint]
# Enable `from __future__ import annotations` imports
future-annotations = true
```

---

#### [`ignore`](#lint_ignore)

A list of rule codes or prefixes to ignore. Prefixes can specify exact
rules (like `F841`), entire categories (like `F`), or anything in
between.

When breaking ties between enabled and disabled rules (via `select` and
`ignore`, respectively), more specific prefixes override less
specific prefixes. `ignore` takes precedence over `select` if the same
prefix appears in both.

**Default value**: `[]`

**Type**: `list[RuleSelector]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
# Skip unused variable rules (`F841`).
ignore = ["F841"]
```

```
[lint]
# Skip unused variable rules (`F841`).
ignore = ["F841"]
```

---

#### [`ignore-init-module-imports`](#lint_ignore-init-module-imports)

Deprecated

This option has been deprecated in 0.4.4. `ignore-init-module-imports` will be removed in a future version because F401 now recommends appropriate fixes for unused imports in `__init__.py` (currently in preview mode). See documentation for more information and please update your configuration.

Avoid automatically removing unused imports in `__init__.py` files. Such
imports will still be flagged, but with a dedicated message suggesting
that the import is either added to the module's `__all__` symbol, or
re-exported with a redundant alias (e.g., `import os as os`).

This option is enabled by default, but you can opt-in to removal of imports
via an unsafe fix.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
ignore-init-module-imports = false
```

```
[lint]
ignore-init-module-imports = false
```

---

#### [`logger-objects`](#lint_logger-objects)

A list of objects that should be treated equivalently to a
`logging.Logger` object.

This is useful for ensuring proper diagnostics (e.g., to identify
`logging` deprecations and other best-practices) for projects that
re-export a `logging.Logger` object from a common module.

For example, if you have a module `logging_setup.py` with the following
contents:

```
import logging

logger = logging.getLogger(__name__)
```

Adding `"logging_setup.logger"` to `logger-objects` will ensure that
`logging_setup.logger` is treated as a `logging.Logger` object when
imported from other modules (e.g., `from logging_setup import logger`).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
logger-objects = ["logging_setup.logger"]
```

```
[lint]
logger-objects = ["logging_setup.logger"]
```

---

#### [`per-file-ignores`](#lint_per-file-ignores)

A list of mappings from file pattern to rule codes or prefixes to
exclude, when considering any matching files. An initial '!' negates
the file pattern.

**Default value**: `{}`

**Type**: `dict[str, list[RuleSelector]]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.per-file-ignores]
# Ignore `E402` (import violations) in all `__init__.py` files, and in `path/to/file.py`.
"__init__.py" = ["E402"]
"path/to/file.py" = ["E402"]
# Ignore `D` rules everywhere except for the `src/` directory.
"!src/**.py" = ["D"]
```

```
[lint.per-file-ignores]
# Ignore `E402` (import violations) in all `__init__.py` files, and in `path/to/file.py`.
"__init__.py" = ["E402"]
"path/to/file.py" = ["E402"]
# Ignore `D` rules everywhere except for the `src/` directory.
"!src/**.py" = ["D"]
```

---

#### [`preview`](#lint_preview)

Whether to enable preview mode. When preview mode is enabled, Ruff will
use unstable rules and fixes.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
# Enable preview features.
preview = true
```

```
[lint]
# Enable preview features.
preview = true
```

---

#### [`select`](#lint_select)

A list of rule codes or prefixes to enable. Prefixes can specify exact
rules (like `F841`), entire categories (like `F`), or anything in
between.

When breaking ties between enabled and disabled rules (via `select` and
`ignore`, respectively), more specific prefixes override less
specific prefixes. `ignore` takes precedence over `select` if the
same prefix appears in both.

**Default value**: `["E4", "E7", "E9", "F"]`

**Type**: `list[RuleSelector]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
# On top of the defaults (`E4`, E7`, `E9`, and `F`), enable flake8-bugbear (`B`) and flake8-quotes (`Q`).
select = ["E4", "E7", "E9", "F", "B", "Q"]
```

```
[lint]
# On top of the defaults (`E4`, E7`, `E9`, and `F`), enable flake8-bugbear (`B`) and flake8-quotes (`Q`).
select = ["E4", "E7", "E9", "F", "B", "Q"]
```

---

#### [`task-tags`](#lint_task-tags)

A list of task tags to recognize (e.g., "TODO", "FIXME", "XXX").

Comments starting with these tags will be ignored by commented-out code
detection (`ERA`), and skipped by line-length rules (`E501`) if
[`ignore-overlong-task-comments`](#lint_pycodestyle_ignore-overlong-task-comments) is set to `true`.

**Default value**: `["TODO", "FIXME", "XXX"]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
task-tags = ["HACK"]
```

```
[lint]
task-tags = ["HACK"]
```

---

#### [`typing-extensions`](#lint_typing-extensions)

Whether to allow imports from the third-party `typing_extensions` module for Python versions
before a symbol was added to the first-party `typing` module.

Many rules try to import symbols from the `typing` module but fall back to
`typing_extensions` for earlier versions of Python. This option can be used to disable this
fallback behavior in cases where `typing_extensions` is not installed.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
# Disable `typing_extensions` imports
typing-extensions = false
```

```
[lint]
# Disable `typing_extensions` imports
typing-extensions = false
```

---

#### [`typing-modules`](#lint_typing-modules)

A list of modules whose exports should be treated equivalently to
members of the `typing` module.

This is useful for ensuring proper type annotation inference for
projects that re-export `typing` and `typing_extensions` members
from a compatibility module. If omitted, any members imported from
modules apart from `typing` and `typing_extensions` will be treated
as ordinary Python objects.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
typing-modules = ["airflow.typing_compat"]
```

```
[lint]
typing-modules = ["airflow.typing_compat"]
```

---

#### [`unfixable`](#lint_unfixable)

A list of rule codes or prefixes to consider non-fixable.

**Default value**: `[]`

**Type**: `list[RuleSelector]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint]
# Disable fix for unused imports (`F401`).
unfixable = ["F401"]
```

```
[lint]
# Disable fix for unused imports (`F401`).
unfixable = ["F401"]
```

---

### [`lint.flake8-annotations`](#lintflake8-annotations)

Options for the `flake8-annotations` plugin.

#### [`allow-star-arg-any`](#lint_flake8-annotations_allow-star-arg-any)

Whether to suppress `ANN401` for dynamically typed `*args` and
`**kwargs` arguments.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-annotations]
allow-star-arg-any = true
```

```
[lint.flake8-annotations]
allow-star-arg-any = true
```

---

#### [`ignore-fully-untyped`](#lint_flake8-annotations_ignore-fully-untyped)

Whether to suppress `ANN*` rules for any declaration
that hasn't been typed at all.
This makes it easier to gradually add types to a codebase.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-annotations]
ignore-fully-untyped = true
```

```
[lint.flake8-annotations]
ignore-fully-untyped = true
```

---

#### [`mypy-init-return`](#lint_flake8-annotations_mypy-init-return)

Whether to allow the omission of a return type hint for `__init__` if at
least one argument is annotated.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-annotations]
mypy-init-return = true
```

```
[lint.flake8-annotations]
mypy-init-return = true
```

---

#### [`suppress-dummy-args`](#lint_flake8-annotations_suppress-dummy-args)

Whether to suppress `ANN000`-level violations for arguments matching the
"dummy" variable regex (like `_`).

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-annotations]
suppress-dummy-args = true
```

```
[lint.flake8-annotations]
suppress-dummy-args = true
```

---

#### [`suppress-none-returning`](#lint_flake8-annotations_suppress-none-returning)

Whether to suppress `ANN200`-level violations for functions that meet
either of the following criteria:

* Contain no `return` statement.
* Explicit `return` statement(s) all return `None` (explicitly or
  implicitly).

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-annotations]
suppress-none-returning = true
```

```
[lint.flake8-annotations]
suppress-none-returning = true
```

---

### [`lint.flake8-bandit`](#lintflake8-bandit)

Options for the `flake8-bandit` plugin.

#### [`allowed-markup-calls`](#lint_flake8-bandit_allowed-markup-calls)

A list of callable names, whose result may be safely passed into
[`markupsafe.Markup`](https://markupsafe.palletsprojects.com/en/stable/escaping/#markupsafe.Markup).

Expects to receive a list of fully-qualified names (e.g., `bleach.clean`, rather than `clean`).

This setting helps you avoid false positives in code like:

```
from bleach import clean
from markupsafe import Markup

cleaned_markup = Markup(clean(some_user_input))
```

Where the use of [`bleach.clean`](https://bleach.readthedocs.io/en/latest/clean.html)
usually ensures that there's no XSS vulnerability.

Although it is not recommended, you may also use this setting to whitelist other
kinds of calls, e.g. calls to i18n translation functions, where how safe that is
will depend on the implementation and how well the translations are audited.

Another common use-case is to wrap the output of functions that generate markup
like [`xml.etree.ElementTree.tostring`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.tostring)
or template rendering engines where sanitization of potential user input is either
already baked in or has to happen before rendering.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-bandit]
allowed-markup-calls = ["bleach.clean", "my_package.sanitize"]
```

```
[lint.flake8-bandit]
allowed-markup-calls = ["bleach.clean", "my_package.sanitize"]
```

---

#### [`check-typed-exception`](#lint_flake8-bandit_check-typed-exception)

Whether to disallow `try`-`except`-`pass` (`S110`) for specific
exception types. By default, `try`-`except`-`pass` is only
disallowed for `Exception` and `BaseException`.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-bandit]
check-typed-exception = true
```

```
[lint.flake8-bandit]
check-typed-exception = true
```

---

#### [`extend-markup-names`](#lint_flake8-bandit_extend-markup-names)

A list of additional callable names that behave like
[`markupsafe.Markup`](https://markupsafe.palletsprojects.com/en/stable/escaping/#markupsafe.Markup).

Expects to receive a list of fully-qualified names (e.g., `webhelpers.html.literal`, rather than
`literal`).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-bandit]
extend-markup-names = ["webhelpers.html.literal", "my_package.Markup"]
```

```
[lint.flake8-bandit]
extend-markup-names = ["webhelpers.html.literal", "my_package.Markup"]
```

---

#### [`hardcoded-tmp-directory`](#lint_flake8-bandit_hardcoded-tmp-directory)

A list of directories to consider temporary (see `S108`).

**Default value**: `["/tmp", "/var/tmp", "/dev/shm"]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-bandit]
hardcoded-tmp-directory = ["/foo/bar"]
```

```
[lint.flake8-bandit]
hardcoded-tmp-directory = ["/foo/bar"]
```

---

#### [`hardcoded-tmp-directory-extend`](#lint_flake8-bandit_hardcoded-tmp-directory-extend)

A list of directories to consider temporary, in addition to those
specified by [`hardcoded-tmp-directory`](#lint_flake8-bandit_hardcoded-tmp-directory) (see `S108`).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-bandit]
hardcoded-tmp-directory-extend = ["/foo/bar"]
```

```
[lint.flake8-bandit]
hardcoded-tmp-directory-extend = ["/foo/bar"]
```

---

### [`lint.flake8-boolean-trap`](#lintflake8-boolean-trap)

Options for the `flake8-boolean-trap` plugin

#### [`extend-allowed-calls`](#lint_flake8-boolean-trap_extend-allowed-calls)

Additional callable functions with which to allow boolean traps.

Expects to receive a list of fully-qualified names (e.g., `pydantic.Field`, rather than
`Field`).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-boolean-trap]
extend-allowed-calls = ["pydantic.Field", "django.db.models.Value"]
```

```
[lint.flake8-boolean-trap]
extend-allowed-calls = ["pydantic.Field", "django.db.models.Value"]
```

---

### [`lint.flake8-bugbear`](#lintflake8-bugbear)

Options for the `flake8-bugbear` plugin.

#### [`extend-immutable-calls`](#lint_flake8-bugbear_extend-immutable-calls)

Additional callable functions to consider "immutable" when evaluating, e.g., the
`function-call-in-default-argument` rule (`B008`) or `function-call-in-dataclass-defaults`
rule (`RUF009`).

Expects to receive a list of fully-qualified names (e.g., `fastapi.Query`, rather than
`Query`).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-bugbear]
# Allow default arguments like, e.g., `data: List[str] = fastapi.Query(None)`.
extend-immutable-calls = ["fastapi.Depends", "fastapi.Query"]
```

```
[lint.flake8-bugbear]
# Allow default arguments like, e.g., `data: List[str] = fastapi.Query(None)`.
extend-immutable-calls = ["fastapi.Depends", "fastapi.Query"]
```

---

### [`lint.flake8-builtins`](#lintflake8-builtins)

Options for the `flake8-builtins` plugin.

#### [`allowed-modules`](#lint_flake8-builtins_allowed-modules)

List of builtin module names to allow.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-builtins]
allowed-modules = ["secrets"]
```

```
[lint.flake8-builtins]
allowed-modules = ["secrets"]
```

---

#### [`builtins-allowed-modules`](#lint_flake8-builtins_builtins-allowed-modules)

Deprecated

This option has been deprecated in 0.10.0. `builtins-allowed-modules` has been renamed to `allowed-modules`. Use that instead.

DEPRECATED: This option has been renamed to `allowed-modules`. Use `allowed-modules` instead.

List of builtin module names to allow.

This option is ignored if both `allowed-modules` and `builtins-allowed-modules` are set.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-builtins]
builtins-allowed-modules = ["secrets"]
```

```
[lint.flake8-builtins]
builtins-allowed-modules = ["secrets"]
```

---

#### [`builtins-ignorelist`](#lint_flake8-builtins_builtins-ignorelist)

Deprecated

This option has been deprecated in 0.10.0. `builtins-ignorelist` has been renamed to `ignorelist`. Use that instead.

DEPRECATED: This option has been renamed to `ignorelist`. Use `ignorelist` instead.

Ignore list of builtins.

This option is ignored if both `ignorelist` and `builtins-ignorelist` are set.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-builtins]
builtins-ignorelist = ["id"]
```

```
[lint.flake8-builtins]
builtins-ignorelist = ["id"]
```

---

#### [`builtins-strict-checking`](#lint_flake8-builtins_builtins-strict-checking)

Deprecated

This option has been deprecated in 0.10.0. `builtins-strict-checking` has been renamed to `strict-checking`. Use that instead.

DEPRECATED: This option has been renamed to `strict-checking`. Use `strict-checking` instead.

Compare module names instead of full module paths.

This option is ignored if both `strict-checking` and `builtins-strict-checking` are set.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-builtins]
builtins-strict-checking = true
```

```
[lint.flake8-builtins]
builtins-strict-checking = true
```

---

#### [`ignorelist`](#lint_flake8-builtins_ignorelist)

Ignore list of builtins.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-builtins]
ignorelist = ["id"]
```

```
[lint.flake8-builtins]
ignorelist = ["id"]
```

---

#### [`strict-checking`](#lint_flake8-builtins_strict-checking)

Compare module names instead of full module paths.

Used by [`A005` - `stdlib-module-shadowing`](https://docs.astral.sh/ruff/rules/stdlib-module-shadowing/).

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-builtins]
strict-checking = true
```

```
[lint.flake8-builtins]
strict-checking = true
```

---

### [`lint.flake8-comprehensions`](#lintflake8-comprehensions)

Options for the `flake8-comprehensions` plugin.

#### [`allow-dict-calls-with-keyword-arguments`](#lint_flake8-comprehensions_allow-dict-calls-with-keyword-arguments)

Allow `dict` calls that make use of keyword arguments (e.g., `dict(a=1, b=2)`).

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-comprehensions]
allow-dict-calls-with-keyword-arguments = true
```

```
[lint.flake8-comprehensions]
allow-dict-calls-with-keyword-arguments = true
```

---

### [`lint.flake8-copyright`](#lintflake8-copyright)

Options for the `flake8-copyright` plugin.

#### [`author`](#lint_flake8-copyright_author)

Author to enforce within the copyright notice. If provided, the
author must be present immediately following the copyright notice.

**Default value**: `null`

**Type**: `str`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-copyright]
author = "Ruff"
```

```
[lint.flake8-copyright]
author = "Ruff"
```

---

#### [`min-file-size`](#lint_flake8-copyright_min-file-size)

A minimum file size (in bytes) required for a copyright notice to
be enforced. By default, all files are validated.

**Default value**: `0`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-copyright]
# Avoid enforcing a header on files smaller than 1024 bytes.
min-file-size = 1024
```

```
[lint.flake8-copyright]
# Avoid enforcing a header on files smaller than 1024 bytes.
min-file-size = 1024
```

---

#### [`notice-rgx`](#lint_flake8-copyright_notice-rgx)

The regular expression used to match the copyright notice, compiled
with the [`regex`](https://docs.rs/regex/latest/regex/) crate.
Defaults to `(?i)Copyright\s+((?:\(C\)|©)\s+)?\d{4}((-|,\s)\d{4})*`, which matches
the following:

* `Copyright 2023`
* `Copyright (C) 2023`
* `Copyright 2021-2023`
* `Copyright (C) 2021-2023`
* `Copyright (C) 2021, 2023`

**Default value**: `"(?i)Copyright\s+((?:\(C\)|©)\s+)?\d{4}((-|,\s)\d{4})*"`

**Type**: `str`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-copyright]
notice-rgx = "(?i)Copyright \\(C\\) \\d{4}"
```

```
[lint.flake8-copyright]
notice-rgx = "(?i)Copyright \\(C\\) \\d{4}"
```

---

### [`lint.flake8-errmsg`](#lintflake8-errmsg)

Options for the `flake8-errmsg` plugin.

#### [`max-string-length`](#lint_flake8-errmsg_max-string-length)

Maximum string length for string literals in exception messages.

**Default value**: `0`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-errmsg]
max-string-length = 20
```

```
[lint.flake8-errmsg]
max-string-length = 20
```

---

### [`lint.flake8-gettext`](#lintflake8-gettext)

Options for the `flake8-gettext` plugin.

#### [`extend-function-names`](#lint_flake8-gettext_extend-function-names)

Additional function names to consider as internationalization calls, in addition to those
included in [`function-names`](#lint_flake8-gettext_function-names).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-gettext]
extend-function-names = ["ugettetxt"]
```

```
[lint.flake8-gettext]
extend-function-names = ["ugettetxt"]
```

---

#### [`function-names`](#lint_flake8-gettext_function-names)

The function names to consider as internationalization calls.

**Default value**: `["_", "gettext", "ngettext"]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-gettext]
function-names = ["_", "gettext", "ngettext", "ugettetxt"]
```

```
[lint.flake8-gettext]
function-names = ["_", "gettext", "ngettext", "ugettetxt"]
```

---

### [`lint.flake8-implicit-str-concat`](#lintflake8-implicit-str-concat)

Options for the `flake8-implicit-str-concat` plugin

#### [`allow-multiline`](#lint_flake8-implicit-str-concat_allow-multiline)

Whether to allow implicit string concatenations for multiline strings.
By default, implicit concatenations of multiline strings are
allowed (but continuation lines, delimited with a backslash, are
prohibited).

Setting `allow-multiline = false` will automatically disable the
`explicit-string-concatenation` (`ISC003`) rule. Otherwise, both
implicit and explicit multiline string concatenations would be seen
as violations, making it impossible to write a linter-compliant multiline
string.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-implicit-str-concat]
allow-multiline = false
```

```
[lint.flake8-implicit-str-concat]
allow-multiline = false
```

---

### [`lint.flake8-import-conventions`](#lintflake8-import-conventions)

Options for the `flake8-import-conventions` plugin

#### [`aliases`](#lint_flake8-import-conventions_aliases)

The conventional aliases for imports. These aliases can be extended by
the [`extend-aliases`](#lint_flake8-import-conventions_extend-aliases) option.

**Default value**: `{"altair": "alt", "matplotlib": "mpl", "matplotlib.pyplot": "plt", "numpy": "np", "numpy.typing": "npt", "pandas": "pd", "seaborn": "sns", "tensorflow": "tf", "tkinter": "tk", "holoviews": "hv", "panel": "pn", "plotly.express": "px", "polars": "pl", "pyarrow": "pa", "xml.etree.ElementTree": "ET"}`

**Type**: `dict[str, str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-import-conventions.aliases]
# Declare the default aliases.
altair = "alt"
"matplotlib.pyplot" = "plt"
numpy = "np"
pandas = "pd"
seaborn = "sns"
scipy = "sp"
```

```
[lint.flake8-import-conventions.aliases]
# Declare the default aliases.
altair = "alt"
"matplotlib.pyplot" = "plt"
numpy = "np"
pandas = "pd"
seaborn = "sns"
scipy = "sp"
```

---

#### [`banned-aliases`](#lint_flake8-import-conventions_banned-aliases)

A mapping from module to its banned import aliases.

**Default value**: `{}`

**Type**: `dict[str, list[str]]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-import-conventions.banned-aliases]
# Declare the banned aliases.
"tensorflow.keras.backend" = ["K"]
```

```
[lint.flake8-import-conventions.banned-aliases]
# Declare the banned aliases.
"tensorflow.keras.backend" = ["K"]
```

---

#### [`banned-from`](#lint_flake8-import-conventions_banned-from)

A list of modules that should not be imported from using the
`from ... import ...` syntax.

For example, given `banned-from = ["pandas"]`, `from pandas import DataFrame`
would be disallowed, while `import pandas` would be allowed.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-import-conventions]
# Declare the banned `from` imports.
banned-from = ["typing"]
```

```
[lint.flake8-import-conventions]
# Declare the banned `from` imports.
banned-from = ["typing"]
```

---

#### [`extend-aliases`](#lint_flake8-import-conventions_extend-aliases)

A mapping from module to conventional import alias. These aliases will
be added to the [`aliases`](#lint_flake8-import-conventions_aliases) mapping.

**Default value**: `{}`

**Type**: `dict[str, str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-import-conventions.extend-aliases]
# Declare a custom alias for the `dask` module.
"dask.dataframe" = "dd"
```

```
[lint.flake8-import-conventions.extend-aliases]
# Declare a custom alias for the `dask` module.
"dask.dataframe" = "dd"
```

---

### [`lint.flake8-pytest-style`](#lintflake8-pytest-style)

Options for the `flake8-pytest-style` plugin

#### [`fixture-parentheses`](#lint_flake8-pytest-style_fixture-parentheses)

Boolean flag specifying whether `@pytest.fixture()` without parameters
should have parentheses. If the option is set to `false` (the default),
`@pytest.fixture` is valid and `@pytest.fixture()` is invalid. If set
to `true`, `@pytest.fixture()` is valid and `@pytest.fixture` is
invalid.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-pytest-style]
fixture-parentheses = true
```

```
[lint.flake8-pytest-style]
fixture-parentheses = true
```

---

#### [`mark-parentheses`](#lint_flake8-pytest-style_mark-parentheses)

Boolean flag specifying whether `@pytest.mark.foo()` without parameters
should have parentheses. If the option is set to `false` (the
default), `@pytest.mark.foo` is valid and `@pytest.mark.foo()` is
invalid. If set to `true`, `@pytest.mark.foo()` is valid and
`@pytest.mark.foo` is invalid.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-pytest-style]
mark-parentheses = true
```

```
[lint.flake8-pytest-style]
mark-parentheses = true
```

---

#### [`parametrize-names-type`](#lint_flake8-pytest-style_parametrize-names-type)

Expected type for multiple argument names in `@pytest.mark.parametrize`.
The following values are supported:

* `csv` — a comma-separated list, e.g.
  `@pytest.mark.parametrize("name1,name2", ...)`
* `tuple` (default) — e.g.
  `@pytest.mark.parametrize(("name1", "name2"), ...)`
* `list` — e.g. `@pytest.mark.parametrize(["name1", "name2"], ...)`

**Default value**: `tuple`

**Type**: `"csv" | "tuple" | "list"`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-pytest-style]
parametrize-names-type = "list"
```

```
[lint.flake8-pytest-style]
parametrize-names-type = "list"
```

---

#### [`parametrize-values-row-type`](#lint_flake8-pytest-style_parametrize-values-row-type)

Expected type for each row of values in `@pytest.mark.parametrize` in
case of multiple parameters. The following values are supported:

* `tuple` (default) — e.g.
  `@pytest.mark.parametrize(("name1", "name2"), [(1, 2), (3, 4)])`
* `list` — e.g.
  `@pytest.mark.parametrize(("name1", "name2"), [[1, 2], [3, 4]])`

**Default value**: `tuple`

**Type**: `"tuple" | "list"`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-pytest-style]
parametrize-values-row-type = "list"
```

```
[lint.flake8-pytest-style]
parametrize-values-row-type = "list"
```

---

#### [`parametrize-values-type`](#lint_flake8-pytest-style_parametrize-values-type)

Expected type for the list of values rows in `@pytest.mark.parametrize`.
The following values are supported:

* `tuple` — e.g. `@pytest.mark.parametrize("name", (1, 2, 3))`
* `list` (default) — e.g. `@pytest.mark.parametrize("name", [1, 2, 3])`

**Default value**: `list`

**Type**: `"tuple" | "list"`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-pytest-style]
parametrize-values-type = "tuple"
```

```
[lint.flake8-pytest-style]
parametrize-values-type = "tuple"
```

---

#### [`raises-extend-require-match-for`](#lint_flake8-pytest-style_raises-extend-require-match-for)

List of additional exception names that require a match= parameter in a
`pytest.raises()` call. This extends the default list of exceptions
that require a match= parameter.
This option is useful if you want to extend the default list of
exceptions that require a match= parameter without having to specify
the entire list.
Note that this option does not remove any exceptions from the default
list.

Supports glob patterns. For more information on the glob syntax, refer
to the [`globset` documentation](https://docs.rs/globset/latest/globset/#syntax).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-pytest-style]
raises-extend-require-match-for = ["requests.RequestException"]
```

```
[lint.flake8-pytest-style]
raises-extend-require-match-for = ["requests.RequestException"]
```

---

#### [`raises-require-match-for`](#lint_flake8-pytest-style_raises-require-match-for)

List of exception names that require a match= parameter in a
`pytest.raises()` call.

Supports glob patterns. For more information on the glob syntax, refer
to the [`globset` documentation](https://docs.rs/globset/latest/globset/#syntax).

**Default value**: `["BaseException", "Exception", "ValueError", "OSError", "IOError", "EnvironmentError", "socket.error"]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-pytest-style]
raises-require-match-for = ["requests.RequestException"]
```

```
[lint.flake8-pytest-style]
raises-require-match-for = ["requests.RequestException"]
```

---

#### [`warns-extend-require-match-for`](#lint_flake8-pytest-style_warns-extend-require-match-for)

List of additional warning names that require a match= parameter in a
`pytest.warns()` call. This extends the default list of warnings that
require a match= parameter.

This option is useful if you want to extend the default list of warnings
that require a match= parameter without having to specify the entire
list.

Note that this option does not remove any warnings from the default
list.

Supports glob patterns. For more information on the glob syntax, refer
to the [`globset` documentation](https://docs.rs/globset/latest/globset/#syntax).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-pytest-style]
warns-extend-require-match-for = ["requests.RequestsWarning"]
```

```
[lint.flake8-pytest-style]
warns-extend-require-match-for = ["requests.RequestsWarning"]
```

---

#### [`warns-require-match-for`](#lint_flake8-pytest-style_warns-require-match-for)

List of warning names that require a match= parameter in a
`pytest.warns()` call.

Supports glob patterns. For more information on the glob syntax, refer
to the [`globset` documentation](https://docs.rs/globset/latest/globset/#syntax).

**Default value**: `["Warning", "UserWarning", "DeprecationWarning"]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-pytest-style]
warns-require-match-for = ["requests.RequestsWarning"]
```

```
[lint.flake8-pytest-style]
warns-require-match-for = ["requests.RequestsWarning"]
```

---

### [`lint.flake8-quotes`](#lintflake8-quotes)

Options for the `flake8-quotes` plugin.

#### [`avoid-escape`](#lint_flake8-quotes_avoid-escape)

Whether to avoid using single quotes if a string contains single quotes,
or vice-versa with double quotes, as per [PEP 8](https://peps.python.org/pep-0008/#string-quotes).
This minimizes the need to escape quotation marks within strings.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-quotes]
# Don't bother trying to avoid escapes.
avoid-escape = false
```

```
[lint.flake8-quotes]
# Don't bother trying to avoid escapes.
avoid-escape = false
```

---

#### [`docstring-quotes`](#lint_flake8-quotes_docstring-quotes)

Quote style to prefer for docstrings (either "single" or "double").

When using the formatter, only "double" is compatible, as the formatter
enforces double quotes for docstrings strings.

**Default value**: `"double"`

**Type**: `"single" | "double"`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-quotes]
docstring-quotes = "single"
```

```
[lint.flake8-quotes]
docstring-quotes = "single"
```

---

#### [`inline-quotes`](#lint_flake8-quotes_inline-quotes)

Quote style to prefer for inline strings (either "single" or
"double").

When using the formatter, ensure that [`format.quote-style`](#format_quote-style) is set to
the same preferred quote style.

**Default value**: `"double"`

**Type**: `"single" | "double"`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-quotes]
inline-quotes = "single"
```

```
[lint.flake8-quotes]
inline-quotes = "single"
```

---

#### [`multiline-quotes`](#lint_flake8-quotes_multiline-quotes)

Quote style to prefer for multiline strings (either "single" or
"double").

When using the formatter, only "double" is compatible, as the formatter
enforces double quotes for multiline strings.

**Default value**: `"double"`

**Type**: `"single" | "double"`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-quotes]
multiline-quotes = "single"
```

```
[lint.flake8-quotes]
multiline-quotes = "single"
```

---

### [`lint.flake8-self`](#lintflake8-self)

Options for the `flake8_self` plugin.

#### [`extend-ignore-names`](#lint_flake8-self_extend-ignore-names)

Additional names to ignore when considering `flake8-self` violations,
in addition to those included in [`ignore-names`](#lint_flake8-self_ignore-names).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-self]
extend-ignore-names = ["_base_manager", "_default_manager",  "_meta"]
```

```
[lint.flake8-self]
extend-ignore-names = ["_base_manager", "_default_manager",  "_meta"]
```

---

#### [`ignore-names`](#lint_flake8-self_ignore-names)

A list of names to ignore when considering `flake8-self` violations.

**Default value**: `["_make", "_asdict", "_replace", "_fields", "_field_defaults", "_name_", "_value_"]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-self]
ignore-names = ["_new"]
```

```
[lint.flake8-self]
ignore-names = ["_new"]
```

---

### [`lint.flake8-tidy-imports`](#lintflake8-tidy-imports)

Options for the `flake8-tidy-imports` plugin

#### [`ban-relative-imports`](#lint_flake8-tidy-imports_ban-relative-imports)

Whether to ban all relative imports (`"all"`), or only those imports
that extend into the parent module or beyond (`"parents"`).

**Default value**: `"parents"`

**Type**: `"parents" | "all"`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-tidy-imports]
# Disallow all relative imports.
ban-relative-imports = "all"
```

```
[lint.flake8-tidy-imports]
# Disallow all relative imports.
ban-relative-imports = "all"
```

---

#### [`banned-api`](#lint_flake8-tidy-imports_banned-api)

Specific modules or module members that may not be imported or accessed.
Note that this rule is only meant to flag accidental uses,
and can be circumvented via `eval` or `importlib`.

**Default value**: `{}`

**Type**: `dict[str, { "msg": str }]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-tidy-imports.banned-api]
"cgi".msg = "The cgi module is deprecated, see https://peps.python.org/pep-0594/#cgi."
"typing.TypedDict".msg = "Use typing_extensions.TypedDict instead."
```

```
[lint.flake8-tidy-imports.banned-api]
"cgi".msg = "The cgi module is deprecated, see https://peps.python.org/pep-0594/#cgi."
"typing.TypedDict".msg = "Use typing_extensions.TypedDict instead."
```

---

#### [`banned-module-level-imports`](#lint_flake8-tidy-imports_banned-module-level-imports)

List of specific modules that may not be imported at module level, and should instead be
imported lazily (e.g., within a function definition, or an `if TYPE_CHECKING:`
block, or some other nested context). This also affects the rule `import-outside-top-level`
if `banned-module-level-imports` is enabled.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-tidy-imports]
# Ban certain modules from being imported at module level, instead requiring
# that they're imported lazily (e.g., within a function definition).
banned-module-level-imports = ["torch", "tensorflow"]
```

```
[lint.flake8-tidy-imports]
# Ban certain modules from being imported at module level, instead requiring
# that they're imported lazily (e.g., within a function definition).
banned-module-level-imports = ["torch", "tensorflow"]
```

---

### [`lint.flake8-type-checking`](#lintflake8-type-checking)

Options for the `flake8-type-checking` plugin

#### [`exempt-modules`](#lint_flake8-type-checking_exempt-modules)

Exempt certain modules from needing to be moved into type-checking
blocks.

**Default value**: `["typing"]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-type-checking]
exempt-modules = ["typing", "typing_extensions"]
```

```
[lint.flake8-type-checking]
exempt-modules = ["typing", "typing_extensions"]
```

---

#### [`quote-annotations`](#lint_flake8-type-checking_quote-annotations)

Whether to add quotes around type annotations, if doing so would allow
the corresponding import to be moved into a type-checking block.

For example, in the following, Python requires that `Sequence` be
available at runtime, despite the fact that it's only used in a type
annotation:

```
from collections.abc import Sequence


def func(value: Sequence[int]) -> None:
    ...
```

In other words, moving `from collections.abc import Sequence` into an
`if TYPE_CHECKING:` block above would cause a runtime error, as the
type would no longer be available at runtime.

By default, Ruff will respect such runtime semantics and avoid moving
the import to prevent such runtime errors.

Setting `quote-annotations` to `true` will instruct Ruff to add quotes
around the annotation (e.g., `"Sequence[int]"`), which in turn enables
Ruff to move the import into an `if TYPE_CHECKING:` block, like so:

```
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence


def func(value: "Sequence[int]") -> None:
    ...
```

Note that this setting has no effect when `from __future__ import annotations`
is present, as `__future__` annotations are always treated equivalently
to quoted annotations. Similarly, this setting has no effect on Python
versions after 3.14 because these annotations are also deferred.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-type-checking]
# Add quotes around type annotations, if doing so would allow
# an import to be moved into a type-checking block.
quote-annotations = true
```

```
[lint.flake8-type-checking]
# Add quotes around type annotations, if doing so would allow
# an import to be moved into a type-checking block.
quote-annotations = true
```

---

#### [`runtime-evaluated-base-classes`](#lint_flake8-type-checking_runtime-evaluated-base-classes)

Exempt classes that list any of the enumerated classes as a base class
from needing to be moved into type-checking blocks.

Common examples include Pydantic's `pydantic.BaseModel` and SQLAlchemy's
`sqlalchemy.orm.DeclarativeBase`, but can also support user-defined
classes that inherit from those base classes. For example, if you define
a common `DeclarativeBase` subclass that's used throughout your project
(e.g., `class Base(DeclarativeBase) ...` in `base.py`), you can add it to
this list (`runtime-evaluated-base-classes = ["base.Base"]`) to exempt
models from being moved into type-checking blocks.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-type-checking]
runtime-evaluated-base-classes = ["pydantic.BaseModel", "sqlalchemy.orm.DeclarativeBase"]
```

```
[lint.flake8-type-checking]
runtime-evaluated-base-classes = ["pydantic.BaseModel", "sqlalchemy.orm.DeclarativeBase"]
```

---

#### [`runtime-evaluated-decorators`](#lint_flake8-type-checking_runtime-evaluated-decorators)

Exempt classes and functions decorated with any of the enumerated
decorators from being moved into type-checking blocks.

Common examples include Pydantic's `@pydantic.validate_call` decorator
(for functions) and attrs' `@attrs.define` decorator (for classes).

This also supports framework decorators like FastAPI's `fastapi.FastAPI.get`
which will work across assignments in the same module.

For example:

```
import fastapi

app = FastAPI("app")

@app.get("/home")
def home() -> str: ...
```

Here `app.get` will correctly be identified as `fastapi.FastAPI.get`.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-type-checking]
runtime-evaluated-decorators = ["pydantic.validate_call", "attrs.define"]
```

```
[lint.flake8-type-checking]
runtime-evaluated-decorators = ["pydantic.validate_call", "attrs.define"]
```

---

#### [`strict`](#lint_flake8-type-checking_strict)

Enforce `TC001`, `TC002`, and `TC003` rules even when valid runtime imports
are present for the same module.

See flake8-type-checking's [strict](https://github.com/snok/flake8-type-checking#strict) option.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-type-checking]
strict = true
```

```
[lint.flake8-type-checking]
strict = true
```

---

### [`lint.flake8-unused-arguments`](#lintflake8-unused-arguments)

Options for the `flake8-unused-arguments` plugin

#### [`ignore-variadic-names`](#lint_flake8-unused-arguments_ignore-variadic-names)

Whether to allow unused variadic arguments, like `*args` and `**kwargs`.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.flake8-unused-arguments]
ignore-variadic-names = true
```

```
[lint.flake8-unused-arguments]
ignore-variadic-names = true
```

---

### [`lint.isort`](#lintisort)

Options for the `isort` plugin.

#### [`case-sensitive`](#lint_isort_case-sensitive)

Sort imports taking into account case sensitivity.

Note that the [`order-by-type`](#lint_isort_order-by-type) setting will
take precedence over this one when enabled.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
case-sensitive = true
```

```
[lint.isort]
case-sensitive = true
```

---

#### [`classes`](#lint_isort_classes)

An override list of tokens to always recognize as a Class for
[`order-by-type`](#lint_isort_order-by-type) regardless of casing.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
classes = ["SVC"]
```

```
[lint.isort]
classes = ["SVC"]
```

---

#### [`combine-as-imports`](#lint_isort_combine-as-imports)

Combines as imports on the same line. See isort's [`combine-as-imports`](https://pycqa.github.io/isort/docs/configuration/options.html#combine-as-imports)
option.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
combine-as-imports = true
```

```
[lint.isort]
combine-as-imports = true
```

---

#### [`constants`](#lint_isort_constants)

An override list of tokens to always recognize as a CONSTANT
for [`order-by-type`](#lint_isort_order-by-type) regardless of casing.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
constants = ["constant"]
```

```
[lint.isort]
constants = ["constant"]
```

---

#### [`default-section`](#lint_isort_default-section)

Define a default section for any imports that don't fit into the specified [`section-order`](#lint_isort_section-order).

**Default value**: `"third-party"`

**Type**: `str`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
default-section = "first-party"
```

```
[lint.isort]
default-section = "first-party"
```

---

#### [`detect-same-package`](#lint_isort_detect-same-package)

Whether to automatically mark imports from within the same package as first-party.
For example, when `detect-same-package = true`, then when analyzing files within the
`foo` package, any imports from within the `foo` package will be considered first-party.

This heuristic is often unnecessary when `src` is configured to detect all first-party
sources; however, if `src` is *not* configured, this heuristic can be useful to detect
first-party imports from *within* (but not *across*) first-party packages.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
detect-same-package = false
```

```
[lint.isort]
detect-same-package = false
```

---

#### [`extra-standard-library`](#lint_isort_extra-standard-library)

A list of modules to consider standard-library, in addition to those
known to Ruff in advance.

Supports glob patterns. For more information on the glob syntax, refer
to the [`globset` documentation](https://docs.rs/globset/latest/globset/#syntax).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
extra-standard-library = ["path"]
```

```
[lint.isort]
extra-standard-library = ["path"]
```

---

#### [`force-single-line`](#lint_isort_force-single-line)

Forces all from imports to appear on their own line.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
force-single-line = true
```

```
[lint.isort]
force-single-line = true
```

---

#### [`force-sort-within-sections`](#lint_isort_force-sort-within-sections)

Don't sort straight-style imports (like `import sys`) before from-style
imports (like `from itertools import groupby`). Instead, sort the
imports by module, independent of import style.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
force-sort-within-sections = true
```

```
[lint.isort]
force-sort-within-sections = true
```

---

#### [`force-to-top`](#lint_isort_force-to-top)

Force specific imports to the top of their appropriate section.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
force-to-top = ["src"]
```

```
[lint.isort]
force-to-top = ["src"]
```

---

#### [`force-wrap-aliases`](#lint_isort_force-wrap-aliases)

Force `import from` statements with multiple members and at least one
alias (e.g., `import A as B`) to wrap such that every line contains
exactly one member. For example, this formatting would be retained,
rather than condensing to a single line:

```
from .utils import (
    test_directory as test_directory,
    test_id as test_id
)
```

Note that this setting is only effective when combined with
`combine-as-imports = true`. When [`combine-as-imports`](#lint_isort_combine-as-imports) isn't
enabled, every aliased `import from` will be given its own line, in
which case, wrapping is not necessary.

When using the formatter, ensure that [`format.skip-magic-trailing-comma`](#format_skip-magic-trailing-comma) is set to `false` (default)
when enabling `force-wrap-aliases` to avoid that the formatter collapses members if they all fit on a single line.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
force-wrap-aliases = true
combine-as-imports = true
```

```
[lint.isort]
force-wrap-aliases = true
combine-as-imports = true
```

---

#### [`forced-separate`](#lint_isort_forced-separate)

A list of modules to separate into auxiliary block(s) of imports,
in the order specified.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
forced-separate = ["tests"]
```

```
[lint.isort]
forced-separate = ["tests"]
```

---

#### [`from-first`](#lint_isort_from-first)

Whether to place `import from` imports before straight imports when sorting.

For example, by default, imports will be sorted such that straight imports appear
before `import from` imports, as in:

```
import os
import sys
from typing import List
```

Setting `from-first = true` will instead sort such that `import from` imports appear
before straight imports, as in:

```
from typing import List
import os
import sys
```

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
from-first = true
```

```
[lint.isort]
from-first = true
```

---

#### [`known-first-party`](#lint_isort_known-first-party)

A list of modules to consider first-party, regardless of whether they
can be identified as such via introspection of the local filesystem.

Supports glob patterns. For more information on the glob syntax, refer
to the [`globset` documentation](https://docs.rs/globset/latest/globset/#syntax).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
known-first-party = ["src"]
```

```
[lint.isort]
known-first-party = ["src"]
```

---

#### [`known-local-folder`](#lint_isort_known-local-folder)

A list of modules to consider being a local folder.
Generally, this is reserved for relative imports (`from . import module`).

Supports glob patterns. For more information on the glob syntax, refer
to the [`globset` documentation](https://docs.rs/globset/latest/globset/#syntax).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
known-local-folder = ["src"]
```

```
[lint.isort]
known-local-folder = ["src"]
```

---

#### [`known-third-party`](#lint_isort_known-third-party)

A list of modules to consider third-party, regardless of whether they
can be identified as such via introspection of the local filesystem.

Supports glob patterns. For more information on the glob syntax, refer
to the [`globset` documentation](https://docs.rs/globset/latest/globset/#syntax).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
known-third-party = ["src"]
```

```
[lint.isort]
known-third-party = ["src"]
```

---

#### [`length-sort`](#lint_isort_length-sort)

Sort imports by their string length, such that shorter imports appear
before longer imports. For example, by default, imports will be sorted
alphabetically, as in:

```
import collections
import os
```

Setting `length-sort = true` will instead sort such that shorter imports
appear before longer imports, as in:

```
import os
import collections
```

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
length-sort = true
```

```
[lint.isort]
length-sort = true
```

---

#### [`length-sort-straight`](#lint_isort_length-sort-straight)

Sort straight imports by their string length. Similar to [`length-sort`](#lint_isort_length-sort),
but applies only to straight imports and doesn't affect `from` imports.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
length-sort-straight = true
```

```
[lint.isort]
length-sort-straight = true
```

---

#### [`lines-after-imports`](#lint_isort_lines-after-imports)

The number of blank lines to place after imports.
Use `-1` for automatic determination.

Ruff uses at most one blank line after imports in typing stub files (files with `.pyi` extension) in accordance to
the typing style recommendations ([source](https://typing.python.org/en/latest/guides/writing_stubs.html#blank-lines)).

When using the formatter, only the values `-1`, `1`, and `2` are compatible because
it enforces at least one empty and at most two empty lines after imports.

**Default value**: `-1`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
# Use a single line after each import block.
lines-after-imports = 1
```

```
[lint.isort]
# Use a single line after each import block.
lines-after-imports = 1
```

---

#### [`lines-between-types`](#lint_isort_lines-between-types)

The number of lines to place between "direct" and `import from` imports.

When using the formatter, only the values `0` and `1` are compatible because
it preserves up to one empty line after imports in nested blocks.

**Default value**: `0`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
# Use a single line between direct and from import.
lines-between-types = 1
```

```
[lint.isort]
# Use a single line between direct and from import.
lines-between-types = 1
```

---

#### [`no-lines-before`](#lint_isort_no-lines-before)

A list of sections that should *not* be delineated from the previous
section via empty lines.

**Default value**: `[]`

**Type**: `list["future" | "standard-library" | "third-party" | "first-party" | "local-folder" | str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
no-lines-before = ["future", "standard-library"]
```

```
[lint.isort]
no-lines-before = ["future", "standard-library"]
```

---

#### [`no-sections`](#lint_isort_no-sections)

Put all imports into the same section bucket.

For example, rather than separating standard library and third-party imports, as in:

```
import os
import sys

import numpy
import pandas
```

Setting `no-sections = true` will instead group all imports into a single section:

```
import numpy
import os
import pandas
import sys
```

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
no-sections = true
```

```
[lint.isort]
no-sections = true
```

---

#### [`order-by-type`](#lint_isort_order-by-type)

Order imports by type, which is determined by case, in addition to
alphabetically.

Note that this option takes precedence over the
[`case-sensitive`](#lint_isort_case-sensitive) setting when enabled.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
order-by-type = true
```

```
[lint.isort]
order-by-type = true
```

---

#### [`relative-imports-order`](#lint_isort_relative-imports-order)

Whether to place "closer" imports (fewer `.` characters, most local)
before "further" imports (more `.` characters, least local), or vice
versa.

The default ("furthest-to-closest") is equivalent to isort's
[`reverse-relative`](https://pycqa.github.io/isort/docs/configuration/options.html#reverse-relative) default (`reverse-relative = false`); setting
this to "closest-to-furthest" is equivalent to isort's
`reverse-relative = true`.

**Default value**: `"furthest-to-closest"`

**Type**: `"furthest-to-closest" | "closest-to-furthest"`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
relative-imports-order = "closest-to-furthest"
```

```
[lint.isort]
relative-imports-order = "closest-to-furthest"
```

---

#### [`required-imports`](#lint_isort_required-imports)

Add the specified import line to all files.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
required-imports = ["from __future__ import annotations"]
```

```
[lint.isort]
required-imports = ["from __future__ import annotations"]
```

---

#### [`section-order`](#lint_isort_section-order)

Override in which order the sections should be output. Can be used to move custom sections.

**Default value**: `["future", "standard-library", "third-party", "first-party", "local-folder"]`

**Type**: `list["future" | "standard-library" | "third-party" | "first-party" | "local-folder" | str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
section-order = ["future", "standard-library", "first-party", "local-folder", "third-party"]
```

```
[lint.isort]
section-order = ["future", "standard-library", "first-party", "local-folder", "third-party"]
```

---

#### [`sections`](#lint_isort_sections)

A list of mappings from section names to modules.

By default, imports are categorized according to their type (e.g., `future`, `third-party`,
and so on). This setting allows you to group modules into custom sections, to augment or
override the built-in sections.

For example, to group all testing utilities, you could create a `testing` section:

```
testing = ["pytest", "hypothesis"]
```

The values in the list are treated as glob patterns. For example, to match all packages in
the LangChain ecosystem (`langchain-core`, `langchain-openai`, etc.):

```
langchain = ["langchain-*"]
```

Custom sections should typically be inserted into the [`section-order`](#lint_isort_section-order) list to ensure that
they're displayed as a standalone group and in the intended order, as in:

```
section-order = [
  "future",
  "standard-library",
  "third-party",
  "first-party",
  "local-folder",
  "testing"
]
```

If a custom section is omitted from [`section-order`](#lint_isort_section-order), imports in that section will be
assigned to the [`default-section`](#lint_isort_default-section) (which defaults to `third-party`).

**Default value**: `{}`

**Type**: `dict[str, list[str]]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort.sections]
# Group all Django imports into a separate section.
"django" = ["django"]
```

```
[lint.isort.sections]
# Group all Django imports into a separate section.
"django" = ["django"]
```

---

#### [`single-line-exclusions`](#lint_isort_single-line-exclusions)

One or more modules to exclude from the single line rule.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
single-line-exclusions = ["os", "json"]
```

```
[lint.isort]
single-line-exclusions = ["os", "json"]
```

---

#### [`split-on-trailing-comma`](#lint_isort_split-on-trailing-comma)

If a comma is placed after the last member in a multi-line import, then
the imports will never be folded into one line.

See isort's [`split-on-trailing-comma`](https://pycqa.github.io/isort/docs/configuration/options.html#split-on-trailing-comma) option.

When using the formatter, ensure that [`format.skip-magic-trailing-comma`](#format_skip-magic-trailing-comma) is set to `false` (default) when enabling `split-on-trailing-comma`
to avoid that the formatter removes the trailing commas.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
split-on-trailing-comma = false
```

```
[lint.isort]
split-on-trailing-comma = false
```

---

#### [`variables`](#lint_isort_variables)

An override list of tokens to always recognize as a var
for [`order-by-type`](#lint_isort_order-by-type) regardless of casing.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.isort]
variables = ["VAR"]
```

```
[lint.isort]
variables = ["VAR"]
```

---

### [`lint.mccabe`](#lintmccabe)

Options for the `mccabe` plugin.

#### [`max-complexity`](#lint_mccabe_max-complexity)

The maximum McCabe complexity to allow before triggering `C901` errors.

**Default value**: `10`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.mccabe]
# Flag errors (`C901`) whenever the complexity level exceeds 5.
max-complexity = 5
```

```
[lint.mccabe]
# Flag errors (`C901`) whenever the complexity level exceeds 5.
max-complexity = 5
```

---

### [`lint.pep8-naming`](#lintpep8-naming)

Options for the `pep8-naming` plugin.

#### [`classmethod-decorators`](#lint_pep8-naming_classmethod-decorators)

A list of decorators that, when applied to a method, indicate that the
method should be treated as a class method (in addition to the builtin
`@classmethod`).

For example, Ruff will expect that any method decorated by a decorator
in this list takes a `cls` argument as its first argument.

Expects to receive a list of fully-qualified names (e.g., `pydantic.validator`,
rather than `validator`) or alternatively a plain name which is then matched against
the last segment in case the decorator itself consists of a dotted name.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pep8-naming]
classmethod-decorators = [
    # Allow Pydantic's `@validator` decorator to trigger class method treatment.
    "pydantic.validator",
    # Allow SQLAlchemy's dynamic decorators, like `@field.expression`, to trigger class method treatment.
    "declared_attr",
    "expression",
    "comparator",
]
```

```
[lint.pep8-naming]
classmethod-decorators = [
    # Allow Pydantic's `@validator` decorator to trigger class method treatment.
    "pydantic.validator",
    # Allow SQLAlchemy's dynamic decorators, like `@field.expression`, to trigger class method treatment.
    "declared_attr",
    "expression",
    "comparator",
]
```

---

#### [`extend-ignore-names`](#lint_pep8-naming_extend-ignore-names)

Additional names (or patterns) to ignore when considering `pep8-naming` violations,
in addition to those included in [`ignore-names`](#lint_pep8-naming_ignore-names).

Supports glob patterns. For example, to ignore all names starting with `test_`
or ending with `_test`, you could use `ignore-names = ["test_*", "*_test"]`.
For more information on the glob syntax, refer to the [`globset` documentation](https://docs.rs/globset/latest/globset/#syntax).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pep8-naming]
extend-ignore-names = ["callMethod"]
```

```
[lint.pep8-naming]
extend-ignore-names = ["callMethod"]
```

---

#### [`ignore-names`](#lint_pep8-naming_ignore-names)

A list of names (or patterns) to ignore when considering `pep8-naming` violations.

Supports glob patterns. For example, to ignore all names starting with `test_`
or ending with `_test`, you could use `ignore-names = ["test_*", "*_test"]`.
For more information on the glob syntax, refer to the [`globset` documentation](https://docs.rs/globset/latest/globset/#syntax).

**Default value**: `["setUp", "tearDown", "setUpClass", "tearDownClass", "setUpModule", "tearDownModule", "asyncSetUp", "asyncTearDown", "setUpTestData", "failureException", "longMessage", "maxDiff"]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pep8-naming]
ignore-names = ["callMethod"]
```

```
[lint.pep8-naming]
ignore-names = ["callMethod"]
```

---

#### [`staticmethod-decorators`](#lint_pep8-naming_staticmethod-decorators)

A list of decorators that, when applied to a method, indicate that the
method should be treated as a static method (in addition to the builtin
`@staticmethod`).

For example, Ruff will expect that any method decorated by a decorator
in this list has no `self` or `cls` argument.

Expects to receive a list of fully-qualified names (e.g., `belay.Device.teardown`,
rather than `teardown`) or alternatively a plain name which is then matched against
the last segment in case the decorator itself consists of a dotted name.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pep8-naming]
# Allow Belay's `@Device.teardown` decorator to trigger static method treatment.
staticmethod-decorators = ["belay.Device.teardown"]
```

```
[lint.pep8-naming]
# Allow Belay's `@Device.teardown` decorator to trigger static method treatment.
staticmethod-decorators = ["belay.Device.teardown"]
```

---

### [`lint.pycodestyle`](#lintpycodestyle)

Options for the `pycodestyle` plugin.

#### [`ignore-overlong-task-comments`](#lint_pycodestyle_ignore-overlong-task-comments)

Whether line-length violations (`E501`) should be triggered for
comments starting with [`task-tags`](#lint_task-tags) (by default: "TODO", "FIXME",
and "XXX").

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pycodestyle]
ignore-overlong-task-comments = true
```

```
[lint.pycodestyle]
ignore-overlong-task-comments = true
```

---

#### [`max-doc-length`](#lint_pycodestyle_max-doc-length)

The maximum line length to allow for [`doc-line-too-long`](https://docs.astral.sh/ruff/rules/doc-line-too-long/) violations within
documentation (`W505`), including standalone comments. By default,
this is set to `null` which disables reporting violations.

The length is determined by the number of characters per line, except for lines containing Asian characters or emojis.
For these lines, the [unicode width](https://unicode.org/reports/tr11/) of each character is added up to determine the length.

See the [`doc-line-too-long`](https://docs.astral.sh/ruff/rules/doc-line-too-long/) rule for more information.

**Default value**: `null`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pycodestyle]
max-doc-length = 88
```

```
[lint.pycodestyle]
max-doc-length = 88
```

---

#### [`max-line-length`](#lint_pycodestyle_max-line-length)

The maximum line length to allow for [`line-too-long`](https://docs.astral.sh/ruff/rules/line-too-long/) violations. By default,
this is set to the value of the [`line-length`](#line-length) option.

Use this option when you want to detect extra-long lines that the formatter can't automatically split by setting
`pycodestyle.line-length` to a value larger than [`line-length`](#line-length).

```
# The formatter wraps lines at a length of 88.
line-length = 88

[pycodestyle]
# E501 reports lines that exceed the length of 100.
max-line-length = 100
```

The length is determined by the number of characters per line, except for lines containing East Asian characters or emojis.
For these lines, the [unicode width](https://unicode.org/reports/tr11/) of each character is added up to determine the length.

See the [`line-too-long`](https://docs.astral.sh/ruff/rules/line-too-long/) rule for more information.

**Default value**: `null`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pycodestyle]
max-line-length = 100
```

```
[lint.pycodestyle]
max-line-length = 100
```

---

### [`lint.pydoclint`](#lintpydoclint)

Options for the `pydoclint` plugin.

#### [`ignore-one-line-docstrings`](#lint_pydoclint_ignore-one-line-docstrings)

Skip docstrings which fit on a single line.

Note: The corresponding setting in `pydoclint`
is named `skip-checking-short-docstrings`.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pydoclint]
# Skip docstrings which fit on a single line.
ignore-one-line-docstrings = true
```

```
[lint.pydoclint]
# Skip docstrings which fit on a single line.
ignore-one-line-docstrings = true
```

---

### [`lint.pydocstyle`](#lintpydocstyle)

Options for the `pydocstyle` plugin.

#### [`convention`](#lint_pydocstyle_convention)

Whether to use Google-style, NumPy-style conventions, or the [PEP 257](https://peps.python.org/pep-0257/)
defaults when analyzing docstring sections.

Enabling a convention will disable all rules that are not included in
the specified convention. As such, the intended workflow is to enable a
convention and then selectively enable or disable any additional rules
on top of it.

For example, to use Google-style conventions but avoid requiring
documentation for every function parameter:

```
[tool.ruff.lint]
# Enable all `pydocstyle` rules, limiting to those that adhere to the
# Google convention via `convention = "google"`, below.
select = ["D"]

# On top of the Google convention, disable `D417`, which requires
# documentation for every function parameter.
ignore = ["D417"]

[tool.ruff.lint.pydocstyle]
convention = "google"
```

To enable an additional rule that's excluded from the convention,
select the desired rule via its fully qualified rule code (e.g.,
`D400` instead of `D4` or `D40`):

```
[tool.ruff.lint]
# Enable D400 on top of the Google convention.
extend-select = ["D400"]

[tool.ruff.lint.pydocstyle]
convention = "google"
```

**Default value**: `null`

**Type**: `"google" | "numpy" | "pep257"`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pydocstyle]
# Use Google-style docstrings.
convention = "google"
```

```
[lint.pydocstyle]
# Use Google-style docstrings.
convention = "google"
```

---

#### [`ignore-decorators`](#lint_pydocstyle_ignore-decorators)

Ignore docstrings for functions or methods decorated with the
specified fully-qualified decorators.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pydocstyle]
ignore-decorators = ["typing.overload"]
```

```
[lint.pydocstyle]
ignore-decorators = ["typing.overload"]
```

---

#### [`ignore-var-parameters`](#lint_pydocstyle_ignore-var-parameters)

If set to `true`, ignore missing documentation for `*args` and `**kwargs` parameters.

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pydocstyle]
ignore-var-parameters = true
```

```
[lint.pydocstyle]
ignore-var-parameters = true
```

---

#### [`property-decorators`](#lint_pydocstyle_property-decorators)

A list of decorators that, when applied to a method, indicate that the
method should be treated as a property (in addition to the builtin
`@property` and standard-library `@functools.cached_property`).

For example, Ruff will expect that any method decorated by a decorator
in this list can use a non-imperative summary line.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pydocstyle]
property-decorators = ["gi.repository.GObject.Property"]
```

```
[lint.pydocstyle]
property-decorators = ["gi.repository.GObject.Property"]
```

---

### [`lint.pyflakes`](#lintpyflakes)

Options for the `pyflakes` plugin.

#### [`allowed-unused-imports`](#lint_pyflakes_allowed-unused-imports)

A list of modules to ignore when considering unused imports.

Used to prevent violations for specific modules that are known to have side effects on
import (e.g., `hvplot.pandas`).

Modules in this list are expected to be fully-qualified names (e.g., `hvplot.pandas`). Any
submodule of a given module will also be ignored (e.g., given `hvplot`, `hvplot.pandas`
will also be ignored).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pyflakes]
allowed-unused-imports = ["hvplot.pandas"]
```

```
[lint.pyflakes]
allowed-unused-imports = ["hvplot.pandas"]
```

---

#### [`extend-generics`](#lint_pyflakes_extend-generics)

Additional functions or classes to consider generic, such that any
subscripts should be treated as type annotation (e.g., `ForeignKey` in
`django.db.models.ForeignKey["User"]`.

Expects to receive a list of fully-qualified names (e.g., `django.db.models.ForeignKey`,
rather than `ForeignKey`).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pyflakes]
extend-generics = ["django.db.models.ForeignKey"]
```

```
[lint.pyflakes]
extend-generics = ["django.db.models.ForeignKey"]
```

---

### [`lint.pylint`](#lintpylint)

Options for the `pylint` plugin.

#### [`allow-dunder-method-names`](#lint_pylint_allow-dunder-method-names)

Dunder methods name to allow, in addition to the default set from the
Python standard library (see `PLW3201`).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pylint]
allow-dunder-method-names = ["__tablename__", "__table_args__"]
```

```
[lint.pylint]
allow-dunder-method-names = ["__tablename__", "__table_args__"]
```

---

#### [`allow-magic-value-types`](#lint_pylint_allow-magic-value-types)

Constant types to ignore when used as "magic values" (see `PLR2004`).

**Default value**: `["str", "bytes"]`

**Type**: `list["str" | "bytes" | "complex" | "float" | "int"]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pylint]
allow-magic-value-types = ["int"]
```

```
[lint.pylint]
allow-magic-value-types = ["int"]
```

---

#### [`max-args`](#lint_pylint_max-args)

Maximum number of arguments allowed for a function or method definition
(see `PLR0913`).

**Default value**: `5`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pylint]
max-args = 10
```

```
[lint.pylint]
max-args = 10
```

---

#### [`max-bool-expr`](#lint_pylint_max-bool-expr)

Maximum number of Boolean expressions allowed within a single `if` statement
(see `PLR0916`).

**Default value**: `5`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pylint]
max-bool-expr = 10
```

```
[lint.pylint]
max-bool-expr = 10
```

---

#### [`max-branches`](#lint_pylint_max-branches)

Maximum number of branches allowed for a function or method body (see `PLR0912`).

**Default value**: `12`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pylint]
max-branches = 15
```

```
[lint.pylint]
max-branches = 15
```

---

#### [`max-locals`](#lint_pylint_max-locals)

Maximum number of local variables allowed for a function or method body (see `PLR0914`).

**Default value**: `15`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pylint]
max-locals = 20
```

```
[lint.pylint]
max-locals = 20
```

---

#### [`max-nested-blocks`](#lint_pylint_max-nested-blocks)

Maximum number of nested blocks allowed within a function or method body
(see `PLR1702`).

**Default value**: `5`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pylint]
max-nested-blocks = 10
```

```
[lint.pylint]
max-nested-blocks = 10
```

---

#### [`max-positional-args`](#lint_pylint_max-positional-args)

Maximum number of positional arguments allowed for a function or method definition
(see `PLR0917`).

If not specified, defaults to the value of `max-args`.

**Default value**: `5`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pylint]
max-positional-args = 3
```

```
[lint.pylint]
max-positional-args = 3
```

---

#### [`max-public-methods`](#lint_pylint_max-public-methods)

Maximum number of public methods allowed for a class (see `PLR0904`).

**Default value**: `20`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pylint]
max-public-methods = 30
```

```
[lint.pylint]
max-public-methods = 30
```

---

#### [`max-returns`](#lint_pylint_max-returns)

Maximum number of return statements allowed for a function or method
body (see `PLR0911`)

**Default value**: `6`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pylint]
max-returns = 10
```

```
[lint.pylint]
max-returns = 10
```

---

#### [`max-statements`](#lint_pylint_max-statements)

Maximum number of statements allowed for a function or method body (see `PLR0915`).

**Default value**: `50`

**Type**: `int`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pylint]
max-statements = 75
```

```
[lint.pylint]
max-statements = 75
```

---

### [`lint.pyupgrade`](#lintpyupgrade)

Options for the `pyupgrade` plugin.

#### [`keep-runtime-typing`](#lint_pyupgrade_keep-runtime-typing)

Whether to avoid [PEP 585](https://peps.python.org/pep-0585/) (`List[int]` -> `list[int]`) and [PEP 604](https://peps.python.org/pep-0604/)
(`Union[str, int]` -> `str | int`) rewrites even if a file imports
`from __future__ import annotations`.

This setting is only applicable when the target Python version is below
3.9 and 3.10 respectively, and is most commonly used when working with
libraries like Pydantic and FastAPI, which rely on the ability to parse
type annotations at runtime. The use of `from __future__ import annotations`
causes Python to treat the type annotations as strings, which typically
allows for the use of language features that appear in later Python
versions but are not yet supported by the current version (e.g., `str |
int`). However, libraries that rely on runtime type annotations will
break if the annotations are incompatible with the current Python
version.

For example, while the following is valid Python 3.8 code due to the
presence of `from __future__ import annotations`, the use of `str | int`
prior to Python 3.10 will cause Pydantic to raise a `TypeError` at
runtime:

```
from __future__ import annotations

import pydantic

class Foo(pydantic.BaseModel):
    bar: str | int
```

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.pyupgrade]
# Preserve types, even if a file imports `from __future__ import annotations`.
keep-runtime-typing = true
```

```
[lint.pyupgrade]
# Preserve types, even if a file imports `from __future__ import annotations`.
keep-runtime-typing = true
```

---

### [`lint.ruff`](#lintruff)

Options for the `ruff` plugin

#### [`allowed-markup-calls`](#lint_ruff_allowed-markup-calls)

Deprecated

This option has been deprecated in 0.10.0. The `allowed-markup-names` option has been moved to the `flake8-bandit` section of the configuration.

A list of callable names, whose result may be safely passed into
[`markupsafe.Markup`](https://markupsafe.palletsprojects.com/en/stable/escaping/#markupsafe.Markup).

Expects to receive a list of fully-qualified names (e.g., `bleach.clean`, rather than `clean`).

This setting helps you avoid false positives in code like:

```
from bleach import clean
from markupsafe import Markup

cleaned_markup = Markup(clean(some_user_input))
```

Where the use of [`bleach.clean`](https://bleach.readthedocs.io/en/latest/clean.html)
usually ensures that there's no XSS vulnerability.

Although it is not recommended, you may also use this setting to whitelist other
kinds of calls, e.g. calls to i18n translation functions, where how safe that is
will depend on the implementation and how well the translations are audited.

Another common use-case is to wrap the output of functions that generate markup
like [`xml.etree.ElementTree.tostring`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.tostring)
or template rendering engines where sanitization of potential user input is either
already baked in or has to happen before rendering.

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.ruff]
allowed-markup-calls = ["bleach.clean", "my_package.sanitize"]
```

```
[lint.ruff]
allowed-markup-calls = ["bleach.clean", "my_package.sanitize"]
```

---

#### [`extend-markup-names`](#lint_ruff_extend-markup-names)

Deprecated

This option has been deprecated in 0.10.0. The `extend-markup-names` option has been moved to the `flake8-bandit` section of the configuration.

A list of additional callable names that behave like
[`markupsafe.Markup`](https://markupsafe.palletsprojects.com/en/stable/escaping/#markupsafe.Markup).

Expects to receive a list of fully-qualified names (e.g., `webhelpers.html.literal`, rather than
`literal`).

**Default value**: `[]`

**Type**: `list[str]`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.ruff]
extend-markup-names = ["webhelpers.html.literal", "my_package.Markup"]
```

```
[lint.ruff]
extend-markup-names = ["webhelpers.html.literal", "my_package.Markup"]
```

---

#### [`parenthesize-tuple-in-subscript`](#lint_ruff_parenthesize-tuple-in-subscript)

Whether to prefer accessing items keyed by tuples with
parentheses around the tuple (see `RUF031`).

**Default value**: `false`

**Type**: `bool`

**Example usage**:

pyproject.tomlruff.toml

```
[tool.ruff.lint.ruff]
# Make it a violation to use a tuple in a subscript without parentheses.
parenthesize-tuple-in-subscript = true
```

```
[lint.ruff]
# Make it a violation to use a tuple in a subscript without parentheses.
parenthesize-tuple-in-subscript = true
```

---