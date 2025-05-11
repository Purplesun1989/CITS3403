from exts import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime



class UserModel(db.Model,UserMixin):
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

class CategoryModel(db.Model):
    __tablename__ = 'category_table'
    category_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), unique=True)
    total_likes = db.Column(db.Integer)

class SpotModel(db.Model):
    __tablename__ = 'spot_table'
    spot_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    spot_name =db. Column(db.String(50))
    category_ID =db. Column(db.Integer,db. ForeignKey('category_table.category_ID'))
    locationx =db. Column(db.Float(100))
    locationy = db.Column(db.Float(100))
    description =db. Column(db.Text)
    num_likes =db. Column(db.Integer)


class ImgModel(db.Model):
    __tablename__ = 'image_table'
    img_ID =db. Column(db.Integer, primary_key=True, autoincrement=True)
    path = db.Column(db.String(255))
    spot_ID = db.Column(db.Integer,db. ForeignKey('spot_table.spot_ID'))


class reviewstModel(db.Model):
    __tablename__ = 'reviews_table'
    review_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    spot_ID =db. Column(db.Integer, db.ForeignKey('spot_table.spot_ID'))
    user_id =db. Column(db.Integer, db.ForeignKey('user_table.id'))
    text =db. Column(db.Text)

    rank_cleanliness = db.Column(db.Integer)
    rank_atmosphere = db.Column(db.Integer)
    rank_comfort = db.Column(db.Integer)
    rank_accessibility = db.Column(db.Integer)
    rank_value = db.Column(db.Integer)
    rank_service_quality = db.Column(db.Integer)
    rank_noise_level = db.Column(db.Integer)
    rank_crowdedness = db.Column(db.Integer)

    rank_visitfrequency = db.Column(db.Integer)
    rank_overall = db.Column(db.Integer)

    created_at =db. Column(db.DateTime, default=datetime.utcnow)


class collectionModel(db.Model):
    __tablename__ = 'collection_table'

    user_id = db.Column(db.Integer,db. ForeignKey('user_table.id'), primary_key=True)
    item_ID =db. Column(db.Integer, db.ForeignKey('spot_table.spot_ID'),primary_key=True)


class TendencyModel(db.Model):
    __tablename__ = 'tendency_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_ID = db.Column(db.Integer, db.ForeignKey('category_table.category_ID'), nullable=False)
    snapshot_date = db.Column(db.Date, nullable=False)
    like_count = db.Column(db.Integer, nullable=False, default=0)
    __table_args__ = (
        db.UniqueConstraint('category_ID', 'snapshot_date', name='uq_category_date'),
        db.Index('idx_category_date', 'category_ID', 'snapshot_date')
    )


class LikeModel(db.Model):
    __tablename__ = 'like_table'
    user_id =db. Column(db.Integer,db. ForeignKey('user_table.id'), primary_key=True)
    spot_ID =db. Column(db.Integer, db.ForeignKey('spot_table.spot_ID'), primary_key=True)


class relationRequestModel(db.Model):
    __tablename__ = 'relation_requests'
    sender_id = db.Column(db.Integer, db.ForeignKey('user_table.id'), nullable=False, primary_key=True)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user_table.id'), nullable=False, primary_key=True)
    status = db.Column(db.Integer)
    request_text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expired_at = db.Column(db.DateTime)

    __table_args__ = (
        db.UniqueConstraint('sender_id', 'receiver_id', name='uq_friend_request'),
    )


class relationModel(db.Model):
    __tablename__ = 'relationships_Table'
    user_id_1 = db.Column(db.Integer, db.ForeignKey('user_table.id'), nullable=False,primary_key=True)
    user_id_2 = db.Column(db.Integer, db.ForeignKey('user_table.id'), nullable=False,primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Integer)  # 可选：'active', 'blocked'

    __table_args__ = (
        db.UniqueConstraint('user_id_1', 'user_id_2', name='uq_friendship'),
    )

class WallpaperModel(db.Model):
    __tablename__ = 'wallpaper_table'
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'), primary_key=True)
    path = db.Column(db.String(255), nullable=False)  # 建议加非空限制


