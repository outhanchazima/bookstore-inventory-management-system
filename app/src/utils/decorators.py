from functools import wraps

from flask import request

from app.src.services.users.auth import Auth
from app.src.utils.errors import FORBIDDEN
from typing import Callable


def tokenRequired(f) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.getLoggedInUser(request)
        token = data.get('data')

        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated


def adminTokenRequired(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.getLoggedInUser(request)
        token = data.get('data')

        if not token:
            return data, status

        admin = token.get('admin')
        if not admin:
            return FORBIDDEN

        return f(*args, **kwargs)

    return decorated