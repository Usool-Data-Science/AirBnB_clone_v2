#!/usr/bin/python3
"""A script that starts flask web application"""
from flask import Flask, render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python_(text="is cool"):
    """Displays python followed by the text argument"""
    arg = text.replace("_", " ")
    return f"Python {arg}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display the number n if only it is an integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays a HTML page only if n is an integer"""
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_even_or_odd(n):
    """Displays whether a number is even or odd"""
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
