from flask import Blueprint, render_template, request, jsonify,Response
from flask_login import current_user, login_required


from exts import db;
from models import UserModel,relationModel,relationRequestModel;
from datetime import datetime, timedelta

datashare_bp = Blueprint("share",__name__,url_prefix="/profile")

@datashare_bp.route("/profile/<int:userid>")
@login_required
def personal(userid):
    current = UserModel.query.get(current_user.id)


    user = [
        current.username,
        current.profile_path,
        current.wallpaper.path if hasattr(current, 'wallpaper') else "/static/wallpaper/P1040675.webp"
    ]

    # 好友列表（双向匹配）
    friend_relations = relationModel.query.filter(
        ((relationModel.user_id_1 == current.id) | (relationModel.user_id_2 == current.id)),
        relationModel.status == 1
    ).all()

    friend_ids = [
        r.user_id_2 if r.user_id_1 == current.id else r.user_id_1
        for r in friend_relations
    ]

    friend = [
        {
            "name": u.username,
            "path": u.profile_path,
            "uid": str(u.id)
        }
        for u in UserModel.query.filter(UserModel.id.in_(friend_ids)).all()
    ]


    allUsers = [
        {
            "name": u.username,
            "path": u.profile_path,
            "uid": str(u.id)
        }
        for u in UserModel.query.all() if u.id != current.id
    ]


    requests = relationRequestModel.query.filter_by(receiver_id=current.id, status=0).all()
    newrequest = [
        {
            "name": UserModel.query.get(r.sender_id).username,
            "date": r.created_at.strftime('%Y-%m-%d'),
            "message": r.request_text or "please confirm",
            "path": UserModel.query.get(r.sender_id).profile_path
        }
        for r in requests
    ]


    return render_template("datashare.html",
                           user=user,
                           friend=friend,
                           allUsers=allUsers,
                           newrequest=newrequest)

@datashare_bp.route("/enlistfriend/<int:userid>",  methods=["POST"])

def enlist(userid):
    sender_id = current_user.id
    receiver_id = userid
    data = request.get_json()
    message = data.get("message", "Hi, let's be friends!")
    existing = relationRequestModel.query.filter_by(
        sender_id=sender_id,
        receiver_id=receiver_id,
        status=1
    ).first()

    if not existing:
        now = datetime.utcnow()

        new_request = relationRequestModel(
            sender_id=sender_id,
            receiver_id=receiver_id,
            status=1,
            request_text=message,
            created_at=datetime.utcnow(),
            expired_at=now + timedelta(days=7)
        )

        db.session.add(new_request)
        db.session.commit()
    return Response(status=204)

