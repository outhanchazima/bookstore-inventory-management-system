from app.src import db

class BaseModel(db.Model):
    _abstract__ = True

    @classmethod
    def save(cls, **kw):
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()

    # TODO: should not delete from the database
    @classmethod
    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()
