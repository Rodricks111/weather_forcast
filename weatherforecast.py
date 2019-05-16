#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 04:01:45 2019

@author: Fun_ix
"""

from datetime import datetime, timedelta
import time
from collections import namedtuple
import pandas as pd
import requests
import matplotlib.pyplot as plt

APPID="xxxxxxxxxxxxxxxxxxxxxxx"

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q=Las Vegas,US&APPID=5218dcef6cfcc05dc6dc462413a27430"+APPID
features = ["sys", "weather", "main", "cod"]
target_hour = timedelta(hours=1)
#datetime.timedelta(-1,68400)
print(_)
def extract_weather_data(url,target_hour,hour):
    records = []
    for _ in range(hour):
        #request = BASE_URL.format(target_hour.strftime(hour), json)
        #response = requests.get(request)
        response =requests.get("http://api.openweathermap.org/data/2.5/weather?q=New York,US&"+APPID)
        if response.status_code ==200:
            data = response.json()['history']['dailysummary'][0]
            records.append(DailuSummary(
                    hour=target_hour,
                    sys = data['sys'],
                    weather = data['weather']))
            time.sleep(6)
            target_hour += timedelta(hour=5)
        return records
    records = extract_weather_data(BASE_URL,target_hour,5)
    records += extract_weather_data(BASE_URL,  target_hour, 5)
    df = pd.DataFrame(records, columns = features).set_index('hour')
    tmp = df[['sys', 'weather']].head(10)
    tmp

response.content.decode("utf-8")

response =requests.get("http://api.openweathermap.org/data/2.5/weather?q=Ahmedabad, India&APPID"+APPID)
print(response.status_code)
data = response.json()
print(data)
