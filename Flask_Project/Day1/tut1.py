from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/siba")
def siba():
    return "Hello Siba"
app.run(debug=True)