# config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "this_should_never_be_a_personal_project"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DB_FILENAME = 'u_pal.sqlite3'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, DB_FILENAME)}"

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True
    WTF_CSRF_ENABLED = False

