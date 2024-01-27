#!/usr/bin/python3
"""starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_appcontext(exception):
    """ remove the current SQLAlchemy Session
    After each request
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """displays the list of all State objects
    present in DBStorage sorted by name
    """
    return render_template("7-states_list.html", states=storage.all(State))


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
