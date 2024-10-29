# main/library_init.py
from flask import Flask
from routes import routes_bp
from .db_init import db


def library_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
    db.init_app(app)
    app.register_blueprint(routes_bp)
    return app
