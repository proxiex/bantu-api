from flask import Flask
from config import config
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    cors = CORS(app)
    db.init_app(app)
    
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # app.config.from_object('config.Config')

    with app.app_context():
        # Imports
        from . import routes

        # Create tables for our models
        db.create_all()

        return app
