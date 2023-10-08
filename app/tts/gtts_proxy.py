import os.path

from gtts import gTTS
from app.models import Chat, Audio
import time
from app.type import AudioType
from app import db
from pathlib import Path


def convert_to_audio(user_id, chat_id, text_content, lang):
    # 定时任务清理
    tts = gTTS(text_content, lang=lang)
    audio_filename = str(Path("app/files/output",
                              user_id + "_" + chat_id + "_" + str(int(time.time())) + ".wav").absolute())
    tts.save(audio_filename)

    with open(audio_filename, 'rb') as f:
        audio_data = f.read()

    audio = Audio(chat_id=chat_id, type=AudioType.INPUT.name, audio_data=audio_data)
    db.session.add(audio)
    db.session.commit()

    return audio.id
