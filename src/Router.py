from datetime import datetime, timedelta
from http import cookies
import bcrypt
from flask import current_app, jsonify, render_template, request, Blueprint
from flask_jwt_extended import create_access_token, set_access_cookies
from flask_login import login_required, login_user, logout_user, current_user
import jwt
from server import db
from models import Users

blueprint = Blueprint('main', __name__)

def successMessage(message, data = "") :
    return {
        "seccess" : True,
        "message" : message,
        "data" : data
    }
def errorMessage(message, data = "") :
    return {
        "seccess" : False,
        "message" : message,
        "data" : data
    }

@blueprint.route('/home')
def home():
    return render_template('index.html')

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if not request.is_json:
            return errorMessage("json 형식이 아닙니다.", request.data)
        data = request.get_json()
        id = data['id']
        password = data['password']

        remember = True if data['remember'] else False

        user = Users.query.filter_by(id=id, password=password).first()

        if user: #and bcrypt.checkpw(password.encode('UTF-8'), user['hashed_password'].encode('UTF-8')):
            #로그인 정보 세션에 저장
            access_token = create_access_token(identity=id)
            login_user(user, remember=remember)
            resp = jsonify(successMessage("로그인 성공", {"access_token" : access_token}))
            set_access_cookies(resp, access_token)
            return resp, 200
        else:
            return errorMessage("일치하는 유저가 존재하지 않습니다.", data['id'])


@blueprint.route('/logout')
def logout():
    logout_user()
    return "logout"

@blueprint.route('/verify')
def verify():
    return 'verify!'

@blueprint.route('/contents')
@login_required
def contents():
    return successMessage("jwt 인증 성공.", current_user.id)

@blueprint.route('/signup', methods=['POST'])
def signup():
    if not request.is_json:
        return errorMessage("json 형식이 아닙니다.", request.data)

    data = request.get_json()
    id = data['id']
    password = data['password']

    user = Users.query.filter_by(id = id).first()


    if user:
        return errorMessage("중복된 아이디입니다.")

    new_user = Users(id = id, password = password)
    db.session.add(new_user)
    db.session.commit()
    
    return successMessage("회원 가입 성공", new_user.id)

@blueprint.route('/delete/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    user = Users.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return successMessage("회원 삭제 성공", user)

#DB 유저 리스트
@blueprint.route('/list')
def get():
    rows = Users.query.all()
    result = [{
        '_id': row._id,
        'id': row.id,
        'password': row.password
    } for row in rows]
    return successMessage("유저 리스트", result)