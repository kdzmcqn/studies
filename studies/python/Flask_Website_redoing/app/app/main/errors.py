from flask import render_template
from . import main

"""
from app.errorhandler --> app_errorhandler

the app_errorhandler is for blueprint

if errorhanlder decorator is used, the handler will be
only invoked only for errors that originate in routes
defined by the blueprint

for application-wide error handlers,

app_errorhandler decorator must be used instead.

"""
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500