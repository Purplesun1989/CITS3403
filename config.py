# config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

DB_FILENAME = 'u_pal.sqlite3'
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, DB_FILENAME)}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
