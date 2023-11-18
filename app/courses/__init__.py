# coding=utf-8

from flask import Blueprint

courses = Blueprint('courses', __name__, static_folder='static', template_folder='templates', url_prefix='/courses')

from . import views