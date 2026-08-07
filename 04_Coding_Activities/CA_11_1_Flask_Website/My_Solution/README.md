# Coding Activity 11.1: Creating a Website Using Flask

## Learning Outcome

Use Flask to create a website.

---

## Objective

Create a simple Flask web application and progressively enhance it by:

1. Returning plain text from a Flask route.
2. Returning HTML content.
3. Creating an HTML template.
4. Rendering the template from Flask.
5. Displaying a personalized message.

---

## Activity Files

### Starter Files

Place instructor-provided files here:

```text
Video_Files/
```

Examples:

```text
Video_Files/
├── Video 11.2 Files
├── Final Video 11.2 Files
├── Video 11.3 Files
└── Video 11.4 Files
```

---

## Step 1: Display Plain Text

Modify `app.py` to display:

```text
My first GET request
```

Example:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "My first GET request"

if __name__ == "__main__":
    app.run(debug=True)
```

### Deliverables

Screenshot showing:

- VS Code
- Modified app.py
- Browser displaying:

```text
My first GET request
```

---

## Step 2: Return HTML

Modify `app.py` to return HTML.

Example:

```python
@app.route("/")
def index():
    return """
    <html>
        <body>
            <h1>My first GET request</h1>
        </body>
    </html>
    """
```

### Deliverables

Screenshot showing:

- Modified code
- Browser rendering HTML

---

## Step 3: Create index.html

Create:

```text
templates/
└── index.html
```

Contents:

```html
<html>
    <body>
        <h1>Hello, my name is Clifford Ferraren</h1>
    </body>
</html>
```

### Deliverables

Screenshot showing browser output.

---

## Step 4: Render Template

Update app.py:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

### Deliverables

Screenshot showing:

- Modified decorator
- render_template() usage

---

## Expected Folder Structure

```text
CA_11_1_Flask_Website
│
├── README.md
│
├── Screenshots
│   ├── Step1_Code.png
│   ├── Step1_Browser.png
│   ├── Step2_Code.png
│   ├── Step2_Browser.png
│   ├── Step3_Browser.png
│   └── Step4_Code.png
│
├── My_Solution
│   ├── app.py
│   └── templates
│       └── index.html
│
└── Video_Files
    ├── Video 11.2 Files
    ├── Final Video 11.2 Files
    ├── Video 11.3 Files
    └── Video 11.4 Files
```

---

## Submission Checklist

### Required Screenshots

- [ ] Modified app.py displaying "My first GET request"
- [ ] Browser displaying "My first GET request"
- [ ] Modified app.py displaying HTML
- [ ] Browser displaying HTML output
- [ ] Browser displaying "Hello, my name is Clifford J Ferraren"
- [ ] Modified app.py showing render_template()

### Required Files

- [xapp.py
- [x] [templates/index.html[x] [Activity11_1_Clifford_J_Ferraren.zip](./Activity11_1_Clifford_J_Ferraren.zip

## Final Submission

### Submission Package

📦 **Download ZIP**

./Activity11_1_Clifford_J_Ferraren.zip

### Location

```text
My_Solution/
└── Activity11_1_Clifford_J_Ferraren.zip
```

Contents:

- Modified Flask project
- app.py
- templates/index.html
- Word document containing required screenshots