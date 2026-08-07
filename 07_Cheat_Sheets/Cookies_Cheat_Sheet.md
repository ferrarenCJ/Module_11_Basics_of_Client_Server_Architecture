# Cookies Cheat Sheet

## Purpose

Cookies maintain state in a stateless HTTP environment.

---

## Cookie Flow

Browser Request
    ↓
Server Creates Cookie
    ↓
Browser Stores Cookie
    ↓
Future Requests Include Cookie

---

## Types

### Session Cookie
- Temporary
- Removed when browser closes
- Used for authentication

### Persistent Cookie
- Stored until expiration date
- Used for preferences and settings

---

## Flask Examples

### Set Cookie

```python
response.set_cookie("username", "cliff")