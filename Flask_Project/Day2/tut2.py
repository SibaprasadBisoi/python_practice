from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('index.html')
@app.route("/Siba")
def siba():
    name = "Siba"
    return render_template('about.html', name= Siba)
app.run(debug=True)