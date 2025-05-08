from flask import Blueprint,render_template,request,jsonify,redirect, url_for,session
from models import UserModel;

auth_bp = Blueprint("auth",__name__,url_prefix="/auth")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("Login.html")

    uwa_email = request.form.get('uwa_email');
    password  = request.form.get('password');

    if not uwa_email or not password:
        return render_template("Login.html", error="Missing credentials")


    user = UserModel.query.filter_by(uwa_email=uwa_email).first()

    if user and user.verify_password:
        session['user_id'] = user.id
        return redirect(url_for('Home.home'))
    else:
        return render_template("Login.html",error="Invalid email or password")


@auth_bp.route("/register",methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("Login.html")




