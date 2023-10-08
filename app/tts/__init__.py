from flask import Blueprint

bp = Blueprint('tts', __name__)

from app.tts import gtts_proxy
