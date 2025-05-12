import os 

basedir = os.path.abspath(os.path.dirname(__file__))
default_database_path = 'sqlite:///'+os.path.join(basedir, 'app.db')

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or default_database_path
