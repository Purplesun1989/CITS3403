from flask import Blueprint, jsonify
from models import reviewstModel, SpotModel
from exts import db
from sqlalchemy import func

awards_bp = Blueprint("awards", __name__, url_prefix="/awards")

@awards_bp.route('/best_study_spot', methods=['GET'])
# Finding the study spot with the highest score
def best_study_spot():
    subquery = db.session.query(
        reviewstModel.spot_ID,
        func.avg(reviewstModel.rank_overall).label('avg_score')
    ).join(SpotModel, reviewstModel.spot_ID == SpotModel.spot_ID)\
     .filter(SpotModel.category_ID == 6)\
     .group_by(reviewstModel.spot_ID).subquery()

    result = db.session.query(
        SpotModel.spot_ID,
        SpotModel.spot_name,
        subquery.c.avg_score
    ).join(subquery, SpotModel.spot_ID == subquery.c.spot_ID)\
     .order_by(subquery.c.avg_score.desc())\
     .first()

    return jsonify({
        "spot_name": result.spot_name,
        "avg_score": round(result.avg_score, 2)
    })

@awards_bp.route('/quietest_study_spot', methods=['GET'])
# Finding the study spot with the quietest environment
def quietest_spot():
    subquery = db.session.query(
        reviewstModel.spot_ID,
        func.avg(reviewstModel.rank_noise_level).label("avg_noise")
    ).join(SpotModel, reviewstModel.spot_ID == SpotModel.spot_ID)\
     .filter(SpotModel.category_ID == 6)\
     .group_by(reviewstModel.spot_ID).subquery()

    result = db.session.query(
        SpotModel.spot_ID,
        SpotModel.spot_name,
        subquery.c.avg_noise
    ).join(subquery, SpotModel.spot_ID == subquery.c.spot_ID)\
     .order_by(subquery.c.avg_noise.asc()).first()

    return jsonify({
        "spot_name": result.spot_name,
        "avg_noise": round(result.avg_noise, 2)
    })

@awards_bp.route('/best_vibes', methods=['GET'])
def best_vibes():
    subquery = db.session.query(
        reviewstModel.spot_ID,
        func.avg(reviewstModel.rank_atmosphere).label("avg_atmosphere")
    ).join(SpotModel, reviewstModel.spot_ID == SpotModel.spot_ID)\
     .filter(SpotModel.category_ID == 6)\
     .group_by(reviewstModel.spot_ID).subquery()

    result = db.session.query(
        SpotModel.spot_ID,
        SpotModel.spot_name,
        subquery.c.avg_atmosphere
    ).join(subquery, SpotModel.spot_ID == subquery.c.spot_ID)\
     .order_by(subquery.c.avg_atmosphere.desc()).first()

    return jsonify({
        "spot_name": result.spot_name,
        "avg_vibes": round(result.avg_atmosphere, 2)
    })