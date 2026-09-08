from flask import Blueprint

app = Blueprint("admin", __name__)

@app.route("/admin")
def main():
    return "this is admin page"
