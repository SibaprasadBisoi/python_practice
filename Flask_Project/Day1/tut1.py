from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"

app.route("/Siba")
def siba():
    return "Hellow Siba"
app.run(debug=True)