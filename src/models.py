from sqlalchemy import Column, TEXT, INTEGER
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from server import db

#DB 유저 클래스 세팅
class Users(UserMixin, db.Model):
    __tablename__ = 'users'

    _id = db.Column(INTEGER, autoincrement=True, primary_key=True)
    id = db.Column(TEXT)
    password = db.Column(TEXT)