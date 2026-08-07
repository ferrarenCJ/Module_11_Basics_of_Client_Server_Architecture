# Coding Activity 11.2: Adding a Cookie to a Website

## Learning Outcome

Create and retrieve cookies from a website.

---

## Objective

Learn how to:

- Create cookies using Flask
- Store cookies in a browser
- Retrieve cookie values
- Handle missing cookies
- Remove cookies
- Inspect browser cookie storage

---

## Activity Overview

This activity extends a Flask application by implementing cookie management.

You will:

1. Create a cookie
2. Store the cookie in the browser
3. Retrieve the cookie value
4. Handle missing cookies
5. Remove cookies

---

## Folder Structure

```text
CA_11_2_Cookies
│
├── README.md
├── Screenshots
├── My_Solution
│   ├── app.py
│   └── templates
│
└── Video_Files
    ├── Activity_11_2.zip
    └── Related_Files
```

---

## Step 1: Run the Application

Open the project in VS Code.

Run:

```bash
python app.py
```

Navigate to:

```text
http://localhost:88
```

Expected output:

```text
Practicing Cookies!
```

### Deliverable

Screenshot showing:

- VS Code
- app.py
- Browser displaying:

```text
Practicing Cookies!
```

---

## Step 2: Create a Cookie

Complete:

```python
def addCookie():
```

Create a cookie named:

```text
myFirstCookie
```

Value:

```text
Hello World - my first cookie!
```

Example:

```python
@app.route('/addCookie')
def addCookie():
    response = make_response("Cookie added!")
    response.set_cookie(
        "myFirstCookie",
        "Hello World - my first cookie!"
    )
    return response
```

### Test

Navigate to:

```text
http://localhost:88/addCookie
```

Expected:

```text
Cookie added!
```

### Deliverables

- Screenshot of completed method
- Screenshot of browser output
- Screenshot showing cookie in browser settings

---

## Step 3: Display Cookie Value

Complete:

```python
def displayCookieValue():
```

Requirements:

### If Cookie Exists

Display:

```text
Found the cookie:
Hello World - my first cookie!
```

### If Cookie Does Not Exist

Display:

```text
Cookie not found!
```

Example:

```python
@app.route('/displayCookieValue')
def displayCookieValue():
    try:
        cookieValue = request.cookies.get("myFirstCookie")

        if cookieValue:
            return (
                "Found the cookie: "
                + cookieValue
            )
        else:
            return "Cookie not found!"

    except:
        return "Cookie not found!"
```

### Test

Navigate to:

```text
http://localhost:88/displayCookieValue
```

### Deliverables

- Screenshot of completed method
- Screenshot displaying cookie value

---

## Step 4: Delete Cookie Manually

Using browser settings:

1. Locate:

```text
myFirstCookie
```

2. Delete it

3. Refresh:

```text
http://localhost:88/displayCookieValue
```

Expected:

```text
Cookie not found!
```

### Deliverable

Screenshot showing:

```text
Cookie not found!
```

---

## Step 5: Remove Cookie Using Flask

Complete:

```python
def removeCookie():
```

Example:

```python
@app.route('/removeCookie')
def removeCookie():
    response = make_response(
        "Cookie Removed"
    )

    response.set_cookie(
        "myFirstCookie",
        "",
        max_age=0
    )

    return response
```

### Purpose

```python
max_age=0
```

forces the browser to delete the cookie.

---

## Testing Cookie Removal

### First

Create the cookie:

```text
http://localhost:88/addCookie
```

### Verify

Check browser settings.

Cookie should exist.

### Then

Navigate to:

```text
http://localhost:88/removeCookie
```

Expected:

```text
Cookie Removed
```

### Verify

Check browser settings.

Cookie should no longer exist.

---

## Flask Cookie Functions

### Create Cookie

```python
response.set_cookie(
    "myFirstCookie",
    "Hello World - my first cookie!"
)
```

### Read Cookie

```python
request.cookies.get(
    "myFirstCookie"
)
```

### Remove Cookie

```python
response.set_cookie(
    "myFirstCookie",
    "",
    max_age=0
)
```

---

## Cookie Lifecycle

```text
Create Cookie
      |
      v
Browser Stores Cookie
      |
      v
Browser Sends Cookie
with Future Requests
      |
      v
Read Cookie Value
      |
      v
Delete Cookie
```

---

## Required Screenshots

### Step 1

- [ ] app.py in VS Code
- [ ] Browser displaying "Practicing Cookies!"

### Step 2

- [ ] Completed addCookie method
- [ ] Browser displaying "Cookie added!"
- [ ] Browser settings showing myFirstCookie

### Step 3

- [ ] Completed displayCookieValue method
- [ ] Browser showing cookie value

### Step 4

- [ ] Browser displaying "Cookie not found!"

### Step 5

- [ ] Completed removeCookie method
- [ ] Browser settings confirming cookie removal

---

## Submission Package

### Word Document

Include all required screenshots.

### Final Deliverable

```text
Activity11_2_Clifford_J_Ferraren.docx
```

or

```text
Activity11_2_Clifford_J_Ferraren.zip
```

depending on instructor requirements.

---

## Key Takeaways

- Cookies are stored in the browser.
- Browsers automatically return cookies with future requests.
- Flask can create, retrieve, and delete cookies.
- Session management depends on cookies.
- Removing a cookie is accomplished using:

```python
max_age=0
```

- Cookies help maintain state in the stateless HTTP protocol.