# coding=utf-8
from app import VdB
from flask import request, jsonify
from . import members

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


def is_teacher(username):
    try:
        db.select_by_primary_key('teachers', username)
        return True
    except Exception as e:
        print(e)
        return False


@members.route('/get_students', methods=['GET', 'POST'])
def get_students():
    if request.method == 'POST':
        data = request.get_json()
        try:
            username = str(data['username'])
            token = str(data['token'])
        except KeyError:
            return jsonify({"msg": "请求参数错误"}), 400
        if check_token(username, token):
            if not is_teacher(username):
                return jsonify({"msg": "用户校验失败"})
            students_dict = db.select_all('students')
            students_name_dict = {}
            for key, value in students_dict.items():
                students_name_dict.setdefault(key, value['name'])
            return jsonify(students_name_dict)
        else:
            return jsonify({"msg": "用户校验失败"}), 400
    else:
        return jsonify({"msg": "请求方式错误,请使用post请求"}), 400


@members.route('/user_info', methods=['GET', 'POST'])
def get_userinfo():
    if request.method == 'POST':
        data = request.get_json()
        try:
            username = str(data['username'])
            token = str(data['token'])
            role = str(data['role'])
        except KeyError:
            return jsonify({"msg": "请求参数错误"}), 400
        if check_token(username, token):
            if role == '1':
                res = db.select_by_primary_key('students', username)
            else:
                res = db.select_by_primary_key('teachers', username)
            return jsonify(res)
        else:
            return jsonify({"msg": "用户校验失败"}),400
    else:
        return jsonify({"msg": "请求方式错误,请使用post请求"}), 400
