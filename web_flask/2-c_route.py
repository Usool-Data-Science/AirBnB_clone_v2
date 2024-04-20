#!/usr/bin/python3
"""First route that prints HBNB when visiting /hbnb"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Prints a greeting message"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Prints HBNB when visiting the corresponding route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_(text):
    """Prints display C followed by the text argumente"""
    arg = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
