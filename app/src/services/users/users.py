import uuid
import datetime

from app.src import db
from app.src.models.user import User
from app.src.utils.errors import EMAIL_IN_USE, ERROR_OCCURED
from typing import Dict, Tuple


def saveNewUser(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        User.save(new_user)
        return generateToken(new_user)
    else:
        return EMAIL_IN_USE


def getAllUsers():
    return User.query.all()


def getAUser(public_id):
    return User.query.filter_by(public_id=public_id).first()


def generateToken(user: User) -> Tuple[Dict[str, str], int]:
    try:
        # generate the auth token
        authToken = User.encodeAuthToken(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': authToken.decode()
        }
        return response_object, 201
    except Exception as e:
        return ERROR_OCCURED