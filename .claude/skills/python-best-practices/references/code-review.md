# Code Review Checklist

Comprehensive checklist for reviewing Python code. See SKILL.md for quick reference.

## Priority Levels

- **Blocker**: Must fix before merge
- **High**: Should fix soon
- **Medium**: Nice to have
- **Low**: Nitpick / suggestion

---

## 1. Correctness (Blocker)

### Logic and Edge Cases

- [ ] Does the code do what it's supposed to do?
- [ ] Are edge cases handled? (empty input, None, negative numbers)
- [ ] Are off-by-one errors possible?
- [ ] Are race conditions possible in concurrent code?

```python
# Check for edge cases
def get_first(items: list[T]) -> T:  # What if empty?
    return items[0]  # IndexError!

# Better
def get_first(items: list[T]) -> T | None:
    return items[0] if items else None
```

### Error Handling

- [ ] Are exceptions caught specifically (not bare `except:`)?
- [ ] Are errors logged with context?
- [ ] Are resources properly cleaned up?
- [ ] Is error propagation appropriate?

---

## 2. Security (Blocker)

### Input Validation

- [ ] Is all external input validated?
- [ ] Are SQL queries parameterized?
- [ ] Are file paths validated against traversal?
- [ ] Is HTML output escaped?

```python
# NEVER allow
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")  # SQL injection

# ALWAYS require
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```

### Secrets and Credentials

- [ ] Are there any hardcoded secrets?
- [ ] Are credentials loaded from environment?
- [ ] Are sensitive values logged?

### Authentication/Authorization

- [ ] Are authorization checks present?
- [ ] Are permissions validated before operations?

---

## 3. Error Handling (Blocker)

### Anti-Patterns to Flag

```python
# BLOCKER: Bare except
try:
    do_something()
except:
    pass

# BLOCKER: Silent failure
try:
    save_to_database(data)
except Exception:
    pass  # Data lost!

# BLOCKER: Catching KeyboardInterrupt
try:
    long_operation()
except Exception:  # Catches KeyboardInterrupt!
    pass

# HIGH: Too broad
try:
    complex_operation()
except Exception:  # Should catch specific exceptions
    log_error()
```

### Required Patterns

```python
# GOOD: Specific exception with logging
try:
    save_to_database(data)
except DatabaseConnectionError as e:
    logger.error(f"Failed to save: {e}", extra={"data_id": data.id})
    raise
```

---

## 4. Type Safety (High)

### Type Hints

- [ ] Are public functions typed?
- [ ] Are return types specified?
- [ ] Is `Any` used excessively?
- [ ] Are `Optional` / `| None` used correctly?

```python
# HIGH: Missing types on public function
def process(data):  # What types?
    return transform(data)

# GOOD
def process(data: dict[str, Any]) -> Result:
    return transform(data)
```

### Type Guardrails

- [ ] Does mypy pass without errors?
- [ ] Are there `# type: ignore` comments that should be fixed?

---

## 5. Testing (Blocker/High)

### Coverage

- [ ] Are there tests for new code?
- [ ] Do tests cover the happy path?
- [ ] Do tests cover error cases?
- [ ] Are edge cases tested?

### Test Quality

- [ ] Do tests test behavior, not implementation?
- [ ] Are tests isolated (no shared mutable state)?
- [ ] Are test names descriptive?

```python
# GOOD test name
def test_transfer_insufficient_funds_raises_error():
    ...

# BAD test name
def test_account():
    ...
```

---

## 6. Code Quality (Medium)

### Naming

- [ ] Are names clear and descriptive?
- [ ] Do names follow PEP 8 conventions?
- [ ] Are boolean names prefixed (is_, has_, can_)?

```python
# MEDIUM: Unclear names
d = 86400
lst = []
flag = True

# GOOD
SECONDS_PER_DAY = 86400
users = []
is_active = True
```

### Functions

- [ ] Does each function do one thing?
- [ ] Are functions reasonably short (< 30 lines)?
- [ ] Are there too many parameters (> 5)?

### DRY

- [ ] Is there duplicated code?
- [ ] Can similar logic be consolidated?

---

## 7. Performance (Medium)

### Common Issues

- [ ] Are there N+1 query problems?
- [ ] Is there unnecessary work in loops?
- [ ] Are large objects being copied unnecessarily?
- [ ] Are blocking calls in async functions?

```python
# MEDIUM: N+1 problem
for user in users:
    orders = get_orders(user.id)  # N queries!

# BETTER: Batch query
user_ids = [u.id for u in users]
all_orders = get_orders_batch(user_ids)
```

### Memory

- [ ] Are large files loaded entirely into memory?
- [ ] Are generators used where appropriate?

---

## 8. Documentation (Low/Medium)

### When Documentation is Needed

- [ ] Complex algorithms explained?
- [ ] Non-obvious business logic documented?
- [ ] Public APIs documented?

```python
# MEDIUM: Needs docstring
def calculate_compound_interest(principal, rate, years):
    # What formula? What units for rate?
    ...

# GOOD
def calculate_compound_interest(principal: float, rate: float, years: int) -> float:
    """Calculate compound interest using A = P(1 + r)^t.

    Args:
        principal: Initial amount in dollars
        rate: Annual rate as decimal (0.05 = 5%)
        years: Number of years

    Returns:
        Final amount after compounding
    """
    ...
```

---

## 9. Style (Low)

### PEP 8

- [ ] Are lines under 88/100 characters?
- [ ] Is indentation consistent (4 spaces)?
- [ ] Are imports organized correctly?

### Nitpicks (Don't Block)

- Minor style preferences
- Subjective naming improvements
- Optional refactoring suggestions

---

## Review Decision Matrix

| Issue Type | Priority | Action |
|------------|----------|--------|
| Security vulnerability | Blocker | Must fix |
| Bug / incorrect logic | Blocker | Must fix |
| Missing tests | High | Should fix |
| Missing types | High | Should fix |
| Code duplication | Medium | Discuss |
| Performance issue | Medium | Discuss |
| Style nitpick | Low | Optional |

## Quick Checklist for Reviewers

```
□ Security: No SQL injection, secrets, eval
□ Correctness: Logic works, edge cases handled
□ Error Handling: Specific exceptions, no silent failures
□ Types: Public interfaces typed
□ Tests: New code tested, edge cases covered
□ Quality: Clear names, single responsibility
□ Performance: No obvious inefficiencies
```
