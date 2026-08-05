# Cookies (Video 11.5)

## Learning Objectives

- Understand what cookies are and how they work
- Learn why websites use cookies
- Explore how cookies support client-server communication
- Understand the advantages and limitations of cookies

---

## What Are Cookies?

### Definition

A cookie is a small piece of data stored on a user's device by a web browser.

### Purpose

Cookies allow websites to remember information between requests.

---

## Why Cookies Are Used

### User Preferences

Examples:

- Language settings
- Theme preferences
- Display settings

### Session Management

Examples:

- Login status
- Shopping cart contents
- User-specific settings

### Tracking and Analytics

Examples:

- Website usage patterns
- Visit frequency
- User behavior analysis

---

## How Cookies Work

### Step 1

User visits a website.

### Step 2

Server sends a cookie to the browser.

### Step 3

Browser stores the cookie locally.

### Step 4

Browser sends the cookie back with future requests.

---

## Cookie Lifecycle

### Creation

Server creates a cookie.

### Storage

Browser stores the cookie.

### Transmission

Browser sends the cookie with requests.

### Expiration

Cookie expires or is deleted.

---

## Types of Cookies

### Persistent Cookies

Stored on the user's device until their expiration date.

#### Examples

- Saved usernames
- Language preferences
- Site settings

---

### Session Cookies

Temporary cookies that are removed when the browser closes.

#### Examples

- Login sessions
- Temporary shopping carts
- Active user sessions

---

## Cookie Components

### Name

Identifies the cookie.

### Value

Stores the cookie data.

### Expiration Date

Determines how long the cookie remains valid.

### Domain

Specifies which domain may access the cookie.

### Path

Specifies where the cookie applies.

---

## Advantages of Cookies

### User Convenience

Websites can remember preferences.

### Better User Experience

Reduces repetitive actions.

### Session Management

Supports authenticated user interactions.

---

## Limitations and Risks

### Security Concerns

Cookies may contain sensitive information.

### Privacy Concerns

Cookies can be used for tracking user activity.

### Storage Limits

Browsers enforce size and quantity restrictions.

---

## Flask Example

### Setting a Cookie

```python
from flask import make_response

response = make_response("Welcome!")
response.set_cookie("username", "cliff")
return response
```

### Reading a Cookie

```python
from flask import request

username = request.cookies.get("username")
```

---

## Client-Server Architecture Connection

### Client

Browser stores the cookie.

### Server

Creates and reads cookie information.

### Communication

Cookies help maintain state between requests in an otherwise stateless HTTP protocol.

---

## Data Engineering Connections

### Authentication

Used to maintain authenticated sessions.

### Internal Applications

Enterprise applications use cookies to manage user interactions.

### APIs

Authentication tokens may be stored in cookies in some implementations.

---

## Questions

- How are cookies different from sessions?
- What information should never be stored in cookies?
- When should persistent cookies be used?

---

## Key Takeaways

- Cookies are stored in the browser.
- Cookies help websites remember users.
- HTTP is stateless, and cookies help maintain state.
- Cookies can be persistent or session-based.
- Security and privacy must be considered when using cookies.

---

## Summary

Cookies are small pieces of data stored by the browser that allow websites to remember information across requests. They play an important role in session management, personalization, and 