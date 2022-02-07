from datetime import datetime
from app.src import db

class Authors(db.Model):
    __tablename__ = 'authors'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name: str = db.Column(db.String(64), nullable=False)
    last_name: str = db.Column(db.String(64), nullable=False)
    email: str = db.Column(db.String|(50), nullable=False, unique=True)
    date_of_birth: datetime = db.Column(db.DateTime, nullable=True)

    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()

    @classmethod
    def findByAutherID(cls, id: int) -> "Authors":
        return cls.query.filter_by(id=id).first()

    @classmethod 
    def find_by_botname(cls, botname: str) -> "Authors":
        return cls.query.filter_by(botname=botname).first()