# usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<span style='color:red'>I am app 1. Hello!</span>"

app.run(debug=False, threaded=True, host="0.0.0.0", port=2046)