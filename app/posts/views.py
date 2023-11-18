# coding=utf-8
from app import VdB
from flask import request, jsonify
from . import posts

db = VdB.VdB()


@posts.route('/list', methods=['GET', 'POST'])
def get_posts_list():
    if request.method == 'POST':
        try:
            posts_dict = db.select_posts()
            posts_list = []
            for post_id in range(len(posts_dict)):
                post_title = posts_dict[str(post_id + 1)]['title']
                post_cover = posts_dict[str(post_id + 1)]['cover']
                posts_list.append({'title': post_title, 'cover': post_cover})
        except Exception as e:
            print(e)
            return jsonify({'msg': 'error'}), 400
        return jsonify(posts_list)
    else:
        return jsonify({"msg": "请求方式错误,请使用post请求"}), 400


@posts.route('/content', methods=['GET', 'POST'])
def get_posts():
    if request.method == 'POST':
        try:
            data = request.get_json()
            post_title = data['post_title']
            post_dict = db.select_posts()
            for post_id in range(len(post_dict)):
                if post_dict[str(post_id + 1)]['title'] == post_title:
                    return jsonify({"content": post_dict[str(post_id + 1)]['content']})
        except Exception as e:
            print(e)
            return jsonify({'msg': 'error'}), 400
    else:
        return jsonify({"msg": "请求方式错误,请使用post请求"}), 400
