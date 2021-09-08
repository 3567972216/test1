import json
import sys

import requests
from flask import Flask, request

x = "bazinga"

app = Flask(__name__)


@app.route('/')
def hello():
    global x
    return x


@app.route('/', methods=['POST'])
def example():
    if request.json == "exit":
        sys.exit()
    global x
    data = request.json
    x = "HIHIIHIH" + json.dumps(data)
    return x


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=9002)
