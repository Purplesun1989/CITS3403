from flask import Blueprint

# Import blueprints from individual modules
from BluePrint.auth import auth_bp
from BluePrint.datashare import datashare_bp
from BluePrint.home import home_bp
from BluePrint.specific import spe_bp as specific_bp
from BluePrint.awards import awards_bp
from BluePrint.awards import awards_grub, awards_study, top_reviews_data

# Create a function to register all blueprints
def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(datashare_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(specific_bp)
    app.register_blueprint(awards_bp)