#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Returns some text."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """Return other text."""
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """replace with text."""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """replace symbols"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
