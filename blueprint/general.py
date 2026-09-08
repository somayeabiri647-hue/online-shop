from flask import Blueprint

app = Blueprint("general", __name__)


@app.route("/")
def hello_word():
    return "this is main page"
