from flask import Blueprint

bp = Blueprint('open_ai', __name__)

from app.open_ai import chatgpt_proxy, whisper_proxy, gpt_prompt, whisper_model
