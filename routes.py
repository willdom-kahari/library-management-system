# routes.py
from flask import Blueprint, jsonify

from main.book_model import Book
from main.db_init import db
from sqlalchemy import select

routes_bp = Blueprint('routes', __name__)


@routes_bp.route('/')
def index():
    valz = db.paginate(select(Book)).items
    books_list = [{
        'id': book.id,
        'book_id': book.book_id,
        'title': book.title,
        'author': book.author,
        'available': book.available
    } for book in valz]
    return jsonify(books_list)
