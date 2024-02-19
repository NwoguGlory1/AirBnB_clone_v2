#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

""" imports Flask webframe, render template """

app = Flask(__name__)
""" Creates an instance of class, Flask"""


@app.route('/states', strict_slashes=False)
def display_states():
    """
    Function that executes if user accesses '/cities_by_states'
    """
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def display_state_cities(id):
    """ Display a HTML page with cities of a specific State """
    state = storage.get(State, id)
    if state:
        return render_template('9-states_cities.html', state=state)
    else:
        return render_template('9-states_cities.html', state=state)

@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Function to handle the teardown, to close the SQLAchemy session
    after each request.
    """
    storage.close()


if __name__ == '__main__':
    """
    Ensures script runs only when excuted directly,
    not when imported as a module in another script.
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
