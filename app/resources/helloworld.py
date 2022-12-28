from flask import Blueprint, jsonify

app = Blueprint("helloworld", __name__)


@app.route("")
def helloworld():
    return jsonify({"message": "hello world"})
