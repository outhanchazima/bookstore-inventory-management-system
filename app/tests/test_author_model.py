from http.cookies import BaseCookie
from app.src import db
from app.src.models.author import Author
from app.tests.base import BaseTestCase
import datetime

author = {
    "first_name": "test",
    "last_name":"user",
    "email":"test@user.com",
    "date_of_birth": datetime.datetime.utcnow(),
    "created_on": datetime.datetime.utcnow()
}

class TestAuthorModel(BaseTestCase):
    def test_add_author(self):
        bookAuthor = Author(**author)
        db.session.add(bookAuthor)
        db.session.commit()
        self.assertEqual(Author.findByAuthorID(bookAuthor.id).email, "test@user.com")  