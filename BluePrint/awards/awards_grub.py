from flask import Blueprint, render_template
from models import reviewstModel, SpotModel, ImgModel
from exts import db
from sqlalchemy import func
from BluePrint.awards import awards_bp

@awards_bp.route('/grub')
def grub_awards_page():
    # Best overall grub spot
    best_grub_spot = db.session.query(
        SpotModel,
        func.avg(reviewstModel.rank_overall).label('avg_score')
    ).join(reviewstModel, SpotModel.spot_ID == reviewstModel.spot_ID)\
     .filter(SpotModel.category_ID == 3)\
     .group_by(SpotModel.spot_ID)\
     .order_by(func.avg(reviewstModel.rank_overall).desc())\
     .first()

    # Most worth it
    most_worth_it = db.session.query(
        SpotModel,
        func.avg(reviewstModel.rank_value).label('avg_value')
    ).join(reviewstModel, SpotModel.spot_ID == reviewstModel.spot_ID)\
     .filter(SpotModel.category_ID == 3)\
     .group_by(SpotModel.spot_ID)\
     .order_by(func.avg(reviewstModel.rank_value).desc())\
     .first()

    # Best service
    best_service = db.session.query(
        SpotModel,
        func.avg(reviewstModel.rank_service_quality).label('avg_service')
    ).join(reviewstModel, SpotModel.spot_ID == reviewstModel.spot_ID)\
     .filter(SpotModel.category_ID == 3)\
     .group_by(SpotModel.spot_ID)\
     .order_by(func.avg(reviewstModel.rank_service_quality).desc())\
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

    best_grub_spot = attach_data(best_grub_spot, 'avg_score')
    most_worth_it = attach_data(most_worth_it, 'avg_value')
    best_service = attach_data(best_service, 'avg_service')

    return render_template(
        'awards.html',
        best_grub_spot=best_grub_spot,
        most_worth_it=most_worth_it,
        best_service=best_service
    )