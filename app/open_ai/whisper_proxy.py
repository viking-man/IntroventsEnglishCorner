from whisper import audio
from app.open_ai.whisper_model import WhisperModel
from app.models import Chat, Audio


def transcribe_to_text(audio_path):
    load_audio = audio.load_audio(audio_path)
    whisper_model = WhisperModel()
    whisper_model.load_model()
    transcribe_result = whisper_model.transcribe(load_audio, None)
    print(f'Transcribe result->{str(transcribe_result)}')

    chat_text = ""
    segments_ = transcribe_result['segments']
    for segment in segments_:
        chat_text = chat_text + segment['text'] + ","
    chat_text = chat_text[:-1]

    return chat_text
