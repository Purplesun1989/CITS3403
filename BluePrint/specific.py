from flask import Blueprint,render_template,request,jsonify,Response
from flask_login import current_user, login_required
from sqlalchemy import func

from exts import db;
from models import reviewstModel, SpotModel, ImgModel, collectionModel, UserModel;
from datetime import datetime


spe_bp = Blueprint("spe",__name__,url_prefix="/index")

@spe_bp.route('/<int:spot_id>')
@login_required
def specific(spot_id):
    # 1. 获取 spot 及其随机图片
    spot = SpotModel.query.get(spot_id)
    images = (
        ImgModel.query
        .filter_by(spot_ID=spot_id)
        .order_by(func.random())
        .limit(6)
        .all()
    )
    img_paths = [img.path for img in images]
    while len(img_paths) < 6:
        img_paths.append("/static/imgs/nomore.jfif")

    metainfo = [
        current_user.username,
        spot_id,
        current_user.profile_path,
        "1",
        img_paths[0], img_paths[1], img_paths[2],
        img_paths[3], img_paths[4], img_paths[5],
        spot.spot_name,
        spot.locationx,
        spot.locationy,
        spot.num_likes,
        spot.description
    ]

    # 2. 生成当前用户的收藏列表
    liked_entries = collectionModel.query.filter_by(user_id=current_user.id).all()
    likeData = []
    for entry in liked_entries:
        s = SpotModel.query.get(entry.item_ID)
        if not s:
            continue
        first_img = (
            ImgModel.query
            .filter_by(spot_ID=s.spot_ID)
            .order_by(ImgModel.img_ID)
            .first()
        )
        likeData.append({
            'name': s.spot_name,
            'path': first_img.path if first_img else '',
            'likes': s.num_likes or 0,
            'spotid': s.spot_ID
        })

    # 3. 拉取评论并格式化
    reviews = reviewstModel.query.filter_by(spot_ID=spot_id).all()
    commentsection = []
    for r in reviews:
        user = UserModel.query.get(r.user_id)
        date_str = r.created_at.strftime('%B %d, %Y').replace(' 0', ' ')
        commentsection.append({
            'author': user.username if user else 'Unknown',
            'date': date_str,
            'comment': r.text,
            'rating': r.rank_overall,
            'spotid': r.spot_ID
        })

    # 4. 计算各维度平均评分
    metrics = [
        ("Cleanliness",    "Dirty",        "Spotless",   "rank_cleanliness"),
        ("Atmosphere",     "Unpleasant",   "Welcoming",  "rank_atmosphere"),
        ("Comfort",        "Uncomfortable","Cozy",       "rank_comfort"),
        ("Accessibility",  "Inconvenient", "Convenient", "rank_accessibility"),
        ("Value",          "Overpriced",   "Worth It",   "rank_value"),
        ("service_quality","Rude",  "Gentle",   "rank_service_quality"),
        ("noise_level",    "unbearable",  "Quiet",   "rank_noise_level"),
        ("Crowdedness",    "Too Crowded",  "Spacious",   "rank_crowdedness"),
        ("visit_frequency","Rarely",       "Often",      "rank_visitfrequency"),
    ]
    ratingsData = []
    for name, left_label, right_label, field in metrics:
        vals = [getattr(r, field) for r in reviews if getattr(r, field) is not None]
        avg = int(round(sum(vals) / len(vals))) if vals else 0
        ratingsData.append({
            'name':  name,
            'left':  left_label,
            'right': right_label,
            'score': avg
        })
    # 生成charts数据
    liked_entries = collectionModel.query.filter_by(item_ID=spot_id).all()
    user_ids = [e.user_id for e in liked_entries]


    age_counts = {'12-18': 0, '18-25': 0, '25+': 0}
    users = UserModel.query.filter(UserModel.id.in_(user_ids)).all()
    for u in users:
        age = u.age
        if 12 <= age <= 18:
            age_counts['12-18'] += 1
        elif 19 <= age <= 25:
            age_counts['18-25'] += 1
        else:
            age_counts['25+']  += 1


    gender_counts = {'male': 0, 'female': 0, 'none binary': 0}
    for u in users:
        g = u.gender.lower()
        if g == 'male':
            gender_counts['male'] += 1
        elif g == 'female':
            gender_counts['female'] += 1
        else:
            gender_counts['none binary'] += 1


    visit_counts = {'1': 0, '<3': 0, '3+': 0}
    reviews = (reviewstModel.query
               .filter_by(spot_ID=spot_id)
               .filter(reviewstModel.user_id.in_(user_ids))
               .all())
    for r in reviews:
        v = r.rank_visitfrequency or 0
        if v == 1:
            visit_counts['1']  += 1
        elif v < 3:
            visit_counts['<3'] += 1
        else:
            visit_counts['3+'] += 1


    charts = [
        {
            'id': 'pie1',
            'title': 'Agepalooza',
            'data': [
                {'value': age_counts['12-18'], 'name': '12-18'},
                {'value': age_counts['18-25'], 'name': '18-25'},
                {'value': age_counts['25+'],  'name': '25+'}
            ]
        },
        {
            'id': 'pie2',
            'title': 'Genderpalooza',
            'data': [
                {'value': gender_counts['male'],        'name': 'male'},
                {'value': gender_counts['female'],      'name': 'female'},
                {'value': gender_counts['none binary'], 'name': 'none binary'}
            ]
        },
        {
            'id': 'pie3',
            'title': 'WeekiVisits',
            'data': [
                {'value': visit_counts['1'],  'name': '1'},
                {'value': visit_counts['<3'],'name': '<3'},
                {'value': visit_counts['3+'],'name': '3+'}
            ]
        }
    ]
    # 渲染模板
    return render_template(
        "specific.html",
        metainfo=metainfo,
        likeData=likeData,
        commentsection=commentsection,
        ratingsData=ratingsData,
        charts = charts
    )

@spe_bp.route('/like/<int:spot_id>')
def like(spot_id):
    exsitlike = db.session.query(collectionModel).filter_by(
        user_id=current_user.id,
        item_ID=spot_id
    ).first()

    if not exsitlike:
        new_like = collectionModel(user_id=current_user.id, item_ID=spot_id)
        db.session.add(new_like)
        db.session.commit()

        spot = SpotModel.query.get(spot_id)
        if spot:
            spot.num_likes = (spot.num_likes or 0) + 1
            db.session.commit()
        else:
            db.session.rollback()

    return Response(status=204)

@spe_bp.route('/dislike/<int:spot_id>')
def dislike(spot_id):

    everliked = db.session.query(collectionModel).filter_by(
        user_id=current_user.id,
        item_ID=spot_id
    ).first()

    if everliked :
        db.session.delete(everliked)
        spot = SpotModel.query.get(spot_id)
        if spot:
            spot.num_likes = max((spot.num_likes or 0) - 1, 0)
            db.session.commit()
        else:
            db.session.rollback()
    return Response(status=204)

@spe_bp.route('/insert_review/<int:spot_id>',methods= ["POST"])
def insert_review(spot_id):

    cleanliness = request.form.get('cleanliness')
    atmosphere = request.form.get('atmosphere')
    comfort = request.form.get('comfort')
    accessibility = request.form.get('accessibility')
    value = request.form.get('value')
    service_quality = request.form.get('service_quality')
    noise_level =  request.form.get('noise_level')
    crowdedness = request.form.get('crowdedness')
    visit_frequency = request.form.get('visit_frequency')
    comment = request.form.get('comment')

    scores = {
        "cleanliness": cleanliness,
        "atmosphere": atmosphere,
        "comfort": comfort,
        "accessibility": accessibility,
        "value": value,
        "service_quality": service_quality,
        "noise_level": noise_level,
        "crowdedness": crowdedness
    }


    category_weights = {
        1: {  # Chill
            "cleanliness": 0.05, "atmosphere": 0.25, "comfort": 0.25, "accessibility": 0.05,
            "value": 0.05, "service_quality": 0.05, "noise_level": 0.15, "crowdedness": 0.15
        },
        2: {  # Fun
            "cleanliness": 0.05, "atmosphere": 0.2, "comfort": 0.1, "accessibility": 0.15,
            "value": 0.1, "service_quality": 0.2, "noise_level": 0.1, "crowdedness": 0.1
        },
        3: {  # Grub
            "cleanliness": 0.15, "atmosphere": 0.05, "comfort": 0.2, "accessibility": 0.05,
            "value": 0.25, "service_quality": 0.25, "noise_level": 0.025, "crowdedness": 0.025
        },
        4: {  # Shop
            "cleanliness": 0.05, "atmosphere": 0.1, "comfort": 0.1, "accessibility": 0.2,
            "value": 0.3, "service_quality": 0.2, "noise_level": 0.05, "crowdedness": 0.05
        },
        5: {  # Snap
            "cleanliness": 0.15, "atmosphere": 0.3, "comfort": 0.05, "accessibility": 0.05,
            "value": 0.05, "service_quality": 0.05, "noise_level": 0.2, "crowdedness": 0.15
        },
        6: {  # Study
            "cleanliness": 0.1, "atmosphere": 0.1, "comfort": 0.25, "accessibility": 0.15,
            "value": 0.05, "service_quality": 0.05, "noise_level": 0.2, "crowdedness": 0.1
        },
    }

    spot = SpotModel.query.get(spot_id)

    weights = category_weights.get(spot.category_ID)

    overall = 0

    for key, weight in weights.items():
        val = float(scores.get(key, 0))
        overall += val * weight

    overall= round(overall)

    review = reviewstModel(
        spot_ID=int(spot_id),
        user_id=int(current_user.id),
        text=comment,
        rank_cleanliness=int(cleanliness),
        rank_atmosphere=int(atmosphere),
        rank_comfort=int(comfort),

        rank_accessibility=int(accessibility),
        rank_value=int(value),
        rank_service_quality=int(service_quality),

        rank_noise_level=int(noise_level),
        rank_crowdedness = int(crowdedness),

        rank_visitfrequency = int(visit_frequency),

        rank_overall=overall,
        created_at=datetime.utcnow(),

    )

    existing_review = db.session.query(reviewstModel).filter_by(
        user_id=current_user.id,
        spot_ID=spot_id
    ).first()

    if existing_review:
        db.session.delete(existing_review)


    db.session.add(review)
    db.session.commit()

    return Response(status=204)

