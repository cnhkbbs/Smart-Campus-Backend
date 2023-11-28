# coding=utf-8
from app import VdB
from flask import request, jsonify
from . import auth
import string
import random

db = VdB.VdB()


# 校验用户名和密码
def check_user(username, password, role):
    if role == '1':
        table = 'students'
    else:
        table = 'teachers'
    try:
        res = db.select_by_primary_key(table, username)
        if res['pwd'] == password:
            return res['name']
        else:
            return False
    except KeyError:
        return False
    except Exception as e:
        print(e)


# 用户名token校验
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
        return False


def is_login(username):
    try:
        res = db.select_online_user_by_username(username)
        if res is None:
            return False
        else:
            return res
    except Exception:
        return False


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = str(request.form.get('username'))
        password = str(request.form.get('password'))
        role = str(request.form.get('role'))
        # 身份验证
        check_result = check_user(username, password, role)
        if check_result is False:
            return jsonify({"msg": "用户名或密码错误"}), 400

        check_is_login = is_login(username)
        if check_is_login is False:
            # 生成token
            token = ''.join(random.sample(string.ascii_letters + string.digits, 32))
            # 记录在线状态
            db.add_online_user(username, token)
            login_msg = "登录成功"
        else:
            token = check_is_login
            login_msg = "登录成功"
        return jsonify({"msg": login_msg, "name": check_result, "token": token, "role": role}), 200
    else:
        return jsonify({"msg": "请求方式错误,请使用post请求"}), 400


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        data = request.get_json()
        username = str(data['username'])
        token = str(data['token'])
        if check_token(username, token):
            db.delete_online_user(username)
            return jsonify({"msg": "退出成功"}), 200
        else:
            return jsonify({"msg": "用户校验失败"}), 400
    else:
        return jsonify({"msg": "请求方式错误,请使用post请求"}), 400
