from flask import Blueprint, render_template

app = Blueprint("admin", __name__)

@app.route("/admin/login")
def login():
    return render_template('admin/login.html')
