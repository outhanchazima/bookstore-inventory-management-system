import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from app.src.config import config_by_name


db = SQLAlchemy()
flask_bcrypt = Bcrypt()
migrate = Migrate()


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    CORS(app)
    db.init_app(app)
    flask_bcrypt.init_app(app)
    migrate.init_app(app, db)

    return app


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')