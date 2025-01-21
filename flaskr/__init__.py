import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, static_folder='static')
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .app import app_routes
    app.register_blueprint(app_routes)

    return app