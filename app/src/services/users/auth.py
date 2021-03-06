from app.src.models.user import User
from app.src.services.users.blacklist import saveToken
from typing import Dict, Tuple
from app.src.utils.errors import UNAUTHORIZED


class Auth:

    @staticmethod
    def loginUser(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            # fetch the user data
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.checkPassword(data.get('password')):
                auth_token = User.encodeAuthToken(user.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logoutUser(data: str) -> Tuple[Dict[str, str], int]:
        """
        this method will logout currently lkogged out user
        """
        if data:
            auth_token = data
        else:
            auth_token = ''
        if auth_token:
            resp = User.decodeAuthToken(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return saveToken(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def getLoggedInUser(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decodeAuthToken(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'admin': user.admin,
                        'registered_on': str(user.registered_on)
                    }
                }
                return response_object, 200
            return UNAUTHORIZED

        else:
            return UNAUTHORIZED
