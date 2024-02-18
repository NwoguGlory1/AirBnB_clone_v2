#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask
from flask import render_template
from models.state import Storage

""" imports Flask webframe, render template """

app = Flask(__name__)
""" Creates an instance of class, Flask"""


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Function that executes if user accesses '/states_list'
    """
    my_model_instances = storage.all(FileStorage)
    return render_template('7-states_list.html', data=my_model_instances)


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
