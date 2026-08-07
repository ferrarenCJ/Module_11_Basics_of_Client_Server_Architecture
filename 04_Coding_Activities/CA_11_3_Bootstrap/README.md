# Coding Activity 11.3: Customizing Bootstrap Code

## Learning Outcome

Modify Bootstrap code to enhance a website.

---

## Objective

In this activity, you will:

- Run a Flask application that displays a Bootstrap table.
- Examine the table data stored in `app.py`.
- Modify the table contents.
- Display the updated information in the browser.
- Document your results with screenshots.

---

## Activity Overview

Bootstrap provides a quick way to create professional-looking tables.

In this activity, you will modify an existing Bootstrap table that contains:

- 3 Rows
- 3 Columns

The structure of the table should remain unchanged.

Only the table data should be modified.

---

## Folder Structure

```text
CA_11_3_Bootstrap
│
├── README.md
├── Screenshots
├── My_Solution
│   ├── app.py
│   └── templates
│
└── Activity_Files
    └── Activity_11_3.zip
```

---

# Step 1: Download Activity Files

Download:

```text
Activity 11.3.zip
```

Extract the files.

Open the folder in VS Code.

---

## Screenshot #1

Capture:

- VS Code
- Open project folder
- Activity 11.3 files

---

# Step 2: Open app.py

Locate:

```text
app.py
```

Review the contents.

Observe:

- Flask application
- Route definitions
- Table data
- Template rendering

---

## Screenshot #2

Capture:

- app.py opened in VS Code

---

# Step 3: Run the Application

Open a terminal.

Run:

```bash
python app.py
```

Navigate to:

```text
http://localhost:5000
```

You should see a Bootstrap table.

The table contains:

- 3 Rows
- 3 Columns

The entries are defined within:

```python
app.py
```

---

## Screenshot #3

Capture:

- Browser displaying the original table

---

# Step 4: Review the Table Data

Look for a structure similar to:

```python
table = [
    ["Value1", "Value2", "Value3"],
    ["Value4", "Value5", "Value6"],
    ["Value7", "Value8", "Value9"]
]
```

or

```python
data = [
    {
        ...
    }
]
```

The exact structure may vary.

---

# Step 5: Modify the Table Entries

Keep:

✅ 3 Rows

✅ 3 Columns

Change:

✅ Table contents

### Suggested Theme

#### Module 11 Concepts

| Topic | Technology | Purpose |
|---------|---------|---------|
| Flask | Web Framework | Build Web Server |
| Cookies | Session Management | Maintain User State |
| Bootstrap | UI Framework | Enhance Website |

#### AWS Data Engineering

| Service | Category | Purpose |
|-----------|-----------|-----------|
| S3 | Storage | Data Lake |
| Glue | ETL | Data Transformation |
| Athena | Analytics | SQL Queries |

#### MIT Course Topics

| Module | Topic | Technology |
|-----------|-----------|-----------|
| 11 | Client-Server | Flask |
| 10 | Databases | SQL |
| 9 | GitHub | Git |

Use any topic that interests you.

---

## Screenshot #4

Capture:

- First portion of modified code

If the entire code does not fit:

### Screenshot #5

Capture:

- Remaining portion of the modified code

---

# Step 6: Run the Updated Application

Save:

```text
app.py
```

Restart Flask if necessary.

Navigate to:

```text
http://localhost:5000
```

The updated Bootstrap table should display your new data.

---

## Screenshot #6

Capture:

- Browser displaying updated table

---

# Submission Checklist

## Required Screenshots

### Step 1

- [ ] Downloaded Activity 11.3 files

### Step 2

- [ ] app.py opened successfully

### Step 3

- [ ] Original table displayed

### Step 4

- [ ] Modified table code (Screenshot 1)
- [ ] Modified table code (Screenshot 2 if needed)

### Step 5

- [ ] Updated table displayed

---

## Custom Table Entries

The original Bootstrap table was modified to reflect key concepts learned in Module 11.

| Name | Type | Description |
|--------|--------|--------|
| Flask | Web Framework | Creates web applications |
| Cookies | Session Management | Maintains user state |
| Bootstrap | UI Framework | Enhances website appearance |

---

# Deliverables

Create:

```text
Activity11_3_Clifford_J_Ferraren.docx
```

Include all required screenshots.

---

# Key Takeaways

- Bootstrap simplifies table creation.
- Flask can dynamically render Bootstrap tables.
- Bootstrap improves readability and presentation.
- Data displayed on a webpage can be modified by changing Python data structures.
- Bootstrap is commonly used in dashboards, reports, and internal business applications.