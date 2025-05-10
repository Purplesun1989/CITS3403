from flask import Blueprint,render_template,request
from flask_login import current_user
from exts import db;
from models import reviewstModel;
import datetime


spe_bp = Blueprint("home",__name__,url_prefix="/index")

@spe_bp.route('/')
def specifc():
    return render_template("specific.html")
@spe_bp.route('/<int:spot_id>')
def test(spot_id):
    return str(spot_id)

@spe_bp.route('/insert_review')
def insert_review():
    comment = request.form.get('comment')
    cleanliness = request.form.get('cleanliness')
    atmosphere = request.form.get('atmosphere')
    comfort = request.form.get('comfort')
    spot_id = request.form.get('spot_id')

    review = reviewstModel(
        spot_ID=int(spot_id),
        user_id=current_user.id,
        text=comment,
        rank_cleanliness=int(cleanliness),
        rank_atmosphere=int(atmosphere),
        rank_comfort=int(comfort),
        rank_overall=(int(cleanliness) + int(atmosphere) + int(comfort)) // 3,  # 可选计算
        created_at=datetime.utcnow()
    )

    existing_review = db.session.query(reviewstModel).filter_by(
        user_id=current_user.id,
        spot_ID=spot_id
    ).first()

    if existing_review:
        db.session.delete(existing_review)


    db.session.query()
    # 3. 插入数据库
    # db.session.add(review)
    # db.session.commit()

    return f"comment={comment}, cleanliness={cleanliness}, atmosphere={atmosphere}, comfort={comfort}"


