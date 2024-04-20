#!/usr/bin/python3
"""Takes and return url arguments when visiting the route"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Prints a greeting message"""
    return "Hello HBNB!"

@app.route('/c/<text>', strict_slashes=False)
def hbnb(text):
    """Prints display C followed by the text argumente"""
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
