from cfenv import AppEnv
from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)
    app_env = AppEnv()

    @app.route("/")
    def index():
        return jsonify(app_env.app)

    @app.route("/services")
    def services():
        return jsonify([s.__dict__ for s in app_env.services])

    return app
