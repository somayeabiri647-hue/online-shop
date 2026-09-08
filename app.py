from flask import Flask
from blueprint.general import general

app = Flask(__name__)

app.register_blueprint(general)

@app.route("/")
def home():
    return "hello world"

app.run(host="0.0.0.0", port=5000, debug=True)