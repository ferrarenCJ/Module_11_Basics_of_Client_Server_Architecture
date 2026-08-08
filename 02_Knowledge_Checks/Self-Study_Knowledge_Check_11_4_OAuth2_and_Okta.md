# Self-Study Knowledge Check 11.4: OAuth2 and Okta

## Learning Outcome

Identify key concepts of security, encryption, and authentication.

---

## Question 1

### What is OAuth2?

✅ OAuth2 is an authorization protocol used to access services without specific login credentials for those services.

### Explanation

OAuth2 is an industry-standard authorization framework.

It allows users and applications to access protected resources without sharing their actual passwords.

Example:

```text
Sign in with Google
Sign in with Microsoft
Sign in with GitHub
```

Instead of sharing credentials with every application, OAuth2 uses access tokens to grant access.

---

## Question 2

### Which of the following can be achieved using OAuth2?

✅ OAuth2 can help a user to log in on two unrelated websites.

### Explanation

OAuth2 enables delegated authorization.

Example:

```text
Website A
     |
Use Google Login
     |
Google Verifies User
     |
Website A Grants Access
```

The user can access an application using credentials managed by another trusted provider.

### Real-World Examples

- Sign in with Google
- Sign in with Microsoft
- Sign in with GitHub
- Sign in with Facebook

---

## Question 3

### What is the purpose of Okta?

✅ Okta enables users to access various services and applications by means of a single login.

### Explanation

Okta is an Identity and Access Management (IAM) platform.

It provides:

- Authentication
- Authorization
- Single Sign-On (SSO)
- User Management
- API Security

Example:

```text
Login Once
     |
     +-- Salesforce
     +-- Microsoft 365
     +-- AWS Console
     +-- Internal Applications
```

This simplifies user access while maintaining security.

---

## Question 4

### Which of the following is OAuth2 related to?

✅ Authorization

### Explanation

OAuth2 focuses on:

```text
What are you allowed to do?
```

rather than:

```text
Who are you?
```

OAuth2 uses:

- Access Tokens
- Scopes
- Permissions

to determine what resources can be accessed.

---

# Key Concepts Reinforced

## Authentication

Answers:

```text
Who are you?
```

Examples:

- Username
- Password
- Kerberos
- SSO

---

## Authorization

Answers:

```text
What are you allowed to do?
```

Examples:

- API Access
- Resource Access
- Permissions
- Roles

OAuth2 primarily focuses on authorization.

---

## OAuth2

Authorization framework that:

- Uses access tokens
- Protects APIs
- Supports delegated access
- Avoids sharing credentials

---

## Access Tokens

OAuth2 uses access tokens rather than passwords.

Example:

```text
eyJhbGciOi...
```

Benefits:

- Temporary
- Revocable
- Scoped permissions

---

## Okta

Identity and Access Management (IAM) platform that supports:

- OAuth2
- SSO
- User Authentication
- User Authorization
- API Security

---

## Single Sign-On (SSO)

Provides:

```text
One Login
    |
Multiple Applications
```

Benefits:

- Better user experience
- Centralized security
- Reduced password management

---

# OAuth2 Workflow

```text
User
   |
Application
   |
Okta
   |
Access Token
   |
Protected Resource
```

OAuth2 grants access through tokens instead of passwords.

---

# OAuth2 vs Authentication

| Authentication | Authorization |
|---------------|---------------|
| Who are you? | What can you access? |
| Kerberos | OAuth2 |
| Identity | Permissions |
| Login Process | Access Control |

---

# Result

✅ 4 / 4 Questions Correct

---

# Key Takeaways

- OAuth2 is an authorization framework.
- OAuth2 allows access without exposing user credentials.
- Access tokens replace direct credential sharing.
- Okta is an Identity and Access Management platform.
- Okta supports Single Sign-On and OAuth2.
- OAuth2 is related to authorization, not authentication.
- OAuth2 is commonly used to secure web applications, cloud services, and APIs.

---

# Summary

This knowledge check reinforced the concepts of OAuth2 and Okta. OAuth2 enables secure authorization through access tokens, while Okta provides identity and access management capabilities such as authentication, authorization, Single Sign-On, and API security. Together, these technologies are widely used to secure modern cloud platforms, enterprise systems, and web applications.