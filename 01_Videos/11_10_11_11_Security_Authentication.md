# Security and Authentication (Videos 11.10 and 11.11)

## Learning Objectives

- Understand authentication and authorization
- Learn the purpose of Kerberos
- Understand distributed authentication challenges
- Learn the basics of Public Key Infrastructure (PKI)
- Understand public and private keys
- Learn how digital signing works
- Understand encryption concepts
- Learn the role of OpenSSL in security

---

# Video 11.10: Security Overview - Kerberos

**Duration:** 11:43

## Summary

This video introduces security fundamentals in distributed systems.

Dr. Williams explains the difference between authentication and authorization and introduces Kerberos, a distributed authentication system developed at MIT.

Kerberos provides a secure method of identifying users and services across a network without repeatedly transmitting passwords.

---

## Authentication vs Authorization

### Authentication

Answers:

```text
Who are you?
```

Purpose:

- Verify identity
- Confirm user credentials

Examples:

- Username and password
- Session cookies
- Security tokens

---

### Authorization

Answers:

```text
What are you allowed to do?
```

Purpose:

- Control access
- Restrict resources
- Enforce permissions

Examples:

- Read access
- Administrative access
- Restricted routes

---

## Why Authentication Is Needed

In distributed systems:

```text
Client
    |
Network
    |
Server
```

The server must determine:

- Who is making the request
- Whether the identity is legitimate
- Whether access should be granted

---

## What Is Kerberos?

Kerberos is an authentication protocol developed at MIT.

Purpose:

- Securely authenticate users
- Avoid transmitting passwords repeatedly
- Support distributed computing environments

---

## Kerberos Components

### Client

User requesting access.

---

### Authentication Server (AS)

Verifies user credentials.

---

### Ticket Granting Server (TGS)

Issues tickets used to access services.

---

### Service Server

Resource being accessed.

Examples:

- Database
- Web application
- File server

---

## Kerberos Workflow

```text
Client
    |
Authentication Request
    |
Authentication Server
    |
Ticket Granting Ticket
    |
Ticket Granting Server
    |
Service Ticket
    |
Protected Resource
```

---

## Benefits of Kerberos

- Centralized authentication
- Reduced password exposure
- Improved security
- Support for distributed systems
- Widely used in enterprise environments

---

## Distributed Computing Connection

Modern systems often include:

```text
Web Applications
Databases
API Services
Cloud Resources
```

Users need a secure mechanism for moving between services.

Kerberos provides that mechanism.

---

# Video 11.11: OpenSSL - PKI Keys, Encryption, and Signing

**Duration:** 09:24

## Summary

This video introduces OpenSSL and demonstrates how public key cryptography is used to:

- Generate keys
- Encrypt information
- Sign documents
- Verify identity

These technologies form the foundation of modern internet security.

---

## What Is OpenSSL?

OpenSSL is an open-source security library.

Functions include:

- Encryption
- Decryption
- Certificate management
- Key generation
- Digital signatures

---

## Public Key Infrastructure (PKI)

PKI uses cryptographic key pairs.

Each user receives:

### Public Key

Shared with others.

### Private Key

Kept secret.

---

## Key Pair Structure

```text
Public Key
     |
     |
Private Key
```

The keys are mathematically related.

---

## Public Key

Purpose:

- Verify signatures
- Encrypt information

May be freely distributed.

---

## Private Key

Purpose:

- Create signatures
- Decrypt information

Must remain secret.

---

## Encryption

Encryption converts readable information into unreadable data.

Example:

```text
Plain Text
      |
Encryption
      |
Cipher Text
```

Only authorized users should be able to decrypt the data.

---

## Decryption

Process of converting encrypted information back into readable form.

```text
Cipher Text
      |
Decryption
      |
Plain Text
```

---

## Digital Signing

Digital signatures prove:

- Identity
- Integrity
- Authenticity

Process:

```text
Document
     |
Private Key
     |
Digital Signature
```

---

## Signature Verification

Verification uses:

```text
Document
     |
Public Key
     |
Verification Result
```

If verification succeeds:

- Document is authentic
- Document has not been altered

---

## GitHub Example

Public/private keys are frequently used with GitHub.

Benefits:

- Verify commit ownership
- Authenticate developers
- Protect source code repositories

---

## Security Tokens

Security tokens help systems verify identity and establish trust.

Used for:

- Authentication
- Authorization
- Session management

Examples:

- Kerberos tickets
- OAuth tokens
- Session identifiers

---

## Security Architecture

```text
User
   |
Authentication
   |
Kerberos / Tokens
   |
Authorization
   |
Protected Resource
```

---

## Enterprise Security Applications

Common uses:

- Corporate networks
- Cloud services
- Source control systems
- Web applications
- Enterprise databases

---

## Important Terms

| Term | Definition |
|--------|------------|
| Authentication | Verifying identity |
| Authorization | Determining permissions |
| Kerberos | Distributed authentication protocol |
| OpenSSL | Security and cryptography library |
| PKI | Public Key Infrastructure |
| Public Key | Shared cryptographic key |
| Private Key | Secret cryptographic key |
| Encryption | Converting data into unreadable form |
| Decryption | Restoring encrypted data |
| Digital Signature | Verification of authenticity |
| Security Token | Credential used for authentication |

---

## Data Engineering Connections

### Cloud Platforms

Services such as:

- AWS
- Azure
- Google Cloud

use authentication tokens and PKI extensively.

---

### Data Platforms

Security mechanisms protect:

- Data lakes
- Data warehouses
- ETL pipelines
- Reporting platforms

---

### Source Control

GitHub commonly uses:

- SSH keys
- Public/private keys
- Signed commits

for authentication and verification.

---

## Questions for Review

- What is the difference between authentication and authorization?
- Why was Kerberos developed?
- What problem does PKI solve?
- How do public and private keys work together?
- What is a digital signature?
- Why is encryption important?

---

## Key Takeaways

- Authentication identifies users.
- Authorization determines permissions.
- Kerberos provides secure authentication for distributed systems.
- OpenSSL provides cryptographic capabilities.
- PKI uses public and private key pairs.
- Digital signatures verify authenticity and integrity.
- Encryption protects sensitive information.
- Modern cloud and web systems rely heavily on these security concepts.

---

## Summary

Videos 11.10 and 11.11 introduce the security foundations required for modern distributed systems. Kerberos provides a solution for authentication and secure access to services, while OpenSSL demonstrates how public key cryptography, digital signatures, encryption, and PKI are used to establish trust and protect communications across networks.