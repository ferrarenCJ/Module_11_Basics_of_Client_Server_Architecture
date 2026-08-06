from flask import Flask, request

app = Flask(__name__)



@app.route("/", methods=["GET"])
def first_route():
    #return "You issued a GET request"
    return ''' <HTML>
    <h1> You issued a GET request </h1>
    '''
 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
