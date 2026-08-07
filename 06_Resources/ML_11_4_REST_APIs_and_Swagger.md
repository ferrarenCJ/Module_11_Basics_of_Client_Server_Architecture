# Mini-Lesson 11.4: REST APIs and Swagger

## What Are APIs?

An API (Application Programming Interface) enables applications to communicate with one another.

Examples:

- Web browser ↔ Web application
- Mobile app ↔ Cloud service
- Dashboard ↔ Database
- Flask application ↔ External service

APIs provide a standardized method for sending requests and receiving responses.

---

## Types of APIs

Two common API styles are:

### SOAP

SOAP stands for:

```text
Simple Object Access Protocol
```

Characteristics:

- Formal specification
- Maintained by W3C
- XML-based messaging
- Strict standards

Advantages:

- Strong security
- Formal contracts
- Enterprise integration

---

### REST

REST stands for:

```text
Representational State Transfer
```

Characteristics:

- Lightweight
- URL-based
- HTTP-driven
- Data-focused

Advantages:

- Simplicity
- Scalability
- Flexibility
- Broad adoption

---

## What Is a REST API?

REST APIs follow the REST architectural style.

REST APIs are often called:

```text
RESTful APIs
```

REST APIs expose resources through URLs and use HTTP methods to interact with those resources.

Example:

```text
GET /books
```

Returns information about books.

---

## Six REST Design Principles

### 1. Uniform Interface

Each request identifies resources using a URL.

Example:

```text
/books
/books/1
/users
```

Resources are separated from how they are presented to the client.

---

### 2. Client-Server Decoupling

The client and server operate independently.

Benefits:

- Easier maintenance
- Scalability
- Technology flexibility

Example:

```text
Browser
    |
REST API
    |
Database
```

The browser does not need to know how data is stored.

---

### 3. Statelessness

Every request must contain all required information.

The server does not remember previous requests.

Example:

```text
Request 1
Request 2
Request 3
```

Each request is processed independently.

---

### 4. Cacheability

Responses should be cacheable whenever possible.

Benefits:

- Faster performance
- Reduced network traffic
- Better scalability

---

### 5. Layered System Architecture

Requests may travel through multiple layers.

Example:

```text
Browser
    |
Load Balancer
    |
API Gateway
    |
Application Server
    |
Database
```

Clients do not need to know the internal architecture.

---

### 6. Code on Demand (Optional)

Servers may provide executable code.

Examples:

- JavaScript
- Scripts
- Embedded logic

This principle is optional.

---

## REST API Operations

REST APIs generally support CRUD operations.

### Create

```http
POST
```

Create new records.

Example:

```text
POST /books
```

---

### Read

```http
GET
```

Retrieve records.

Example:

```text
GET /books
```

---

### Update

```http
PUT
```

Update records.

Example:

```text
PUT /books/1
```

---

### Delete

```http
DELETE
```

Delete records.

Example:

```text
DELETE /books/1
```

---

## REST Architecture

```text
Client
    |
HTTP Request
    |
REST API
    |
Business Logic
    |
Database
    |
HTTP Response
    |
Client
```

---

## REST APIs in Module 10

Module 10 used REST APIs through Postman.

Methods used:

| Method | Purpose |
|----------|----------|
| GET | Retrieve records |
| POST | Create records |
| PUT | Update records |
| DELETE | Delete records |

Example:

```text
GET /api/books
```

---

# Swagger

## What Is Swagger?

Swagger is a framework for documenting and testing APIs.

Swagger helps developers understand:

- Endpoints
- Parameters
- Request formats
- Response formats

without reading source code.

---

## Swagger Capabilities

### API Documentation

Swagger automatically documents:

- Routes
- Inputs
- Outputs
- HTTP methods

---

### Interactive Testing

Developers can:

- Send requests
- Test responses
- Validate APIs

directly from the browser.

---

### Development Support

Swagger simplifies:

- Development
- Validation
- Debugging
- Collaboration

---

## Example

Swagger may display:

```text
GET /books

POST /books

PUT /books/{id}

DELETE /books/{id}
```

and allow developers to execute these requests.

---

## Swagger and the Books Application

The Books application exposes API endpoints that can be documented using Swagger.

Benefits:

- Easier development
- Better testing
- Improved visibility into API behavior

---

# OpenAPI 3.0

## What Is OpenAPI?

OpenAPI 3.0 is an open standard specification for describing REST APIs.

Swagger tools use OpenAPI specifications.

OpenAPI provides a machine-readable definition of an API.

---

## OpenAPI Features

### Enhanced API Design

Supports:

- Examples
- Media types
- Request definitions
- Response definitions

---

### Reusable Components

Allows reuse of:

- Schemas
- Parameters
- Responses
- Security definitions

---

### Security Support

Supports:

- OAuth 2.0
- OpenID Connect
- Authentication frameworks

---

### Documentation Generation

Works with tools such as:

- Swagger UI
- Redoc
- Postman

---

## OpenAPI Use Cases

### API Documentation

Generate interactive documentation automatically.

---

### Code Generation

Generate:

- Client SDKs
- Server stubs
- Documentation

---

### Testing

Use specifications as the basis for automated testing.

---

### Collaboration

Provides a common contract for development teams.

---

## OpenAPI Development Workflow

```text
API Design
     |
OpenAPI Specification
     |
Documentation
     |
Testing
     |
Automation
     |
Deployment
```

---

## Swagger vs OpenAPI

| Swagger | OpenAPI |
|----------|----------|
| Toolset | Specification |
| Swagger UI | OpenAPI Definition |
| Testing and Documentation | API Standards |
| Implementation Tools | API Description Format |

---

## Data Engineering Connections

### Data Services

REST APIs commonly expose:

- Data pipelines
- Data quality services
- Metrics
- Analytics

---

### Cloud Platforms

Modern cloud services expose APIs.

Examples:

- AWS
- Azure
- Google Cloud

---

### Enterprise Systems

REST APIs integrate:

- Applications
- Databases
- Dashboards
- Data warehouses

---

## Important Terms

| Term | Definition |
|--------|------------|
| API | Application Programming Interface |
| REST | Representational State Transfer |
| RESTful API | API following REST principles |
| Endpoint | URL exposed by an API |
| Swagger | API documentation and testing framework |
| OpenAPI | REST API specification standard |
| GET | Retrieve data |
| POST | Create data |
| PUT | Update data |
| DELETE | Remove data |
| Cache | Temporary storage for faster access |
| Stateless | Every request contains all required information |

---

## Questions for Review

- What is the difference between SOAP and REST?
- What are the six REST principles?
- Why is statelessness important?
- What advantages does Swagger provide?
- How does OpenAPI improve API development?
- When should GET, POST, PUT, and DELETE be used?

---

## Key Takeaways

- REST APIs provide a lightweight and scalable approach to application communication.
- REST follows six architectural principles.
- CRUD operations map naturally to HTTP methods.
- Swagger provides interactive API documentation and testing.
- OpenAPI is the modern standard for describing REST APIs.
- APIs are foundational components of modern cloud and data engineering systems.

---

## Summary

REST APIs allow applications to communicate through standardized HTTP requests and responses. They follow six design principles that promote scalability, flexibility, and maintainability. Swagger simplifies API documentation and testing, while OpenAPI 3.0 provides a standard specification for designing, documenting, testing, and automating REST APIs. Together, these technologies form the foundation of modern web services and cloud-based architectures.