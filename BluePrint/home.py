from flask import Blueprint, render_template, request, session, jsonify
from flask_login import current_user
from sqlalchemy import func
import random
from collections import defaultdict
from exts import db;
from models import relationRequestModel, UserModel, SpotModel, LikeModel, ImgModel, TendencyModel, collectionModel;
from datetime import date, datetime, timedelta

home_bp = Blueprint("Home",__name__,)

@home_bp.route('/')
def home():
    # 获取点赞数前五的地点
    top5_query = db.session.query(
        SpotModel.spot_name,
        SpotModel.num_likes,
        SpotModel.spot_ID,
        SpotModel.locationx,
        SpotModel.locationy
    ).order_by(SpotModel.num_likes.desc()) \
        .limit(5).all()

    top5 = [
        {
            "spot": name,
            "value": likes,
            "id": spot_id,
            "lat": lat,
            "lon": lon
        }
        for name, likes, spot_id, lat, lon in top5_query
    ]


    # 获取点赞数前六名的地点以及图片
    top_spots = (
        db.session.query(SpotModel)
        .order_by(SpotModel.num_likes.desc())
        .limit(6)
        .all()
    )

    #趋势图
    # # 获取最近五天的日期
    today = date.today()
    days = [today - timedelta(days=i) for i in range(4, -1, -1)]  # 从5天前到今天（升序）

    # 查询最近五天所有点赞记录
    records = (
        db.session.query(TendencyModel.category_ID, TendencyModel.snapshot_date, TendencyModel.like_count)
        .filter(TendencyModel.snapshot_date.in_(days))
        .all()
    )

    # 初始化：{category_ID: [0, 0, 0, 0, 0]}
    category_like_map = defaultdict(lambda: [0, 0, 0, 0, 0])

    # # 填充数据
    day_index = {d: i for i, d in enumerate(days)}
    for cid, date_, count in records:
        idx = day_index.get(date_)
        if idx is not None:
            category_like_map[cid][idx] = count

    # # 查询过去五天内的数据
    records = (
        db.session.query(TendencyModel.category_ID, TendencyModel.snapshot_date, TendencyModel.like_count)
        .filter(TendencyModel.snapshot_date.in_(days))
        .all()
    )
    #
    # # 构建二维映射：category_ID -> date -> like_count
    data_map = defaultdict(lambda: {d: 0 for d in days})  # 默认每个日期都初始化为0

    for cid, snapshot_date, count in records:
        data_map[cid][snapshot_date] = count

    # 按 category_ID 排序输出二维数组
    sorted_ids = sorted(data_map.keys())
    tendency = [ [data_map[cid][d] for d in days] for cid in sorted_ids ]

    # 查找每个景点的第一张图片
    top6 = []
    for spot in top_spots:
        first_img = (
            db.session.query(ImgModel.path)
            .filter_by(spot_ID=spot.spot_ID)
            .order_by(ImgModel.img_ID.asc())
            .first()
        )
        if first_img:
            top6.append({
                "name": spot.spot_name,
                "path": first_img.path,
                "likes": spot.num_likes
            })


    default = ["Stranger","0" ,'/static/profiles/Default_user.jfif', "true"];

    if not current_user.is_authenticated:
        return render_template("Home.html",top5=top5,top6=top6, metainfo = default, tendency = tendency)

    current = UserModel.query.get(current_user.id)
    exists = relationRequestModel.query.filter_by(receiver_id=current_user.id).first() is not None
    userinfo = [current_user.username, current_user.id, current_user.profile_path, str(exists).lower()]





    return render_template("Home.html",top5=top5,top6=top6, user=current,metainfo = userinfo,tendency = tendency)

@home_bp.route('/index/get_liked_data')
def get_recommend_data():
    num = random.randint(15, 25)
    spots = SpotModel.query.order_by(func.random()).limit(num).all()
    recommond = []

    for spot in spots:
        images = ImgModel.query.filter_by(spot_ID=spot.spot_ID).all()
        selected_image = random.choice(images).path if images else None

        recommond.append({
            "id": spot.spot_ID,
            "name": spot.spot_name,
            "locationx": spot.locationx,
            "locationy": spot.locationy,
            "path": selected_image
        })

    return jsonify(recommond)

@home_bp.route('/index/search',methods = ["POST"])
def search():
    data = request.get_json()
    input_value = data.get('inputValue')
    search_term = input_value.replace(" ", "_")
    match = SpotModel.query.filter(SpotModel.spot_name.contains(search_term)).first()
    if match:
        return jsonify({'spot_id': match.spot_ID})
    else:
        return jsonify({'spot_id': None})