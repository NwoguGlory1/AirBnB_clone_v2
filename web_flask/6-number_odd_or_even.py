#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask
from flask import render_template
""" imports Flask webframe, render template """

app = Flask(__name__)
""" Creates an instance of class, Flask"""


@app.route('/', strict_slashes=False)
def hello():
    """ Function that executes if user accesses '/' URL"""
    return f'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Function that exceutes if user accesses '/hbnb' """
    return f'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """ Function that exceutes if user accesses '/c/<text> """
    new_text = text.replace('_', ' ')
    return f'C {new_text}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_Python(text='is cool'):
    """ Function that executes if user accesses '/python/<text>' """
    new_text = text.replace('_', ' ')
    return f'Python {new_text}'


@app.route('/number/<int:n>', strict_slashes=False)
def display_n(n):
    """ Function that executes if user accesses '/number/<n>' """
    return f'{n} is a number'


@app.route('/number_template/', strict_slashes=False)
@app.route('/number_template/<int:n>', strict_slashes=False)
def template_n(n):
    """
    Function that executes if user accesses '/number_template/
    or /number_template/<int:n>
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def template_odd_even():
    """
    Function that executes if user accesses '/number_odd_or_even/<int:n>'
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    """
    Ensures script runs only when excuted directly,
    not when imported as a module in another script.
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
