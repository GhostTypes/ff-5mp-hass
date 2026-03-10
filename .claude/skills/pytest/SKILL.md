---
name: pytest
description: Comprehensive pytest testing framework skill for Python. Use when working with pytest tests, fixtures, parametrization, markers, assertions, configuration, plugins, or test discovery. Covers pytest 9.x with full API reference, how-to guides, best practices, and examples for writing, running, and debugging Python tests.
---

# pytest Testing Framework

pytest is a mature, full-featured Python testing framework that makes it easy to write small, readable tests that can scale to support complex functional testing.

## Quick Start

### Installation

```bash
pip install -U pytest
pytest --version
```

### Basic Test

```python
# test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
```

Run with `pytest` - it auto-discovers `test_*.py` and `*_test.py` files.

### Test Discovery Rules

- Files: `test_*.py` or `*_test.py`
- Functions: `test_` prefix outside classes
- Classes: `Test` prefix (no `__init__`)
- Methods: `test_` prefix in `Test` classes

## Core Concepts

### Fixtures

Fixtures provide fixed baseline for tests:

```python
import pytest

@pytest.fixture
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
```

**Scopes:** `function` (default), `class`, `module`, `package`, `session`

### Parametrization

Run same test with multiple inputs:

```python
@pytest.mark.parametrize("input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    pytest.param("6*9", 42, marks=pytest.mark.xfail),
])
def test_eval(input, expected):
    assert eval(input) == expected
```

### Markers

```python
@pytest.mark.skip(reason="not implemented")
@pytest.mark.skipif(sys.platform == "win32", reason="linux only")
@pytest.mark.xfail(reason="known bug")
@pytest.mark.slow  # custom marker
def test_something():
    pass
```

Run by marker: `pytest -m slow`

### Assertions

```python
# Basic assert with introspection
assert func(3) == 5

# Exception testing
with pytest.raises(ValueError, match="invalid"):
    raise ValueError("invalid input")

# Floating point comparison
assert 0.1 + 0.2 == pytest.approx(0.3)

# Warnings
with pytest.warns(UserWarning):
    warnings.warn("hello", UserWarning)
```

## CLI Reference

```bash
pytest                           # run all tests
pytest test_mod.py               # specific file
pytest tests/                    # directory
pytest -k "MyClass and not method"  # keyword filter
pytest -m slow                   # by marker
pytest -x                        # stop on first failure
pytest -v                        # verbose
pytest -s                        # show stdout
pytest --tb=short                # shorter traceback
pytest --fixtures                # list fixtures
pytest --collect-only            # show tests without running
pytest -n 4                      # parallel (needs pytest-xdist)
```

## Documentation Index

### Getting Started
- [getting-started.md](references/getting-started.md) - Installation, first test, grouping tests, temporary directories

### How-To Guides

**Testing Basics:**
- [how-to/usage.md](references/how-to/usage.md) - Invoking pytest, selecting tests, CLI options
- [how-to/assert.md](references/how-to/assert.md) - Assertions, exceptions, warnings, approx comparisons
- [how-to/fixtures.md](references/how-to/fixtures.md) - Complete fixture guide: scopes, teardown, parametrization, factories
- [how-to/parametrize.md](references/how-to/parametrize.md) - Parametrizing tests and fixtures
- [how-to/mark.md](references/how-to/mark.md) - Custom markers, registering marks
- [how-to/skipping.md](references/how-to/skipping.md) - skip, skipif, xfail markers

**Test Organization:**
- [how-to/tmp_path.md](references/how-to/tmp_path.md) - Temporary directories and files
- [how-to/monkeypatch.md](references/how-to/monkeypatch.md) - Monkeypatching for testing
- [how-to/cache.md](references/how-to/cache.md) - Caching values across test runs
- [how-to/doctest.md](references/how-to/doctest.md) - Running doctests with pytest

**Output & Capture:**
- [how-to/capture-stdout-stderr.md](references/how-to/capture-stdout-stderr.md) - Capturing output
- [how-to/capture-warnings.md](references/how-to/capture-warnings.md) - Capturing warnings
- [how-to/logging.md](references/how-to/logging.md) - Logging during tests
- [how-to/output.md](references/how-to/output.md) - Managing test output
- [how-to/failures.md](references/how-to/failures.md) - Handling test failures

**Integration:**
- [how-to/unittest.md](references/how-to/unittest.md) - Running unittest tests
- [how-to/existingtestsuite.md](references/how-to/existingtestsuite.md) - Migrating existing test suites
- [how-to/xunit_setup.md](references/how-to/xunit_setup.md) - xUnit-style setup/teardown
- [how-to/subtests.md](references/how-to/subtests.md) - Subtest support

**Plugins:**
- [how-to/plugins.md](references/how-to/plugins.md) - Using pytest plugins
- [how-to/writing_plugins.md](references/how-to/writing_plugins.md) - Writing plugins
- [how-to/writing_hook_functions.md](references/how-to/writing_hook_functions.md) - Hook functions

**Other:**
- [how-to/bash-completion.md](references/how-to/bash-completion.md) - Bash completion setup

### Reference

- [reference/reference.md](references/reference/reference.md) - Complete API reference
- [reference/fixtures.md](references/reference/fixtures.md) - Built-in fixtures reference
- [reference/customize.md](references/reference/customize.md) - Configuration and customization
- [reference/exit-codes.md](references/reference/exit-codes.md) - Exit codes reference
- [reference/plugin_list.md](references/reference/plugin_list.md) - Plugin list

### Explanation

- [explanation/fixtures.md](references/explanation/fixtures.md) - Fixture concepts explained
- [explanation/anatomy.md](references/explanation/anatomy.md) - Anatomy of a test
- [explanation/goodpractices.md](references/explanation/goodpractices.md) - Best practices, project layout, import modes
- [explanation/flaky.md](references/explanation/flaky.md) - Dealing with flaky tests
- [explanation/ci.md](references/explanation/ci.md) - CI integration
- [explanation/pythonpath.md](references/explanation/pythonpath.md) - Python path handling
- [explanation/types.md](references/explanation/types.md) - Type annotations in pytest

### Examples

- [example/simple.md](references/example/simple.md) - Simple test examples
- [example/parametrize.md](references/example/parametrize.md) - Parametrization examples
- [example/markers.md](references/example/markers.md) - Marker examples
- [example/pythoncollection.md](references/example/pythoncollection.md) - Collection examples
- [example/customdirectory.md](references/example/customdirectory.md) - Custom directory layouts
- [example/nonpython.md](references/example/nonpython.md) - Non-Python tests
- [example/reportingdemo.md](references/example/reportingdemo.md) - Reporting demonstration
- [example/special.md](references/example/special.md) - Special use cases

## Common Patterns

### conftest.py

Share fixtures across test files:

```python
# tests/conftest.py
import pytest

@pytest.fixture
def database():
    db = Database()
    yield db
    db.close()
```

### Yield Fixture (Teardown)

```python
@pytest.fixture
def resource():
    r = acquire_resource()
    yield r
    release_resource(r)  # teardown
```

### Fixture Factories

```python
@pytest.fixture
def make_customer():
    created = []
    def _make(name):
        c = Customer(name)
        created.append(c)
        return c
    yield _make
    for c in created:
        c.delete()
```

### Autouse Fixtures

```python
@pytest.fixture(autouse=True)
def clean_db(db):
    yield
    db.rollback()
```

## Configuration

### pyproject.toml

```toml
[pytest]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short"
markers = [
    "slow: marks tests as slow",
    "integration: integration tests",
]
```

### pytest.ini

```ini
[pytest]
testpaths = tests
addopts = -v
```

## Official Resources

- Documentation: https://docs.pytest.org/
- PyPI: https://pypi.org/project/pytest/
- GitHub: https://github.com/pytest-dev/pytest/
