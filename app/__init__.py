from flask import Flask

app = Flask(__name__, static_folder='static')

app.config['DEBUG'] = True

from app import views # noqa
