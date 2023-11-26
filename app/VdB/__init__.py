# coding = utf-8
from . import virtual_database
import os
import json
from datetime import datetime, timedelta


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
        self.update_cache(virtual_database.Online_Users)
        print(f'online users: {virtual_database.Online_Users}')

    def delete_online_user(self, username):
        del virtual_database.Online_Users[username]
        self.update_cache(virtual_database.Online_Users)
        print(f'online users: {virtual_database.Online_Users}')

    def select_online_user_by_username(self, username):
        try:
            if self.get_cache() is None:
                pass
            else:
                virtual_database.Online_Users = self.get_cache()
                print(f'online users: {virtual_database.Online_Users}')
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

    # 系统缓存操作
    def update_cache(self, users_dict, cache_key='online_users', cache_duration_hours=24):
        users_json = json.dumps(users_dict)
        os.environ[cache_key] = users_json
        cache_expiry_time = datetime.now() + timedelta(hours=cache_duration_hours)
        os.environ[cache_key + "_ttl"] = cache_expiry_time.isoformat()

    def get_cache(self, cache_key='online_users'):
        if cache_key not in os.environ:
            return None
        ttl_key = cache_key + "_ttl"
        if ttl_key not in os.environ:
            return None
        cache_expiry_time_str = os.environ[ttl_key]
        cache_expiry_time = datetime.fromisoformat(cache_expiry_time_str)
        current_time = datetime.now()
        if current_time > cache_expiry_time:
            return None
        users_json = os.environ[cache_key]
        users_dict = json.loads(users_json)
        return users_dict
