from sqlalchemy import Column, TEXT, INTEGER
from flask_restx import fields
from server import db, api

#DB 유저 클래스 세팅
class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(INTEGER, autoincrement=True, primary_key=True)
    name = db.Column(TEXT)
    password = db.Column(TEXT)

userDTO = api.model("User", {
    "id" : fields.Integer,
    "name" : fields.String,
    "password" : fields.String,
})

userInputDTO = api.model("UserInput", {
    "name" : fields.String,
    "password" : fields.String,
})