# my_project/__init__.py
from flask import Flask
from flask_migrate import Migrate
from flasgger import Swagger
import yaml
import os
from my_project.database import db
from my_project.terminals.routes.__init__ import register_routes

def create_app():
    app = Flask(__name__)

    # Load configurations from YAML
    config_path = os.path.join(os.path.dirname(__file__), '../config/my_app.yml')
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    # Configure the database URI and disable track modifications warnings
    app.config['SQLALCHEMY_DATABASE_URI'] = config['database']['uri']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # Initialize Flask extensions
    db.init_app(app)  # Initialize the database
    Migrate(app, db)  # Initialize Flask-Migrate

    # Register blueprints
    register_routes(app)

    swagger_config = {
        "swagger": "2.0",  # or "openapi": "3.0.0"
        "info": {
            "title": "My Project API",
            "version": "1.0",
            "description": "REST API for Terminals and Customer Companies"
        },
        "host": "13.61.4.78:5000",  # optional, can leave blank for auto
        "basePath": "/",          # base path for your endpoints
        "schemes": ["http"],      # or ["http", "https"]
    }

    Swagger(app, template=swagger_config)
    

    return app
