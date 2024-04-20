#!/usr/bin/python3
"""First route that prints HBNB when visiting /hbnb"""
from flask import Flask


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Prints HBNB when visiting the corresponding route"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
