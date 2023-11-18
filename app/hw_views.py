from flask import jsonify
from app import app


@app.route('/weather')
def hw01_localweather():
    return app.send_static_file('hw01_localweather.html')


# This route serves the dictionary d at the route /data
@app.route("/api/weather")
def api_weather():
    # define some data
    d = {
        "AQI": 80,
        "PM10": 82,
        "PM2.5": 80,
        "Temperature": 22,
        "Time" : "2023-11-18T22:00:00+07:00"
    }
    return jsonify(d)  # convert your data to JSON and return