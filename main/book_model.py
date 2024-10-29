# main/book_model.py
from dataclasses import dataclass

from .db_init import db

@dataclass
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    available = db.Column(db.Boolean, nullable=False)