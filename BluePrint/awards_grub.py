from flask import Blueprint, jsonify
from models import reviewstModel, SpotModel
from exts import db
from sqlalchemy import func


awards_bp = Blueprint("awards", __name__, url_prefix="/awards")

@awards_bp.route('/best_grub_spot', methods=['GET'])
def best_grub_spot():
    subquery = db.session.query(
        reviewstModel.spot_ID,
        func.avg(reviewstModel.rank_overall).label('avg_score')
    ).join(SpotModel, reviewstModel.spot_ID == SpotModel.spot_ID)\
     .filter(SpotModel.category_ID == 3)\
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


@awards_bp.route('/most_worth_it', methods=['GET'])
def most_worth_it():
    subquery = db.session.query(
        reviewstModel.spot_ID,
        func.avg(reviewstModel.rank_value).label("avg_value")
    ).join(SpotModel, reviewstModel.spot_ID == SpotModel.spot_ID)\
     .filter(SpotModel.category_ID == 3)\
     .group_by(reviewstModel.spot_ID).subquery()

    result = db.session.query(
        SpotModel.spot_ID,
        SpotModel.spot_name,
        subquery.c.avg_price
    ).join(subquery, SpotModel.spot_ID == subquery.c.spot_ID)\
     .order_by(subquery.c.avg_price.desc()).first()

    return jsonify({
        "spot_name": result.spot_name,
        "avg_price": round(result.avg_price, 2)
    })


@awards_bp.route('/best_service', methods=['GET'])
def best_service():
    subquery = db.session.query(
        reviewstModel.spot_ID,
        func.avg(reviewstModel.rank_service_quality).label("avg_service")
    ).join(SpotModel, reviewstModel.spot_ID == SpotModel.spot_ID)\
     .filter(SpotModel.category_ID == 3)\
     .group_by(reviewstModel.spot_ID).subquery()

    result = db.session.query(
        SpotModel.spot_ID,
        SpotModel.spot_name,
        subquery.c.avg_service
    ).join(subquery, SpotModel.spot_ID == subquery.c.spot_ID)\
     .order_by(subquery.c.avg_service.desc()).first()

    return jsonify({
        "spot_name": result.spot_name,
        "avg_service": round(result.avg_service, 2)
    })