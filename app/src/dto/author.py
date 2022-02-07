from flask_restx import Namespace, fields


class AuthorDto:
    api = Namespace('author', description='user related operations')
    author = api.model('author', {
        'first_name': fields.String(required=True, description='authors first name'),
        'last_name': fields.String(required=True, description='author lastname'),
        'email': fields.String(required=True, description='authors email'),
        'date_of_birth': fields.DateTime(description='user Identifier'),

    })