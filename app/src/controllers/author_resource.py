from flask import request
from flask_restx import Resource

from app.src.dto.author import AuthorDto
from app.src.utils.decorators import tokenRequired
from app.src.services.authors.authors_service import saveNewAuthor, getAllAuthors, getAnAuthor
from typing import Dict, Tuple

api = AuthorDto.api
author = AuthorDto.author

@api.route('/')
class AuthorResource(Resource):
    @api.doc('List all available authors')
    # @tokenRequired
    def get(self):
        """List all available authors"""
        return getAllAuthors()

    @api.expect(author, validate=True)
    @api.response(201, 'Author successfully created.')
    # @tokenRequired
    @api.marshal_with(author)
    def post(self) -> Tuple[Dict[str, str], int]:
        """Create a new author"""
        data = request.json
        return saveNewAuthor(data)