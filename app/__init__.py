from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="../templates")
    app.config.from_object("config.Config")

    # Register Blueprints or routes
    from .routes import routes
    app.register_blueprint(routes)

    return app

# Import workouts from routes and expose it
from .routes import workouts