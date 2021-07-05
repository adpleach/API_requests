# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 09:05:20 2021

@author: adple
"""

# https://www.youtube.com/watch?v=1lxrb_ezP-g&ab_channel=CoreySchafer

import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
import time


def get_columnheaders(url):
    r = requests.get(url)
    data_json = r.json()
    data = pd.DataFrame(data_json)
    # course_users = json.dumps(course_json) - alternative using json library
    return data.columns


def get_nextAPIs(url_1, url_2, column_name, username, password, url_2b=None):
    r = requests.get(url_1)
    data_json = r.json()
    data = pd.DataFrame(data_json)

    df_nextAPI = pd.DataFrame()

    for i in data[column_name]:
        data_id = i
        data_url = f'{url_2}/{data_id}/{url_2b}'
        r = requests.get(data_url, auth=HTTPBasicAuth(username, password))
        data2_json = r.json()
        data2 = pd.DataFrame(data2_json)
        df_nextAPI = df_nextAPI.append(data2)

        time.sleep(r.elapsed.total_seconds())

    return df_nextAPI
