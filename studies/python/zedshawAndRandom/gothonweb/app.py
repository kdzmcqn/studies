from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/trials")
def trials():
    return render_template("trials.html")

@app.route("/hello", methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        greet = request.form['greet'] # dapat match
        name = request.form['name'] # ang pagkakasunod sa form
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")


if __name__ == "__main__":
    app.run()