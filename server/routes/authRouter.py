from flask import request
from flask_restx import Resource, Namespace
from server import db
from ..models import Users

auth = Namespace('', description='인증 API')

@auth.route('/login/<string:name>')
class User_login(Resource) :
    def get(self, name):
        return {"message" : "login %s" % name}

@auth.route('/logout')
class User_logout(Resource) :
    def get(self):
        return 'logout'

@auth.route('/verify')
class User_verify(Resource) :
    def get(self):
        return 'verity!'

#DB 유저 리스트
@auth.route('/list')
class getList(Resource):
    def get(self):
        rows = Users.query.all()
        result = [{
            'id': row.id,
            'name': row.name,
            'password': row.password
        } for row in rows]
        return result

@auth.route('/add')
class Add(Resource):
    def post(res):
        if request.is_json:
            data = request.get_json()
            name = data['name']
            password = data['password']

            new_user = Users(name=name, password=password)
            db.session.add(new_user)
            db.session.commit()
            
            return {"message": f"user {new_user} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

@auth.route('/delete/<user_id>', methods=['DELETE'])
class handel(Resource):
    def delete(user_id):
        user = Users.query.get_or_404(user_id)

        if request.method == 'DELETE':
            db.session.delete(user)
            db.session.commit()

        return {"success" : "success"}
