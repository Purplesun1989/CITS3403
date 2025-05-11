from flask import Flask
from exts import db
from flask_migrate import Migrate
from flask_login import LoginManager
from models import UserModel  # 关键：导入 UserModel，才能用于 user_loader

from BluePrint.auth import auth_bp
from BluePrint.home import home_bp
from BluePrint.specific import spe_bp
from BluePrint.datashare import datashare_bp

import config

app = Flask(__name__)
app.config.from_object(config)

# 初始化数据库
db.init_app(app)
migrate = Migrate(app, db)


login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))

# 注册蓝图
app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)
app.register_blueprint(spe_bp)
app.register_blueprint(datashare_bp)

@app.route('/', methods=["POST", "GET"])
def hello_world():
    return "this is a test"

if __name__ == '__main__':
    app.run()
