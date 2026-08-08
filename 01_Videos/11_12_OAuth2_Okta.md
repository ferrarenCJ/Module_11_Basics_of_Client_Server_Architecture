# Video 11.12: OAuth2 Example Set-Up

**Duration:** 08:18

## Learning Objectives

- Understand the purpose of OAuth2
- Learn the difference between authentication and authorization
- Understand how third-party identity providers work
- Learn the role of Okta in identity and access management
- Understand how OAuth2 protects APIs
- Explore enterprise access management concepts

---

# Summary

This video introduces OAuth2 and demonstrates how Okta can be used to protect APIs.

OAuth2 is an industry-standard authorization framework that enables applications to obtain limited access to protected resources without exposing user credentials.

Rather than allowing applications to directly manage usernames and passwords, OAuth2 delegates authorization decisions to a trusted third-party identity provider.

Dr. Williams demonstrates how Okta can be used as that identity provider.

---

# What Is OAuth2?

OAuth2 stands for:

```text
Open Authorization 2.0
```

OAuth2 is an authorization framework used to control access to protected resources.

OAuth2 answers:

```text
What is this user allowed to access?
```

---

# Authentication vs Authorization

## Authentication

Answers:

```text
Who are you?
```

Examples:

- Username and password
- Kerberos
- Single Sign-On (SSO)

---

## Authorization

Answers:

```text
What are you allowed to do?
```

Examples:

- Read a file
- Access an API
- View dashboard data
- Modify application settings

OAuth2 primarily focuses on authorization.

---

# Traditional Authentication Problem

Without OAuth2:

```text
Application
      |
Stores User Password
      |
Accesses Resource
```

Problems:

- Password exposure
- Security risks
- Credential