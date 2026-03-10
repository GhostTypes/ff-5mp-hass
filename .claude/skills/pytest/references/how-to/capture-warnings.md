.. _`warnings`:

## How to capture warnings

Starting from version `3.1`, pytest now automatically catches warnings during test execution
and displays them at the end of the session:

```python

    # content of test_show_warnings.py
    import warnings

    def api_v1():
        warnings.warn(UserWarning("api v1, should use functions from v2"))
        return 1

    def test_one():
        assert api_v1() == 1

```

Running pytest now produces this output:

```

    $ pytest test_show_warnings.py
    =========================== test session starts ============================
    platform linux -- Python 3.x.y, pytest-9.x.y, pluggy-1.x.y
    rootdir: /home/sweet/project
    collected 1 item

    test_show_warnings.py .                                              [100%]

    ============================= warnings summary =============================
    test_show_warnings.py::test_one
      /home/sweet/project/test_show_warnings.py:5: UserWarning: api v1, should use functions from v2
        warnings.warn(UserWarning("api v1, should use functions from v2"))

    -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
    ======================= 1 passed, 1 warning in 0.12s =======================

```

.. _`controlling-warnings`:

## Controlling warnings

Similar to Python's `warning filter`_ and [-W option](python:-W) flag, pytest provides
its own `-W` flag to control which warnings are ignored, displayed, or turned into
errors. See the `warning filter`_ documentation for more
advanced use-cases.

.. _`warning filter`: https://docs.python.org/3/library/warnings.html#warning-filter

This code sample shows how to treat any `UserWarning` category class of warning
as an error:

```

    $ pytest -q test_show_warnings.py -W error::UserWarning
    F                                                                    [100%]
    ================================= FAILURES =================================
    _________________________________ test_one _________________________________

        def test_one():
    >       assert api_v1() == 1
                   ^^^^^^^^

    test_show_warnings.py:10:
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

        def api_v1():
    >       warnings.warn(UserWarning("api v1, should use functions from v2"))
    E       UserWarning: api v1, should use functions from v2

    test_show_warnings.py:5: UserWarning
    ========================= short test summary info ==========================
    FAILED test_show_warnings.py::test_one - UserWarning: api v1, should use ...
    1 failed in 0.12s

```

The same option can be set in the configuration file using the
`filterwarnings` configuration option. For example, the configuration below will ignore all
user warnings and specific deprecation warnings matching a regex, but will transform
all other warnings into errors.

```toml

        [pytest]
        filterwarnings = [
            'error',
            'ignore::UserWarning',
            # Note the use of single quote below to denote "raw" strings in TOML.
            'ignore:function ham\(\) is deprecated:DeprecationWarning',
        ]

```

```ini

        [pytest]
        filterwarnings =
            error
            ignore::UserWarning
            ignore:function ham\(\) is deprecated:DeprecationWarning

```

When a warning matches more than one option in the list, the action for the last matching option
is performed.

> **NOTE:**
> The ``-W`` flag and the :confval:`filterwarnings` configuration option use warning filters that are
> similar in structure, but each configuration option interprets its filter
> differently. For example, *message* in ``filterwarnings`` is a string containing a
> regular expression that the start of the warning message must match,
> case-insensitively, while *message* in ``-W`` is a literal string that the start of
> the warning message must contain (case-insensitively), ignoring any whitespace at
> the start or end of message. Consult the `warning filter`_ documentation for more
> details.

.. _`filterwarnings`:

## `@pytest.mark.filterwarnings`

You can use the `@pytest.mark.filterwarnings` mark to add warning filters to specific test items,
allowing you to have finer control of which warnings should be captured at test, class or
even module level:

```python

    import warnings

    def api_v1():
        warnings.warn(UserWarning("api v1, should use functions from v2"))
        return 1

    @pytest.mark.filterwarnings("ignore:api v1")
    def test_one():
        assert api_v1() == 1

```

You can specify multiple filters with separate decorators:

```python

    # Ignore "api v1" warnings, but fail on all other warnings
    @pytest.mark.filterwarnings("ignore:api v1")
    @pytest.mark.filterwarnings("error")
    def test_one():
        assert api_v1() == 1

```

> **IMPORTANT:**
> Regarding decorator order and filter precedence:
> it's important to remember that decorators are evaluated in reverse order,
> so you have to list the warning filters in the reverse order
> compared to traditional :py:func:`warnings.filterwarnings` and :option:`-W option <python:-W>` usage.
> This means in practice that filters from earlier :ref:`@pytest.mark.filterwarnings <pytest.mark.filterwarnings ref>` decorators
> take precedence over filters from later decorators, as illustrated in the example above.

Filters applied using a mark take precedence over filters passed on the command line or configured
by the `filterwarnings` configuration option.

You may apply a filter to all tests of a class by using the `filterwarnings` mark as a class
decorator or to all tests in a module by setting the `pytestmark` variable:

```python

    # turns all warnings into errors for this module
    pytestmark = pytest.mark.filterwarnings("error")

```

> **NOTE:**
> If you want to apply multiple filters
> (by assigning a list of :ref:`filterwarnings <pytest.mark.filterwarnings ref>` mark to :globalvar:`pytestmark`),
> you must use the traditional :py:func:`warnings.filterwarnings` ordering approach (later filters take precedence),
> which is the reverse of the decorator approach mentioned above.

*Credits go to Florian Schulze for the reference implementation in the* `pytest-warnings`_
*plugin.*

.. _`pytest-warnings`: https://github.com/fschulze/pytest-warnings

## Disabling warnings summary

Although not recommended, you can use the `--disable-warnings` command-line option to suppress the
warning summary entirely from the test run output.

## Disabling warning capture entirely

This plugin is enabled by default but can be disabled entirely in your configuration file with:

```toml

        [pytest]
        addopts = ["-p", "no:warnings"]

```

```ini

        [pytest]
        addopts = -p no:warnings

```

Or passing `-p no:warnings` in the command-line. This might be useful if your test suite handles warnings
using an external system.

.. _`deprecation-warnings`:

## DeprecationWarning and PendingDeprecationWarning

By default pytest will display `DeprecationWarning` and `PendingDeprecationWarning` warnings from
user code and third-party libraries, as recommended by `565`.
This helps users keep their code modern and avoid breakages when deprecated warnings are effectively removed.

However, in the specific case where users capture any type of warnings in their test, either with
`pytest.warns()`, `pytest.deprecated_call()` or using the `recwarn` fixture,
no warning will be displayed at all.

Sometimes it is useful to hide some specific deprecation warnings that happen in code that you have no control over
(such as third-party libraries), in which case you might use the warning filters options (configuration or marks) to ignore
those warnings.

For example:

```toml

        [pytest]
        filterwarnings = [
            'ignore:.*U.*mode is deprecated:DeprecationWarning',
        ]

```

```ini

        [pytest]
        filterwarnings =
            ignore:.*U.*mode is deprecated:DeprecationWarning

```

This will ignore all warnings of type `DeprecationWarning` where the start of the message matches
the regular expression `".*U.*mode is deprecated"`.

See `@pytest.mark.filterwarnings` and
`Controlling warnings` for more examples.

> **NOTE:**
> If warnings are configured at the interpreter level, using
> the :envvar:`python:PYTHONWARNINGS` environment variable or the
> ``-W`` command-line option, pytest will not configure any filters by default.
> Also pytest doesn't follow :pep:`565` suggestion of resetting all warning filters because
> it might break test suites that configure warning filters themselves
> by calling :func:`warnings.simplefilter` (see :issue:`2430` for an example of that).

.. _`ensuring a function triggers a deprecation warning`:

## Ensuring code triggers a deprecation warning

You can also use `pytest.deprecated_call()` for checking
that a certain function call triggers a `DeprecationWarning`, `PendingDeprecationWarning` or
`FutureWarning`:

```python

    import pytest

    def test_myfunction_deprecated():
        with pytest.deprecated_call():
            myfunction(17)

```

This test will fail if `myfunction` does not issue a deprecation warning
when called with a `17` argument.

.. _`asserting warnings`:

.. _`asserting warnings with the warns function`:

## Asserting warnings with the warns function

You can check that code raises a particular warning using `pytest.warns()`,
which works in a similar manner to `raises` (except that
`raises` does not capture all exceptions, only the
`expected_exception`):

```python

    import warnings

    import pytest

    def test_warning():
        with pytest.warns(UserWarning):
            warnings.warn("my warning", UserWarning)

```

The test will fail if the warning in question is not raised. Use the keyword
argument `match` to assert that the warning matches a text or regex.
To match a literal string that may contain regular expression metacharacters like `(` or `.`, the pattern can
first be escaped with `re.escape`.

Some examples:

```pycon

    >>> with warns(UserWarning, match="must be 0 or None"):
    ...     warnings.warn("value must be 0 or None", UserWarning)
    ...

    >>> with warns(UserWarning, match=r"must be \d+$"):
    ...     warnings.warn("value must be 42", UserWarning)
    ...

    >>> with warns(UserWarning, match=r"must be \d+$"):
    ...     warnings.warn("this is not here", UserWarning)
    ...
    Traceback (most recent call last):
      ...
    Failed: DID NOT WARN. No warnings of type ...UserWarning... were emitted...

    >>> with warns(UserWarning, match=re.escape("issue with foo() func")):
    ...     warnings.warn("issue with foo() func")
    ...

```

You can also call `pytest.warns()` on a function or code string:

```python

    pytest.warns(expected_warning, func, *args, **kwargs)
    pytest.warns(expected_warning, "func(*args, **kwargs)")

```

The function also returns a list of all raised warnings (as
`warnings.WarningMessage` objects), which you can query for
additional information:

```python

    with pytest.warns(RuntimeWarning) as record:
        warnings.warn("another warning", RuntimeWarning)

    # check that only one warning was raised
    assert len(record) == 1
    # check that the message matches
    assert record[0].message.args[0] == "another warning"

```

Alternatively, you can examine raised warnings in detail using the
`recwarn` fixture (see `below`).

The `recwarn` fixture automatically ensures to reset the warnings
filter at the end of the test, so no global state is leaked.

.. _`recording warnings`:

## Recording warnings

You can record raised warnings either using the `pytest.warns()` context manager or with
the `recwarn` fixture.

To record with `pytest.warns()` without asserting anything about the warnings,
pass no arguments as the expected warning type and it will default to a generic Warning:

```python

    with pytest.warns() as record:
        warnings.warn("user", UserWarning)
        warnings.warn("runtime", RuntimeWarning)

    assert len(record) == 2
    assert str(record[0].message) == "user"
    assert str(record[1].message) == "runtime"

```

The `recwarn` fixture will record warnings for the whole function:

```python

    import warnings

    def test_hello(recwarn):
        warnings.warn("hello", UserWarning)
        assert len(recwarn) == 1
        w = recwarn.pop(UserWarning)
        assert issubclass(w.category, UserWarning)
        assert str(w.message) == "hello"
        assert w.filename
        assert w.lineno

```

Both the `recwarn` fixture and the `pytest.warns()` context manager return the same interface for recorded
warnings: a `~_pytest.recwarn.WarningsRecorder` instance. To view the recorded warnings, you can
iterate over this instance, call `len` on it to get the number of recorded
warnings, or index into it to get a particular recorded warning.

.. _`warns use cases`:

## Additional use cases of warnings in tests

Here are some use cases involving warnings that often come up in tests, and suggestions on how to deal with them:

- To ensure that **at least one** of the indicated warnings is issued, use:

```python

    def test_warning():
        with pytest.warns((RuntimeWarning, UserWarning)):
            ...

```

- To ensure that **only** certain warnings are issued, use:

```python

    def test_warning(recwarn):
        ...
        assert len(recwarn) == 1
        user_warning = recwarn.pop(UserWarning)
        assert issubclass(user_warning.category, UserWarning)

```

-  To ensure that **no** warnings are emitted, use:

```python

    def test_warning():
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            ...

```

- To suppress warnings, use:

```python

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        ...

```

## Custom failure messages

Recording warnings provides an opportunity to produce custom test
failure messages for when no warnings are issued or other conditions
are met.

```python

    def test():
        with pytest.warns(Warning) as record:
            f()
            if not record:
                pytest.fail("Expected a warning!")

```

If no warnings are issued when calling `f`, then `not record` will
evaluate to `True`.  You can then call `pytest.fail()` with a
custom error message.

.. _internal-warnings:

## Internal pytest warnings

pytest may generate its own warnings in some situations, such as improper usage or deprecated features.

For example, pytest will emit a warning if it encounters a class that matches `python_classes` but also
defines an `__init__` constructor, as this prevents the class from being instantiated:

```python

    # content of test_pytest_warnings.py
    class Test:
        def __init__(self):
            pass

        def test_foo(self):
            assert 1 == 1

```

    $ pytest test_pytest_warnings.py -q

    ============================= warnings summary =============================
    test_pytest_warnings.py:1
      /home/sweet/project/test_pytest_warnings.py:1: PytestCollectionWarning: cannot collect test class 'Test' because it has a __init__ constructor (from: test_pytest_warnings.py)
        class Test:

    -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
    1 warning in 0.12s

```

These warnings might be filtered using the same builtin mechanisms used to filter other types of warnings.

Please read our `backwards-compatibility` to learn how we proceed about deprecating and eventually removing
features.

The full list of warnings is listed in `the reference documentation`.

.. _`resource-warnings`:

## Resource Warnings

Additional information of the source of a `ResourceWarning` can be obtained when captured by pytest if
`tracemalloc` module is enabled.

One convenient way to enable `tracemalloc` when running tests is to set the `PYTHONTRACEMALLOC` to a large
enough number of frames (say `20`, but that number is application dependent).

For more information, consult the [Python Development Mode](https://docs.python.org/3/library/devmode.html)_
section in the Python documentation.
