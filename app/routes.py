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
    return query.first()  # Returns (spot_name, avg_metric)

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

    # Study category (ID 1)
    study_best_reviews = get_top_spot_by_metric(1, 'rank_overall')
    study_quietest = get_top_spot_by_metric(1, 'rank_noise_level', ascending=True)
    study_comfiest = get_top_spot_by_metric(1, 'rank_comfort')

    # Grub category (ID 2)
    grub_best_reviews = get_top_spot_by_metric(2, 'rank_overall')
    grub_best_value = get_top_spot_by_metric(2, 'rank_value')
    grub_best_service = get_top_spot_by_metric(2, 'rank_service_quality')

    # Chill category (ID 5)
    chill_best_reviews = get_top_spot_by_metric(5, 'rank_overall')
    chill_coziest = get_top_spot_by_metric(5, 'rank_comfort')
    chill_least_crowded = get_top_spot_by_metric(5, 'rank_crowdedness', ascending=True)

    # Shop category (ID 6)
    shop_best_reviews = get_top_spot_by_metric(6, 'rank_overall')
    shop_most_accessible = get_top_spot_by_metric(6, 'rank_accessibility')
    shop_cleanest = get_top_spot_by_metric(6, 'rank_cleanliness')

    # Build winners lists (include both spot name and score)
    snap_winners = [
        Winner(spots=snap_best_reviews[0] if snap_best_reviews else "N/A", score=round(snap_best_reviews[1], 1) if snap_best_reviews else "N/A"),
        Winner(spots=snap_solo_shoot[0] if snap_solo_shoot else "N/A", score=round(snap_solo_shoot[1], 1) if snap_solo_shoot else "N/A"),
        Winner(spots=snap_best_vibe[0] if snap_best_vibe else "N/A", score=round(snap_best_vibe[1], 1) if snap_best_vibe else "N/A"),
    ]
    fun_winners = [
        Winner(spots=fun_best_reviews[0] if fun_best_reviews else "N/A", score=round(fun_best_reviews[1], 1) if fun_best_reviews else "N/A"),
        Winner(spots=fun_worth_it[0] if fun_worth_it else "N/A", score=round(fun_worth_it[1], 1) if fun_worth_it else "N/A"),
        Winner(spots=fun_most_welcoming[0] if fun_most_welcoming else "N/A", score=round(fun_most_welcoming[1], 1) if fun_most_welcoming else "N/A"),
    ]
    study_winners = [
        Winner(spots=study_best_reviews[0] if study_best_reviews else "N/A", score=round(study_best_reviews[1], 1) if study_best_reviews else "N/A"),
        Winner(spots=study_quietest[0] if study_quietest else "N/A", score=round(study_quietest[1], 1) if study_quietest else "N/A"),
        Winner(spots=study_comfiest[0] if study_comfiest else "N/A", score=round(study_comfiest[1], 1) if study_comfiest else "N/A"),
    ]
    grub_winners = [
        Winner(spots=grub_best_reviews[0] if grub_best_reviews else "N/A", score=round(grub_best_reviews[1], 1) if grub_best_reviews else "N/A"),
        Winner(spots=grub_best_value[0] if grub_best_value else "N/A", score=round(grub_best_value[1], 1) if grub_best_value else "N/A"),
        Winner(spots=grub_best_service[0] if grub_best_service else "N/A", score=round(grub_best_service[1], 1) if grub_best_service else "N/A"),
    ]
    chill_winners = [
        Winner(spots=chill_best_reviews[0] if chill_best_reviews else "N/A", score=round(chill_best_reviews[1], 1) if chill_best_reviews else "N/A"),
        Winner(spots=chill_coziest[0] if chill_coziest else "N/A", score=round(chill_coziest[1], 1) if chill_coziest else "N/A"),
        Winner(spots=chill_least_crowded[0] if chill_least_crowded else "N/A", score=round(chill_least_crowded[1], 1) if chill_least_crowded else "N/A"),
    ]
    shop_winners = [
        Winner(spots=shop_best_reviews[0] if shop_best_reviews else "N/A", score=round(shop_best_reviews[1], 1) if shop_best_reviews else "N/A"),
        Winner(spots=shop_most_accessible[0] if shop_most_accessible else "N/A", score=round(shop_most_accessible[1], 1) if shop_most_accessible else "N/A"),
        Winner(spots=shop_cleanest[0] if shop_cleanest else "N/A", score=round(shop_cleanest[1], 1) if shop_cleanest else "N/A"),
    ]

    # Award names
    snap_award_names = ['Best Reviews', 'Solo Shoot', 'Best Vibe']
    fun_award_names = ['Best Reviews', 'Worth it!', 'Most Welcoming']
    study_award_names = ['Best Reviews', 'Quietest Spot', 'Most Comfy']
    grub_award_names = ['Best Reviews', 'Worth it!', 'Great Service']
    chill_award_names = ['Best Reviews', 'Coziest Hangout', 'Hidden Gem']
    shop_award_names = ['Best Reviews', 'Most Accessable', 'Cleanest']

    return render_template(
        'Awardspage-current.html',
        snap_zipped_winners=zip(snap_winners, snap_award_names),
        fun_zipped_winners=zip(fun_winners, fun_award_names),
        study_zipped_winners=zip(study_winners, study_award_names),
        grub_zipped_winners=zip(grub_winners, grub_award_names),
        chill_zipped_winners=zip(chill_winners, chill_award_names),
        shop_zipped_winners=zip(shop_winners, shop_award_names),
    )
