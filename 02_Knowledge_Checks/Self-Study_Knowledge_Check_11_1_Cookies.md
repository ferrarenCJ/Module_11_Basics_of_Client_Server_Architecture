# Self-Study Knowledge Check 11.1: Cookies

## Learning Outcome

Identify key client-server architecture components.

---

## Question 1

### Which Python framework can be used to write code for a web server?

✅ Flask

### Notes

Flask is a lightweight Python web framework used to create web applications and web servers.

Other options:

- SciPy → Scientific computing
- NumPy → Numerical computing
- pandas → Data analysis

---

## Question 2

### What are cookies?

✅ Cookies are files with small pieces of user information that are stored on a web browser.

### Notes

Cookies:

- Store small pieces of information
- Help websites remember users
- Maintain session state
- Support authentication

---

## Question 3

### Which Flask function can send a template as a response to an HTTP request?

✅ render_template()

### Example

```python
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")
```

### Notes

`render_template()` loads HTML files from the `templates` folder and returns them to the browser.

---

## Question 4

### How do you ensure that different functions are called for various URL routes?

✅ Use decorators, which map the functions to different routes.

### Example

```python
@app.route("/shopping")
def getcart():
    pass

@app.route("/login")
def getuser():
    pass
```

### Notes

Decorators map URLs to Python functions.

---

## Question 5

### Which of the following is the correct syntax to retrieve cookie information from an HTTP request?

✅ request.cookies.get("CookieName")

### Example

```python
username = request.cookies.get("username")
```

### Notes

Flask stores cookie information inside:

```python
request.cookies
```

---

## Key Concepts Reinforced

### Flask

Python web development framework.

### Cookies

Small pieces of information stored by a browser.

### Routes

URLs mapped to Python functions using decorators.

### Templates

HTML files rendered using:

```python
render_template()
```

### Sessions

Mechanism used to maintain user state between requests.

---

## Score

✅ 5 / 5 Questions Correct

---

## Key Takeaways

- Flask is used to build web servers and web applications.
- Cookies store user information in a browser.
- `render_template()` returns HTML templates to clients.
- Route decorators map URLs to functions.
- Cookie data can be retrieved with:

```python
request.cookies.get()
```

- Cookies and sessions are fundamental components of modern client-server applications.