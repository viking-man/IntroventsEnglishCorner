import os.path

from gtts import gTTS
from app.models import Chat, Audio
import time
from app.type import AudioType
from app import db
from pathlib import Path
import re, sys


def convert_to_audio(user_id, chat_id, text_content, lang):
    # 定时任务清理
    tts = gTTS(text_content, lang=lang)
    audio_filename = str(Path("app/files/output",
                              user_id + "_" + chat_id + "_" + str(int(time.time())) + ".wav").absolute())
    audio_filename = deal_windows_path(audio_filename)
    tts.save(audio_filename)

    with open(audio_filename, 'rb') as f:
        audio_data = f.read()

    audio = Audio(chat_id=chat_id, type=AudioType.INPUT.name, audio_data=audio_data)
    db.session.add(audio)
    db.session.commit()

    return audio.id


def escape_windows_path(path):
    # 将单个反斜杠替换为双反斜杠
    sub = re.sub(r'\\', r'\\\\', path)
    sub = "\'" + sub + "\'"
    split = sub.split(":")
    if len(split) == 2:
        return split[0] + "\\" + ":" + split[1]

    return sub


def deal_windows_path(path):
    if is_windows():
        path = escape_windows_path(path)
    return path


def is_windows():
    return sys.platform.startswith('win')
