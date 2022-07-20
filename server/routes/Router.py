from flask import request
from flask_restx import Resource, Namespace, fields
from server import db, api
from ..models import Users, userDTO, userInputDTO

main = Namespace('', description='메인 API')

@main.route('/login/')
class User_login(Resource) :
    @main.expect(userInputDTO)
    @main.response(200, 'Success', userDTO)
    def post(self):
        '''아이디를 입력받아 로그인 처리를 수행합니다.'''
        return {"message" : "login %s" % id}

@main.route('/logout')
class User_logout(Resource) :
    @main.response(200, 'Success', message={"message" : "Success"})
    def get(self):
        '''jwt가 있는 경우 로그아웃 처리를 수행합니다.'''
        return 'logout'

@main.route('/verify')
class User_verify(Resource) :
    def get(self):
        '''jwt가 올바른지 인증을 수행합니다.'''
        return 'verity!'

test_fields = api.model("Test", {"contents" : fields.String(description="test")})
@main.route('/contents')
class Contents(Resource) :
    @main.response(200, 'Success', test_fields)
    def get(self):
        '''jwt가 있을 경우 컨텐츠(유저 정보)를 응답합니다.'''
        return { "test" : "test" }

@main.route('/add')
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

@main.route('/delete/<int:user_id>', methods=['DELETE'])
class handel(Resource):
    def delete(self, user_id):
        user = Users.query.get_or_404(user_id)

        if request.method == 'DELETE':
            db.session.delete(user)
            db.session.commit()

        return {"success" : "success"}

#DB 유저 리스트
@main.route('/list')
class getList(Resource):
    def get(self):
        rows = Users.query.all()
        result = [{
            'id': row.id,
            'name': row.name,
            'password': row.password
        } for row in rows]
        return result