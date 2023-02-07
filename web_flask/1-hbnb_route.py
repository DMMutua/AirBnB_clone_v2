#!/usr/bin/python3
"""A Script that Starts a Flask Web Application with 2 Views:
        the Index View
        the /hbnb View
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


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
