# Session Cookies (Videos 11.6 and 11.7)

## Learning Objectives

- Understand how session cookies work
- Learn how browsers store and manage cookies
- Explore how session cookies support authentication
- Understand Flask session management
- Learn how protected routes use session information

---

# Video 11.6: Session Cookie Exercise

**Duration:** 05:05

## Summary

This video explores how browsers store cookies and demonstrates how session cookies are used within the Books web application.

Dr. Williams shows how to inspect cookies using browser developer tools and provides an exercise to demonstrate what happens when all browser cookies are cleared.

The exercise highlights the importance of session cookies in maintaining user authentication and application state.

---

## Key Concepts

### Browser Cookie Storage

Browsers store cookies locally and automatically include them in future requests.

Common browser actions:

- View cookies
- Delete cookies
- Inspect cookie values
- Monitor cookie activity

---

### Session Cookies

Session cookies are temporary cookies used to maintain user identity during a browsing session.

Examples:

- Login sessions
- User authentication
- Temporary user preferences

---

### Browser Developer Tools

Developer tools can be used to:

- View active cookies
- Inspect cookie contents
- Monitor HTTP requests
- Track session information

---

### Clearing Cookies

Deleting browser cookies removes stored session information.

Result:

```text
Session Cookie Removed
        |
        v
User Session Lost
        |
        v
Authentication Required
```

---

### Session Management

Session cookies enable applications to maintain state across multiple requests.

Without cookies:

```text
Request 1
Request 2
Request 3
```

Server treats every request independently.

With cookies:

```text
Request 1
     |
Session Cookie
     |
Request 2
     |
Session Cookie
     |
Request 3
```

Server recognizes the same user.

---

## Exercise Outcome

When cookies are deleted:

- Login state disappears
- User identity information is removed
- Protected pages may become inaccessible
- Browser must re-authenticate

---

## Key Takeaways

- Browsers store session cookies locally.
- Session cookies identify users across requests.
- Deleting cookies removes session information.
- Applications use cookies to maintain authentication state.

---

# Video 11.7: Register User Information in a Browser Session

**Duration:** 14:24

## Summary

This video enhances the Books application by using Flask session information to determine whether a user is authenticated.

If no valid session exists, users are redirected to a registration or login page before being allowed to access protected content.

The video demonstrates how Flask sessions can be used to secure application routes while maintaining a seamless user experience.

---

## Key Concepts

### User Authentication

Authentication verifies a user's identity.

Common credentials:

- Username
- Password

Example:

```text
testuser
testuser
```

---

### Session Information

Once authenticated, user information is stored in the Flask session.

Example:

```python
session["username"] = username
```

Flask creates a signed session cookie that is returned to the browser.

---

### Session Validation

Applications should verify that required session data exists.

Example:

```python
if "username" in session:
```

If the session data is missing, the user should be redirected to login.

---

### Protected Routes

Protected routes should only be accessible to authenticated users.

Examples:

- Books page
- User profile
- Administrative pages

---

### Access Control Flow

```text
User Requests Resource
           |
           v
Is User Authenticated?
      /           \
    Yes            No
     |              |
Display Page   Redirect Login
```

---

### Registration Workflow

```text
User Visits Site
       |
       v
Register Page
       |
Enter Credentials
       |
       v
Login Validation
       |
       v
Create Session
       |
       v
Access Application
```

---

### Redirecting Unauthenticated Users

If a session is unavailable:

```text
Protected Route
        |
        v
No Session Found
        |
        v
Redirect to Register/Login
```

This prevents unauthorized access.

---

## Flask Session Examples

### Store Session Data

```python
session["username"] = username
```

### Check Session

```python
if "username" in session:
```

### Read Session

```python
session.get("username")
```

### Remove Session

```python
session.pop("username", None)
```

### Clear Session

```python
session.clear()
```

---

## Authentication vs Authorization

### Authentication

Determines:

```text
Who are you?
```

Examples:

- Username
- Password
- Login process

---

### Authorization

Determines:

```text
What are you allowed to access?
```

Examples:

- Protected pages
- Administrative functions
- Restricted resources

---

## Session Cookies and Scalability

Session cookies support scalable web applications because:

- Servers remain stateless
- User identity travels with requests
- Applications support large numbers of users
- Memory usage is minimized on the server

---

## Data Engineering Connections

### Enterprise Applications

Cookies and sessions are commonly used to:

- Manage logins
- Secure dashboards
- Control application access

### Internal Data Platforms

Many analytics and data engineering tools use session-based authentication to protect:

- Reports
- Data pipelines
- Administrative interfaces

---

## Important Terms

| Term | Definition |
|--------|------------|
| Session | User-specific state maintained across requests |
| Session Cookie | Temporary cookie used to identify a session |
| Authentication | Verification of user identity |
| Authorization | Determination of user permissions |
| Protected Route | Route requiring authentication |
| Browser Session | Active interaction between client and server |
| Session Validation | Verification that session data exists |
| Access Control | Restricting resources to approved users |

---

## Questions for Review

- What happens when a session cookie is deleted?
- Why are session cookies important for authentication?
- How does Flask manage sessions?
- What is the difference between authentication and authorization?
- Why should protected routes validate session information?

---

## Key Takeaways

- Session cookies maintain user identity between requests.
- Clearing browser cookies removes session information.
- Flask uses session objects to manage authenticated users.
- Protected routes should verify session data before granting access.
- Authentication and authorization serve different purposes.
- Session cookies enable secure and scalable web applications.

---

## Summary

Videos 11.6 and 11.7 build on the concepts introduced in Cookies (Video 11.5) by demonstrating how session cookies support authentication and access control. Flask uses session data to determine whether users can access protected resources, while browsers store and automatically return session cookies with future requests. Together, these concepts form the foundation of user authentication and session management in modern web applications.