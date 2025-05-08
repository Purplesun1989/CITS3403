from exts import db

from werkzeug.security import generate_password_hash, check_password_hash

from exts import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

class UserModel(db.Model):
    __tablename__ = 'user_table'
    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username      = db.Column(db.String(80), unique=True, nullable=False)
    uwa_email     = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    age           = db.Column(db.Integer, nullable=False)
    birthday      = db.Column(db.Date, nullable=True)
    gender        = db.Column(db.String(10), nullable=False)
    profile_path  = db.Column(db.String(255),
                              default='static/imgs/Login/Default_user.jfif',
                              server_default='static/imgs/Login/Default_user.jfif')

    @property
    def password(self):
        raise AttributeError("undefined data!!!")

    @password.setter
    def password(self, plaintext):
        self.password_hash = generate_password_hash(plaintext)

    def verify_password(self, plaintext):
        return check_password_hash(self.password_hash, plaintext)

    def __repr__(self):
        return f'<User {self.username}>'

class CategoryModel:

    pass

class SpotModel:
    pass

class ImgModel:
    pass

class commentModel:
    pass

class collectionModel:
    pass

class TendencyModel:
    pass;

class VoteModel:
    pass;