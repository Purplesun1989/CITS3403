from flask import Blueprint,render_template,request,jsonify,redirect, url_for,session
from flask_login import login_user
from models import UserModel;
from werkzeug.utils import secure_filename
from exts import db
from datetime import datetime, date
import os

auth_bp = Blueprint("auth",__name__,url_prefix="/auth")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    raw_path = request.args.get("path")
    path = [raw_path] if raw_path else ["/static/profiles/Default_user.jfif"]
    if request.method == "GET":

        return render_template("Login.html",path=path)

    uwa_email = request.form.get('uwa_email', '').strip().lower()
    password = request.form.get('password', '')

    if not uwa_email or not password:
        return render_template("Login.html", error="Missing credentials")

    user = UserModel.query.filter_by(uwa_email=uwa_email).first()

    if user and user.verify_password(password):
        login_user(user)
        return redirect(url_for('Home.home'))
    else:
        return render_template("Login.html", error="Invalid email or password")

@auth_bp.route("/register",methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("Login.html")

    username = request.form.get("register_username").lower()
    email = request.form.get("register_email").lower()
    password = request.form.get("register_password")
    birthday = request.form.get("register_birthday")
    birthday = datetime.strptime(birthday, "%Y-%m-%d").date()
    today = date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    gender = request.form.get("gender")

    avatar_file = request.files.get("avatar")

    if avatar_file:
        filename = secure_filename(avatar_file.filename)
        save_path = os.path.join("static", "profiles", filename)
        avatar_file.save(save_path)
        avatar_url = url_for("static", filename=f"profiles/{filename}")

    # print({
    #     "username": username,
    #     "email": email,
    #     "password": password,
    #     "age": age,
    #     "birthday": birthday,
    #     "gender": gender,
    #     "avatar_url": avatar_url,
    # })

    if not email.endswith("@student.uwa.edu.au"):
        return render_template("Login.html", error="This site is for UWA students only")

    user = UserModel.query.filter_by(uwa_email=email).first()
    if user:
        return render_template("Login.html", error="You have a account already!",path = [user.profile_path])

    user = UserModel(
        username=username,
        uwa_email=email,
        age=int(age) ,
        birthday=birthday,
        gender=gender,
        profile_path=avatar_url
    )
    user.password = password;

    db.session.add(user)
    db.session.commit()

    return redirect(url_for("auth.login",path = avatar_url))



