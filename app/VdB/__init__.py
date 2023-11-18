# coding = utf-8
import flask

from . import virtual_database


class VdB:
    def __init__(self):
        pass

    def select_by_primary_key(self, table, primary_key):
        if table == "students":
            return virtual_database.Students[primary_key]
        elif table == "teachers":
            return virtual_database.Teachers[primary_key]
        elif table == "grades":
            return virtual_database.Grades[primary_key]
        else:
            return None

    def select_all(self, table):
        if table == "students":
            return virtual_database.Students
        elif table == "teachers":
            return virtual_database.Teachers
        elif table == "grades":
            return virtual_database.Grades
        else:
            return None

    def delete_by_primary_key(self, table, primary_key):
        if table == "students":
            del virtual_database.Students[primary_key]
        elif table == "teachers":
            del virtual_database.Teachers[primary_key]
        elif table == "grades":
            del virtual_database.Grades[primary_key]
        else:
            return None
        return True

    def update_by_primary_key(self, table, primary_key, data):
        if table == "students":
            virtual_database.Students[primary_key] = data
        elif table == "teachers":
            virtual_database.Teachers[primary_key] = data
        elif table == "grades":
            virtual_database.Grades[primary_key] = data
        else:
            return None
        return True

    # 在线用户记录操作
    def add_online_user(self, username, token):
        virtual_database.Online_Users.setdefault(username, token)
        print(f'online users: {virtual_database.Online_Users}')

    def delete_online_user(self, username):
        del virtual_database.Online_Users[username]
        print(f'online users: {virtual_database.Online_Users}')

    def select_online_user_by_username(self, username):
        try:
            return virtual_database.Online_Users[username]
        except Exception:
            return None

    # 推文查询
    def select_posts(self):
        return virtual_database.Posts

    # 成绩获取
    def select_grades(self, student_id):
        return virtual_database.Grades[student_id]

    # 课程表查询
    def select_courses(self, username):
        return virtual_database.Courses[username]


