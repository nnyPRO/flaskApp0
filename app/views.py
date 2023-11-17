from app import app


@app.route('/')
def home():
    return "Nan says 'Hello world!'"
