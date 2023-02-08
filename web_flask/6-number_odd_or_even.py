#!/usr/bin/python3
"""A Script that Starts a Flask Web Application dubbed `app` with 7 Views:
        the Index View <static><text>
        the /hbnb View <static><text>
        the /c/<text> View <dynamic><text>
        the /python/<text> View <dynamic><text>
        the /number/<n> View <dynamic><number>
        the /number_template/<n> <dynamic><number><template>
        the /number_odd_or_even/<n> <dynamic><number><template>

   The `app` listens on; 0.0.0.0:, port 5000.
"""


from flask import Flask
from flask import render_template


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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonplus(text='is cool'):
    """Function that returns a string: 'Python ' followed by contents of `text`
    All Underscores in `text` are replaced by space symbol.
    The default value for text is "is cool".
    """
    text = text.replace('_', ' ')
    return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def isitnum(n):
    """Displays the text; `<n> is a number` only if <n> is a number
    Otherwise returns nothing; which evaluates a 404 error on browser"""
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_if_number(n):
    """Function that Displays an HTML template if contents of <n>
    passed to URL are of type `int`"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def html_if_even(n):
    """Function that Displays an HTML template that
    displays if contents of <n> are even or not. <n> is type `int`,
    otherwise error 404 if URL is accessed
    """
    n_state = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, n_state=n_state)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
