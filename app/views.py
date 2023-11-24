# from flask import jsonify
from app import app
# from app import hw_views



@app.route('/lab02')
def resume():
    return app.send_static_file('lab02_resume.html')