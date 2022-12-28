from flask import Flask


def create_app():
    app = Flask(__name__)

    from .resources.helloworld import app as helloworld

    app.register_blueprint(helloworld, url_prefix="/helloworld")
    return app
