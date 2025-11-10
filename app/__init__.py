from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Register Blueprints or routes
    with app.app_context():
        from . import routes
        return app

# Import workouts from routes and expose it
from .routes import workouts