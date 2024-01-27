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


@app.route("cities_by_states", strict_slashes=False)
def cities_by_states():
    """displays list of all State objects
    present in DBStorage sorted by name
    """
    states = storage.all("State").sort("name")
    states_list = []
    for state in states:
        city_list = []
        if storage.engine.name == "db":
            cities = state.cities
        else:
            cities = state.cities()
        for city in cities.sort("name"):
            city_list.append({"id": city.id, "name": city.name})
        states_list.append({"id": state.id, "name": state.name, "cities": city_list})
    return render_template("8-cities_by_states.html", states=states_list)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
