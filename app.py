from flask import Flask
from exts import db, csrf
from flask_migrate import Migrate
from flask_login import LoginManager
from models import UserModel
from config import DevelopmentConfig
from BluePrint import register_blueprints  # Or import each bp directly

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Init extensions
    db.init_app(app)
    csrf.init_app(app)
    Migrate(app, db)

    # Setup login manager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return UserModel.query.get(int(user_id))

    # Register Blueprints
    register_blueprints(app)

    # Optional root route
    @app.route("/", methods=["GET", "POST"])
    def hello_world():
        return "this is a test"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)