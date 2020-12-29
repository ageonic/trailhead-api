import os
from flask import Flask

__version__ = "0.1.0"


def create_app():
    # initialize the flask app
    app = Flask(__name__)

    # register flask blueprints
    from trailhead_api.api import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    return app
