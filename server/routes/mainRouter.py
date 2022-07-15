from flask import request
from flask_restx import Resource, Namespace
from server import api, db
from ..models import Users

main = Namespace('', description='인증 API')

@main.route('/')
class mp(Resource) :
    def get():
        return {"message" : "hello?"}

@main.route('/contents')
class Contents(Resource) :
    def get(self):
        return { "test" : "test" }