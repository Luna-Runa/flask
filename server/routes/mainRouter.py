from flask_restx import Resource, Namespace
from ..models import Users
from server import blueprint

main = Namespace('', description='인증 API')

@blueprint.route('/home')
def helloo():
    return "hello"

@main.route('/')
class mp(Resource) :
    def get(self):
        return {"message" : "hello?"}

@main.route('/contents')
class Contents(Resource) :
    def get(self):
        return { "test" : "test" }