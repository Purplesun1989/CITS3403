from exts import db

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False) 
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))  # 'Male', 'Female', 'Other'
    birthday = db.Column(db.Date)
    profile_picture = db.Column(db.String(255))  # can store image URL or filepath

class CategoryModel:
### Still need for clarification
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string(80), unique=True, nullable=False)

class SpotModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spot_name = db.Column(db.String(120), nullable=False)
    coordinates = db.Column(db.String(100), nullable=True) 
    num_likes = db.Column(db.Integer, default=0)

class ImgModel:
    id = db.Column(db.Integer, primary_key=True)
    # Foreign key to Spot model
    spot_id = db.Column(db.Integer, db.ForeignKey('spot.id'), nullable=False)

class commentModel:
    id = db.Column(db.Integer, primary_key=True)
    # Foreign key to Spot model 
    spot_id = db.Column(db.Integer, db.ForeignKey('spot.id'), nullable=False)
    # Foreign key to User model 
    student_email = db.Column(db.String(120), db.ForeignKey('users.student_email'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    rank_item1 = db.Column(db.Integer)
    rank_item2 = db.Column(db.Integer)

class collectionModel:
### Still need for clarification
    id = db.Column(db.Integer, primary_key=True)
    # Foreign key to User model 
    student_email = db.Column(db.String(120), db.ForeignKey('users.student_email'), nullable=False)
    items = db.Column(db.String(50), nullable=False)

class TendencyModel:
### Still need for clarification
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    like_increment_1_day_ago = db.Column(db.Integer)
    like_increment_2_day_ago = db.Column(db.Integer)
    like_increment_3_day_ago = db.Column(db.Integer)
    like_increment_4_day_ago = db.Column(db.Integer)
    like_increment_5_day_ago = db.Column(db.Integer)

class VoteModel:
    pass;

