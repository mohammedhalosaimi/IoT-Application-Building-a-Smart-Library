from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json
from flask import current_app as app

api = Blueprint("api", __name__)

db = SQLAlchemy()
ma = Marshmallow()


# Declaring the model.
class Book(db.Model):
    __tablename__ = "Book"
    BookID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ISBN = db.Column(db.Text, nullable=False)
    Title = db.Column(db.Text, nullable=False)
    Author = db.Column(db.Text, nullable=False)
    
    def __init__(self, ISBN, Title, Author, BookID=None):
        self.BookID = BookID
        self.ISBN = ISBN
        self.Title = Title
        self.Author = Author


class BookSchema(ma.Schema):
    # Reference: https://github.com/marshmallow-code/marshmallow/issues/377#issuecomment-261628415
    def __init__(self, strict=True, **kwargs):
        super().__init__(strict=strict, **kwargs)
    
    class Meta:
        # Fields to expose.
        fields = ("BookID", "ISBN", "Title", "Author")

BooksSchema = BookSchema(many=True)
BookSchema = BookSchema()

# Endpoint to show all books
@api.route("/book", methods=["GET"])
def getBooks():
    books = Book.query.all()
    result = BooksSchema.dump(books)

    return jsonify(result.data)

# Endpoint to get a book
@api.route("/book/<id>", methods=["GET"])
def getBook(id):
    person = Book.query.get(id)

    return BookSchema.jsonify(person)

# Endpoint to create a new book
@api.route("/book", methods=["POST"])
def addBook():
    ISBN = request.json["ISBN"]
    Title = request.json["Title"]
    Author = request.json["Author"]

    newBook = Book(ISBN=ISBN, Title=Title, Author=Author)

    db.session.add(newBook)
    db.session.commit()

    return BookSchema.jsonify(newBook)

# Endpoint to update a book
@api.route("/book/<id>", methods=["PUT"])
def personUpdate(id):
    book = Book.query.get(id)
    ISBN = request.json["ISBN"]
    Title = request.json["Title"]
    Author = request.json["Author"]

    book.ISBN = ISBN
    book.Title = Title
    book.Author = Author

    db.session.commit()

    return BookSchema.jsonify(book)

# Endpoint to delete a book
@api.route("/book/<id>", methods=["DELETE"])
def personDelete(id):
    book = Book.query.get(id)

    db.session.delete(book)
    db.session.commit()

    return BookSchema.jsonify(book)
