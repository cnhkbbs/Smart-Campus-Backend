# coding=utf-8

from flask import Blueprint

message = Blueprint('message', __name__, static_folder='static', template_folder='templates', url_prefix='/message')

from . import views