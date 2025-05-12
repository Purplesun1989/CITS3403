from flask import Blueprint, render_template, request, jsonify,Response
from flask_login import current_user, login_required
from sqlalchemy import or_,and_
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
        current.wallpaper.path if hasattr(current, 'wallpaper') else "/static/wallpaper/P1040675.webp",
        current.id
    ]


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


    requests = relationRequestModel.query.filter_by(receiver_id=current.id, status=1).all()
    newrequest = [
        {
            "name": UserModel.query.get(r.sender_id).username,
            "date": r.created_at.strftime('%Y-%m-%d'),
            "message": r.request_text or "please confirm",
            "path": UserModel.query.get(r.sender_id).profile_path,
            "uid": str(r.sender_id),
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

@datashare_bp.route("/confirm/<int:userid>",  methods=["POST","GET"])

def confirmrequest(userid):
    sender_id = userid
    receiver_id = current_user.id

    request_row = relationRequestModel.query.filter_by(
        sender_id=sender_id,
        receiver_id=receiver_id,

        status=1
    ).first()

    if request_row:

        db.session.delete(request_row)

        new_relation = relationModel(
            user_id_1=sender_id,
            user_id_2=receiver_id,
            status=1
        )
        db.session.add(new_relation)
        db.session.commit()

    relations = relationModel.query.filter(
        or_(
            relationModel.user_id_1 == current_user.id,
            relationModel.user_id_2 == current_user.id
        ),
        relationModel.status == 1
    ).all()

    friends = []
    for rel in relations:

        friend_id = rel.user_id_2 if rel.user_id_1 == current_user.id else rel.user_id_1
        user = UserModel.query.get(friend_id)
        if not user:
            continue
        friends.append({
            "uid":    user.id,
            "name":   user.username,
            "path":   user.profile_path
        })
    print(friends)
    return jsonify(friends)

@datashare_bp.route("/decline/<int:userid>",  methods=["GET"])

def declinerequest(userid):

    request_row = relationRequestModel.query.filter(
        and_(
            relationRequestModel.sender_id == userid,
            relationRequestModel.receiver_id == current_user.id,
            relationRequestModel.status == 1
        )
    ).first()

    if not request_row:

        return Response(status=404)


    db.session.delete(request_row)
    db.session.commit()

    return Response(status=204)
