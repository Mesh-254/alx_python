#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """function that return home route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def show_hbnb():
    """function that return home route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    """function that return home route"""
    return f'C {text}'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
