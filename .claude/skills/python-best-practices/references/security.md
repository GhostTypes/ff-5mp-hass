# Security Best Practices

Comprehensive guide to Python security. See SKILL.md for quick reference.

## Core Principles

1. **Never trust input** - Validate everything from external sources
2. **Least privilege** - Only permissions needed, nothing more
3. **Defense in depth** - Multiple layers of security
4. **Secure by default** - Fail closed, not open

## Input Validation

### Always Validate External Input

```python
# BAD: Direct use of user input
def search(query: str):
    return db.execute(f"SELECT * FROM products WHERE name LIKE '%{query}%'")

# GOOD: Validate and sanitize
import re
from html import escape

def search(query: str) -> list[Product]:
    # Validate length
    if len(query) > 100:
        raise ValidationError("Query too long")

    # Sanitize for display
    safe_query = escape(query)

    # Use parameterized query
    return db.query(Product).filter(Product.name.ilike(f"%{query}%")).all()
```

### Input Validation Patterns

```python
from pydantic import BaseModel, EmailStr, validator

class UserCreate(BaseModel):
    email: EmailStr  # Validates email format
    username: str
    age: int

    @validator('username')
    def validate_username(cls, v):
        if not re.match(r'^[a-zA-Z0-9_]{3,20}$', v):
            raise ValueError('Username must be 3-20 alphanumeric characters')
        return v

    @validator('age')
    def validate_age(cls, v):
        if not 0 <= v <= 150:
            raise ValueError('Invalid age')
        return v
```

## SQL Injection Prevention

### NEVER Use String Formatting in SQL

```python
# BAD: SQL injection vulnerability
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
cursor.execute("SELECT * FROM users WHERE name = '%s'" % name)

# GOOD: Parameterized queries
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
cursor.execute("SELECT * FROM users WHERE name = %s", (name,))

# GOOD: ORM (SQLAlchemy)
session.query(User).filter(User.id == user_id).first()
```

## Command Injection Prevention

### NEVER Use Shell=True or String Formatting

```python
import subprocess

# BAD: Command injection vulnerability
subprocess.run(f"convert {filename} output.png", shell=True)
os.system(f"ping {host}")

# GOOD: Use list of arguments, no shell
subprocess.run(["convert", filename, "output.png"], check=True)

# GOOD: Validate input before use
import re

def ping(host: str) -> str:
    # Validate hostname format
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    result = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True,
        text=True
    )
    return result.stdout
```

## Secrets Management

### NEVER Hardcode Secrets

```python
# BAD: Secrets in code
API_KEY = "sk-abc123..."
DATABASE_PASSWORD = "secret123"
SECRET_KEY = "my-secret-key"

# GOOD: Environment variables
import os
from functools import lru_cache

@lru_cache
def get_api_key() -> str:
    return os.environ["API_KEY"]

# GOOD: Use python-dotenv for development
from dotenv import load_dotenv
load_dotenv()  # Loads from .env file

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise EnvironmentError("API_KEY not set")
```

### Secure Random Generation

```python
import secrets

# BAD: Predictable random
import random
token = str(random.random())  # Not cryptographically secure

# GOOD: Use secrets module
token = secrets.token_urlsafe(32)  # For API keys, tokens
api_key = secrets.token_hex(16)
password = secrets.choice(string.ascii_letters + string.digits)

# GOOD: Secure integer
secure_int = secrets.randbelow(1000000)
```

## Password Handling

### Password Hashing

```python
import hashlib
import os
import bcrypt  # Recommended library

# BAD: Plain text or weak hashing
stored_password = password  # Never store plain text
hashed = hashlib.md5(password.encode())  # MD5 is broken

# GOOD: Use bcrypt or argon2
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

# Alternative with hashlib (less preferred)
def hash_with_pbkdf2(password: str, salt: bytes | None = None) -> tuple[str, bytes]:
    salt = salt or os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return key.hex(), salt
```

## Path Traversal Prevention

```python
import os
from pathlib import Path

# BAD: Path traversal vulnerability
def read_file(filename: str) -> str:
    with open(f"/uploads/{filename}") as f:  # Could be "../../../etc/passwd"
        return f.read()

# GOOD: Validate and sanitize paths
def read_file_safe(filename: str, base_dir: Path) -> str:
    # Validate filename doesn't contain path separators
    if '/' in filename or '\\' in filename:
        raise ValueError("Invalid filename")

    # Resolve to absolute path
    file_path = (base_dir / filename).resolve()

    # Ensure it's within base directory
    if not str(file_path).startswith(str(base_dir.resolve())):
        raise ValueError("Access denied")

    with open(file_path) as f:
        return f.read()
```

## Cross-Site Scripting (XSS) Prevention

```python
from html import escape
import bleach

# BAD: Direct output of user content
html = f"<div>{user_input}</div>"

# GOOD: Escape HTML entities
safe_html = f"<div>{escape(user_input)}</div>"

# GOOD: Sanitize HTML with bleach
def sanitize_html(content: str) -> str:
    allowed_tags = ['p', 'b', 'i', 'u', 'a', 'ul', 'ol', 'li']
    allowed_attrs = {'a': ['href', 'title']}
    return bleach.clean(content, tags=allowed_tags, attributes=allowed_attrs)
```

## Error Handling and Information Disclosure

```python
# BAD: Exposes internal details
@app.errorhandler(Exception)
def handle_error(e):
    return str(e), 500  # Leaks stack traces, paths, etc.

# GOOD: Generic error to user, detailed to logs
import logging
logger = logging.getLogger(__name__)

@app.errorhandler(Exception)
def handle_error(e):
    logger.exception("Internal error occurred")
    return {"error": "An internal error occurred"}, 500

# GOOD: Different behavior for debug mode
@app.errorhandler(Exception)
def handle_error(e):
    if app.debug:
        return {"error": str(e), "type": type(e).__name__}, 500
    logger.exception("Internal error")
    return {"error": "Internal server error"}, 500
```

## Security Checklist

### Authentication & Authorization

- [ ] Use strong password hashing (bcrypt/argon2)
- [ ] Implement rate limiting on login
- [ ] Use secure session management
- [ ] Implement proper logout (invalidate tokens)
- [ ] Use HTTPS everywhere
- [ ] Set secure cookie flags (HttpOnly, Secure, SameSite)

### Input Handling

- [ ] Validate all external input
- [ ] Use parameterized queries
- [ ] Sanitize output for context (HTML, JSON, shell)
- [ ] Limit file upload sizes and types
- [ ] Validate file paths

### Secrets & Configuration

- [ ] No secrets in code
- [ ] Use environment variables or secret managers
- [ ] Different credentials per environment
- [ ] Rotate credentials regularly

### Dependencies

- [ ] Keep dependencies updated
- [ ] Use dependency scanning tools
- [ ] Pin dependency versions
- [ ] Review transitive dependencies

## Quick Reference

| Vulnerability | Prevention |
|--------------|------------|
| SQL Injection | Parameterized queries, ORM |
| Command Injection | Avoid shell=True, validate input |
| XSS | Escape output, sanitize HTML |
| Path Traversal | Validate paths, use resolve() |
| Weak Auth | bcrypt/argon2, rate limiting |
| Info Disclosure | Generic errors, no stack traces |
| Insecure Random | secrets module, not random |
