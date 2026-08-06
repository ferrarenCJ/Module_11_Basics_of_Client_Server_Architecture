# Videos 11.2-11.4: Creating a Website Using Flask

## Summary

This section introduces Flask, a lightweight Python web framework for building web applications. Using Flask and the Jinja templating language, developers can create dynamic web pages, pass data between Python and HTML, and build interactive websites.

The section progresses from creating a simple "Hello World" application to implementing user authentication using HTTP requests, responses, and session cookies.

---

# Video 11.2: Basics of Flask Web Server - Part 1

## Summary

Flask is a Python framework used to build web applications and web servers.

Dr. Williams demonstrates how to:

- Install and configure Flask
- Create a basic Flask application
- Define routes
- Start a web server
- Build a "Hello World" website

Jinja is introduced as a templating language that allows Flask applications to generate HTML content dynamically.

## Key Concepts

### Flask

- Lightweight Python web framework
- Used to create web applications
- Handles HTTP requests and responses
- Supports routing and templates

### Route

A route maps a URL to a Python function.

Example:

```python
@app.route("/")
def home():
    return "Hello World"
```

### Hello World Application

The simplest web application that confirms the server is working correctly.

### Jinja

- Python templating engine
- Combines Python data with HTML templates
- Renders dynamic content

## Key Takeaway

Flask makes it easy to create and deploy web applications using Python.

---

# Video 11.3: Basics of Flask Web Server - Part 2

## Summary

This video demonstrates how Flask and Jinja work together to generate web content dynamically.

Variables and data structures are passed from Python code to HTML templates, allowing webpages to display data dynamically.

## Key Concepts

### Dynamic Content

Content generated at runtime using application data.

### Template Rendering

Flask sends variables to HTML templates.

Example:

```python
return render_template(
    "books.html",
    books=book_list
)
```

### Jinja Variables

Variables can be displayed inside HTML pages.

Example:

```html
{{ title }}
```

### Jinja Loops

Display multiple records dynamically.

Example:

```html
{% for book in books %}
    <p>{{ book }}</p>
{% endfor %}
```

## Benefits

- Separates presentation from business logic
- Keeps code organized
- Supports reusable templates

## Key Takeaway

Jinja allows Python applications to render dynamic HTML pages efficiently.

---

# Video 11.4: Flask Server Registration and Login

## Summary

This video demonstrates how Flask applications handle authentication and distributed computing concepts using HTTP requests, responses, and session cookies.

The Books web application is enhanced with user registration and login functionality.

## Key Concepts

### HTTP Request

Sent by the client to the server requesting information or actions.

Examples:

- GET
- POST

### HTTP Response

Returned by the server to the client.

May include:

- HTML pages
- JSON data
- Redirects
- Status codes

### Login Workflow

1. User submits credentials.
2. Server validates credentials.
3. Session is created.
4. User gains access to secured content.

### Session Cookie

A temporary cookie used to identify a user session.

Benefits:

- Maintains login state
- Tracks authenticated users
- Supports personalization

### Authentication

Verification of a user's identity through credentials such as:

- Username
- Password

## Distributed Computing Concepts

Client and server communicate using:

- HTTP requests
- HTTP responses
- Session state

The server processes requests while the client renders the returned content.

## Key Takeaway

Session cookies allow Flask applications to maintain user state and implement secure login functionality.

---

# Technologies Covered

- Python
- Flask
- Jinja
- HTML
- HTTP
- Session Cookies

# Important Terms

| Term | Definition |
|--------|------------|
| Flask | Python web framework for web applications |
| Jinja | Python templating engine used with Flask |
| Route | URL mapped to a Python function |
| Template | HTML file containing Jinja code |
| HTTP | Communication protocol used on the web |
| Request | Message sent from client to server |
| Response | Message returned from server to client |
| Cookie | Data stored to maintain state |
| Session Cookie | Temporary cookie used for authentication |
| Authentication | Process of verifying user identity |

# Key Takeaways

- Flask simplifies web application development.
- Jinja enables dynamic HTML generation.
- Routes connect URLs to Python functions.
- HTTP powers communication between clients and servers.
- Session cookies allow user authentication and state management.
- Flask and Jinja together create interactive web applications.