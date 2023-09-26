from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config.from_object(config_class)

    handler = logging.FileHandler('app.log')  # 日志输出到一个文件
    handler.setLevel(logging.DEBUG)  # 设置日志级别为DEBUG
    app.logger.addHandler(handler)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.open_ai import bp as open_ai_bp
    app.register_blueprint(open_ai_bp)

    from app.tts import bp as tts_bp
    app.register_blueprint(tts_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app


from app import models