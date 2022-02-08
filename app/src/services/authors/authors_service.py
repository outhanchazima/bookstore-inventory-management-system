from flask import jsonify
from app.src.models.author import Author
from app.src.utils.base_model import serializerDB
from app.src.utils.logger import Logger

logger = Logger().getLogger()

def getAllAuthors():
    try:
        authors = Author.getAllAuthors()
    except Exception as e:
        return {"status": "fail", "message":str(e)}, 400
    logger.debug(f"Authors from the database {authors}")
    if authors:
        AuthorsList = serializerDB(jsonify(authors))
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
  
def saveNewAuthor():
    pass

def getAnAuthor():
    pass