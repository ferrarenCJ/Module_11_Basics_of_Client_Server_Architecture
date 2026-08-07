# Required Coding Activity 11.4: Using Swagger to Expose an API

## Learning Outcome

Use Swagger to expose an API.

---

# Objective

In this activity you will:

1. Install Swagger UI support for Flask.
2. Run the My Books Site application.
3. Access the Swagger interface.
4. Test a GET API endpoint.
5. Test a POST API endpoint.
6. Observe API requests and responses.

---

# Background

Swagger provides an interactive interface that allows developers to:

- Document APIs
- Test APIs
- View HTTP requests
- View HTTP responses
- Debug API functionality

Swagger acts as a browser-based API testing tool.

---

# Step 1: Install flask-swagger-ui

Open VS Code.

Open a terminal.

Run:

```bash
pip install flask-swagger-ui
```

If that fails:

```bash
pip3 install flask-swagger-ui
```

Wait until installation completes successfully.

---

# Step 2: Extract Activity Files

Download:

```text
Activity 11.4.zip
```

Extract the ZIP file.

Open the extracted folder in VS Code.

You should see:

```text
app.py
templates/
swagger.json
```

(or similar supporting files)

---

# Step 3: Open app.py

Locate:

```text
app.py
```

Open the file.

Review:

- Flask Application
- API Routes
- Swagger Configuration
- Books Endpoints

---

## Screenshot #1

Capture:

- VS Code
- app.py open

Purpose:

Demonstrates that the project was opened correctly.

---

# Step 4: Run the Application

Open a terminal.

Run:

```bash
python app.py
```

Wait for Flask to start.

You should see:

```text
Running on http://localhost:5000
```

---

# Step 5: View the Application

Open your browser.

Navigate to:

```text
http://localhost:5000
```

Expected:

```text
My Books Site
```

The website should be displayed.

---

## Screenshot #2

Capture:

- Browser
- URL:

```text
http://localhost:5000
```

- My Books Site visible

Purpose:

Demonstrates that the application is running successfully.

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

---

## Screenshot #3

Capture:

- Browser
- Swagger UI opened

Purpose:

Demonstrates that Swagger is successfully connected to the API.

---

# Step 7: Test GET /books

Locate:

```text
GET /books
```

Expand the endpoint.

Select:

```text
Try it out
```

Then select:

```text
Execute
```

Swagger will send a GET request.

You should see:

### cURL Request

```bash
curl -X GET ...
```

### Response

Example:

```json
[
  {
    "author": "Hernando de Soto",
    "title": "The Mystery of Capital"
  }
]
```

---

## Screenshot #4

Capture:

- GET /books endpoint
- cURL request
- Response body

Purpose:

Demonstrates that the API successfully returned data.

---

# Step 8: Test POST /books

Locate:

```text
POST /books
```

Expand the endpoint.

Select:

```text
Try it out
```

Swagger will display a JSON request body.

Example:

```json
{
  "author": "Clifford Ferraren",
  "title": "Module 11 API Testing"
}
```

Replace values if desired.

Select:

```text
Execute
```

Swagger sends the POST request.

---

# Expected Result

The API should:

1. Receive the request.
2. Create a new book entry.
3. Return a successful response.

Example:

```json
{
  "author": "Clifford Ferraren",
  "title": "Module 11 API Testing"
}
```

---

## Screenshot #5

Capture:

- POST /books endpoint
- Request body
- Response body

Purpose:

Demonstrates that a new book was successfully created through the API.

---

# What Swagger Shows

Swagger displays:

## Endpoint

Example:

```text
GET /books
```

---

## Request

Example:

```http
GET /books HTTP/1.1
```

---

## cURL Command

Example:

```bash
curl -X GET
```

---

## Response

Example:

```json
[
  {
    "title": "Book Title"
  }
]
```

---

# API Concepts Demonstrated

## GET

Used to:

```text
Read data
```

Example:

```text
GET /books
```

---

## POST

Used to:

```text
Create data
```

Example:

```text
POST /books
```

---

## Swagger

Used to:

- Document APIs
- Test APIs
- View requests
- View responses
- Debug APIs

---

# Submission Checklist

## Screenshot 1

✅ app.py in VS Code

---

## Screenshot 2

✅ Browser showing:

```text
http://localhost:5000
```

My Books Site running

---

## Screenshot 3

✅ Swagger UI

```text
http://localhost:5000/swagger
```

---

## Screenshot 4

✅ GET /books execution

Include:

- cURL
- Response

---

## Screenshot 5

✅ POST /books execution

Include:

- Request body
- Response body

---

# Word Document

Create:

```text
Activity11_4_Clifford_J_Ferraren.docx
```

Insert all required screenshots.

Label each screenshot.

Example:

1. Opened app.py
2. My Books Site running
3. Swagger Interface
4. GET Books Request
5. POST Create Book Request

---

# Key Takeaways

- Swagger provides interactive API documentation.
- Swagger can execute API requests directly from a browser.
- GET requests retrieve data.
- POST requests create data.
- Swagger simplifies API verification and debugging.
- Flask and Swagger work together to expose and test REST APIs.