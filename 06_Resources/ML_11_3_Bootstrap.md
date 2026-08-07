# Mini-Lesson 11.3: Bootstrap

## What Is Bootstrap?

Bootstrap is a front-end framework used to enhance web pages and web applications.

Bootstrap combines:

- HTML
- CSS
- JavaScript

to provide developers with a collection of reusable components and styles that improve the appearance, layout, and functionality of websites.

---

## Why Use Bootstrap?

Bootstrap helps developers quickly create:

- Responsive layouts
- Navigation bars
- Tables
- Forms
- Buttons
- Menus
- Cards
- Alerts

Benefits include:

- Consistent user interfaces
- Mobile-friendly design
- Faster development
- Professional appearance

---

## Common Bootstrap Components

### Navigation Bar

Bootstrap provides prebuilt navigation bars that help users move through an application.

Example uses:

- Home Pages
- Login Pages
- Book Listings
- Administrative Menus

Example:

```html
<nav class="navbar navbar-default">
    ...
</nav>
```

---

### Tables

Bootstrap tables provide enhanced formatting and improved readability.

Benefits:

- Better appearance
- Improved readability
- Responsive design
- Easier data presentation

---

## Bootstrap Table Example

Bootstrap provides many table styles.

One popular option is:

```text
.table-striped
```

This style displays alternating row colors.

Example:

```html
<table class="table table-striped">
```

Benefits:

- Easier data reading
- Better visual separation of rows
- Professional appearance

---

## Example Table

| First Name | Last Name | Student ID |
|------------|-----------|-------------|
| Mary | Smith | 100001 |
| John | Dan | 100002 |
| Jessica | Cooper | 100003 |

---

## Bootstrap Setup

To use Bootstrap, include the Bootstrap CSS file in the HTML page.

Example:

```html
<link rel="stylesheet"
href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
```

Additional JavaScript functionality can be enabled using:

```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
```

---

## Basic Bootstrap Page Structure

```html
<!DOCTYPE html>
<html>

<head>
    <title>Bootstrap Example</title>

    maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
</head>

<body>

<div class="container">

    Content Goes Here

</div>

</body>

</html>
```

---

## Bootstrap Containers

Containers help organize page content.

Example:

```html
<div class="container">
    Content
</div>
```

Benefits:

- Consistent spacing
- Better alignment
- Improved responsiveness

---

## Bootstrap Table Example Code

```html
<div class="container">

  <table class="table table-striped">

    <thead>
      <tr>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Student ID</th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>Mary</td>
        <td>Smith</td>
        <td>100001</td>
      </tr>

      <tr>
        <td>John</td>
        <td>Dan</td>
        <td>100002</td>
      </tr>

      <tr>
        <td>Jessica</td>
        <td>Cooper</td>
        <td>100003</td>
      </tr>
    </tbody>

  </table>

</div>
```

---

## Bootstrap in Flask Applications

Bootstrap can be integrated into Flask by including Bootstrap CSS and JavaScript references inside templates.

Example:

```html
<head>

bootstrap.min.css

</head>
```

Common Flask uses:

- Navigation bars
- Data tables
- Forms
- Dashboards
- Administrative pages

---

## Data Engineering Connections

Bootstrap is frequently used for:

### Data Dashboards

- KPI reporting
- Monitoring pages
- Analytics applications

### Administrative Applications

- User management
- Configuration pages
- Internal business tools

### Data Portals

- Data catalogs
- Data quality reports
- Data governance dashboards

---

## Key Terms

| Term | Definition |
|--------|------------|
| Bootstrap | Front-end framework for web development |
| Navigation Bar | Component used for site navigation |
| Table | Structured data display element |
| Container | Bootstrap layout component |
| Responsive Design | Layout adapts to different screen sizes |
| CSS | Cascading Style Sheets used for styling |
| JavaScript | Programming language used for page interactivity |

---

## Questions for Review

- What problem does Bootstrap solve?
- Why are Bootstrap tables useful?
- What is the purpose of a Bootstrap container?
- How can Bootstrap be integrated into Flask?
- What advantages do navigation bars provide?

---

## Key Takeaways

- Bootstrap is a front-end framework built using HTML, CSS, and JavaScript.
- Bootstrap helps developers quickly build professional web interfaces.
- Navigation bars simplify website navigation.
- Bootstrap tables improve readability and presentation.
- Containers help structure content on a page.
- Bootstrap integrates easily into Flask applications.
- Responsive design ensures applications work across different devices.

---

## Summary

Bootstrap is a powerful framework that enhances the appearance and usability of web applications. It provides prebuilt components such as navigation bars, tables, and responsive layouts that can be quickly integrated into Flask applications. Using Bootstrap allows developers to build cleaner, more professional, and more user-friendly web interfaces with minimal effort.