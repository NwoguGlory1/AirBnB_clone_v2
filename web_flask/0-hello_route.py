#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask
""" imports Flask webframe """

app = Flask(__name__)
""" Creates an instance of class, Flask"""


@app.route('/', strict_slashes=False)
def hello():
    """ Function that executes if user accesses '/' URL"""
    return f'Hello HBNB!'


if __name__ == '__main__':
    """
    Ensures script runs only when excuted directly,
    not when imported as a module in another script.
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
