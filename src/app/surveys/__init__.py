from flask import Blueprint

survery_bp = Blueprint('survery', __name__)

from . import routes