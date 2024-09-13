#!/usr/bin/env python3
"""Setting up a basic flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """A index.html that outputs Welcome to Holberton as page title
    and Hello world as a header."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
