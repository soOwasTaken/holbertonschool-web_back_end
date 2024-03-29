#!/usr/bin/env python3
""" Basic Flask app """""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

app = Flask(__name__)
babel = Babel(app)


SUPPORTED_TIMEZONES = [
    "Europe/Paris",
    "US/Central",
    "Vulcan",
    "Europe/London",
]


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


def get_user():
    """ returns a user dictionary or None
    if the ID cannot be found or if login_as was not passed """
    try:
        userId = request.args.get('login_as')
        return users[int(userId)]
    except Exception:
        return None


@app.before_request
def before_request():
    """Before request"""
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    """ Get timezone from request"""
    url_timezone = request.args.get('timezone')

    if hasattr(g, 'user') and g.user and 'timezone' in g.user:
        user_timezone = g.user['timezone']
        if user_timezone in SUPPORTED_TIMEZONES:
            return user_timezone

    if url_timezone:
        try:
            if url_timezone in SUPPORTED_TIMEZONES:
                return url_timezone
            else:
                raise pytz.exceptions.UnknownTimeZoneError
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return 'UTC'


@babel.localeselector
def get_locale():
    """ to determine the best match with our supported languages """
    localLang = request.args.get('locale')
    supportLang = app.config['LANGUAGES']
    if localLang in supportLang:
        return localLang
    userId = request.args.get('login_as')
    if userId:
        localLang = users[int(userId)]['locale']
        if localLang in supportLang:
            return localLang
    localLang = request.headers.get('locale')
    if localLang in supportLang:
        return localLang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.config.from_object(Config)


@app.route('/')
def index():
    """ Basic Flask app"""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
