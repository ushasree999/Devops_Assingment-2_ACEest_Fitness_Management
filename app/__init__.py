from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Register Blueprints or routes
    from . import routes
    return app

# Import workouts from routes and expose it
from .routes import workouts