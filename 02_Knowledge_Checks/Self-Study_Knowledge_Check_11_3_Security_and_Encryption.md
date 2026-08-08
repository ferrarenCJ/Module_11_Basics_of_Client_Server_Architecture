# Self-Study Knowledge Check 11.3: Security and Encryption

## Learning Outcome

Identify key concepts of security, encryption, and authentication.

---

## Question 1

### What is Kerberos?

✅ Kerberos is a trusted third-party tool that provides an authentication mechanism between the client and the server.

### Explanation

Kerberos is an authentication protocol developed at MIT that enables secure identity verification in distributed systems.

Benefits:

- Centralized authentication
- Reduced password exposure
- Secure ticket-based authentication
- Support for distributed computing environments

---

## Question 2

### What is the difference between authentication and authorization?

✅ Authentication verifies the user's identity, whereas authorization verifies the user's access level.

### Explanation

#### Authentication

Answers:

```text
Who are you?
```

Examples:

- Username and password
- Kerberos tickets
- OAuth login

#### Authorization

Answers:

```text
What are you allowed to do?
```

Examples:

- View books
- Add books
- Administrative access

---

## Question 3

### What is Single Sign On (SSO)?

✅ SSO is a secured technology where the user has to log in only once to access multiple applications.

### Explanation

SSO allows users to authenticate once and gain access to multiple authorized applications.

Example:

```text
Login Once
     |
     +-- Gmail
     +-- Teams
     +-- SharePoint
     +-- Internal Apps
```

Benefits:

- Improved user experience
- Centralized authentication
- Reduced password fatigue

---

## Question 4

### What is OpenSSL?

✅ OpenSSL is a library used in communication to encrypt and decrypt messages for security purposes.

### Explanation

OpenSSL is an open-source cryptographic library used for:

- Encryption
- Decryption
- Public/private key generation
- Digital signatures
- Certificate management

Common commands:

```bash
openssl genrsa
openssl rsa
openssl dgst
```

---

## Question 5

### Which of the following keys does OpenSSL work with?

✅ Both private and public keys

### Explanation

OpenSSL uses key pairs:

#### Private Key

Used for:

- Signing
- Decryption

#### Public Key

Used for:

- Verification
- Encryption

Example:

```bash
openssl genrsa -out private.pem 512

openssl rsa -in private.pem -pubout > public.pem
```

---

## Question 6

### What is RSA?

✅ RSA is an encryption algorithm that uses public and private keys.

### Explanation

RSA (Rivest-Shamir-Adleman) is a public-key cryptography algorithm.

RSA supports:

- Encryption
- Decryption
- Digital signatures
- Authentication

RSA uses:

```text
Public Key
Private Key
```

to establish secure communications.

---

## Question 7

### Which of the following is the correct syntax to generate a private RSA key using the OpenSSL library?

✅

```bash
openssl genrsa -out private.pem [bits]
```

### Example

```bash
openssl genrsa -out private.pem 512
```

### Explanation

- `openssl` → OpenSSL executable
- `genrsa` → Generate RSA private key
- `-out private.pem` → Output file
- `[bits]` → Key length

---

## Question 8

### Which of the following libraries can be used to sign a document for security purposes in the communication process?

✅ OpenSSL

### Example

```bash
openssl dgst -sha1 \
-sign private.pem \
-out sha1.sign \
your_document.txt
```

### Explanation

OpenSSL can generate digital signatures to verify:

- Authenticity
- Integrity
- Ownership

of a document.

---

# Key Concepts Reinforced

## Kerberos

Trusted third-party authentication protocol.

---

## Authentication

Verifies identity:

```text
Who are you?
```

---

## Authorization

Determines permissions:

```text
What can you do?
```

---

## SSO

Single login providing access to multiple applications.

---

## OpenSSL

Cryptographic library for:

- Encryption
- Decryption
- Signing
- Verification

---

## RSA

Public-key cryptography algorithm using:

- Public Keys
- Private Keys

---

## PKI

Public Key Infrastructure.

Provides trust using:

```text
Public Key
Private Key
```

pairs.

---

# Security Architecture

```text
User
   |
Authentication
   |
Kerberos / SSO
   |
Authorization
   |
Protected Resource
   |
Encryption
   |
OpenSSL / RSA
```

---

# Result

✅ 8 / 8 Questions Correct

---

# Key Takeaways

- Kerberos provides authentication services.
- Authentication verifies identity.
- Authorization determines access permissions.
- SSO allows one login for multiple systems.
- OpenSSL performs cryptographic operations.
- RSA uses public and private keys.
- OpenSSL can generate keys, encrypt data, and create digital signatures.
- Security technologies are foundational to modern client-server and distributed systems.

---

# Summary

This knowledge check reinforced the core security concepts introduced in Module 11, including authentication, authorization, Single Sign-On (SSO), Kerberos, OpenSSL, RSA encryption, public/private key cryptography, and digital signatures. Together, these technologies provide the foundation for securing modern web applications, distributed systems, and cloud-based services.