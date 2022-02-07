import datetime
from app.src import db
from app.src.utils.base_model import BaseModel

class Book(db.Model, BaseModel):
    __tablename__ = 'books'

    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(100), nullable=False)
    year_published: datetime = db.Column(db.Datetime, nullable=False)
    isbn_no = db.Column(db.String(100), nullable=False)
    description: str = db.Column(db.String(1000), nullable=False)
    created_on: datetime = db.Column(db.Datetime, nullable=False, default=datetime.datetime.utcnow())

    # relatiionship with authors
    author_id: int = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    @classmethod
    def getByBookId(cls, book_id: int) -> 'Book':
        return cls.query.filter_by(id=book_id).first()

    @classmethod
    def getByAuthorId(cls, author_id: int) -> 'Book':
        return cls.query.filter_by(author_id=author_id).all()
    
    @classmethod
    def getByYearPublished(cls, year_published: int) -> 'Book':
        return cls.query.filter_by(year_published>=year_published).all()