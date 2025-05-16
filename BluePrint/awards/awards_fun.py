from flask import Blueprint, render_template
from models import reviewstModel, SpotModel, ImgModel
from exts import db
from sqlalchemy import func
from BluePrint.awards import awards_bp

@awards_bp.route('/fun', methods=['GET'])
def fun_awards_page():
    category_id = 2  

    # Best Reviews → rank_overall
    best_reviews = db.session.query(
        SpotModel,
        func.avg(reviewstModel.rank_overall).label('avg_score')
    ).join(reviewstModel, SpotModel.spot_ID == reviewstModel.spot_ID)\
     .filter(SpotModel.category_ID == category_id)\
     .group_by(SpotModel.spot_ID)\
     .order_by(func.avg(reviewstModel.rank_overall).desc())\
     .first()

    # Most Welcoming → best atmosphere
    most_welcoming = db.session.query(
        SpotModel,
        func.avg(reviewstModel.rank_atmosphere).label('avg_atmosphere')
    ).join(reviewstModel, SpotModel.spot_ID == reviewstModel.spot_ID)\
     .filter(SpotModel.category_ID == category_id)\
     .group_by(SpotModel.spot_ID)\
     .order_by(func.avg(reviewstModel.rank_atmosphere).desc())\
     .first()

    # Worth it! → highest value
    worth_it = db.session.query(
        SpotModel,
        func.avg(reviewstModel.rank_value).label('avg_value')
    ).join(reviewstModel, SpotModel.spot_ID == reviewstModel.spot_ID)\
     .filter(SpotModel.category_ID == category_id)\
     .group_by(SpotModel.spot_ID)\
     .order_by(func.avg(reviewstModel.rank_value).desc())\
     .first()

    def attach_data(result_tuple, avg_label):
        spot, avg = result_tuple
        image = ImgModel.query.filter_by(spot_ID=spot.spot_ID).first()
        spot.image_path = image.path.replace('static/', '', 1) if image and image.path else 'imgs/Awards/Placeholder.jpg'
        setattr(spot, avg_label, round(avg, 2))
        return spot

    best_reviews = attach_data(best_reviews, 'avg_score')
    most_welcoming = attach_data(most_welcoming, 'avg_atmosphere')
    worth_it = attach_data(worth_it, 'avg_value')

    return render_template(
        'awards.html',
        best_reviews=best_reviews,
        most_welcoming=most_welcoming,
        worth_it=worth_it
    )
