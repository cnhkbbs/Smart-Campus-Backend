# coding=utf-8
from app import VdB
from flask import request, jsonify
from . import grades

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


def is_teacher(username):
    try:
        db.select_by_primary_key('teachers', username)
        return True
    except Exception as e:
        print(e)
        return False


@grades.route('/get_grades', methods=['GET', 'POST'])
def get_grades():
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
                try:
                    grade = db.select_grades(username)
                    return jsonify({"grades": grade}), 200
                except Exception as e:
                    print(e)
                    return jsonify({'msg': 'error'}), 400
            else:
                try:
                    if is_teacher(username):
                        try:
                            student_id = data['student_id']
                        except KeyError:
                            return jsonify({"msg": "请求参数错误"}), 400
                        grade = db.select_grades(student_id)
                        return jsonify({"grades": grade}), 200
                    else:
                        return jsonify({'msg': '用户校验失败'}), 400
                except Exception as e:
                    print(e)
                    return jsonify({'msg': 'error'}), 400
        else:
            return jsonify({'msg': '用户校验失败'}), 400
    else:
        return jsonify({"msg": "请求方式错误,请使用post请求"}), 400
