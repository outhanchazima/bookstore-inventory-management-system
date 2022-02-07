from app.src import db
import json


class BaseModel():

    _abstract__ = True

    @classmethod
    def save(cls, **kw):
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()

    # TODO: should not delete from the database
    @classmethod
    def delete(cls) -> None:
        db.session.delete(cls)
        db.session.commit()


def serializerDB(jsonify_resp):
    """
    Takes the jsonify results and dumps to json
    """
    items = []
    if len(jsonify_resp.response) > 1:
        for item in jsonify_resp.response:
            result = json.loads(item)
            items.append(result)
    else:
        items = json.loads(jsonify_resp.response[0])
    return json.dumps(items)