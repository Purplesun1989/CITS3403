from flask import Flask
from exts import db
from models import UserModel;
from BluePrint.auth import auth_bp;
from BluePrint.home import home_bp;
from BluePrint.specific import spe_bp;


import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)
app.register_blueprint(spe_bp)

@app.route('/')
def hello_world():
    return "this is a test"

if __name__ == '__main__':
    app.run()
