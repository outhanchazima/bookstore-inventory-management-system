import enum
import datetime

from sqlalchemy import Enum
from app.src import db
from app.src.utils.base_model import BaseModel

class StockStatus(enum.Enum):
    GOOD = 'good'
    BAD = 'bad'
    CRITICAL = 'critical'
    OUTofSTOCK = 'out of stock'

class StockEvent(enum.Enum):
    ADDED = 'added'
    SOLD = 'sold'


class Stocks(db.Model, BaseModel):
    __table_name__ = 'stocks'

    id: int = db.Column(db.Integer, primary_key=True)
    book_id: int = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    items_available: int = db.Column(db.Integer, nullable=False)
    status: str = db.Column(Enum(StockStatus), nullable=False, default=StockStatus.GOOD)
    initialized_on: datetime = db.Column(db.Datetime, nullable=False, default=datetime.datetime.utcnow())
    updated_on: datetime = db.Column(db.Datetime, nullable=False, default=datetime.datetime.utcnow())
    stock_history: list = db.relationship('StockHistory', backref='stocks', lazy=True)

    @classmethod
    def getByBookId(cls, book_id: int) -> 'Stocks':
        return cls.query.filter_by(book_id=book_id).first()
    
    @classmethod
    def getByStatus(cls, status: str) -> 'Stocks':
        return cls.query.filter_by(status=status).all()

class StockHistory(db.Model, BaseModel):
    __table_name__ = 'stock_history'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_id: int = db.Column(db.Integer, db.ForeignKey('stocks.id'), nullable=False)
    stock_event: str = db.Column(Enum(StockEvent), nullable=False)
    quantity: int = db.Column(db.Integer, nullable=False)
    created_on: datetime = db.Column(db.Datetime, nullable=False, default=datetime.datetime.utcnow())

    @classmethod
    def getByStockId(cls, stock_id: int) -> 'StockHistory':
        return cls.query.filter_by(stock_id=stock_id).all()
    
    @classmethod
    def getByStockEvent(cls, stock_event: str) -> 'StockHistory':
        return cls.query.filter_by(stock_event=stock_event).all()

    @classmethod
    def getByStockEventAndStockId(cls, stock_event: str, stock_id: int) -> 'StockHistory':
        return cls.query.filter_by(stock_event=stock_event, stock_id=stock_id).all()