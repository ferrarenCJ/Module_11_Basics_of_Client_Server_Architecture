# Video 11.1: Introduction

**Duration:** 04:51

## Summary

This video introduces the foundational concepts of client-server architecture and web computing. Modern web applications operate using a request-response model where clients send requests to web servers and receive responses containing web pages, data, or other resources.

The video provides an overview of Flask, Jinja templating, HTTP communication, distributed computing, cookies, APIs, Swagger documentation, and security technologies that will be covered throughout Module 11.

---

## Key Concepts

### Client-Server Architecture

Client-server architecture separates responsibilities between:

- Clients (web browsers or applications)
- Servers (systems that process requests and return responses)

Communication occurs through a request-response model.

Example:

```text
Browser --> Request --> Web Server
Browser <-- Response <-- Web Server
```

---

### HTTP

HTTP (Hypertext Transfer Protocol) is the universal messaging language used by web applications.

HTTP allows systems developed in different languages to communicate effectively, including:

- Python
- JavaScript
- Go
- .NET

---

### Flask

Flask is a Python framework used to build web applications and web servers.

Throughout this module Flask will be used to:

- Create web applications
- Process requests
- Return responses
- Build APIs

---

### Jinja

Jinja is Flask's templating engine.

Jinja allows developers to:

- Combine Python code with HTML
- Render dynamic content
- Display variables within web pages

---

### Flask Routes

Routes connect URLs to server-side functions.

A route allows the client to trigger a specific function running on the server.

Example:

```python
@app.route("/")
def home():
    return "Hello World"
```

Routes form the foundation of distributed computing because they enable code execution on remote systems.

---

### Distributed Computing

Distributed computing occurs when one system can invoke functionality on another system across a network.

Basic process:

1. Client sends request
2. Server executes function
3. Server returns response
4. Client processes results

---

### Stateless Web Servers

Web servers are generally stateless.

This means:

- Servers do not remember previous requests
- Each request is treated independently
- User identity must be maintained externally

Benefits include:

- Scalability
- Reduced memory usage
- Better performance

---

### Cookies

Cookies provide a mechanism for maintaining user identity between requests.

Cookies can:

- Identify users
- Preserve session information
- Maintain login status
- Personalize user experiences

Special focus is placed on Session Cookies in this module.

---

### APIs

API stands for Application Programming Interface.

APIs allow software systems to communicate using structured requests and responses.

Topics covered later in the module include:

- REST APIs
- Protected API routes
- API documentation

---

### Swagger

Swagger is a tool used to document APIs.

Swagger helps developers understand:

- Available endpoints
- Required parameters
- Expected responses
- API structure

Benefits:

- Easier integration
- Improved testing
- Better documentation

---

## Security Concepts Introduced

### Security Tokens

Security tokens help establish trust between systems.

They are commonly used to:

- Authenticate users
- Authorize requests
- Secure communications

---

### Kerberos

Kerberos is an authentication protocol used to demonstrate the importance of security tokens and identity verification.

---

### Public Key Infrastructure (PKI)

PKI uses public and private keys to establish trust and secure communication.

Common uses include:

- Authentication
- Digital signatures
- Encryption

---

### Public and Private Keys

Private Key

- Kept secret
- Used to sign messages

Public Key

- Shared publicly
- Used to verify signatures

Example:

GitHub can verify that commits originate from you by validating signatures using your public key.

---

### OAuth2

OAuth2 is a modern authorization framework used to provide secure access to applications and services.

OAuth2 is one of the major security standards discussed in this module.

---

## Technologies Covered in Module 11

- Flask
- Jinja
- HTTP
- Cookies
- Session Cookies
- REST APIs
- Swagger
- Kerberos
- Public Key Infrastructure (PKI)
- OAuth2
- GitHub Key Authentication

---

## Important Terms

| Term | Definition |
|--------|------------|
| Client | System requesting services from a server |
| Server | System responding to client requests |
| HTTP | Protocol used for web communication |
| Flask | Python web application framework |
| Jinja | Python templating engine used by Flask |
| Route | URL mapped to a server function |
| Cookie | Data used to maintain state between requests |
| Session Cookie | Temporary cookie identifying a user session |
| API | Interface allowing software communication |
| Swagger | API documentation framework |
| Kerberos | Network authentication protocol |
| PKI | Public Key Infrastructure |
| OAuth2 | Authorization framework for secure access |

---

## Key Takeaways

- Web applications use a client-server request-response model.
- HTTP serves as the universal communication language of the web.
- Flask and Jinja are used together to build dynamic web applications.
- Routes enable distributed computing by allowing remote function execution.
- Web servers are stateless and rely on cookies for session management.
- Swagger helps document and expose APIs.
- Security concepts such as Kerberos, PKI, digital signatures, and OAuth2 are critical components of modern web applications.