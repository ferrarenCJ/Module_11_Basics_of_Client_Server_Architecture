# Mini-Lesson 11.6: OAuth2 and Okta

## What Is OAuth2?

OAuth2 is an authorization protocol that allows applications and services to securely access protected resources without requiring users to share their login credentials directly.

OAuth2 was introduced as an update to the original OAuth framework and has become the industry standard for authorization in web, mobile, and cloud applications.

---

## Purpose of OAuth2

OAuth2 allows a user to grant limited access to resources without giving an application their username and password.

Instead of sharing credentials directly:

```text
User
   |
Authorization
   |
OAuth2 Provider
   |
Access Token
   |
Application
```

An access token is issued that grants specific permissions.

---

## OAuth2 Example

A common example is:

```text
Sign in with Google
Sign in with Microsoft
Sign in with GitHub
```

When using these options:

1. The user is redirected to the external provider.
2. Authentication occurs there.
3. The provider confirms the user's identity.
4. An access token is returned.
5. Access is granted to the requesting application.

The user never shares their password directly with the application.

---

## OAuth2 Focuses on Authorization

OAuth2 is primarily concerned with:

```text
Authorization
```

rather than:

```text
Authentication
```

### Authentication

Answers:

```text
Who are you?
```

Examples:

- Username
- Password
- Multi-factor authentication

---

### Authorization

Answers:

```text
What are you allowed to do?
```

Examples:

- Read data
- Update records
- Access an API
- Manage resources

---

## Benefits of OAuth2

### Improved Security

Applications do not need to store user passwords.

### Token-Based Access

Tokens can be revoked without changing user credentials.

### Granular Permissions

Access can be limited to specific actions.

### Better User Experience

Users can access services using trusted providers.

---

# OAuth2 Architecture

```text
User
   |
Application
   |
OAuth2 Provider
   |
Access Token
   |
Protected Resource
```

The OAuth2 provider determines whether access should be granted.

---

# Access Tokens

OAuth2 uses access tokens to authorize requests.

Example:

```text
eyJhbGciOi...
```

Characteristics:

- Temporary
- Revocable
- Permission-based
- More secure than passwords

---

## OAuth2 Scopes

Scopes define what a token can do.

Examples:

```text
read
write
admin
profile
email
```

A token only grants access to the scopes assigned to it.

---

# What Is Okta?

Okta is an Identity and Access Management (IAM) platform.

Purpose:

- Authentication
- Authorization
- Single Sign-On (SSO)
- User management
- API security

Okta implements OAuth2 and other industry-standard security protocols.

---

# Why Organizations Use Okta

Organizations commonly use Okta to:

- Centralize user management
- Simplify access control
- Improve security
- Support cloud applications
- Enable Single Sign-On

---

## Single Sign-On (SSO)

One login grants access to multiple applications.

Example:

```text
Employee Login
      |
      +-- Application A
      +-- Application B
      +-- Application C
```

Benefits:

- Fewer passwords
- Better security
- Improved user experience

---

# Identity and Access Management (IAM)

IAM systems manage:

- Users
- Groups
- Roles
- Permissions
- Authentication
- Authorization

Examples:

- Okta
- Microsoft Entra ID (Azure AD)
- AWS IAM

---

# API Token Management with Okta

Okta uses API tokens to authenticate requests made to Okta APIs.

API tokens function similarly to session cookies.

Purpose:

- Authenticate API requests
- Identify users
- Control permissions

---

## Characteristics of API Tokens

### User-Specific

Each token belongs to a specific user.

### Permission-Based

The token inherits the permissions of its creator.

### Dynamic Permissions

If user permissions change:

```text
User Permissions Change
            |
            v
Token Permissions Change
```

---

## Token Expiration

Okta API tokens remain active for:

```text
30 days
```

of inactivity.

Every successful use renews the expiration period.

---

## Token Revocation

A token becomes invalid when:

### User Is Deactivated

```text
User Disabled
      |
Token Invalid
```

### Token Is Inactive

```text
Inactive > 30 Days
         |
         v
Token Revoked
```

---

## Token Reactivation

If the user account is reactivated:

```text
User Reactivated
       |
Token Valid Again
```

assuming the token itself has not been revoked.

---

# OAuth2 and Okta APIs

OAuth2 allows applications to access Okta APIs using access tokens.

Instead of:

```text
Username
Password
```

applications use:

```text
OAuth2 Access Token
```

---

## Scoped Access

Each token contains specific scopes.

Example:

```text
read:users
write:users
read:groups
```

The token determines what operations are permitted.

---

# OAuth2 Workflow with Okta

```text
User Requests Access
          |
          v
Application Redirects User
          |
          v
Okta Login
          |
Authentication
          |
          v
Access Token Issued
          |
          v
Application Uses Token
          |
          v
Protected Resource
```

---

# OAuth2 vs Authentication

| Authentication | Authorization |
|---------------|---------------|
| Verifies identity | Verifies permissions |
| Answers "Who are you?" | Answers "What can you do?" |
| Username/password | Access token/scopes |
| Kerberos | OAuth2 |

---

# OAuth2 vs Kerberos

| OAuth2 | Kerberos |
|---------|----------|
| Authorization-focused | Authentication-focused |
| Token-based | Ticket-based |
| API access | Enterprise authentication |
| Cloud applications | Internal enterprise systems |

---

# Data Engineering Connections

## Cloud Platforms

OAuth2 protects access to:

- AWS APIs
- Azure APIs
- Google Cloud APIs

---

## Data Platforms

OAuth2 commonly secures:

- Data catalogs
- Data pipelines
- Analytics services
- Reporting platforms

---

## Enterprise Applications

OAuth2 and Okta are frequently used to protect:

- Internal dashboards
- Web applications
- Administrative tools
- Developer portals

---

# Important Terms

| Term | Definition |
|--------|------------|
| OAuth2 | Authorization protocol |
| Authentication | Verification of identity |
| Authorization | Verification of permissions |
| Okta | Identity and Access Management platform |
| IAM | Identity and Access Management |
| API Token | Credential used to authorize API requests |
| Access Token | OAuth2 token that grants access |
| Scope | Permission assigned to a token |
| SSO | Single Sign-On |

---

# Questions for Review

- What problem does OAuth2 solve?
- Why is OAuth2 considered an authorization protocol?
- How does Okta implement OAuth2?
- What is an API token?
- What is the purpose of token scopes?
- Why are access tokens more secure than sharing passwords?

---

# Key Takeaways

- OAuth2 is an authorization protocol.
- OAuth2 enables secure access without exposing user credentials.
- OAuth2 uses access tokens instead of passwords.
- Okta is an Identity and Access Management platform.
- API tokens act on behalf of users and inherit user permissions.
- Token scopes control what resources can be accessed.
- OAuth2 and Okta are commonly used to secure APIs and cloud services.
- Authorization and authentication are related but distinct concepts.

---

# Summary

OAuth2 is an industry-standard authorization framework that enables secure access to resources using access tokens rather than usernames and passwords. Okta implements OAuth2 to provide centralized identity and access management, allowing organizations to secure applications, APIs, and cloud services through token-based authorization, Single Sign-On (SSO), and permission management.