# เมษนี ลายเฮือง - แนน
# 650510676
# Sec001 

from flask import jsonify, render_template
from app import app
import json
from urllib.request import urlopen
import datetime


@app.route('/weather')
def hw01_localweather():
    return app.send_static_file('hw01_localweather.html')


# This route serves the dictionary d at the route /data
@app.route("/api/weather")
def api_weather():
    # define some data
    url = "https://api.waqi.info/feed/Chiangmai/?token=830b47529331aafbd839b57c9415608551d1d4f8"
    d = urlopen(url)
    data = json.load(d)
    a = {
        "AQI" : data["data"]["aqi"],
        "PM10" : data["data"]["iaqi"]["pm10"]["v"],
        "PM2.5" : data["data"]["iaqi"]["pm25"]["v"],
        "Temperature" : data["data"]["iaqi"]["t"]["v"],
        "Time" : data["data"]["time"]["iso"]
        # "a" : 28
    }
    # app.logger.debug(a)
    return jsonify(a)  # convert your data to JSON and return

@app.route("/hw03/pm25/")
def hw03_pm25():
    url = "https://api.waqi.info/feed/Chiangmai/?token=830b47529331aafbd839b57c9415608551d1d4f8"
    d = urlopen(url)
    data = json.load(d)
    # pm25 = {
    #     "AQI" : data["data"]["forecast"]["daily"]["pm25"][0]
    # }
    list_pm25 = data["data"]["forecast"]["daily"]["pm25"]
    date_ls1 = (list_pm25[0]["day"]).split('-')
    date_ls2 = (list_pm25[-1]["day"]).split('-')
    d1 = datetime.date(int(date_ls1[0]), int(date_ls1[1]), int(date_ls1[2]))
    d2 = datetime.date(int(date_ls2[0]), int(date_ls2[1]), int(date_ls2[2]))
    # d1 = list_pm25[0]["day"]
    # d1 = datetime.date(2023, 12, 1)
    # d2 = datetime.date(2023, 12, 31)
    # d2 = list_pm25[-1]["day"]
    weeks = (d1-d2).days//7
    # app.logger.debug(type(list_pm25[0]["avg"]))
    
    return render_template('lab03/hw03_pm25.html', list_pm25=list_pm25, weeks=abs(weeks))

@app.route("/api/pm25")
def api_pm25():
    
    # define some data
    url = "https://api.waqi.info/feed/Chiangmai/?token=830b47529331aafbd839b57c9415608551d1d4f8"
    d = urlopen(url)
    data = json.load(d)
    # pm25 = {
    #     "AQI" : data["data"]["forecast"]["daily"]["pm25"][0]
    # }
    pm25 = data["data"]["forecast"]["daily"]["pm25"]
    # print(pm25)
    # app.logger.debug(pm25)
    return jsonify(pm25)  # convert your data to JSON and return