from flask import Blueprint, jsonify, request
from models import reviewstModel, SpotModel
from exts import db
from sqlalchemy import func
from BluePrint.awards import awards_bp

@awards_bp.route('/top_reviews_data')
def top_reviews_data():
    from sqlalchemy import func
    category_id = request.args.get('category_id', type=int)
    metric = request.args.get('metric', default='rank_overall')

    allowed = {
        'rank_overall': reviewstModel.rank_overall,
        'rank_noise_level': reviewstModel.rank_noise_level,
        'rank_value': reviewstModel.rank_value,
        'rank_service_quality': reviewstModel.rank_service_quality,
        'rank_atmosphere': reviewstModel.rank_atmosphere,
        'rank_crowdedness': reviewstModel.rank_crowdedness
    }

    if metric not in allowed:
        return jsonify({"error": "Invalid metric"}), 400

    metric_col = allowed[metric]

    results = db.session.query(
        reviewstModel.spot_ID,
        func.avg(metric_col).label("avg_value")
    ).join(SpotModel, reviewstModel.spot_ID == SpotModel.spot_ID)\
     .filter(SpotModel.category_ID == category_id)\
     .group_by(reviewstModel.spot_ID)\
     .order_by(func.avg(metric_col).asc() if metric == "rank_noise_level" else func.avg(metric_col).desc())\
     .limit(5).all()

    data = [
        {
            "name": db.session.query(SpotModel.spot_name).filter_by(spot_ID=row.spot_ID).scalar(),
            "avg": round(row.avg_value, 2)
        }
        for row in results
    ]

    return jsonify(data)
