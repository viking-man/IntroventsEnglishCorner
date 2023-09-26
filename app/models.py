from datetime import datetime
from app import db


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), unique=False, nullable=False)
    chat_id = db.Column(db.String(80), unique=False, nullable=False)
    chat_history = db.Column(db.Text, unique=False, nullable=False)

    # audio_id = db.Column(db.Integer, db.ForeignKey('audio.id'), nullable=True)
    audios = db.relationship('Audio',
                             backref=db.backref('chat', lazy=True))

    def __repr__(self):
        return '<Chat {}>'.format(self.chat_id)


class Audio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'))
    type = db.Column(db.String(10), unique=False, nullable=False)
    audio_data = db.Column(db.LargeBinary, unique=False, nullable=False)
