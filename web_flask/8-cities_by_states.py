#!/usr/bin/python3
"""initialize flask web app"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """diplay HTML page with state and cities sorted"""
    slist = sorted(storage.all(
        State).values(), key=lambda x: x.name)

    for s in slist:
        s.cities.sort(key=lambda x: x.name)
    return render_template("8-cities_by_states.html", sorted_states_list=slist)


@app.teardown_appcontext
def terminate(excep):
    """close the storage after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
