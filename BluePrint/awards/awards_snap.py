from flask import Blueprint, render_template
from models import reviewstModel, SpotModel, ImgModel
from exts import db
from sqlalchemy import func
from BluePrint.awards import awards_bp

@awards_bp.route('/snap', methods=['GET'])
def snap_awards_page():
    category_id = 5  # NOTE: SNAP CATEGORY

    # Most Instagramable → rank_overall
    Most_Instagrammable = db.session.query(
        SpotModel,
        func.avg(reviewstModel.rank_overall).label('avg_score')
    ).join(reviewstModel, SpotModel.spot_ID == reviewstModel.spot_ID)\
     .filter(SpotModel.category_ID == category_id)\
     .group_by(SpotModel.spot_ID)\
     .order_by(func.avg(reviewstModel.rank_overall).desc())\
     .first()

    # Solo Shoot → least crowdedness
    solo_shoot = db.session.query(
        SpotModel,
        func.avg(reviewstModel.rank_crowdedness).label('avg_crowdedness')
    ).join(reviewstModel, SpotModel.spot_ID == reviewstModel.spot_ID)\
     .filter(SpotModel.category_ID == category_id)\
     .group_by(SpotModel.spot_ID)\
     .order_by(func.avg(reviewstModel.rank_crowdedness).asc())\
     .first()

    # Best Vibe → best atmosphere
    best_vibe = db.session.query(
        SpotModel,
        func.avg(reviewstModel.rank_atmosphere).label('avg_atmosphere')
    ).join(reviewstModel, SpotModel.spot_ID == reviewstModel.spot_ID)\
     .filter(SpotModel.category_ID == category_id)\
     .group_by(SpotModel.spot_ID)\
     .order_by(func.avg(reviewstModel.rank_atmosphere).desc())\
     .first()

    def attach_data(result_tuple, avg_label):
        spot, avg = result_tuple
        image = ImgModel.query.filter_by(spot_ID=spot.spot_ID).first()
        spot.image_path = image.path.replace('static/', '', 1) if image and image.path else 'imgs/Awards/Placeholder.jpg'
        setattr(spot, avg_label, round(avg, 2))
        return spot

    Most_Instagrammable = attach_data(Most_Instagrammable, 'avg_score')
    solo_shoot = attach_data(solo_shoot, 'avg_crowdedness')
    best_vibe = attach_data(best_vibe, 'avg_atmosphere')

    return render_template(
        'awards.html',
        Most_Instagrammable=Most_Instagrammable,
        solo_shoot=solo_shoot,
        best_vibe=best_vibe
    )
