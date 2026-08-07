# Mini-Lesson 11.2: Cookies

## What Are Cookies?

Cookies, formally known as HTTP cookies, are small text files stored by a web browser. Cookies contain small amounts of information, typically in the form of name-value pairs.

A server sends cookie information to a browser as part of an HTTP response. The browser stores the cookie and automatically sends it back to the same server during future requests.

This allows the server to recognize whether multiple requests originate from the same browser.

---

## What Are Cookies Used For?

Cookies are primarily used to maintain state within the stateless HTTP protocol.

### Session Management

Cookies allow websites to manage user sessions and maintain login status.

Examples:

- User authentication
- Shopping carts
- Game scores
- User session tracking

Web applications commonly generate a unique identifier and store it within a cookie to associate future requests with the correct user.

---

### Personalization

Cookies allow websites to remember user preferences and settings.

Examples:

- Language preferences
- Theme settings
- Display options
- User customization settings

This helps provide a more consistent user experience.

---

### Activity Tracking

Cookies are frequently used to track user activity.

Examples:

- Browsing history
- Page visits
- Product recommendations
- Targeted advertising

Websites use this information to better understand user behavior and deliver personalized content.

---

## Cookie Lifespan

### Session Cookies

Session cookies are temporary.

Characteristics:

- Exist only during an active browsing session
- Deleted when the browser session ends
- Commonly used for authentication

Examples:

- Logged-in users
- Shopping carts
- Temporary selections

---

### Persistent Cookies

Persistent cookies remain available until a predetermined expiration date and time.

Characteristics:

- Survive browser restarts
- Persist until expiration
- Used for long-term preferences

Examples:

- Remember Me functionality
- Language selections
- Saved settings

---

## Deleting Cookies

Cookies can be removed programmatically by setting the cookie expiration time to zero.

Example:

```python
@app.route('/delete-cookie/')
def delete_cookie():
    res = make_response("Your_desired_message")
    res.set_cookie('foo', 'bar', max_age=0)
    return res