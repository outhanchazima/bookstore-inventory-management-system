from flask_restx import Resource

from app.src.dto.author import AuthorDto
from app.src.utils.decorators import tokenRequired
from app.src.services.authors.authors_service import saveNewAuthor, getAllAuthors, getAnAuthor

api = AuthorDto.api
author = AuthorDto.author

@api.route('/')
class AuthorResource(Resource):
    @api.doc('List all available authors')
    # @tokenRequired
    @api.marshal_list_with(author, envelope='data')
    def get(self):
        """List all available authors"""
        return getAllAuthors()