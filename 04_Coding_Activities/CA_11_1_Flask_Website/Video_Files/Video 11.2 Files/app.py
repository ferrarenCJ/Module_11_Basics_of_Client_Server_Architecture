from flask import Flask, request, render_template

app = Flask(__name__)



@app.route("/", methods=["GET"])
def first_route():
    #return "You issued a GET request"
    # return ''' <HTML>
    # <h1> You issued a GET request </h1> 
    # '''
    return render_template("index.html", message = " hello Earthling")

    
 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
