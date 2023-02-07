#!/usr/bin/python3
"""A Script that Starts a Flask Web Application dubbed `app` with 3 Views:
        the Index View <static><text>
        the /hbnb View <static><text>
        the /c/<text> View <dynamic><text>

   The `app` listens on; 0.0.0.0:, port 5000.
"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def homepage():
    """A Function that Displays `app`'s Index View
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """A Function that Returns the word 'HBNB' when Executed"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cplus(text):
    """Function that returns a string 'C' followed by contents of `text`
    All Underscores on the variable `text` are replaced by space symbol.
    """
    text = text.replace('_', ' ')
    return "C " + text


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
