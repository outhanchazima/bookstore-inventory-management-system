import datetime
from app.src import db

class Book(db.Model):
    __tablename__ = 'books'

    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(100), nullable=False)
    year_published: datetime = db.Column(db.Datetime, nullable=False)
    isbn_no = db.Column(db.String(100), nullable=False)
    description: str = db.Column(db.String(1000), nullable=False)

    # relatiionship with authors
    author_id: int = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
   