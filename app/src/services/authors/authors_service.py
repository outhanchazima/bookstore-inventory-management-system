from flask import jsonify
from app.src.models.author import Author
from app.src.services import authors
from app.src.utils.base_model import serializerDB
from app.src.utils.logger import Logger
from app.src import db
from typing import Dict, Tuple
import json

logger = Logger().getLogger()

def getAllAuthors()-> Tuple[Dict[str, str], int]:
    authors = db.session.query(Author).all()
    logger.debug(f"Authors from the database {authors}")
    if authors:
        AuthorsList = [{
            "id": author.id,
            "first_name": author.first_name,
            "last_name": author.last_name,
            "date_of_birth": author.date_of_birth.strftime("%d-%b-%Y (%H:%M:%S.%f)"),
            "created_on": author.created_on.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        } for author in authors ]
        logger.debug(f"Authors from the database {authors}")
        responseObject = {
            "status": "success",
            "message": AuthorsList
        }
        return responseObject, 200
    else:
        responseObject ={
            "status": "success",
            "message": []
        }
        return responseObject, 200
  
def saveNewAuthor(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    # Check if author already exists
    author = db.session.query(Author).filter_by(email = data["email"]).first()
    if not author:
        newAuthor = Author(
            first_name = data["first_name"],
            last_name = data["last_name"],
            email = data["email"],
            date_of_birth = data["date_of_birth"]
        )
        db.session.add(newAuthor)
        db.session.commit()

        return {"status":"success","message": "Author created successfully"}, 201
    else:
        return {"status":"fail","message":"An author with that email already exists"}, 409

def getAnAuthor():
    pass