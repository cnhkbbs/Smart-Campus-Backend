# coding=utf-8

from flask import Blueprint

feedback = Blueprint('feedback', __name__, static_folder='static', template_folder='templates', url_prefix='/feedback')

from . import views