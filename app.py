from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Pi Programmers"

@app.route('/pi')
def pi():
    return "PI device"

@app.route("/db")
def db():
    return "DB DATA"

