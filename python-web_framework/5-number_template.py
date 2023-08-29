#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """function that return home route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def show_hbnb():
    """function that return hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """function that return c text route"""
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """function that return python text route"""
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def display_integer(n):
    """function that return display integer route"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_page(n):
    """function that return display page"""

    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
