# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 09:05:20 2021

@author: adple
"""

# https://www.youtube.com/watch?v=1lxrb_ezP-g&ab_channel=CoreySchafer

import pandas as pd
import requests
from requests.auth import HTTPBasicAuth

r = requests.get('url')
courses_json = r.json()
courses = pd.DataFrame(courses_json)
# course_users = json.dumps(course_json) - alternative using json library

print(courses.columns)

df_course = pd.DataFrame()

for i in courses['id']:
    course_id = i
    course_url = f'url/{course_id}/users'
    r = requests.get(course_url, auth=HTTPBasicAuth(
        'user', 'password'))
    course_json = r.json()
    course = pd.DataFrame(course_json)
    df_course = df_course.append(course)

df_user = pd.DataFrame()

for i in df_course['id']:
    user_id = i
    user_url = f'url/{user_id}/course-progress'
    r = requests.get(user_url, auth=HTTPBasicAuth(
        'user', 'password'))
    user_json = r.json()
    user = pd.DataFrame(user_json)
    df_user = df_user.append(user)

print(df_user.head())
