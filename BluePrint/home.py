from flask import Blueprint,render_template

home_bp = Blueprint("Home",__name__,url_prefix="/Home")

@home_bp.route('/')
def home():
    return render_template("Home.html")

