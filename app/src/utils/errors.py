EMAIL_IN_USE = ({'message': 'User with that email already exists'}, 409)
UNAUTHORIZED = (
    {'message': 'Authentication is required to access this resource', 'type': 'UNAUTHORIZED'}, 401)
BAD_CREDENTIALS = (
    {'message': 'Incorrect username or password', 'type': 'BAD_CREDENTIALS'}, 401)
FORBIDDEN = ({'message': 'Access to this resource is forbidden'}, 403)
RESET_PASSWORD_CODE_NOT_VALID = (
    {'message': 'Valid code is required to reset a password'}, 418)
TOO_MANY_REQUESTS = ({'message': 'Too many requests'}, 429)