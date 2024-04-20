#!/usr/bin/python3
"""A script that starts flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """A view that prints Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Prints HBNB when visiting the corresponding route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_(text):
    """Prints display C followed by the text argument"""
    arg = text.replace('_', ' ')
    return f"C {arg}"


@app.route('/python/<text>', strict_slashes=False)
def Python_(text="is cool"):
    """Displays python followed by the text argument"""
    arg = text.replace("_", " ")
    return f"Python {arg}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
