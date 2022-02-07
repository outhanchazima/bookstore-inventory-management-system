from app.src import db


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
