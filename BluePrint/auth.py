from flask import Blueprint,render_template,request,jsonify,redirect, url_for,session
from flask_login import login_user
from models import UserModel;
from werkzeug.utils import secure_filename
from exts import db
from datetime import datetime, date
from forms import LoginForm, RegisterForm
import os

auth_bp = Blueprint("auth",__name__,url_prefix="/auth")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    register_form = RegisterForm()
    raw_path = request.args.get("path")
    path = [raw_path] if raw_path else ["/static/profiles/Default_user.jfif"]

    if form.validate_on_submit():
        uwa_email = form.uwa_email.data.strip().lower()
        password = form.password.data

        user = UserModel.query.filter_by(uwa_email=uwa_email).first()
        if user and user.verify_password(password):
            login_user(user)
            return redirect(url_for('Home.home'))
        else:
            return render_template("Login.html",
                                   form=form,
                                   register_form=register_form,
                                   path=path,
                                   error="Invalid email or password")

    return render_template("Login.html",
                           form=form,
                           register_form=register_form,
                           path=path)


@auth_bp.route("/register",methods = ["GET", "POST"])

def register():
    register_form = RegisterForm()
    form = LoginForm()  # 登录表单用空白的

    if register_form.validate_on_submit():
        username = register_form.register_username.data.lower()
        email = register_form.register_email.data.lower()
        password = register_form.register_password.data
        birthday = register_form.register_birthday.data
        gender = register_form.gender.data
        avatar_file = register_form.avatar.data

        today = date.today()
        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

        if UserModel.query.filter_by(uwa_email=email).first():
            return render_template("Login.html",
                                   error="You already have an account!",
                                   form=form,
                                   register_form=register_form)

        if UserModel.query.filter_by(username=username).first():
            return render_template(
                "Login.html",
                error="Username already taken!",
                form=LoginForm(),
                register_form=register_form
            )

        avatar_url = "/static/profiles/Default_user.jfif"
        if avatar_file:
            filename = secure_filename(avatar_file.filename)
            save_path = os.path.join("static", "profiles", filename)
            avatar_file.save(save_path)
            avatar_url = url_for("static", filename=f"profiles/{filename}")

        new_user = UserModel(
            username=username,
            uwa_email=email,
            age=age,
            birthday=birthday,
            gender=gender,
            profile_path=avatar_url
        )
        new_user.password = password
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("auth.login", path=avatar_url))

    return render_template("Login.html", form=form, register_form=register_form)
