from flask import Blueprint, render_template
from models import reviewstModel, SpotModel, ImgModel
from exts import db
from sqlalchemy import func
from BluePrint.awards import awards_bp

@awards_bp.route('/study', methods=['GET'])
def study_awards_page():
    # Best overall study spot
    best_study_spot = db.session.query(
        SpotModel,
        func.avg(reviewstModel.rank_overall).label('avg_score')
    ).join(reviewstModel, SpotModel.spot_ID == reviewstModel.spot_ID)\
     .filter(SpotModel.category_ID == 6)\
     .group_by(SpotModel.spot_ID)\
     .order_by(func.avg(reviewstModel.rank_overall).desc())\
     .first()
    
    # Quietest study spot
    quietest_spot = db.session.query(
        SpotModel,
        func.avg(reviewstModel.rank_noise_level).label('avg_noise')
    ).join(reviewstModel, SpotModel.spot_ID == reviewstModel.spot_ID)\
     .filter(SpotModel.category_ID == 6)\
     .group_by(SpotModel.spot_ID)\
     .order_by(func.avg(reviewstModel.rank_noise_level).asc())\
     .first()

    # Best vibes (atmosphere)
    best_vibes = db.session.query(
        SpotModel,
        func.avg(reviewstModel.rank_atmosphere).label('avg_atmosphere')
    ).join(reviewstModel, SpotModel.spot_ID == reviewstModel.spot_ID)\
     .filter(SpotModel.category_ID == 6)\
     .group_by(SpotModel.spot_ID)\
     .order_by(func.avg(reviewstModel.rank_atmosphere).desc())\
     .first()
    
    # Attach images and values
    def attach_data(result_tuple, avg_label):
        spot, avg = result_tuple

        image = ImgModel.query.filter_by(spot_ID=spot.spot_ID).first()
        if image and image.path:
            # Remove leading "static/" so url_for doesn't double it
            relative_path = image.path.replace('static/', '', 1)
            spot.image_path = relative_path
        else:
            spot.image_path = 'imgs/Awards/Placeholder.jpg'

        setattr(spot, avg_label, round(avg, 2))
        return spot

    best_study_spot = attach_data(best_study_spot, 'avg_score')
    quietest_spot = attach_data(quietest_spot, 'avg_noise')
    best_vibes = attach_data(best_vibes, 'avg_atmosphere')

    return render_template(
        'awards.html',
        best_study_spot=best_study_spot,
        quietest_spot=quietest_spot,
        best_vibes=best_vibes
    )