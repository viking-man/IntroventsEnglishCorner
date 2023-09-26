from flask import Blueprint

bp = Blueprint('tts', __name__)

from app.tts import qtts_proxy
