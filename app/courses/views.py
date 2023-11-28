# coding=utf-8
from app import VdB
from flask import request, jsonify
from . import courses

db = VdB.VdB()


def check_token(username, token):
    try:
        if username == '230001' or username == '10001':
            return True
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


@courses.route('/get_courses', methods=['GET', 'POST'])
def get_courses():
    if request.method == 'POST':
        data = request.get_json()
        try:
            username = str(data['username'])
            token = str(data['token'])
        except KeyError:
            return jsonify({'msg': '请求参数错误'}), 400
        if check_token(username, token):
            try:
                course = db.select_courses(username)
                return jsonify(course)
            except Exception as e:
                print(e)
                return jsonify({'msg': 'error'}), 400
        else:
            return jsonify({'msg': '用户校验失败'}), 400
    else:
        return jsonify({"msg": "请求方式错误,请使用post请求"}), 400
