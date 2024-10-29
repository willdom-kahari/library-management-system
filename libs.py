# # Import necessary modules and packages
# import json # work with json data
# import datetime # work with dates
# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask
#
# # prepare database for invocation and default state
# def initialise_db(app):
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
#     db = SQLAlchemy(app)
#
#
#
#
#     with app.app_context():
#         db.create_all()
#
#     return db
#
#
#
# """ Add a single book. The cursor execute method allows to run queries to the database.
# It allows parameterized queries and accepts tuples as the parameter.
# Calling the execute method opens a transaction and only persists the data if the connection commits.
# """
# # def add_book(single_book):
# #     cur.execute("""INSERT INTO books(book_id, title, author, available) VALUES (?,?,?,?)""", single_book )
# #     conn.commit()
# #
# #
# # # checks if the book title is present in the database and prints the book details
# # def search_book(title):
# #     title = title.title()
# #     # Search for books in the library that match the given title (case-insensitive)
# #     cur.execute("SELECT * FROM books WHERE title = ?", (title,))
# #     found_books = cur.fetchall()
# #
# #     if found_books:
# #         # Iterate through the found books and print their details
# #         for book in found_books:
# #             status = "Available" if book[-3] else "Borrowed"
# #
# #             print(
# #                 f"ID: {book[1]}, Title: {book[2]}, "
# #                 f"Author: {book[3]}, Status: {status}"
# #             )
# #
# #     else:
# #         print(f"No books with the title '{title}' have been found.")
# #
# #
# # # If a book is borrowed, its status is set to unavailable
# # def borrow_book(user, book_id):
# #     # Check if the specified book is available and mark it as borrowed
# #     cur.execute("SELECT * FROM books WHERE book_id = ? AND available = ?", (book_id.upper(), True))
# #     found_books = cur.fetchall()
# #     for book in found_books:
# #         if book[1] == book_id and book[-3]:
# #             cur.execute("UPDATE books SET available = ?, borrower = ?, borrowed_date= ? WHERE id = ?", (False, user, datetime.date.today().strftime("%d-%m-%Y"),book[0]))
# #             conn.commit()
# #
# #             print(f"Book '{book[2]}' borrowed by {user}.")
# #             return
# #
# #     print("Book not available or does not exist.")
# #
# #
# # # Returning a book changes its status to available
# # def return_book(book_id):
# #     # Check if the book is in borrowed_books and mark it as available
# #     cur.execute("SELECT * FROM books WHERE book_id = ? AND available = ?", (book_id, False))
# #     borrowed_books = cur.fetchall()
# #     for book in borrowed_books:
# #         if book[1] == book_id:
# #             cur.execute("UPDATE books SET available = ?, borrower = ?, borrowed_date = ?  WHERE id = ?", (True,"","", book[0]))
# #             conn.commit()
# #
# #             print(f"Book '{book[2]}' returned.")
# #             return
# #
# #     print("Book not found in borrowed books.")
# #
# #
# # # To avoid memory leaks all connections must be closed
# # def close_db():
# #     print("Closing database cursor ...")
# #     cur.close()
# #     print("Database cursor closed")
# #     print("Closing database connection ...")
# #     conn.close()
# #     print("Database connection closed")
# #
# #
# # # Read a list of books from json and adds them to the database during initialisation
# def __preload_books():
#     with open('books_def.json', 'r') as file:
#         data = json.load(file)
#         books = []
#         for book in data:
#
#             books.append((book["book_id"], book["title"].title(), book["author"].title(), book["available"]))
#
#         return books
# #
# #
# # # The execute many method allows to save a list of books  as tuples at once in the database
# # def __add_books(books):
# #     cur.executemany("""INSERT INTO books(book_id, title, author, available) VALUES (?,?,?,?)""", books)
# #     conn.commit()