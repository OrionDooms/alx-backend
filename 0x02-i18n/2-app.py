#!/usr/bin/env python3
"""Setting up a basic flask app"""
from flask import request, Flask, render_template
from flask_babel import Babel


class Config:
    """Config class defines LANGUAGES attribute with 'en' and 'fr'.
    The default locale languages is 'en' and the default
    timezone is set to 'UTC'."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


"""Initialize the app and Babel object, Apply the Config
Class to Flask, and Babel pass the Flask app"""
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def Index():
    """A index.html that outputs Welcome to Holberton as page title
    and Hello world as a header."""
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """request.accept_languages.best_match() checks the
    Accept-language header from request and matches
    config.LANGUAGES"""
    return request.accept_languages.best_match([Config.LANGUAGES])


if __name__ == '__main__':
    app.run(debug=True, port=5000)
