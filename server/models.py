from sqlalchemy import Column, TEXT, INTEGER
from server import db

#DB 유저 클래스 세팅
class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(INTEGER, autoincrement=True, primary_key=True)
    name = db.Column(TEXT)
    password = db.Column(TEXT)