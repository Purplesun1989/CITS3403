from flask import Blueprint

awards_bp = Blueprint("awards", __name__, url_prefix="/awards")
from . import awards_snap
from . import awards_fun