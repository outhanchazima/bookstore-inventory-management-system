from app.src import db

from app.src.models.blacklist import BlacklistToken
from typing import Dict, Tuple
from app.src.utils.errors import BLACKLIST_FAILED

def save_token(token: str) -> Tuple[Dict[str, str], int]:
    blacklist_token = BlacklistToken(token=token)
    try:
        # insert the token
        db.session.add(blacklist_token)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully logged out.'
        }
        return response_object, 200
    except Exception as e:

        return BLACKLIST_FAILED