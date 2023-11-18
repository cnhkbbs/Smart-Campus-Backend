# coding=utf-8

from flask import Blueprint

members = Blueprint('members', __name__, static_folder='static', template_folder='templates', url_prefix='/members')

from . import views