# Required Coding Activity 11.4: Using Swagger to Expose an API

## Learning Outcome

Use Swagger to expose an API.

---

# Objective

In this activity, you will:

1. Install Swagger support for Flask.
2. Run the My Books Site application.
3. Open the Swagger interface.
4. Use Swagger to execute a GET request.
5. Use Swagger to execute a POST request.
6. Observe how APIs can be tested through Swagger.

---

# Understanding the Application

The provided application already contains:

## Flask Application

```python
app = Flask(__name__)
```

## Swagger Configuration

```python
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"
```

This configuration tells Flask:

```text
Swagger UI
        |
        v
/static/swagger.json
```

The Swagger interface reads the API definitions from:

```text
static/swagger.json
```

and automatically generates documentation and testing screens.

---

# Step 1: Install flask-swagger-ui

Open VS Code.

Open Terminal.

Run:

```bash
pip install flask-swagger-ui
```

If pip fails:

```bash
pip3 install flask-swagger-ui
```

Wait until installation completes.

---

## Verify Installation

Run:

```bash
pip show flask-swagger-ui
```

Expected:

```text
Name: flask-swagger-ui
```

---

# Step 2: Extract Activity Files

Download:

```text
Activity 11.4.zip
```

Extract the files.

Open the folder in VS Code.

You should see files similar to:

```text
app.py
static/
templates/
swagger.json
```

---

# Step 3: Open app.py

Open:

```text
app.py
```

Review the important sections.

### Swagger Setup

```python
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"
```

### Books API

```python
@app.route("/books")
def getBooks():
```

### Add Book API

```python
@app.route("/addbook")
def addBook():
```

---

## Screenshot #1

Capture:

- VS Code
- app.py open

This satisfies:

> Screenshot of Visual Studio Code showing app.py from the Activity 11.4 zip file.

---

# Step 4: Run the Application

Open a terminal.

Run:

```bash
python app.py
```

Expected:

```text
Running on http://127.0.0.1:5000
```

---

# Step 5: Open My Books Site

Navigate to:

```text
http://localhost:5000
```

Expected:

```text
Register Page
```

or

```text
My Books Site
```

depending on the provided files.

The site should load successfully.

---

## Screenshot #2

Capture:

```text
http://localhost:5000
```

with the application running.

This satisfies:

> Screenshot of the web browser pointing to localhost:5000 and showing the application running.

---

# Step 6: Open Swagger

Navigate to:

```text
http://localhost:5000/swagger
```

Swagger UI should appear.

You should see available API endpoints.

Examples:

```text
GET /books
POST /books
```

If Swagger loads, the Swagger configuration is working correctly.

---

## Screenshot #3

Capture:

```text
http://localhost:5000/swagger
```

showing Swagger UI.

This satisfies:

> Screenshot of the browser pointing to localhost:5000/swagger

---

# Step 7: Test GET Books API

Locate:

```text
GET /books
```

inside Swagger.

Select:

```text
GET
```

Expand the endpoint.

Select:

```text
Try it out
```

Swagger will enable the Execute button.

Select:

```text
Execute
```

---

# What Swagger Does

Swagger generates:

```bash
curl -X GET ...
```

and sends the request to Flask.

Flask executes:

```python
@app.route("/books")
def getBooks():
```

and returns:

```python
books
```

---

# Expected Response

Example:

```json
[
  {
    "author": "Hernando de Soto",
    "title": "The Mystery of Capital"
  },
  {
    "author": "Hans Christian Andersen",
    "title": "Fairy Tales"
  }
]
```

---

## Screenshot #4

Capture all of:

- GET endpoint
- Try it out
- Execute
- cURL request
- Response section

This satisfies:

> Screenshot of the call to GET method to get books, including output.

---

# Step 8: Test POST Books API

Locate:

```text
POST /books
```

inside Swagger.

Expand the endpoint.

Select:

```text
Try it out
```

Swagger displays a request body.

---

# Add a New Book

Enter:

```json
{
  "author": "Clifford Ferraren",
  "title": "Module 11 Swagger Testing"
}
```

or any author/title of your choice.

Select:

```text
Execute
```

---

# What Happens Internally

Swagger sends:

```http
POST /books
```

Flask executes:

```python
@app.route("/addbook")
def addBook():
```

A new book is added to:

```python
books.append(newbook)
```

---

# Expected Response

Example:

```json
{
  "author": "Clifford Ferraren",
  "title": "Module 11 Swagger Testing"
}
```

or a success response showing the updated books list.

---

## Screenshot #5

Capture:

- POST endpoint
- Request body
- Execute button
- Response section

This satisfies:

> Screenshot of the call to POST method to create a book, including output.

---

# Optional Verification

Execute:

```text
GET /books
```

again.

Verify your newly added book appears.

Example:

```json
{
  "author": "Clifford Ferraren",
  "title": "Module 11 Swagger Testing"
}
```

This confirms the POST request succeeded.

---

# Understanding the Swagger Architecture

```text
Browser
    |
    v
Swagger UI
    |
    v
REST API
    |
    v
Flask Route
    |
    v
Books Data
```

Swagger acts as a testing interface between the browser and API.

---

# API Concepts Demonstrated

## GET

Retrieve data.

Example:

```http
GET /books
```

---

## POST

Create data.

Example:

```http
POST /books
```

---

## REST API

Uses:

- URL
- HTTP Method
- JSON Data

to communicate.

---

## Swagger

Provides:

- API documentation
- Testing interface
- Debugging support

without writing client code.

---

# Submission Checklist

## Screenshot 1

✅ app.py open in VS Code

---

## Screenshot 2

✅ Application running at localhost:5000

---

## Screenshot 3

✅ Swagger UI at localhost:5000/swagger

---

## Screenshot 4

✅ GET /books execution

Include:

- cURL request
- JSON response

---

## Screenshot 5

✅ POST /books execution

Include:

- Request body
- JSON response

---

# Word Document

Create:

```text
Activity11_4_Clifford_J_Ferraren.docx
```

Include:

1. Opened app.py
2. My Books Site running
3. Swagger Interface
4. GET Books Request
5. POST Create Book Request

Label each screenshot clearly.

---

# Key Takeaways

- Swagger automatically documents APIs.
- Swagger can execute API calls directly from a browser.
- GET requests retrieve information.
- POST requests create information.
- Flask routes become API endpoints.
- Swagger simplifies API development, testing, and debugging.