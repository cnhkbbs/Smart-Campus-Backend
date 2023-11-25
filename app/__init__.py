from flask import Flask, jsonify

app = Flask(__name__)

# 注册蓝图
from .auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)

from .posts import posts as posts_blueprint

app.register_blueprint(posts_blueprint)

from .grades import grades as grades_blueprint

app.register_blueprint(grades_blueprint)

from .courses import courses as courses_blueprint

app.register_blueprint(courses_blueprint)

from .members import members as members_blueprint

app.register_blueprint(members_blueprint)

from .feedback import feedback as feedback_blueprint

app.register_blueprint(feedback_blueprint)

from .message import message as message_blueprint

app.register_blueprint(message_blueprint)


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hi'


@app.route('/notice', methods=['GET', 'POST'])
def notice():
    return '当前服务器为演示模式，所有内容会定期重置。'


@app.route('/visitor_registration', methods=['GET', 'POST'])
def visitor_registration():
    return jsonify({"msg": "登记成功"})
