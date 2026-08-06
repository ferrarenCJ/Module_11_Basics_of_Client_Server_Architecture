# Mini-Lesson 11.1: Flask Web Server

## What Is Flask?

Flask is a lightweight Python web framework used for building web applications.

It provides:

- Routing
- HTTP request handling
- Template rendering
- Session management
- Web application development tools

Applications can run locally during development or be deployed to production web servers.

---

## Advantages of Flask

### Simplicity

Flask applications require very little code to get started.

### Python-Based

All logic is written in Python.

### Lightweight

Flask includes only the essential components needed for web development.

### Extensible

Additional functionality can be added through plugins and extensions.

---

## Requirements for Flask Development

To build a Flask application you need:

- Python
- Flask
- A code editor (VS Code recommended)
- A project directory

Example:

```bash
mkdir flask_project
cd flask_project
```

---

## Basic Flask Application Structure

Example:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )
```

---

## Core Components

### Flask Application Object

```python
app = Flask(__name__)
```

Creates the web application instance.

---

### Route Decorator

```python
@app.route('/')
```

Maps a URL to a Python function.

---

### Route Function

```python
def index():
```

Executed whenever a request reaches the mapped route.

---

### Application Startup

```python
app.run()
```

Starts the Flask development web server.

---

## HTTP Methods

Flask routes can handle different request types.

Examples:

### GET

Retrieve information.

```python
@app.route("/", methods=["GET"])
```

### POST

Submit information to the server.

```python
@app.route("/login", methods=["POST"])
```

---

## Using HTML with Flask

Instead of returning plain strings:

```python
return "Hello World"
```

Flask can render HTML pages.

---

## Templates Folder

Flask automatically looks for HTML files inside:

```text
templates/
```

Example:

```text
project/
│
├── app.py
│
└── templates/
    └── index.html
```

---

## Rendering HTML Templates

Import:

```python
from flask import render_template
```

Use:

```python
@app.route("/")
def index():
    return render_template("index.html")
```

Flask loads the file from:

```text
templates/index.html
```

and returns it to the browser.

---

## Multiple Templates

Applications can contain many pages.

Example:

```text
templates/
│
├── index.html
├── books.html
├── register.html
└── login.html
```

Each template should have a corresponding Flask route.

---

## Request Flow

```text
Browser
    |
HTTP Request
    |
Flask Route
    |
Python Function
    |
render_template()
    |
HTML Page
    |
Browser
```

---

## Key Takeaways

- Flask is a lightweight Python web framework.
- Flask applications are written primarily in Python.
- Routes connect URLs to Python functions.
- HTML files are stored inside the templates directory.
- render_template() loads HTML pages and sends them to the browser.
- Flask supports GET and POST requests.
- Flask can scale from simple local applications to production websites.