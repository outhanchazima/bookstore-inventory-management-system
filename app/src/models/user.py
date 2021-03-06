from app.src import db, flask_bcrypt
import datetime
import jwt
from typing import Union
from app.src.config import Config
from app.src.models.blacklist import BlacklistToken

KEY = Config.SECRET_KEY

class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    public_id = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(100))
    
    def __init__(self, email, registered_on, public_id, username, password) -> None:
        self.email = email
        self.registered_on = registered_on
        self.public_id = public_id
        self.username = username
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')
        

    def checkPassword(self, password: str) -> bool:
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    @staticmethod
    def encodeAuthToken(user_id: int) -> bytes:
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decodeAuthToken(auth_token: str) -> Union[str, int]:
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, KEY)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def __repr__(self):
        return "<User '{}'>".format(self.username)