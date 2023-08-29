#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """function that return home route"""
    return 'Hello HBNB!'


@app.route('/HBNB', strict_slashes=False)
def hello():
    """function that return home route"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
