from flask import Blueprint
bp = Blueprint('main', __name__)
from app.main import routes

"""
It is important to note that the modules are imported
at the bottom of the app/main/__init__.py script to 
avoid errors due to circular dependencies.

The problem is that app/main/views.py and app/main/errors.py
in turn are going to import the main blueprint object,
so the imports are going to fail unless circular reference
occurs after the main is defined.
"""
