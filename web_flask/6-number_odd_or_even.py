#!/usr/bin/python3
"""script to display HBNB"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """function to return hello HBNB"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def index_hbnb():
    """ function to return HBNB"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def index_c(text):
    """function to return C is fun"""
    return 'C ' + text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pytfon_is_cool(text='is cool'):
    """return 'python' followed by the text variable value set to it"""
    return 'Python ' + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def a_number(n):
    """display only a number passed on url"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_html(n):
    return render_template("5-number.html", p=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def render_html_variables(n):
    """html page is rendered with variabes"""
    if n % 2 == 0:
        is_odd_or_is_even = "even"
    else:
        is_odd_or_even = "odd"
    return render_template("6-number_odd_or_even.html", p=n, m=is_odd_or_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
