import os.path

from flask import Flask, render_template, request, jsonify, send_file
from app.open_ai import chatgpt_proxy
from app.tts import gtts_proxy
from app.models import Audio
from app.open_ai import whisper_proxy
from app.main import bp
import io
import time
from app import create_app
from pathlib import Path

app = create_app()


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')


@bp.route('/text_chat', methods=['POST'])
def text_chat():  # put application's code here
    print(str(request))
    # 获取参数
    user_message = request.form['user_message']
    user_id = request.form['user_id']
    chat_id = request.form['chat_id']
    if chat_id is None or chat_id == 'undefined' or len(chat_id) == 0:
        chat_id = str(abs(hash(user_message)))
    gpt_version = request.form['gpt_version']

    # chatgpt请求
    ai_message, chat_history = chatgpt_proxy.text_chat(user_message, user_id, chat_id, gpt_version)

    # tts转成语音
    audio_id = gtts_proxy.convert_to_audio(user_id, chat_id, ai_message, "en")

    # 返回信息
    return jsonify({
        'ai_message': ai_message,
        'chat_history': chat_history,
        'audio_id': audio_id,
        'chat_id': chat_id
    })


@bp.route('/get_audio', methods=['POST'])
def receive_audio():
    audio_id = request.form['audio_id']
    audio = Audio.query.get_or_404(audio_id)

    return send_file(
        io.BytesIO(audio.audio_data),
        mimetype="audio/wav"  # 设置适当的MIME类型
    )


@bp.route('/speech_chat', methods=['POST'])
def speech_chat():
    print(str(request))
    user_id = request.form.get('user_id')
    chat_id = request.form.get('chat_id')
    gpt_version = request.form.get('gpt_version')

    audio_file = request.files['audio']
    # Save the audio file (optional)
    audio_path = str(
        Path("app/files/input", user_id + "_" + chat_id + "_" + str(time.time()) + ".wav").absolute())
    audio_file.save(audio_path)

    chat_text = whisper_proxy.transcribe_to_text(audio_path)

    if chat_id is None or chat_id == 'undefined' or len(chat_id) == 0:
        chat_id = str(abs(hash(chat_text)))

    # chatgpt请求
    ai_message, chat_history = chatgpt_proxy.text_chat(chat_text, user_id, chat_id, gpt_version)

    # tts转成语音
    audio_id = gtts_proxy.convert_to_audio(user_id, chat_id, ai_message, "en")

    return jsonify({
        'user_message': chat_text,
        'ai_message': ai_message,
        'audio_id': audio_id,
        'chat_id': chat_id})


@bp.route('/clear_history', methods=['POST'])
def clear_history():
    data = request.get_json()
    userid = data.get('userId')
    print(data)
    return jsonify({'message': 'History cleared successfully'})

# @bp.before_request
# def log_request_info():
#     app.logger.debug('Headers: %s', request.headers)
#     app.logger.debug('Body: %s', request.get_data())
#
#
# @bp.after_request
# def log_response_info(response):
#     app.logger.debug('Headers: %s', response.headers)
#     app.logger.debug('Body: %s', response.get_data())
#     return response
