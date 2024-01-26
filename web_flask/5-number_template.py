#!/usr/bin/python3
"""starts a Flask web application
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """display Hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ display “C ” followed by the value
    of the text variable
    """
    f_text = text.replace("_", " ")
    return f"C {f_text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """display “Python ”, followed by the value
    of the text variable
    """
    f_text = text.replace("_", " ")
    return f"Python {f_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n=None):
    """display n if its integer
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n=None):
    """displays html page
    if n is integer
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
