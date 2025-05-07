from flask import Blueprint,render_template

spe_bp = Blueprint("home",__name__,url_prefix="/index")

@spe_bp.route('/')
def index():
    return render_template("specific.html")
