#!/usr/bin/env python3
"""
Basic flask config
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """class definition"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    return configured language baed on decorator
    """
    return request.accept_languages.best_match(Config['LANGUAGES'])


@app.route('/')
def index():
    """
    A function for a basic route
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
