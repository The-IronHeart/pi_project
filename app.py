from flask import Flask

app = Flask(__name__)

@app.@app.route('/')
def home():
    return "Hello Pi Programmers"