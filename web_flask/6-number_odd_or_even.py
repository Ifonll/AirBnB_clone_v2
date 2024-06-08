#!/usr/bin/python3
""""flask starts a web application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def saying_hello():
    """"dispplays hello"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """"displays hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def aboutC(text):
    """c is so good"""
    modified_text = text.replace('_', ' ')
    return f"C {modified_text}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def aboutPython(text):
    """"python is amazing"""
    modified_text = text.replace('_', ' ')
    return f"Python {modified_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def aboutnumbers(n):
    """display number"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def aboutHTML(n):
    """"display html content"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """display number is odd or even"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
