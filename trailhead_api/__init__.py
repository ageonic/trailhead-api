import os
from flask import Flask
from flask_cors import CORS

__version__ = "0.1.0"

# initialize global extensions
cors = CORS()


def create_app():
    # initialize the flask app
    app = Flask(__name__)

    # initialize flask extensions with app
    cors.init_app(app, resources=r"/api/*")

    # register flask blueprints
    from trailhead_api.api import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    return app
