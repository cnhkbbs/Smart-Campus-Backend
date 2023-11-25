# coding=utf-8
from app import VdB
from flask import request, jsonify
from . import message

db = VdB.VdB()


def check_token(username, token):
    try:
        tk = db.select_online_user_by_username(username)
        if tk is None:
            return False
        elif tk == token:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


@message.route('/', methods=['GET', 'POST'])
def get_message():
    if request.method == 'POST':
        data = request.get_json()
        try:
            username = str(data['username'])
            token = str(data['token'])
        except KeyError:
            return jsonify({"msg": "请求参数错误"}), 400
        if check_token(username, token):
            return jsonify({'msg': '暂无消息', 'count': 0})
        else:
            return jsonify({"msg": "用户校验失败"}), 400
    else:
        return jsonify({"msg": "请求方式错误,请使用post请求"}), 400
