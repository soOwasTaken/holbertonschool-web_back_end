#!/usr/bin/env python3
""" Basic Flask app """""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Babel configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """get user"""
    return users.get(user_id)


@app.before_request
def before_request():
    """Before request"""
    user_id = request.args.get('login_as')
    if user_id:
        g.user = get_user(int(user_id))
    else:
        g.user = None


@babel.localeselector
def get_locale():
    """ Get locale from request """

    requested_locale = request.args.get('locale')

    if requested_locale in app.config['LANGUAGES']:
        return requested_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.config.from_object(Config)


@app.route('/')
def index():
    """ Basic Flask app"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
