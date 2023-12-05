from flask import jsonify, render_template
from app import app
from app import hw_views
import datetime

@app.route('/')
def home():
    return "Nan says 'Hello world!'"

@app.route('/phonebook')
def index():
    return app.send_static_file('phonebook.html')

# This route serves the dictionary d at the route /data
@app.route("/api/data")
def data():
    # define some data
    d = {
        "Alice": "(708) 727-2377",
        "Bob": "(305) 734-0429"
    }
    app.logger.debug(str(len(d)) + " entries in phonebook") #debug

    return jsonify(d)  # convert your data to JSON and return

@app.route('/crash')
def crash():
    return 1/0

@app.route('/lab02')
def resume():
    return app.send_static_file('lab02_resume.html')

@app.route('/lab03')
def lab03_home():
    return render_template('lab03/index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/lab03/about/')
def lab03_about():
    return render_template('lab03/about.html')

@app.route('/lab03/comments/')
def lab03_comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.']


    return render_template('lab03/comments.html', comments=comments)
