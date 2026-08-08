# Mini-Lesson 11.5: OpenSSL

## What Is OpenSSL?

OpenSSL is an open-source cryptographic library used to:

- Encrypt data
- Decrypt data
- Generate cryptographic keys
- Create digital signatures
- Verify signatures
- Secure communications

OpenSSL is widely used in web applications, cloud platforms, enterprise systems, and secure network communications.

---

## Why OpenSSL Is Important

OpenSSL helps protect:

- Sensitive information
- User credentials
- Files
- Network communications

Common use cases:

- HTTPS websites
- SSL/TLS certificates
- Public Key Infrastructure (PKI)
- Digital signing
- Encryption and decryption

---

## General Command Syntax

```bash
openssl command [command_options] [command_arguments]
```

Example:

```bash
openssl version
```

Displays the installed OpenSSL version.

---

# Public Key Infrastructure (PKI)

PKI uses a pair of keys:

## Private Key

- Kept secret
- Used for signing
- Used for decryption

## Public Key

- Shared publicly
- Used for verification
- Used for encryption

---

## Key Pair Relationship

```text
Private Key
      |
      |
Public Key
```

The two keys are mathematically related.

---

# Generating a Private Key

Generate an RSA private key:

```bash
openssl genrsa -out private.pem 512
```

### Explanation

```text
genrsa
```

Generate RSA private key.

```text
-out private.pem
```

Save key to:

```text
private.pem
```

```text
512
```

Key size in bits.

---

## Output

```text
private.pem
```

Example:

```text
-----BEGIN RSA PRIVATE KEY-----
...
-----END RSA PRIVATE KEY-----
```

---

# Generating a Public Key

Create a public key from the private key:

```bash
openssl rsa -in private.pem -pubout > public.pem
```

### Explanation

```text
-in private.pem
```

Read existing private key.

```text
-pubout
```

Generate public key.

```text
> public.pem
```

Save to:

```text
public.pem
```

---

## Output

```text
public.pem
```

Example:

```text
-----BEGIN PUBLIC KEY-----
...
-----END PUBLIC KEY-----
```

---

# Digital Signing

A digital signature proves:

- Identity
- Authenticity
- Integrity

---

## Create a Document

Example:

```text
your_document.txt
```

Contents:

```text
Hello World
```

---

## Sign the Document

```bash
openssl dgst -sha1 -sign private.pem -out sha1.sign your_document.txt
```

---

### Explanation

```text
dgst
```

Digest operation.

```text
-sha1
```

Hash algorithm.

```text
-sign private.pem
```

Use private key to sign.

```text
-out sha1.sign
```

Save signature.

---

## Output Files

```text
your_document.txt
sha1.sign
```

---

# Verify a Signature

Verify the document using the public key.

```bash
openssl dgst -sha1 -verify public.pem -signature sha1.sign your_document.txt
```

---

## Verification Result

Successful:

```text
Verified OK
```

Failed:

```text
Verification Failure
```

---

# Encryption

Encryption converts readable data into ciphertext.

```text
Plain Text
      |
Encryption
      |
Cipher Text
```

---

## Encrypt a Document

```bash
openssl rsautl -encrypt \
-pubin \
-inkey public.pem \
-ssl \
-in your_document.txt \
-out your_encrypted_document.txt
```

---

### Explanation

```text
-encrypt
```

Encrypt data.

```text
-pubin
```

Input is a public key.

```text
-inkey public.pem
```

Use public key.

```text
-in your_document.txt
```

File to encrypt.

```text
-out your_encrypted_document.txt
```

Encrypted output.

---

## Output

```text
your_encrypted_document.txt
```

Contains encrypted data.

---

# Decryption

Decryption converts ciphertext back into readable data.

```text
Cipher Text
      |
Decryption
      |
Plain Text
```

---

## Decrypt a Document

```bash
openssl rsautl -decrypt \
-inkey user_private.pem \
-in user_document.txt \
-out user_decrypted_document.txt
```

---

### Explanation

```text
-decrypt
```

Decrypt input file.

```text
-inkey user_private.pem
```

Private key used for decryption.

```text
-in user_document.txt
```

Encrypted file.

```text
-out user_decrypted_document.txt
```

Decrypted output.

---

# OpenSSL Workflow

```text
Generate Private Key
          |
Generate Public Key
          |
Sign Document
          |
Verify Signature
          |
Encrypt Document
          |
Decrypt Document
```

---

# Common Hash Algorithms

## SHA1

```bash
-sha1
```

Historically common.

---

## SHA256

```bash
-sha256
```

More secure.

---

## SHA384

```bash
-sha384
```

Enhanced security.

---

## SHA512

```bash
-sha512
```

Highest commonly used SHA family strength.

---

# GitHub Connection

GitHub commonly uses:

- Public Keys
- Private Keys
- SSH Authentication
- Signed Commits

Purpose:

- Verify developer identity
- Secure repository access

---

# Data Engineering Connections

## Cloud Platforms

Security mechanisms in:

- AWS
- Azure
- Google Cloud

rely heavily on PKI concepts.

---

## Data Pipelines

Encryption protects:

- Sensitive files
- Credentials
- Data transfers

---

## Enterprise Applications

Digital signatures help ensure:

- Data integrity
- User identity verification
- Secure communications

---

# Important Terms

| Term | Definition |
|--------|------------|
| OpenSSL | Cryptographic library for security operations |
| PKI | Public Key Infrastructure |
| RSA | Public key cryptographic algorithm |
| Private Key | Secret key used for signing and decryption |
| Public Key | Shared key used for verification and encryption |
| Encryption | Conversion of data into ciphertext |
| Decryption | Restoration of ciphertext to readable form |
| Digital Signature | Verification of authenticity and integrity |
| SHA | Family of cryptographic hash functions |

---

# Questions for Review

- What is the difference between a public and private key?
- Why are digital signatures useful?
- What is the purpose of encryption?
- How does PKI establish trust?
- Why is OpenSSL important for distributed systems?

---

# Key Takeaways

- OpenSSL is a security-focused cryptographic library.
- RSA uses public/private key pairs.
- Private keys are used for signing and decryption.
- Public keys are used for verification and encryption.
- Digital signatures verify authenticity and integrity.
- Encryption protects sensitive information.
- OpenSSL forms the foundation of many secure internet communications.

---

# Summary

OpenSSL provides tools for generating keys, signing documents, verifying signatures, encrypting data, and decrypting information. It relies heavily on Public Key Infrastructure (PKI), which uses public and private key pairs to establish trust and secure communications. These concepts are foundational to modern cybersecurity, cloud platforms, and distributed computing systems.