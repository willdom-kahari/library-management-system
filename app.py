# app.py
import main.book_model as book_model
import os
import json
from main.library_init import library_app
from main.db_init import db


def __preload_books():
    default_books = os.getcwd() + "/main/books_def.json"
    with open(default_books, 'r') as file:
        data = json.load(file)
        default_books = []
        for book in data:
            current_book = book_model.Book()
            current_book.book_id = book['book_id']
            current_book.title = book['title']
            current_book.author = book['author']
            current_book.available = book['available']
            default_books.append(current_book)
        return default_books


with library_app().app_context():
    db.create_all()
    books = __preload_books()
    db.session.add_all(books)
    db.session.commit()

if __name__ == "__main__":
    library_app().run(debug=True)
