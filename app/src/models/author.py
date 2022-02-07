from datetime import datetime
from app.src import db

class Author(db.Model):
    __tablename__ = 'author'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name: str = db.Column(db.String(64), nullable=False)
    last_name: str = db.Column(db.String(64), nullable=False)
    email: str = db.Column(db.String(50), nullable=False, unique=True)
    date_of_birth: datetime = db.Column(db.DateTime, nullable=True)
    created_on: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    
    # one to many with Books table 
    book = db.relationship('Book', backref='author', lazy=True)

    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()

    @classmethod
    def findByAuthorID(cls, id: int) -> "Author":
        return cls.query.filter_by(id=id).first()