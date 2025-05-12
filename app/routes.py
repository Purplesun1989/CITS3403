from flask import render_template
from sqlalchemy import func
from app import application, db
from app.models import SpotModel, ReviewModel, Winner

def get_top_spot_by_metric(category_id, metric_column, ascending=False):
    query = (
        db.session.query(SpotModel.spot_name, func.avg(getattr(ReviewModel, metric_column)).label('avg_metric'))
        .join(ReviewModel)
        .filter(SpotModel.category_ID == category_id)
        .group_by(SpotModel.spot_ID)
    )
    query = query.order_by(func.avg(getattr(ReviewModel, metric_column)).asc() if ascending else func.avg(getattr(ReviewModel, metric_column)).desc())
    return query.first()

@application.route('/')
def index():
    # Snap category (ID 3)
    snap_best_reviews = get_top_spot_by_metric(3, 'rank_overall')
    snap_solo_shoot = get_top_spot_by_metric(3, 'rank_crowdedness', ascending=True)
    snap_best_vibe = get_top_spot_by_metric(3, 'rank_atmosphere')

    # Fun category (ID 4)
    fun_best_reviews = get_top_spot_by_metric(4, 'rank_overall')
    fun_worth_it = get_top_spot_by_metric(4, 'rank_value')
    fun_most_welcoming = get_top_spot_by_metric(4, 'rank_atmosphere')

    snap_winners = [
        Winner(spots=snap_best_reviews[0] if snap_best_reviews else "N/A"),
        Winner(spots=snap_solo_shoot[0] if snap_solo_shoot else "N/A"),
        Winner(spots=snap_best_vibe[0] if snap_best_vibe else "N/A"),
    ]
    fun_winners = [
        Winner(spots=fun_best_reviews[0] if fun_best_reviews else "N/A"),
        Winner(spots=fun_worth_it[0] if fun_worth_it else "N/A"),
        Winner(spots=fun_most_welcoming[0] if fun_most_welcoming else "N/A"),
    ]

    snap_award_names = ['Best Reviews', 'Solo Shoot', 'Best Vibe']
    fun_award_names = ['Best Reviews', 'Worth it!' , 'Most Welcoming']

    snap_zipped_winners = zip(snap_winners, snap_award_names)
    fun_zipped_winners = zip(fun_winners, fun_award_names)

    return render_template('Awardspage-current.html',
                           fun_zipped_winners=fun_zipped_winners,
                           snap_zipped_winners=snap_zipped_winners)
