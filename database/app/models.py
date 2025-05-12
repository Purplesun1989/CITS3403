from app import db
from datetime import date, datetime

class UserModel(db.Model):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    uwa_email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    birthday = db.Column(db.Date, nullable=True)
    gender = db.Column(db.String(10), nullable=False)

class CategoryModel(db.Model):
    __tablename__ = 'category_table'
    category_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), unique=True)
    total_likes = db.Column(db.Integer)

class SpotModel(db.Model):
    __tablename__ = 'spot_table'
    spot_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    spot_name =db. Column(db.String(50))
    category_ID =db. Column(db.Integer,db. ForeignKey('category_table.category_ID', name="fk_category_id")) #added the name because it would not let me update 
    locationx =db. Column(db.Float)#removed the 100 it was causing an error 
    locationy = db.Column(db.Float)
    description =db. Column(db.Text)
    num_likes =db. Column(db.Integer)

    category = db.relationship('CategoryModel', backref='spots') # added a relationship for marks 
    reviews = db.relationship('ReviewModel', backref='spot', lazy=True)
    images = db.relationship('ImgModel', backref='spot', lazy=True)

class ImgModel(db.Model):
    __tablename__ = 'image_table'
    img_ID =db. Column(db.Integer, primary_key=True, autoincrement=True)
    path = db.Column(db.String(255))
    spot_ID = db.Column(db.Integer,db. ForeignKey('spot_table.spot_ID'))


class ReviewModel(db.Model): #fixed the typo 
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

    rank_overall = db.Column(db.Integer)

    user = db.relationship('UserModel', backref='reviews', lazy=True)
