from .models import Surverys
from .models import Answers
from flask import Blueprint

survery_bp = Blueprint('survery', __name__)

from . import routes