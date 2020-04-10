from flask import Flask, g

from .middleware import init_db


def register_blueprints(app):
    from app.home.views import home
    app.register_blueprint(home)


def create_app(config):
    app = Flask(__name__)

    # Configurations
    app.config.from_object(config)
    # redis
    app.before_request(init_db)
    # Blueprints
    register_blueprints(app)
    return app
