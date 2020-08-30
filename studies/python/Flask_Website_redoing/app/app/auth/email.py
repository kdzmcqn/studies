from flask import render_template, current_app
from flask_babel import _
from app.email import send_email


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(
        _('[Asklypso] Reset your password'),
        sender=current_app.config['ADMINS'][0],
        text_body=render_template('reset_password.txt',
                                  user=user, token=token),
        html_body=render_template('reset_password.html',
                                  user=user, token=token)
    )
