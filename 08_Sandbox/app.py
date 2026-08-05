from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Module 11 Flask Sandbox</h1>
    <p>Testing Client-Server Architecture using Flask.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)