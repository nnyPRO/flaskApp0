from flask import Flask

app = Flask(__name__, static_folder='static')

app.jinja_options = app.jinja_options.copy()
app.jinja_options.update({
    'trim_blocks': True,
    'lstrip_blocks': True
})

app.config['DEBUG'] = True

from app import views # noqa

