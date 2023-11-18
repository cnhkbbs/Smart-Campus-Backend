# coding=utf-8

from flask import Blueprint

grades = Blueprint('grades', __name__, static_folder='static', template_folder='templates', url_prefix='/grades')

from . import views