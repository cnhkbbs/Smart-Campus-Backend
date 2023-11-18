# coding=utf-8

from flask import Blueprint

posts = Blueprint('posts', __name__, static_folder='static', template_folder='templates', url_prefix='/posts')

from . import views
